
from string_utils import StringUtils


utils = StringUtils()  # Создаем экземпляр класса
# ================== Тесты для метода capitalize ==================


def test_capitalize_pozitive():
    """Проверяем, что метод корректно делает первую букву заглавной"""
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"


def test_capitalize_negative():
    """Проверяем обработку краевых случаев: пустая строка, строка из цифр"""
    assert utils.capitalize("") == ""  # Пустая строка
    assert utils.capitalize("123") == "123"  # Строка с цифрами
    assert utils.capitalize(" ") == " "  # Строка с пробелом


# ================== Тесты для метода trim ==================
def test_trim_positive():
    """Проверяем, что метод удаляет пробелы в начале строки"""
    assert utils.trim("    skypro") == "skypro"
    assert utils.trim("  hello  ") == "hello  "  # Пробелы в конце сохраняются


def test_trim_negative():
    """Проверяем строки без пробелов в начале и пустую строку"""
    assert utils.trim("skypro") == "skypro"  # Без пробелов в начале
    assert utils.trim("") == ""


# ================== Тесты для метода contains ==================
def test_contains_positive():
    """Проверяем, что метод правильно находит искомый символ"""
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "k") is True


def test_contains_negative():
    """Проверяем, что метод возвращает False, если символ не найден"""
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False  # Пустая строка


# ================== Тесты для метода delete_symbol ==================
def test_delete_symbol_positive():
    """Проверяем удаление одного символа и подстроки"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_negative():
    """Проверяем, что если символа нет, строка не меняется"""
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert utils.delete_symbol("", "a") == ""  # Пустая строка
