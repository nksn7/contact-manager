import uuid
contacts = []


def list_contacts(contacts_list):
    string_list = "Lista de Contatos\n\n"

    for contact in contacts_list:
        string_list += f"- {contact}\n"

    return string_list


def add_contact(name, phone, email):
    id_contact = uuid.uuid4()

    contact = {"ID": id_contact, "Nome": name, "Telefone": phone, "Email": email}

    for element in contacts:

        if element == contact:
            return False

    contacts.append(contact)

    return True


def found_contact(id_contact):
    contact_found = False

    for contact in contacts:

        if contact["ID"] == id_contact:
            contact_found = contact

    return contact_found


def remove_contact(id_contact):
    contact_remove = found_contact(id_contact)

    for contact in contacts:

        if contact == contact_remove:
            contacts.remove(contact_remove)
            break

    return contact_remove
