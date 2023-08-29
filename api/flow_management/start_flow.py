from tencentcloud.ess.v20201111.models import StartFlowRequest, UserInfo

from api.common import get_client_instance
from config import Config


def start_flow(operator_user_id, flow_id):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = StartFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FlowId = flow_id

    response = client.StartFlow(req)
    return response


if __name__ == '__main__':
    """
    发起流程调用样例
    """

    try:
        _flow_id = '********************************'

        resp = start_flow(Config.operator_user_id, _flow_id)
        print(resp)
    except Exception as e:
        print(e)
