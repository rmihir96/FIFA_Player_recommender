from flask import Flask, render_template, url_for, request
from flask_bootstrap  import Bootstrap
from sklearn.externals import joblib
import pandas as pd
from get_imgs import get_imgs

app = Flask(__name__)
Bootstrap(app) 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])



def predict():
	player_indices = joblib.load(r'C:\Users\rmihi\Desktop\MyApp\models\finalized_model.sav')
	dataset = pd.read_csv(r"C:/Users/rmihi/Desktop/MyApp/data.csv")
# datafile.tail()

	# def get_index(x):
 #    #print(dataset[x in dataset["Name"]])
 #    return dataset[dataset['Name'].str.contains(x)].index.tolist()[0]

	# def recommend_me(player):
	#     print('Here are 5 players similar to', player, ':' '\n')
	#     index = get_index(player)
	#     for i in player_indices[index][1:]:
	#             print(dataset.iloc[i]['Name'], '\n')

	if request.method == 'POST':
		player_list = []
		img_list = []
		result = []
		pred_pos = []
		pred_club = []
		pred_oa = []
		player = request.form['namequery']
		print(player)
		index = dataset[dataset['Name'].str.lower().str.contains(player)].index.tolist()[0]
		query_player = dataset.iloc[index]['Photo']
		selected_club = dataset.iloc[index]['Club']
		selected_pos = dataset.iloc[index]['Position']
		selected_overall = dataset.iloc[index]['Overall']
		name = dataset.iloc[index]['Name']
		query_img  = get_imgs(name, query_player)
		result.append((query_img,selected_club ,selected_pos, selected_overall))
		for i in player_indices[index][1:]:
	            player_list.append(dataset.iloc[i]['Name'])
	            img_list.append(get_imgs(dataset.iloc[i]['Name'], (dataset.iloc[i]['Photo'])))
	            pred_club.append(dataset.iloc[i]['Club'])
	            pred_pos.append(dataset.iloc[i]['Position'])
	            pred_oa.append(dataset.iloc[i]['Overall'])
	            pred_img_list = zip(player_list, img_list, pred_club, pred_pos, pred_oa)

	return render_template('results.html', name = player.upper(), res = result, pred_imgs = pred_img_list)



if __name__ == '__main__':
	app.run(debug=True)