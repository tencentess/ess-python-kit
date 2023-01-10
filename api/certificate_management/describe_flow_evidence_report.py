from tencentcloud.ess.v20201111.models import DescribeFlowEvidenceReportRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_evidence_report(operator_user_id, report_id):
    """
    DescribeFlowEvidenceReport 查询出证报告

    官网文档：https://cloud.tencent.com/document/product/1323/83441

    查询出证报告，返回报告 URL。
    """

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = DescribeFlowEvidenceReportRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 出证报告编号
    req.FlowId = report_id

    response = client.DescribeFlowEvidenceReport(req)
    return response


if __name__ == '__main__':
    """
    查询出证报告调用样例
    """

    try:
        _report_id = '********************************'

        resp = create_flow_evidence_report(Config.operator_user_id, _report_id)
        print(resp)
    except Exception as e:
        print(e)
