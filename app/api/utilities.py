from http import client as httplib
from flask import jsonify, make_response



def get_post_data(request, required_fields=None):
    """
    This is a common method to get and validate the post request data
    """
    is_bad_request = True
    if request.content_type == 'application/json':
        json_data = request.get_json()

    if required_fields:
        if not json_data:
            return is_bad_request, "POST request data is required."

        for key in required_fields:
            if json_data.get(key) == None:
                return is_bad_request, f"{key} is required."

    is_bad_request = False
    return is_bad_request, json_data


def bad_request(error):
    return make_response(
        jsonify({"Error": str(error)}), httplib.BAD_REQUEST
    )
