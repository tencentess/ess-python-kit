from tencentcloud.ess.v20201111.models import DescribeFlowTemplatesRequest, UserInfo, Filter, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_describe_flow_templates(operator_user_id, template_ids, proxy_organization_id):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFlowTemplatesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    query_filter = Filter()
    query_filter.Key = "template-id"  # 查询过滤条件的Key
    query_filter.Values = template_ids  # 查询过滤条件的Value列表

    req.Filters = [query_filter]

    response = client.DescribeFlowTemplates(req)
    return response


if __name__ == '__main__':
    """
    查询模板调用样例
    """

    try:
        _proxy_organization_id = "********************************"
        _template_ids = ['********************************']

        resp = group_describe_flow_templates(Config.operator_user_id, _template_ids, _proxy_organization_id)
        print(resp)
    except Exception as e:
        print(e)
