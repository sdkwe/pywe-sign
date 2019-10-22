=========
pywe-sign
=========

Wechat Sign Module for Python.

Installation
============

::

    pip install pywe-sign


Usage
=====

::

<<<<<<< HEAD
    from pywe_sign import calculate_signature, check_signature, fill_signature, jsapi_signature, calculate_jsapi_signature, check_jsapi_signature, fill_jsapi_signature, basic_signature, calculate_basic_signature, calculate_callback_signature, check_callback_signature, calculate_msg_signature, check_msg_signature
=======
    from pywe_sign import calculate_signature, check_signature, fill_signature, jsapi_signature, calculate_jsapi_signature, check_jsapi_signature, fill_jsapi_signature, basic_signature, calculate_basic_signature, check_callback_signature
>>>>>>> f350ba9271d3f9f189dced2c0a0d635ebe937599


Method
======

::

    def calculate_signature(params, api_key):

    def check_signature(params, api_key, sign=None, sign_key='sign'):

    def fill_signature(params, api_key, sign_key='sign'):

    def jsapi_signature(params):

    def calculate_jsapi_signature(params):

    def check_jsapi_signature(params, sign=None, sign_key='sign'):

    def fill_jsapi_signature(params, sign_key='sign'):

    def basic_signature(data, delimiter=b''):

    def calculate_basic_signature(data, delimiter=b''):

    def check_callback_signature(token, signature, timestamp, nonce):

    def basic_signature(data, delimiter=b''):

    def calculate_basic_signature(data, delimiter=b''):

    def calculate_callback_signature(token, timestamp, nonce):

    def check_callback_signature(token, signature, timestamp, nonce):

    def calculate_msg_signature(token, timestamp, nonce, encrypt):

    def check_msg_signature(token, msg_signature, timestamp, nonce, encrypt):

