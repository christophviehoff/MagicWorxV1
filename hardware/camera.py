import threading
import sys, atexit
from cfgreader import read_camera_config

from cameracontrol import Ui_Controller

import numpy as np


from PyQt5 import QtCore, QtGui, uic, QtWidgets #works for pyqt5

# import the necessary packages
from imutils.video import VideoStream
from imutils import resize,rotate,rotate_bound
# Imports the Google Cloud client library
from google.cloud import vision

import datetime
import imutils
import time
import cv2
import os

import enchant
from enchant.checker import SpellChecker


def run_detect_document(filename):
    """Detects document features in an image."""
    vision_client = vision.Client()

    image = vision_client.image(filename=filename)

    document = image.detect_full_text()

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))

    return block_text,block.bounding_box

def image_to_text(filename):

    #default if no text was found in image
    vertices = []
    msg=None

    """Detects first text features in an image."""
    #vision_client = vision.Client(project="SightMachine")
    # set already at the beginning with env variable  GOOGLE_CLOUD_PROJECT
    vision_client = vision.Client()

    # Loads the image into memory
    image = vision_client.image(filename=filename)

    # SEE https://googlecloudplatform.github.io/google-cloud-python/stable/vision-usage.html
    #client = vision.Client()
    #image = client.image(source_uri='gs://my-test-bucket/image.jpg')
    #with io.open('../pictures/cropped.jpeg', 'rb') as image_file:
    #    image = vision_client.image(content=image_file.read())

    texts = image.detect_text()
    #TODO deal with indexError exception
    try:  # first one found only
        for bound in texts[0].bounds.vertices:
            vertices.append((bound.x_coordinate, bound.y_coordinate))
        return texts[0].description, vertices
    except IndexError:
        return msg, vertices



