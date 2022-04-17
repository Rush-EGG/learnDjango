from django.db import models

# Create your models here.

# 对数据进行操作

"""
下面这个类定义会让django通过orm去操作MySQL
类名就代指了数据库中的表名
字段名其实就是表中的列名
相当于create table app01_userinfo(
    id bigint auto_increment primary key, # 这一行是自动添加的
    name varchar(32),
    password varchar(64),
    age int
)
"""


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # age = models.IntegerField()
    size = models.IntegerField()
    # 可能在添加新的一个列名时，表中已经存在数据
    # 为了保证已有数据所在行的新增列上有相关数据，可以括号中加入"default = ？"来添加默认值
    # 为所有行的新增列都加上这个字段
    age = models.IntegerField(default=2)
    # 当然也可以允许某一个列名所带的值为空
    data = models.IntegerField(null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=16)

# class Role(models.Model):
#     caption = models.CharField(max_length=16)


# 添加数据
# Department.objects.create(title="销售部")
# UserInfo.objects.create(name="tt", password="123", size=5, age=23)
