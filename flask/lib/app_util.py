'''
Module which provide Utility functions for app .
'''
from flask import jsonify

def get_response_for_message(message_str,response_code):
    '''
    Given a message_str and response_code return json response
    '''
    resp = jsonify({'status': 'error', 'message': message_str})
    resp.status_code = response_code
    return resp
