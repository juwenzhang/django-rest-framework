# 返回信息通用模板，由于设计初期的不规范，实际上的话是可以分文件存储的，但是这里就不做处理了
# 开发中如果需要进行处理分模块定义，也是可以的哈

LOGIN_REQUEST_ERROR_MSG: dict = {
    "status": False,
    "mag": "用户名或者密码缺失"
}

LOGIN_USERNAME_ERROR_MSG: dict = {
    "status": False,
    "msg": "用户不存在"
}

LOGIN_USER_ERROR_MSG: dict = {
    "status": False,
    "msg": "密码错误",
    "redirect": "/register"
}

LOGIN_DATABASE_ERROR_MSG: dict = {
    "status": False,
    "code": 500,
    "msg": "服务器内部出错"
}

# =================================================
REGISTER_USERNAME_ERROR_MSG: dict = {
    "status": False,
    "msg": "用户名已经存在"
}

REGISTER_EMAIL_ERROR_MSG: dict = {
    "status": False,
    "msg": "邮箱已经存在"
}

REGISTER_MOBILE_ERROR_MSG: dict = {
    "status": False,
    "msg": "电话号码重复注册"
}

REGISTER_DATABASE_ERROR_MSG: dict = {
    "code": 500,
    "status": False,
    "msg": "服务器内部错误"
}

REGISTER_SUCCESS_MSG: dict = {
    "status": True,
    "msg": "注册成功",
    "redirect": "/login"
}

# ==================================================
VIEW_NOT_TOKEN_ERROR_MSG: dict = {
    "status": False,
    "msg": "视图未提供 token"
}

VIEW_NOT_COOKIE_ERROR_MSG: dict = {
    "status": False,
    "msg": "未通过 cookie 校验"
}

VIEW_NOT_PERMISSION_MSG: dict = {
    "status": False,
    "msg": "当前用户无权限"
}

# ===================================================
AUTHENTICATION_USER_NOT_PASS_ERROR_MSG: dict = {
    "status": False,
    "message": "用户不存在失败"
}

AUTHENTICATION_DATABASE_ERROR_MSG: dict = {
    "status": False,
    "message": "500 服务端故障"
}

AUTHENTICATION_ALL_NOT_PASS_MSG: dict = {
    "status": False,
    "message": "认证失败"
}

# ==================================================
PERMISSION_NOT_PASS_MSG: dict = {
    "status": False,
    "msg": "该用户没有权限访问~~~~"
}

# ==================================================
