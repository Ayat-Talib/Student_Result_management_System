from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    class_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField(default=100)

    class Meta:
        unique_together = ['student', 'subject']

    def percentage(self):
        return (self.marks_obtained / self.total_marks) * 100

    def grade(self):
        per = self.percentage()
        if per >= 90: return 'A+'
        elif per >= 80: return 'A'
        elif per >= 70: return 'B'
        elif per >= 60: return 'C'
        else: return 'F'