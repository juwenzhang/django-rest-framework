### python django django-rest-framework-demo

**`pip install virtualenvwrapper-win` | `pip install virtualenvwrapper`**

**`mkvirtualenv env_name`**

**`workon env_name`**

**`pip install -r requirement.txt`**

**`python manage.py runserver`**

**`python manage.py startapp application_name`**

**`python manage.py makemigrations`**

**`python manage.py migrate`**


### asgi 和 wsgi 
* 由于 python 作为服务的效率是十分低的，所以说这个时候我们就可以使用一下 python 后续提出的一些改进
* 从 wsgi 服务 转变到了 asgi 服务
  * asgi 服务器含有： uvicorn | daphne
  * 同时我们还可以实现创建异步视图： asyncio django>=3.1


### 技术栈使用
* jwt 认证
* redis
* mysql
* docker
* linux
* nginx
* jenkins
* centos-stream
* djangorestframework


### 使用中间件
* authentication token认证限制
  * 提供了从请求头 | 请求体 | 查询参数 校验token的机制
* permission 权限认证
  * 该功能有待完善，当前还是使用的是服务器随机生成随机数来间接性的给用户权限
* throttle 限流认证
  * 提供了用户名限流和IP地址限流两大模式
* serializer 序列化处理
  * 对于返回数据使用其进行了一定的序列化操作 json 数据
* version 限制
  * 对于请求版本的限制，只有服务器允许的版本才可以进行访问接口
  * 服务端默认的是 web 请求版本，所以说各位请求数据的时候可以不用携带版本号了
* mysql | redis
  * mysql 存储数据
  * redis 存储限流的键值对: ip限流键值对 | user限流键值对


### 接口可使用
* 首先先启动服务器： **`python manage.py runserver`**
* http://localhost:8000/api/login/
  * 登录接口
  * 登录接口含有限流登录
    * ip 限流 - 触发后限流1h
    * user 限流 - 触发后限流 300s
* http://localhost:8000/api/register/
  * 注册用户接口
  * ip 限流
* http://localhost:8000/api/order/
  * developer
* http://localhost:8000/api/user/
  * developer
* http://localhost:8000/api/default/version/id/
  * demo-api interface
* http://localhost:8000/api/detail/
  * 返回的是所有用户信息