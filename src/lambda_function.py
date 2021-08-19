import json

from src.modules.authentication.authentication import Authentication
from src.modules.sign_up.signup import Signup


def lambda_handler(event, context):
    print('event: ', json.dumps(event))
    if event and event.get('operationType') and event.get('objectRequest'):

        if event.get('operationType') == 'SIGNUP':
            signup_main = Signup()
            signup_main.signup_process(event.get('objectRequest'))
            return {
                'statusCode': 200,
                'body': generic_body_response_object(
                    'El codigo de la transacciòn no es valido',
                    'El codigo de la transacciòn no corresponde que las posibles acciones'
                )
            }
        elif event.get('operationType') == 'AUTH':
            auth_main = Authentication()
            auth_main.authentication_process(event.get('objectRequest'))
            return {
                'statusCode': 200,
                'body': generic_body_response_object(
                    'El codigo de la transacciòn no es valido',
                    'El codigo de la transacciòn no corresponde que las posibles acciones'
                )
            }
        else:
            return {
                'statusCode': 400,
                'body': generic_body_response_object(
                    'El codigo de la transacciòn no es valido',
                    'El codigo de la transacciòn no corresponde que las posibles acciones'
                )
            }
    else:
        return {
            'statusCode': 400,
            'body': generic_body_response_object(
                'Error en el payload de la peticion',
                ''
            )
        }


def generic_response_object(code, body_as_json):
    return {
        'statusCode': code,
        'body': body_as_json
    }


def generic_body_response_object(message, reason):
    return {
        'message': message,
        'reason': reason
    }
