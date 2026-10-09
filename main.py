from models import Animal, BankAccount, Cart, Dog, FileManager, Product, Table


def main() -> None:
    print("=== Лабораторная работа № 3 (Вариант 3) ===")

    # 1. Банковский счёт (Средняя № 3)
    account = BankAccount("Арсений Юрченко", 1000.0)
    account.deposit(500.0)
    account.withdraw(300.0)
    print(f"[Средняя 3] Банковский счет: {account}, текущий баланс: {account.balance:.2f} руб.")

    # 2. Наследование: Животное -> Собака (Средняя № 5)
    dog = Dog(name="Бим", age=3, breed="Лабрадор")
    generic_animal = Animal(name="Лесной житель", age=5)
    print(f"[Средняя 5] Базовый класс: {generic_animal.speak()}")
    print(f"[Средняя 5] Наследник: {dog.speak()} | {dog.fetch('мячик')}")

    # 3. Класс для работы с файлами (Средняя № 9)
    file_worker = FileManager("demo_file.txt")
    file_worker.write("Пример безопасной записи в файл через FileManager.\n")
    file_content = file_worker.read().strip()
    print(f"[Средняя 9] Чтение из файла: '{file_content}' (существует: {file_worker.exists()})")
    file_worker.delete()

    # 4. Система заказов: Товар и Корзина (Повышенная № 3)
    laptop = Product("Ноутбук", 75000.0)
    mouse = Product("Мышь", 2500.0)
    cart = Cart()
    cart.add_product(laptop, quantity=1)
    cart.add_product(mouse, quantity=2)
    print(f"[Повышенная 3] Позиции в корзине: {cart.get_items()}")
    print(f"[Повышенная 3] Итоговая стоимость заказа: {cart.calculate_total():.2f} руб.")

    # 5. Мини-ORM Таблица (Повышенная № 7)
    users_table = Table(name="users", schema=["username", "role", "active"])
    users_table.insert({"username": "arsenij", "role": "admin", "active": True})
    users_table.insert({"username": "ivan", "role": "user", "active": True})
    users_table.insert({"username": "guest_12", "role": "user", "active": False})

    admin_records = users_table.select(role="admin")
    active_users = users_table.select(predicate=lambda row: row["active"] is True)

    print(f"[Повышенная 7] ORM select(role='admin'): {admin_records}")
    print(f"[Повышенная 7] ORM select активных пользователей: {len(active_users)} записи")


if __name__ == "__main__":
    main()