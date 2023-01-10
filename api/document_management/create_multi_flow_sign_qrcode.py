from tencentcloud.ess.v20201111.models import CreateMultiFlowSignQRCodeRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_multi_flow_sign_qrcode(operator_user_id, template_id, flow_name):
    """
    CreateMultiFlowSignQRCode 创建一码多扫流程签署二维码

    官网文档：https://cloud.tencent.com/document/product/1323/75450

    此接口（CreateMultiFlowSignQRCode）用于创建一码多扫流程签署二维码。
    适用场景：无需填写签署人信息，可通过模板id生成签署二维码，签署人可通过扫描二维码补充签署信息进行实名签署。常用于提前不知道签署人的身份信息场景，例如：劳务工招工、大批量员工入职等场景。
    适用的模板仅限于B2C（1、无序签署，2、顺序签署时B静默签署，3、顺序签署时B非首位签署）、单C的模板，且模板中发起方没有填写控件。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateMultiFlowSignQRCodeRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 模板ID
    req.TemplateId = template_id
    # 签署流程名称，最大长度不超过200字符
    req.FlowName = flow_name

    response = client.CreateMultiFlowSignQRCode(req)
    return response


if __name__ == '__main__':
    """
    创建一码多扫流程签署二维码调用样例
    """

    try:
        # 模板ID
        _template_id = '********************************'

        # 签署流程名称，最大长度不超过200字符
        _flow_name = '扫码签流程'

        resp = create_multi_flow_sign_qrcode(Config.operator_user_id, _template_id, _flow_name)
        print(resp)
    except Exception as e:
        print(e)
