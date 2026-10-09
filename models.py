class BankAccount:
    """Класс банковского счета с операциями пополнения и снятия (Средняя № 3)."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if not owner or not isinstance(owner, str):
            raise ValueError("Владелец счета должен быть непустой строкой.")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner: str = owner
        self._balance: float = float(initial_balance)

    @property
    def balance(self) -> float:
        """Текущий остаток на счете."""
        return self._balance

    def deposit(self, amount: float) -> float:
        """Пополнение счета на указанную сумму."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительным числом.")
        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Снятие указанной суммы при наличии средств."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительным числом.")
        if amount > self._balance:
            raise ValueError(f"Недостаточно средств. Баланс: {self._balance:.2f}, запрошено: {amount:.2f}")
        self._balance -= float(amount)
        return self._balance

    def __repr__(self) -> str:
        return f"BankAccount(owner='{self.owner}', balance={self._balance:.2f})"

class Animal:
    """Базовый класс животного (Средняя № 5)."""

    def __init__(self, name: str, age: int) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Имя животного не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name: str = name
        self.age: int = int(age)

    def speak(self) -> str:
        """Базовый метод воспроизведения звука."""
        return f"{self.name} издает звук."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"


class Dog(Animal):
    """Класс собаки, наследующий класс животного (Средняя № 5)."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        if not breed or not isinstance(breed, str):
            raise ValueError("Порода собаки должна быть непустой строкой.")
        self.breed: str = breed

    def speak(self) -> str:
        """Переопределенный звук собаки."""
        return f"{self.name} говорит Гав!"

    def fetch(self, item: str) -> str:
        """Специфичное поведение собаки."""
        return f"{self.name} приносит {item}!"import os


class FileManager:
    """Класс для безопасной работы с текстовыми файлами (Средняя № 9)."""

    def __init__(self, filepath: str) -> None:
        if not filepath or not isinstance(filepath, str):
            raise ValueError("Путь к файлу должен быть непустой строкой.")
        self.filepath: str = filepath

    def write(self, content: str, mode: str = "w") -> None:
        """Запись или дозапись текста в файл."""
        if mode not in ("w", "a"):
            raise ValueError("Поддерживаются только режимы записи 'w' и дозаписи 'a'.")
        with open(self.filepath, mode=mode, encoding="utf-8") as file:
            file.write(content)

    def read(self) -> str:
        """Чтение содержимого файла."""
        if not self.exists():
            raise FileNotFoundError(f"Файл '{self.filepath}' не существует.")
        with open(self.filepath, mode="r", encoding="utf-8") as file:
            return file.read()

    def exists(self) -> bool:
        """Проверка существования файла."""
        return os.path.exists(self.filepath)

    def delete(self) -> bool:
        """Удаление файла при его наличии."""
        if self.exists():
            os.remove(self.filepath)
            return True
        return False

class Product:
    """Класс товара (Повышенная № 3)."""

    def __init__(self, name: str, price: float) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Название товара не может быть пустым.")
        if price < 0:
            raise ValueError("Цена товара не может быть отрицательной.")
        self.name: str = name
        self.price: float = float(price)

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price:.2f})"


class Cart:
    """Класс корзины заказов (Повышенная № 3)."""

    def __init__(self) -> None:
        self._items: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """Добавление товара в корзину."""
        if not isinstance(product, Product):
            raise TypeError("Товар должен быть объектом класса Product.")
        if quantity <= 0:
            raise ValueError("Количество товара должно быть больше 0.")
        self._items[product] = self._items.get(product, 0) + quantity

    def remove_product(self, product_name: str) -> None:
        """Удаление товара из корзины по наименованию."""
        target = next((item for item in self._items if item.name == product_name), None)
        if target is None:
            raise ValueError(f"Товар '{product_name}' отсутствует в корзине.")
        del self._items[target]

    def calculate_total(self) -> float:
        """Расчет суммарной стоимости товаров в корзине."""
        return sum(item.price * qty for item, qty in self._items.items())

    def get_items(self) -> list[tuple[Product, int]]:
        """Получение списка позиций корзины."""
        return list(self._items.items())

class Table:
    """Мини-ORM класс таблицы с методами insert и select (Повышенная № 7)."""

    def __init__(self, name: str, schema: list[str]) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Имя таблицы должно быть непустой строкой.")
        if not schema:
            raise ValueError("Схема таблицы должна содержать хотя бы одно поле.")
        self.name: str = name
        self.schema: list[str] = list(schema)
        self._records: list[dict[str, Any]] = []
        self._auto_id: int = 1

    def insert(self, record: dict[str, Any]) -> dict[str, Any]:
        """Вставка записи с проверкой соответствия схеме."""
        if not isinstance(record, dict):
            raise TypeError("Запись должна быть словарем.")
        for field in self.schema:
            if field not in record:
                raise ValueError(f"Отсутствует обязательное поле схемы: '{field}'.")
        row = {"id": self._auto_id, **record}
        self._auto_id += 1
        self._records.append(row)
        return row.copy()

    def select(self, predicate: Callable[[dict[str, Any]], bool] | None = None, **kwargs: Any) -> list[dict[str, Any]]:
        """Выборка записей по полям или кастомному предикату."""
        rows = self._records
        if kwargs:
            rows = [row for row in rows if all(row.get(k) == v for k, v in kwargs.items())]
        if predicate is not None:
            rows = [row for row in rows if predicate(row)]
        return [row.copy() for row in rows]

    def all(self) -> list[dict[str, Any]]:
        """Возвращает копию всех записей."""
        return [row.copy() for row in self._records]