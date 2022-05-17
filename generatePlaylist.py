import spotipy
import numpy as np
import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'ffbef2bcb4b84e80b3a0039a2906cb01'
secret = '6c57daa1247f4abe96f38635d38869a0'
username = 'francocasadei'
redirect_uri = 'https://developer.spotify.com/dashboard/applications/ffbef2bcb4b84e80b3a0039a2906cb01'

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print (" %d %s %s" % (i, track['artists'][0]['name'],track['name']))

def get_track_features(track_id,sp):
    if track_id is None:
        return None
    else:
        features = sp.audio_features([track_id])
    return features

def get_features(tracks,sp):
    tracks_with_features=[]

    for track in tracks:
        features = get_track_features(track['id'],sp)
        print (track['name'])
        if not features:
            print("passing track %s" % track['name'])
            pass
        else:
            f = features[0]
            tracks_with_features.append(dict(
                                            name=track['name'],
                                            artist=track['artist'],
                                            id=track['id'],
                                            danceability=f['danceability'],
                                            energy=f['energy'],
                                            loudness=f['loudness'],
                                            speechiness=f['speechiness'],
                                            acousticness=f['acousticness'],
                                            tempo=f['tempo'],
                                            liveness=f['liveness'],
                                            valence=f['valence']
                                            ))
    return tracks_with_features

def get_tracks_from_playlists(username, sp):
    playlists = sp.user_playlists(username)
    trackList = []
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print (playlist['name'],' no. of tracks: ',playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],fields="tracks,next")
            tracks = results['tracks']
            for i, item in enumerate(tracks['items']):
                track = item['track']
                trackList.append(dict(name=track['name'], id=track['id'], artist=track['artists'][0]['name']))
    return trackList

def write_to_csv(track_features):
    df = pd.DataFrame(track_features)
    df.drop_duplicates(subset=['name','artist'])
    print ('Total tracks in data set', len(df))
    df.to_csv('mySongsDataset.csv',index=False)

def spotify_data(track_features):
    df = pd.DataFrame(track_features)
    df.drop_duplicates(subset=['name','artist'])
    return df

def main(username):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    tracks = get_tracks_from_playlists(username, sp)
    tracks_with_features = get_features(tracks,sp)
    write_to_csv(tracks_with_features)
    return spotify_data(tracks_with_features)

