from tencentcloud.ess.v20201111.models import VerifyPdfRequest, UserInfo

from api.common import get_client_instance
from config import Config


def verify_pdf(operator_user_id, flow_id):
    """
    VerifyPdf 合同文件验签

    官网文档：https://cloud.tencent.com/document/product/1323/80797

    验证合同文件
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = VerifyPdfRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程id
    req.FlowId = flow_id

    response = client.VerifyPdf(req)
    return response


if __name__ == '__main__':
    """
    合同文件验签调用样例
    """

    try:
        _flow_id = '********************************'

        resp = verify_pdf(Config.operator_user_id, _flow_id)
        print(resp)
    except Exception as e:
        print(e)
