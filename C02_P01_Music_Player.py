import time
import random
import csv


# This class will help in creating song object
# It conatins information related to song such as id, name and duration
class Song:
    def __init__(self, song_id, song_name, song_length):
        self.song_id = song_id
        self.song_name = song_name
        self.song_length = song_length

    def __str__(self):
        return str({'song_id': self.song_id,
                    'song_name': self.song_name,
                    'song_length': self.song_length})


# Node for each of teh cong object that is going to be created. 
# Each of these node will contain the song data nd reference to the next element
class ListNode:
    def __init__(self, song: Song):
        self.song = song
        self.next = None

    def __str__(self):
        return str(self.song)


# Linked list class that will be used to do the various operations
# Insert, create, delete, traversal of the linked list
# Few other operation such as 
# a. deletion of song, 
# b. sorting a linked list based on song 
# c. randomly picking a song for playing

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.count = 0

    # Traversing the linked lists
    def traversal(self):
        if self.head_node is None:
            return

        temp_node = self.head_node

        while temp_node is not None:
            print(temp_node.song)
            time.sleep(2)
            temp_node = temp_node.next

        time.sleep(2)

        return

    # insertion of the node in the beginning of the linked lists
    def insert_at_start(self, node):
        if self.head_node is None:
            self.head_node = node
            self.count = self.count + 1
            return True

        node.next = self.head_node
        self.head_node = node

        return True

    # insertion of the node after a particular song    
    def insert_after(self, song_name, node):
        temp_node = self.head_node

        # Checking till we find the song_name we are looking for
        while temp_node.song.song_name != song_name:
            temp_node = temp_node.next

        # if song is not found  
        if temp_node is None:
            return False

        # if song is found
        else:
            # Checking if it is the last node
            if temp_node.next is None:
                temp_node.next = node
            # If it is not the last node
            else:
                node.next = temp_node.next
                temp_node.next = node

            return True

    # insertion of the node before a particular song in the linked lists    
    def insert_before(self, song_name, node):
        temp_node = self.head_node
        prev_node = None

        # Checking till we find the song_name we are looking for
        while temp_node.song.song_name != song_name:
            prev_node = temp_node
            temp_node = temp_node.next

        # if song is not found  
        if temp_node is None:
            return False

        # if list has only one song
        if prev_node is None:
            node.next = self.head_node
            self.head_node = node
            return True

        # updating the linked list and inserting the data
        prev_node.next = node
        node.next = temp_node

        return True

    # Deleting a song from the linekd list
    def delete_song(self, song_name):
        if self.head_node is None:
            return
        temp_node=self.head_node
        if temp_node is not None:
            if temp_node.song.song_name==song_name:
                self.head_node=temp_node.next
                del temp_node
                return
            while temp_node is not None:
                if temp_node.song.song_name==song_name:
                    break
                prev_node=temp_node
                temp_node=temp_node.next
            if temp_node is None:
                return
            prev_node.next=temp_node.next
            del temp_node
            return

    def sort_list(self):
        current = self.head_node
        index = None
        if current is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.song.song_name > index.song.song_name:
                        temp = current.song
                        current.song = index.song
                        index.song = temp
                    index = index.next
                current = current.next
        return

        # This means the whole list will be updated based on the song.
        # Please understand that the sorting should happen based on the song_name.
        # You can use the sorted method that is available inbuilt. sorted() function
        # Once the list is updated return result to the function from where ot was called.

    def shuffle_song(self):
        count = []
        if self.head_node is None:
            return

        temp_node = self.head_node

        while temp_node is not None:
            count.append(temp_node.song.song_id)
            temp_node = temp_node.next
        random_song_id = random.choice(count)
        temp_node = self.head_node
        while temp_node is not None:
            if temp_node.song.song_id == random_song_id:
                print(temp_node.song)
                time.sleep(2)
            temp_node = temp_node.next
        return


