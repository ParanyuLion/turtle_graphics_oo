import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self):
        turtle.penup()
        turtle.goto(random.randint(-300, 300), random.randint(-200, 200))
        turtle.setheading(self.orientation)


class EmbeddedPolygon(Polygon):
    def draw(self, num_levels, reduction_ratio):
        for i in range(num_levels):
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.num_sides):
                turtle.forward(self.size)
                turtle.left(360 / self.num_sides)
            turtle.penup()
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio


class PolygonArt:
    def __init__(self):
        pass
    def run(self, choice):

        if choice == 1:
            for i in range(30):
                Triangles = Polygon(3, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255),
                                           random.randint(0, 255), random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Triangles.draw()
                Triangles.move()
            turtle.done()
        elif choice == 2:
            for i in range(30):
                Rectangle = Polygon(4, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Rectangle.draw()
                Rectangle.move()
            turtle.done()
        elif choice == 3:
            for i in range(30):
                Pentagon = Polygon(5, size=random.randint(50, 150),
                                   orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Pentagon.draw()
                Pentagon.move()
            turtle.done()
        elif choice == 4:
            for i in range(10):
                Triangles = Polygon(3, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Triangles.draw()
                Triangles.move()
                Rectangle = Polygon(4, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Rectangle.draw()
                Pentagon = Polygon(5, size=random.randint(50, 150),
                                   orientation=random.randint(0, 90),
                                   location=[random.randint(-300, 300), random.randint(-200, 200)],
                                   color=(random.randint(0, 255), random.randint(0, 255),
                                          random.randint(0, 255)),
                                   border_size=random.randint(1, 10))
                Pentagon.draw()
                Pentagon.move()
            turtle.done()
        elif choice == 5:
            for i in range(30):
                Triangles = EmbeddedPolygon(3, size=random.randint(50, 150),
                                            orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Triangles.draw(3,0.618)
                Triangles.move()
            turtle.done()
        elif choice == 6:
            for i in range(30):
                Square = EmbeddedPolygon(4, size=random.randint(50, 150),
                                         orientation=random.randint(0, 90),
                                            location=[random.randint(-300, 300), random.randint(-200, 200)],
                                            color=(random.randint(0, 255), random.randint(0, 255),
                                                   random.randint(0, 255)),
                                            border_size=random.randint(1, 10))
                Square.draw(3, 0.618)
                Square.move()
            turtle.done()
        elif choice == 7:
            for i in range(30):
                Pentagon = EmbeddedPolygon(5, size=random.randint(50, 150),
                                           orientation=random.randint(0, 90),
                                            location=[random.randint(-300, 300), random.randint(-200, 200)],
                                            color=(random.randint(0, 255), random.randint(0, 255),
                                                   random.randint(0, 255)),
                                            border_size=random.randint(1, 10))
                Pentagon.draw(3, 0.618)
                Pentagon.move()
            turtle.done()
        elif choice == 8:
            for i in range(10):
                Triangles = EmbeddedPolygon(3, size=random.randint(50, 150),
                                            orientation=random.randint(0, 90),
                                            location=[random.randint(-300, 300), random.randint(-200, 200)],
                                            color=(
                                            random.randint(0, 255), random.randint(0, 255),
                                            random.randint(0, 255)),
                                            border_size=random.randint(1, 10))
                Triangles.draw(3, 0.618)
                Triangles.move()
                Square = EmbeddedPolygon(4, size=random.randint(50, 150),
                                         orientation=random.randint(0, 90),
                                         location=[random.randint(-300, 300), random.randint(-200, 200)],
                                         color=(random.randint(0, 255), random.randint(0, 255),
                                                random.randint(0, 255)),
                                         border_size=random.randint(1, 10))
                Square.draw(3, 0.618)
                Square.move()
                Pentagon = EmbeddedPolygon(5, size=random.randint(50, 150),
                                           orientation=random.randint(0, 90),
                                           location=[random.randint(-300, 300), random.randint(-200, 200)],
                                           color=(
                                           random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                           border_size=random.randint(1, 10))
                Pentagon.draw(3, 0.618)
                Pentagon.move()
            turtle.done()
        elif choice == 9:
            for i in range(4):
                Triangles = Polygon(3, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Triangles.draw()
                Triangles.move()
                Rectangle = Polygon(4, size=random.randint(50, 150),
                                    orientation=random.randint(0, 90),
                                    location=[random.randint(-300, 300), random.randint(-200, 200)],
                                    color=(random.randint(0, 255), random.randint(0, 255),
                                           random.randint(0, 255)),
                                    border_size=random.randint(1, 10))
                Rectangle.draw()
                Pentagon = Polygon(5, size=random.randint(50, 150),
                                   orientation=random.randint(0, 90),
                                   location=[random.randint(-300, 300), random.randint(-200, 200)],
                                   color=(random.randint(0, 255), random.randint(0, 255),
                                          random.randint(0, 255)),
                                   border_size=random.randint(1, 10))
                Pentagon.draw()
                Pentagon.move()
                Triangles = EmbeddedPolygon(3, size=random.randint(50, 150),
                                            orientation=random.randint(0, 90),
                                            location=[random.randint(-300, 300), random.randint(-200, 200)],
                                            color=(
                                                random.randint(0, 255), random.randint(0, 255),
                                                random.randint(0, 255)),
                                            border_size=random.randint(1, 10))
                Triangles.draw(3, 0.618)
                Triangles.move()
                Square = EmbeddedPolygon(4, size=random.randint(50, 150),
                                         orientation=random.randint(0, 90),
                                         location=[random.randint(-300, 300), random.randint(-200, 200)],
                                         color=(random.randint(0, 255), random.randint(0, 255),
                                                random.randint(0, 255)),
                                         border_size=random.randint(1, 10))
                Square.draw(3, 0.618)
                Square.move()
                Pentagon = EmbeddedPolygon(5, size=random.randint(50, 150),
                                           orientation=random.randint(0, 90),
                                           location=[random.randint(-300, 300), random.randint(-200, 200)],
                                           color=(
                                               random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255)),
                                           border_size=random.randint(1, 10))
                Pentagon.draw(3, 0.618)
                Pentagon.move()
            turtle.done()


choice = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
PolygonArt = PolygonArt()
PolygonArt.run(choice)
