import json

from src.utilities.utility_class import UtilityClass
from src.utilities.enums.message_enum import MessageEnum
from src.sdk.rekognition.rekognition_main import RekognitionMain
from http import HTTPStatus


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
        if add_face_response and add_face_response.get('FaceRecords') and len(add_face_response.get('FaceRecords')) > 0:
            return UtilityClass.generic_response_object(
                HTTPStatus.OK,
                {
                    'faceId': add_face_response.get('FaceRecords')[0].get('Face').get('FaceId')
                }
            )
        else:
            return UtilityClass.generic_response_object(
                HTTPStatus.BAD_REQUEST,
                UtilityClass.generic_body_response_object(
                    MessageEnum.SIGNUP_PROCESS_MESSAGE_BAD_REQUEST.value,
                    MessageEnum.SIGNUP_PROCESS_REASON_BAD_REQUEST.value
                )
            )
