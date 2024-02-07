from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Author,Book,Borrower,LibraryBranch,Transaction,Category,Publisher,Employee,Membership,Reservation,Fine,UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import BorrowBookForm,BookSearchForm
from django.http import HttpResponseBadRequest

# Create your views here.

def index(request):
    return render(request, 'auth/login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/dashboard/')  # Redirect superusers to the dashboard
                else:
                    return redirect('/dashboard/')  # Redirect regular users to their dashboard
        else:
            # Invalid login credentials
            return render(request, 'auth/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('/dashboard/')  # Redirect superusers to the dashboard
            else:
                return redirect('/dashboard/')  # Redirect regular users to their dashboard
        else:
            form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})
        
def dashboard(request):
    if request.user.is_authenticated == True:
        books = Book.objects.all()
        return render(request, 'dashboard/index.html', {'books': books})
    else:
        return redirect('/login/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ucontact = request.POST.get('contact')
        uaddress = request.POST.get('address')
        
        
        user = User.objects.create_user(username=username,email=email,password=password,last_name=lname,first_name=username)
        user.save()
        
        useR = User.objects.get(username=username)
        id = useR.id
        borrower = Borrower.objects.create(name=username,contact=ucontact,email=email,address=uaddress, user_id=id)
        
        borrower.save()
        return redirect('/login/')
    return render(request, 'registration/register.html')

@login_required
def borrow_book(request):
    if request.method == "POST":
        req_book_id = int(request.POST.get('book_id'))
        req_borrower_id = int(request.POST.get('borrower_id'))
        req_borrowed_at = request.POST.get('borrowed_at')
        req_due_date = request.POST.get('due_date')

        book = Book.objects.get(id=req_book_id)
        if book.quantity_available>0:
            book.quantity_available -= 1
            book.save()
        
        #logged-in user
        
        borrower, created = Borrower.objects.get_or_create(user=request.user)
        

        borrow = Transaction.objects.create(
        book_id=book,
        borrower_id = borrower,
        date_borrowed = req_borrowed_at,
        due_date = req_due_date,
        )

        borrow.save();

        if borrow:
            return redirect('/dashboard/borrow/')
        else:
            return render(request,'/dashboard/borrow/index.html',{'error':'Error Something went wrong '})
    else:    
        if request.user.is_authenticated:
            borrower = request.user
            
            books = Book.objects.all();
            transactions = Transaction.objects.filter(borrower_id__user=request.user);
            return render(request, 'dashboard/borrow/index.html',{'borrowers':borrower,'books':books,'transactions':transactions})
        else:
            return redirect('/login/')
@login_required       
def delete_borrow(request,id):
    if request.user.is_authenticated:
        borrow = Transaction.objects.get(id=id)
        borrow.delete()
        return redirect('/dashboard/borrow/')
    else:
        return redirect('/login')
    
@login_required  
def edit_borrow(request, id):
    if request.method == "POST":
        req_book_id = request.POST.get('book_id')
        req_borrower_id = request.POST.get('borrower_id')
        req_borrowed_at = request.POST.get('borrowed_at')
        req_returned_at = request.POST.get('returned_at')
        req_due_date = request.POST.get('due_date')

        # Ensure req_book_id and req_borrower_id are valid integers
        if req_book_id is None or req_borrower_id is None:
            return HttpResponseBadRequest("Invalid request: book_id and borrower_id are required")

        try:
            book = Book.objects.get(id=req_book_id)
            borrower, created = Borrower.objects.get_or_create(user=request.user)
            if req_returned_at:
                is_returned_value = True
                book.quantity_available += 1
                book.save()

            borrow = Transaction.objects.get(id=id)
            borrow.book_id = book
            borrow.borrower_id = borrower
            if req_returned_at:
                borrow.returned_at = req_returned_at
                borrow.is_returned = is_returned_value

            borrow.save()
            return redirect('/dashboard/borrow/')
        except (Book.DoesNotExist, Borrower.DoesNotExist, Transaction.DoesNotExist) as e:
            return HttpResponseBadRequest("Invalid request: {}".format(str(e)))
    else:    
        if request.user.is_authenticated:
            try:
                transactions = Transaction.objects.get(id=id, borrower_id__user=request.user)
                borrowers = Borrower.objects.filter(user=request.user)
                books = Book.objects.all()
                return render(request, 'dashboard/borrow/edit.html', {'borrowers': borrowers, 'books': books, 'transactions': transactions})
            except Transaction.DoesNotExist:
                return HttpResponseBadRequest("Transaction does not exist or does not belong to the current user")
        else:
            return redirect('/login/')


@login_required        
def view_borrowed(request):
    if request.method == 'GET':
        user = request.user
        borrowed_books = Transaction.objects.filter(is_returned=False,borrower_id__user=user).select_related('book_id')
        return render(request, 'dashboard/borrow/viewBorrow.html', {'borrowed_books': borrowed_books})
    
def search_books(request):
    
    
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        filtered_books = []
        if form.is_valid():
            
            book_name = form.cleaned_data.get('book')
            genre = form.cleaned_data.get('genre')
            author = form.cleaned_data.get('author')
            
            
            # Apply search filter
            if book_name:
                filtered_books = Book.objects.filter(title__icontains=book_name)
            
            # Apply genre filter
            if genre:
                filtered_books = Book.objects.filter(genre__icontains=genre)
                
            # Apply author filter
            if author:
                filtered_books = Book.objects.filter(author__name__icontains=author)
            
            
           
    else:
        form = BookSearchForm()
    
    return render(request, 'dashboard/search/search.html', {'form': form, 'filtered_books': filtered_books})