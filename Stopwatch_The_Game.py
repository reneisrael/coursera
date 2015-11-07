# "Stopwatch: The Game"
import simplegui

# define global variables
contador = 0
corre = False
intentos = 0
aciertos = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t%10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global corre
    timer.start()
    corre = True

def stop():
    global corre, intentos, aciertos
    timer.stop()
    if corre:
        intentos += 1
        if contador % 10 == 0:
            aciertos += 1
    corre = False

def reset():
    global corre, contador, aciertos, intentos
    timer.stop()
    contador = 0
    aciertos = 0
    intentos = 0
    corre = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global contador
    contador += 1
    
# define draw handler
def dibuja(canvas):
    canvas.draw_text(format(contador), [60, 85], 30, "White")
    canvas.draw_text(str(aciertos)+"/"+str(intentos), [155, 25], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)
frame.set_draw_handler(dibuja)
timer = simplegui.create_timer(100, tick)


# start frame
frame.start()

# Please remember to review the grading rubric
