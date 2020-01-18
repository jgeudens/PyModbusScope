# PyModbusScope

A little toy project to control [ModbusScope](https://github.com/jgeudens/modbusscope) from the commandline.

## Pre-condition
Make sure to use Python 3.7.4 (or lower). Python 3.8.1 and Python 3.7.5 or higher currently have an issue: https://github.com/pywinauto/pywinauto/issues/868

## Installing
1. Make sure [ModbusScope](https://github.com/jgeudens/modbusscope) is installed.
2. Install script in a venv
```
python -m venv venv
venv\Scripts\Activate.bat
pip install -e .
    or during dev
pip install -r requirements.txt
```


## Usage
### Add ModbusScope to PATH
```batch
set PATH=C:\Program Files\ModbusScope;%PATH%
```
```ps
$env:Path += ";C:\Program Files\ModbusScope"
```
### Logging with given mbs file for 5 seconds
```python
from time import sleep
from pymodbusscope import ModbusScope

mbs = ModbusScope()
mbs.load_project('myproject.mbs')
mbs.start_logging()
sleep(5)
mbs.stop_logging()
```