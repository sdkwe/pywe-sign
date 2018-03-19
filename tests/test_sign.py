# -*- coding: utf-8 -*-

import copy

from pywe_sign import (basic_signature, calculate_basic_signature, calculate_jsapi_signature, calculate_signature,
                       check_callback_signature, check_jsapi_signature, check_signature, fill_jsapi_signature,
                       fill_signature, jsapi_signature)


class TestSignCommands(object):

    def test_pay_signature_relative(self):
        params = {
            'appid': 'wxd930ea5d5a258f4f',
            'mch_id': 10000100,
            'device_info': 1000,
            'body': 'test',
            'nonce_str': 'ibuaiVcKdpRxkhJA'
        }
        api_key = '192006250b4c09247ec02edce69f6a2d'
        sign = '9A0A8659F005D6984697E2CA0A9CF3B7'
        assert calculate_signature(params, api_key) == sign
        params2 = copy.deepcopy(params)
        params2['sign'] = sign
        assert check_signature(params2, api_key)
        assert check_signature(params, api_key, sign)
        assert fill_signature(params, api_key) == params2

    def test_jsapi_signature_relative(self):
        params = {
            'noncestr': 'Wm3WZYTPz0wzccnW',
            'jsapi_ticket': 'sM4AOVdWfPE4DxkXGEs8VMCPGGVi4C3VM0P37wVUCFvkVAy_90u5h9nbSlYy3-Sl-HhTdfl2fzFy1AOcHKP7qg',
            'timestamp': 1414587457,
            'url': 'http://mp.weixin.qq.com?params=value'
        }
        sign = '0f9de62fce790f9a083d5c99e95740ceb90c27ed'
        assert jsapi_signature(params) == sign
        assert calculate_jsapi_signature(params) == sign
        params2 = copy.deepcopy(params)
        params2['sign'] = sign
        assert check_jsapi_signature(params2)
        assert check_jsapi_signature(params, sign)
        assert fill_jsapi_signature(params) == params2

    def test_callback_signature_relative(self):
        data = ['789', '456', '123']
        sign = 'f7c3bc1d808e04732adf679965ccc34ca7ae3441'
        assert basic_signature(data) == sign
        assert calculate_basic_signature(data) == sign
        assert check_callback_signature('789', sign, '456', '123')
