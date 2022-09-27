from tkinter import *
import welcome
import register

class Login:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Login Form')
        self.wn.geometry('400x300+300+200')
        self.wn.bg="black"

        # label code
        self.lb_head = Label(self.wn, text='Login System', fg='Black', font=('arial', 20, 'bold'), bg='lightgreen')
        self.lb_head.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn,bg="crimson")
        self.frame1.place(x=50, y=100,)

        self.lb_urname = Label(self.frame1, text='User Name', font=('arial', 15, 'bold'), fg='black')
        self.lb_urname.grid(row=0, column=0, padx=10, pady=10)


        self.lb_pass = Label(self.frame1, text='Password', font=('arial', 15, 'bold'), fg='black')
        self.lb_pass.grid(row=1, column=0, padx=10, pady=10)

        self.lb_fotter = Label( text='@Copyright Reserved 2020ANISHSHREE ', font=('arial', 8, 'bold'), fg='black')
        self.lb_fotter.place(x=100, y=250)



        #Entry codes
        self.ent_usrname = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_usrname.grid(row=0, column=1, padx=10, pady=10)

        self.ent_pass = Entry(self.frame1, font=('arial', 10, 'bold'), show='*')
        self.ent_pass.grid(row=1, column=1, padx=10, pady=10)

        # signup button
        self.btn_signup = Button(self.wn, text='Signup', bg='black', fg='white', font=('arial', 10, 'bold'),
                                 command=self.sign_up_handler)
        self.btn_signup.place(x=200, y=210)

        #login btn and reset btn
        self.btn_login = Button(self.wn, text='Login', fg='white',bg="black", font=('arial', 10, 'bold'),
                                command=self.log_in_handler)
        self.btn_login.place(x=150, y=210)

        self.btn_reset = Button(self.wn, text='Reset', fg='white', bg='black', font=('arial', 10, 'bold'),command=self.reset_btn)
        self.btn_reset.place(x=270, y=210)

     #commandbutton_func

    def reset_btn(self):
        self.wn.withdraw()
        a = Toplevel(self.wn)
        Login(a)


    def log_in_handler(self):
        d = {}
        f = open('output.txt')
        d = f.readlines()
        for i in d:
            if i.split(',')[0] == self.ent_usrname.get():
                if i.split(',')[1] == self.ent_pass.get():
                    f.close()
                    self.wn.withdraw()
                    welcome.main()



    def sign_up_handler(self):
        self.wn.withdraw()
        register.main()





def main():
    wn = Tk()
    Login(wn)
    wn.mainloop()


if __name__ == '__main__':
    main()
