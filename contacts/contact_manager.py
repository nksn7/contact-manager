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


def pesquisar_contato(id_contato):
    contato_encontrado = False

    for contato in contatos:

        if contato["ID"] == id_contato:
            contato_encontrado = contato

    return contato_encontrado


def exclui_contato(id_contato):
    contato_excluir = pesquisar_contato(id_contato)

    for contato in contatos:

        if contato == contato_excluir:
            contatos.remove(contato_excluir)
            break

    return contato_excluir
