# -- coding:utf8 --
import hashlib
import hmac

# 回调消息验证签名

def sign(value, key):
    j = hmac.new(key.encode('utf-8'), value.encode('utf-8'), digestmod=hashlib.sha256)
    ret = j.hexdigest()
    return ret


# 回调消息体
payload = "**********"
# secretToken 创建应用号时配置的
secretToken = "**********"

# 1. 取出header [Content-Signature]
signFromHeader = "***********"

# 2. 验证签名
signHash = 'sha256=' + sign(payload, secretToken)

# 3. 如果验证通过，继续处理。如果不通过，忽略该请求
print(signHash == signFromHeader)
