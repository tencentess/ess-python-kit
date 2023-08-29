from tencentcloud.ess.v20201111.models import CreateFlowRequest, CreateDocumentRequest, StartFlowRequest, UserInfo, Agent
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from api.common import get_client_instance

def group_create_flow(operator_user_id, flow_name, approvers, proxy_organization_id):

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

    req.FlowName = flow_name

    response = client.CreateFlow(req)
    return response


def group_create_document(operator_user_id, flow_id, template_id, file_name, form_fields, proxy_organization_id):

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

    req.FileNames = [file_name]

    req.FlowId = flow_id

    # 用户上传的模板ID,在控制台模版管理中可以找到
    # 单个个人签署模版
    req.TemplateId = template_id

    # 填写控件内容
    req.FormFields = form_fields

    response = client.CreateDocument(req)
    return response


def group_start_flow(operator_user_id, flow_id, proxy_organization_id):

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

    req.FlowId = flow_id

    response = client.StartFlow(req)
    return response


if __name__ == '__main__':

    import time
    from tencentcloud.ess.v20201111.models import FlowCreateApprover
    from config import Config

    try:
        # 需要代发起的子企业的企业id
        proxy_organization_id = "********************************"

        flow_name = "********************************"

        # 构造签署人
        approvers = []

        # 签署参与者信息
        # 个人签署方
        approver = FlowCreateApprover()
        approver.ApproverType = 1

        approver.ApproverName = "****************"

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
