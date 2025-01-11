### python django django-rest-framework

**`pip install virtualenvwrapper-win` | `pip install virtualenvwrapper`**

**`mkvirtualenv env_name`**

**`workon env_name`**

**`pip install -r requirement.txt`**

**`python manage.py runserver`**

**`python manage.py startapp application_name`**

**`python manage.py makemigrations`**

**`python manage.py migrate`**


* 由于 python 作为服务的效率是十分低的，所以说这个时候我们就可以使用一下 python 后续提出的一些改进
* 从 wsgi 服务 转变到了 asgi 服务
  * asgi 服务器含有： uvicorn | daphne
  * 同时我们还可以实现创建异步视图： asyncio django>=3.1