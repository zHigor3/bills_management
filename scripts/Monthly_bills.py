import json
import tkinter as tk
from tkinter import ttk

class Monthly_bills:
   def __init__(self, window, monthly, year):
      # Carrega as contas do banco de dados
      with open('./data/db.json') as file:
         self.content = file.read()
         self.bills = json.loads(self.content)

      # Separa as contas do mês atual
      self.list_monthly_bills = []
      for i in self.bills:
         if i['monthly'] == monthly and i['year'] == year:
            self.list_monthly_bills.append(i)

      # Frame que vai conter a lista de contas do mês atual/selecionado
      self.bills_frame = tk.Frame(window, width=300, height=200, bd=1, relief=tk.SOLID)
      self.bills_frame.place(x=300, y=5)

      # Mostra a conta selecionada
      def on_select(event):
         item = self.bills_list.focus()

         # Criação do popup
         self.bills_edit_popup = tk.Tk()
         self.bills_edit_popup.title("Bills Edit")
         self.bills_edit_popup.geometry("300x100")

         self.entry = tk.Entry(self.bills_edit_popup, width=30)
         self.entry.grid(row=0, column=1)
         self.entry.insert(0, self.bills_list.item(item)['values'][0])

         self.bills_edit_popup.mainloop()

         # print("Item selecionado:", self.bills_list.item(item)['values'])

      # Verifica se têm contas do mês
      if len(self.list_monthly_bills) > 0:
         # Criação do título do frame
         self.rotulo = tk.Label(self.bills_frame, text="Contas do mês")
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
         for i in self.list_monthly_bills:
            self.bills_list.insert("", tk.END, values=(i['name'], str(f"R$ {'{:.2f}'.format(i['value'])}")))

         # Associação da função on_select() ao evento de seleção
         self.bills_list.bind("<<TreeviewSelect>>", on_select)

      else:
         # Criação do título do frame
         self.rotulo = tk.Label(self.bills_frame, text="Não têm contas para este mês")
         self.rotulo.grid(row=0, column=0)
         