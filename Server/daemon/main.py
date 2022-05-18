import asyncio
import warnings
        
class TimeMachineDaemon():
    """获取指定时间的存档、启动容器进程
    """
    def __init__(self):
        
        pass
    
    def get_time_slice(self, time_slice):
        
        cfs = CloudFileSystem("./TENCENT_KEY")



class CloudFileSystem():
    def __init__(self, config_path):
        
        try:
            with open(path, mode='rt') as f:
                self.api_id, self.api_key = f.readlines()
        except IOError as err:
            warnings.warn('IOError, check if TENCENT_KEY file is exsit')
            raise err
        
    def restore_from_snapshot(self, name):
        """从快照新建文件系统
        
            name: 快照名字
        
        """
        

