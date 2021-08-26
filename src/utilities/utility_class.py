
class UtilityClass:

    def __init__(self):
        pass

    @staticmethod
    def generic_response_object(code, body_as_json):
        return {
            'statusCode': code,
            'body': body_as_json
        }

    @staticmethod
    def generic_body_response_object(message, reason):
        return {
            'message': message,
            'reason': reason
        }
