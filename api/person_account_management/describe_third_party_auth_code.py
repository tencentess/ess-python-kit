from tencentcloud.ess.v20201111.models import DescribeThirdPartyAuthCodeRequest, UserInfo, Filter

from api.common import get_client_instance
from config import Config


def describe_third_party_auth_code(operator_user_id, auth_code):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeThirdPartyAuthCodeRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.AuthCode = auth_code

    response = client.DescribeThirdPartyAuthCode(req)
    return response


if __name__ == '__main__':

    try:
        auth_code = '********************************'

        resp = describe_third_party_auth_code(Config.operator_user_id, auth_code)
        print(resp)
    except Exception as e:
        print(e)
