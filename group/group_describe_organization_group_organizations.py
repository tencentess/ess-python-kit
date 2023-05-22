from tencentcloud.ess.v20201111.models import DescribeOrganizationGroupOrganizationsRequest, UserInfo, Filter, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_describe_flow_templates(operator_user_id, limit, offset):
    """
    查询集团企业列表

    官网文档：https://cloud.tencent.com/document/product/1323/86114

    此API接口用户查询加入集团的成员企业
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeOrganizationGroupOrganizationsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    user_info.ClientIp = "8.8.8.8"
    user_info.Channel = "YUFU"
    req.Operator = user_info

    req.Limit = limit
    req.Offset = offset

    response = client.DescribeOrganizationGroupOrganizations(req)
    return response


if __name__ == '__main__':
    """
    查询集团企业列表调用样例
    """

    try:
        # 需要代发起的子企业的企业id
        _limit = 10
        _offset = 0

        resp = group_describe_flow_templates(Config.operator_user_id, _limit, _offset)
        print(resp)
    except Exception as e:
        print(e)
