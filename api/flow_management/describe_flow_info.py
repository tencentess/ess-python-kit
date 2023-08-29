from tencentcloud.ess.v20201111.models import DescribeFlowInfoRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_flow_info(operator_user_id, flow_ids):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFlowInfoRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FlowIds = flow_ids

    response = client.DescribeFlowInfo(req)
    return response


if __name__ == '__main__':
    """
    查询流程摘要调用样例
    """

    try:
        _flow_ids = ['********************************']

        resp = describe_flow_info(Config.operator_user_id, _flow_ids)
        print(resp)
    except Exception as e:
        print(e)
