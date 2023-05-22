from tencentcloud.ess.v20201111.models import DescribeFlowTemplatesRequest, UserInfo, Filter, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_describe_flow_templates(operator_user_id, template_ids, proxy_organization_id):
    """
    DescribeFlowTemplates 查询模板

    官网文档：https://cloud.tencent.com/document/product/1323/74803

    适用场景：当模板较多或模板中的控件较多时，可以通过查询模板接口更方便的获取自己主体下的模板列表，以及每个模板内的控件信息。
    该接口常用来配合“创建电子文档”接口作为前置的接口使用。
    """

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

    # 需要查询的模板ID列表
    query_filter = Filter()
    query_filter.Key = "template-id"  # 查询过滤条件的Key
    query_filter.Values = template_ids  # 查询过滤条件的Value列表

    # 搜索条件，具体参考Filter结构体。本接口取值：template-id：按照【 模板唯一标识 】进行过滤
    req.Filters = [query_filter]

    response = client.DescribeFlowTemplates(req)
    return response


if __name__ == '__main__':
    """
    查询模板调用样例
    """

    try:
        # 需要代发起的子企业的企业id
        _proxy_organization_id = "********************************"
        _template_ids = ['********************************']

        resp = group_describe_flow_templates(Config.operator_user_id, _template_ids, _proxy_organization_id)
        print(resp)
    except Exception as e:
        print(e)
