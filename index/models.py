from django.db import models
from django.utils.html import format_html


# 创建产品分类表
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    # 设置返回值，若不设置，则默认返回Type对象。可使下拉框显示字段 type_name
    def __str__(self):
        return self.type_name


# 创建产品信息表
# 设置字段中文名，用于Admin后台显示
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='产品名称')
    weight = models.CharField(max_length=20, verbose_name='重量')
    size = models.CharField(max_length=20, verbose_name='尺寸')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='产品类型')

    # 设置返回值
    def __str__(self):
        return self.name

    class Meta:
        # 如果只设置 verbose_name，在 Admin 会显示为 "产品信息 s"
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'
        # 自定义权限
        permissions = (('visit_Product', 'Can visit Product'),)

    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html('<span style="color:{};">{}</span>', color_code, self.type)

    # 设置 colored_type 在 Admin 中的标题
    colored_type.short_description = '带颜色的产品类型'


# 一对一关系的表1
class PerformerOne(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)


# 一对一关系的表2
class Perforer_info(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.OneToOneField(PerformerOne, on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)


# 一对多关系的表1
class PerformerTwo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)


# 一对多关系的表2
class ProgramOne(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.ForeignKey(PerformerTwo, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


# 多对多关系的表1
class PerformerThree(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)


# 多对多关系的表2
class ProgramTwo(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.ManyToManyField(PerformerThree)
    name = models.CharField(max_length=20)


# 省份信息
class Province(models.Model):
    name = models.CharField(max_length=10)


# 城市信息
class City(models.Model):
    name = models.CharField(max_length=5)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)


# 人物信息表
class Person(models.Model):
    name = models.CharField(max_length=10)
    living = models.ForeignKey(City, on_delete=models.CASCADE)
