from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    birthdate = models.DateField()
    nationality = models.CharField(max_length = 20)
    biography = models.CharField(max_length = 200)
    
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length = 200)
    publication_date = models.DateField()
    #publisher = 
    description = models.CharField(max_length = 150)
    quantity_available = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    contact = models.IntegerField(null=True, blank=True)
    #membership_id = models.IntegerField()
    #borrower_id = models.CharField(max_length = 10)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField()
    due_date = models.DateTimeField()
    returned_at = models.DateField(blank = True, null = True)
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.borrower_id.name} borrowed {self.book_id.title}"
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 150)
    
    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    contact = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class LibraryBranch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    contact = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    position = models.CharField(max_length = 20)
    contact = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name

class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length = 20)
    benefits = models.CharField(max_length = 150)
    fees = models.CharField(max_length = 10)
    duration = models.DateTimeField()
    
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    date_reserved = models.DateTimeField()
    expiry_id = models.DateTimeField()
    
class Fine(models.Model):
    id = models.AutoField(primary_key=True)
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reason = models.CharField(max_length = 100)
    date_imposed = models.DateTimeField()
    

    

   
