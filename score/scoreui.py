#import pygame
class ScoreUI:
    def __init__(self, score_system):
        self.__score_system = score_system

    def update_ui(self):
        score = self.__score_system.get_score()
        #Send the score to the label that displays the score.


