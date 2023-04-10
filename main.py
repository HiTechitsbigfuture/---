

# создаем пустой список для хранения клиентов
clients = []

# функция для регистрации клиента
def register():
    print("Регистрация клиента")
    name = input("Введите ваше имя: ").strip()
    age = int(input("Введите ваш возраст: ").strip())
    gender = input("Введите ваш пол (м/ж): ").strip().lower()
    email = input("Введите ваш email: ").strip()
    phone = input("Введите ваш номер телефона: ").strip()
    membership = input("Введите тип вашей подписки (один раз в неделю/два раза в неделю/безлимит): ").strip().lower()
    
    client = {
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "membership": membership
    }

    clients.append(client)
    
    print()
    print("Вы успешно зарегистрировались в фитнес-клубе!")
    print()

    return client

# функция для вывода списка клиентов
def show_clients():
    print("Список клиентов")
    for client in clients:
        print("Имя: {}, Возраст: {}, Пол: {}, Email: {}, Телефон: {}, Подписка: {}".format(
            client["name"], client["age"], client["gender"], client["email"], client["phone"], client["membership"]))
    print()

# функция для поиска клиента по имени
def find_client(name):
    for client in clients:
        if client["name"].lower() == name.lower():
            return client
    return None

# функция для удаления клиента
def delete_client(name):
    client = find_client(name)
    if client:
        clients.remove(client)
        print()
        print("Клиент '{}' успешно удален".format(name))
        print()
    else:
        print()
        print("Клиент '{}' не найден".format(name))
        print()

# клиентский интерфейс
while True:
    print("Фитнес-клуб")
    print("1. Зарегистрироваться")
    print("2. Показать список клиентов")
    print("3. Удалить клиента")
    print("4. Выход")

    choice = input("Выберите пункт: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        show_clients()
    elif choice == "3":
        name = input("Введите имя клиента, которого хотите удалить: ").strip()
        delete_client(name)
    elif choice == "4":
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
    print()
  
