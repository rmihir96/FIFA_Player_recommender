# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

from sklearn.externals import joblib
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
# print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

datafile = pd.read_csv(r"C:/Users/rmihi/Desktop/MyApp/data.csv")
# datafile.tail()

# list(datafile)

#Select the features you want in the model

features = [
 'Age',
 'Overall',
 'Potential',
 'Preferred Foot',
 'Weak Foot',
 'Skill Moves',
 'Crossing',
 'Finishing',
 'HeadingAccuracy',
 'ShortPassing',
 'Volleys',
 'Dribbling',
 'Curve',
 'FKAccuracy',
 'LongPassing',
 'BallControl',
 'Acceleration',
 'SprintSpeed',
 'Agility',
 'Reactions',
 'Balance',
 'ShotPower',
 'Jumping',
 'Stamina',
 'Strength',
 'LongShots',
 'Aggression',
 'Interceptions',
 'Positioning',
 'Vision',
 'Penalties',
 'Composure',
 'Marking',
 'StandingTackle',
 'SlidingTackle',
 'GKDiving',
 'GKHandling',
 'GKKicking',
 'GKPositioning',
 'GKReflexes',
]

#Filter the dataset based on the above features:
attributes = datafile[features]
#attributes["Work Rate"] = datafile["Work Rate"].str.get_dummies(sep='/ ')

attributes["Preferred Foot"] = np.where(attributes["Preferred Foot"] == 'Left', 0, 1)
dataset = attributes
attributes = attributes.dropna()
# attributes.head()


#Changing categorical variables to numeric.
scaled = StandardScaler()
dataset_scaled = scaled.fit_transform(attributes)

df = pd.DataFrame(dataset_scaled)
# df.head()

dataset["Name"] = datafile["Name"]
dataset["Nationality"] = datafile["Nationality"]
dataset = dataset.dropna()

dataset.to_csv("dataset.csv")
# dataset.head()

#Building the model
from sklearn.neighbors import NearestNeighbors

recommendations = NearestNeighbors(n_neighbors=6, algorithm='auto').fit(dataset_scaled)

# print(recommendations)

# print(len(recommendations.kneighbors(dataset_scaled)[1]))

player_indices = recommendations.kneighbors(dataset_scaled)[1]

filename = 'finalized_model.sav'
joblib.dump(player_indices, filename)




