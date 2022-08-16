class _ConstConfig(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        self.__dict__[name] = value


# 基础配置，调用API之前必须填充的参数
Config = _ConstConfig()

# 调用API的密钥对，通过腾讯云控制台获取
Config.secret_id = '****************'
Config.secret_key = '****************'

# operatorUserId: 经办人Id，电子签控制台获取
Config.operator_user_id = '****************'

# 企业方静默签用的印章Id，电子签控制台获取
Config.server_sign_seal_id = "****************"

# 模板Id，电子签控制台获取，仅在通过模板发起时使用
Config.template_id = "****************"

# API域名，现网使用 ess.tencentcloudapi.com
Config.endpoint = 'ess.test.ess.tencent.cn'

# 文件服务域名，现网使用 file.ess.tencent.cn
Config.file_service_end_point = 'file.test.ess.tencent.cn'
