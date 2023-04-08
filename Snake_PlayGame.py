'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from Snake_Snake import *
from Snake_DeathEvents import DeathEventsClass
from Snake_WindowsOpen import WindowsOpenClass
from Snake_Coordinate import CoordinateClass
from Snake_DataInput import DataInputClass
from Snake_Event import ProccessEventClass
ClassInput=DataInputClass()
ClassInput.DataFileInput()
ClassWindows=WindowsOpenClass()
ClassWindows.WindowsOpen()
ClassCoordinateRow = SnakeCoordinateRowClass()
level=0
ClassProcessEvent=ProccessEventClass(level)
ClassSnake=SnakeClass()
ClassDeath=DeathEventsClass()
class SnakePlayGameClass:
    def __init__(self):
        self.apple = CoordinateClass(1,1)
        ClassWindows.ui.set_animation_speed(6)
        self.level=0
        self.wall_x=0
        self.wall_y=0
        ClassSnake.AppleCoordinate(ClassWindows.ui,self.apple,self.level)
    def SnakePlay(self):
        ClassWindows.ui.clear()
        for coordinates in (ClassCoordinateRow.coordinate_row):
            ClassWindows.ui.place(coordinates.x, coordinates.y, ClassWindows.ui.SNAKE)
        self.snake_head = ClassCoordinateRow.coordinate_row[-1]
        self.snake_head_coordinate = CoordinateClass(self.snake_head.x + ClassProcessEvent.direction_x,
                                                     self.snake_head.y + ClassProcessEvent.direction_y)
        ClassCoordinateRow.AddCoordinate(self.snake_head_coordinate)
        ClassSnake.PageTransition(self.snake_head_coordinate)
        '''Yilanin ilerlemesini sagliyor'''
        ClassWindows.ui.place(self.apple.x, self.apple.y, ClassWindows.ui.FOOD)
        '''elma yerlestiriliyor'''
        for input in range(1,len(ClassInput.input_data[self.level])):
            if input ==1:
                self.wall_x =   ClassInput.input_data[self.level][input].split("=")[2].split(" ")[0]
                self.wall_y = ClassInput.input_data[self.level][input].split("=")[2].split(" ")[1]
            else:
                self.wall_x=ClassInput.input_data[self.level][input].split(" ")[0]
                self.wall_y = ClassInput.input_data[self.level][input].split(" ")[1]
            ClassWindows.ui.place(int(self.wall_x), int(self.wall_y), ClassWindows.ui.WALL)
            '''duvarlar yerlestiriliyor'''
            ClassDeath.HitWall(ClassWindows.ui, self.snake_head, self.wall_x, self.wall_y)
            '''Duvara carpma olayini kotrol etmek icin SelfBump def'ine gidiyor'''
        ClassWindows.ui.show()
        ClassDeath.SelfBump(ClassWindows.ui,self.snake_head,ClassCoordinateRow.coordinate_row)
        '''Kendine carpma olayini kotrol etmek icin SelfBump def'ine gidiyor'''
        if not ClassSnake.EatingApple(self.apple,ClassCoordinateRow.coordinate_row):
            ClassCoordinateRow.coordinate_row.remove(ClassCoordinateRow.coordinate_row[0])
        else:
            self.level+=1
            if self.level<4:
                self.coordinate2 = ClassInput.input_data[self.level][0]
                self.coordinate1 = ClassInput.input_data[self.level][1].split("=")[0]
            ClassProcessEvent.__init__(self.level)
            ClassCoordinateRow.coordinate_row=[]
            ClassCoordinateRow.AddCoordinate(CoordinateClass(int(self.coordinate1.split(" ")[0]), int(self.coordinate1.split(" ")[1])))
            ClassCoordinateRow.AddCoordinate(CoordinateClass(int(self.coordinate2.split(" ")[0]), int(self.coordinate2.split(" ")[1])))
            ClassSnake.AppleCoordinate(ClassWindows.ui,self.apple, self.level)
        '''elmayi yeme olayi kontrol ediliyor'''
ClassPlay=SnakePlayGameClass()
while ClassPlay.level<4:
    event = ClassWindows.ui.get_event()
    ClassProcessEvent.ProcessEvent(event)
    ClassPlay.SnakePlay()


