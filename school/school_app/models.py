from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class MaterialProvide(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    # material_provide = models.ManyToManyField(MaterialProvide)

    def __str__(self):
        return self.name
