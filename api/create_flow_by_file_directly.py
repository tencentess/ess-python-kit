from api.create_flow_by_files import create_flow_by_file_id
from api.create_schema_url import create_schema_url
from api.upload_files import upload_files


def create_flow_by_file_directly(operator_user_id, file_base64, flow_name, approvers):
    """
    通过文件base64直接发起签署流程，返回flowId
    """

    # 上传文件获取fileId
    upload_resp = upload_files(operator_user_id, file_base64, flow_name)
    file_id = upload_resp.FileIds[0]

    # 创建签署流程
    create_flow_resp = create_flow_by_file_id(operator_user_id, flow_name, approvers, file_id)
    flow_id = create_flow_resp.FlowId

    # 获取签署链接
    scheme_resp = create_schema_url(operator_user_id, flow_id, 1)
    scheme_url = scheme_resp.SchemeUrl

    return {'FlowId': flow_id, "SchemeUrl": scheme_url}
