from tkinter import *
root=Tk()
root.geometry("500x300")
def choise():
    if(ac_value==1):
        root.configure()
    elif(ac_value==2):
        root.configure()

cust_user=Label(root, text="Custid")
cust_user.grid(row=1, column=2)
custname_user=Label(root, text="Customer Name :")
custname_user.grid(row=2,column=2)
branch_user=Label(root, text="Branch")
branch_user.grid(row=3, column=2)
ac_user=Label(root, text="account type")
ac_user.grid(row=4, column=2)
amount_user=Label(root,text="Amount")
amount_user.grid(row=5, column=2)

cust_value=StringVar
custname_value=StringVar
branch_value=StringVar
ac_value=IntVar()
amount_value=DoubleVar


cust_box=Entry(root, textvariable=cust_value)
cust_box.grid(row=1, column=3)
custname_box=Entry(root, textvariable=custname_value)
custname_box.grid(row=2, column=3)
branch_box=Entry(root, textvariable=cust_value)
branch_box.grid(row=3, column=3)

rb1_box=Radiobutton(root, text="Saving", variable=ac_value,value=1,command=choise)
rb1_box.grid(row=4, column=3)
rb2_box=Radiobutton(root,text="Non Saving", variable=ac_value,value=2,command=choise)
rb2_box.grid(row=4, column=4)

scale_box=Scale(root,variable=amount_value,from_=1,to=100,orient=HORIZONTAL)
scale_box.grid(row=5,column=3)

Button(text="Update",command=root.destroy).grid(row=6,column=3)
Button(text="Insert",command=root.destroy).grid(row=6,column=2)
Button(text="Delete",command=root.destroy).grid(row=7,column=2)
Button(text="Select",command=root.destroy).grid(row=7,column=3)

root.mainloop()