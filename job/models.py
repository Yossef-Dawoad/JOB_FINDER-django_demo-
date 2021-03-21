from django.db import models

# Create your models here.




'''
why django field in django
    -html widgets
    -validations
    -db size handler
'''

JOB_TYPE = (
    ('FullTime','FullTime'),
    ('PartTime','PartTime'),
)


class Job(models.Model): # table in db

    title = models.CharField(max_length=100) # Columns in db
    jobtype = models.CharField(max_length=15,choices=JOB_TYPE)
    descriptions = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)    
    Salary = models.IntegerField(default=0)    
    Experience = models.IntegerField(default=1)    

    def __str__(self):
        return self.title


