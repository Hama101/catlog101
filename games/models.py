from django.db import models as m

# Create your models here.


class Games(m.Model):
    choices = [("ps3", 'ps3'),
               ("ps4", 'ps4'),
               ("pc", 'pc'),
               ("Xbox", 'Xbox'),
               ]
    title = m.CharField(max_length=50)
    console = m.CharField(max_length=5, choices=choices, default="pc")
    category = m.CharField(max_length=50)
    price = m.IntegerField()
    os = m.CharField(max_length=50)
    cpu = m.CharField(max_length=50)
    gpu = m.CharField(max_length=50)
    ram = m.CharField(max_length=50)
    hdd = m.CharField(max_length=50)
    shortDescription = m.CharField(max_length=255, null=True)
    longDescription = m.CharField(max_length=2088, null=True)
    coverImg = m.CharField(max_length=2083, null=True)
    img1Url = m.CharField(max_length=2083, null=True)
    img2Url = m.CharField(max_length=2083, null=True)
    img3Url = m.CharField(max_length=2083, null=True)
    youtubeUrl = m.CharField(max_length=2083, null=True)

    def __str__(self):
        return self.title
