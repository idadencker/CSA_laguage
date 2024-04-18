from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def extract_emotions(df):
    '''
    A pipeline is specified for easy processing
    '''
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False)

    '''
    Text is made into list. Hereafter the text is classified using the pipeline and values are saved
    '''
    text = [str(i) for i in df['Sentence'].tolist()]
    emotion_scores = classifier(text)

    '''
    Appends the items to the dataframe
    '''
    labels = []
    scores = []

    for item in emotion_scores:
        labels.append(item['label'])
        scores.append(item['score'])

    df['emotion'] = labels
    df['score'] = scores

    return df



def emotions_count_for_seasons(df):
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    '''
    Loops through data and creates a histogram plot for each season
    '''
    for i, season_label in enumerate(df['Season'].unique()):
            season_data = df[df['Season'] == season_label]
            ax = season_data['emotion'].value_counts().sort_index().plot(kind='bar', title=f'Count of emotions in {season_label}', ax=axs[i // 3, i % 3])
            ax.set_xlabel('Emotions')
            ax.set_ylabel('Count')

    plt.tight_layout()
    plt.savefig("out/Count_all_emotions_for_seasons.png")
    plt.show()


def season_rel_freq_for_emotions(df):
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    '''
    Loops through data and creates a histogram plot for each emotion
    '''
    for i, emotion_label in enumerate(df['emotion'].unique()):
        emotion_data = df[df['emotion'] == emotion_label]
        counts = emotion_data['Season'].value_counts().sort_index()
        total_count = counts.sum()
        relative_freq = counts / total_count  
        ax = relative_freq.plot(kind='bar', title=f'Relative frequency of {emotion_label} across all seasons', ax=axs[i // 3, i % 3])
        ax.set_xlabel('seasons')
        ax.set_ylabel('Relative Frequency')

    plt.tight_layout()
    plt.savefig("out/Relative_frequency_of_emotions_across_all_seasons.png")
    plt.show()



def main():
    df = pd.read_csv("../../../../cds-lang-data/GoT-scripts/Game_of_Thrones_Script.csv")
    df = extract_emotions(df)
    emotions_count_for_seasons(df)
    season_rel_freq_for_emotions(df)

    

if __name__ == "__main__":
    main()