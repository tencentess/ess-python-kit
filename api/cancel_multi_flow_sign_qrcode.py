from tencentcloud.ess.v20201111.models import CancelMultiFlowSignQRCodeRequest, UserInfo

from api.common import get_client_instance
from config import Config


def cancel_multi_flow_sign_qrcode(operator_user_id, qrcode_id):
    """
    此接口（CancelMultiFlowSignQRCode）用于取消一码多扫二维码。
    该接口对传入的二维码ID，若还在有效期内，可以提前失效。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CancelMultiFlowSignQRCodeRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 二维码id
    req.QrCodeId = qrcode_id

    response = client.CancelMultiFlowSignQRCode(req)
    return response


if __name__ == '__main__':
    """
    取消一码多扫二维码调用样例
    """

    try:
        # 二维码id
        _qrcode_id = '********************************'

        resp = cancel_multi_flow_sign_qrcode(Config.operator_user_id, _qrcode_id)
        print(resp)
    except Exception as e:
        print(e)
