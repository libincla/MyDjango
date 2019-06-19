from django.contrib import admin

from .models import *

# 修改 title 和 header
admin.site.site_title = 'MyDjango 后台管理'
admin.site.site_header = 'MyDjango'


# 将index定义的模型展示在Admin后台系统中

# 方法1：将模型直接注册到admin后台
# admin.site.register(Product)

# 方法2：自定义 ProductAdmin 类并继承 ModelAdmin
# 注册方法1：使用 Python 装饰器将 ProductAdmin 和模型 Product 绑定并注册到后台
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     # 设置显示的字段
#     list_display = ['id', 'name', 'weight', 'size', 'type']
# 注册方法2：
class ProductAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'weight', 'size', 'type']


admin.site.register(Product, ProductAdmin)
