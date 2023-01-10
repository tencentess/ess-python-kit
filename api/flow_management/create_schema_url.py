from tencentcloud.ess.v20201111.models import CreateSchemeUrlRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_schema_url(operator_user_id, flow_id, path_type):
    """
    CreateSchemeUrl 获取小程序跳转链接

    官网文档： https://cloud.tencent.com/document/product/1323/70359

    适用场景：如果需要签署人在自己的APP、小程序、H5应用中签署，可以通过此接口获取跳转腾讯电子签小程序的签署跳转链接。
    注：如果签署人是在PC端扫码签署，可以通过生成跳转链接自主转换成二维码，让签署人在PC端扫码签署。
    跳转到小程序的实现，参考官方文档（分为全屏、半屏两种方式）
    如您需要自主配置小程序跳转链接，请参考: 跳转小程序链接配置说明
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateSchemeUrlRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程编号 (PathType=1时必传)
    req.FlowId = flow_id

    # 跳转页面 1: 小程序合同详情 2: 小程序合同列表页 0: 不传, 默认主页
    req.PathType = path_type

    response = client.CreateSchemeUrl(req)
    return response


if __name__ == '__main__':
    """
    获取小程序跳转链接调用样例
    """

    try:
        # 成功发起合同的flowId
        _flow_id = '********************************'
        # 跳转页面 1: 小程序合同详情 2: 小程序合同列表页 0: 不传, 默认主页
        _path_type = 1

        resp = create_schema_url(Config.operator_user_id, _flow_id, _path_type)
        print(resp)
    except Exception as e:
        print(e)
