from django import forms
from .models import *
from django.core.exceptions import ValidationError


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    # 设置错误信息并设置样式
    name = forms.CharField(max_length=20, label='名字',
                           widget=forms.widgets.TextInput(attrs={'class': 'cl'}), error_messages={'required': '名字不能为空'})
    # 使用自定义数据验证函数
    weight = forms.CharField(max_length=50, label='重量', validators=[weight_validate])
    size = forms.CharField(max_length=50, label='尺寸')
    # 通过数据库数据设置下拉框
    choices_list = [(i + 1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    # 设置 CSS 样式
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'type', 'size': '1'}), choices=choices_list, label='产品类型')
