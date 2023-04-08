'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
import time
class DeathEventsClass:
    def SelfBump(self,Snake_ui,snake_head,coordinate_row):
        for coordinates in coordinate_row[:-1]:
            snake_head = coordinate_row[-1]
            if coordinates.x == snake_head.x and coordinates.y == snake_head.y:
                self.SnakeDeath(Snake_ui)
    '''Yilan kendine carpinca SnakeDeath'e geciyor'''
    def HitWall(self,Snake_ui,snake_head,wall_x,wall_y):
        if int(wall_x) == snake_head.x and int(wall_y) == snake_head.y:
            self.SnakeDeath(Snake_ui)
    '''Yilan duvara carpinca SnakeDeath'e geciyor'''
    def SnakeDeath(self,Snake_ui):
        Snake_ui.print_("\n\t\t\t\t    GAME OVER\n\n\n\t\t\t          YOU LOST GAME")
        time.sleep(1)
        Snake_ui.close()
    '''Game over mesaji verip pencereyi kapatiyor'''