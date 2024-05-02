import os
import pandas as pd
import glob
import spacy
import re
from tqdm import tqdm



""" Counts the POS tags for a doc """
def count_pos(doc):
    nouns_count = 0
    for token in doc:
        if token.pos_ == "NOUN":
            nouns_count += 1

    verbs_count = 0
    for token in doc:
        if token.pos_ == "VERB":
            verbs_count += 1

    adverbs_count = 0
    for token in doc:
        if token.pos_ == "ADV":
            adverbs_count += 1

    adjectives_count = 0
    for token in doc:
        if token.pos_ == "ADJ":
            adjectives_count += 1

    return nouns_count, verbs_count, adverbs_count, adjectives_count



""" Calculates the relative frquency pr. 10000 words """
def rel_freq(count, len_doc): 

    return round((count/len_doc * 10000), 2)



""" Gets the unique no entities for a doc by extracting all entities, deleting duplicates. Entites of interest is defined and counted """
def unique_NE(doc):
    enteties = []

    for e in doc.ents: 
        enteties.append((e.text, e.label_))
        
    ents_pd = pd.DataFrame(enteties, columns=["ent", "label"])
    ents_pd = ents_pd.drop_duplicates()
    unique_counts = ents_pd.value_counts(subset = "label")
        
    unique_labels = ['PERSON', 'LOC', 'ORG']
    unique_row = []
    
    for label in unique_labels:
        if label in (unique_counts.index): 
            unique_row.append(unique_counts[label]) 
        else:
            unique_row.append(0)

    return unique_row



""" Saves a csv named after the current subfolder """
def save_csv(out_df, text_row, subfolder):
    out_df.loc[len(out_df)] = text_row
    csv_filename = f"out/{subfolder}_data.csv"
    out_df.to_csv(csv_filename, index=False)



def loop_extract_save(filepath, nlp):
    '''
    Loops over all 14 subfolders and all files within each subfolder
    '''
    for subfolder in tqdm (sorted(os.listdir(filepath)), desc='Looping over folders'):
        subfolder_path = os.path.join(filepath, subfolder)
        """ Empty dataframe for holding data """
        
        out_df = pd.DataFrame(columns=("Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADV",
                                        "RelFreq ADJ", "No. Unique PER", "No. Unique LOC", "No. Unique ORG"))

        for file in sorted (glob.glob((os.path.join(subfolder_path, "*.txt")))):
            if os.path.isfile(file): 
                with open(file, "r", encoding = "latin-1") as f:
                    text = re.sub(r"<*?>", "", f.read()) 
                    doc = nlp(text)           
                '''
                Calculate the counts, relative frequency per 10,000 words and Number of unique entities
                '''
                nouns_count, verbs_count, adverbs_count, adjectives_count = count_pos(doc)

                len_doc = len(doc)
                nouns_relative_freq = rel_freq(nouns_count, len_doc)
                verbs_relative_freq = rel_freq(verbs_count, len_doc)
                adverbs_relative_freq = rel_freq(adverbs_count, len_doc)
                adjectives_relative_freq = rel_freq(adjectives_count, len_doc)

                No_unique_per, No_unique_loc, No_unique_org = unique_NE(doc)
                
                """ All calculations are saves in text_row """
                text_name = file.split("/")[-1]
                text_row = [text_name, nouns_relative_freq, verbs_relative_freq, adverbs_relative_freq, adjectives_relative_freq,
                    No_unique_per, No_unique_loc, No_unique_org]

                save_csv(out_df, text_row, subfolder)
                
    

def main(): 
    nlp = spacy.load("en_core_web_md")
    filepath = os.path.join("in", "USEcorpus")
    loop_extract_save(filepath,nlp)

    

if __name__ == "__main__":
    main()