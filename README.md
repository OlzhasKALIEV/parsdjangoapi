# parsdjangoapi

Парсер сервиса https://opendata.mkrf.ru/opendata на Python, который сохранит данные из
таблицы https://opendata.mkrf.ru/opendata/7705851331-patriot_music в базу данных.

HTTP метод всех запросов: GET, POST, PUT DELETE
Формат ответов: JSON

GET: http://127.0.0.1:8000/api/v1/patriotic-music/ запрос возвращает информацию Каталога патриотической музыки(скрин)

![img.png](media/img.png)

POST: http://127.0.0.1:8000/api/v1/patriotic-music/ добавление информации в Каталога патриотической музыки(скрин)

формат добавления JSON
{
    "fullname": "",
    "composer": "",
    "genre": "",
    "theme": "",
    "creationyear": ""
}
![img_1.png](media/img_1.png)

GET: http://127.0.0.1:8000/api/v1/patriotic-music?id=1  запрос возвращает информацию Каталога патриотической музыки по
ID(скрин)

![img_2.png](media/img_2.png)

