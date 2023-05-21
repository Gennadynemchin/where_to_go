# Where to go
The web site about interesting places in your city


![app_screen.jpeg](./app_screen.jpeg)

## Demo version on Pythonanywhere
Avaliable here: [WhereToGo](https://genapoliss.pythonanywhere.com/)

## How to run

- It's strongly recommended to use virtual enviroment for deploy. You should use Python 3.10 and Django 4 (see requirements.txt)
- Clone the repo:
```bash
git clone https://github.com/Gennadynemchin/where_to_go.git
```

- Install all requested requirements:
```bash
pip install -r requirements.txt
```

## Env vars
Some of app settings placed in enviroment variables. For use them rename the `example.env` to `.env`
then fill out the file like this: `VARIABLE=value`.

Available variables:
- `SECRET_KEY` — Secret key of your project;
- `DEBUG_STATUS` — Debug mode;
- `ALLOWED_HOSTS` — Please follow to the link for additional information: [Django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts).
- `SESSION_COOKIE_SECURE` — Please follow to the link for additional information: [Django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#session-cookie-secure)
- `CSRF_COOKIE_SECURE` — Please follow to the link for additional information: [Django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-secure)
- `SECURE_SSL_REDIRECT` — Please follow to the link for additional information: [Django docs](https://django-secure.readthedocs.io/en/v0.1.1/settings.html#secure-ssl-redirect)

- Then make migrations:
```bash
python manage.py migrate
```
- Run server:
```bash
python manage.py runserver
```

## How to load places
Use custom command (replace PLACE_URL to requested .json file):
```commandline
python manage.py load_place PLACE_URL
```
The .json must looks like the example:

```commandline
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```