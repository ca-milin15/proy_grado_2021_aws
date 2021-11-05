import json

from src.utilities.utility_class import UtilityClass
from src.utilities.enums.message_enum import MessageEnum
from src.sdk.rekognition.rekognition_main import RekognitionMain
from http import HTTPStatus


class Authentication:

    def __init__(self):
        pass

    @classmethod
    def authentication_process(cls, auth_object):
        print('authentication_process: ', json.dumps(auth_object))
        rekognition_main = RekognitionMain()
        search_response = rekognition_main.search_face_in_collection(
            auth_object.get('imageS3Bucket'),
            auth_object.get('imageBucketName')
        )
        print('search_response:', json.dumps(search_response))
        if search_response.get('FaceMatches') and len(search_response.get('FaceMatches')) > 0:
            result = list(map(lambda object:
                {
                    'similarity' : object.get('Similarity'),
                    'face': {
                        'faceId': object.get('Face').get('FaceId'),
                        'imageId': object.get('Face').get('ImageId'),
                        'externalImageId': object.get('Face').get('ExternalImageId'),
                        'confidence': object.get('Face').get('Confidence')
                    }
                },
            search_response.get('FaceMatches')
            ))
            print('result:', json.dumps(result))
            return UtilityClass.generic_response_object(
                HTTPStatus.OK,
                {
                    'faceMatches': result
                }
            )
        else:
            return UtilityClass.generic_response_object(
                HTTPStatus.NOT_FOUND,
                UtilityClass.generic_body_response_object(
                    MessageEnum.FACE_SEARCH_MESSAGE_NOT_FOUND.value,
                    MessageEnum.FACE_SEARCH_REASON_NOT_FOUND.value
                )
            )
