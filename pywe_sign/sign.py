# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import copy
import hashlib

from pywe_utils import to_binary, to_text


__all__ = ['format_url', 'calculate_signature', 'check_signature', 'fill_signature', 'jsapi_signature', 'calculate_jsapi_signature', 'check_jsapi_signature', 'fill_jsapi_signature', 'basic_signature', 'calculate_basic_signature', 'calculate_callback_signature', 'check_callback_signature', 'calculate_msg_signature', 'check_msg_signature']


def is_param_has_value(param, ignore_zero=False):
    return param or (not ignore_zero and param == 0)


def format_url(params, api_key=None, ignore_zero=False):
    data = [to_binary('{0}={1}'.format(k, params[k])) for k in sorted(params) if is_param_has_value(params[k], ignore_zero=ignore_zero)]
    if api_key:
        data.append(to_binary('key={0}'.format(api_key)))
    return b'&'.join(data)


# WxPay Relative Signature Algorithm
#   See: https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=4_3

def calculate_signature(params, api_key, ignore_zero=False):
    url = format_url(params, api_key, ignore_zero=ignore_zero)
    return to_text(hashlib.md5(url).hexdigest().upper())


def check_signature(params, api_key, sign=None, sign_key='sign', ignore_zero=False):
    _params = copy.deepcopy(params)
    sign = sign or _params.pop(sign_key, '')
    return sign == calculate_signature(_params, api_key, ignore_zero=ignore_zero)


def fill_signature(params, api_key, sign_key='sign', ignore_zero=False):
    sign = calculate_signature(params, api_key, ignore_zero=ignore_zero)
    params[sign_key] = sign
    return params


# JSAPI Relative Signature Algorithm
#   See: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421141115

def jsapi_signature(params, ignore_zero=False):
    url = format_url(params, ignore_zero=ignore_zero)
    return hashlib.sha1(url).hexdigest()


def calculate_jsapi_signature(params, ignore_zero=False):
    return jsapi_signature(params, ignore_zero=ignore_zero)


def check_jsapi_signature(params, sign=None, sign_key='sign', ignore_zero=False):
    _params = copy.deepcopy(params)
    sign = sign or _params.pop(sign_key, '')
    return sign == jsapi_signature(_params, ignore_zero=ignore_zero)


def fill_jsapi_signature(params, sign_key='sign', ignore_zero=False):
    sign = jsapi_signature(params, ignore_zero=ignore_zero)
    params[sign_key] = sign
    return params


# Callback Relative Signature Algorithm
#   See: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421135319

def basic_signature(data, delimiter=b''):
    str2sign = to_binary(delimiter).join([to_binary(d) for d in sorted(data)])
    return hashlib.sha1(str2sign).hexdigest()


def calculate_basic_signature(data, delimiter=b''):
    return basic_signature(data, delimiter=delimiter)


def calculate_callback_signature(token, timestamp, nonce):
    return basic_signature([token, timestamp, nonce])


def check_callback_signature(token, signature, timestamp, nonce):
    return signature == calculate_callback_signature(token, timestamp, nonce)


def calculate_msg_signature(token, timestamp, nonce, encrypt):
    return basic_signature([token, timestamp, nonce, encrypt])


def check_msg_signature(token, msg_signature, timestamp, nonce, encrypt):
    return msg_signature == calculate_msg_signature(token, timestamp, nonce, encrypt)
