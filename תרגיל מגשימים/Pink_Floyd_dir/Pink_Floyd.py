PATH = r"Pink_Floyd_DB.txt"

def extract_albums_and_songs(path):
    """
    a function that gets a path of file
    and creates two dictionaries: 1st to album and its songs, 2nd to a song and its words
    :param path: the path of the file
    :return: 2 dictionaries to album and songs
    """
    album_dict = {}
    songs_dict = {}
    with open(path, 'r') as pink_floyd_file:
        for line in pink_floyd_file:
            if line[0] == '#': # case album
                album_name = line.split("::")[0][1:] # gets the album name
                if album_name not in album_dict:
                    album_dict[album_name] = []
            elif line[0] == '*': # case song
                split_line = line.split("::")
                song_name = split_line[0][1:]
                album_dict[album_name] += [song_name] # adds the song in the album
                length = [split_line[2]]
                songs_dict[song_name] = length # adds the length of the song to the start of the list of the words
                songs_dict[song_name] += [split_line[3][:-1]] # add the words in the first line (with the song name) without '\n'
            else:

                songs_dict[song_name] += [line[:-1]] # adds the words

    return album_dict, songs_dict


def get_albums_list(albums):
    """
    a function that returns all albums
    :param albums: the dictionary that holds the albums names
    :return: a list with the albums names
    """
    return " the albums are: {}\n".format(list(albums.keys()))


def get_songs_by_albums(album_name, albums):
    """
    a function that returns the songs of an album
    :param album_name: the name of the album
    :param albums: the dictionary of the albums
    :return: a string that says the songs of a specific album
    """
    return "the album: {} have the songs: {}".format(album_name, albums[album_name])


def get_song_length(song, songs):
    """
    a function that returns the length of a song
    :param song: a song from the list
    :param songs: the dictionary of songs
    :return: a string with the song name and its length
    """
    length = songs[song][0]
    return "the length of the song: {} is: {}".format(song, length)


def get_song_words(song, songs):
    """
    a function that returns the words of a specific song
    :param song: a song from the list
    :param songs: the dictionary of songs
    :return: words od a chosen song
    """
    words = songs[song][1:]
    return "the words of the song: {} are: {}".format(song, words)


def get_album_by_song(song, albums):
    """
    a function that finds the albums with a specific song in it
    :param song: a song that we search its albums
    :param albums: the album's dictionary
    :return: a list with the albums name that had this song
    """
    albums_names = []
    for album in albums.keys():
        values = albums[album]
        if song in values:
            albums_names += [album]
    return 'the albums: {} have the song: {}'.format(albums_names, song)


def get_every_song_with_word(word, songs):
    """
    a function that returns the songs with a words in their words
    :param word: the word we looking for
    :param songs: the songs' dictionary
    :return: a list with the songs that the word in their words
    """
    upper_word = word.upper()
    songs_list = []
    for song in songs:
        for line in songs[song]:
            upper_line = line.upper()
            if upper_word in upper_line:
                songs_list += [song]
                break # because we looking line by line we stops if we find immediately
    return "the songs: {} have the word: {} in it".format(songs_list, word)


def get_every_name_with_word(word, songs):
    """
       a function that returns the songs with a words in their name
       :param word: the word we looking for
       :param songs: the songs' dictionary
       :return: a list with the songs that the word in their name
       """
    upper_word = word.upper()
    songs_list = []
    for song in songs:
        upper_song = song.upper()
        if upper_word in upper_song:
            songs_list += [song]
    return "the songs: {} have in their name the word: {}".format(songs_list, word)


def main():
    albums, songs = extract_albums_and_songs(PATH)
    while True:
        choose = input(("Insert value between 1-8:\n"
                        "1 - get the album's list.\n"
                        "2 - get songs by album.\n"
                        "3 - get song length.\n"
                        "4 - get song words.\n"
                        "5 - get an album by song in it.\n"
                        "6 - get a list of songs by name.\n"
                        "7 - get a list of songs by word in it.\n"
                        "8 - exit.\n"))
        if choose == '8':
            break
        elif choose == '1':
            print(get_albums_list(albums))
        elif choose == '2':
            album_name = input("Insert an album name:\n")
            print(get_songs_by_albums(album_name, albums))
        elif choose == '3':
            song = input("Insert song name:\n")
            print(get_song_length(song, songs))
        elif choose == '4':
            song = input("Insert song name:\n")
            print(get_song_words(song, songs))
        elif choose == '5':
            song = input("Insert song name:\n")
            print(get_album_by_song(song, albums))
        elif choose == '6':
            word = input("insert a word:\n")
            print(get_every_name_with_word(word, songs))
        elif choose == '7':
            word = input("insert a word:\n")
            print(get_every_song_with_word(word, songs))
        else:
            print("Invalid choose\n")


if __name__ == '__main__':
    main()
