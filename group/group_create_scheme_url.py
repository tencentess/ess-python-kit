from tencentcloud.ess.v20201111.models import CreateSchemeUrlRequest, UserInfo, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_create_scheme_url(operator_user_id, flow_id, path_type, proxy_organization_id):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateSchemeUrlRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    req.FlowId = flow_id

    req.PathType = path_type

    response = client.CreateSchemeUrl(req)
    return response


if __name__ == '__main__':

    try:

        _proxy_organization_id = "********************************"

        _flow_id = '********************************'

        _path_type = 1

        resp = group_create_scheme_url(Config.operator_user_id, _flow_id, _path_type, _proxy_organization_id)
        print(resp)
    except Exception as e:
        print(e)
