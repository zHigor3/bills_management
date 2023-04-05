import json
import tkinter as tk
from tkinter import ttk
from functools import partial

class Monthly_bills:
   def __init__(self, window, monthly, year):
      # Carrega as contas do banco de dados
      with open('./data/db.json') as file:
         self.content = file.read()
         self.bills = json.loads(self.content)

      # Frame que vai conter a lista de contas do mês atual/selecionado
      self.bills_frame = tk.Frame(window, width=300, height=200, bd=1, relief=tk.SOLID)
      self.bills_frame.place(x=300, y=5)

      try:
         # Acessa as contas da data selecionada
         self.bills = self.bills[str(year)][monthly]
   
         # Separa as contas do mês atual
         self.list_monthly_bills = []
         for i in self.bills:
            self.list_monthly_bills.append(i)
         
         self.container_bills(window, self.bills_frame, self.list_monthly_bills)

      except:
         # Criação do título do frame
         self.rotulo = tk.Label(self.bills_frame, text="Não têm contas para este mês")
         self.rotulo.grid(row=0, column=0)
         print("Não tem contas para o mês selecionado")

   def container_bills(self, window, frame, bills):
      # Criação do título do frame
      self.rotulo = tk.Label(frame, text="Contas do mês")
      self.rotulo.grid(row=0, column=0)

      # Criando o Treeview com duas colunas
      self.bills_list = ttk.Treeview(frame, columns=("col1", "col2", "col3"), show="headings")
      self.bills_list.grid(row=1, column=0)

      # Definindo o cabeçalho das colunas
      self.bills_list.heading("#1", text="ID")
      self.bills_list.heading("#2", text="Conta")
      self.bills_list.heading("#3", text="Valor")

      # Definindo largura das colunas
      self.bills_list.column("#0", width=0, stretch=tk.NO)
      self.bills_list.column("#3", width=80)
      self.bills_list.column("#1", width=30)

      # Adiciona as contas recorrentes no listbox
      for i in bills:
         self.bills_list.insert("", tk.END, values=(i['id'], i['name'], str(f"R$ {'{:.2f}'.format(i['value'])}")))

      # Associação da função on_select() ao evento de seleção
      self.bills_list.bind("<<TreeviewSelect>>", self.on_select)   

   # Mostra a conta selecionada
   def on_select(self, event):
      item = self.bills_list.focus()
      self.Id = self.bills_list.item(item)['values'][0]
      self.description = self.bills_list.item(item)['values'][1]
      self.value = self.bills_list.item(item)['values'][2]

      # Criação do popup
      self.bills_edit_popup = tk.Tk()
      self.bills_edit_popup.title("Bills Edit")
      self.bills_edit_popup.geometry("300x100")

      # Campo de descrição
      self.description_label = tk.Label(self.bills_edit_popup, text="Descrição")
      self.description_label.grid(row=0, column=0)
      self.description_entry = tk.Entry(self.bills_edit_popup, width=30)
      self.description_entry.grid(row=0, column=1)
      self.description_entry.insert(0, self.description)

      # Campo de valor
      self.value_label = tk.Label(self.bills_edit_popup, text="Valor")
      self.value_label.grid(row=1, column=0)
      self.value_entry = tk.Entry(self.bills_edit_popup, width=30)
      self.value_entry.grid(row=1, column=1)
      self.value_entry.insert(0, self.value)

      # Botão que atualiza a conta
      self.update = tk.Button(
         self.bills_edit_popup, 
         text="Atualizar", 
         command=partial(
            self.update_bill, 
            self.Id, 
            self.value_entry, 
            self.description_entry
         )
      )

      self.update.grid(row=2, column=1)

      self.bills_edit_popup.mainloop()
      # print("Item selecionado:", self.bills_list.item(item)['values'])

   def update_bill(self, Id, desc, val):
      print(Id, desc.get(), val.get())
