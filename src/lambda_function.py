import json

from src.utilities.utility_class import UtilityClass
from src.modules.authentication.authentication import Authentication
from src.modules.sign_up.signup import Signup
from src.utilities.enums.message_enum import MessageEnum
from src.utilities.enums.operation_type import OperationType

from http import HTTPStatus


def lambda_handler(event, context):
    print('event: ', json.dumps(event))
    if event and event.get('operationType') and event.get('objectRequest'):

        if event.get('operationType') == OperationType.SIGNUP_OPERATION.value:
            signup_main = Signup()
            return signup_main.signup_process(event.get('objectRequest'))
        elif event.get('operationType') == OperationType.AUTH_OPERATION.value:
            auth_main = Authentication()
            return auth_main.authentication_process(event.get('objectRequest'))
        else:
            return UtilityClass.generic_response_object(
                HTTPStatus.BAD_REQUEST,
                UtilityClass.generic_body_response_object(
                    MessageEnum.ACTION_REQUEST_MESSAGE_NOT_FOUND.value,
                    MessageEnum.ACTION_REQUEST_REASON_NOT_FOUND.value
                )
            )
    else:
        return UtilityClass.generic_response_object(
            HTTPStatus.BAD_REQUEST,
            UtilityClass.generic_body_response_object(
                MessageEnum.PAYLOAD_REQUEST_MESSAGE_NOT_FOUND.value,
                MessageEnum.PAYLOAD_REQUEST_REASON_NOT_FOUND.value
            )
        )
