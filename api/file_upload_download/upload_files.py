import base64

from tencentcloud.ess.v20201111.models import UploadFilesRequest, Caller, UploadFile

from api.common import get_client_instance
from config import Config


def upload_files(operator_user_id, file_base64, filename):

    # 构造客户端调用实例
    # 文件上传的endPoint为file域名
    client = get_client_instance(Config.secret_id, Config.secret_key, Config.file_service_end_point)

    # 构造请求体
    req = UploadFilesRequest()

    # 调用方用户信息，参考通用结构
    caller = Caller()
    caller.UserId = operator_user_id
    req.Caller = caller

    req.BusinessType = "DOCUMENT"

    file = UploadFile()

    file.FileBody = file_base64.decode("utf-8")

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

        _filename = 'test.pdf'

        resp = upload_files(Config.operator_user_id, _file_base64, _filename)
        print(resp)
    except Exception as e:
        print(e)
