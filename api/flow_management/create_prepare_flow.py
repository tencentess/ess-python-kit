from tencentcloud.ess.v20201111.models import CreatePrepareFlowRequest, UserInfo, FlowCreateApprover

from api.common import get_client_instance
from config import Config


def create_prepare_flow(operator_user_id, flow_name, resource_id, approvers):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreatePrepareFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程参与者信息
    req.Approvers = approvers

    req.FlowName = flow_name

    req.ResourceId = resource_id

    response = client.CreatePrepareFlow(req)
    return response


if __name__ == '__main__':
    """
    创建快速发起流程调用样例
    """

    try:
        _flow_name = '快速发起流程'
        _resource_id = '******************'

        # 签署流程参与者信息
        _approvers = []

        # 个人签署方
        approver = FlowCreateApprover()

        approver.ApproverType(1)

        approver.ApproverName("********************************")

        approver.ApproverMobile("********************************")

        _approvers.append(approver)

        resp = create_prepare_flow(Config.operator_user_id, _flow_name, _resource_id, _approvers)
        print(resp)
    except Exception as e:
        print(e)
