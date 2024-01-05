## Описание
Выполняется парсинг данных со страницы с общей информацией о PEP (https://peps.python.org/), 
переход по ссылкам и сбор данных о каждом PEP.
Парсер подготавливает данные и сохраняет их в два файла формата ```csv``` в папку ```results```.

## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Ogyrecheg/scrapy_parser_pep.git
```

```bash
cd scrapy_parser_pep
```

Создать и активировать виртуальное окружение:

```bash
python -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Запустить парсер из командной строки:
```
scrapy crawl pep
```

Результаты работу парсера лежат в папке ``results``

**Технологии:**
- Python
- Scrapy

### Автор проекта:
[Шевченко Александр](https://github.com/Ogyrecheg)
