from flask import Flask, jsonify, request
from os import environ
from functools import wraps
import jwt

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
        #  --> Checking for a Bearer Token here
       if 'Authorization' in request.headers:
           auth_header = request.headers['Authorization'].split()
           token = auth_header[1]
           print("token is ", token)
        
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           data = jwt.decode(str(token), environ.get('JWT_SECRET'), "HS256")
           current_user = data['email']
       except:
           return jsonify({'message': 'token is invalid'})
       return f(current_user, *args, **kwargs)
   return decorator