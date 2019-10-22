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

    from pywe_sign import calculate_signature, check_signature, fill_signature, jsapi_signature, calculate_jsapi_signature, check_jsapi_signature, fill_jsapi_signature, basic_signature, calculate_basic_signature, calculate_callback_signature, check_callback_signature, calculate_msg_signature, check_msg_signature


Method
======

::

    def format_url(params, api_key=None, ignore_zero=False):

    def calculate_signature(params, api_key, ignore_zero=False):

    def check_signature(params, api_key, sign=None, sign_key='sign', ignore_zero=False):

    def fill_signature(params, api_key, sign_key='sign', ignore_zero=False):

    def jsapi_signature(params, ignore_zero=False):

    def calculate_jsapi_signature(params, ignore_zero=False):

    def check_jsapi_signature(params, sign=None, sign_key='sign', ignore_zero=False):

    def fill_jsapi_signature(params, sign_key='sign', ignore_zero=False):

    def basic_signature(data, delimiter=b''):

    def calculate_basic_signature(data, delimiter=b''):

    def check_callback_signature(token, signature, timestamp, nonce):

    def basic_signature(data, delimiter=b''):

    def calculate_basic_signature(data, delimiter=b''):

    def calculate_callback_signature(token, timestamp, nonce):

    def check_callback_signature(token, signature, timestamp, nonce):

    def calculate_msg_signature(token, timestamp, nonce, encrypt):

    def check_msg_signature(token, msg_signature, timestamp, nonce, encrypt):

