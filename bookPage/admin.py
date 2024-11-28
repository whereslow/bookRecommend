from django.contrib import admin

from bookPage.models import BookInfo, Review, BookImage, Account, AccessCode


# Register your models here.
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessCode)
class AccessCodeAdmin(admin.ModelAdmin):
    pass
