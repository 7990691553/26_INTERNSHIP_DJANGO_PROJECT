from django.db import models

# Create your models here.
# python class

# parent class MOdel
# create table student(studentName,varchar(100),studentAge int,studentCity varchar(40));
# it will generate primary key column student_id automatically
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)
    
    #meta class
    class Meta:
        db_table = "student"  #table name

    def __str__(self):
        return self.studentName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=30,null=True)
    productStatus = models.BooleanField(default=True)   
    
    class Meta:
        db_table = "product"
       
class StudentProfile(models.Model):
    hobbies = (("reading","reading"),("travel","travel"),("music","music"))
    studentID = models.OneToOneField(Student, on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentID.studentName

#cat --> #service

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName 