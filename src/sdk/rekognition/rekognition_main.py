import json

import botocore.exceptions
import logging
from src.sdk.sdk_general_config import SDKGeneralConfig

FACE_COLLECTION_NAME = 'coleccionRostrosAutenticacionBiometrica'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class RekognitionMain:
    client_instance = None

    def __init__(self):
        pass

    @classmethod
    def list_collections(cls):
        print('RekognitionMain list_collections')
        list_collections_resp = cls.get_client_instance().list_collections(
            MaxResults=123
        )
        print('list_collections_resp:', json.dumps(list_collections_resp))

    @classmethod
    def get_collection_name(cls, active_profile):
        collection_name = '{}_{}'.format(FACE_COLLECTION_NAME, active_profile)
        print('CollectionName: ', collection_name)
        return collection_name

    @classmethod
    def purge_collection(cls, active_profile):
        purge_collection_resp = cls.get_client_instance().delete_collection(
            CollectionId=cls.get_collection_name(active_profile)
        )
        print('purge_collection_resp:', json.dumps(purge_collection_resp))

    @classmethod
    def get_client_instance(cls):
        if cls.client_instance is None:
            cls.client_instance = cls.get_instance_rekognition()
        return cls.client_instance

    @classmethod
    def faces_collection_create_process(cls, collection_name):
        return cls.faces_collection_create(collection_name)

    @classmethod
    def get_instance_rekognition(cls):
        config = SDKGeneralConfig()
        return config.get_instance()

    @classmethod
    def faces_collection_create(cls, collection_name):
        faces_collection_create_resp = cls.get_client_instance().create_collection(
            CollectionId=collection_name
        )
        print('faces_collection_create:', json.dumps(faces_collection_create_resp))
        return faces_collection_create_resp

    @classmethod
    def faces_collection_search(cls, collection_name):
        print('faces_collection_search: 1111 ', collection_name)
        try:
            collection_validate = cls.get_client_instance().describe_collection(
                CollectionId=collection_name
            )
            print('faces_collection_search response:', collection_validate)
            return True
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'ResourceAlreadyExistsException':
                return True
            else:
                return False

    @classmethod
    def search_face_in_collection(cls, bucket_path_s3, bucket_name, active_profile):
        collection_name = cls.get_collection_name(active_profile)
        try:
            if cls.faces_collection_search(collection_name):
                return cls.get_client_instance().search_faces_by_image(
                    CollectionId=collection_name,
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
    def add_face_in_collection(cls, bucket_path_s3, bucket_name, external_id, active_profile):
        collection_name = cls.get_collection_name(active_profile)
        if cls.faces_collection_search(collection_name):
            index_faces_response = cls.get_client_instance().index_faces(
                CollectionId=collection_name,
                Image={
                    'S3Object': {
                        'Bucket': bucket_path_s3,
                        'Name': bucket_name,
                    }
                },ExternalImageId=external_id
            )
            print('add_face_in_collection_response:', json.dumps(index_faces_response))
            return index_faces_response
        else:
            cls.faces_collection_create_process(collection_name)
