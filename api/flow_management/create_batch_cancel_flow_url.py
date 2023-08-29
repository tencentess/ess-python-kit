from tencentcloud.ess.v20201111.models import CreateBatchCancelFlowUrlRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_batch_cancel_flow_url(operator_user_id, flow_ids):

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = CreateBatchCancelFlowUrlRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FlowIds = flow_ids

    response = client.CreateBatchCancelFlowUrl(req)
    return response


if __name__ == '__main__':
    """
    获取批量撤销签署流程链接调用样例
    """

    try:
        _flow_ids = ['********************************', '********************************']

        resp = create_batch_cancel_flow_url(Config.operator_user_id, _flow_ids)
        print(resp)
    except Exception as e:
        print(e)
