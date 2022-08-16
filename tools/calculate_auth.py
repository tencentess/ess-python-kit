import hashlib
import hmac
import sys
import time

SECRET_ID = "****"  # 腾讯云secret_id
SECRET_KEY = "****"  # 腾讯云secret_key


# 获取签名Authorization请求头
def calculate_auth(host, method, uri, querystring, content_type, service, date, payload):

    # 1.获取规范请求串
    canonical_request = get_canonical_request(method, uri, content_type, host, querystring, payload)

    # 2.拼接待签名字符串
    algorithm = 'TC3-HMAC-SHA256'  # 签名算法
    credential_scope = date + '/' + service + '/tc3_request'  # 认证范围
    if sys.version_info[0] == 3:
        canonical_request = canonical_request.encode("utf8")
    digest = hashlib.sha256(canonical_request).hexdigest()  # 规范请求串哈希值
    str2sign = '%s\n%s\n%s\n%s' % (algorithm, date, credential_scope, digest)  # 待签名串

    # 3.计算签名
    signature = sign(date, service, str2sign)

    # 4.拼接Authorization请求头
    auth = "TC3-HMAC-SHA256 Credential=%s/%s/%s/tc3_request, SignedHeaders=content-type;host, Signature=%s" % (
        SECRET_ID, date, service, signature)
    return auth


# 生成规范请求串
def get_canonical_request(method, uri, content_type, host, querystring, payload):
    canonical_querystring = ''
    if method == "GET":
        canonical_querystring = querystring
    payload_hash = ""
    if method == "POST":
        if sys.version_info[0] == 3 and isinstance(payload, type("")):
            payload = payload.encode("utf8")
        payload_hash = hashlib.sha256(payload).hexdigest()

    signed_headers = 'content-type;host'
    canonical_headers = 'content-type:%s\nhost:%s\n' % (content_type, host)

    canonical_request = '%s\n%s\n%s\n%s\n%s\n%s' % (
        method, uri, canonical_querystring, canonical_headers, signed_headers, payload_hash)
    return canonical_request


# 计算鉴权签名
def sign(date, service, str2sign):
    signing_key = get_signature_key(SECRET_KEY, date, service)
    signature = hmac_sha256(signing_key, str2sign).hexdigest()
    return signature


# 获取签名key
def get_signature_key(key, date, service):
    k_date = hmac_sha256(('TC3' + key).encode('utf-8'), date)
    k_service = hmac_sha256(k_date.digest(), service)
    k_signing = hmac_sha256(k_service.digest(), 'tc3_request')
    return k_signing.digest()


# 加密签名
def hmac_sha256(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256)


if __name__ == '__main__':
    test_host = 'ess.tencentcloudapi.com'
    test_method = 'POST'
    test_uri = '/'
    test_querystring = ''
    test_content_type = 'application/json'
    test_payload = '{"UserId": "123"}'
    test_service = 'ess'
    test_date = str(int(time.time()))

    auth_header = calculate_auth(
        test_host, test_method, test_uri, test_querystring, test_content_type, test_service, test_date, test_payload)
    print(auth_header)
