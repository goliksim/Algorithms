import turtle as tur

def curve(iter):
    if(iter < 0): 
        tur.forward(size)
        return None
    curve(iter-1)
    tur.right(45)
    tur.forward(size)
    tur.right(45)
    curve(iter-1)
    tur.left(45)
    tur.forward(size)
    tur.left(45)
    curve(iter-1)
    tur.left(45)
    tur.forward(size)
    tur.left(45)
    curve(iter-1)
    tur.right(45)
    tur.forward(size)
    tur.right(45)
    curve(iter-1)
     

def drawOctagon(iter):
    for i in range(4):
        curve(iter-1)
        tur.right(45)
        tur.forward(size)
        tur.right(45)


# Конфигурация черепашки
tur.speed(speed=0)
tur.screensize(400, 400)
tur.tracer(0) # <- отключение отрисовки
# Начало для черепашки


#Рисуем
if __name__ == "__main__":
    iter = 3

    offset=3**iter
    size = 200/offset
    
    tur.setpos(-(offset-0.5)*(size*1.2),(offset)*(size*1.2))
    tur.clear()
    
    #строим
    drawOctagon(iter)
    tur.update() 

    tur.mainloop()
    