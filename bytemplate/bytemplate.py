from tencentcloud.ess.v20201111.models import FlowCreateApprover


def build_flow_create_approvers():
    """
    构造签署人 - 以B2B2C为例, 实际请根据自己的场景构造签署方
    """
    # 个人签署方构造参数
    person_name = '********************'
    person_mobile = '********************'

    # 企业签署方构造参数
    organization_name = '********************'
    organization_user_name = '********************'
    organization_user_mobile = '********************'

    # 此处添加的签署人类型、数量、顺序需要和模板中的配置保持一致
    approvers = [
        build_server_sign_flow_create_approver(),  # 发起方企业静默签署
        build_organization_flow_create_approver(organization_user_name, organization_user_mobile,
                                                organization_name),  # 另一家企业签署方
        build_person_flow_create_approver(person_name, person_mobile)  # 个人签署方
    ]

    return approvers


def build_person_flow_create_approver(name, mobile):
    """
    打包个人签署方参与者信息
    """
    # 签署参与者信息
    # 个人签署方
    approver = FlowCreateApprover()

    approver.ApproverType = 1

    approver.ApproverName = name

    approver.ApproverMobile = mobile

    approver.NotifyType = "sms"

    return approver


def build_organization_flow_create_approver(name, mobile, organization_name):
    """
    打包企业签署方参与者信息
    """
    # 签署参与者信息
    approver = FlowCreateApprover()

    approver.ApproverType = 0

    approver.ApproverName = name

    approver.ApproverMobile = mobile

    approver.OrganizationName = organization_name

    approver.NotifyType = "none"

    return approver


def build_server_sign_flow_create_approver():
    """
    打包企业静默签署方参与者信息
    """
    # 签署参与者信息
    approver = FlowCreateApprover()

    approver.ApproverType = 3

    return approver
