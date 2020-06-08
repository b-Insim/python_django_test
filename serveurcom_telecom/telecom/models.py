from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=200, unique=True) # blank=True, null=True, default='SOME STRING') #, unique=True)
    ref = models.CharField(max_length=200, blank=True, null=True)#,  unique=True)
    description = models.CharField(max_length=200, unique=True)
    
    class Meta:
        ordering = ["-name"]
        abstract = True

class Reference(CommonInfo):

    def __str__(self):
         return self.name

class Contact(CommonInfo):
    email = models.EmailField(max_length=100)
    table = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Comptoir(CommonInfo):
    position = models.CharField(max_length=10)
    table = models.IntegerField(null=False)
    reference = models.ManyToManyField(Reference, related_name='reference', blank=True)
    
    def __str__(self):
        return self.position

class Reservation(CommonInfo):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

class Stock(CommonInfo):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    stock = models.IntegerField(null=False)

    def __str__(self):
        return self.stock

class Menu(CommonInfo):
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name







# class Reference(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     ref = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     #available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
    
# class Contact(models.Model):
#     email = models.EmailField(max_length=100)
#     name = models.CharField(max_length=200)
#     table = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Comptoir(models.Model):
#     position = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200)
#     table = models.IntegerField(null=False)
#     description = models.CharField(max_length=200)
#     reference = models.ManyToManyField(Reference, related_name='reference', blank=True)
    
#     def __str__(self):
#         return self.position

# class Reservation(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     contacted = models.BooleanField(default=False)
#     ref = models.CharField(max_length=200, unique=True)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.contact.name


# class Stock(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     contacted = models.BooleanField(default=False)
#     ref = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     stock = models.IntegerField(null=False)

#     def __str__(self):
#         return self.stock

# class Menu(models.Model):
#     ref = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.available





# class Reference(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     ref = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Contact(models.Model):
#     email = models.EmailField(max_length=100)
#     name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     table = models.IntegerField(null=False)

# class Menu(models.Model):
#     ref = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=30, unique=True)
#     description = models.CharField(max_length=200)
#     available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.available

# class Bars(models.Model):
#     comptoir = models.CharField(max_length=20)
#     name = models.CharField(max_length=30)
#     table = models.IntegerField(null=False)
#     description = models.CharField(max_length=200)
#     reference = models.ManyToManyField(Reference, related_name='reference', blank=True)
    
#     def __str__(self):
#         return self.comptoir

# class Stock(models.Model):
#     ref = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     stock = models.IntegerField(null=False)

#     def __str__(self):
#         return self.stock
    
# class Commande(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     contacted = models.BooleanField(default=False)
#     name = models.CharField(max_length=200, unique=True)
#     ref = models.CharField(max_length=200, unique=True)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.contact.name

# class Comptoir(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     bars = models.IntegerField(null=False)
#     reference = models.ManyToManyField(Reference, related_name='reference', blank=True)
    
#     def __str__(self):
#         return self.position