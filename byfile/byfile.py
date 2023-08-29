from tencentcloud.ess.v20201111.models import ApproverInfo, Component
from config import Config


def build_approvers():
    """
    构造签署人 - 以B2B2C为例, 实际请根据自己的场景构造签署方、控件
    """

    # 个人签署方构造参数
    person_name = '********************'
    person_mobile = '********************'

    # 企业签署方构造参数
    organization_name = '********************'
    organization_user_name = '********************'
    organization_user_mobile = '********************'

    approvers = [
        build_server_sign_approver(),  # 发起方企业静默签署，此处需要在config.php中设置一个持有的印章值serverSignSealId
        build_organization_approver(organization_user_name, organization_user_mobile, organization_name),  # 另一家企业签署方
        build_person_approver(person_name, person_mobile)  # 个人签署方
    ]
    return approvers


def build_person_approver(name, mobile):
    """
    打包个人签署方参与者信息
    """

    # 签署参与者信息
    # 个人签署方
    approver = ApproverInfo()

    approver.ApproverType = 1

    approver.ApproverName = name

    approver.ApproverMobile = mobile

    approver.NotifyType = "sms"

    # 模板控件信息
    # 签署人对应的签署控件
    component = build_component(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, '')

    approver.SignComponents = [component]

    return approver


def build_organization_approver(name, mobile, organization_name):
    """
    打包企业签署方参与者信息
    """

    # 签署参与者信息
    approver = ApproverInfo()

    approver.ApproverType = 0

    approver.ApproverName = name

    approver.ApproverMobile = mobile

    approver.OrganizationName = organization_name

    approver.NotifyType = "none"

    # 模板控件信息
    # 签署人对应的签署控件
    component = build_component(246.15625, 472.78125, 112, 40, 0, "SIGN_SEAL", 1, '')

    approver.SignComponents = [component]

    return approver


def build_server_sign_approver():
    """
    打包企业静默签署方参与者信息
    """
    # 签署参与者信息
    approver = ApproverInfo()

    approver.ApproverType = 3

    # 模板控件信息
    # 签署人对应的签署控件
    component = build_component(346.15625, 472.78125, 112, 40, 0, "SIGN_SEAL", 1, Config.server_sign_seal_id)

    approver.SignComponents = [component]

    return approver


def build_component(component_pos_x, component_pos_y, component_width, component_height,
                    file_index, component_type, component_page, component_value):
    """
    构建（签署）控件信息
    """
    # 模板控件信息
    # 签署人对应的签署控件
    component = Component()

    component.ComponentPosX = component_pos_x

    component.ComponentPosY = component_pos_y

    component.ComponentWidth = component_width

    component.ComponentHeight = component_height

    component.FileIndex = file_index

    component.ComponentType = component_type

    component.ComponentPage = component_page

    component.ComponentValue = component_value

    return component
