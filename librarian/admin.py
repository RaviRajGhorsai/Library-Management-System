from django.contrib import admin
from .models import Author,Book,Borrower,LibraryBranch,Transaction,Category,Publisher,Employee,Membership,Reservation,Fine

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(LibraryBranch)
admin.site.register(Employee)
admin.site.register(Membership)
admin.site.register(Reservation)
admin.site.register(Fine)
