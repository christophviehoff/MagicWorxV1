#!/usr/bin/python


# https://cloud.google.com/storage/docs/xml-api/gspythonlibrary#setup

# use the command gsutil config -e and reference service account credentials with a .boto file.

import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time
# URI scheme for Cloud Storage.


#Uniform Resource Identifier (URI) is a string of characters used to identify a resource.
BUCKET= 'magicworx'
OTHER_BUCKET='mtgimages'
GOOGLE_STORAGE = 'gs'
header_values = {"x-goog-project-id": '791399645015'}


uri = boto.storage_uri('', GOOGLE_STORAGE)
# If the default project is defined, call get_all_buckets() without arguments.
for bucket in uri.get_all_buckets(headers=header_values):
  print bucket.name



# URI scheme for accessing local files.
LOCAL_FILE = 'file'
i=0
uri = boto.storage_uri(BUCKET, GOOGLE_STORAGE)
for obj in uri.get_bucket():
  #print '%s://%s/%s' % (uri.scheme, uri.bucket_name, obj.name)
  print obj.name.strip('0123456789/VM')
  i+=1
  #print '  "%s"' % obj.get_contents_as_string()

print i

#find the files and copy them to home and other bucket


dest_dir = os.getenv('HOME')
for filename in ('cancel.hq.jpg', 'clone.hq.jpg'):
  src_uri = boto.storage_uri(
      BUCKET + '/M10/' + filename, GOOGLE_STORAGE)

  # Create a file-like object for holding the object contents.
  object_contents = StringIO.StringIO()

  # The unintuitively-named get_file() doesn't return the object
  # contents; instead, it actually writes the contents to
  # object_contents.
  src_uri.get_key().get_file(object_contents)

  local_dst_uri = boto.storage_uri(
      os.path.join(dest_dir, filename), LOCAL_FILE)

  bucket_dst_uri = boto.storage_uri(
      OTHER_BUCKET + '/' + filename, GOOGLE_STORAGE)

  for dst_uri in (local_dst_uri, bucket_dst_uri):
    object_contents.seek(0)
    dst_uri.new_key().set_contents_from_file(object_contents)

  object_contents.close()