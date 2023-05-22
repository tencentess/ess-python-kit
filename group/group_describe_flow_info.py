from tencentcloud.ess.v20201111.models import DescribeFlowInfoRequest, UserInfo, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_describe_flow_info(operator_user_id, flow_ids, proxy_organization_id):
    """
    DescribeFlowInfo 查询合同详情

    官网文档：https://cloud.tencent.com/document/product/1323/80032

    查询合同详情
    适用场景：可用于主动查询某个合同详情信息。

    tips: 如果仅需查询合同摘要，需要使用查询合同摘要接口 https://cloud.tencent.com/document/product/1323/70358
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFlowInfoRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    # 需要查询的流程ID列表
    req.FlowIds = flow_ids

    response = client.DescribeFlowInfo(req)
    return response


if __name__ == '__main__':
    """
     主企业代子企业查询合同信息的使用样例
     注意：使用集团代发起功能，需要主企业和子企业均已加入集团，并且主企业OperatorUserId对应人员被赋予了对应操作权限
    """

    try:
        # 需要代发起的子企业的企业id
        _proxy_organization_id = "********************************"
        # 需要查询的流程ID列表
        _flow_ids = ['********************************']

        resp = group_describe_flow_info(Config.operator_user_id, _flow_ids, _proxy_organization_id)
        print(resp)
    except Exception as e:
        print(e)
