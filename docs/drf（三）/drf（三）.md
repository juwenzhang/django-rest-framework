# drf（三）

## 后端接口版本的兼容设计

### 在查询参数中实现携带版本信息

**from rest_framework.versioning import QueryParameterVersioning**

* 从表观的呈现效果就是： 在客户端的请求参数中携带 **version** 字段，然后后端的 **request** 中就具备了 **.version** 属性
  * 在视图函数中配置静态属性： **versioning_class = QueryParameterVersioning**
  * **request.version** 实现获取客户端请求的版本号信息
  * 同时内部还具备我们的 **request.version_scheme** 获取生成反向 url 的对象
* 该字段默认的是 version，但是我们是可以通过全局文件的配置实现来修改获取版本号的字段信息的
  * **"VERSION_PARAM": "version"**

* 同时还可以在我们的 url，请求头中设置我们的版本信息的

> * 在我们的实际开发中，对于版本信息的传递的话就是实现的是
>   * 通过 get 请求的参数实现获取
>   * 通过 url 路径进行传递
>   * 请求体/请求头传递版本号信息
>   * 服务器反向生成 url 信息
> * drf 的源码还是十分清晰的，有其他的需要可以直接进行使用即可



## drf 解析器

* 在我们实现解析器的时候，我们使用的可以是： **parser_classes + content_negotiation_class**
  * 前者是我们的所有的解析器
  * 后者就是我们的根据请求头来实现匹配解析器的规则定义
* 源码的中实现解析的流程的话需要注意一下我们的 json 工具的使用
* 四种解析器：
  * **JsonParser**
    * **json.loads(对象)**  实现的是将我们的 json 数据转化为 python 中的数据的
    * **json.load(json文件对象)** 实现的是将我们的 json 文件对象进行解析的，然后获取得到最终数据的流程
      * 在前后端传输数据的时候，我们最后获取得到的数据实质上是一个 json 的内存对象，在传输过程中，我们使用的是
      * 二进制的格式实现的传输，所以说在源码中的解析就是通过的是我们的 **json.load()** 实现的解析
  * **FormParser**
    * **formdata** 数据格式的上传
  * **FileUploadParser**
    * 实现的是我们的文件上传的功能，纯文件类型的上传
  * **MultipartParser**
    * 就是实现的是我们的即上传文件又解析数据用的解析器类型



## drf 元类

* 类和对象

  * 我们通过对一个类的实例化就可以获得我们的对象

  * 通过对象可以实现调用类中的方法以及获取得到类中的成员属性

    * 成员的话分为我们的类成员和静态成员

  * ```python
    class foo:
        def func():
            print("我是第一种创建类的方式")
    ```

  * ```python
    type("foo", (object,), {"v1":111, "func": lambda self:123})
    # 第二种创建类的方法，这个就是元类的定义方式 type("类名", (父类,), {成员属性 + 成员方法})
    ```



## drf 序列化器

* 序列化就是实现的是我们的从数据库获取得到的数据转化为 json 数据进行传递的
* **from rest_framework import serializers**