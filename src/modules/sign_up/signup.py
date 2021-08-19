import json

from src.sdk.rekognition.rekognition_main import RekognitionMain


class Signup:

    def __init__(self):
        pass

    @classmethod
    def signup_process(cls, signup_object):
        print('signup_process: ', json.dumps(signup_object))
        rekognition_main = RekognitionMain()
        add_face_response = rekognition_main.add_face_in_collection(
            signup_object.get('imageS3Bucket'),
            signup_object.get('imageBucketName')
        )
        return add_face_response
