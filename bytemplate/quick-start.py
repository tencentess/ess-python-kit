if __name__ == '__main__':
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from api.create_flow_by_template_directly import create_flow_by_template_directly
    from api.describe_file_urls import describe_file_urls
    from config import Config
    from bytemplate import build_person_flow_create_approver

    try:
        # Step 1
        # 定义合同名
        flow_name = '我的第一个合同'

        # 构造签署人
        approvers = []

        # 此块代码中的approvers仅用于快速发起一份合同样例，非正式对接用
        person_name = "****************"  # 个人签署方的姓名
        person_mobile = "****************"  # 个人签署方的手机号

        approvers.append(build_person_flow_create_approver(person_name, person_mobile))

        # 如果是正式接入，需使用这里注释的approvers。请进入BuildFlowCreateApprovers函数内查看说明，构造需要的场景参数
        # approvers = BuildFlowCreateApprovers()

        # Step 2
        # 发起合同
        resp = create_flow_by_template_directly(Config.operator_user_id, flow_name, approvers)

        # 返回合同Id
        print("您创建的合同Id为：")
        print(resp['FlowId'])
        print("\r\n")

        # 返回签署的链接
        print("签署链接（请在手机浏览器中打开）为：")
        print(resp['SchemeUrl'])
        print("\r\n")

        # Step 3
        # 下载合同
        file_url_resp = describe_file_urls(Config.operator_user_id, [resp['FlowId']], "FLOW")
        # 返回合同下载链接
        print("请访问以下地址下载您的合同：")
        print(file_url_resp.FileUrls[0].Url)

    except Exception as e:
        print(e)
