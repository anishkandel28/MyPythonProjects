from tkinter import *
import employee
import department


class welcome:
    def __init__(self, window, ):
        self.wn = window
        self.title = ('login details')

        self.wn.geometry('500x500+500+100')

        # =========label
        self.lb_head = Label(self.wn, text='Employee User details', fg='white', font=('arial', 20, 'bold'), bg='black')

        self.lb_head.place(x=0, y=0, relwidth=1)

        self.lb_fotter = Label(text='@Copyright Reserved 2020ANISHSHREE ', font=('arial', 8, 'bold'), fg='black')
        self.lb_fotter.place(x=100, y=400)

        self.frame1 = Frame(self.wn,bg="crimson")
        self.frame1.place(x=50, y=100)

        # ==========Button
        self.btn_dpt = Button(self.frame1, text='Department', bg='black', fg='white',
                              font=('arial', 18, 'bold'))

        self.btn_dpt.configure(command=self.goto_department)
        self.btn_dpt.grid(row=1, column=0, padx=16, pady=16)

        self.btn_dpt = Button(self.frame1, text='Employee', bg='black', fg='white', font=('arial', 18, 'bold'))
        self.btn_dpt.configure(command=self.goto_employee)
        self.btn_dpt.grid(row=2, column=0, padx=16, pady=16)

        self.btn_dpt = Button(self.frame1, text='Exit', bg='black', fg='white', font=('Dark', 18, 'bold'),
                              command=exit)
        self.btn_dpt.grid(row=3, column=0, padx=16, pady=16)

    def goto_employee(self):
        employee.main()

    def goto_department(self):
        department.main()




def main():
    wn = Tk()
    welcome(wn)
    wn.mainloop()


if __name__ == '__main__':
    main()
