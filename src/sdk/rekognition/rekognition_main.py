import json

import boto3

FACE_COLLECTION_NAME = 'coleccionRostrosAutenticacionBiometrica'


class RekognitionMain:
    client_instance = None

    def __init__(self):
        pass

    @classmethod
    def get_client_instance(cls):
        if cls.client_instance is None:
            cls.client_instance = cls.get_instance_rekognition()
        return cls.client_instance

    @classmethod
    def faces_collection_create_process(cls):
        return cls.faces_collection_create(FACE_COLLECTION_NAME)

    @classmethod
    def get_instance_rekognition(cls):
        return boto3.client('rekognition')

    @classmethod
    def faces_collection_create(cls, collection_name):
        faces_collection_create_resp = cls.get_client_instance().create_collection(
            CollectionId=collection_name
        )
        print('faces_collection_create:', json.dumps(faces_collection_create_resp))
        return faces_collection_create_resp

    @classmethod
    def faces_collection_search(cls, collection_name):
        collection_validate = cls.get_client_instance().describe_collection(
            CollectionId=collection_name
        )
        print('faces_collection_search:', json.dumps(collection_validate))
        return collection_validate

    @classmethod
    def faces_collection_validate(cls, collection_name):
        try:
            collection_validation = cls.faces_collection_search(collection_name)
            return collection_validation and collection_validation.get('CollectionARN')
        finally:
            # TODO
            pass

    @classmethod
    def search_face_in_collection(cls, bucket_path_s3, bucket_name):
        try:
            if cls.faces_collection_validate(FACE_COLLECTION_NAME):
                return cls.get_client_instance().search_faces_by_image(
                    CollectionId=FACE_COLLECTION_NAME,
                    Image={
                        'S3Object': {
                            'Bucket': bucket_path_s3,
                            'Name': bucket_name,
                        }
                    }
                )
            else:
                # TODO agregar excepcion
                pass
        finally:
            pass

    @classmethod
    def add_face_in_collection(cls, bucket_path_s3, bucket_name):
        if cls.faces_collection_validate(FACE_COLLECTION_NAME):
            index_faces_response = cls.get_client_instance().index_faces(
                CollectionId=FACE_COLLECTION_NAME,
                Image={
                    'S3Object': {
                        'Bucket': bucket_path_s3,
                        'Name': bucket_name,
                    }
                },
                ExternalImageId=""
            )
            print('add_face_in_collection:', json.dumps(index_faces_response))
            return index_faces_response
        else:
            cls.faces_collection_create_process()
