import os
'''读取Excel文件的方法'''
def data_dir(data=None,fileName=None):
    '''查找文件的目录'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)
