# 回调解密 - 旧合同结构

class FlowInfo(object):
    """
    回调数据对象 FlowInfo
    """

    def __init__(self, data):
        """
        将回调数据转化为封装对象
        """
        # string 流程编号。
        self.flow_id = data["FlowId"]

        # string 使用的文档 ID。
        self.document_id = data["DocumentId"]

        # string 回调的类型：
        # sign：签署回调
        # review：审核回调
        self.callback_type = data["CallbackType"]

        # string 流程名称。
        self.flow_name = data["FlowName"]

        # string 流程的类型。
        self.flow_type = data["FlowType"]

        # string 流程的描述。
        self.flow_description = data["FlowDescription"]

        # boolean 流程类型顺序：
        # true：为无序
        # false：为有序
        self.unordered = data["Unordered"]

        # integer 流程的创建时间戳。
        self.create_on = data["CreateOn"]

        # integer 流程的修改时间戳。
        self.updated_on = data["UpdatedOn"]

        # integer 流程的过期时间0为永远不过期。
        self.deadline = data["DeadLine"]

        # integer 流程现在的状态：
        # 1：待签署
        # 2：部分签署
        # 3：已拒签
        # 4：已签署
        # 5：已过期
        # 6：已撤销
        self.flow_callback_status = data["FlowCallbackStatus"]

        # string 本环节需要操作人 UserId。
        self.user_id = data["UserId"]

        # string 签署区 ID。
        self.recipient_id = data["RecipientId"]

        # string 动作：
        # start：发起
        # sign：签署
        # reject：拒签
        # cancel：取消
        # finish：结束
        # deadline：过期
        self.operate = data["Operate"]

        # string 创建的时候设置的透传字段。
        self.user_data = data["UserData"]

        # array 流程签约方列表。
        self.approvers = []
        approvers_str = data["Approvers"]
        for i in range(0, len(approvers_str)):
            self.approvers.append(Approver(approvers_str[i]))


class Approver(object):
    """
    FlowInfo 参数 Approver 结构
    """

    def __init__(self, data):
        """
        将回调数据转化为封装对象
        """

        # string 本环节需要操作人 UserId。
        self.user_id = data["UserId"]

        # string 签署区 ID。
        self.recipient_id = data["RecipientId"]

        # integer 参与者类型：
        # 0：企业
        # 1：个人
        # 3：企业静默签署
        self.approver_type = data["ApproverType"]

        # string 企业或者个人的名字。
        self.organization_name = data["OrganizationName"]

        # boolean 是否需要签名。
        self.required = data["Required"]

        # string 本环节需要操作人的名字。
        self.approver_name = data["ApproverName"]

        # string 本环节需要操作人的手机号。
        self.approver_mobile = data["ApproverMobile"]

        # string 签署人证件类型：
        # ID_CARD：身份证。
        # HONGKONG_AND_MACAO：港澳居民来往内地通行证。
        # HONGKONG_MACAO_AND_TAIWAN：港澳台居民居住证(格式同居民身份证)。
        self.approver_id_card_type = data["ApproverIdCardType"]

        # string 签署人证件类型。
        self.approver_id_card_number = data["ApproverIdCardNumber"]

        # integer 签署状态：
        # 2：待签署
        # 3：已签署
        # 4：已拒签
        # 5：已过期
        # 6：已撤销
        self.approve_callback_status = data["ApproveCallbackStatus"]

        # string 拒签的原因。
        self.approve_message = data["ApproveMessage"]

        # string 签署意愿方式，WEIXINAPP：人脸识别。
        self.verify_channel = data["VerifyChannel"]

        # integer 签约的时间。
        self.approve_time = data["ApproveTime"]


if __name__ == '__main__':
    """
    创建回调Key调用样例
    """
    from Crypto.Cipher import AES
    from base64 import b64decode
    import json

    try:
        # 此处填入CallbackUrlKey
        key = '******************'
        iv = key[0:16]

        # 加密方式
        method = AES.MODE_CBC

        # 获取推送的body内容，测试内容见：
        # https://cloud.tencent.com/document/product/1323/78890#.E5.9B.9E.E8.B0.83.E6.A0.B7.E4.BE.8B
        raw_data = "<callback-body>"

        # 解密后的明文，为json格式字符串，格式见：
        # https://cloud.tencent.com/document/product/1323/72309#.E5.9B.9E.E8.B0.83.E6.95.B0.E6.8D.AE.E6.9C.89.E5.93.AA.E4.BA.9B.E5.8F.82.E6.95.B0.E5.91.A2.EF.BC.9F
        cipher = AES.new(bytes(key, encoding='utf-8'), method, bytes(iv, encoding='utf-8'))
        plaintext = cipher.decrypt(b64decode(raw_data))

        # 对json格式字符串进行编码
        json_data = json.loads(plaintext)
        print(json.dumps(json_data, indent=4, sort_keys=True))

        # 解析为对象
        flow_info = FlowInfo(json_data)

        # 流程id
        flow_id = flow_info.flow_id

        # todo 获取参数&业务处理

        print("ok")

    except Exception as e:
        print(e)
