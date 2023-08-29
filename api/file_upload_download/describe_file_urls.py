from tencentcloud.ess.v20201111.models import DescribeFileUrlsRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_file_urls(operator_user_id, business_ids, business_type):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFileUrlsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.BusinessType = business_type

    req.BusinessIds = business_ids

    response = client.DescribeFileUrls(req)
    return response


if __name__ == '__main__':
    """
    查询文件下载URL调用样例
    """

    try:
        _flow_ids = '********************************'

        _business_type = "FLOW"

        resp = describe_file_urls(Config.operator_user_id, [_flow_ids], _business_type)
        print(resp)
    except Exception as e:
        print(e)
