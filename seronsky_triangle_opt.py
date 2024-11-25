import turtle
import random

def draw_big_triangle(x1, y1, x2, y2, x3, y3):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.update()

def choose_apex(x1, y1, x2, y2, x3, y3):
    apex = random.choice([(x1, y1), (x2, y2), (x3, y3)])
    return apex

def generate_dot(x_prev, y_prev, x_apex, y_apex):
    x_new = (x_prev + x_apex) / 2
    y_new = (y_prev + y_apex) / 2
    turtle.goto(x_new, y_new)
    turtle.dot(1)
    turtle.update()
    return x_new, y_new

def main():
    turtle.tracer(0, 0)
    turtle.hideturtle()

    x1, y1 = -200, -200
    x2, y2 = 200, -200
    x3, y3 = 0, 200

    draw_big_triangle(x1, y1, x2, y2, x3, y3)

    x_prev, y_prev = None, None
    x_apex, y_apex = choose_apex(x1, y1, x2, y2, x3, y3)

    if x_apex == x1:
        x_prev, y_prev = random.uniform(min(x2, x3), max(x2, x3)), y2
    elif x_apex == x2:
        x_prev, y_prev = x3, random.uniform(min(y1, y3), max(y1, y3))
    else:
        x_prev, y_prev = random.uniform(min(x1, x2), max(x1, x2)), y1

    turtle.goto(x_prev, y_prev)
    turtle.dot(10, "red")

    num_dots = 10000

    progress_step = int(num_dots / 100)
    progress = 0

    for i in range(num_dots):
        x_apex, y_apex = choose_apex(x1, y1, x2, y2, x3, y3)
        turtle.penup()
        turtle.goto(x_apex, y_apex)
        turtle.dot(1, "blue")
        turtle.update()
        x_prev, y_prev = generate_dot(x_prev, y_prev, x_apex, y_apex)

        if i % progress_step == 0:
            progress += 1
            progress_percent = progress / (num_dots / 100)
            print(f"Progress: {progress_percent:.2f}%")

    turtle.update()
    turtle.exitonclick()


if __name__ == '__main__':
    main()

