from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

#import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root,bd=28,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",foreground="red",background="white",font=("times ne roman",40,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===================Data Frame =+===========

        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)


        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("ariel",12,"bold"),text="Patient Information")

        DataframeLeft.place(x=0,y=5,width=930,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("ariel",12,"bold"),text="Prescription")

        DataframeRight.place(x=940,y=5,width=330,height=350)

        #=================Butons Frame===============

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #=================Details Frame===============

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=150)


root=Tk()
ob=Hospital(root)
root.mainloop()