# INDEX 设置中文，代码编写在 App 的 __init__.py文件中
from django.apps import AppConfig
import os

# 修改App在Admin后台显示的名称
# default_app_config 的值来自 apps.py 的类名
default_app_config = 'index.IndexConfig'


# 获取当前App的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


# 重写类 IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'
