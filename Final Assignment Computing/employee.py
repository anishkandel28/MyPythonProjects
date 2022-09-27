from tkinter import *
import os
import pickle
import tkinter.messagebox
import view

d = {}


class employee:
    def __init__(self, window, ):
        self.wn = window
        self.title = ('login details')
        self.wn.geometry('600x600+350+50')
        self.ID_value = StringVar()
        self.Name_value = StringVar()
        self.age_value = StringVar()
        self.address_value = StringVar()
        self.contact_value = StringVar()
        self.department_value = StringVar()

        # =========label
        self.lb_head = Label(self.wn, text='Employee Form', fg='white', font=('arial', 20, 'bold'), bg='black')

        self.lb_head.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn,bg="crimson")
        self.frame1.place(x=50, y=100)



        self.lb_head = Label(self.wn, text='Employee Form', fg='white', font=('arial', 20, 'bold'), bg='black')
        self.lb_head.place(x=0, y=0, relwidth=1)


        self.lb_ID = Label(self.frame1, text='ID:', font=('arial', 15, 'bold'), fg='black')
        self.lb_ID.grid(row=0, column=0, padx=10, pady=10)

        self.lb_Name = Label(self.frame1, text='Full Name:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Name.grid(row=1, column=0, padx=10, pady=10)

        self.lb_Age = Label(self.frame1, text='Age:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Age.grid(row=2, column=0, padx=10, pady=10)

        self.lb_Address = Label(self.frame1, text='Address:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Address.grid(row=3, column=0, padx=10, pady=10)

        self.lb_Contact = Label(self.frame1, text='Contact:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Contact.grid(row=4, column=0, padx=10, pady=10)

        self.lb_Department = Label(self.frame1, text='Department:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Department.grid(row=5, column=0, padx=10, pady=10)

        self.lb_fotter = Label(text='@Copyright Reserved 2020ANISHSHREE ', font=('arial', 8, 'bold'), fg='black')
        self.lb_fotter.place(x=100, y=520)

        self.ent_ID = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_ID.grid(row=0, column=1, padx=10, pady=10)

        self.ent_Name = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Name.grid(row=1, column=1, padx=10, pady=10)

        self.ent_Age = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Age.grid(row=2, column=1, padx=10, pady=10)

        self.ent_Address = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Address.grid(row=3, column=1, padx=10, pady=10)

        self.ent_Contact = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Contact.grid(row=4, column=1, padx=10, pady=10)

        self.ent_Department = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Department.grid(row=5, column=1, padx=10, pady=10)

        self.btn1 = Button(self.wn, text='Add', font=('arial', 14, 'bold'), fg='white', bg="black", command=self.btn_add_click)
        self.btn1.place(relx=0.35, rely=0.80)

        # ====reset
        def res():
            self.ent_ID.delete(0, END)
            self.ent_Name.delete(0, END)
            self.ent_Age.delete(0, END)
            self.ent_Address.delete(0, END)
            self.ent_Contact.delete(0, END)
            self.ent_Department.delete(0, END)


        self.btn2 = Button(self.wn, text='Reset', font=('arial', 14, 'bold'), fg='white',bg='black',
                           command=res)
        self.btn2.place(relx=0.45, rely=0.80)

        # ======for gender
        self.btn3 = Radiobutton(self.wn, text='Male', bg='black', font=('arial', 13, 'bold'), fg='white',
                                value=1).place(relx=0.5, rely=0.7)
        self.btn3 = Radiobutton(self.wn, text='Female', bg='black', font=('arial', 13, 'bold'), fg='white',
                                value=2).place(relx=0.3, rely=0.7)

        # ========back buttom
        self.btn4 = Button(self.wn, text='Back', font=('arial', 14, 'bold'), fg='white', bg='black',
                           command=self.back_btn)
        self.btn4.place(relx=0.08, rely=0.93)

        self.btn_dpt = Button(self.frame1, text='View', bg='white', fg='black', font=('Dark', 16, 'bold'),
                              command=self.btn_view)
        self.btn_dpt.grid(row=7, column=0, padx=16, pady=16)

    def btn_view(self):
        b = Toplevel(self.wn)
        view.Emp_Display(b)

    def btn_add_click(self):
        self.insert()

    def back_btn(self):
        self.wn.withdraw()
        a = Toplevel(self.wn)
        employee(a)

    def insert(self):
        global d
        le = os.path.getsize('C:\\Users\\dell\\PycharmProjects\\Final Assignment Computing\\new.txt')
        ID = self.ID_value.get()
        Name = self.Name_value.get()
        di = {ID: [self.ent_ID.get(), self.ent_Name.get(), self.ent_Age.get(), self.ent_Address.get(), self.ent_Contact.get(), self.ent_Department.get()]}
        if le>0:
            f = open('new.txt', 'rb+')
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            tkinter.messagebox.showinfo('success', 'Data saved successfully')
            f.close()
        else:
            f = open('new.txt', 'wb')
            d.update(d)
            pickle.dump(d,f)
            tkinter.messagebox.showinfo('success', 'Data saved successfully')
            f.close()




def main():
    wn = Tk()
    employee(wn)
    wn.mainloop()

def btn_view(self):
        view.main()

if __name__ =='__main__':
    main()
