from django.db import models

class Student(models.Model):
    # 순번이 순차적으로증가  AutoField 
    no = models.AutoField(primary_key=True)# 오라클sequence와같은기능
    name = models.CharField(max_length=100)# varchar2 
    major = models.CharField(max_length=100)# varchar2 
    # 숫자타입 Integer 
    grade = models.IntegerField(default=0)# number
    age = models.IntegerField(default=0) # number
    gender = models.CharField(max_length=30,blank=True) #추가 - 100개 
    hobby = models.CharField(max_length=100,blank=True) 
    sdate = models.DateTimeField(auto_now=True) # date객체 -sysdate와같은기능
    memo = models.TextField(blank=True) #빈공간도 가능 clob과같은기능
    
    #관리자페이지
    def __str__(self):
       return f"{self.no},{self.name},{self.sdate}"
