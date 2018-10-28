from . import app
from flask import render_template, send_from_directory, request, url_for, redirect, jsonify
from werkzeug.utils import secure_filename
from lib.counting import *
from lib.stitching import *
import os
import datetime
from PIL import Image

ALLOWED_IMAGE_EXTENSIONS = set(['jpg', 'jpeg'])
ALLOWED_VIDEO_EXTENSIONS = set(['mp4', 'avi'])

"""
    Description: a function used to see if the uploaded file is in a valid format.
    @Param filename - name of the file being uploaded.
    @Param extensionList - set of allowed file extensions.
    @return a boolean indicating whether the image is in an acceptable format or not.
"""
def isFileAllowed(filename, extensionList):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensionList

def setupUploadDir():
    # create new folder to hold users data for run
    uploadDir = './Server/resources/uploads'
    now = datetime.datetime.now()
    newFolder = now.strftime("%Y-%m-%dT%H-%M-%S")
    newDir = uploadDir + "/" + newFolder
    os.mkdir(newDir)
    subfolders = ['images', 'videos', 'maps', 'results']
    for folder in subfolders:
        subDir = newDir + "/" + folder
        os.mkdir(subDir)
    return newDir

# route for serving static resources (images/js/css)
@app.route('/resources/<path:path>')
def sendJs(path):
    return send_from_directory('resources', path)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    errorMessage = request.args['errorMessage']
    return render_template('error.html',error=errorMessage)

@app.route('/uploadImages', methods=["POST"])
def uploadImages(): 
    images = request.files.getlist("images")
    magLevel = request.form["magLevel"]

    newDir = setupUploadDir()

    for i in images: 
        #redirect to error page if the image is in an unacceptable
        if(isFileAllowed(i.filename,ALLOWED_IMAGE_EXTENSIONS) == False): 
            return redirect(url_for('error',errorMessage="One or more of the images that were uploaded are in the incorrect format. Accepted formats: "+(", ".join(ALLOWED_IMAGE_EXTENSIONS))))

        print("Image is permitted: "+str(isFileAllowed(i.filename,ALLOWED_IMAGE_EXTENSIONS))) #see if the image format is allowed
        print("Secure filename: "+str(secure_filename(i.filename))) #escape the filename

        imgPath = newDir + "/images/" + str(secure_filename(i.filename))
        i.save(imgPath)
    

    #TODO: return location of the directory to the user
    return redirect('/getStitchedImage/' + newDir.split('/')[-1]) #redirect to homepage

@app.route('/uploadVideo', methods=["POST"])
def uploadVideo(): 
    video = request.files['video']

    newDir = setupUploadDir()

    #redirect to the error page if the video is not the correct format
    if(isFileAllowed(video.filename,ALLOWED_VIDEO_EXTENSIONS) == False):
        return redirect(url_for('error',errorMessage="The uploaded video is in the incorrect format. Accepted formats: "+(", ".join(ALLOWED_VIDEO_EXTENSIONS))))

    print("Video is permitted: "+str(isFileAllowed(video.filename,ALLOWED_VIDEO_EXTENSIONS))) #see if the image format is allowed
    print("Secure filename: "+str(secure_filename(video.filename))) #escape the filename

    # place video in a unique directory
    vidPath = newDir + "/videos/" + str(secure_filename(video.filename))
    video.save(vidPath)
    return redirect(url_for('index')) #redirect to homepage

# accepts a path to the image directory to use for stitching
@app.route('/getStitchedImage/<path:directory>')
def getStitchedImage(directory): 
    dirPrefix="Server/resources/uploads/"
    stitcher = Stitching()
    stitcher.setDirectory(dirPrefix + directory + "/images") #dirPrefix+directory+"/images"
    #resultPath = dirPrefix+directory+"/map"+str(numFiles)+".jpg"

    #!!!REMOVE THIS COMMENT!!!
    
    imageMap = stitcher.twoRoundStitch()
    numFiles = len([name for name in os.listdir(dirPrefix+directory+"/maps")]) + 1
    print("Finished stitching")
    #resultPath = "/resources/uploads/"+directory+"/maps/map.png" #!!!REMOVE THIS!!!!
    #print(resultPath)
    #return "<img src='"+resultPath+"'>" #return the stitched map. this is just to show that it's working
    return render_template('stitched.html', numFiles=numFiles)

# accepts a path to the stitched image directory
@app.route('/getResults/<path:directory>')
def getResults(directory): 
    print("getting getResults")
    print(directory)

    results = ""
    #TODO: format results from bead counting 
    #TODO: return results and store them locally
    directory = 'Server/resources/uploads/' + directory
    results = directory + '/results/'
    for file in results:
        filePath = os.path.join(results, file)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
        except Exception as e:
            print(e)
    directory += '/maps/'
    valid = 0
    water = 0
    images = [file for file in os.listdir(directory) if os.path.isfile((directory+file))]
    for image in images:
        print(directory+image)
        count = Counting(directory+image)
        #TODO: add logic here for config
        circles = count.getColorBeads(HoughConfig.OBJX10)
        results += "Valid beads: " + str(len(circles))
        valid += len(circles)
        results += "\n" + "Water beads: " + str(len(count.waterBeads)) +'\n'
        water += len(count.waterBeads)
    print(results)
    return render_template('results.html', numImages = len(images),validBeads=valid, waterBeads=water) 
