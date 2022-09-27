from tkinter import *
import welcome


class department:
    def __init__(self, window, ):
        self.wn = window
        self.title = ('login details')
        self.wn.geometry('600x500+350+50')
        self.ent_employee = StringVar()
        self.ent_Name1_value = StringVar()
        self.ent_Name2_value = StringVar()
        # =========label
        self.lb_head = Label(self.wn, text=' Welcome To Employee Department Form', fg='lightgreen', font=('arial', 20, 'bold'))

        self.lb_head.place(x=0, y=0, relwidth=1)

        self.lb_head = Label(self.wn, text=' Thanks for Visit', fg='black',
                             font=('arial', 20, 'bold'))

        self.lb_head.place(x=100, y=300, relwidth=1)

        self.frame1 = Frame(self.wn,bg="crimson")
        self.frame1.place(x=50, y=100)

        self.lb_fotter = Label(text='@Copyright Reserved 2020ANISHSHREE ', font=('arial', 8, 'bold'), fg='black')
        self.lb_fotter.place(x=100, y=290)

        self.lb_employee = Label(self.frame1, text='Employee ID:', font=('arial', 14, 'bold'), fg='black')
        self.lb_employee.grid(row=0, column=0, padx=10, pady=10)

        self.lb_Name = Label(self.frame1, text='Employment code:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Name.grid(row=1, column=0, padx=10, pady=10)

        self.lb_Name = Label(self.frame1, text='Contact:', font=('arial', 15, 'bold'), fg='black')
        self.lb_Name.grid(row=2, column=0, padx=10, pady=10)

        self.ent_employee= Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_employee.grid(row=0, column=1, padx=10, pady=10)

        self.ent_Name1 = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Name1.grid(row=1, column=1, padx=10, pady=10)

        self.ent_Name2 = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_Name2.grid(row=2, column=1, padx=10, pady=10)

        # ==========Button
        self.btn1 = Button(self.wn, text='Add', font=('arial', 14, 'bold'), fg='white', bg="black", command=self.btn_add)
        self.btn1.place(x=200, y=250)
        self.btn2 = Button(self.wn, text='Reset', font=('arial', 14, 'bold'), fg='white', bg="black", command=self.reset_btn)
        self.btn2.place(x=100, y=250)

        # ========back button
        self.btn3 = Button(self.wn, text='Back', font=('arial', 14, 'bold'), fg='white', bg="black", command=self.back_btn)
        self.btn3.place(relx=0.08, rely=0.93)

    def back_btn(self):
        self.wn.withdraw()
        a = Toplevel(self.wn)
        welcome.welcome(a)

    def reset_btn(self):
        self.wn.withdraw()
        a = Toplevel(self.wn)
        department(a)

    def btn_add(self):
        self.wn.withdraw()
        a = Toplevel(self.wn)
        welcome.welcome(a)



def main():
    wn = Tk()
    department(wn)
    wn.mainloop()

if __name__ == '__main__':
    main()
