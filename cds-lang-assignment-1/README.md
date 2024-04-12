# Extracting linguistic features using spaCy

## Introduction
This program contains scripts that will extract lingustic information including Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words as well as total number of unique PER, LOC, and ORG entities on txt files from the Uppsala Student English Corpus (USE). The extracted lingustic information is formatted to csv and located in the out folder


## Data source
The dataset is the ```The Uppsala Student English Corpus (USE)``` dataset which ...
The dataset has x images. The dataset can be found [here](https://). 


## Repository structure

The repository consists of 2 bash scripts, 1 README.md file, 1 txt file, and 3 folders. The folders contains the following:

-   in: for storing input data
-   out: holds the saved results i.e. 1 csv for each file subfolder 
-   src: consists of script for extracting linguistic features 


## Reproducibility 
To make the program work do the following:

1) download the dataset and place it in the 'in' folder. Unzip it so data becomes accessible 
2) in the script Extracting_linguistic_features change file_path to where your data is located 
3) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
5) then run 
    $ source run.sh
All csv files will be saved in the out folder 


## Summary and discussion
 

