from tencentcloud.ess.v20201111.models import CreatePrepareFlowRequest, UserInfo, FlowCreateApprover

from api.common import get_client_instance
from config import Config


def create_prepare_flow(operator_user_id, flow_name, resource_id, approvers):
    """
    CreatePrepareFlow 创建快速发起流程

    官网文档：https://cloud.tencent.com/document/product/1323/83412

    适用场景：用户通过API 合同文件及签署信息，并可通过我们返回的URL在页面完成签署控件等信息的编辑与确认，快速发起合同.
    注：该接口文件的resourceId 是通过上传文件之后获取的。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreatePrepareFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署流程参与者信息
    req.Approvers = approvers

    # 签署流程名称,最大长度200个字符
    req.FlowName = flow_name

    # 资源Id,通过上传UploadFiles接口获得
    req.ResourceId = resource_id

    response = client.CreatePrepareFlow(req)
    return response


if __name__ == '__main__':
    """
    创建快速发起流程调用样例
    """

    try:
        _flow_name = '快速发起流程'
        _resource_id = '******************'

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

        resp = create_prepare_flow(Config.operator_user_id, _flow_name, _resource_id, _approvers)
        print(resp)
    except Exception as e:
        print(e)
