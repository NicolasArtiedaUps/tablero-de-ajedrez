# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:30:15 2023

@author: Nicolas
"""
import tkinter as tk
ventana=tk.Tk()
ventana.geometry("355x700")
for f in range(0,8):
    for c in range(0,8):
        if (c+f)%2==0:
            boton=tk.Button(ventana,bg="white",width=5,height=5)
        else:
            boton=tk.Button(ventana,bg="black",width=5,height=5)
        boton.grid(row=f,column=c,padx=0,pady=0)
        
ventana.mainloop()