school_bus_system/
├── manage.py             # Django管理脚本
├── school_bus/           # 项目主目录
│   ├── __init__.py
│   ├── asgi.py           # ASGI配置（用于WebSocket）
│   ├── settings.py       # 项目设置
│   ├── urls.py           # 主URL路由
│   └── wsgi.py           # WSGI配置
└── bus_system/           # 应用目录
    ├── migrations/       # 数据库迁移文件
    ├── management/       # 自定义管理命令
    │   └── commands/
    │       └── init_data.py  # 初始化数据命令
    ├── templates/        # 模板文件
    │   └── bus_system/
    │       ├── base.html
    │       ├── realtime_monitor.html
    │       └── statistics.html
    ├── __init__.py
    ├── admin.py          # 后台管理配置
    ├── apps.py           # 应用配置
    ├── models.py         # 数据模型
    ├── tests.py          # 测试用例
    ├── urls.py           # 应用URL路由
    └── views.py          # 视图函数
