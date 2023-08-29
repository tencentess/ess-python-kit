import time

from tencentcloud.ess.v20201111.models import CreateFlowRequest, UserInfo, FlowCreateApprover

from api.common import get_client_instance
from config import Config


def create_flow(operator_user_id, flow_name, approvers):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.Approvers = approvers

    req.FlowName = flow_name

    response = client.CreateFlow(req)
    return response


def create_flow_extended():

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    req.FlowName = '测试合同'

    approvers = []

    # 企业静默签署
    server_ent = FlowCreateApprover()

    server_ent.ApproverType = 3


    # 个人签署
    person = FlowCreateApprover()

    person.ApproverName = '张三'

    person.ApproverMobile = '1*********8'

    person.NotifyType = 'sms'

    # 企业签署
    ent = FlowCreateApprover()

    ent.ApproverName = '李四'

    ent.ApproverMobile = '1*********1'

    ent.OrganizationName = 'XXXXX公司'

    ent.NotifyType = 'sms'

    approvers.append(server_ent)
    approvers.append(person)
    approvers.append(ent)
    req.Approvers = approvers

    req.Unordered = False

    req.UserData = 'UserData'

    req.DeadLine = int(time.time()) + 7 * 24 * 3600

    response = client.CreateFlow(req)
    print(response)


if __name__ == '__main__':
    """
    创建签署流程调用样例
    """

    try:
        _flow_name = '我的第一份模板合同'

        # 签署流程参与者信息
        _approvers = []

        # 个人签署方
        approver = FlowCreateApprover()

        approver.ApproverType(1)

        approver.ApproverName("********************************")

        approver.ApproverMobile("********************************")

        _approvers.append(approver)

        resp = create_flow(Config.operator_user_id, _flow_name, _approvers)
        print(resp)
    except Exception as e:
        print(e)
