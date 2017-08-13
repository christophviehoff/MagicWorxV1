"""
Google Vision API Tutorial with a Raspberry Pi and Raspberry Pi Camera.  See more about it here:  https://www.dexterindustries.com/howto/use-google-cloud-vision-on-the-raspberry-pi/
Use Google Cloud Vision on the Raspberry Pi to take a picture with the Raspberry Pi Camera and classify it with the Google Cloud Vision API.   First, we'll walk you through setting up the Google Cloud Platform.  Next, we will use the Raspberry Pi Camera to take a picture of an object, and then use the Raspberry Pi to upload the picture taken to Google Cloud.  We can analyze the picture and return labels (what's going on in the picture), logos (company logos that are in the picture) and faces.
This script uses the Vision API's label detection capabilities to find a label
based on an image's content.
"""

import argparse
import base64
import picamera
import json
# requires export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/SightMachine-f74a1bee6d38.json"
# to work properly


from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('titlecrop.PNG')

def main():
    #takephoto() # First take a picture
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)
    images = {}


    with open('title_crop.png', 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 10
                }]
            }]
        })


        responses = service_request.execute()
        #
        #  print json.dumps(response, indent=1, sort_keys=True)	#Print it out and make it somewhat pretty.
        #print responses['responses']

        ocr_response = []
        for response in responses['responses']:
            if 'fullTextAnnotation' in response:
                ocr_response= response['fullTextAnnotation']
            else:
                ocr_response = []

        #drill down to the fisrt textAnnotation element, description filed

        #print json.dumps(text_response,indent=1,sort_keys=True)

        print ocr_response['text']

        #y coordinate of bounding box
        print ocr_response['pages'][0]['blocks'][0]['boundingBox']['vertices'][0]['y']
        print ocr_response['pages'][0]['blocks'][0]['boundingBox']['vertices'][0]['x']

        '''
        # access x coordinate of bouinding polygon
        #print text_response[0]['boundingPoly']['vertices'][0]['x']

        x1=text_response[0]['boundingPoly']['vertices'][0]['x']
        y1=text_response[0]['boundingPoly']['vertices'][0]['y']

        print x1,y1

        x2 = text_response[0]['boundingPoly']['vertices'][1]['x']
        y2 = text_response[0]['boundingPoly']['vertices'][1]['y']

        print x2,y2
        '''




if __name__ == '__main__':

    main()