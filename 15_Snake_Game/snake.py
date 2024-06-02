from turtle import Turtle
Move_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    "Create snake class"
    def __init__(self):
        self.snake_body = []
        self.change_x_axes = 0
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for _ in range(3):
            self.add_snake_body()

    def add_snake_body(self):
        "Create snake body objects and append it the snake_body list"
        new_snake_body = Turtle(shape="square") # Creating snake body object (turtle object)
        new_snake_body.color("white") # set snake body color to white
        new_snake_body.penup()
        new_snake_body.goto(x=0 + self.change_x_axes, y=0) # place snake body side by side
        self.snake_body.append(new_snake_body) # append newly created snake body object to list
        self.change_x_axes -= 20
        # for _ in range(3):
        #     new_snake_body = Turtle(shape="square") # Creating snake body object (turtle object)
        #     new_snake_body.color("white") # set snake body color to white
        #     new_snake_body.penup()
        #     new_snake_body.goto(x=0 + self.change_x_axes, y=0) # place snake body side by side
        #     self.snake_body.append(new_snake_body) # append newly created snake body object to list
        #     self.change_x_axes -= 20
    
    # def extend_body_length(self):
    #     self.add_snake_body()

    def move(self):
        "Move the snake forward."
        for body_part_num in range(len(self.snake_body)-1, 0, -1):
            x_axes = self.snake_body[body_part_num - 1].xcor()
            y_axes = self.snake_body[body_part_num - 1].ycor()
            self.snake_body[body_part_num].goto(x_axes, y_axes)
        self.snake_body[0].forward(Move_DISTANCE)
        
        # self.snake_body[0].left(10)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
