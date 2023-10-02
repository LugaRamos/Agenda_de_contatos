import mysql.connector
import os

conexao = mysql.connector.connect(
    host="wagnerweinert.com.br",
    user="tads22_luis",
    password="tads22_luis",
    database="tads22_luis",
)

cursor = conexao.cursor()

def cadastar_contato(nome, telefone, email):

    sql = "INSERT INTO contato (nome) VALUES (%s)"

    cursor.execute(sql, (nome,))
    conexao.commit()

    codigo = cursor.lastrowid 

    cursor.execute("SELECT COUNT(*) FROM telefone WHERE telefone = %s", (telefone,))
    resultado = cursor.fetchone()

    if resultado[0] == 0:
        sql = "INSERT INTO telefone (telefone, codigo) VALUES (%s, %s)"
        cursor.execute(sql, (telefone, codigo))
        conexao.commit()

    cursor.execute("SELECT COUNT(*) FROM email WHERE email = %s", (email,))
    resultado = cursor.fetchone()

    if resultado[0] == 0: 
        sql = "INSERT INTO email (email, codigo) VALUES (%s, %s)"
        cursor.execute(sql, (email, codigo))
        conexao.commit()
    
    print("Contato cadastrado")

def buscar_contato(criterio):

    sql = """SELECT c.codigo, c.nome, GROUP_CONCAT(DISTINCT t.telefone ORDER BY t.telefone ASC SEPARATOR ', ') AS telefones,
                        GROUP_CONCAT(DISTINCT e.email ORDER BY e.email ASC SEPARATOR ', ') AS emails
                 FROM contato c
                 LEFT JOIN telefone t ON c.codigo = t.codigo
                 LEFT JOIN email e ON c.codigo = e.codigo
                 WHERE c.codigo = %s OR c.nome LIKE %s OR t.telefone LIKE %s OR e.email LIKE %s
                 GROUP BY c.codigo, c.nome
                 """

    cursor.execute(sql, (criterio, f"%{criterio}%", criterio, criterio))
    resultado = cursor.fetchall()

    if resultado:
        print("\nResultados encontrados:\n")
        for contato in resultado:
            codigo, nome, telefones, emails = contato
            print(f"Código: {codigo}, Nome: {nome}")
            if telefones:
                print(f"Telefones: {telefones}")
            if emails:
                print(f"Emails: {emails}")
            print()
    else:
        print("Nenhum resultado encontrado")
        
def mostrar_contatos():

    sql_contato = "SELECT * FROM contato"

    cursor.execute(sql_contato)
    contatos = cursor.fetchall()

    if contatos:
        print("\nContatos na agenda:\n")
        for contato in contatos:
            codigo = contato[0]
            nome = contato[1]

            sql_telefone = "SELECT telefone FROM telefone WHERE codigo = %s"
            cursor.execute(sql_telefone, (codigo,))
            telefones = [telefone[0] for telefone in cursor.fetchall()] 

            sql_email= "SELECT email FROM email WHERE codigo = %s"
            cursor.execute(sql_email, (codigo,))
            emails = [email[0] for email in cursor.fetchall()] 

            print(f"Código: {codigo} \nNome: {nome} \nTelefones: {', '.join(map(str, telefones))} \nEmails: {', '.join(map(str, emails))}")

    else:
        print("Nenhum contato encontrado na agenda.")

def atualizar_contato(codigo, nome):

    sql = "UPDATE contato SET nome = %s WHERE codigo = %s"
    
    valores = (nome, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def atualizar_telefone(codigo, novo_telefone):

    sql = "UPDATE telefone SET telefone = %s WHERE codigo = %s"
    
    valores = (novo_telefone, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def atualizar_email(codigo, novo_email):

    sql = "UPDATE email SET email = %s WHERE codigo = %s"
    
    valores = (novo_email, codigo)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Contato atualizado")

def excluir_contato(codigo):

    sql_telefone = "DELETE FROM telefone WHERE codigo= %s"

    cursor.execute(sql_telefone, (codigo,))
    conexao.commit()
    
    sql_email = "DELETE FROM email WHERE codigo= %s"

    cursor.execute(sql_email, (codigo,))
    conexao.commit()

    sql_contato = "DELETE FROM contato WHERE codigo= %s"

    cursor.execute(sql_contato, (codigo,))
    conexao.commit()


    print("Contato excluido.")


while True:
    os.system("cls")
    print("\nOpções:\n")
    print("1. Cadastrar contato")
    print("2. Buscar contato")
    print("3. Mostrar contato")
    print("4. Atualizar/Alterar contato")
    print("5. Excluir contato")
    print("6. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        os.system("cls")
        nome = input("\nNome: ")

        telefones = []
        while True:
            telefone = input ("Telefone: ")
            telefones.append(telefone)
            add_telefone = input("Deseja adicionar mais um telefone? (s/n): ")
            
            if add_telefone.lower() != 's':
                break

        emails = []
        while True:
            email = input("Email: ")
            emails.append(email)
            add_email = input("Deseja adicionar mais um email? (s/n): ")

            if add_email.lower() != 's':
                break
        cadastar_contato(nome, telefone, email)

    elif opcao == "2":
        os.system("cls")
        criterio = input("Digite o código, nome, telefone ou email para buscar: ")
        buscar_contato(criterio)

    elif opcao == "3":
        os.system("cls")
        mostrar_contatos()

    elif opcao == "4":
        os.system("cls")
        mostrar_contatos()
        codigo = int(input("\nDigite o código do contato que deseja alterar: "))

        print("\nOpção de atualização:\n")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Voltar")

        escolha = input("\nQual deseja atualizar:\n")

        os.system("cls")
        if escolha == '1':
            novo_nome = input("Novo Nome: ")
            atualizar_contato(codigo, novo_nome)
            mostrar_contatos()

        elif escolha == '2':
            novo_telefone = input("Novo telefone: ")
            atualizar_telefone(codigo, novo_telefone)
            mostrar_contatos()

        elif escolha == '3':
            novo_email = input("Novo email: ")
            atualizar_email(codigo, novo_email)
            mostrar_contatos()

        elif escolha == '4':
            print("Operação de atualização cancelada")
    
        else:
            print("Opçao invalida. Tente novamente")
    
    elif opcao == "5":
        os.system("cls")
        mostrar_contatos()
        codigo = int(input("\nDigite o código do contato que deseja excluir: "))
        excluir_contato(codigo)

    elif opcao == "6":
        os.system("cls")
        print("Encerrando Programa")
        break

    else:
        print("Opção inválida. Tenta novamente.")
 
conexao.close()