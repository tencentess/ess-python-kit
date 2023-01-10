from tencentcloud.ess.v20201111.models import DescribeFileUrlsRequest, UserInfo

from api.common import get_client_instance
from config import Config


def describe_file_urls(operator_user_id, business_ids, business_type):
    """
    DescribeFileUrls 查询文件下载URL

    官网文档：https://cloud.tencent.com/document/product/1323/70366

    适用场景：通过传参合同流程编号，下载对应的合同PDF文件流到本地。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = DescribeFileUrlsRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 文件对应的业务类型，目前支持：
    # - 模板 "TEMPLATE"
    # - 文档 "DOCUMENT"
    # - 印章 “SEAL”
    # - 流程 "FLOW"
    req.BusinessType = business_type

    # 业务编号的数组，如模板编号、文档编号、印章编号
    # 最大支持20个资源
    req.BusinessIds = business_ids

    response = client.DescribeFileUrls(req)
    return response


if __name__ == '__main__':
    """
    查询文件下载URL调用样例
    """

    try:
        # 业务编号的数组，如模板编号、文档编号、印章编号
        # 最大支持20个资源
        _flow_ids = '********************************'

        # 文件对应的业务类型，目前支持：
        # - 模板 "TEMPLATE"
        # - 文档 "DOCUMENT"
        # - 印章 “SEAL”
        # - 流程 "FLOW"
        _business_type = "FLOW"

        resp = describe_file_urls(Config.operator_user_id, [_flow_ids], _business_type)
        print(resp)
    except Exception as e:
        print(e)
