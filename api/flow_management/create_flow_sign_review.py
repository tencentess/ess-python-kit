from tencentcloud.ess.v20201111.models import CreateFlowSignReviewRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_sign_review(operator_user_id, flow_id, review_type, review_message):

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

    req.FlowId = flow_id

    req.ReviewType = review_type

    req.ReviewMessage = review_message

    response = client.CreateFlowSignReview(req)
    return response


if __name__ == '__main__':
    """
    提交企业签署流程审批结果调用样例
    """

    try:
        _flow_id = '********************************'

        _review_type = '********************************'

        _review_message = '********************************'

        resp = create_flow_sign_review(Config.operator_user_id, _flow_id, _review_type, _review_message)
        print(resp)
    except Exception as e:
        print(e)
