import pandas as pd 
import gensim.downloader as api
import argparse
import string


def get_artist_and_word():
    '''
    Function for getting and saving argparsers
    '''
    parser= argparse.ArgumentParser(description= "Loading and printing an array")
    parser.add_argument("--artist", 
                        "-a",
                        required= True, 
                        help= "put name of artist") 
    parser.add_argument("--search_term", 
                        "-s",
                        required= True, 
                        help= "put a search term") 
    args = parser.parse_args()
    args.artist= args.artist.lower()
    args.search_term= args.search_term.lower()
    return args


def calculate_stats(args): 
    '''
    Function that will return name of the artist chosen, the chosen search term, and the percentage of that artist songs that contain word(s) related to the search term
    '''
    name_of_artist = args.artist
    chosen_search_term = args.search_term

    model = api.load("glove-wiki-gigaword-50")
    song_data = pd.read_csv("data/Spotify Million Song Dataset_exported.csv")

    similar_words_list = []
    words = model.most_similar(chosen_search_term)
    for word, _ in words:
        similar_words_list.append(word)

    
    song_data['text'] = song_data['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
        
    artist_df = song_data[song_data['artist'].str.lower() == name_of_artist]

    songs_already_counted = set()  

    n_songs_where_word_from_wordslist_appears = 0
    for word in similar_words_list:
        for song_text in artist_df['text'].str.lower():
            if word in song_text and song_text not in songs_already_counted:
                n_songs_where_word_from_wordslist_appears += 1
                songs_already_counted.add(song_text)  

    total_n_songs_for_artist = len(artist_df)

    percentage = round(((n_songs_where_word_from_wordslist_appears / total_n_songs_for_artist) * 100),2)

    return name_of_artist, chosen_search_term, percentage


def main():
    args= get_artist_and_word()
    name_of_arist, chosen_search_term, percentage= calculate_stats(args)
    print(f"{percentage}% of {name_of_arist}'s songs contain words related to {chosen_search_term}")
    

if __name__ == "__main__":
    main()