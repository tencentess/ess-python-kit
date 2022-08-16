from tencentcloud.ess.v20201111.ess_client import EssClient
from tencentcloud.common.credential import Credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def get_client_instance(secret_id, secret_key, endpoint):
    """
    构造客户端调用实例
    """

    # 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    cred = Credential(secret_id, secret_key)

    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    http_profile = HttpProfile()
    http_profile.reqMethod = "POST"  # post请求(默认为post请求)
    http_profile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    http_profile.endpoint = endpoint  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    client_profile = ClientProfile()
    client_profile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    client_profile.unsignedPayload = False
    client_profile.httpProfile = http_profile

    client = EssClient(cred, "ap-guangzhou", client_profile)

    return client
