import time

from tencentcloud.ess.v20201111.models import CreateFlowByFilesRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_by_files(operator_user_id, flow_name, approvers, file_id):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowByFilesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FileIds = [file_id]

    req.FlowName = flow_name

    req.Approvers = approvers

    response = client.CreateFlowByFiles(req)
    return response


def create_flow_by_files_extended():

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowByFilesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    req.FlowName = '测试合同'

    # 构建签署方信息
    # 注意：文件发起时，签署方不能进行控件填写！！！如果有填写需求，请设置为发起方填写，或者使用模板发起！！！
    server_ent = ApproverInfo()

    server_ent.ApproverType = 3

    server_ent.SignComponents = [
        # 坐标定位，印章类型，并传入印章Id
        build_component_normal("SIGN_SEAL", "*************"),
        # 关键字定位，印章类型，并传入印章Id
        build_component_keyword("SIGN_SEAL", "*************"),
        # 表单域定位，印章类型，并传入印章Id
        build_component_field("SIGN_SEAL", "*************")]

    # 个人签署
    person = ApproverInfo()

    person.ApproverName = '张三'

    person.ApproverMobile = '1*********8'

    person.NotifyType = 'sms'
    # 这里可以设置用户进行手动签名，分别可以使用坐标、表单域、关键字进行定位
    person.SignComponents = [
        # 坐标定位，手写签名类型
        build_component_normal("SIGN_SIGNATURE", ""),
        # 关键字定位，手写签名类型
        build_component_keyword("SIGN_SIGNATURE", ""),
        # 表单域定位，手写签名类型
        build_component_field("SIGN_SIGNATURE", "")]

    # 企业签署
    ent = ApproverInfo()

    ent.ApproverName = '李四'

    ent.ApproverMobile = '1*********1'

    ent.OrganizationName = 'XXXXX公司'

    ent.NotifyType = 'sms'
    # 这里可以设置企业手动签章（如果需要自动请使用静默签署），分别可以使用坐标、表单域、关键字进行定位
    ent.SignComponents = [
        # 坐标定位，印章类型
        build_component_normal("SIGN_SEAL", ""),
        # 关键字定位，印章类型
        build_component_keyword("SIGN_SEAL", ""),
        # 表单域定位，印章类型
        build_component_field("SIGN_SEAL", "")]

    req.Approvers = [server_ent, person, ent]

    req.FileIds = ["*************************"]

    req.FlowType = "销售合同"

    # 经办人内容控件配置，必须在此处给控件进行赋值，合同发起时控件即被填写完成。
    req.Components = [
        # 坐标定位，单行文本类型
        build_component_normal("TEXT", "单行文本"),
        # 关键字定位，单行文本类型
        build_component_keyword("TEXT", "单行文本"),
        # 表单域定位，单行文本类型
        build_component_field("TEXT", "单行文本")]

    req.NeedPreview = False

    req.PreviewType = 0

    req.Deadline = int(time.time()) + 7 * 24 * 3600

    req.Unordered = False

    req.NeedSignReview = False

    req.UserData = "UserData"

    response = client.CreateFlowByFiles(req)
    print(response)


# buildSignComponentNormal 使用坐标模式进行控件定位
def build_component_normal(component_type, component_value):

    component = Component()
    component.ComponentPosX = 146.15625
    component.ComponentPosY = 472.78125
    component.ComponentWidth = 112
    component.ComponentHeight = 40

    component.FileIndex = 0

    component.ComponentPage = 1

    component.ComponentType = component_type

    if component_value != '':
        component.ComponentValue = component_value

    return component


# buildComponentKeyword 使用关键字模式进行控件定位
def build_component_keyword(component_type, component_value):

    component = Component()

    component.GenerateMode = 'KEYWORD'

    component.ComponentId = '签名'

    component.ComponentWidth = 112
    component.ComponentHeight = 40

    component.FileIndex = 0

    component.OffsetX = 10.5
    component.OffsetY = 10.5

    component.KeywordOrder = 'Reverse'

    component.KeywordIndexes = [1]

    component.ComponentType = component_type

    if component_value != '':
        component.ComponentValue = component_value

    return component


#  buildComponentField 使用表单域模式进行控件定位
def build_component_field(component_type, component_value):

    component = Component()

    component.GenerateMode = 'FIELD'

    component.ComponentName = '表单'

    component.FileIndex = 0

    component.ComponentType = component_type

    if component_value != '':
        component.ComponentValue = component_value

    return component


if __name__ == '__main__':
    """
    通过上传后的pdf资源编号来创建待签署的合同流程调用样例
    """
    from tencentcloud.ess.v20201111.models import ApproverInfo, Component


    def build_components():
        """
        构建需要发起方填写的控件，在发起时直接给控件进行赋值
        """

        # 发起方需要填写的控件
        components = []

        component1 = Component()

        component1.ComponentPosY(472.78125)

        component1.ComponentPosX(146.15625)

        component1.ComponentWidth(112)

        component1.ComponentHeight(40)

        component1.FileIndex(0)

        component1.ComponentType("TEXT")

        component1.ComponentValue("content")

        component1.ComponentPage(1)

        components.append(component1)


    try:
        _file_id = "********************************"

        _flow_name = '我的第一份文件合同'

        # 签署参与者信息
        _approvers = []

        # 个人签署方
        approver = ApproverInfo()

        approver.ApproverType(1)

        approver.ApproverName("********************************")

        approver.ApproverMobile("********************************")

        # 签署人对应的签署控件
        component = Component()

        component.ComponentPosY(472.78125)

        component.ComponentPosX(146.15625)

        component.ComponentWidth(112)

        component.ComponentHeight(40)

        component.FileIndex(0)

        component.ComponentType("SIGN_SIGNATURE")
        component.ComponentPage(1)

        approver.SignComponents = [component]

        _approvers.append(approver)

        resp = create_flow_by_files(Config.operator_user_id, _flow_name, _approvers, _file_id)
        print(resp)

    except Exception as e:
        print(e)
