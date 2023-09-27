from pynput.keyboard import Key, Listener as KeyboardListener

key_down_set = set()
moving_linearly = False
turning = False

def on_forward():
    global moving_linearly
    if moving_linearly:
        return
    moving_linearly = True
    
    print("Moving forward...")

def on_backward():
    global moving_linearly
    if moving_linearly:
        return
    moving_linearly = True
    
    print("Moving backward...")

def on_left():
    global turning
    if turning:
        return
    turning = True
    
    print("Turning left...")

def on_right():
    global turning
    if turning:
        return
    turning = True
    
    print("Turning right...")

def stop_robot():
    pass

def on_press(key):
    if (key in key_down_set):
        return

    key_down_set.add(key)
    if key == Key.w:
        on_forward()
    elif key == Key.s:
        on_backward()
    elif key == Key.a:
        on_left()
    elif key == Key.d:
        on_right()
    

def on_release(key):
    global moving_linearly
    global turning

    key_down_set.remove(key)
    match key:
        case Key.s, Key.w:
            moving_linearly = False
        case Key.a, Key.d:
            turning = False

def print_controls():
    print("Teleop Client")
    print("Press 'w' to move forward")
    print("Press 's' to move backward")
    print("Press 'a' to move left")
    print("Press 'd' to move right\n")
    print("To avoid cluttering up your terminal, you can take focus off your terminal.")

def main():
    print_controls()
    with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminating Teleop Client and Stopping Robot...")
        stop_robot()
