
# Описание. 
Проект управления записями в БД через API.

Позволяет работать с моделями:
Post - публикации
Comment - комментарии
Group - группы пользователей
Follow - подписчики  

# Расширенная документация по API доступан после установки:

Документация к API проекта Yatube (v1)
./redoc/

# Установка. 

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/Alexander-Fedorovtsev/api_final_yatube.git
cd api_final_yatube

Cоздать и активировать виртуальное окружение:
python3 -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python3 manage.py migrate

Запустить проект:
python3 manage.py runserver

# Примеры.
Получение публикаций
Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией:
Запрос:
./api/v1/posts/
Ответ:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

