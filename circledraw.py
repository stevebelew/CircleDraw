# Counter ticks

###################################################
# Student should add code where relevant to the following.

import simplegui 
increase_radius = True
radius = 2
counter = 0
bg_counter = 1
# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
def start():
    timer.start()
    
def stop():
    timer.stop()   
    
def reset():
    global counter
    
    counter = 0
    
def background_timer():
    global bg_counter
    
    if bg_counter % 2 == 0:
        my_frame.set_canvas_background('Red')
    else:
        my_frame.set_canvas_background('Blue')
    bg_counter += 1
    

def draw_circle(canvas):
    canvas.draw_circle([100,100],radius,3,"White") 
    
def circle_timer():
    global radius
    global increase_radius
    if radius == 100:
        increase_radius = False
        radius -= 1
    elif radius > 0 and  not increase_radius == True:
        radius -=1
    else:
        increase_radius = True
        radius +=1
        
    
    

    
# create timer
my_frame = simplegui.create_frame("My Frame", 200, 200)
start_button = my_frame.add_button('Start',start)
stop_button = my_frame.add_button('Stop',stop)
reset_button = my_frame.add_button('Reset',reset)
my_frame.set_draw_handler(draw_circle)
timer = simplegui.create_timer(1000, tick)
background_timer = simplegui.create_timer(3000, background_timer)
circle_timer = simplegui.create_timer(10, circle_timer)
background_timer.start()
circle_timer.start()
my_frame.start()



