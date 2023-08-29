from tencentcloud.ess.v20201111.models import CreateDocumentRequest, UserInfo, FormField

from api.common import get_client_instance
from config import Config


def create_document(operator_user_id, flow_id, template_id, file_name, form_fields):

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateDocumentRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = operator_user_id
    req.Operator = user_info

    req.FileNames = [file_name]

    req.FlowId = flow_id

    req.TemplateId = template_id

    req.FormFields = form_fields

    response = client.CreateDocument(req)
    return response

def create_document_extended():

    # 构造客户端调用实例
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.endpoint)

    # 构造请求体
    req = CreateDocumentRequest()

    # 调用方用户信息，参考通用结构
    user_info = UserInfo()
    user_info.UserId = Config.operator_user_id
    req.Operator = user_info

    req.FlowId = '**********************'

    req.FileNames = ['filename']

    req.TemplateId = '**********************'

    # 这里为需要发起方填写的控件进行赋值操作，推荐使用ComponentName + ComponentValue的方式进行赋值，ComponentName即模板编辑时设置的控件名称
    form_field_1 = FormField()
    form_field_1.ComponentName = '单行文本'
    form_field_1.ComponentValue = '文本内容'
    form_field_2 = FormField()
    form_field_2.ComponentName = '勾选框'
    form_field_2.ComponentValue = 'true'
    req.FormFields = [form_field_1, form_field_2]

    req.NeedPreview = True

    req.PreviewType = 1

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
