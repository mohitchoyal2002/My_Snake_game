from turtle import Turtle
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        for i in starting_position:
            self.add_segment(i)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)  # the points are at centre of square
        self.segments.append(snake)

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()# list is cleared
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

