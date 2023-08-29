from tencentcloud.ess.v20201111.models import DescribeOrganizationSealsRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_organization_seals(operator_user_id, limit):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeOrganizationSealsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.Limit = limit

    response = client.DescribeOrganizationSeals(req)
    return response


if __name__ == '__main__':
    """
    查询模板调用样例
    """

    try:
        _limit = 10

        resp = describe_organization_seals(Config.operator_user_id, _limit)
        print(resp)
    except Exception as e:
        print(e)
