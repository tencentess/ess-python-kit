import base64

from tencentcloud.ess.v20201111.models import UploadFilesRequest, Caller, UploadFile

from api.common import get_client_instance
from config import Config


def upload_files(operator_user_id, file_base64, filename):
    """
    UploadFiles 此接口（UploadFiles）用于文件上传。

    官网文档：https://cloud.tencent.com/document/api/1323/73066

    适用场景：用于生成pdf资源编号（FileIds）来配合“用PDF创建流程”接口使用，使用场景可详见“用PDF创建流程”接口说明。
    调用是请注意此处的 Endpoint 和其他接口不同
    """

    # 构造客户端调用实例
    # 文件上传的endPoint为file域名
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.file_service_end_point)

    # 构造请求体
    req = UploadFilesRequest()

    # 调用方用户信息，参考通用结构
    caller = Caller()
    caller.UserId = operator_user_id
    req.Caller = caller

    # 文件对应业务类型，用于区分文件存储路径：
    # 1. TEMPLATE - 模板； 文件类型：.pdf/.html
    # 2. DOCUMENT - 签署过程及签署后的合同文档 文件类型：.pdf/.html
    # 3. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
    req.BusinessType = "DOCUMENT"

    # 上传文件内容
    file = UploadFile()
    # Base64编码后的文件内容
    file.FileBody = file_base64.decode("utf-8")
    # 文件名，最大长度不超过200字符
    file.FileName = filename

    req.FileInfos = [file]

    response = client.UploadFiles(req)
    return response


def to_base64(filepath):
    with open(filepath, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)
        return base64_data


if __name__ == '__main__':
    """
    上传文件调用样例
    """

    try:
        # 将文件处理为Base64编码后的文件内容
        _filepath = "../testdata/test.pdf"
        _file_base64 = to_base64(_filepath)

        # 文件名，最大长度不超过200字符
        _filename = 'test.pdf'

        resp = upload_files(Config.operator_user_id, _file_base64, _filename)
        print(resp)
    except Exception as e:
        print(e)