# playlist class that contains the feature of the playlist in any music player
# a. Give playlist_id, name and the linked_list or list of songs it contains. 

class PlayList:
    def __init__(self, id, playlist_name, linked_list: LinkedList):
        self.playlist_id = id
        self.playlist_name = playlist_name
        self.playlist_linked_list = linked_list

    def get_playlist(self):
        return self.playlist_linked_list

    def get_playlist_name(self):
        return self.playlist_name

    def get_playlist_id(self):
        return self.playlist_id


# Music Player class
# this will have operation to pick a playlist, 
# play songs from the play list, append new songs
# delete songs from the playlist
# Sort the songs that are available in the playlist
# Play the shuffled songs that are available in the play list

class MusicPlayer:
    # Creating list of playlists in the musicplayer
    def __init__(self):
        self.playlists = list()

    # Adding new playlist in the music player
    def add_playlist(self, new_playlist: PlayList):
        self.playlists.append(new_playlist)

    # playing songs that are available in the playlist
    def play_playlist(self, playlist_name):
        for playlist in self.playlists:
            # if the playlist exist with the provided name
            if playlist.get_playlist_name() == playlist_name:
                # Traversing the linked list and playing songs from linked list
                playlist.get_playlist().traversal()
            else:
                print('No such playlist exists in the Music Player')

    # Method ro delete a song from the playlist
    def delete_song_from_playlist(self, playlist_name, song_name):
        playlist = self.search_playlist_by_name(playlist_name)
        # Checking playlist exists
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        # Deleting the sonf grom the playlist by calling delete method
        playlist.get_playlist().delete_song(song_name)
        return

    # Method to perform sorting on the given linked list    
    def sort_playlist(self, playlist_name):
        # Checking playlist exists
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        # calling the sorting method to perform the sort based on the 
        # song name available in each of the node,
        playlist.get_playlist().sort_list()
        return

    def play_shuffled_song(self, playlist_name):
        # Checking playlist exists
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        # Picking a song randomly from the playlist and playing it. 
        print(playlist.get_playlist().shuffle_song())
        return

    # lsiting down all the playlist available in the music player
    def list_all_playlists(self):
        for playlist in self.playlists:
            print(playlist.playlist_name)

    # Seacrhing a song in the playlist
    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                return playlist

        return None

    # deleting a playlist from the music player
    def delete_playlist(self, name):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                del playlist
                return True

        return False


# This methid will take the song available in the csv file and create a linked list.
# This will also insert the songs in the linked list
def create_linked_list():
    with open('app_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        linked_list = LinkedList()
        for row in reader:
            song = Song(row['Song ID'], row['Song Name'], row['Song Length'])
            listnode = ListNode(song)
            linked_list.insert_at_start(listnode)

    return linked_list


if __name__ == "__main__":
    musicplayer = MusicPlayer()

    # This will create the linked list from the CSV file
    linked_list = create_linked_list()

    # Creating a playlist using the linked lists created in previous step
    playlist = PlayList(1, 'Songs', linked_list)

    # Adding the playlist in the music player
    print("\nAdding playlist to the Music Player \n")
    musicplayer.add_playlist(playlist)

    # playing all the songs that are avilable in the playlist
    print(f'Playing all songs in the playlist : {playlist.playlist_name}: \n')
    musicplayer.play_playlist('Songs')

    # Deleting a song from the playlist
    print(f'\nDeleting the Song with name : Old And Secrets \n')
    musicplayer.delete_song_from_playlist('Songs', 'Old And Secrets')
    musicplayer.play_playlist('Songs')

    # performing a sort on the playlist.
    # This method should return the playlist in sorted order based on the song name
    print('\nPlaying all songs after sorting based on song names: \n')
    musicplayer.sort_playlist('Songs')
    musicplayer.play_playlist('Songs')

    # Playing a shuffled song from  the playlist
    # Every time this function is called a different should be played
    print('\nPlaying shuffled song \n')
    musicplayer.play_shuffled_song('Songs')
