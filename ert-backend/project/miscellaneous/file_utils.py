import os

import smart_open

from config.settings.base import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME


def upload_filestream_to_s3(filestream, filename, s3_dir):
    try:
        file_ext = filestream.content_type.split('/')[-1]
        file_url = 's3://%s:%s@%s/%s/%s.%s' % (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
                                               AWS_STORAGE_BUCKET_NAME, s3_dir, filename, file_ext)
        with smart_open.open(file_url, 'wb') as fout:
            fout.write(filestream.file.read())
        return {
            'status': True,
            'url': 'https://%s.s3.%s.amazonaws.com/%s/%s.%s' %
                   (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, s3_dir, filename, file_ext)
        }
    except Exception as e:
        print(e)
        return {'status': False}


def delete_file_local(path, filename):
    os.remove(os.path.abspath('media/' + path + '/' + filename))
