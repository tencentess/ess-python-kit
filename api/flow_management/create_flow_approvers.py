from tencentcloud.ess.v20201111.models import CreateFlowApproversRequest, UserInfo, FillApproverInfo

from api.common import get_client_instance
from config import Config


def create_flow_approvers(operator_user_id, flow_id, approvers):

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = CreateFlowApproversRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FlowId = flow_id

    req.Approvers = approvers

    response = client.CreateFlowApprovers(req)
    return response


if __name__ == '__main__':
    """
    补充签署流程本企业签署人信息调用样例
    """

    try:
        # 签署流程编号
        _flow_id = '********************************'

        # 签署人签署Id
        _recipient_id = '********************************'

        # 签署人来源
        # WEWORKAPP: 企业微信
        _approver_source = 'WEWORKAPP'

        # 企业自定义账号Id
        # WEWORKAPP场景下指企业自有应用获取企微明文的userid
        _custom_user_id = '********************************'

        approver = FillApproverInfo()
        approver.RecipientId = _recipient_id
        approver.ApproverSource = _approver_source
        approver.CustomUserId = _custom_user_id

        approvers = [approver]

        resp = create_flow_approvers(Config.operator_user_id, _flow_id, approvers)
        print(resp)
    except Exception as e:
        print(e)
