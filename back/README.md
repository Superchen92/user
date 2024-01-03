# 安装
## 创建虚拟环境
``` sh
py -3 -m venv .venv
```
## 激活虚拟环境
``` sh
.venv\Scripts\activate
```
## 安装依赖
``` sh
#安装flask
pip install Flask

#安装 sqlalcheny
pip install sqlalcheny

#安装 cors
pip install flask_cors

#安装mysql
pip install pymysql
```



# 运行

## 激活虚拟环境
``` sh
.venv\Scripts\activate
```

## 运行程序
``` sh
flask --app main run --debug
```