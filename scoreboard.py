from turtle import Turtle


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-10, 275)
        self.score = 0
        self.highscore = 0
        with open('file.txt') as file:
            self.highscore = int(file.read())

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score}  Highscore:{self.highscore}', align='center', font=('Ariel', 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Users/Aranjeeta Parihar/Desktop/file.txt', mode='a') as file:
                file.write(f'{self.highscore}')
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(-70, 0)
    #     self.write('GAME OVER', font=('Ariel', 20, 'normal') )
    #
