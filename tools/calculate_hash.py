import hashlib
from pysmx.SM3 import SM3


# 计算md5
def calc_md5(content):
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()


# 计算sha1
def calc_sha1(content):
    sha1 = hashlib.sha1()
    sha1.update(content)
    return sha1.hexdigest()


# 计算sha256
def calc_sha256(content):
    sha256 = hashlib.sha256()
    sha256.update(content)
    return sha256.hexdigest()


# 计算sm3
def calc_sm3(content):
    sm3 = SM3()
    sm3.update(content)
    return sm3.hexdigest()


if __name__ == "__main__":
    filepath = "/test/path/file.pdf"
    with open(filepath) as f:
        file_data = f.read().encode('utf-8')
        print("file_md5: %s" % calc_md5(file_data))
        print("file_sha1: %s" % calc_sha1(file_data))
        print("file_sha256: %s" % calc_sha256(file_data))
        print("file_sm3: %s" % calc_sm3(file_data))
