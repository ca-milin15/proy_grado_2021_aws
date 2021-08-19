import json

from src.sdk.rekognition.rekognition_main import RekognitionMain


class Authentication:

    def __init__(self):
        pass

    """
    {
        'SearchedFaceBoundingBox': {
            'Width': ...,
            'Height': ...,
            'Left': ...,
            'Top': ...
        },
        'SearchedFaceConfidence': ...,
        'FaceMatches': [
            {
                'Similarity': ...,
                'Face': {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                }
            },
        ],
        'FaceModelVersion': 'string'
    }
    """
    @classmethod
    def authentication_process(cls, auth_object):
        print('authentication_process: ', json.dumps(auth_object))
        rekognition_main = RekognitionMain()
        search_response = rekognition_main.search_face_in_collection(
            auth_object.get('imageS3Bucket'),
            auth_object.get('imageBucketName')
        )
        return search_response.get('SearchedFaceConfidence')
