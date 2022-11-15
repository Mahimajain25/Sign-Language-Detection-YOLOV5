import os
import shutil
import sys
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

IMG_FOLDER = os.path.join('static', 'upload')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

PRED_FOLDER = os.path.join('yolov5','runs','detect','exp')

DETECT_FOLDER = os.path.join('yolov5','runs','detect')

detect_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       DETECT_FOLDER )

upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        app.config['UPLOAD_FOLDER'])

exp_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"yolov5/runs/detect/exp")

yolov5_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),"yolov5")



@app.route('/', methods=['GET',"POST"])
def landing_page():
    ## removing old upload and prediction folder 
    if os.path.exists(detect_path):
        shutil.rmtree(detect_path)
    if os.path.exists(upload_path):
        shutil.rmtree(upload_path)
    return render_template('index.html')

@app.route('/upload_img', methods=['GET',"POST"])
def upload_img():
    ## removing old upload & prediction folder and creating new upload folder 
    if os.path.exists(upload_path):
        shutil.rmtree(upload_path)
    else:
        os.makedirs(upload_path)

    if os.path.exists(detect_path):
        shutil.rmtree(detect_path)
    return render_template('upload.html')

@app.route('/uploader', methods=['GET',"POST"])
def home():
    if request.method == 'POST':
      # Fetching the uploading file
      f = request.files['file']
      f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        app.config['UPLOAD_FOLDER'],
                        secure_filename(f.filename))) # Then save the file
      os.chdir(yolov5_dir)
      # detecting the image (yolov5 detect) and internally will save the img in yolov5/run/detect/exp
      os.system("python detect.py --weights best.pt --img 416 --conf 0.5 --source ../static/upload")
      os.chdir("D:\Sign-language-Detection\Sign-Language-Detection-YOLOV5")
      
      ## creating uploaded img path
      l1 = os.listdir(IMG_FOLDER)
      upload_img = os.path.join("upload/", l1[0])
    
      ## Predicted img path preparation and keeping pred img in upload folder
      pred_base_path = os.path.join('yolov5','runs','detect','exp')
      l2 = os.listdir(PRED_FOLDER)
      name_ext = os.path.splitext(l2[0])
      new_name = os.path.join(pred_base_path,name_ext[0] + 'pred' + name_ext[1])
      old_name = os.path.join(pred_base_path,l2[0])
      pred_img_rename = os.rename(old_name,new_name)
      l3 = os.listdir(PRED_FOLDER)
      pred_img = os.path.join(pred_base_path,l3[0])
      shutil.copy2((pred_img),IMG_FOLDER)

      # fetching list of upload and pred image
      l4 = os.listdir(IMG_FOLDER)
      l4 = ['upload/' + i for i in l4]
      
    return render_template("predict.html", imagelist=l4)

@app.route('/rtdetection', methods=['GET',"POST"])
def rtdetection():
    ## removing old upload & prediction folder and creating new upload folder 
    if os.path.exists(upload_path):
        shutil.rmtree(upload_path)
    else:
        os.makedirs(upload_path)

    if os.path.exists(detect_path):
        shutil.rmtree(detect_path)
    return render_template("rtdetection.html")
  
@app.route('/rtpred', methods=['GET',"POST"])
def start():
    os.chdir(yolov5_dir)
    os.system("python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
    return render_template("rtend.html")
    

if __name__ == '__main__':
    app.run(debug=True)