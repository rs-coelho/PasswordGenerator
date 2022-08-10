
import random
from tkinter import messagebox
from PasswordCatalog import PasswordCatalog
import tkinter as tk


class Execute(tk.Tk):

    def __init__(self):
        super(Execute, self).__init__()
        print('############# Password Generator Main Menu Initiated #############\n')
        self.title("Password Generator")
        self.geometry("430x390")
        padding_x = 5
        padding_y = 5

        label = tk.LabelFrame(self, text="How many characters?")
        label.grid(row=1,columnspan=2,pady=20, padx=20)
        
        #size_pass = tk.Text(self)
        #size_pass.grid(row=1, column=0, padx=padding_x, pady=padding_y, sticky='NWSE',rowspan=1)
        
        self.size_pass = tk.Entry(label, font=("Helvetica", 24))
        self.size_pass.grid(row=1, columnspan=2,pady=10, padx=10)
        
        self.lowerbtn_v = tk.IntVar()
        lowerbtn = tk.Checkbutton(self, text='Lower Case Letters',variable=self.lowerbtn_v)
        #btn.config(command=Pilha)
        lowerbtn .grid(row=2, column=0, padx=padding_x, pady=padding_y, sticky='NWSE')

        self.upperbtn_v = tk.IntVar()
        upperbtn = tk.Checkbutton(self, text='Upper Case Letters',variable=self.upperbtn_v)
        #btn2.config(command=Fila)
        upperbtn.grid(row=2, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')
        
        self.numberbtn_v = tk.IntVar()
        numberbtn = tk.Checkbutton(self, text='Numbers',variable=self.numberbtn_v)
        #btn3.config(command=ListaSE)
        numberbtn.grid(row=3, column=0, padx=padding_x, pady=padding_y, sticky='NWSE')
        
        self.symbolbtn_v = tk.IntVar()
        symbolbtn = tk.Checkbutton(self, text='Special Symbols',variable=self.symbolbtn_v)
        #btn4.config(command=ListaDE)
        symbolbtn.grid(row=3, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')
        
        # Create Entry Box For Our Returned Password
        self.pw_entry = tk.Entry(self, text='', font=("Helvetica", 24), bd=3)
        self.pw_entry.grid(row=4, columnspan=2,pady=20)
        
        btn5 = tk.Button(self, text='Generate')
        btn5.config(command=self.generate)
        btn5.grid(row=5, padx=padding_x, pady=padding_y, sticky='NWSE')
        
        btn6 = tk.Button(self, text='Copy to clipboard')
        btn6.config(command=self.clipper)
        btn6.grid(row=5, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')
        
        btn7 = tk.Button(self, text='Add to Catalog')
        btn7.config(command=self.call_PasswordCatalog)
        btn7.grid(row=6, columnspan=2, padx=padding_x, pady=padding_y, sticky='NWSE')



        msg2 = 'Created by Rodrigo Coelho'
        label1 = tk.Label(self, text=msg2)
        label1.grid(row=10, columnspan=2, pady=20)
        
    # Copy to clipboard
    def clipper(self):
        # Clear the clipboard
        self.clipboard_clear()
        # Copy to clipboard
        self.clipboard_append(self.pw_entry.get())
        
    def generate(self):
        self.pw_entry.delete(0, tk.END)
        contents_={'abcdefghijklmnopqrstuvwxyz':self.lowerbtn_v.get(),'ABCDEFGHIJKLMNOPQRTSUVWXYZ':self.upperbtn_v.get(),
                   '1234567890':self.numberbtn_v.get(),'!@#$%*&\/?':self.symbolbtn_v.get()}
        
        pass_elements=''
        for key,val in contents_.items():
            if val:
                pass_elements += key
        
        if not pass_elements:
            messagebox.showerror('Nothing Selected','Please select at least one of the options to generete a password!')
        elif not self.size_pass.get():
            messagebox.showerror('Something is missing','Please type the size of the disered password!')
            
        self.pw_entry.insert(0,''.join(random.sample(pass_elements,int(self.size_pass.get()))))
        print('\nGenerated password: ',self.pw_entry.get())
        return self.pw_entry.get()

    def call_PasswordCatalog(self):
        if len(self.pw_entry.get())>0:
            PasswordCatalog(self.pw_entry.get())
        else:
           messagebox.showerror('Error','No password was genereted to be entered in the Catalog')

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    print('----------------- Log Begin -------------------')
    ex = Execute()
    ex.run()
    print('-----------------  Log End  -------------------')
    



