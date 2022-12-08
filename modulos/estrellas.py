from turtle import *

    
def estrella():
    
    pen(pencolor = 'blue', fillcolor = 'purple', pensize = 4)      #  defino el tamaño del boli, el color y de que color se rellena la figura
    begin_fill()                                                 #  empieza a rellenar la figura
    
    while True:
        forward(300)                        #  avanza 300 pasos
        right(160)                          #  gira 160 grados
        if abs(pos()) < 1:                  
            break
    end_fill()                              #  termina de rellenar la figura
    done()                                  #  termina el programa


