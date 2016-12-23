# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import copy
import hashlib

import six


__all__ = ['to_text', 'to_binary', 'format_url', 'calculate_signature', 'check_signature']


# Signature Algorithm
#   See: https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=4_3


def to_text(value, encoding='utf-8'):
    """Convert value to unicode, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def to_binary(value, encoding='utf-8'):
    """Convert value to binary string, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return six.binary_type(value)


def format_url(params, api_key=None):
    data = [to_binary('{}={}'.format(k, params[k])) for k in sorted(params) if params[k]]
    if api_key:
        data.append(to_binary('key={}'.format(api_key)))
    return b'&'.join(data)


def calculate_signature(params, api_key):
    url = format_url(params, api_key)
    return to_text(hashlib.md5(url).hexdigest().upper())


def check_signature(params, api_key):
    _params = copy.deepcopy(params)
    sign = _params.pop('sign', '')
    return sign == calculate_signature(_params, api_key)
