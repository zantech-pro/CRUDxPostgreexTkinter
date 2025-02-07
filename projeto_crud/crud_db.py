### Class para operações C - R - U - D (Criar(creat) - Ler(Read) - Atualizar(update) - Deletar(Delete) ###

#import das bibliotecas
import psycopg2 as pg2
from tkinter import messagebox


#Classse usada penas para agrupar os produtos, em conjunto com metodos da classe DbConnect que servião para alteraçãoes de dados no banco (Inserte, update)
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class DbConnect:

    def __init__(self):
        pass
    
    # Metodo para instaciar uma conexão com banco de dados
    def abrir_conn_db(self):   
        try:

            self.conexao = pg2.connect(database="projeto_estacio", user="postgres", password="perola7512", host="127.0.0.1", port="5432")

        except (Exception, pg2.Error) as erro:
            aviso = "Problema de conectividade!\nSe persistir contacte o admnistrador!", erro
            messagebox.showerror("Error: ", aviso)
    
    #Inserir dados no banco de dados
    def inserir_dados(self, codigo, nome, preco):

        self.conector = self.conexao.cursor()
        comando_sql = '''INSERT INTO produtos (codigo, nome, preco) VALUES (%s, %s, %s)'''
        dados = (codigo, nome, preco)
        try:
            self.conector.execute(comando_sql, dados)
            self.conexao.commit()
            #numero_alteracoes = self.conector.rowcount
            messagebox.showinfo("Informação: ", "Registro inserido com sucesso!!!")
        except (Exception, pg2.Error) as error:
            aviso = "Erro ao inserir dados... ", error
            messagebox.showerror("Error: ", aviso)
        finally:
            self.conector.close()
            self.conexao.close()

    #Inserir dados no banco de dados
    def selecionar_dados(self):
        try:
            self.conector = self.conexao.cursor()
        except(Exception, pg2.Error) as error:
            aviso = "Erro ao tentar conectar na base de dados..."
            messagebox.showerror("Error: ", aviso)
            return False

        comando_sql = '''SELECT codigo, nome, preco FROM produtos'''
        try:
            self.conector.execute(comando_sql)
            dados_coletados = self.conector.fetchall()
        except (Exception, pg2.Error) as error:
            aviso = "Erro ao coletar dados... ", error
            messagebox.showerror("Error: ", aviso)
        finally:
            self.conector.close()
            self.conexao.close()
        return dados_coletados
    
    def atualizar_dados(self, codigo, nome, preco):

        self.conector = self.conexao.cursor()
        comando_sql = '''UPDATE produtos SET (nome, preco) = (%s, %s) WHERE codigo = %s'''
        dados = (nome, preco, codigo)
        try:
            self.conector.execute(comando_sql, dados)
            self.conexao.commit()
            #linhas_alteradas = self.conector.rowcount
        except (Exception, self.conexao.Error) as error:
            aviso = "Erro ao tentar altera dados... ", error
            messagebox.showerror("Error: ", aviso)
        finally:
            self.conector.close()
            self.conexao.close()

    def excluir_dados(self, codigo):

        self.conector = self.conexao.cursor()
        comando_sql = '''DELETE FROM produtos WHERE codigo = %s'''
        try:
            self.conector.execute(comando_sql, (codigo,))
            self.conexao.commit()
            #linhas_alteradas = self.conector.rowcount
        except (Exception, self.conexao.Error) as error:
            aviso = "Erro ao tentar excluir dados... ", error
            messagebox.showerror("Error: ", aviso)
        finally:
            self.conector.close()
            self.conexao.close()
