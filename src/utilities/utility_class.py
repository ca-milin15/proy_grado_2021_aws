
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

    @staticmethod
    def get_active_profile(invoked_function_arn):
        print("Lambda function ARN: ", invoked_function_arn)
        url_as_array = invoked_function_arn.split(":")
        profile = url_as_array[len(url_as_array)-1]
        return profile
