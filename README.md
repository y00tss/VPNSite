
<br>

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-4.2-blue.svg)](https://docs.djangoproject.com/en/4.2/releases/4.2/)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-13-green.svg)](https://www.postgresql.org/docs/13/release-13-2.html)
[![Flake8](https://img.shields.io/badge/Flake8-Check%20Code-yellow.svg)](https://flake8.pycqa.org/)
[![Beautiful Soup Version](https://img.shields.io/badge/beautifulsoup4-4.12.2-orange.svg)](https://pypi.org/project/beautifulsoup4/)


## Running the Project Locally

1. Open you terminal and put the command:
```bash
git clone https://github.com/y00tss/VPNSite
```
2. Open Docker Desktop on your Windows

3. Back to your terminal and put the command:
```bash
cd VPNSite
```
4. Next step is creating the conteiner by following command:
```bash
docker-compose build
```
6. After we need to create a superuser. Follow the guide inside (username and passwordx2) or you can follow next step if you don`t want to visit Django Admin:
```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
7. Start the server:
```bash
docker-compose up
```
# Note:
If you received the same issues:

<img alt="issue" src="https://i.ibb.co/syNFhqD/s.jpg">

Perform the actions below:
1. ctrl + c
2. perform docker-compose up command again

There is applied migrations and runserver that looks like on the screenshot
<img alt="issue" src="https://i.ibb.co/QmHXj8T/s.jpg">

8. Open the link:
<a href="http://127.0.0.1:8000/" target="_blank">WebApp</a>

# Settings
1. Database local, default PORT = 5432 , keep this port free before Running App
