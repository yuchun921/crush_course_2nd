"""User Albums:
Start with your program from Exercise 8-7.
Write a "while loop" that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
"""


def make_album(singer, album):
    # Build a dict containing album info
    album_info = {'singer': singer.title(), 'album': album.title()}
    return album_info


def main():
    while True:
        print("\nPlease enter singer and album, press 'q' to quit.")
        singer = input("Singer: ")
        if singer.lower() == "q":
            break
        album = input("Album: ")
        if album.lower() == "q":
            break

        album_info = make_album(singer, album)
        print(album_info)


if __name__ == "__main__":
    main()
