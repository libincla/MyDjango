from django import template

# 声明一个模板对象，也称为注册过滤器
register = template.Library()


# 声明并定义过滤器
@register.filter
def myreplace(value, args):
    oldValue = args.split('：')[0]  # 注意冒号的中英文格式，须与模板中的冒号保持一致
    newValue = args.split('：')[1]  # 注意冒号的中英文格式，须与模板中的冒号保持一致
    return value.replace(oldValue, newValue)
