from turtle import Turtle


class Snake:

    def __init__(self): 
        self.head = Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.pu()

        self.snake_body = []
        self.snake_body.append(self.head)
        print(self.snake_body)

    def move(self):
        for segment_num in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[segment_num -1].xcor()
            new_y = self.snake_body[segment_num -1].ycor()
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

    # def move_up(self):
    #     self.head.setheading(90)

    # def move_down(self):
    #     self.head.setheading(180)
    
    def move_right(self):
        self.head.right(90)

    def move_left(self):
        self.head.left(90)



