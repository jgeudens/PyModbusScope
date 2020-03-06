"""
Script for automating ModbusScope
"""

from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.keyboard import send_keys

class ModbusScope:
    ''' API class for ModbusScope '''

    def __init__(self, path='ModbusScope.exe'):
        ''' Create an API object that can control a single instance of ModbusScope '''
        try:
             self.app = Application(backend="uia").connect(title=u'ModbusScope', class_name = u'ModbusScope')
        except ElementNotFoundError:
            try:
                self.app = Application(backend="uia").start(path)
            except ElementNotFoundError:
                raise RuntimeError("ModbusScope is not running or in PATH")

        self.main_window = self.app['ModbusScope.*']
        self.main_window.set_focus()
        #self.app['ModbusScope.*'].print_control_identifiers()

    def load_project(self, file, path=""):
        ''' Load a project (.mbs) file from the given absolute or relative path '''
        self.main_window.set_focus()
        self.main_window.toolBar.LoadProjectFile.click_input()
        if path is not "":
            self.main_window.SelectMbsFile.BestandsNaamEdit.type_keys(path, with_spaces=True)
            send_keys("{ENTER}")

        self.main_window.SelectMbsFile.BestandsNaamEdit.type_keys(file, with_spaces=True)
        send_keys("{ENTER}")

    def start_logging(self):
        ''' Start logging - Some registers must be added '''
        self.main_window.set_focus()
        self.main_window.toolBar.StartLogging.click_input()

    def stop_logging(self):
        ''' Stop the current logging '''
        self.main_window.set_focus()
        self.main_window.toolBar.StopLogging.click_input()

    def add_register(self, address):
        ''' Add a register at the given address '''
        self.main_window.toolBar.RegisterSettings.click_input()
        self.main_window.RegisterSettings.AddNewRegister.click_input()
        self.main_window.RegisterSettings.print_control_identifiers()

    def about(self):
        ''' Open the About menu '''
        self.main_window.Menu2.menu_select("? -> About")

    def quit(self):
        ''' Open the About menu '''
        self.app.kill()

    def take_screenshot(self, name):
        ''' take screenshot '''
        img = self.main_window.capture_as_image()
        img.save(name)
