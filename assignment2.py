from tkinter import *
root=Tk()
root.geometry("400x400")

Label(root,text="Student Counceling Form",font=("rubik","15","bold")).grid(row=0,column=2)
sname_user=Label(root,text="Student Name").grid(row=1,column=1)
year_user=Label(root,text="Year").grid(row=2,column=1)
date_user=Label(root,text="Date").grid(row=3,column=1)
dept_user=Label(root,text="Department").grid(row=4,column=1)
ac_user=Label(root,text="Academic Issue").grid(row=5,column=1)
pc_user=Label(root,text="Personal Issue").grid(row=6,column=1)
fa_user=Label(root,text="Faculty Incharge").grid(row=7,column=1)

sname_value=StringVar()
year_value=IntVar()
date_value=IntVar()
dept_value=StringVar()
ac_value=StringVar()
pc_value=StringVar()
fa_value=StringVar()

sname_box=Entry(root,textvariable=sname_value).grid(row=1,column=2)
year_box=Entry(root,textvariable=year_value).grid(row=2,column=2)
date_box=Entry(root,textvariable=date_value).grid(row=3,column=2)
dept_box=Entry(root,textvariable=dept_value).grid(row=4,column=2) 
ac_box=Entry(root,textvariable=ac_value).grid(row=5,column=2,pady=10,ipadx=40,ipady=30)
pc_box=Entry(root,textvariable=pc_value).grid(row=6,column=2,pady=5,ipadx=40,ipady=30)
fa_box=Entry(root,textvariable=fa_value).grid(row=7,column=2)

# padx means=space between two element in HORIZONTAL
# pady means=space between two element in VERTICAL

# ipadx is use to config height in grid function
# ipady is use to config width in grid function

root.mainloop()