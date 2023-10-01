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

def buscar_contato(criterio):

    sql = "SELECT * FROM contatos WHERE codigo = %s OR nome LIKE %s OR telefone LIKE %s OR email LIKE %s"

    cursor.execute(sql, (criterio, f"%{criterio}%", criterio, criterio))
    resultado = cursor.fetchall()

    if resultado:
        print("\nResultados encontrado:\n")
        for contato in resultado:
            print(f"Código: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")
    else:
        print("Nenhum resultado encontrado")
        
def mostrar_contatos():

    sql = "SELECT * FROM contatos"

    cursor.execute(sql)
    resultados = cursor.fetchall()

    if resultados:
        print("\nContatos na agenda:\n")
        for contato in resultados:
            print(f"Contato: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

    else:
        print("Nenhum contato encontrado na agenda.")

def atualizar_contato(codigo, nome):

    sql = "UPDATE contatos SET nome = %s, telefone = %s, email = %s WHERE codigo = %s"
    
    valores = (nome, telefone, email, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def atualizar_telefone(codigo, novo_email):

    sql = "UPDATE contatos SET nome = %s, telefone = %s, email = %s WHERE codigo = %s"
    
    valores = (nome, telefone, email, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def atualizar_email(codigo, nome):

    sql = "UPDATE contatos SET nome = %s, telefone = %s, email = %s WHERE codigo = %s"
    
    valores = (nome, telefone, email, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def excluir_contato(codigo):

    sql = "DELETE FROM contatos WHERE codigo= %s"

    cursor.execute(sql, (codigo, ))
    conexao.commit()
    print("Contato excluido.")


while True:
    print("\nOpções:\n")
    print("1. Cadastrar contato")
    print("2. Buscar contato")
    print("3. Mostrar contato")
    print("4. Atualizar/Alterar contato")
    print("5. Excluir contato")
    print("6. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("\nNome: ")

        telefones = []
        while True:
            telefone = input ("Telefone: ")
            telefone.append(telefone)
            add_telefone = input("Deseja adicionar mais um telefone? (s/n): ")
            
            if add_telefone.lower() != 's':
                break

        email = []
        while True:
            email = input("Email: ")
            email.append(email)
            add_email = input("Deseja adicionar mais um email? (s/n): ")

            if add_email.lower() != 's':
                break
        cadastar_contato(nome, telefone, email)

    elif opcao == "2":
        criterio = input("Digite o código, nome, telefone ou email para buscar: ")
        buscar_contato(criterio)

    elif opcao == "3":
        mostrar_contatos()

    elif opcao == "4":
        mostrar_contatos()
        codigo = int(input("\nDigite o código do contato que deseja alterar: "))

        print("\nOpção de atualização:\n")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Voltar")

        escolha = input("Qual deseja atualizar: ")

        if escolha == '1':
            novo_nome = input("Novo Nome: ")
            atualizar_contato(codigo, novo_nome)
            mostrar_contatos()

        elif escolha == '2':
            novo_telefone = input("Novo telefone: ")
            atualizar_contato(codigo, novo_telefone)
            mostrar_contatos()

        elif escolha == '3':
            novo_email = input("Novo email: ")
            atualizar_contato(codigo, novo_email)
            mostrar_contatos()

        elif escolha == '4':
            print("Operação de atualização cancelada")
    
        else:
            print("Opçao invalida. Tente novamente")


        nome = input("Novo Nome: ")
        telefone = input ("Novo Telefone: ")
        email = input("Novo Email: ")
        atualizar_contato(codigo, nome, telefone, email)
    
    elif opcao == "5":
        mostrar_contatos()
        codigo = int(input("\nDigite o código do contato que deseja excluir: "))
        excluir_contato(codigo)

    elif opcao == "6":
        print("Encerrando Programa")
        break

    else:
        print("Opção inválida. Tenta novamente.")
 
conexao.close()