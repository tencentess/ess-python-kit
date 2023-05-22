from tencentcloud.ess.v20201111.models import CreateFlowRequest, CreateDocumentRequest, StartFlowRequest, UserInfo, Agent
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from api.common import get_client_instance

def group_create_flow(operator_user_id, flow_name, approvers, proxy_organization_id):
    """
    CreateFlow 创建签署流程

    官网文档：https://cloud.tencent.com/document/api/1323/70361

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

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    # 签署流程参与者信息
    req.Approvers = approvers

    # 签署流程名称,最大长度200个字符
    req.FlowName = flow_name

    response = client.CreateFlow(req)
    return response


def group_create_document(operator_user_id, flow_id, template_id, file_name, form_fields, proxy_organization_id):
    """
    CreateDocument 创建电子文档

    官方文档：https://cloud.tencent.com/document/api/1323/70364

    适用场景：见创建签署流程接口。注：该接口需要给对应的流程指定一个模板id，并且填充该模板中需要补充的信息。是“发起流程”接口的前置接口。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateDocumentRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    # 文件名列表,单个文件名最大长度200个字符
    req.FileNames = [file_name]

    # 签署流程编号,由CreateFlow接口返回
    req.FlowId = flow_id

    # 用户上传的模板ID,在控制台模版管理中可以找到
    # 单个个人签署模版
    req.TemplateId = template_id

    # 填写控件内容
    req.FormFields = form_fields

    response = client.CreateDocument(req)
    return response


def group_start_flow(operator_user_id, flow_id, proxy_organization_id):
    """
    StartFlow 此接口用于发起流程

    官网文档：https://cloud.tencent.com/document/product/1323/70357

    适用场景：见创建签署流程接口。
    注：该接口是“创建电子文档”接口的后置接口，用于激活包含完整合同信息（模板及内容信息）的流程。激活后的流程就是一份待签署的电子合同。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = StartFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    # 签署流程编号，由CreateFlow接口返回
    req.FlowId = flow_id

    response = client.StartFlow(req)
    return response


if __name__ == '__main__':
    """
      主企业代子企业使用模板发起合同的简单样例，如需更详细的参数使用说明，请参考 flow_management 目录下的 create_flow/create_document/start_flow
      注意：使用集团代发起功能，需要主企业和子企业均已加入集团，并且主企业OperatorUserId对应人员被赋予了对应操作权限
    """

    import time
    from tencentcloud.ess.v20201111.models import FlowCreateApprover
    from config import Config

    try:
        # 需要代发起的子企业的企业id
        proxy_organization_id = "********************************"

        # 定义合同名
        flow_name = "********************************"

        # 构造签署人
        approvers = []

        # 签署参与者信息
        # 个人签署方
        approver = FlowCreateApprover()
        # 参与者类型：
        # 0：企业
        # 1：个人
        # 3：企业静默签署
        # 注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。
        approver.ApproverType = 1
        # 本环节需要操作人的名字
        approver.ApproverName = "****************"
        # 本环节需要操作人的手机号
        approver.ApproverMobile = "****************"
        approvers.append(approver)

        # 创建流程
        create_flow_resp = group_create_flow(Config.operator_user_id, flow_name, approvers, proxy_organization_id)
        flow_id = create_flow_resp.FlowId
        print(create_flow_resp)

        # 创建电子文档
        create_document_resp = group_create_document(Config.operator_user_id, flow_id, Config.template_id,
                                                     flow_name, [], proxy_organization_id)
        print(create_document_resp)

        # 等待文档异步合成
        time.sleep(3)

        # 开启流程
        start_flow_resp = group_start_flow(Config.operator_user_id, flow_id, proxy_organization_id)
        print(start_flow_resp)

    except Exception as e:
        print(e)
