#!/usr/bin/python
#
# This script uses the AWS Python SDK to set and retreive metadata for objects that 
# have previously been stored in Amazon S3.
# Usage: Supply 3/4 command line arguments.
#   1. Bucket name - the name of the S3 bucket that we want to work in
#   2. Key name - the name of the key within that bucket that we want to show or update metadata for
#   3. Metadata key - the metadata key that we want to print or update a value for
#   4. Metadata value [optional] - if supplied, we will update the specified metadata key with this value
#
# Output:
#   Prints a confirmation message as to whether metadata is being set or retrieved
#   Prints metadata key value pair if retrieving metadataß

import boto
import sys

def main(argv):
    
    # assign Access Key and Secret Key to variables for later use
    access_key = 'ACCESS KEY'
    secret_key = 'SECRET KEY'
    
    # check that we have the correct number of arguements (3 or 4), exit with usage guidance if not
    argc = len(sys.argv)
    if (argc > 5) or (argc < 4): 
        print "Usage: PrintSetMetaData.py <Bucket Name> <Key Name> <Metadata Key> [<Metadata Value>]"
        sys.exit();
        
    # deal with the print case if we have 3 arguments
    if (argc - 1 == 3):
        # we have arguments, so set some meaningful names for them 
        bucket = sys.argv[1]
        key = sys.argv[2]
        mdkey = sys.argv[3]
        print "Getting object metadata for object: " + key + " in bucket: " + bucket
        # create an S3 connection object
        conn = boto.connect_s3(access_key,secret_key)
        # create a bucket object for the bucket specified in the supplied command line argument
        bucket = conn.get_bucket(bucket)
        # create a key object for the specified key
        key = bucket.get_key(key)
        # print the specified meta data key value pair 
        print mdkey + "=" + key.get_metadata(mdkey)
        
    
    # deal with the set case if we have 4 arguments
    if (argc - 1 == 4):
        # we have arguments, so set some meaningful names for them 
        bucket = sys.argv[1]
        key = sys.argv[2]
        mdkey = sys.argv[3]
        mdvalue = sys.argv[4]
        print "Setting object metadata to " + mdkey + "=" + mdvalue + " for object: " + key + " in bucket: " + bucket
        # create an S3 connection object
        conn = boto.connect_s3(access_key,secret_key)
        # create a bucket object for the bucket specified in the supplied command line argument
        bucket = conn.get_bucket(bucket)
        # create a key object for the specified key
        key = bucket.get_key(key)
        # construct a dictionary object containing the metadata key value pair
        metadata = {mdkey:mdvalue}
        # copy the existing key to a new key with the same name, adding the dictionary object containing the metadata 
        key.copy(bucket.name, key.name, metadata, preserve_acl=True)
	

if __name__ == '__main__':
    main(sys.argv[1:])
