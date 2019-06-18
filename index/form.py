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


class ProductModelForm(forms.ModelForm):
    # 添加模型外的表单字段
    productId = forms.CharField(max_length=20, label='产品序号')

    # 模型与表单设置
    class Meta:
        # 绑定模型
        model = Product
        # fields 属性用于设置转换字段，'__all__'是将全部模型字段转换成表单字段
        # fields = '__all__'
        fields = ['name', 'weight', 'size', 'type']
        # exclude 用于禁止模型字段转换表单字段
        exclude = []
        # labels 设置HTML元素控件的 label 标签
        labels = {
            'name': '产品名称',
            'weight': '重量',
            'size': '尺寸',
            'type': '产品类型'
        }
        # 定义widgets设置表单字段的CSS样式
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'cl'})
        }
        # 定义字段的类型，一般情况下模型的字段会自动转换成表单字段
        field_classes = {
            'name': forms.CharField
        }
        # 帮助提示信息
        help_texts = {
            'name': ''
        }
        # 自定义错误信息
        error_messages = {
            # __all__ 设置全部错误信息
            '__all__': {'required': '请输入内容', 'invalid': '请检查输入的内容'},
            # 设置某个字段的错误信息
            'weight': {'required': '请输入重量数值', 'invalid': '请检查数值是否正确'}
        }

    # 自定义表单字段 weight 的数据清洗
    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data + 'g'
