from turtle import Turtle


class Snake:

    def __init__(self): 
        self.head = Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.pu()

        self.snake_body = []
        self.snake_body.append(self.head)

    def move(self):
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)
        self.head.forward(20)

     
    def create_body(self):
        for square in range(1, 3):
            body = Turtle()
            body.shape("square")
            body.color("white")
            body.pu()
            body.setpos(0 - (square*20), 0)
            self.snake_body.append(body)

    def add_segment(self):
        body_extension = Turtle()
        body_extension.shape("square")
        body_extension.color("white")
        body_extension.pu()
        body_extension.goto(self.snake_body[-1].position())
        self.snake_body.append(body_extension)     

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        # Move all current segments off screen
        for segment in self.snake_body:
            segment.goto(1000, 1000)

        self.snake_body.clear()

        # Reset the existing head
        self.head.goto(0, 0)
        self.head.setheading(0)

        # Put the head back in the list
        self.snake_body.append(self.head)
        self.create_body()