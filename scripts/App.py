import datetime
import tkinter as tk

# Classes auxiliares
from Container_recorrent_bills import Container_recorrent_bills
from Monthly_bills import Monthly_bills

class App:
   def __init__(self, window, title, resolution):
      # Configurações da janela
      window.title(title)
      window.geometry(resolution)

      # Obtenção do mês atual
      self.monthly = datetime.datetime.now().month
      self.monthly = datetime.date(1900, self.monthly, 1).strftime('%B')

      # Obtenção do ano atual
      self.year = datetime.datetime.now().year
      
      # Cria o container de contas recorrentes
      Container_recorrent_bills(window)

      # Cria o container de contas do mês
      Monthly_bills(window, self.monthly, self.year)

      # Executa a janela
      window.mainloop()
   
# Estancia a classe App e executa o programa
app = App(tk.Tk(), "My Bills", "800x500")
