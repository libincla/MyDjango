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
    # 设置可搜索的字段，并在Admin后台数据生成搜索框，如有外键，应使用双下划线连接两个模型的字段
    search_fields = ['id', 'name', 'type__type_name']
    # 设置过滤器，在后台数据的右侧生成导航栏，如有外键，应使用双下划线连接两个模型的字段
    list_filter = ['name', 'type__type_name']
    # 设置排序方式，【'id']为生序，['-id']为降序
    ordering = ['id']
    # 设置时间选择器，如果字段中有时间格式才可以使用
    # date_hierarchy = Field
    # 在添加新数据时，设置可添加数据的字段
    fields = ['name', 'weight', 'size', 'type']

    # 设置可读字段，在修改或新增数据时使其无法设置
    # readonly_fields = ['name']

    # 重写 get_readonly_fields 函数，设置超级用户和普通用户的权限
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['name']
        return self.readonly_fields

    # 添加自定义字段
    list_display.append('colored_type')

    # 重写 get_queryset 函数，根据不同用户角色设置数据的访问权限
    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=6)


admin.site.register(Product, ProductAdmin)
