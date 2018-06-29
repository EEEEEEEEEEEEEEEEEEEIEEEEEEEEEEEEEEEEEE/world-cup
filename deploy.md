# 部署文档

1. 获取源码并安装依赖
```bash
$ git clone xxx
# 建议使用 virtualenv 虚拟环境
$ cd world_cpu
$ pip install -r requirements
```

2. 初始化数据库
```bash
$ python controller.py
```

3. 境服务器建议使用 gunicorn
```bash
$ gunicorn -w 4 -b 127.0.0.1:4000 api:app
# 项目将会在 4000 端口启动
```

4. nginx 参考 flask 官方给出的示例
```
server {
    listen 80;

    server_name _;

    access_log  /var/log/nginx/access.log;
    error_log  /var/log/nginx/error.log;

    location / {
        proxy_pass         http://127.0.0.1:8000/;
        proxy_redirect     off;

        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```

5. 喝杯咖啡
