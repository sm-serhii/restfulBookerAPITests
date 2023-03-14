import json

from requests import Response

""" List of checking """


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        positive_result = f"{response.status_code} 'Expected'"
        negative_result = f"{response.status_code} 'Error'"
        if response.status_code == status_code:
            print(positive_result)
        else:
            print(negative_result)

    @staticmethod
    def check_response_json(response: Response, expected_value):
        response = json.loads(response.text)
        assert list(response) == expected_value
        positive_result = f"Successfully: response contain {expected_value}"
        negative_result = f"Unsuccessfully: response does not contain {expected_value}"
        if expected_value == list(response):
            print(positive_result)
        else:
            print(negative_result)

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert expected_value == check_info
        positive_result = f"Successfully: response contain '{field_name}' with '{expected_value}'"
        negative_result = f"Unsuccessfully: response does not contain '{field_name}' with '{expected_value}'"
        if expected_value == check_info:
            print(positive_result)
        else:
            print(negative_result)

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        positive_result = f"Successfully: response contain '{field_name}' with '{search_word}'"
        negative_result = f"Unsuccessfully: response does not contain '{field_name}' with '{search_word}'"
        if search_word in check_info:
            print(positive_result)
        else:
            print(negative_result)
