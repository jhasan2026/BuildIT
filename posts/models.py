from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    post_pic1 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic1/')
    post_pic2 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic2/')
    post_pic3 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic3/')
    post_pic4 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic4/')
    post_pic5 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic5/')
    post_pic6 = models.FileField(default='empty.jpg',null=True,blank=True,upload_to='post-pic6/')
    address = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)
    use_for = models.IntegerField(default=0)
    map = models.CharField(max_length=400, default='')
    MSZoning = models.CharField(max_length=50, default='')
    LotFrontage = models.IntegerField(default=0)
    LotArea = models.IntegerField(default=0)
    BldgType = models.CharField(max_length=50, default='')
    OverallQual = models.CharField(max_length=50, default='')
    OverallCond = models.CharField(max_length=50, default='')
    YearBuilt = models.IntegerField(default=0)
    RoofStyle = models.CharField(max_length=50, default='')
    RoofMatl = models.CharField(max_length=50, default='')
    Exterior1st = models.CharField(max_length=50, default='')
    Exterior2nd = models.CharField(max_length=50, default='')
    ExterQual = models.CharField(max_length=50, default='')
    ExterCond = models.CharField(max_length=50, default='')
    Foundation = models.CharField(max_length=50, default='')
    BsmtQual = models.CharField(max_length=50, default='')
    BsmtCond = models.CharField(max_length=50, default='')
    TotalBsmtSF = models.IntegerField(default=0)
    CentralAir = models.CharField(max_length=50, default='')
    FirstFlrSF = models.IntegerField(default=0)
    SecondFlrSF = models.IntegerField(default=0)
    GrLivArea = models.IntegerField(default=0)
    KitchenQual = models.CharField(max_length=50, default='')
    TotRmsAbvGrd = models.IntegerField(default=0)
    GarageType = models.CharField(max_length=50, default='')
    GarageCars = models.IntegerField(default=0)
    GarageArea = models.IntegerField(default=0)
    GarageQual = models.CharField(max_length=50, default='')
    GarageCond = models.CharField(max_length=50, default='')
    PoolArea = models.IntegerField(default=0)
    MiscVal = models.IntegerField(default=0)

    SaleType = models.CharField(max_length=50,default='')
    SaleCondition = models.CharField(max_length=50, default='')


    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self,*args,**kwargs):
        super(Post,self).save(*args,*kwargs)
        img1 = Image.open(self.post_pic1.path)
        if img1.height > 300 or img1.width > 300 :
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.post_pic1.path)

        img2 = Image.open(self.post_pic2.path)
        if img2.height > 300 or img2.width > 300 :
            output_size = (300,300)
            img2.thumbnail(output_size)
            img2.save(self.post_pic2.path)

        img3 = Image.open(self.post_pic3.path)
        if img3.height > 300 or img3.width > 300 :
            output_size = (300,300)
            img3.thumbnail(output_size)
            img3.save(self.post_pic3.path)

        img4 = Image.open(self.post_pic4.path)
        if img4.height > 300 or img4.width > 300 :
            output_size = (300,300)
            img4.thumbnail(output_size)
            img4.save(self.post_pic4.path)

        img5 = Image.open(self.post_pic5.path)
        if img5.height > 300 or img5.width > 300 :
            output_size = (300,300)
            img5.thumbnail(output_size)
            img5.save(self.post_pic5.path)

        img6 = Image.open(self.post_pic6.path)
        if img6.height > 300 or img6.width > 300 :
            output_size = (300,300)
            img6.thumbnail(output_size)
            img6.save(self.post_pic6.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # rating from 1 to 5
    title = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - Rating: {self.rating}"