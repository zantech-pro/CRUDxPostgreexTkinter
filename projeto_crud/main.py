import tkinter as tk
from tkinter import ttk, messagebox
from crud_db import DbConnect



## Funções do Sistema ###
# 
# Limpar Cmapos
def limpar_campos_input():
    conteudo_codigo = entry_codigo.get()
    conteudo_nome = entry_nome.get()
    conteudo_preco = entry_preco.get()

    if len(conteudo_codigo) > 0:
        for item in range(len(conteudo_codigo)+1):
            entry_codigo.delete(first=0)

    if len(conteudo_nome) > 0:  
        for item in range(len(conteudo_nome)+1):
            entry_nome.delete(first=0)

    if len(conteudo_preco) > 0:  
        for item in range(len(conteudo_preco)+1):
            entry_preco.delete(first=0)
    
    #Descobrir uma forma mais simples de limpar os campos
    #usando exemplo: entry_preco.option_clean() kkkkkkk


#Limpar Arvore TreeView para colocar dados nonos
def limpar_arvore_dados():
    itens_tela = coletanea.get_children()
    if len(itens_tela) > 0:
        for item in itens_tela:
            coletanea.delete(item)

# Selecionado itens para para exibir na TreeView
def atualizar():
    limpar_campos_input()
    limpar_arvore_dados()
    ha_itens = coletanea.get_children()
    if len(ha_itens) == 0:
        coletar_dados = DbConnect()
        coletar_dados.abrir_conn_db()
        registros = coletar_dados.selecionar_dados()

        if str(type(registros)) != "<class 'bool'>":
            if len(registros) > 1:
                for item in registros:
                    coletanea.insert(parent="", index="end", iid=item[0], text="", values=(item[0], item[1], item[2]))
            else:
                if len(registros) == 1:
                    coletanea.insert(parent="", index="end", iid=registros[0][0], text="", values=(registros[0][0], registros[0][1], registros[0][2]))
    else:
        limpar_arvore_dados()
        atualizar()


def cadastrar_item():
    status1 = status2 = status3 = False
    try:
        codigo = int(entry_codigo.get())
        status1 = True
    except ValueError as error:
        aviso = "Valor no campo 'codigo do produto' é invalido...\nInforme um valor numerico, sem ponto ou virgula."
        messagebox.showwarning("Atenção!!!", aviso)
        status1 = False
    
    nomeProduto = entry_nome.get()
    if nomeProduto == '':
        status2 = False
    else:
        status2 = True
    
    try:
        preco = float(entry_preco.get())
        status3 = True
    except ValueError as error:
        aviso = "Valor no campo 'Preço' é invalido...\nInforme um valor no formato, exemplo: 13.50 ou 1.50"
        messagebox.showwarning("Atenção!!!", aviso)
        status3 = False

    if status1 and status2 and status3:
        conexao_no_banco = DbConnect()
        conexao_no_banco.abrir_conn_db()  
        conexao_no_banco.inserir_dados(codigo, nomeProduto, preco)
        atualizar()
        
    

def excluir_item():
    status1 = status2 = status3 = False
    try:
        codigo = int(entry_codigo.get())
        status1 = True
    except ValueError as error:
        aviso = "Valor no campo 'codigo do produto' é invalido...\nInforme um valor numerico, sem ponto ou virgula."
        messagebox.showwarning("Atenção!!!", aviso)
        status1 = False
    
    nomeProduto = entry_nome.get()
    if nomeProduto == '':
        status2 = False
    else:
        status2 = True
    
    try:
        preco = float(entry_preco.get())
        status3 = True
    except ValueError as error:
        aviso = "Valor no campo 'Preço' é invalido...\nInforme um valor no formato, exemplo: 13.50 ou 1.50"
        messagebox.showwarning("Atenção!!!", aviso)
        status3 = False

    if status1 and status2 and status3:
        lista = coletanea.get_children()
        
        check1 = False
        if len(lista) > 0:
            for item in lista:
                if codigo == coletanea.item(item)["values"][0]:
                    check1 =  (nomeProduto == coletanea.item(item)["values"][1]) and preco == float(coletanea.item(item)["values"][2])
        if check1:
            conn = DbConnect()
            conn.abrir_conn_db()
            conn.excluir_dados(int(codigo))
            atualizar()
        else:
            messagebox.showwarning("Aviso: ", "Campos invalidos para exclusão, favor preencha novamente!!!")

def atualizar_item():
    status1 = status2 = status3 = False
    try:
        codigo = int(entry_codigo.get())
        status1 = True
    except ValueError as error:
        aviso = "Valor no campo 'codigo do produto' é invalido...\nInforme um valor numerico, sem ponto ou virgula."
        messagebox.showwarning("Atenção!!!", aviso)
        status1 = False
    
    nomeProduto = entry_nome.get()
    if nomeProduto == '':
        status2 = False
    else:
        status2 = True
    
    try:
        preco = float(entry_preco.get())
        status3 = True
    except ValueError as error:
        aviso = "Valor no campo 'Preço' é invalido...\nInforme um valor no formato, exemplo: 13.50 ou 1.50"
        messagebox.showwarning("Atenção!!!", aviso)
        status3 = False
    
    if status1 and status2 and status3:
        conexao_no_banco = DbConnect()
        conexao_no_banco.abrir_conn_db()
        conexao_no_banco.atualizar_dados(codigo, nomeProduto, preco)
        atualizar()
    else:
        messagebox.showwarning("Atenção!!!", "Existe campos invalidos!!!\nOperação não concluida.")

