from django import forms
from .models import *


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='名字')
    weight = forms.CharField(max_length=50, label='重量')
    size = forms.CharField(max_length=50, label='尺寸')
    # 设置下拉框
    choices_list = [(i + 1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(choices=choices_list, label='产品类型')
