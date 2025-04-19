#System Controller

from tkinter import *
import os



#Commands
commands='''
restart_time --> command=lambda: os.system('shutdown /r /t 30')
restart --> command=lambda: os.system('shutdown /r /t 1')
close --> command=lambda: root.destroy()
shutdown --> command=lambda: os.system('shutdown /s /t 1')
signout --> command=lambda: os.system('shutdown -1')
'''



if __name__ == '__main__':
    root = Tk()
    root.title('Shutdown')
    root.geometry('398x610+650+150')
    root.resizable(False,False)
    root.config(bg='#1A2030')
    
    icon_image = PhotoImage(file='icon.png')
    root.iconphoto(False,icon_image)
    


    restart_timer = PhotoImage(file='restart_timer.png')
    close = PhotoImage(file='close.png')
    restart = PhotoImage(file='restart.png')
    shutdown = PhotoImage(file='shutdown.png')
    sign_out = PhotoImage(file='sign_out.png')

    Button(root, image=restart_timer,bg='#1A2030', bd=0, command=lambda: os.system('shutdown /r /t 30')).place(x=5, y=10)
    Button(root, image=close,bg='#1A2030', bd=0, command=lambda:root.destroy()).place(x=205, y=10)
    Button(root, image=restart,bg='#1A2030', bd=0, command=lambda: os.system('shutdown /r /t 1')).place(x=5, y=215)
    Button(root, image=shutdown,bg='#1A2030', bd=0, command=lambda: os.system('shutdown /s /t 1')).place(x=205, y=215)
    Button(root, image=sign_out,bg='#1A2030', bd=0, command=lambda: os.system('shutdown /l')).place(x=5, y=420)
    
    root.mainloop()