'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from Snake_DataInput import DataInputClass
ClassInput=DataInputClass()
ClassInput.DataFileInput()
class ProccessEventClass:
    def __init__(self,level):
        if level<4:
            self.direction = ClassInput.input_data[level][1].split("=")[1]
        '''input_data[level][1]'da bulunan yon direction'e aktarilir'''
        self.direction_x = 1
        self.direction_y = 0
    def ProcessEvent(self,event):
        if event.name == 'alarm':
            self.ProcessAlarm(event.data)
        elif event.name == 'arrow':
            self.ProcessArrow(event.data)
    def ProcessArrow(self,data):
        '''ilk gelen yonler'''
        if data == 'L':
            '''sol yonu'''
            self.direction = 'L'
        elif data == 'R':
            '''sag yonu'''
            self.direction = 'R'
        elif data == 'U':
            '''yukari yonu'''
            self.direction = 'U'
        elif data == 'D':
            '''asagi yonu'''
            self.direction = 'D'
    def ProcessAlarm(self,data):
        if data == 'refresh':
            self.SnakeProgression()
    def SnakeProgression(self):
        '''tuslarla gidilen yonler'''
        if self.direction == 'L':
            self.direction_x = -1
            self.direction_y = 0
        elif self.direction == 'R':
            self.direction_x = 1
            self.direction_y = 0
        elif self.direction == 'U':
            self.direction_x = 0
            self.direction_y = -1
        elif self.direction == 'D':
            self.direction_x = 0
            self.direction_y = 1
