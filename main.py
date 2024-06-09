if __name__ == "__main__":
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            name = input("Nome: ")
            phone = input("Telefone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            name = input("Nome do contato a remover: ")
            remove_contact(name)
        elif choice == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
