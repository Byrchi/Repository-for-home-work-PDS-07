class HashTable:

    def __init__(self):
        """Ініціалізує хеш-таблицю з початковим розміром та створює порожній список для елементів таблиці. """
        capacity = self._get_prime(10)
        self.size = capacity
        self.table = [[] for _ in range(capacity)]
        self.elementCount = 0

    def _check_prime(self, n):
        """Приватний допоміжний метод для перевірки, чи число є простим."""
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _get_prime(self, n):
        """Приватний допоміжний метод для пошуку наступного простого числа після n."""
        if n % 2 == 0:
            n += 1
        while not self._check_prime(n):
            n += 2
        return n

    def _hash_function(self, key):
        """Приватний метод для обчислення хеш-значення заданого ключа."""
        return key % self.size

    def insert_data(self, key, data):
        """Вставляє пару ключ-значення в хеш-таблицю з використанням лінійного пробігання для вирішення колізій."""
        index = self._hash_function(key)
        if not self.table[index]:
            self.table[index] = [key, data]
            print("Елемент " + str([key, data]) + " на позиції " + str(index))
            self.elementCount += 1
            return True
        else:
            print("Сталася колізія для елементу " + str([key, data]) + " на позиції " + str(index) + ". Знаходжу нову позицію.")
            for _ in range(1, self.size):
                index = (index + 1) % self.size
                if not self.table[index]:
                    self.table[index] = [key, data]
                    self.elementCount += 1
                    return True
            print("Не вдалося вставити елемент " + str([key, data]) + ". Таблиця заповнена.")
            return False

    def search(self, key):
        """Шукає ключ в хеш-таблиці і повертає його асоційоване значення, якщо знайдено."""
        position = self._hash_function(key)
        for _ in range(1, self.size + 1):
            if self.table[position] and self.table[position][0] == key:
                return self.table[position][1]

        print("Елемент не знайдено")
        return False

    def remove_data(self, key):
        """Видаляє пару ключ-значення з хеш-таблиці за заданим ключем."""
        index = self._hash_function(key)
        self.table[index] = []

    def isFull(self):
        """Перевіряє, чи хеш-таблиця повна."""
        return self.elementCount == self.size

    def display(self):
        """ Виводить вміст хеш-таблиці."""
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("Кількість елементів у таблиці: " + str(self.elementCount))


# Приклад використання:
hashtable = HashTable()
hashtable.insert_data(1, 'Audi')
hashtable.insert_data(2, 'Volvo')
hashtable.insert_data(3, 'Fiat')
hashtable.insert_data(25, 'Mercedes')
hashtable.insert_data(4, 'Mercedes')

hashtable.search(5)
result = hashtable.search(2)
print(result)
hashtable.remove_data(1)
hashtable.display()
