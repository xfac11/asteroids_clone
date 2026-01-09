class ScoreSystem:
    def __init__(self, initial_score=0):
        self.__score = initial_score
    def add(self, score_to_add):
        if score_to_add <= 0:
            raise ValueError("Score_to_add cannot be negative or zero")
        if not isinstance(score_to_add, int):
            raise TypeError("Score_to_add has to be an integer")
        self.__score += score_to_add
        return True
    
    def remove(self, score_to_remove):
        if score_to_remove <= 0:
            raise ValueError("Score_to_remove cannot be negative or zero")
        if not isinstance(score_to_remove, int):
            raise TypeError("Score_to_remove has to be an integer")
        self.__score -= score_to_remove
        self.__score = max(self.__score, 0)
        return True
    
    def get_score(self):
        return self.__score

