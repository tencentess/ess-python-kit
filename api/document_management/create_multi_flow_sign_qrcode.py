from tencentcloud.ess.v20201111.models import CreateMultiFlowSignQRCodeRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_multi_flow_sign_qrcode(operator_user_id, template_id, flow_name):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateMultiFlowSignQRCodeRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.TemplateId = template_id
    req.FlowName = flow_name

    response = client.CreateMultiFlowSignQRCode(req)
    return response


if __name__ == '__main__':

    try:
        _template_id = '********************************'

        _flow_name = '扫码签流程'

        resp = create_multi_flow_sign_qrcode(Config.operator_user_id, _template_id, _flow_name)
        print(resp)
    except Exception as e:
        print(e)
