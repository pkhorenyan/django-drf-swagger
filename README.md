REST API приложение для каталога исполнителей, альбомов и песен, построенный на Django Rest Framework.

## Используeмые технологии

- **Django** — веб-фреймворк
- **Django Rest Framework** — создание REST API
- **drf-yasg** - генерация OpenAPI/Swagger документации
- **PostgreSQL** — база данных
- **Docker** — контейнеризация

## Запуск с использованием Docker Compose

1. Убедитесь, что Docker и Docker Compose установлены.
2. Клонируйте репозиторий:
```bash
git clone https://github.com/pkhorenyan/django-drf-swagger.git
``` 
3. Выполните:
```bash
cd music_catalog
docker-compose up --build
```
4. Приложение доступно на http://127.0.0.1:8000

## API Документация

После запуска сервера доступна Swagger документация:
- **Swagger UI**: http://127.0.0.1:8000/swagger/
- **ReDoc**: http://127.0.0.1:8000/redoc/
- **OpenAPI JSON Schema**: http://127.0.0.1:8000/swagger.json

## Тестирование API

Проверить работу эндпоинтов можно с помощью Postman, либо вручную через curl.

### Тестирование с Postman

Импортируйте OpenAPI схему в Postman:
   - Откройте Postman
   - Нажмите "Import"
   - Выберите "Link" и вставьте: `http://127.0.0.1:8000/swagger.json`
   - Или скачайте JSON файл по этому URL и импортируйте как файл


### Ручное тестирование с curl

#### Создание исполнителя

```bash
curl -X POST http://127.0.0.1:8000/api/artists/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "The Beatles"
  }'
```

#### Создание альбомов

```bash
curl -X POST http://127.0.0.1:8000/api/albums/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Abbey Road",
    "year": 1969,
    "artist": "The Beatles"
  }'
```
```bash
curl -X POST http://127.0.0.1:8000/api/albums/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Let It Be",
    "year": 1970,
    "artist": "The Beatles"
  }'
```
#### Создание песни

```bash
curl -X POST http://127.0.0.1:8000/api/songs/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Come Together",
  }'
```
#### Добавление песни в два разных альбома

```bash
curl -X POST http://127.0.0.1:8000/api/album-songs/ \
  -H "Content-Type: application/json" \
  -d '{
    "album": "Let it Be",
    "song": "Come Together",
    "track_number": 12
  }'
```
```bash
curl -X POST http://127.0.0.1:8000/api/album-songs/ \
  -H "Content-Type: application/json" \
  -d '{
    "album": "Abbey Road",
    "song": "Come Together",
    "track_number": 3
  }'
```
