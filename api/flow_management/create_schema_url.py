from tencentcloud.ess.v20201111.models import CreateSchemeUrlRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_schema_url(operator_user_id, flow_id, path_type):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateSchemeUrlRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FlowId = flow_id

    req.PathType = path_type

    response = client.CreateSchemeUrl(req)
    return response


if __name__ == '__main__':
    """
    获取小程序跳转链接调用样例
    """

    try:

        _flow_id = '********************************'

        _path_type = 1

        resp = create_schema_url(Config.operator_user_id, _flow_id, _path_type)
        print(resp)
    except Exception as e:
        print(e)
