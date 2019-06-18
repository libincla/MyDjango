from django.db import models


# 创建产品分类表
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)


# 创建产品信息表
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


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
