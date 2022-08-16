from tencentcloud.ess.v20201111.models import CreateFlowByFilesRequest, UserInfo

from api.common import get_client_instance
from config import Config


def create_flow_by_file_id(operator_user_id, flow_name, approvers, file_id):
    """
    此接口（CreateFlowByFiles）用来通过上传后的pdf资源编号来创建待签署的合同流程。
    适用场景1：适用非制式的合同文件签署。一般开发者自己有完整的签署文件，可以通过该接口传入完整的PDF文件及流程信息生成待签署的合同流程。
    适用场景2：可通过改接口传入制式合同文件，同时在指定位置添加签署控件。可以起到接口创建临时模板的效果。如果是标准的制式文件，建议使用模板功能生成模板ID进行合同流程的生成。
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

        resp = create_flow_by_file_id(Config.operator_user_id, _flow_name, _approvers, _file_id)
        print(resp)

    except Exception as e:
        print(e)
