from django.db import models
class Cou(models.Model):
	course = models.CharField(max_length=100)

class Bran(models.Model):
    linkA=models.ForeignKey(Cou, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)

class Semes(models.Model):
    linkB=models.ForeignKey(Bran, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100)

class Sec(models.Model):
    linkC=models.ForeignKey(Semes, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)