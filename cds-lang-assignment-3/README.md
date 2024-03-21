# Query Expansion

This program will use a gensim language  model to extract the 10 most similar word to a search term like the word 'dog', and apply it to a dataset containing 57.650 songs, to determine how many percentage of a given aritst's songs contains one or more of the 10 words. 

The dataset is the '57,650 Spotify Songs' data set. It provides a comprehensive collection of data that can be analyzed to gain insights into various aspects of the songs in the Spotify library.


To make the program work do the following:

1) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
2) Run wheter artist and word you want, dont worry about lower or uppercase, the program will understand:
    $ source run.sh --artist "ABBA" --search_term "car"
3) You will now get the statistics directly in your terminal:
    13.27% of abba's songs contain words related to car