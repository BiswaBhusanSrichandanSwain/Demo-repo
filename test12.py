class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=30)
    