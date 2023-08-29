from tencentcloud.ess.v20201111.models import CreateFlowByFilesRequest, UserInfo, Agent

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from api.common import get_client_instance
from config import Config


def group_create_flow_by_files(operator_user_id, flow_name, approvers, file_id, proxy_organization_id):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowByFilesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 设置集团子企业账号
    agent = Agent()
    agent.ProxyOrganizationId = proxy_organization_id
    req.Agent = agent

    req.FileIds = [file_id]

    req.FlowName = flow_name

    # 签署方信息
    req.Approvers = approvers

    response = client.CreateFlowByFiles(req)
    return response


if __name__ == '__main__':

    from tencentcloud.ess.v20201111.models import ApproverInfo, Component

    try:
        # 需要代发起的子企业的企业id
        _proxy_organization_id = "********************************"

        _file_id = "********************************"

        _flow_name = '我的第一份文件合同'

        # 签署参与者信息
        _approvers = []

        # 个人签署方
        approver = ApproverInfo()
        approver.ApproverType = 1
        approver.ApproverName = "********************************"
        approver.ApproverMobile = "********************************"

        # 签署人对应的签署控件
        component = Component()

        component.ComponentPosY = 472.78125

        component.ComponentPosX = 146.15625

        component.ComponentWidth = 112

        component.ComponentHeight = 40

        component.FileIndex = 0

        component.ComponentType = "SIGN_SIGNATURE"

        component.ComponentPage = 1

        approver.SignComponents = [component]

        _approvers.append(approver)

        resp = group_create_flow_by_files(Config.operator_user_id, _flow_name, _approvers, _file_id,
                                          _proxy_organization_id)
        print(resp)

    except Exception as e:
        print(e)
