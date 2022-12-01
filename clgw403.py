from tkinter import *
root=Tk()
root.geometry("500x300")

def choise():
    if(etype_value==1):
        root.configure()
    elif(etype_value==2):
        root.configure()

empid_user=Label(root, text="Empid").grid(row=1, column=2)
ename_user=Label(root, text="Employee Name :").grid(row=2, column=2)
job_user=Label(root, text="Job").grid(row=3, column=2)
etype_user=Label(root, text="Employee type").grid(row=4, column=2)
salary_user=Label(root, text="Salary").grid(row=5, column=2)

empid_value=StringVar()
ename_value=StringVar()
job_value=StringVar()
etype_value=IntVar()
salary_value=IntVar()

empid_box=Entry(root, textvariable=empid_value).grid(row=1, column=3)
ename_box=Entry(root, textvariable=ename_value).grid(row=2,column=3)
job_box=Entry(root, textvariable=job_value).grid(row=3, column=3)
rb1_box=Radiobutton(root,text="Regular", variable=etype_value,value=1,command=choise)
rb1_box.grid(row=4, column=3)
rb2_box=Radiobutton(root,text="Temporary", variable=etype_value,value=2,command=choise)
rb2_box.grid(row=4, column=4)

salary_spin=Spinbox(root,from_=0,to=25)
salary_spin.grid(row=5,column=3)


Button(text="Insert",command=root.destroy).grid(row=6,column=2)
Button(text="Update",command=root.destroy).grid(row=6,column=3)
Button(text="Delete",command=root.destroy).grid(row=7,column=2)
Button(text="Select",command=root.destroy).grid(row=7,column=3)

root.mainloop()

