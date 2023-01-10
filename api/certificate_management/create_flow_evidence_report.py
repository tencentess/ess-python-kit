from tencentcloud.ess.v20201111.models import CreateFlowEvidenceReportRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_evidence_report(operator_user_id, flow_id):
    """
    CreateFlowEvidenceReport 创建并返回出证报告

    官网文档：https://cloud.tencent.com/document/product/1323/79686

    创建出证报告，返回报告 ID。
    """

    # 构造客户端调用实例
    client = get_client_instance(
        Config.secret_id,
        Config.secret_key,
        Config.endpoint)

    # 构造请求体
    req = CreateFlowEvidenceReportRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程id
    req.FlowId = flow_id

    response = client.CreateFlowEvidenceReport(req)
    return response


if __name__ == '__main__':
    """
    创建并返回出证报告调用样例
    """

    try:
        _flow_id = '********************************'

        resp = create_flow_evidence_report(Config.operator_user_id, _flow_id)
        print(resp)
    except Exception as e:
        print(e)
