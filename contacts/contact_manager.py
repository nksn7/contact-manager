contatos = []


def listar_contatos(lista):
    string_listagem = "Lista de Contatos\n\n"

    for contato in lista:
        string_listagem += f"{contato}\n"

    return string_listagem
