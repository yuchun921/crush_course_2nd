"""Album:
Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, \
    and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
"""
from typing import Optional


def make_album(singer, album):
    # Build a dict containing album info
    album_info = {'singer': singer.title(), 'album': album.title()}
    return album_info


def make_album_containing_track(singer: str, album: str, track: Optional[int] = None):
    # Build a dict containing album info
    if track:
        album_info = {'singer': singer.title(), 'album': album.title(), 'track': track}
        return album_info
    album_info = {'singer': singer.title(), 'album': album.title()}
    return album_info


def main():
    print("Function: make_album")
    # Use the function to make three dictionaries representing different albums.
    print(make_album("Jolin", "Ugly Beauty"))
    print(make_album("Hebe", "Nobody knows"))
    print(make_album("T-ara", "DAY BY DAY"))

    print()
    print("Function: make_album_containing_track")
    # Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
    # Make at least one new function call that includes the number of songs on an album.
    print(make_album_containing_track("Jolin", "Ugly Beauty"))
    print(make_album_containing_track("Hebe", "Nobody knows", 11))
    print(make_album_containing_track("T-ara", "DAY BY DAY", 5))


if __name__ == "__main__":
    main()
