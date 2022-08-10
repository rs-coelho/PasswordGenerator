import tkinter as tk
from tkinter import messagebox
#import sqlalchemy as sql


class PasswordCatalog(tk.Toplevel):

    def __init__(self,passw = None):
        super(PasswordCatalog, self).__init__()
        print('------------- Password Catalog Menu Initiated -------------\n')
        self.title("Password Catalog")
        self.geometry("450x370")
        padding_x = 5
        padding_y = 5

        label = tk.LabelFrame(self, text="Username:")
        label.grid(row=1,columnspan=2,pady=20, padx=20)
        
        self.username = tk.Entry(label, font=("Helvetica", 24))
        self.username.grid(row=1, columnspan=2,pady=10, padx=10)
        
        
        label2 = tk.LabelFrame(self, text="Site:")
        label2.grid(row=2,columnspan=2,pady=20, padx=20)
        
        self.site = tk.Entry(label2, font=("Helvetica", 24))
        self.site.grid(row=2, columnspan=2,pady=10, padx=10)
        
        print('This is in the inside of the Catalog',passw)
        # Create Entry Box For Our Returned Password
        self.pw_entry = tk.Entry(self, text='', font=("Helvetica", 24), bd=3)
        self.pw_entry.insert(0,passw)
        self.pw_entry.grid(row=4, columnspan=2,pady=20)
        
        btn5 = tk.Button(self, text='Store')
        btn5.config(command=self.store)
        btn5.grid(row=5,columnspan=2, padx=100, pady=10, sticky='NWSE')
        

        msg2 = 'Created by Rodrigo Coelho'
        label1 = tk.Label(self, text=msg2)
        label1.grid(row=6, columnspan=2, pady=20)        

    def run(self):
        self.mainloop()
        
    def store(self):
        if not(self.username.get() and self.site.get()):
            messagebox.showerror('Something is missing','Please type both username and site!')


if __name__ == '__main__':
    print('----------------- Catalog Log Begin -------------------')
    ex = PasswordCatalog('test')
    ex.run()
    print('-----------------  Catalog Log End  -------------------')
    



