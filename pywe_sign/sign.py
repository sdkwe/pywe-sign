# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import copy
import hashlib

from pywe_utils import to_binary, to_text


__all__ = ['format_url', 'calculate_signature', 'check_signature', 'fill_signature', 'jsapi_signature', 'calculate_jsapi_signature', 'check_jsapi_signature', 'fill_jsapi_signature']


def format_url(params, api_key=None):
    data = [to_binary('{0}={1}'.format(k, params[k])) for k in sorted(params) if params[k]]
    if api_key:
        data.append(to_binary('key={0}'.format(api_key)))
    return b'&'.join(data)


# WxPay Relative Signature Algorithm
#   See: https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=4_3

def calculate_signature(params, api_key):
    url = format_url(params, api_key)
    return to_text(hashlib.md5(url).hexdigest().upper())


def check_signature(params, api_key, sign=None):
    _params = copy.deepcopy(params)
    sign = sign or _params.pop('sign', '')
    return sign == calculate_signature(_params, api_key)


def fill_signature(params, api_key):
    sign = calculate_signature(params, api_key)
    params['sign'] = sign
    return params


# JSAPI Relative Signature Algorithm
#   See: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421141115

def jsapi_signature(params):
    url = format_url(params)
    return hashlib.sha1(url).hexdigest()


def calculate_jsapi_signature(params):
    return jsapi_signature(params)


def check_jsapi_signature(params, sign=None):
    _params = copy.deepcopy(params)
    sign = sign or _params.pop('sign', '')
    return sign == jsapi_signature(_params)


def fill_jsapi_signature(params):
    sign = jsapi_signature(params)
    params['sign'] = sign
    return params
