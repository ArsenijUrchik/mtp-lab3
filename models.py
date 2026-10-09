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
        return f"{self.name} приносит {item}!"