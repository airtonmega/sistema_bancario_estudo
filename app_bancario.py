import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class SistemaBancario:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Controle Bancário")
        self.master.geometry("450x350")
        self.master.resizable(False, False)

        # Estilo moderno e bancário para os widgets
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=6)
        style.configure('TLabel', font=('Arial', 12), foreground="black")
        style.configure('Saldo.TLabel', font=('Arial', 14, 'bold'), foreground="black")
        style.configure('Autor.TLabel', font=('Arial', 10, 'italic'), foreground="black")

        # Estilo personalizado para os botões
        style.configure('Depositar.TButton', foreground="#006600")  # Verde escuro
        style.configure('Sacar.TButton', foreground="#cc0000")      # Vermelho
        style.configure('Extrato.TButton', foreground="#000066")    # Azul escuro
        style.configure('Sair.TButton', foreground="#660000")       # Marrom escuro

        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

        # Frame para o saldo
        frame_saldo = ttk.Frame(master, padding="10")
        frame_saldo.pack(pady=10)

        self.label_saldo_text = ttk.Label(frame_saldo, text="Saldo Atual:", style='Saldo.TLabel')
        self.label_saldo_text.grid(row=0, column=0, sticky='w')

        self.label_saldo = ttk.Label(frame_saldo, text=f"R$ {self.saldo:.2f}", style='Saldo.TLabel')
        self.label_saldo.grid(row=0, column=1, sticky='e')

        # Frame para os botões
        frame_botoes = ttk.Frame(master, padding="10")
        frame_botoes.pack(pady=20)

        self.btn_depositar = ttk.Button(frame_botoes, text="Depositar", command=self.depositar, style='Depositar.TButton', width=20)
        self.btn_depositar.grid(row=0, column=0, padx=10, pady=5)

        self.btn_sacar = ttk.Button(frame_botoes, text="Sacar", command=self.sacar, style='Sacar.TButton', width=20)
        self.btn_sacar.grid(row=1, column=0, padx=10, pady=5)

        self.btn_extrato = ttk.Button(frame_botoes, text="Extrato", command=self.extrato_, style='Extrato.TButton', width=20)
        self.btn_extrato.grid(row=2, column=0, padx=10, pady=5)

        self.btn_sair = ttk.Button(frame_botoes, text="Sair", command=master.quit, style='Sair.TButton', width=20)
        self.btn_sair.grid(row=3, column=0, padx=10, pady=5)

        # Adicionando o nome do autor e o título do bootcamp
        frame_autor = ttk.Frame(master, padding="10")
        frame_autor.pack(side=tk.BOTTOM, anchor=tk.W)

        self.label_autor = ttk.Label(frame_autor, text="José Airton - Bootcamp Dio Engenharia de Dados", style='Autor.TLabel')
        self.label_autor.pack(side=tk.LEFT)

    def depositar(self):
        valor = self.get_valor("Informe o valor do depósito:")
        if valor is None:
            return

        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            self.update_saldo()
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def sacar(self):
        valor = self.get_valor("Informe o valor do saque:")
        if valor is None:
            return

        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            messagebox.showerror("Erro", "Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            messagebox.showerror("Erro", "Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            messagebox.showerror("Erro", "Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            self.update_saldo()
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def extrato_(self):
        extrato_str = "Não foram realizadas movimentações." if not self.extrato else self.extrato
        extrato_str += f"\nSaldo: R$ {self.saldo:.2f}"
        messagebox.showinfo("Extrato", extrato_str)

    def update_saldo(self):
        self.label_saldo.config(text=f"R$ {self.saldo:.2f}")

    def get_valor(self, mensagem):
        valor_str = simpledialog.askstring("Entrada", mensagem)
        if valor_str is None:
            return None
        try:
            valor = float(valor_str)
            return valor
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido! Por favor, insira um número válido.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaBancario(root)
    root.mainloop()
