import argparse
import pprint
import json
import spotipy
import numpy as np
import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from .generatePlaylist import *
from .processing_ import *
from .training import *

"""
python main.py --cid --sid --randomforest
"""

if __name__ == '__main__':
    print ('Starting...')
    parser = argparse.ArgumentParser(description='this sript will grab user playlists')
    parser.add_argument('--username', help='username')
    parser.add_argument('--cid', help='credential id')
    parser.add_argument('--secret', help='secret key')
    parser.add_argument('--training', help='Mention model to be trained')
    parser.add_argument('--tfp', help='Training File Path')
    parser.add_argument('--pfp', help='Predicting File Path')
    args = parser.parse_args()
    songs_data = main(args.username)
    y_train = labelling_dataset(songs_data)
    X_train = songs_features(songs_data)

    model = None

    if args.training == "decisiontreeclassifier":
        model = decisiontreeclassifier(X_train,y_train)
    elif args.training == "randomforestclassifier":
        model = randomforestclassifier(X_train,y_train)
    elif args.training == "kneighborsclassifier":
        model = kneighborsclassifier(X_train,y_train)
    elif args.training == "svmclassifier":
        model = svmclassifier(X_train,y_train)
    elif args.training == "mlpclassifier":
        model = mlpclassifier(X_train, y_train)
    else:
        print("Invalid Training Model Example")
        
    predict_data = pd.read_csv(args.pfp)

    pred_X = songs_features(predict_data)
    pred_y = model.predict(pred_X)

    counts = np.bincount(pred_y)
    max_label = np.argmax(counts)

    print(max_label, counts[max_label]/counts.sum())