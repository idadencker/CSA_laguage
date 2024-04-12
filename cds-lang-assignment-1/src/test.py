import os
import glob
import re
import pandas as pd
import spacy

def process_text_file(file_path, nlp):
    '''
    Process a single text file and extract relevant information.
    '''
    with open(file_path, "r", encoding="latin-1") as f:
        text = f.read()
        text = re.sub(r"<*?>", "", text)
        doc = nlp(text)

        nouns_count = sum(1 for token in doc if token.pos_ == "NOUN")
        verbs_count = sum(1 for token in doc if token.pos_ == "VERB")
        adverb_count = sum(1 for token in doc if token.pos_ == "ADV")
        adjective_count = sum(1 for token in doc if token.pos_ == "ADJ")

        nouns_relative_freq = round((nouns_count / len(doc)) * 10000, 2)
        verbs_relative_freq = round((verbs_count / len(doc)) * 10000, 2)
        adverb_relative_freq = round((adverb_count / len(doc)) * 10000, 2)
        adjective_relative_freq = round((adjective_count / len(doc)) * 10000, 2)

        unique_per_count, unique_loc_count, unique_org_count = unique_named_entities(doc)

        return {
            "Filename": os.path.basename(file_path),
            "Nouns_Relative_Freq": nouns_relative_freq,
            "Verbs_Relative_Freq": verbs_relative_freq,
            "Adverbs_Relative_Freq": adverb_relative_freq,
            "Adjectives_Relative_Freq": adjective_relative_freq,
            "No_unique_per": unique_per_count,
            "No_unique_loc": unique_loc_count,
            "No_unique_org": unique_org_count
        }

def unique_named_entities(doc):
    '''
    Extract unique named entities from a SpaCy doc.
    '''
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    entities_df = pd.DataFrame(entities, columns=["ent", "label"]).drop_duplicates()
    unique_counts = entities_df.value_counts(subset="label")
    unique_labels = ['PERSON', 'LOC', 'ORG']
    unique_row = [unique_counts[label] if label in unique_counts.index else 0 for label in unique_labels]
    return unique_row

def process_subfolder(subfolder_path, nlp):
    '''
    Process all text files in a subfolder.
    '''
    data = []
    for file in glob.glob(os.path.join(subfolder_path, "*.txt")):
        if os.path.isfile(file):
            data.append(process_text_file(file, nlp))
    return data

def loop_extract_save(filepath, nlp):
    '''
    Loops over all 14 subfolders and processes each text file.
    '''
    for subfolder in sorted(os.listdir(filepath)):
        subfolder_path = os.path.join(filepath, subfolder)
        if os.path.isdir(subfolder_path):
            data = process_subfolder(subfolder_path, nlp)
            df = pd.DataFrame(data)
            df = df.sort_values("Filename")
            csv_filename = f"out/{subfolder}_data.csv"
            df.to_csv(csv_filename, index=False)

def main():
    nlp = spacy.load("en_core_web_md")
    filepath = os.path.join("in", "USEcorpus")
    loop_extract_save(filepath, nlp)

if __name__ == "__main__":
    main()
