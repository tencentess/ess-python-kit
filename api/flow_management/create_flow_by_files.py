import time

from tencentcloud.ess.v20201111.models import CreateFlowByFilesRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_by_files(operator_user_id, flow_name, approvers, file_id):
    """
    CreateFlowByFiles 此接口（CreateFlowByFiles）用来通过上传后的pdf资源编号来创建待签署的合同流程。

    官网文档：https://cloud.tencent.com/document/api/1323/70360

    适用场景1：适用非制式的合同文件签署。一般开发者自己有完整的签署文件，可以通过该接口传入完整的PDF文件及流程信息生成待签署的合同流程。
    适用场景2：可通过该接口传入制式合同文件，同时在指定位置添加签署控件。可以起到接口创建临时模板的效果。如果是标准的制式文件，建议使用模板功能生成模板ID进行合同流程的生成。
    注意事项：该接口需要依赖“多文件上传”接口生成pdf资源编号（FileIds）进行使用。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowByFilesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    # 签署pdf文件的资源编号列表，通过UploadFiles接口获取
    req.FileIds = [file_id]

    # 签署流程名称，最大长度不超过200字符
    req.FlowName = flow_name

    # 签署方信息
    req.Approvers = approvers

    response = client.CreateFlowByFiles(req)
    return response


def create_flow_by_files_extended():
    """
    CreateFlowByFilesExtended CreateFlowByFiles接口的详细参数使用样例，前面简要调用的场景不同，此版本旨在提供可选参数的填入参考。
    如果您在实现基础场景外有进一步的功能实现需求，可以参考此处代码。
    注意事项：此处填入参数仅为样例，请在使用时更换为实际值。
    """
    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowByFilesRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    # 签署流程名称, 最大长度200个字符
    req.FlowName = '测试合同'

    # 构建签署方信息
    # 注意：文件发起时，签署方不能进行控件填写！！！如果有填写需求，请设置为发起方填写，或者使用模板发起！！！
    server_ent = ApproverInfo()
    # 这里我们设置签署方类型为企业方静默签署3，注意当类型为静默签署时，签署人会默认设置为发起方经办人。此时姓名手机号企业名等信息无需填写，且填写无效
    server_ent.ApproverType = 3
    # 企业静默签署不会发送短信通知
    # 这里可以设置企业方自动签章，分别可以使用坐标、表单域、关键字进行定位
    server_ent.SignComponents = [
        # 坐标定位，印章类型，并传入印章Id
        build_component_normal("SIGN_SEAL", "*************"),
        # 关键字定位，印章类型，并传入印章Id
        build_component_keyword("SIGN_SEAL", "*************"),
        # 表单域定位，印章类型，并传入印章Id
        build_component_field("SIGN_SEAL", "*************")]

    # 个人签署
    person = ApproverInfo()
    # 个人身份签署一般设置姓名 + 手机号，请确保实际签署时使用的信息和此处一致
    # 本环节需要操作人的名字
    person.ApproverName = '张三'
    # 本环节需要操作人的手机号
    person.ApproverMobile = '15912345678'
    # 合同发起后是否短信通知签署方进行签署：sms - -短信，none - -不通知
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
    # 本环节需要操作人的名字
    ent.ApproverName = '李四'
    # 本环节需要操作人的手机号
    ent.ApproverMobile = '15987654321'
    # 本环节需要企业操作人的企业名称，请注意此处的企业名称要是真实有效的，企业需要在电子签平台进行注册且签署人有加入该企业方能签署。
    # 注：如果该企业尚未注册，或者签署人尚未加入企业，合同仍然可以发起
    ent.OrganizationName = 'XXXXX公司'
    # 合同发起后是否短信通知签署方进行签署：sms - -短信，none - -不通知
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

    # 签署pdf文件的资源编号列表，通过UploadFiles接口获取，暂时仅支持单文件发起
    req.FileIds = ["*************************"]

    # 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符。填写后可以在控制台分类查看合同
    req.FlowType = "销售合同"

    # 经办人内容控件配置，必须在此处给控件进行赋值，合同发起时控件即被填写完成。
    # 注意：目前文件发起模式暂不支持动态表格控件
    req.Components = [
        # 坐标定位，单行文本类型
        build_component_normal("TEXT", "单行文本"),
        # 关键字定位，单行文本类型
        build_component_keyword("TEXT", "单行文本"),
        # 表单域定位，单行文本类型
        build_component_field("TEXT", "单行文本")]

    # 是否需要预览，true：预览模式，false：非预览（默认）；
    # 预览链接有效期300秒；
    # 注：如果使用“预览模式”，出参会返回合同预览链接 PreviewUrl，不会正式发起合同，且出参不会返回签署流程编号 FlowId；如果使用“非预览”，则会正常返回签署流程编号 FlowId，不会生成合同预览链接 PreviewUrl。
    req.NeedPreview = False

    # 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效
    req.PreviewType = 0

    # 签署流程的签署截止时间。
    # 值为unix时间戳,精确到秒,不传默认为当前时间一年后
    req.Deadline = int(time.time()) + 7 * 24 * 3600

    # 发送类型：
    # true：无序签
    # false：有序签
    # 注：默认为false（有序签）
    req.Unordered = False

    # 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
    # 若设置为true，审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。
    # 注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
    req.NeedSignReview = False

    # 用户自定义字段，回调的时候会进行透传，长度需要小于20480
    req.UserData = "UserData"

    response = client.CreateFlowByFiles(req)
    print(response)


# buildSignComponentNormal 使用坐标模式进行控件定位
def build_component_normal(component_type, component_value):
    # 可选参数传入请参考：https://cloud.tencent.com/document/api/1323/70369#Component
    component = Component()
    component.ComponentPosX = 146.15625
    component.ComponentPosY = 472.78125
    component.ComponentWidth = 112
    component.ComponentHeight = 40

    # 控件所属文件的序号，目前均为单文件发起，所以我们固定填入序号0
    component.FileIndex = 0

    # 控件所在的页面数，从1开始取值，请勿超出pdf文件的最大页数
    component.ComponentPage = 1

    # 控件类型，阅读传参文档时请注意控件类型的限制
    component.ComponentType = component_type

    if component_value != '':
        component.ComponentValue = component_value

    return component


# buildComponentKeyword 使用关键字模式进行控件定位
def build_component_keyword(component_type, component_value):
    # 可选参数传入请参考：https://cloud.tencent.com/document/api/1323/70369#Component
    component = Component()

    # KEYWORD 关键字，使用ComponentId指定关键字
    component.GenerateMode = 'KEYWORD'

    # GenerateMode==KEYWORD时，此处赋值用于指定关键字。
    # 注：例如此处指定了关键字为"签名"，那么会全文搜索这个关键字，默认找到所有关键字出现的地方，并以该关键字的左上角为原点划出控件区域
    component.ComponentId = '签名'

    # 控件的长宽
    # 如何确定坐标请参考： https://doc.weixin.qq.com/doc/w3_AKgAhgboACgsf9NKAVqSOKVIkQ0vQ?scode=AJEAIQdfAAoz9916DRAKgAhgboACg
    component.ComponentWidth = 112
    component.ComponentHeight = 40

    # 控件所属文件的序号，目前均为单文件发起，所以我们固定填入序号0
    component.FileIndex = 0

    # 指定关键字时横 / 纵坐标偏移量，单位pt
    # 关键字定位原点默认在关键字的左上角，如果需要偏移该位置可以使用以下参数，如果不需要可以不赋值
    component.OffsetX = 10.5
    component.OffsetY = 10.5

    # 指定关键字排序规则，Positive-正序，Reverse-倒序。传入Positive时会根据关键字在PDF文件内的顺序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的第一个关键字。
    # 传入Reverse时会根据关键字在PDF文件内的反序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的最后一个关键字。
    component.KeywordOrder = 'Reverse'

    # 关键字索引，可选参数，如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。示例：[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
    component.KeywordIndexes = [1]

    # 控件类型，阅读传参文档时请注意控件类型的限制
    component.ComponentType = component_type

    # 企业静默签署时，此处传入了印章Id那么轮到该签署人签署时，会自动进行签章操作
    # 经办人控件填写时，此处传入了控件值，在合同发起后此处会自动进行填充
    if component_value != '':
        component.ComponentValue = component_value

    return component


#  buildComponentField 使用表单域模式进行控件定位
def build_component_field(component_type, component_value):
    # 可选参数传入请参考：https://cloud.tencent.com/document/api/1323/70369#Component
    component = Component()

    # FIELD 表单域，需使用ComponentName指定表单域名称
    component.GenerateMode = 'FIELD'

    # GenerateMode==FIELD 指定表单域名称
    component.ComponentName = '表单'

    # 控件所属文件的序号，目前均为单文件发起，所以我们固定填入序号0
    component.FileIndex = 0

    # 控件类型，阅读传参文档时请注意控件类型的限制
    component.ComponentType = component_type

    # 企业静默签署时，此处传入了印章Id那么轮到该签署人签署时，会自动进行签章操作
    # 经办人控件填写时，此处传入了控件值，在合同发起后此处会自动进行填充
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
        # 参数控件Y位置，单位pt
        component1.ComponentPosY(472.78125)
        # 参数控件X位置，单位pt
        component1.ComponentPosX(146.15625)
        # 参数控件宽度，单位pt
        component1.ComponentWidth(112)
        # 参数控件高度，单位pt
        component1.ComponentHeight(40)
        # 控件所属文件的序号（取值为：0-N）
        component1.FileIndex(0)
        # 可选类型为：
        # TEXT - 内容文本控件
        # MULTI_LINE_TEXT - 多行文本控件
        # CHECK_BOX - 勾选框控件
        # ATTACHMENT - 附件
        # SELECTOR - 选择器
        component1.ComponentType("TEXT")
        # 填写信息为：
        # TEXT - 文本内容
        # MULTI_LINE_TEXT - 文本内容
        # CHECK_BOX - true/false
        # ATTACHMENT - UploadFiles接口上传返回的fileId
        # SELECTOR - 文本内容
        component1.ComponentValue("content")
        # 参数控件所在页码，取值为：1-N
        component1.ComponentPage(1)

        components.append(component1)


    try:
        # 从UploadFiles接口获取到的fileId
        _file_id = "********************************"

        # 签署流程名称,最大长度200个字符
        _flow_name = '我的第一份文件合同'

        # 签署参与者信息
        _approvers = []

        # 个人签署方
        approver = ApproverInfo()
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

        # 签署人对应的签署控件
        component = Component()
        # 参数控件Y位置，单位pt
        component.ComponentPosY(472.78125)
        # 参数控件X位置，单位pt
        component.ComponentPosX(146.15625)
        # 参数控件宽度，单位pt
        component.ComponentWidth(112)
        # 参数控件高度，单位pt
        component.ComponentHeight(40)
        # 控件所属文件的序号（取值为：0-N）
        component.FileIndex(0)
        # 可选类型为：
        # SIGN_SEAL - 签署印章控件
        # SIGN_DATE - 签署日期控件
        # SIGN_SIGNATURE - 手写签名控件
        component.ComponentType("SIGN_SIGNATURE")
        # 参数控件所在页码，取值为：1-N
        component.ComponentPage(1)

        # 本环节操作人签署控件配置，为企业静默签署时，只允许类型为SIGN_SEAL（印章）和SIGN_DATE（日期）控件，并且传入印章编号
        approver.SignComponents = [component]

        _approvers.append(approver)

        resp = create_flow_by_files(Config.operator_user_id, _flow_name, _approvers, _file_id)
        print(resp)

    except Exception as e:
        print(e)
