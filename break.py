"""for x in range(5):
    for y in range(6):
        print(x,y, end=' ')
    print()"""
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.color("green")

while True:
    print("Main Loop")
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)

wn.mainloop()