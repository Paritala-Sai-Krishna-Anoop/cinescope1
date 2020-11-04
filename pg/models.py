from django.db import models
expertise =(
    ("", ""),
    ("acting teacher", "acting teacher"),
    ("video editing", "video editing"),
    ("audio editing", "audio editing"),
    ("direction", "direction"),
    ("acting", "acting"),
    ("musician", "musician"),
    ("theator acting", "theator acting"),
    ("vfx", "vfx"),
    ("technician", "technician"),
    ("others", "others"),
)
audiequip =(
    ("portable field mixer", "portable field mixer"),
    ("field recorder", "field recorder"),
    ("Wireless microphone systems", "Wireless microphone systems"),
    ("shotgun microphones", "shotgun microphones"),
    ("Wind protection for the mics", "Wind protection for the mics"),
    ("boompole", "boompole"),
    ("Headphones", "Headphones"),
)
videosoft=(
    ("", ""),
    ("film editing software", "film editing software"),
    ("composting tool", "composting tool"),
    ("3d tool", "3d tool"),
    ("color grading tool", "color grading tool"),
    ("rendering tool", "rendering tool"),
)


class mainman(models.Model):
    name = models.CharField(max_length=30 , default='')
    email = models.EmailField(blank=True,default='')
    area_of_expertees = models.CharField(max_length=100,default='', choices=expertise)
    tell_us_about_yourself = models.TextField(default='',blank=True, null=True)
    date = models.DateField(blank=True, null=True,auto_now=True)
    def __str__(self):
        return self.name


class camera(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField( max_digits=10, decimal_places=0,default='')
    subject = models.TextField(blank=True,null=True, default="")
    def __str__(self):
        return self.name


class audio(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    subject = models.TextField(blank=True,null=True, default="")
    type = models.CharField(max_length=100, default='new', choices=audiequip)
    def __str__(self):
        return self.name

class audioe(models.Model):
    softwarename = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    def __str__(self):
        return self.softwarename

class videoe(models.Model):
    softwarename = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    softwaretype = models.CharField(max_length=100, default='new', choices=videosoft)

    def __str__(self):
        return self.softwarename

class join(models.Model):
    email = models.EmailField(blank=True, default='')

    def __str__(self):
        return self.email