from tkinter import *

ventana=Tk()

Widget_uno=Frame()
Widget_uno.grid(rows="0",column="0",rowspan= 2 )
Widget_uno.config(width="100",height="200")
Widget_uno.config(bg="blue")

Widget_dos=Frame()
Widget_dos.grid(row="0",column="1")
Widget_dos.config(width="100",height="100")
Widget_dos.config(bg="pink")

Widget_tres=Frame()
Widget_tres.grid(row="2",column="1", columnspan= 2 ) 
Widget_tres.config(width="200",height="100")
Widget_tres.config(bg="red")



ventana.mainloop()