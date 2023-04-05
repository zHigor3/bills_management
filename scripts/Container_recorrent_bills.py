import json
import tkinter as tk
from tkinter import ttk

class Container_recorrent_bills:
   def __init__(self, window):
      # Lê as contas recorrentes
      with open('./data/bills.json') as file:
         self.content = file.read()
         self.bills = json.loads(self.content)

      # Frame que vai conter a lista de contas
      self.bills_frame = tk.Frame(window, width=300, height=200, bd=1, relief=tk.SOLID)
      self.bills_frame.place(x=5, y=5)

      # Criação do título do frame
      self.rotulo = tk.Label(self.bills_frame, text="Contas Recorrentes")
      self.rotulo.grid(row=0, column=0)

      # Criando o Treeview com duas colunas
      self.bills_list = ttk.Treeview(self.bills_frame, columns=("col1", "col2"), show="headings")
      self.bills_list.grid(row=1, column=0)

      # Definindo o cabeçalho das colunas
      self.bills_list.heading("#1", text="Conta")
      self.bills_list.heading("#2", text="Valor")

      # Definindo largura das colunas
      self.bills_list.column("#0", width=0, stretch=tk.NO)
      self.bills_list.column("#2", width=80)

      # Adiciona as contas recorrentes no listbox
      for i in self.bills:
         self.bills_list.insert("", tk.END, values=(i['name'], str(f"R$ {'{:.2f}'.format(i['value'])}")))
         