def modal_de_avisos(title, msg, tipo, error=False):
    if error:
        messagebox.showerror(title, msg)
    else:
        if tipo == "warning":
            messagebox.showwarning(title, msg)
        else:
            messagebox.showinfo(title, msg)





janela_principal = tk.Tk()
janela_principal.title("Bem Vindo a Aplicação de Banco de Dados")
janela_principal.geometry("800x600")
#janela_principal.configure(background='red')
janela_principal.columnconfigure(0, weight=1)
janela_principal.columnconfigure(1, weight=1)
janela_principal.columnconfigure(2, weight=1)
janela_principal.columnconfigure(3, weight=1)
janela_principal.columnconfigure(4, weight=1)
janela_principal.columnconfigure(5, weight=1)
janela_principal.rowconfigure(0, weight=1)
janela_principal.rowconfigure(1, weight=1)
janela_principal.rowconfigure(2, weight=1)
janela_principal.rowconfigure(3, weight=1)
janela_principal.rowconfigure(4, weight=1)
janela_principal.rowconfigure(5, weight=1)
janela_principal.rowconfigure(6, weight=1)
janela_principal.rowconfigure(7, weight=1)


#Tela que recebera os objetos (Widget)
tela = ttk.Frame(janela_principal, padding="10 20 10 20")
tela.grid(column=1, row=1, columnspan=4, rowspan=6, sticky="nsew")
tela.columnconfigure(0, weight=1)
tela.columnconfigure(1, weight=1)
tela.columnconfigure(2, weight=1)
tela.columnconfigure(3, weight=1)
tela.columnconfigure(4, weight=1)
tela.columnconfigure(5, weight=1)
tela.rowconfigure(0, weight=1)
tela.rowconfigure(1, weight=1)
tela.rowconfigure(2, weight=1)
tela.rowconfigure(3, weight=1)
tela.rowconfigure(4, weight=1)
tela.rowconfigure(5, weight=1)
tela.rowconfigure(6, weight=1)
tela.rowconfigure(7, weight=1)


#Campos de Legenda
lbl_codigo = ttk.Label(tela, text="Código do Produto")
lbl_nome = ttk.Label(tela, text="Nome do Produto")
lbl_preco = ttk.Label(tela, text="Preço")

#Campos de entrada
entry_codigo = ttk.Entry(tela)
entry_nome = ttk.Entry(tela)
entry_preco= ttk.Entry(tela)

# botoes
btn_cadastrar = ttk.Button(tela, text="Cadastrar", command=cadastrar_item)
btn_atualizar = ttk.Button(tela, text="Atualizar", command=atualizar_item)
btn_excluir = ttk.Button(tela, text="Excluir", command=excluir_item)
btn_limpar = ttk.Button(tela, text="Limpar", command=limpar_campos_input)

#Lista (Treview)
coletanea = ttk.Treeview(tela)
coletanea['columns'] = ("Codigo", "Nome do Produto", "Preço")
coletanea.column("#0", width=0, stretch=0) #ocultando a coluna
coletanea.column("Codigo", anchor="center", width=120)
coletanea.column("Nome do Produto", anchor="center", width=120)
coletanea.column("Preço", anchor="center", width=120)

coletanea.heading("#0", text="", anchor='w') #tirando nome da coluna
coletanea.heading("Codigo", text="Codigo", anchor='center')
coletanea.heading("Nome do Produto", text="Nome do Produto", anchor='center')
coletanea.heading("Preço", text="Preço", anchor='center')



# coletanea.delete(20) #deleta usado a ref. pelo iid


#mode de selecionar item
def seleciona(evento):
    limpar_campos_input()
    dirc_dados = coletanea.item(coletanea.focus())
    
    if len(dirc_dados['values']) > 0:
        entry_codigo.insert(index=0, string=str(dirc_dados["values"][0]))
        entry_nome.insert(index=0, string=str(dirc_dados["values"][1]))
        entry_preco.insert(index=0, string=str(dirc_dados["values"][2]))


    

coletanea.bind("<<TreeviewSelect>>", seleciona)







# Distribuição na Grid

lbl_codigo.grid(column=1, row=1, sticky='E')
lbl_nome.grid(column=1, row=2, sticky='E')
lbl_preco.grid(column=1, row=3, sticky='E')

entry_codigo.grid(column=2, row=1, columnspan=3, sticky='w', padx=20)
entry_nome.grid(column=2, row=2, columnspan=3, sticky='w', padx=20)
entry_preco.grid(column=2, row=3, columnspan=3, sticky='w', padx=20)

btn_cadastrar.grid(column=1, row=4)
btn_atualizar.grid(column=2, row=4)
btn_excluir.grid(column=3, row=4)
btn_limpar.grid(column=4, row=4)

coletanea.grid(column=1, columnspan=4, row=5, rowspan=7, sticky="nsew")



atualizar()


# Incia Loope que permite nosso sistema funcionar sem parar para cliente possa interagir
janela_principal.mainloop()