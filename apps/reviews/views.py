from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..login.models import User
from .models import Book, Review
from .forms import BookForm, ReviewForm

def login_register(request):
    return redirect(reverse('users:user_index'))

def index(request):
    context = {
        'recent_reviews': Review.objects.order_by('-created_at')[:3],
        'book_reviews': Review.objects.all()
    }
    return render(request, 'reviews/index.html', context)

def add_review(request):
    context = {
        'bookForm': BookForm(),
        'reviewForm': ReviewForm()
    }
    return render(request, 'reviews/add_review.html', context)

def create_review(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        result = Review.objects.create_review(request.POST, user_id)
        book_id = result['book_id']
        return redirect(reverse('reviews:book_info', kwargs={'id':book_id}))

def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST['delete']
        book_id = request.POST['bookid']
        Review.objects.filter(id=review_id).delete()
        return redirect(reverse('reviews:book_info', kwargs={'id':book_id}))

def book_info(request, id):
    context = {
        'book_info': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id).order_by('-created_at'),
        'reviewForm': ReviewForm(),
    }
    return render(request, 'reviews/bookinfo.html', context)

def user_info(request, id):
    context = {
        'user_info': User.objects.get(id=id),
        'books': Review.objects.filter(user=id)
    }
    return render(request, 'reviews/userinfo.html', context)
