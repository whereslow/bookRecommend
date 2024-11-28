from django.contrib import admin
from import_export.admin import ImportExportMixin
from bookPage.models import BookInfo, Review, BookImage, Account, AccessCode
from .resource import BookInfoResource, ReviewResource, BookImageResource, AccountResource, AccessCodeResource


# BookInfo Admin配置，启用导入和导出功能
@admin.register(BookInfo)
class BookInfoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = BookInfoResource
    list_display = ('title', 'intro', 'account_name')  # 可根据需求自定义显示字段


# Review Admin配置，启用导入和导出功能
@admin.register(Review)
class ReviewAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ReviewResource
    list_display = ('user_id', 'book_id', 'content', 'date')  # 可根据需求自定义显示字段


# BookImage Admin配置，启用导入和导出功能
@admin.register(BookImage)
class BookImageAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = BookImageResource
    list_display = ('book_id', 'image')  # 可根据需求自定义显示字段


# Account Admin配置，启用导入和导出功能
@admin.register(Account)
class AccountAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AccountResource
    list_display = ('name', 'url')  # 可根据需求自定义显示字段


# AccessCode Admin配置，启用导入和导出功能
@admin.register(AccessCode)
class AccessCodeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AccessCodeResource
    list_display = ('book_id', 'name', 'link', 'secretId')  # 可根据需求自定义显示字段
