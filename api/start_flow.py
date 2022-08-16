from tencentcloud.ess.v20201111.models import StartFlowRequest, UserInfo

from api.common import get_client_instance
from config import Config


def start_flow(operator_user_id, flow_id):
    """
    此接口用于发起流程
    适用场景：见创建签署流程接口。
    注：该接口是“创建电子文档”接口的后置接口，用于激活包含完整合同信息（模板及内容信息）的流程。激活后的流程就是一份待签署的电子合同。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = StartFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程编号，由CreateFlow接口返回
    req.FlowId = flow_id

    response = client.StartFlow(req)
    return response


if __name__ == '__main__':
    """
    发起流程调用样例
    """

    try:
        # 签署流程编号，由CreateFlow接口返回
        _flow_id = '********************************'

        resp = start_flow(Config.operator_user_id, _flow_id)
        print(resp)
    except Exception as e:
        print(e)
