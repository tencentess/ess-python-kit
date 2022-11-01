from tencentcloud.ess.v20201111.models import CreateFlowApproversRequest, UserInfo, FillApproverInfo

from api.common import get_client_instance
from config import Config


def create_flow_approvers(operator_user_id, flow_id, approvers):
    """
    补充签署流程本企业签署人信息
    适用场景：在通过模版或者文件发起合同时，若未指定本企业签署人信息，则流程发起后，可以调用此接口补充签署人。
    同一签署人可以补充多个员工作为候选签署人,最终签署人取决于谁先领取合同完成签署。
    注：目前暂时只支持补充来源于企业微信的员工作为候选签署人
    """

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

    # 签署流程编号
    req.FlowId = flow_id

    # 补充签署人信息
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
