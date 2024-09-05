from django.db import models

# Create your models here.
class shop_tbl(models.Model):
    fn=models.CharField(max_length=30)
    mb=models.IntegerField()
    em=models.EmailField()
    ps=models.CharField(max_length=30)
    cps=models.CharField(max_length=30)
    pincode=models.IntegerField()
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    house=models.CharField(max_length=50)
    road=models.CharField(max_length=50)
    def __str__(self):
        return self.fn
class product_tbl(models.Model):
    im=models.FileField(upload_to='images')
    cg=models.CharField(max_length=50)
    br=models.CharField(max_length=50)
    nm=models.CharField(max_length=100)
    pr=models.IntegerField()
    of=models.CharField(max_length=200)
    opr=models.IntegerField()
    def __str__(self):
        return self.nm
class cart_tbl(models.Model):
    customer=models.ForeignKey(shop_tbl,on_delete=models.CASCADE)
    product=models.ForeignKey(product_tbl,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.product
class wishlist_tbl(models.Model):
    customer=models.ForeignKey(shop_tbl,on_delete=models.CASCADE)
    product=models.ForeignKey(product_tbl,on_delete=models.CASCADE)
    def __str__(self):
        return self.product
class address_tbl(models.Model):
    name=models.CharField(max_length=30)
    mob=models.IntegerField()
    amb=models.IntegerField()
    pin=models.IntegerField()
    st=models.CharField(max_length=30)
    cty=models.CharField(max_length=30)
    hs=models.CharField(max_length=50)
    rd=models.CharField(max_length=50)
    def __str__(self):
        return self.name
STATUS_CHOICE = (
("pending", "Pending"),
("processing", "Processing"),
("Shipped", "Shipped"),
("delivered", "delivered"),
("Cancelled", "Cancelled"),
)
class order_tbl(models.Model):
    nm=models.CharField(max_length=30)
    mob=models.IntegerField()
    pin=models.IntegerField()
    stat=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    hous=models.CharField(max_length=50)
    road=models.CharField(max_length=50)
    totalprice=models.DecimalField(max_digits=20,decimal_places=2)
    orderstatus=models.CharField(choices=STATUS_CHOICE,default='Pending',max_length=30)
    def __str__(self):
        return self.nm
    

    
