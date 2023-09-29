cadastrar_contato = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
mostrar_contato = "SELECT * FROM contatos"
alterar_contato = "UPDATE contatos SET nome = %s, telefone = %s, email = %s WHERE codigo = %s"
excluir_contato = "DELETE FROM contatos WHERE codigo= %s"