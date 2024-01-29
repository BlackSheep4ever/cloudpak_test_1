from pynput.keyboard import Key, Listener, KeyCode

import open_file
import register_file

print('\nPara ler o arquivo existente aperte "1". \nPara criar ou modificar um arquivo aperte "2". \nPara sair aperte "Esc"\n')

def on_press(key):
    
    if key == KeyCode(char = '1'):
        open_file.view_form()
        print('\nPara ler o arquivo aperte "1". \nPara escrever o arquivo aperte "2". \nPara sair aperte "Esc"\n')
    
    if key == KeyCode(char = '2'):
        register_file.update_form()
        print('\nPara ler o arquivo aperte "1". \nPara escrever o arquivo aperte "2". \nPara sair aperte "Esc"\n')

    if key == Key.esc:
        return False
    
with Listener(on_press) as listener:
    listener.join()
