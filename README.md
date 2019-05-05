# FIFA_Player_recommender
Created a web-app to recommend players using FIFA19 dataset by applying Nearest Neighbours.

## Dataset: https://www.kaggle.com/karangadiya/fifa19/

## Technologies Used:

1. Python
2. Flask
3. Jinja
4. HTML, CSS, JS

## Data Preprocessing:
As per domain knowledge, some features are selected from the given features for training the model. The dataset is preprocessed to remove missing values and converting categorical labels to numeric values.
Finally, the dataset is normalized.

## Model:
The model is trained using nearest neighbor package from sklearn.neighbors. The algorithm method used here is "auto".
5 nearest neighbors are returned by the model which can be later on visualized using Flask.

## Deployment
The model is deployed using Flask and Jinja2 template. Flask is a micro web framework written in Python. Jinja is a web template engine for the Python programming language and is licensed under a BSD License created by Armin Ronacher.
1. The pickle model is loaded in the backend and then the query is passed using the POST method. 
2. To make the output more expressive, images, overall, position, club and name of the query player and predicted players is returned.
3. The images are downloaded during run time using the _get_imgs.py_ script. The images have to be in the _"./static"_ folder as per Flask terminologies.

## Results:
The home page:

![alt text](https://github.com/rmihir96/FIFA_Player_recommender/blob/master/MyApp/home.PNG)

Predictions:

![alt text](https://github.com/rmihir96/FIFA_Player_recommender/blob/master/MyApp/predict.PNG)
