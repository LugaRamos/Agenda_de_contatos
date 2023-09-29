import mysql.connector

conexao = mysql.connector.connect(
    host="wagnerweinert.com.br",
    user="tads22_luis",
    password="tads22_luis",
    database="tads22_luis",
)

cursor = conexao.cursor()

def cadastar_contato(nome, telefone, email):

    sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
    
    valores = (nome, telefone, email)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Contato cadastrado")

def mostrar_contatos():

    sql = "SELECT * FROM contatos"

    cursor.execute(sql)
    resultados = cursor.fetchall()

    if resultados:
        print("Contatos na agenda:")
        for contato in resultados:
            print(f"Código: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

    else:
        print("Nenhum contato encontrado na agenda.")

while True:
    print("\nOpções:")
    print("1. Cadastrar contato")
    print("2. Mostrar contato")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input ("Telefone: ")
        email = input("Email: ")
        cadastar_contato(nome, telefone, email)

    elif opcao == "2":
        mostrar_contatos()
    
    else:
        print("Opção inválida. Tenta novamente.")
 
conexao.close()