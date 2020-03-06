import os
from time import sleep
from pymodbusscope import ModbusScope



try:
    mbs = ModbusScope()

    mbs_path=os.path.dirname(os.path.abspath(__file__))

    #mbs.load_project(path=mbs_path, file='myproject.mbs')

    mbs.take_screenshot('modbusscope.png')

    '''
    mbs.start_logging()
    sleep(5)
    mbs.stop_logging()
    '''
    
except Exception as e:
    raise # reraises the exception

finally:
    mbs.quit()


