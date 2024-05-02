# Extracting linguistic features using spaCy


## Introduction
This program contains a script that will extract lingustic information including the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words as well as total number of unique person (PER), location (LOC), and organisation (ORG) entities on text files from the Uppsala Student English Corpus (USE). The extracted lingustic information for each subfolder is formatted to CSV and located in the out folder. The results are summarized and discussed


## Data source
The dataset is the ```The Uppsala Student English Corpus (USE)``` dataset which consist of 1,489 essays written by 440 Swedish university students of English at three different levels. The essays cover set topics of different types. All 'A' files are first-term essays, all 'B' files are second-term essays, all 'C' files are third-term essays. More information on the dataset and instructuctions for downloads can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). 


## Repository overview 
The repository consists of:
- 1 README.md file
- 2 bash scripts
- 1 requirenments file
- in folder for storing input data
- out folder for holding the saved results
- src folder containing the script for extracting linguistic features 


## Reproducibility 
To make the program work do the following:

1) clone the repository 
```python
$ git clone "URL HERE"
```
1) download the USEcorpus.zip and place the unzipped data in the 'in' folder
3) In a terminal set your directory:
```python
$ cd assignment_1
```
4) To create a virtual environment run:
```python
$ source setup.sh
```
5) To run the script and save results run: 
```python
$ source run.sh
```
14 CSV files will be saved the the out folder 


 ## Summary and discussion

