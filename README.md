# QA_Python_2025_fall

### С чего начать?

1. Сначала нужно скопировать проект себе на компьютер.
Используете HTTPS (самый простой способ)

- копировать ссылку `https://github.com/RedRoverSchool/JenkinsQA_Python_2025_fall.git`
- в PyCharm кликнуть на File -> Project from Version Control
- в открывшемся окне выбрать директорию, где будет находиться проект
- в поле URL вставить скопированную ссылку
- нажать Clone

    Если используете терминал:
- создаете новый проект
- в терминале вводите git clone <скопированная ссылка>

2. Создание виртуального окружения 

    Через настройка PyCharm
- в PyCharm кликнуть на File -> Settings -> Python -> Interpreter -> Add Interpreter -> Add local Interpreter
- выбираем версию питона, жмем на ОК
- открываем терминал, если перед строкой не стоит (venv), то нужно активировать окружение
- Если у вас Windows, то в терминале вводим команду `venv\Scripts\activate` либо `.venv\Scripts\activate`
- Если у вас Linux/Mac, то в терминале вводим команду `source venv/bin/activate` либо `source .venv/bin/activate`

    Если используете терминал:
- Если у вас Windows, то в терминале вводим команду `python -m venv venv`, после команду `venv\Scripts\activate`
- Если у вас Linux/Mac, то в терминале вводим команду `python3 -m venv venv`, после команду `source venv/bin/activate`

    Если у вас перед строкой стоит (venv), то виртуальное окружение активировано

3. Обновить pip
- python.exe -m pip install --upgrade pip

4. Установить все библиотеки из requirements.txt
- pip install -r requirements.txt

