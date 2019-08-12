
def check_index(key):
    """
    指定的键是否可以接受索引
    键必须是非负整数，才是可以接受的，如果不是整数，将引发TypeError异常：如果是负数
    将引发IndexError(因为这个序列的长度是无穷的）
    
    """
    if not isinstance(key, int):raise TypeError
    if key < 0:raise IndexError

class AritthmeticSequence:
    def __init__(self, start = 0, step = 1):
        """
        初始化这个算数序列
        :param start: 序列中的第一个值
        :param step: 两个相邻的差
        changed 一个字典，包含用户修改后的值
        """
        self.start = start #存储起始值
        self.step = step
        self.changed = {}
    def __getitem__(self, key):
        """
        从算数序列中获取一个元素
        :param ket: 
        :return: 
        """
        check_index(key)
        try: return self.changed[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self, key, value):
        """
        修改算数序列中的元素
        :param key: 
        :param value: 
        :return: 
        """
        check_index(key)
        self.changed[key] = value


s = AritthmeticSequence(1, 2)
print(s[4])
