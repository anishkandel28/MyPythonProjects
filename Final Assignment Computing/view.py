from tkinter import *
import pickle


class Emp_Display:
    def __init__(self, window):
        self.wn = window
        self.lb_display = Label(self.wn)
        self.lb_data = Label(window, text='name'+'\t'+'dob'+'\t'+'address'+'\t'+'mail'+'\t'+'contact'+'\t'+'gender'+'\t')
        self.lb_data.pack()
        self.lb_display.pack()
        self.open_file_content()

    def open_file_content(self):
        f = open('new.txt', 'rb')
        d = pickle.load(f)
        data=''
        for i,j in d.items():
           da= ''
           for l in j:
            da = da + l + '\t'
           data = data + da + '\n'
        self.lb_display.config(text=data)
def main():
    wb = Tk()
    Emp_Display(wb)
    wb.mainloop()

if __name__ == '__main__':
    main()