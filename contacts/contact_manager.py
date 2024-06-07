contatos = []


def listar_contatos(lista):
    string_listagem = "Lista de Contatos\n\n"

    for contato in lista:
        string_listagem += f"{contato}\n"

    return string_listagem


def adicionar_contato(id_contato, nome, telefone, email):
    contato = {"ID": id_contato, "Nome": nome, "Telefone": telefone, "Email": email}

    for elemento in contatos:

        if elemento == contato:
            return False

    contatos.append(contato)

    return True
