from tencentcloud.ess.v20201111.models import CreateFlowSignReviewRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_sign_review(operator_user_id, flow_id, review_type, review_message):
    """
    提交企业签署流程审批结果
    适用场景:
    在通过接口(CreateFlow 或者CreateFlowByFiles)创建签署流程时，若指定了参数 NeedSignReview 为true,则可以调用此接口提交企业内部签署审批结果。
    若签署流程状态正常，且本企业存在签署方未签署，同一签署流程可以多次提交签署审批结果，签署时的最后一个“审批结果”有效。
    """

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = CreateFlowSignReviewRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程编号
    req.FlowId = flow_id

    # 企业内部审核结果
    # PASS: 通过
    # REJECT: 拒绝
    req.ReviewType = review_type

    # 审核原因
    # 当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
    req.ReviewMessage = review_message

    response = client.CreateFlowSignReview(req)
    return response


if __name__ == '__main__':
    """
    提交企业签署流程审批结果调用样例
    """

    try:
        # 签署流程编号
        _flow_id = '********************************'

        # 企业内部审核结果
        # PASS: 通过
        # REJECT: 拒绝
        _review_type = '********************************'

        # 审核原因
        # 当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
        _review_message = '********************************'

        resp = create_flow_sign_review(Config.operator_user_id, _flow_id, _review_type, _review_message)
        print(resp)
    except Exception as e:
        print(e)
