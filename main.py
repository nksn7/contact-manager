from contacts.contact_manager import *

if __name__ == "__main__":
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Pesquisar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome: ")
            phone = input("Telefone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            id_contact = input("ID a ser procurado: ")
            found_contact(id_contact)
        elif choice == '4':
            id_contact = input("ID a ser removido: ")
            remove_contact(id_contact)
        elif choice == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
