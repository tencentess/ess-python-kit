from tencentcloud.ess.v20201111.models import DescribeIntegrationEmployeesRequest, UserInfo, Filter

from api.common import get_client_instance
from config import Config


def describe_integration_employees(operator_user_id, limit, offset, filters):
    """
    DescribeIntegrationEmployees 查询员工信息，每次返回的数据量最大为20

    官网文档：https://cloud.tencent.com/document/product/1323/81115

    查询员工信息，每次返回的数据量最大为20
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeIntegrationEmployeesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.Limit = limit
    req.Offset = offset
    req.Filters = filters

    response = client.DescribeIntegrationEmployees(req)
    return response


if __name__ == '__main__':
    """
    查询员工信息调用样例
    """

    try:
        _limit = 20
        _offset = 0

        _filters = []
        _filter = Filter()
        _filter.Key = 'Status'
        _filter.Values = ['IsVerified']
        _filters.append(_filter)

        resp = describe_integration_employees(Config.operator_user_id, _limit, _offset, _filters)
        print(resp)
    except Exception as e:
        print(e)
