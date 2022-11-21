from tencentcloud.ess.v20201111.models import DescribeOrganizationSealsRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_organization_seals(operator_user_id, limit):
    """
    查询企业电子印章
    查询企业印章的列表，需要操作者具有查询印章权限
    客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；入参InfoType控制印章是否携带授权人信息，为1则携带，
    为0则返回的授权人信息为空数组。接口调用成功返回印章的信息列表还有企业印章的总数。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeOrganizationSealsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 返回最大数量，最大为100
    req.Limit = limit

    response = client.DescribeOrganizationSeals(req)
    return response


if __name__ == '__main__':
    """
    查询模板调用样例
    """

    try:
        _limit = 10

        resp = describe_organization_seals(Config.operator_user_id, _limit)
        print(resp)
    except Exception as e:
        print(e)
