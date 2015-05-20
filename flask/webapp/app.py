'''
Customer API - Flask application for below end points
 1. Login - Enables user to login with username and password
 2. User Preference - Persist user preference
 3. Questionnaire - Provides questionnaire data
'''
import os,sys
from flask import Flask, request, g, jsonify, Response
import traceback
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import logger
from config import Config
from app_util import get_response_for_message
from PUCustomerBizComp import PUCustomerBizComp

app = Flask(__name__)
custBizComp = PUCustomerBizComp()

def validate_login_params(params):

        if not any([params[key] if params[key] is not None else None for key in params]):
            message = 'params cannot be empty'
            return get_response_for_message(message,response_code=400)
       # Basic Sanity checking of the arguments
        if 'username' not in params:
                message = 'Missing username argument in post request'
                return get_response_for_message(message,response_code=400)
        elif 'password' not in params:
                message = 'Missing password in post request'
                return get_response_for_message(message,response_code=400)
        username = params['username']
        password = params['password']
        # Check if the username is blank
        if username is not None and username.strip() == '':
            message = 'username cannot be blank or empty'
            resp = jsonify({'status': 'error', 'message': message})
            resp.status_code = 400
            return resp
        username = username.strip()
        password = password.strip()
        resp = jsonify({'status': 'Success', 'message': 'Validation successful'})
        resp.status_code = 200
        return resp
# End point for customer login
@app.route('/customer/login', methods=['POST'])
def login():
    try:
        params = request.get_json()
        resp = validate_login_params(params)
        if resp.status_code == 400 :
            return resp
        username = params['username']
        password = params['password']
        username = username.strip()
        password = password.strip()
        if custBizComp.verifyUserName(username) :
            if custBizComp.verifyUserPwd(username,password) :
               resp = jsonify({'status': 'Success', 'message': "Login successful"})
               resp.status_code = 200
            else:
               resp = jsonify({'status': 'Failed', 'message': "Password didn't match"})
               resp.status_code = 400
        else:
                resp = jsonify({'status': 'Failed', 'message': "Username not found"})
                resp.status_code = 400

        return resp

    except Exception:
        tb = traceback.format_exc()
        logger.customer_logger().fatal("caught exception in %s: %s" % (request.url, tb))

        resp = jsonify({'status': 'error', 'message': 'Internal Server Error'})
        resp.status_code = 500
        return resp

@app.route('/customer/signup', methods=['POST'])
def signup():
    try:
        params = request.get_json()
        validate_login_params(params)
        custBizComp.signup(params)
        resp = jsonify({'status': 'Success', 'message': 'Signup successful'})
        resp.status_code = 200
        return resp
    except Exception:
        tb = traceback.format_exc()
        logger.customer_logger().fatal("caught exception in %s: %s" % (request.url, tb))
        resp = jsonify({'status': 'error', 'message': 'Internal Server Error'})
        resp.status_code = 500
        return resp


if __name__ == '__main__':
    app.run(debug=True)
