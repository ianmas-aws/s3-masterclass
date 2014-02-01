#!/usr/bin/python
#
# This script uses the AWS Python SDK to generate time-limited expiring URLs for objects
# that have previously been stored in Amazon S3.
#
# Usage: Supply three command line arguments.
#   1. Bucket Name - the name of the S3 bucket where the object is stored. 
#       Note that the bucket does NOT need to be publically accessible
#   2. Key - the key for the object that you wish to create an expiring link for
#   3. Expires - the time in seconds that the link will remain valid for
# Output: 
#   Line 1 - confirmation of the input arguments
#   Line 2 - the signed time-limited URL that provides access to the requested object
#
# based on a code example from Ric Harvey from ningeered.co.uk 


import boto
import sys

def main(argv):
    
    # check that we have the correct number of arguements (3), exit with usage guidance if not
    argc = len(sys.argv)

    # assign Access Key and Secret Key to variables for later use
    
    access_key = 'ACCESS KEY'
    secret_key = 'SECRET KEY'

    if argc != 4: 
        print "Usage: CreateExpiringLink.py <Bucket Name> <Key Name> <Expiry In Seconds>"
        sys.exit();

    # we have arguments, so set some meaningful names for them 
    bucket = sys.argv[1]
    key = sys.argv[2]
    expires = int(sys.argv[3])

    # print arguments 
    print "bucket: %s, key: %s, expires in (seconds): %s" % (bucket, key, expires)

    # create an S3 connection object
    S3CONN = boto.connect_s3(access_key,secret_key)

    # generate and print the time-limited URL, a https address is provided by default
    print "Signed URL: ", S3CONN.generate_url(expires, 'GET', bucket=bucket, key=key)

if __name__ == '__main__':
    main(sys.argv[1:])
    

