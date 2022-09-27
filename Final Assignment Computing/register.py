import tkinter.messagebox
from tkinter import *
import login



class register():
    def __init__(self, window):
        self.wn = window
        self.wn.title('User Registration Form')
        self.wn.geometry('500x500+300+200')

        self.ent_username_value = StringVar()
        self.ent_password_value = StringVar()
        self.ent_address_value = StringVar()
        self.ent_age_value = StringVar()
        self.ent_contact_value = StringVar()

        self.lb_head = Label(self.wn, text='User Registration Form', fg='white', font=('arial', 20, 'bold'), bg='black')
        self.lb_head.place(x=0, y=0, relwidth=1)

        self.frame1= Frame(self.wn,bg="crimson")
        self.frame1.place(x=100, y=100)

        self.lb_fotter = Label(text='@Copyright Reserved 2020ANISHSHREE ', font=('arial', 8, 'bold'), fg='black')
        self.lb_fotter.place(x=100, y=370)

        self.lb_username=Label(self.frame1,text='User Name',font=('times new roman',12,'bold'),fg='black')
        self.lb_username.grid(row=0, column=0, padx=10, pady=10)

        self.lb_password= Label(self.frame1,text='Password',font=('times new roman', 12, 'bold'),fg='black')
        self.lb_password.grid(row=1,column=0,padx=10,pady=10)

        self.lb_age= Label(self.frame1, text='Age',font=('times new roman', 12, 'bold'),fg='black')
        self.lb_age.grid(row=2,column=0,padx=10,pady=10)

        self.lb_address= Label(self.frame1, text='Address', font=('times new roman', 12, 'bold'), fg='black')
        self.lb_address.grid(row=3, column=0, padx=10, pady=10)

        self.lb_contact= Label(self.frame1, text='Contact No', font=('times new roman', 12, 'bold'), fg='black')
        self.lb_contact.grid(row=4, column=0, padx=10, pady=10)

        self.ent_username = Entry(self.frame1, font=('arial', 10, 'bold'),textvariable=self.ent_username_value)
        self.ent_username.grid(row=0, column=1, padx=10, pady=10)

        self.ent_password = Entry(self.frame1, font=('arial', 10, 'bold'), show='*',textvariable=self.ent_password_value)
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        self.ent_age = Entry(self.frame1, font=('arial', 10, 'bold'),textvariable=self.ent_age_value)
        self.ent_age.grid(row=2, column=1, padx=10, pady=10)

        self.ent_address = Entry(self.frame1, font=('arial', 10, 'bold'),textvariable=self.ent_address_value)
        self.ent_address.grid(row=3, column=1, padx=10, pady=10)

        self.ent_contact= Entry(self.frame1, font=('arial', 10, 'bold'),textvariable=self.ent_contact_value)
        self.ent_contact.grid(row=4, column=1, padx=10, pady=10)

        self.btn1 = Button(self.wn, text='Submit', bg='black', fg='white', font=('arial', 11, 'bold'), bd=5,command=self.btn_submit_click)
        self.btn1.place(x=140, y=320)

        def res():
            self.ent_username.delete(0, END)
            self.ent_password.delete(0, END)
            self.ent_age.delete(0, END)
            self.ent_address.delete(0, END)
            self.ent_contact.delete(0, END)




        self.btn2 = Button(self.wn, text='Reset', bg='black', fg='white', font=('arial', 11, 'bold'), bd=5,command=res)
        self.btn2.place(x=250,y=320)






    def btn_submit_click(self):
        name = self.ent_username.get()
        password = self.ent_password.get()
        address= self.ent_address.get()
        age = self.ent_age.get()
        contact = self.ent_contact.get()


        user_list=[name,',',password,',',address,',',age,',',contact,',']
        self.save_user_file(user_list)



    def save_user_file(self, ls):
        f = open('output.txt', 'a+')
        f.writelines(ls)
        f.write('\n')
        a = tkinter.messagebox.showinfo('Success', 'file is saved')
        if a == 'ok':
            self.wn.withdraw()
            a = Toplevel(self.wn)
            login.Login(a)
        f.close()






def main():
    wn = Tk()
    register(wn)
    wn.mainloop()

if __name__ =='__main__':
    main()