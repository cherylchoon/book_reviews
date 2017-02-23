from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReviewManager(models.Manager):
    def create_review(self, obj, userid):
        book_title = obj['title']
        book_author = obj['author']
        book_review = obj['review']
        book_rating = obj['rating']
        user = User.objects.get(id=userid)
        try:
            book = Book.objects.get(title=book_title, author=book_author)
        except:
            book = Book.objects.create(title=book_title, author=book_author)
        create_review = Review.objects.create(user=user, book=book, review=book_review, rating=book_rating)
        return {'book_id': book.id}

class Review(models.Model):
    user = models.ForeignKey(User, related_name='user_reviews')
    book = models.ForeignKey(Book, related_name='book_reviews')
    review = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()
