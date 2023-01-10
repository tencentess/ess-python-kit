import time

from tencentcloud.ess.v20201111.models import CreateFlowRequest, UserInfo, FlowCreateApprover

from api.common import get_client_instance
from config import Config


def create_flow(operator_user_id, flow_name, approvers):
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

    # 签署流程参与者信息
    req.Approvers = approvers

    # 签署流程名称,最大长度200个字符
    req.FlowName = flow_name

    response = client.CreateFlow(req)
    return response


def create_flow_extended():
    """
    CreateFlowExtended CreateFlow接口的详细参数使用样例，前面简要调用的场景不同，此版本旨在提供可选参数的填入参考。
    如果您在实现基础场景外有进一步的功能实现需求，可以参考此处代码。
    注意事项：此处填入参数仅为样例，请在使用时更换为实际值。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateFlowRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    # 签署流程名称, 最大长度200个字符
    req.FlowName = '测试合同'

    # 构建签署方信息，注意这里的签署人类型、数量、顺序需要和模板中的设置保持一致
    approvers = []

    # 企业静默签署
    server_ent = FlowCreateApprover()
    # 这里我们设置签署方类型为企业方静默签署3，注意当类型为静默签署时，签署人会默认设置为发起方经办人。此时姓名手机号企业名等信息无需填写，且填写无效
    server_ent.ApproverType = 3
    # 企业静默签署不会发送短信通知

    # 个人签署
    person = FlowCreateApprover()
    # 个人身份签署一般设置姓名 + 手机号，请确保实际签署时使用的信息和此处一致
    # 本环节需要操作人的名字
    person.ApproverName = '张三'
    # 本环节需要操作人的手机号
    person.ApproverMobile = '15912345678'
    # 合同发起后是否短信通知签署方进行签署：sms - -短信，none - -不通知
    person.NotifyType = 'sms'

    # 企业签署
    ent = FlowCreateApprover()
    # 本环节需要操作人的名字
    ent.ApproverName = '李四'
    # 本环节需要操作人的手机号
    ent.ApproverMobile = '15987654321'
    # 本环节需要企业操作人的企业名称，请注意此处的企业名称要是真实有效的，企业需要在电子签平台进行注册且签署人有加入该企业方能签署。
    # 注：如果该企业尚未注册，或者签署人尚未加入企业，合同仍然可以发起
    ent.OrganizationName = 'XXXXX公司'
    # 合同发起后是否短信通知签署方进行签署：sms - -短信，none - -不通知
    ent.NotifyType = 'sms'

    approvers.append(server_ent)
    approvers.append(person)
    approvers.append(ent)
    req.Approvers = approvers

    # 客户端Token，保持接口幂等性, 最大长度64个字符
    # 注意：传入相同的token会返回相同的结果，若无需要请不要进行传值！
    # req.ClientToken = '*********token*******'

    # 发送类型：
    # true：无序签
    # false：有序签
    # 注：默认为false（有序签），请和模板中的配置保持一致。如果传值不一致会以模板中设置的为准！
    req.Unordered = False

    # 用户自定义字段，回调的时候会进行透传，长度需要小于20480
    req.UserData = 'UserData'

    # 签署流程的签署截止时间。
    # 值为unix时间戳, 精确到秒, 不传默认为当前时间一年后
    req.DeadLine = int(time.time()) + 7 * 24 * 3600

    response = client.CreateFlow(req)
    print(response)


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
