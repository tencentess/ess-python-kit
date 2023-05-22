import time

from api.flow_management.create_document import create_document
from api.flow_management.create_flow import create_flow
from api.flow_management.create_schema_url import create_schema_url
from api.flow_management.start_flow import start_flow
from config import Config


def create_flow_by_template_directly(operator_user_id, flow_name, approvers):
    """
    通过模板发起签署流程，并查询签署链接
    """

    # 创建流程
    create_flow_resp = create_flow(operator_user_id, flow_name, approvers)
    flow_id = create_flow_resp.FlowId

    # 创建电子文档
    create_document(operator_user_id, flow_id, Config.template_id, flow_name, [])

    # 等待文档异步合成
    time.sleep(3)

    # 开启流程
    start_flow(operator_user_id, flow_id)

    # 获取签署链接
    scheme_resp = create_schema_url(operator_user_id, flow_id, 1)
    scheme_url = scheme_resp.SchemeUrl

    return {'FlowId': flow_id, "SchemeUrl": scheme_url}
