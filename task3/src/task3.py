import os

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def iter_through_docs(doc: str) -> dict:
    for item in documents:
        if doc == item['number']:
            return item


def get_doc_by_num():
    ans = input("Введите номер документа: ")
    doc_res = iter_through_docs(ans)

    print(f"Владелец документа: {doc_res['name']}")
    return


def on_quit():
    os.system('pause')
    return False


def parse_args(u_input: str) -> None | bool:
    if u_input == 'p':
        return get_doc_by_num()
    if u_input == 'q':
        return on_quit()
    return None


def get_first_input():
    return input('Введите команду: ')


def main():
    while True:
        u_input = get_first_input()
        arg = parse_args(u_input)
        if arg is False:
            break

if __name__ == '__main__':
    main()
