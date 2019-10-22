# -*- coding: utf-8 -*-

import copy

from pywe_sign import (basic_signature, calculate_basic_signature, calculate_callback_signature,
                       calculate_jsapi_signature, calculate_msg_signature, calculate_signature,
                       check_callback_signature, check_jsapi_signature, check_msg_signature, check_signature,
                       fill_jsapi_signature, fill_signature, jsapi_signature)


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
        token = '789'
        timestamp = '456'
        nonce = '123'
        sign = 'f7c3bc1d808e04732adf679965ccc34ca7ae3441'
        assert basic_signature([token, timestamp, nonce]) == sign
        assert calculate_basic_signature([token, timestamp, nonce]) == sign
        assert calculate_callback_signature(token, timestamp, nonce) == sign
        assert check_callback_signature(token, sign, timestamp, nonce)

    def test_msg_signature_relative(self):
        token = 'spamtest'
        msg_signature = '5d197aaffba7e9b25a30732f161a50dee96bd5fa'
        timestamp = '1409735669'
        nonce = '1320562132'
        encrypt = 'hyzAe4OzmOMbd6TvGdIOO6uBmdJoD0Fk53REIHvxYtJlE2B655HuD0m8KUePWB3+LrPXo87wzQ1QLvbeUgmBM4x6F8PGHQHFVAFmOD2LdJF9FrXpbUAh0B5GIItb52sn896wVsMSHGuPE328HnRGBcrS7C41IzDWyWNlZkyyXwon8T332jisa+h6tEDYsVticbSnyU8dKOIbgU6ux5VTjg3yt+WGzjlpKn6NPhRjpA912xMezR4kw6KWwMrCVKSVCZciVGCgavjIQ6X8tCOp3yZbGpy0VxpAe+77TszTfRd5RJSVO/HTnifJpXgCSUdUue1v6h0EIBYYI1BD1DlD+C0CR8e6OewpusjZ4uBl9FyJvnhvQl+q5rv1ixrcpCumEPo5MJSgM9ehVsNPfUM669WuMyVWQLCzpu9GhglF2PE='
        assert basic_signature([token, timestamp, nonce, encrypt]) == msg_signature
        assert calculate_basic_signature([token, timestamp, nonce, encrypt]) == msg_signature
        assert calculate_msg_signature(token, timestamp, nonce, encrypt) == msg_signature
        assert check_msg_signature(token, msg_signature, timestamp, nonce, encrypt)
