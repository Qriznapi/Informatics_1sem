from random import randint
from tkinter import *

WIDTH = 900
HEIGHT = 600


class Ball:
    def __init__(self):
        self.V = 1
        self.R = randint(30, 70) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, WIDTH - self.R) # храним положение по x и y
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill="green") # при создании шарика отрисовываем его

    def move(self):
        if self.V:
            self.x += self.dx
            self.y += self.dy
            if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
                self.dx = -self.dx
            if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
                self.dy = -self.dy
        else:
            self.x = -1000
            self.y = -1000

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def check(event):
    for ball in balls:
        if (ball.x - event.x) ** 2 + (ball.y - event.y) ** 2 <= ball.R ** 2:
            ball.V = 0
def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)
    check(event)


#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

if __name__=="__main__":
	root = Tk()
	root.geometry(f'{WIDTH}x{HEIGHT}')
	canvas = Canvas(root, width = WIDTH, height = HEIGHT)
	canvas.pack()
	#сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
	canvas.bind('<Button-1>', click_handler)
	balls = [Ball() for i in range(5)]
	# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
	tick()
	root.mainloop()
