# Emotion analysis with pre-trained language models 

## Introduction
This program contains a script that will load a csv file of all lines from all 8 seasons of the poular televesion show Game of Thrones (GoT) to perform some computational text analysis. Using a pretrained sentiment analysis model, the emotion-english-distilroberta-base, an emotion for each line is extracted being either anger, disgust, fear, joy, neutral, sadness or surprise as well as a score ranging from 0-1 indication the intensity of the extracted emotion. 
The model is based on the highly complex "DistilRoBERTa" architecture which is a distilled version of the RoBERTa model, which is itself a variant of the well-known BERT (Bidirectional Encoder Representations from Transformers) model, said to be a state-of-the-art model in natural langauge processing. 
Plots demonstrating the distribution of all emotion labels in each season (8 seasons in total) and the relative frequency of each emotion across all seasons (7 emotions in total) is created and saved. The results are summarised and discussed.


## Data source
The dataset is the ```Game of Thrones Script All Seasons``` dataset which consists of all spoken lines from the popular show Game of Thrones. The dataset has a total of 23911 lines. The dataset can be found and downloaded [here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select%253DGame_of_Thrones_Script.csv). 


## Repository structure
The repository consists of 2 bash scripts, 1 README.md file, 1 txt file, and 3 folders. The folders contains the following:

-   in: for storing input data
-   out: holds the saved plots
-   src: script for doing emotion analysis on the GoT data


## Reproducibility 
To make the program work do the following:

1) download the dataset and place it in the 'in' folder.
2) in the script Emotion_analysis change the path to where the data is located 
3) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
4) in the terminal run the code:
    $ source run.sh
2 plots will be saved in the out folder. NOTE that the script will take some time to run since it deals with alot of data. 


## Summary and discussion
From looking at the first plot 'Count_all_emotions_for_seasons' it is clear that neutral is by far the most expressed emotion across all seasons. For all seasons anger is the second most expressed emotion. Generelly a very similar pattern for emotions is displayed for all 8 seasons, meaning that the distribution of emotions is close to identical for all seasons. 
Looking at the relative frequencies of the different emotions across seasons, joy and disgust seems to decrease over the seasons, while more dispersed patterns are seen for the other emotions. Interestingly, the relative frequency of sadness notably drop for the last two seasons 7 and 8. Also fear and surprise is low in the last season campared to the ramaining seasons. Generelly, most emotions are quite stable for seasons with only a few example that deviance from the little-fluctuation-pattern.  

