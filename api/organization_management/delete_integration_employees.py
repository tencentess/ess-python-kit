from tencentcloud.ess.v20201111.models import DeleteIntegrationEmployeesRequest, UserInfo, Staff

from api.common import get_client_instance
from config import Config


def delete_integration_employees(operator_user_id, employees):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DeleteIntegrationEmployeesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.Employees = employees

    response = client.DeleteIntegrationEmployees(req)
    return response


if __name__ == '__main__':
    """
    移除员工调用样例
    """

    try:
        _employees = []

        _employee = Staff()
        _employee.UserId = '************'

        _employees.append(_employee)

        resp = delete_integration_employees(Config.operator_user_id, _employees)
        print(resp)
    except Exception as e:
        print(e)
