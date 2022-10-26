from pydoc_data.topics import topics
from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename
from PIL import Image
import Basic
 


def load_image(img):
    image = Image.open(img)
    image = image.convert('L')
    newsize = (400,400)
    image = image.resize(newsize)
    print(image)
    image = image.save("staticFiles/uploads/upload_400.jpg")

    return None

Flag = 0
img_file_path = ""
#Defining upload folder path
UPLOAD_FOLDER = os.path.join('staticFiles','uploads')
#Define allowed files
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

app = Flask(__name__,template_folder='templates',static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Define secret key to enable session
app.secret_key = "sanaan"

@app.route('/',methods=("POST","GET"))
def index():
    Flag = 0
    img_file_path = ""
    updated_img_file_path = ""
    Algorithm_name = ""
   
    if request.method =='POST':
        if request.form.get('Submit_action')=='Submit':
            #upload file flask
            uploaded_img = request.files['uploaded-file']
            print(uploaded_img.filename)
            #extracting uploaded data file name
            #img_filename = secure_filename(uploaded_img.filename)
            #print(img_filename)
            #Upload file todatabase (defined uploaded folder in staticpath)
            uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'upload.jpg'))
            #Storing uploaded file path in flask session
            session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],'upload.jpg')
            #retriving uploaded file path from session
            img_file_path = session.get('uploaded_img_file_path',None)
            print(img_file_path)
            Flag = 1 
        elif request.form.get('Cascade_action') == 'Submit':
            print('This is cascade')
            Topic = request.form.get("Topic")
            print(Topic)
            Algorithm = request.form.get("Algorithm")
            print(Algorithm)
            if(Topic=='Basic' and Algorithm=='Negative'):
                print('This is negative')
                img_file_path="staticFiles/uploads/upload.jpg"
                #print(img_file_path)
                load_image(img_file_path)
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Negative(gray_image)
                output_image = output_image[1].save("staticFiles/uploads/upload_negative.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_negative.jpg"
                Algorithm_name = 'Negative Image'
            
            elif(Topic=='Basic' and Algorithm=='Threshold'):
                print('This is Threshold')
                threshold_value = int(request.form.get("Threshold_value"))
                print(threshold_value)
                img_file_path="staticFiles/uploads/upload.jpg"
                #print(img_file_path)
                load_image(img_file_path)
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Threshold(gray_image,threshold_value)
                output_image = output_image[1].save("staticFiles/uploads/upload_threshold.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_threshold.jpg"
                Algorithm_name = 'Threshold Image'
                

        else:
            pass

    else:
        img_file_path = ""

    return render_template('index.html',user_image = img_file_path,updated_image=updated_img_file_path,Algorithm_name=Algorithm_name)




#Running the app
if __name__ == '__main__':
    app.run(port=5000,debug=True)