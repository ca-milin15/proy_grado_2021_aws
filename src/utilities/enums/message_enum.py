from enum import Enum


class MessageEnum(Enum):
    FACE_SEARCH_MESSAGE_NOT_FOUND = 'El rostro enviado no se encontró.'
    FACE_SEARCH_REASON_NOT_FOUND = 'Es posible que el rostro no se haya registrado en el sistema.'
    SIGNUP_PROCESS_MESSAGE_BAD_REQUEST = 'Ha ocurrido un error intentando registrar el rostro en el sistema.'
    SIGNUP_PROCESS_REASON_BAD_REQUEST = \
        'Posiblemente haya ocurrido un error interno en el proceso. Comunicarse con el proveedor.'
    ACTION_REQUEST_MESSAGE_NOT_FOUND = 'Ha ocurrido un error en la acción a realizar.'
    ACTION_REQUEST_REASON_NOT_FOUND = \
        'Posiblemente haya ocurrido un error interno en el proceso. Comunicarse con el proveedor.'
    PAYLOAD_REQUEST_MESSAGE_NOT_FOUND = 'Ha ocurrido un error en el cuerpo de la petición.'
    PAYLOAD_REQUEST_REASON_NOT_FOUND = \
        'Posiblemente haya ocurrido un error interno en el proceso. Comunicarse con el proveedor.'
    AUTHENTICATION_FAILED = 'No se llevo a cabo el proceso de auteticacion exitosamente.'
    AUTHENTICATION_FAILED_REASON = \
        'El usuario no tiene registrado datios biometricos en el sistema.'


