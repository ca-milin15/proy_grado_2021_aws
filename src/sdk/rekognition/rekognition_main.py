import boto3
FACE_COLLECTION_NAME = 'coleccionRostrosAutenticacionBiometrica'


class RekognitionMain:

    client_instance = None

    def __init__(self):
        if self.client_instance is None:
            self.client_instance = self.get_instance_rekognition()

    @classmethod
    def faces_collection_create_process(cls):
        return cls.faces_collection_create(FACE_COLLECTION_NAME)

    @classmethod
    def get_instance_rekognition(cls):
        return boto3.client('rekognition')

    @classmethod
    def faces_collection_create(cls, collection_name):
        return cls.client_instance.create_collection(
            CollectionId=collection_name
        )

    @classmethod
    def search_face_in_collection(cls, image_as_byte, bucket_path_s3, bucket_name):
        return cls.client_instance.search_faces_by_image(
            CollectionId=FACE_COLLECTION_NAME,
            Image={
                'Bytes': image_as_byte,
                'S3Object': {
                    'Bucket': bucket_path_s3,
                    'Name': bucket_name,
                }
            }
        )

    @classmethod
    def add_face_in_collection(cls, image_as_byte, bucket_path_s3, bucket_name):
        return cls.client_instance.index_faces(
            CollectionId=FACE_COLLECTION_NAME,
            Image={
                'Bytes': image_as_byte,
                'S3Object': {
                    'Bucket': bucket_path_s3,
                    'Name': bucket_name,
                }
            }
        )
