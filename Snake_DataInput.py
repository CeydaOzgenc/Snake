'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda ÖZgenç '''
class DataInputClass:
    def __init__(self):
        self.input_data=[]
    def DataFileInput(self):
        for level in range(4):
            self.input_data.insert(level,open("SnakeInput"+str(level+1)+".txt").read())
            ''' SnakeInput1.txt, SnakeInput2.txt,SnakeInput3.txt ve SnakeInput4.txt icindeki verileri input_data dizisine aktariyor '''
            self.input_data[level] = self.input_data[level].split("\n")