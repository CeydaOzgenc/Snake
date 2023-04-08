'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from ipy_lib import SnakeUserInterface
class WindowsOpenClass:
    def __init__(self):
        self.width = 32
        self.height = 24
        self.scale = 0.85
    def WindowsOpen(self):
        self.ui = SnakeUserInterface(self.width, self.height, self.scale)
        '''Grafik ekrani acilir'''
        self.ui.show()