class Video():
    def __init__(self, capture):
        self.capture = capture
        self.currentFrame = np.array([])
        self.capture.start()

        # allows the (pi)camera sensor to warmup
        time.sleep(2)
        #source crop corner points
        self.startY =0
        self.endY = 0
        self.startX = 0
        self.endX = 0

        #result crop corenr points
        self.r_startY = 0
        self.r_endY = 0
        self.r_startX = 0
        self.r_endX = 0
        # load configuration data for the camera
        self.load_configuration('Camera')

    def load_configuration(self,data):
        # read configuration of default target, default is Camera
        self.config = read_camera_config(data)
        self.name, self.startY, self.endY, self.startX, self.endX = self.config

    def captureNextFrame(self):
        """
        capture frame and reverse RBG BGR and return opencv image
        """
        readFrame = self.capture.read()  #readfarme is a np array

        # TODO get a return value when no image is there
        self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)

        # draw the timestamp on the frame
        timestamp = datetime.datetime.now()
        ts = "magicworx " + timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(self.currentFrame, ts, (10, self.currentFrame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 1)

        # show capture area: top-left corner and bottom-right corner of rectangle
        self.currentFrame= imutils.rotate_bound(self.currentFrame,-90)
        cv2.rectangle(self.currentFrame, (0, 0), (480, 640), (255, 0, 0), 3)

        # crop frame display
        cv2.rectangle(self.currentFrame, (self.startX, self.startY), (self.endX, self.endY), (0, 255, 0), 1)
        # result cropping
        cv2.rectangle(self.currentFrame, (self.r_startX, self.r_startY), (self.r_endX, self.r_endY), (0, 255, 0), 3)



    def draw_bounding_box(self,vertices):
        # draw the bounding box of text description found
        #print vertices
        try:
            a, b, c, d =vertices
            # print vertices,self.startX,self.startY
            # plus correct for reference frame shift from cropped image
            self.r_startX = a[0]+self.startX
            self.r_startY = a[1]+self.startY
            self.r_endX =c[0]+self.startX
            self.r_endY=c[1]+self.startY
        except ValueError :
            print " no valid vertices"


    def grabFrame(self):
        """
        grab a camera frame and  return opencv images

        grab top and bottom sections incase image is upside down
        """
        imgT = imutils.rotate_bound(self.capture.read(),-90)  # right side up
        imgB = imutils.rotate_bound(self.capture.read(), 90)  # upside down

        #img_cropped=imgT[self.startY:self.endY, self.startX:self.endX]
        #gvision = np.concatenate(
        #    (imgT[self.startY:self.endY, self.startX:self.endX], imgB[self.startY:self.endY, self.startX:self.endX]),
        #    axis=0)  # 380x60

        #manipulate image to improve text to image
        #gray_image = cv2.cvtColor(imgT, cv2.COLOR_BGR2GRAY)

        #blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

        #TODO options for later
        #cv2.imwrite("../pictures/thumbnail.png", imutils.resize(imgT,width=100))  # 100x133

        #cropped_image= cv2.cvtColor(imgT[self.startY:self.endY, self.startX:self.endX], cv2.COLOR_BGR2GRAY)

        #gray = cv2.cvtColor(imgT, cv2.COLOR_BGR2GRAY)
        #edged = imutils.auto_canny(gray)

        #return imgT[self.startY:self.endY, self.startX:self.endX],imgB[self.startY:self.endY, self.startX:self.endX]
        return imgT[self.startY:self.endY, self.startX:self.endX]

    def convertFrame(self):
        """     converts frame to format suitable for QtGui  Qimage then Qpixmap          """
        try:
            height, width = self.currentFrame.shape[:2]
            img = QtGui.QImage(self.currentFrame,
                               width,
                               height,
                               QtGui.QImage.Format_RGB888)

            img = QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img #rotated_img
        except:
            return None

if __name__ == "__main__":
    import difflib
    toggle = False

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/my_private_access_key.json"
    os.environ["GOOGLE_CLOUD_PROJECT"]="SightMachine"

    # Help functions
    def terminate():
       print 'Program terminated by user'

    # main bin test GUI program class
    class MyCameraControl(Ui_Controller):

        def __init__(self, dialog):
            Ui_Controller.__init__(self)
            self.ui=self.setupUi(dialog)
            self.running=False
            self.vertices=[(0,0),(0,0),(0,0),(0,0)]
            self.result=None
            # initialize the video stream and define the resolution default is 320x240
            self.video = Video(VideoStream(usePiCamera=True,resolution=(640,480)))#upscale imagae later
            # self.video = Video(cv2.VideoCapture(0))
            self._timer = QtCore.QTimer(self.ui)
            self._timer.timeout.connect(self.play)
            self._timer.start(27)  # 27ms

            #self.imageFrame.setPixmap(QtGui.QPixmap("deckmaster.png"))  # (png-->qpixmap)
            #self.pwl = enchant.request_pwl_dict("../configurations/cardnames.txt")

            with open("../configurations/cardnames.txt") as word_file:
                self.pwl = set(word.strip() for word in word_file)

            #file used to invoke google cloud visison call
            self.source_file = '../source/source.png'

            # Step 1a :  register callbacks for user interface events and sensors
            self.pb_capture.clicked.connect(self.thread_grab)
            self.pb_live.clicked.connect(self.cb_live)
            self.pb_update.clicked.connect(self.grab_store_analyse_image)

        def play(self):
                try:
                    self.video.captureNextFrame()
                    self.videoFrame.setPixmap(
                        self.video.convertFrame())
                    self.videoFrame.setScaledContents(True)
                except TypeError:
                    print "No video frame"

        # treads:

        def thread_grab(self):
            tGrab = threading.Thread(name="Grab,store and analyse", target=self.grab_store_analyse_image)
            tGrab.daemon = True
            tGrab.start()

        def grab_store_analyse_image(self):

                try:
                    start=time.time()

                    gvision=self.video.grabFrame()  #cropped images

                    # combine both cropped images into one for google cloud vision
                    #gvision = np.concatenate((imgT, imgB),axis=0)  # 380x60

                    #create file to send to gcv
                    cv2.imwrite(self.source_file,gvision)

                    #show file on screen and create file to send to GCV
                    image=QtGui.QPixmap(self.source_file)

                    #run google cloud visison analysis
                    #self.result, self.vertices=run_detect_document(self.source_file)
                    result,self.vertices=image_to_text(self.source_file)

                    #TODO check againts approved card names here and correct
                    #is this a known name ?

                    if result:
                        try:
                            self.result = difflib.get_close_matches(result, self.pwl)[0]#best match is first
                        except IndexError:
                            self.result="no valid match found"
                    else:
                        self.result="no valid cardname found"

                    ## draw box if result exists
                    if self.vertices :
                        # draw the bounding box of text description found
                        self.video.draw_bounding_box(self.vertices)
                        #create cropped bounds for logging =image
                        a, b, c, d = self.vertices
                        # print vertices,self.startX,self.startY
                        intx = a[0]
                        inty = a[1]
                        intwidth = b[0] - a[0]
                        intheight = c[1] - b[1]
                        bounded_result = image.copy(intx, inty, intwidth, intheight)
                        self.imageFrame.setPixmap(bounded_result)  # (png-->qpixmap)
                        # save image record
                        bounded_result.save(("../log_files/{}.jpeg").format(self.result))

                    #show text description that was found
                    self.gcv_result.setText(self.result)

                    #update displays and store result
                    end = time.time() - start
                    self.lcd_update_time.display(end)

                except TypeError:
                    print "No image frame"

        def cb_live(self):
            run_detect_document(self.source_file)

        # Step 3a : Qtimer polling for inputs

        def watchdog(self):
            global toggle
            toggle ^= True
            if toggle:
                self.heartbeat.setEnabled(1)
            else:
                self.heartbeat.setEnabled(0)


    # main program start

     # create user interface MyBinControl

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyCameraControl(dialog)

    dialog.show()

    # setup timers to run heartbeat every 1/2 sec
    timer = QtCore.QTimer()
    timer.timeout.connect(prog.watchdog)
    timer.start(500)

    # regsiter software e-stop
    atexit.register(terminate)

    # start the whole thing
    sys.exit(app.exec_())