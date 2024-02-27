from flask import Flask
from rembg import remove 
from PIL import Image 

app = Flask(__name__)
@app.route('/image/', methods=['GET', 'POST'])
def image():
# Store path of the image in the variable input_path 
 input_path = '/content/dl.beatsnoop.com-high-736229d53e998bd6b6.jpg' 

# Store path of the output image in the variable output_path 
output_path = '/content/rmg.png' 

# Processing the image 
input = Image.open(input_path) 

# Removing the background from the given Image 
output = remove(input) 

#Saving the image in the given path 
output.save(output_path) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)