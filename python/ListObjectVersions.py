#!/usr/bin/python
#
# This script uses the AWS Python SDK to list the versions of the objects in a specific S3 bucket.

import boto
import sys

def main(argv):
 
    # assign Access Key and Secret Key to variables for later use
    access_key = 'ACCESS KEY'
    secret_key = 'SECRET KEY'
    
    # check that we have the correct number of arguements (1), exit with usage guidance if not
    argc = len(sys.argv)
    if argc != 2: 
        print "Usage: ListObjectVersions.py <Bucket Name>"
        sys.exit();

    # we have 1 argument, so set a meaningful names for it 
    bucketname = sys.argv[1]

    # create an S3 connection object
    conn = boto.connect_s3(access_key,secret_key)
    
    # create a bucket object for the bucket specified in the supplied command line argument
    bucket = conn.get_bucket(bucketname)

    # create a list of the versons
    versions = bucket.list_versions()
    
    #iterate over the versions
    for version in versions:
            # format the string formatted timestamp to Date Time
            Timestamp = version.last_modified.split('.')[0].split('T')[0] + ' ' + version.last_modified.split('.')[0].split('T')[1]
            # print the version name, version id and the reformated timestamp
            print version.name + ' : ' + version.version_id + ' : ' + Timestamp

if __name__ == '__main__':
    main(sys.argv[1:])
    