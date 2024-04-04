import pandas as pd 
import gensim.downloader as api
import argparse
import string

def get_artist_and_word():
    parser= argparse.ArgumentParser(description= "Loading and printing an array")
    parser.add_argument("--artist", #long form name
                        "-a",#short form name
                        required= True, #must give it an input in the command 
                        help= "put name of artist") #help message if input is missing 
    parser.add_argument("--search_term", #long form name
                        "-s",#short form name,change
                        required= True, #must give it an input in the command 
                        help= "put a search term") #help message if input is missing 
    args = parser.parse_args()
    args.artist= args.artist.lower()
    args.search_term= args.search_term.lower()
    return args



def calculate_stats(args): 
    name_of_artist = args.artist
    chosen_search_term = args.search_term

    model = api.load("glove-wiki-gigaword-50")
    song_data = pd.read_csv("data/Spotify Million Song Dataset_exported.csv")

    similar_words_list = []
    words = model.most_similar(chosen_search_term)
    for word, _ in words:
        similar_words_list.append(word)

    # Remove punctuation from the 'text' column
    song_data['text'] = song_data['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
        
    artist_df = song_data[song_data['artist'].str.lower() == name_of_artist]

    songs_already_counted = set()  # Set to keep track of songs already counted

    n_songs_where_word_from_wordslist_appears = 0
    for word in similar_words_list:
        # Iterate over each song's text
        for song_text in artist_df['text'].str.lower():
            # Check if the word appears in the song and if the song hasn't been counted yet
            if word in song_text and song_text not in songs_already_counted:
                n_songs_where_word_from_wordslist_appears += 1
                songs_already_counted.add(song_text)  # Add the song to the set to mark it as counted

    total_n_songs_for_artist = len(artist_df)

    percentage = round(((n_songs_where_word_from_wordslist_appears / total_n_songs_for_artist) * 100),2)

    return name_of_artist, chosen_search_term, percentage

def main():
    #call args fuction 
    args= get_artist_and_word()
    #function for calculation stuff
    name_of_arist, chosen_search_term, percentage= calculate_stats(args)
    print(f"{percentage}% of {name_of_arist}'s songs contain words related to {chosen_search_term}")
    


if __name__ == "__main__":
    main()