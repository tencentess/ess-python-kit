from tencentcloud.ess.v20201111.models import CreateDocumentRequest, UserInfo, FormField

from api.common import get_client_instance
from config import Config


def create_document(operator_user_id, flow_id, template_id, file_name, form_fields):
    """
    CreateDocument 创建电子文档

    官方文档：https://cloud.tencent.com/document/api/1323/70364

    适用场景：见创建签署流程接口。注：该接口需要给对应的流程指定一个模板id，并且填充该模板中需要补充的信息。是“发起流程”接口的前置接口。
    """

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateDocumentRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

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

def create_document_extended():
    """
    CreateDocumentExtended CreateDocument接口的详细参数使用样例，前面简要调用的场景不同，此版本旨在提供可选参数的填入参考。
    如果您在实现基础场景外有进一步的功能实现需求，可以参考此处代码。
    注意事项：此处填入参数仅为样例，请在使用时更换为实际值。
    """
    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateDocumentRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    # 签署流程编号, 由CreateFlow接口返回
    # 注意：注意每次创建电子文档前必须先创建流程，文档和流程为一对一的绑定关系！
    req.FlowId = '**********************'

    # 文件名列表, 单个文件名最大长度200个字符。目前仅支持单文件发起，此处传入任意自定义值即可
    req.FileNames = ['filename']

    # 用户上传的模板ID, 在控制台模版管理中可以找到
    # 如何创建模板见官网：https://cloud.tencent.com/document/product/1323/61357
    req.TemplateId = '**********************'

    # 这里为需要发起方填写的控件进行赋值操作，推荐使用ComponentName + ComponentValue的方式进行赋值，ComponentName即模板编辑时设置的控件名称
    form_field_1 = FormField()
    form_field_1.ComponentName = '单行文本'
    form_field_1.ComponentValue = '文本内容'
    form_field_2 = FormField()
    form_field_2.ComponentName = '勾选框'
    form_field_2.ComponentValue = 'true'
    req.FormFields = [form_field_1, form_field_2]

    # 是否需要生成预览文件
    # 默认不生成；
    # 预览链接有效期300秒；
    # 注意：此处生成的链接只能访问一次，访问过后即失效！
    req.NeedPreview = True

    # 预览链接类型 默认: 0 - 文件流, 1 - H5链接 注意: 此参数在NeedPreview 为true 时有效,
    req.PreviewType = 1

    # 客户端Token，保持接口幂等性, 最大长度64个字符
    # 注意：传入相同的token会返回相同的结果，若无需要请不要进行传值！
    # req.ClientToken = '*********token*******'

    response = client.CreateDocument(req)
    print(response)


if __name__ == '__main__':
    """
    创建电子文档调用样例
    """


    def pack_form_fields_example():
        """
        设置发起人填写控件样例
        """

        form_fields = []

        # 单行文本类型赋值 文本内容
        text = FormField()
        text.ComponentName("单行文本1")
        text.ComponentValue("单行文本内容")
        form_fields.append(text)

        # 多行文本类型赋值 文本内容
        multi_line_text = FormField()
        text.ComponentName("多行文本1")
        text.ComponentValue("多行文本内容")
        form_fields.append(multi_line_text)

        # 勾选框类型赋值 true/false
        checkbox = FormField()
        checkbox.ComponentName("勾选框1")
        checkbox.ComponentValue("true")
        form_fields.append(checkbox)

        # 选择器类型赋值 控制台选项值
        selector = FormField()
        selector.ComponentName("选择器1")
        selector.ComponentValue("选项一")
        form_fields.append(selector)

        # 附件类型赋值 UploadFiles接口上传返回的fileId
        attachment = FormField()
        attachment.ComponentName("详见附件1")
        attachment.ComponentValue("***********************")
        form_fields.append(attachment)

        return form_fields


    try:
        # 资源Id，由UploadFiles接口返回
        _flowId = '********************************'
        # 资源类型，2-doc 3-docx
        _template_id = '********************************'
        # 资源名称
        _file_name = '文件名'
        # 填写控件内容（可选）
        _form_fields = pack_form_fields_example()

        resp = create_document(Config.operator_user_id, _flowId, _template_id, _file_name, _form_fields)
        print(resp)
    except Exception as e:
        print(e)
