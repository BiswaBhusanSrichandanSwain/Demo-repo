class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField(max_length=30)
    