from enum import Enum


class OperationType(Enum):
    SIGNUP_OPERATION = 'SIGNUP'
    AUTH_OPERATION = 'AUTH'
    DELETE_COLLECTION = 'PURGE'
    LIST_COLLECTIONS = 'LIST'
