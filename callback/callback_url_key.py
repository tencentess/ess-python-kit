from random import randint


class CallbackUrlKey(object):
    @staticmethod
    def generate_key():
        return "{:04x}{:04x}{:04x}{:04x}{:04x}{:04x}{:04x}{:04x}".format(
            randint(0, 0xffff), randint(0, 0xffff),
            randint(0, 0xffff),
            randint(0, 0x0fff) | 0x4000,
            randint(0, 0x3fff) | 0x8000,
            randint(0, 0xffff), randint(0, 0xffff), randint(0, 0xffff)
        )


if __name__ == '__main__':
    """
    创建回调Key调用样例
    """
    try:
        print("生成key:\r\n")
        print(str.upper(CallbackUrlKey.generate_key()))
        print("\r\n")
    except Exception as e:
        print(e)
