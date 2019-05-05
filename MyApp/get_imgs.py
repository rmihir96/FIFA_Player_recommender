
import requests 
import os.path

save_path = r'C:\Users\rmihi\Desktop\MyApp\static'
def get_imgs(name, image_url):

	# URL of the image to be downloaded is defined as image_url 
	r = requests.get(image_url) # create HTTP response object 
	  
	# send a HTTP request to the server and save 
	# the HTTP response in a response object called r 
	name = name +'.png'
	path = os.path.join(save_path, name)
	if name not in save_path:
		with open(path,'wb') as f: 
		  
		    # Saving received content as a png file in 
		    # binary format 
		  
		    # write the contents of the response (r.content) 
		    # to a new file in binary mode. 
		    f.write(r.content) 
	return name