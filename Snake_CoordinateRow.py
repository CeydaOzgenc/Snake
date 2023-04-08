'''Assignment: Snake
Created on 19 May. 2022
Author: Ceyda Özgenç '''
from Snake_Coordinate import CoordinateClass
class SnakeCoordinateRowClass:
    def __init__(self):
        self.coordinate_row = []
        self.AddCoordinate(CoordinateClass(0, 0))
        self.AddCoordinate(CoordinateClass(1, 0))
    def AddCoordinate(self, coordinate):
        self.coordinate_row.append(coordinate)
    '''Yilanina boyut eklemesi yapiliyor'''