#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#https://cloud.google.com/vision/docs/reference/libraries

# run : gcloud auth application-default login

#https://cloud.google.com/vision/docs/detecting-labels


#https://cloud.google.com/vision/docs/detecting-text

# install grpc-google-cloud-vision and ply

# export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/my_private_access_key.json


# [START vision_quickstart]
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision




def run_detect_document():
    """Detects document features in an image."""
    vision_client = vision.Client(project="SightMachine")

    image = vision_client.image(source_uri='gs://magicworx/M10/ant\ queen.hq.jpg')

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

def run_detect_text():
    """Detects text in the file."""
    # Instantiates a client
    vision_client = vision.Client(project="SightMachine")

    #google cloud console command
    # use \ {sapce} to denote a space in the anem
    image = vision_client.image(source_uri='gs://magicworx/M10/ant\ queen.hq.jpg')

    texts = image.detect_text()
    print('Texts:')

    for text in texts:

        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))

def run_quickstart():

    vision_client = vision.Client(project="SightMachine")

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'mcard.jpg')



    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    document = image.detect_full_text()

    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print('Document:')

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

    texts = image.detect_text()
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                     for bound in text.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/my_private_access_key.json"
    print os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    run_quickstart()
