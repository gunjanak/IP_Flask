from pydoc_data.topics import topics
from flask import Flask, render_template, request, session,redirect,flash
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
            load_image(img_file_path)
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
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Negative(gray_image)
                output_image = output_image[1].save("staticFiles/uploads/upload_negative.jpg")
                print(output_image)

                updated_img_file_path = "staticFiles/uploads/upload_negative.jpg"
                Algorithm_name = 'Negative Image'
            
            elif(Topic=='Basic' and Algorithm=='Threshold'):
                print('This is Threshold')
                threshold_value = request.form.get("Threshold_value")
                print(threshold_value)
                if(threshold_value==''):
                    return redirect('/')

                threshold_value = int(threshold_value)
                 
                
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


            elif(Topic=='Basic' and Algorithm=='BitPlane'):
                print('This is BitPlane Sclicing')
                img_file_path="staticFiles/uploads/upload.jpg"
                Bitplane_value = request.form.get("Bitplane_value")
                print(Bitplane_value)
                if(Bitplane_value==''):
                    return redirect('/')

                Bitplane_value = int(Bitplane_value)
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Bit_Plane(gray_image,Bitplane_value)
                output_image = output_image[1].save("staticFiles/uploads/upload_bitplane.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_bitplane.jpg"
                Algorithm_name = 'BitPlane Sclicing'

            elif(Topic=='Basic' and Algorithm=='LogTransform'):
                print('This is LogTransform')
                img_file_path="staticFiles/uploads/upload.jpg"
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                print(type(gray_image))
                output_image = Basic.Log_transform(gray_image)
                output_image = output_image[1].save("staticFiles/uploads/upload_logTransform.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_logTransform.jpg"
                Algorithm_name = 'Log Transform'

            elif(Topic=='Basic' and Algorithm=='PowerTransform'):
                print('This is Power Transform')
                img_file_path="staticFiles/uploads/upload.jpg"
                Power_value = request.form.get("Power_value")
                print(Power_value)
                if(Power_value==''):
                    return redirect('/')

                Power_value = float(Power_value)
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Power_transform(gray_image,Power_value)
                output_image = output_image[1].save("staticFiles/uploads/upload_power.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_power.jpg"
                Algorithm_name = 'Power Transform'

            elif(Topic=='Basic' and Algorithm=='Histogram'):
                print('This is Histogram Equalization')
                img_file_path="staticFiles/uploads/upload.jpg"
                gray_image="staticFiles/uploads/upload_400.jpg"
                gray_image = Image.open(gray_image)
                output_image = Basic.Histogram_equalization(gray_image)
                print(type(output_image[1]))
                output_image = output_image[1]
                output_image = Image.fromarray(output_image)
                output_image = output_image.convert("L")
                output_image = output_image.save("staticFiles/uploads/upload_histogram.jpg")
                print(output_image)
                updated_img_file_path = "staticFiles/uploads/upload_histogram.jpg"
                Algorithm_name = 'Histogram Equalization'

                

        else:
            pass

    else:
        img_file_path = ""
    
   

    return render_template('index.html',user_image = img_file_path,updated_image=updated_img_file_path,Algorithm_name=Algorithm_name)




#Running the app
if __name__ == '__main__':
    app.run(port=5000,debug=True)