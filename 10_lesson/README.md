# Lesson 10 — PageObject + Allure

Автотесты на Selenium + Pytest + Allure с использованием паттерна Page Object.

## Структура проекта

```
10_lesson/
├── pages/                  # Page Object классы
│   ├── calculator_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Тесты с Allure-разметкой
│   ├── conftest.py         # Общие фикстуры (Chrome, Firefox)
│   ├── test_calculator.py
│   └── test_sauce_demo.py
└── README.md
```

## Требования

- Python 3.8+
- Java 8+ (для Allure CLI)
- Chrome / Firefox + соответствующие драйверы

## Установка

### 1. Python-зависимости

```bash
pip install pytest selenium allure-pytest
```

### 2. Allure CLI (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install -y default-jre wget
wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz
tar -zxvf allure-2.30.0.tgz
sudo mv allure-2.30.0 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
allure --version
```

## Запуск тестов с формированием результатов

Из корня репозитория:

```bash
pytest 10_lesson/tests --alluredir=10_lesson/allure-results
```

Запуск конкретного файла:

```bash
pytest 10_lesson/tests/test_sauce_demo.py --alluredir=10_lesson/allure-results
```

Запуск по severity:

```bash
pytest 10_lesson/tests --allure-severities=critical
```

## Просмотр отчёта

### Вариант 1 — живой сервер (открывается браузер автоматически)

```bash
allure serve 10_lesson/allure-results
```

### Вариант 2 — статичный HTML-отчёт

```bash
allure generate 10_lesson/allure-results -o 10_lesson/allure-report --clean
allure open 10_lesson/allure-report
```

## Разметка Allure в проекте

- `@allure.feature` — группировка тестов по функциональности
- `@allure.severity` — важность теста (critical / normal / minor …)
- `@allure.title` — читаемое название теста
- `@allure.description` — подробное описание
- `with allure.step(...)` — шаги внутри теста
- `@allure.step` — шаги внутри Page Object методов (опционально)
- 