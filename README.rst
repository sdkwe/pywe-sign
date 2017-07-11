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

    from pywe_sign import calculate_signature, check_signature, fill_signature, jsapi_signature, calculate_jsapi_signature, check_jsapi_signature, fill_jsapi_signature


Method
======

::

    def calculate_signature(params, api_key):

    def check_signature(params, api_key, sign=None):

    def fill_signature(params, api_key):

    def jsapi_signature(params):

    def calculate_jsapi_signature(params):

    def check_jsapi_signature(params, sign=None):

    def fill_jsapi_signature(params):

