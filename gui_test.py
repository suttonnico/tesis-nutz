from guizero import *
import random

num = 0

def read_sensor():
    return random.randrange(3200, 5310, 10) / 100

def update_label():
    text.value=int(text.value)+1

if __name__ == '__main__':
    app = App(title='Squirrel Bot',
              height=100,
              width=200,
)

    title = Text(app, 'Nueces clasificadas:', grid=[0, 0])
    text = Text(app, text="1")
    text.events

    text.repeat(1000, update_label)
    app.display()