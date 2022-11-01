from tencentcloud.ess.v20201111.models import CreateIntegrationEmployeesRequest, UserInfo, Staff

from api.common import get_client_instance
from config import Config


def create_integration_employees(operator_user_id, employees):
    """
    创建员工
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateIntegrationEmployeesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 待创建员工的信息，Mobile和DisplayName必填
    req.Employees = employees

    response = client.CreateIntegrationEmployees(req)
    return response


if __name__ == '__main__':
    """
    创建员工调用样例
    """

    try:
        # 待创建员工的信息，Mobile和DisplayName必填
        _employees = []

        _employee = Staff()
        _employee.Mobile = '*********'
        _employee.DisplayName = '张三'

        _employees.append(_employee)

        resp = create_integration_employees(Config.operator_user_id, _employees)
        print(resp)
    except Exception as e:
        print(e)
