class BaseResponse(object):
    """
    一个减少字典操作的类
    """
    def __init__(self):
        self.code = 1000
        self.data = None
        self.error = None
    @property
    def dict(self):
        return self.__dict__

