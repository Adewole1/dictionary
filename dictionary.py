import tkinter as tk
import json
from difflib import get_close_matches
from tkinter import messagebox


data = json.load(open('data1.json'))
# data2 = json.load(open('dictionary.json'))


class Dictionary(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.wm_title('Dictionary')
        self.geometry('730x330+350+150')
        self.maxsize(730, 330)

        l1=tk.Label(self,text='Word:')
        l1.grid(row=0,column=0)

        self.word_text = tk.StringVar()
        self.e1 = tk.Entry(self, textvariable=self.word_text, width=65)
        self.e1.grid(row=0, column=1, columnspan=3, pady=7)

        self.b1 = tk.Button(self, width=8, text='Define', command=self.definition, relief=tk.RAISED)
        self.b1.grid(row=0, column=5)

        self.b2 = tk.Button(self, width=8, text='Clear', command=self.clear, relief=tk.RAISED)
        self.b2.grid(row=0, column=6)
        
        self.b2 = tk.Button(self, width=8, text='Close', command=self.destroy, relief=tk.RAISED)
        self.b2.grid(row=0, column=7)

        self.list1 = tk.Listbox(self, height=15, width=100, relief=tk.RIDGE)
        self.list1.grid(row=2, column=0, rowspan=5, columnspan=8, padx=2)

        self.sb1 = tk.Scrollbar(self)
        self.sb1.grid(row=2, column=9, rowspan=5)

        self.sb2 = tk.Scrollbar(self)
        self.sb2.grid(row=7,column=0,columnspan=16)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.configure(xscrollcommand=self.sb2.set)
        self.sb2.configure(command=self.list1.xview, orient = tk.HORIZONTAL)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        

    def definition(self):
        self.list1['state'] = 'normal'
        self.list1.delete(0, tk.END)
        if self.word_text.get() in data:
            dat = data[self.word_text.get()]
            
            for item in dat:
                self.list1.insert(tk.END, item)
            self.list1['state'] = 'disabled'
            
                
        elif self.word_text.get() == '':
            info = 'You have typed no word, try again!'
            messagebox.showerror("Error", info)

        else:
            suggestions_1 = get_close_matches(self.word_text.get(), data.keys(), n=5)
            if len(suggestions_1) > 0:
                self.list1.insert(tk.END, 'Word not found, Try again!')
                self.list1.insert(tk.END, 'Or try this suggestions:')
                for item in suggestions_1:
                    self.list1.insert(tk.END,item)
            
            else:
                self.list1.insert(tk.END, 'Sorry, there is no defition for the word typed')
                self.list1.insert(tk.END, 'And there are no suggestions!')
                self.list1.insert(tk.END, 'Type a new word.')
                
                
    def clear(self):
        self.list1['state'] = 'normal'
        self.list1.delete(0, tk.END)
        self.word_text.set('')
        info = 'All cleared!'
        messagebox.showerror("Info", info)


    def get_selected_row(self, event):
        global selected_tuple
        index=self.list1.curselection()[0]
        # print(index)
        selected_tuple=self.list1.get(index)
        self.e1.delete(0, tk.END)
        self.e1.insert(tk.END, selected_tuple)


if __name__=='__main__':
    app=Dictionary()
    app.mainloop()
