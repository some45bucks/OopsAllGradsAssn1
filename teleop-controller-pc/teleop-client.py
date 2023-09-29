from pynput.keyboard import Key, KeyCode, Listener as KeyboardListener

last_key_pressed = None
is_key_down = False

def on_forward():
    print("Moving forward...")

def on_backward():
    print("Moving backward...")

def on_left():
    print("Turning left...")

def on_right():
    print("Turning right...")

def stop_robot():
    print('Stop')
    pass

def on_press(key):
    global last_key_pressed
    global is_key_down

    if (key == None or is_key_down):
        return

    match key:
        case KeyCode():
            pressed_key = key.char
        case _ as pressed_key:
            pass

    match pressed_key:
        case 'w':
            on_forward()
        case 's':
            on_backward()
        case 'a':
            on_left()
        case 'd':
            on_right()
        case Key.esc:
            return False
        case _:
            return
    
    last_key_pressed = pressed_key
    is_key_down = True


def on_release(key):
    global is_key_down
    global last_key_pressed
    
    if key == None:
        return
    
    match key:
        case KeyCode():
            released_key = key.char
        case _ as released_key:
            pass
        
    if (released_key == last_key_pressed):
        last_key_pressed = None
        is_key_down = False
        stop_robot()


def print_controls():
    print("Teleop Client")
    print("Press 'w' to move forward")
    print("Press 'a' to move left")
    print("Press 's' to move backward")
    print("Press 'd' to move right\n")
    print("Commands will be sent to the robot as long as this process is running.")

def main():
    print_controls()
    with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    exit()

def exit():
    print("\nTerminating Teleop Client and Stopping Robot...")
    stop_robot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
