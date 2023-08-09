from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.goto(0,270)
        with open ("highscore.txt","r") as file:
            self.highscore = int(file.read())
        self.score = -1
        self.refresh_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",move = False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open ("highscore.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = -1
        self.refresh_score()


    def refresh_score(self):
        self.score += 1
        self.update_scoreboard()
