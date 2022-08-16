from tencentcloud.ess.v20201111.models import DescribeFlowBriefsRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_flow_briefs(operator_user_id, flow_ids):
    """
    查询流程摘要
    适用场景：可用于主动查询某个合同流程的签署状态信息。可以配合回调通知使用。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFlowBriefsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 需要查询的流程ID列表
    req.FlowIds = flow_ids

    response = client.DescribeFlowBriefs(req)
    return response


if __name__ == '__main__':
    """
    查询流程摘要调用样例
    """

    try:
        # 需要查询的流程ID列表
        _flow_ids = ['********************************']

        resp = describe_flow_briefs(Config.operator_user_id, _flow_ids)
        print(resp)
    except Exception as e:
        print(e)
