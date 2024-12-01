from import_export import resources
from bookPage.models import BookInfo, Review, BookImage, Account, AccessCode


class BookInfoResource(resources.ModelResource):
    class Meta:
        model = BookInfo
        fields = ('id', 'title', 'intro', 'details', 'account_name', 'other')


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
        fields = ('id', 'user_id', 'book_id', 'content', 'date')


class BookImageResource(resources.ModelResource):
    class Meta:
        model = BookImage
        fields = ('id', 'book_id', 'image')


class AccountResource(resources.ModelResource):
    class Meta:
        model = Account
        fields = ('id', 'name', 'url')


class AccessCodeResource(resources.ModelResource):
    class Meta:
        model = AccessCode
        fields = ('id', 'book_id', 'name', 'link', 'secretId', 'secret', 'accessCode')
