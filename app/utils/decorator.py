"""
    Log的装饰器
"""


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

    # __isinstance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not cls.__isinstance:
    #         cls.isinstance = object.__new__(cls)
    #         return cls.__isinstance
    #     else:
    #         return cls.__isinstance

