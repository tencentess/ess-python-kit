from tencentcloud.ess.v20201111.models import GetTaskResultApiRequest, UserInfo

from api.common import get_client_instance
from config import Config


def get_task_result_api(operator_user_id, task_id):
    """
    GetTaskResultApi 查询转换任务状态

    官网文档：https://cloud.tencent.com/document/product/1323/78148

    此接口用于查询转换任务状态
    适用场景：将doc/docx文件转化为pdf文件
    注：该接口是“创建文件转换任务”接口的后置接口，用于查询转换任务的执行结果
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = GetTaskResultApiRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 任务Id，“创建文件转换任务”接口返回
    req.TaskId = task_id

    response = client.GetTaskResultApi(req)
    return response


if __name__ == '__main__':
    """
    查询转换任务状态调用样例
    """

    try:
        _task_id = '********************************'

        resp = get_task_result_api(Config.operator_user_id, _task_id)
        print(resp)
    except Exception as e:
        print(e)
