from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import numpy as np
import pandas as pd

def loudness_scaled(songs):
    loudness = songs[['loudness']].values
    min_max_scaler = preprocessing.MinMaxScaler()
    loudness_scaled = min_max_scaler.fit_transform(loudness)
    songs['loudness'] = pd.DataFrame(loudness_scaled)
    return songs

def songs_features(songs):
    songs_ = loudness_scaled(songs)
    songs_feature = songs_.copy()
    songs_feature = songs_feature.drop(['name','artist','id'],axis=1)
    return songs_feature

def labelling_dataset(songs):
    kmeans = KMeans(n_clusters=4)
    songs_feat = songs_features(songs)
    kmeans.fit(songs_feat)
    y_kmeans = kmeans.predict(songs_feat)
    return y_kmeans
 
"""
def visualisation_clusters():
    songs_feat = songs_features()
    y_kmeans = labelling_dataset()
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(songs_feat)
    pc = pd.DataFrame(principal_components)
    pc['label'] = y_kmeans
    pc.columns = ['x', 'y','label']
    cluster = sns.lmplot(data=pc, x='x', y='y', hue='label', 
                   fit_reg=False, legend=True, legend_out=True)
"""