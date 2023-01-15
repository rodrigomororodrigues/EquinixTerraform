from boto3.session import Session

# set aws credentials 

ACESS_KEY_ID = 'AKIASZKKVZKPIF7NDHZV'
SECRET_KEY = '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'

session  = Session(aws_access_key_id=ACESS_KEY_ID,aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

bucket = 'equinixbucket'

my_bucket = s3.Bucket(bucket)

for s3_files in my_bucket.objects.all():
    print(s3_files.key)
    
print("Download from S3 ...")

my_bucket.download_file('index.html','./index.html')


print("Downloadedsuccessfully from S3 ...")


import shutil, os
files = ['index.html']
for f in files:
    shutil.copy(f, '/usr/share/nginx/html/')
