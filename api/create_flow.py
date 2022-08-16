from tencentcloud.ess.v20201111.models import CreateFlowRequest, UserInfo, FlowCreateApprover

from api.common import get_client_instance
from config import Config


def create_flow(operator_user_id, flow_name, approvers):
    """
    创建签署流程
    适用场景：在标准制式的合同场景中，可通过提前预制好模板文件，每次调用模板文件的id，补充合同内容信息及签署信息生成电子合同。
    注：该接口是通过模板生成合同流程的前置接口，先创建一个不包含签署文件的流程。配合“创建电子文档”接口和“发起流程”接口使用。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程参与者信息
    req.Approvers = approvers

    # 签署流程名称,最大长度200个字符
    req.FlowName = flow_name

    response = client.CreateFlow(req)
    return response


if __name__ == '__main__':
    """
    创建签署流程调用样例
    """

    try:
        _flow_name = '我的第一份模版合同'

        # 签署流程参与者信息
        _approvers = []

        # 个人签署方
        approver = FlowCreateApprover()
        # 参与者类型：
        # 0：企业
        # 1：个人
        # 3：企业静默签署
        # 注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。
        approver.ApproverType(1)
        # 本环节需要操作人的名字
        approver.ApproverName("********************************")
        # 本环节需要操作人的手机号
        approver.ApproverMobile("********************************")

        _approvers.append(approver)

        resp = create_flow(Config.operator_user_id, _flow_name, _approvers)
        print(resp)
    except Exception as e:
        print(e)
