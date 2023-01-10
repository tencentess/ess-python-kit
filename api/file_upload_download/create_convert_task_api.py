from tencentcloud.ess.v20201111.models import CreateConvertTaskApiRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_convert_task_api(operator_user_id, resource_id, resource_type, resource_name):
    """
    CreateConvertTaskApi 创建文件转换任务

    官网文档：https://cloud.tencent.com/document/product/1323/78149

    此接口用于创建文件转换任务
    适用场景：将doc/docx文件转化为pdf文件
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateConvertTaskApiRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 资源Id，由UploadFiles接口返回
    req.ResourceId = resource_id

    # 资源类型，2-doc 3-docx
    req.ResourceType = resource_type

    # 资源名称
    req.ResourceName = resource_name

    response = client.CreateConvertTaskApi(req)
    return response


if __name__ == '__main__':
    """
    创建文件转换任务调用样例
    """

    try:
        # 资源Id，由UploadFiles接口返回
        _resource_id = '********************************'
        # 资源类型，2-doc 3-docx
        _resource_type = '********************************'
        # 资源名称
        _resource_name = '********************************'

        resp = create_convert_task_api(Config.operator_user_id, _resource_id, _resource_type, _resource_name)
        print(resp)
    except Exception as e:
        print(e)
