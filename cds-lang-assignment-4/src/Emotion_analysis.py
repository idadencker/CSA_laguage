from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def extract_emotions(df):
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False)

    text = [str(i) for i in df['Sentence'].tolist()]
    emotion_scores_list = classifier(text)

    # Initialize empty lists to store labels and scores
    labels = []
    scores = []

    # Iterate through each item in emotion_scores_list
    for item in emotion_scores_list:
        labels.append(item['label'])
        scores.append(item['score'])

    # Append the labels and scores to the DataFrame
    df['emotion'] = labels
    df['score'] = scores

    return df

def emotions_count_for_seasons(df):
    # Iterate through each season label ('Season 1', 'Season 2', ..., 'Season 8')
    for season_label in df['Season'].unique():
        season_data = df[df['Season'] == season_label]
        plt.figure(figsize=(10, 5))
        ax = season_data['emotion'].value_counts().sort_index().plot(kind='bar', title=f'Count of emotions in {season_label}')
        ax.set_xlabel('Emotions')
        ax.set_ylabel('Count')
        plt.show()
        plt.savefig(f"out/emotions_count_{season_label}.png")


def season_rel_freq_for_emotions(df):
    


def main():
    df = pd.read_csv("../../../../cds-lang-data/GoT-scripts/Game_of_Thrones_Script.csv")

    

if __name__ == "__main__":
    main()