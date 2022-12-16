from turtle import *

    
def estrella():
    
    pen(pencolor = 'blue', fillcolor = 'purple', pensize = 3)      #  defino el tamaño del boli, el color y de que color se rellena la figura
    begin_fill()                                                 
    
    while True:
        forward(300)                        
        right(160)                         
        if abs(pos()) < 1:                  
            break
    end_fill()                              
    done()                                    


