import json

from src.utilities.utility_class import UtilityClass
from src.utilities.enums.message_enum import MessageEnum
from src.sdk.rekognition.rekognition_main import RekognitionMain
from http import HTTPStatus


class PurgeCollection:

    def __init__(self):
        pass

    @classmethod
    def purge_collection(cls, active_profile):
        rekognition_main = RekognitionMain()
        rekognition_main.purge_collection(active_profile)

    @classmethod
    def list_collections(cls):
        print('list_collections')
        rekognition_main = RekognitionMain()
        rekognition_main.list_collections()