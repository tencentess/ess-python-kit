from tencentcloud.ess.v20201111.models import CancelFlowRequest, UserInfo

from api.common import get_client_instance
from config import Config


def cancel_flow(operator_user_id, flow_id, cancel_message):
    """
    CancelFlow 撤销签署流程

    官网文档：https://cloud.tencent.com/document/product/1323/70362

    适用场景：如果某个合同流程当前至少还有一方没有签署，则可通过该接口取消该合同流程。常用于合同发错、内容填错，需要及时撤销的场景。
    注：如果合同流程中的参与方均已签署完毕，则无法通过该接口撤销合同。
    """

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = CancelFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程id
    req.FlowId = flow_id
    # 撤销原因，最长200个字符
    req.CancelMessage = cancel_message

    response = client.CancelFlow(req)
    return response


if __name__ == '__main__':
    """
    撤销签署流程调用样例
    """

    try:
        _flow_id = '********************************'
        _cancel_message = '撤销原因'

        resp = cancel_flow(Config.operator_user_id, _flow_id, _cancel_message)
        print(resp)
    except Exception as e:
        print(e)
