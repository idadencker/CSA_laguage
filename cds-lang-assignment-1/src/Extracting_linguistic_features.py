import os
import pandas as pd
import glob
import spacy
import re

def loop_extract_save(filepath, nlp):
    '''
    Loops over all 14 subfolders
    '''
    for subfolder in sorted(os.listdir(filepath)):
        subfolder_path = os.path.join(filepath, subfolder)

        if os.path.isdir(subfolder_path):
 
            filenames = []
            nouns_freq = []
            verbs_freq = []
            adverbs_freq = []
            adjectives_freq = []
            no_unique_per = []
            no_unique_org = []
            no_unique_loc = []

        
        '''
        Loop over each text file in the subfolder
        '''
            for file in glob.glob(os.path.join(subfolder_path, "*.txt")):
                if os.path.isfile(file): 
                    with open(file, "r", encoding = "latin-1") as f:
                        text = f.read() 
                        text = re.sub(r"<*?>", "", text) 
                        '''
                        Creates spacy doc and count number of each POS
                        '''
                        doc = nlp(text) 

                        nouns_count = 0
                        for token in doc:
                            if token.pos_ == "NOUN":
                                nouns_count += 1

                        verbs_count = 0
                        for token in doc:
                            if token.pos_ == "VERB":
                                verbs_count += 1

                        adverb_count = 0
                        for token in doc:
                            if token.pos_ == "ADV":
                                adverb_count += 1

                        adjective_count = 0
                        for token in doc:
                            if token.pos_ == "ADJ":
                                adjective_count += 1
                    
                        '''
                        Calculate the relative frequency per 10,000 words
                        '''
                        nouns_relative_freq = round(((nouns_count/len(doc)) * 10000),2)
                        verbs_relative_freq = round(((verbs_count/len(doc)) * 10000),2)
                        adverb_relative_freq = round(((adverb_count/len(doc)) * 10000),2)
                        adjective_relative_freq = round(((adjective_count/len(doc)) * 10000),2)
                        

                        ''' 
                        Calculating the NER
                        '''
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
                        
                        '''
                        Apply the function the doc and append to the created lists
                        '''
                        unique_per_count, unique_loc_count, unique_org_count = unique_NE(doc)

                        filenames.append(os.path.basename(file))
                        nouns_freq.append(nouns_relative_freq)
                        verbs_freq.append(verbs_relative_freq)
                        adverbs_freq.append(adverb_relative_freq)
                        adjectives_freq.append(adjective_relative_freq)
                        no_unique_per.append(unique_per_count)
                        no_unique_org.append(unique_org_count)
                        no_unique_loc.append(unique_loc_count)


        '''
        Create dataframe and store data. Save to out folder 
        '''
        df = pd.DataFrame({
            "Filename": filenames, 
            "Nouns_Relative_Freq": nouns_freq,
            "Verbs_Relative_Freq": verbs_freq,
            "Adverbs_Relative_Freq": adverbs_freq,
            "Adjectives_Relative_Freq": adjectives_freq,
            "No_unique_per": no_unique_per,
            "No_unique_loc": no_unique_loc,
            "No_unique_org": no_unique_org
        })

        df = df.sort_values("Filename")
        csv_filename = f"out/{subfolder}_data.csv"
        df.to_csv(csv_filename, index=False)


def main(): 
    nlp = spacy.load("en_core_web_md")
    filepath = os.path.join(
                        "in",
                        "USEcorpus"
                        )
    loop_extract_save(filepath,nlp)

    

if __name__ == "__main__":
    main()