'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from Snake_CoordinateRow import *
from Snake_WindowsOpen import WindowsOpenClass
from Snake_DataInput import DataInputClass
ClassInput=DataInputClass()
ClassInput.DataFileInput()
ClassWindows=WindowsOpenClass()
ClassCoordinateRow = SnakeCoordinateRowClass()
class SnakeClass:
    def PageTransition(self,head_coordinate):
        if head_coordinate.x >= ClassWindows.width:
            head_coordinate.x = 0
        elif head_coordinate.x <= -1:
            head_coordinate.x = ClassWindows.width - 1
        elif head_coordinate.y >= ClassWindows.height:
            head_coordinate.y = 0
        elif head_coordinate.y <= -1:
            head_coordinate.y = ClassWindows.height - 1
        '''yilanin pencere sonundan basina gecmesini sagliyor'''
    def AppleCoordinate(self,Snake_ui,apple,level):
        self.wall_apple = 0
        self.coordinate_apple = 0
        x = Snake_ui.random(ClassWindows.width)
        y = Snake_ui.random(ClassWindows.height)
        '''elmayi pencereye rastgele yelestiriyor '''
        for coordinate in ClassCoordinateRow.coordinate_row:
            if coordinate.x == x and coordinate.y == y:
                self.coordinate_apple = 1
        '''elma yilanin ustunde mi diye bakiliyor'''
        if level<4:
            for input in range(2, len(ClassInput.input_data[level])):
                self.wall_x = ClassInput.input_data[level][input].split(" ")[0]
                self.wall_y = ClassInput.input_data[level][input].split(" ")[1]
                if self.wall_x == str(x) and self.wall_y == str(y):
                    self.wall_apple = 1
            '''elma duvarin ustunde mi diye bakiliyor'''
        Snake_ui.clear()
        if self.wall_apple == 0 and self.coordinate_apple == 0:
            '''elma duvarin veya yilanin ustunde degilse elma yerlestiriliyor'''
            apple.x = x
            apple.y = y
        else:
            '''ustunde ise yeniden donguye giriyor'''
            self.AppleCoordinate(Snake_ui,apple,level)
    def EatingApple(self,apple,coordinate_row):
        for coordinates in coordinate_row:
            if coordinates.x == apple.x and coordinates.y == apple.y:
                return True
            '''yilanin elmayi yiyip yemedigini kotrol ediyor'''
        return False