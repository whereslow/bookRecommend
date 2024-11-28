from django.shortcuts import render, redirect
from .models import BookInfo, BookImage, Review, Account, AccessCode
from django.core.cache import cache
import socket
import struct
from django.contrib import messages
import random


# Create your views here.
def bookPage(request, book_id):
    book = BookInfo.objects.get(id=book_id)
    account_name = book.account_name
    account = Account.objects.get(name=account_name)
    images = BookImage.objects.filter(book_id=book_id)
    image_urls = [image.image for image in images]
    comments = Review.objects.filter(book_id=book_id)
    access_code = AccessCode.objects.get(book_id=book_id)
    access = request.GET.get("access")
    return render(request, "BookPage.html", {
        "title": book.title,
        "detail": book.details,
        "image_urls": image_urls,
        "comments": comments,
        "book_id": book_id,
        "account_url": account.url,
        "account_title": account.name,
        "link": access_code.link,
        "access": access
    })


def index(request):
    books = list(BookInfo.objects.all())
    # 随机选取最多6本书籍
    random_books = random.sample(books, min(len(books), 6))
    return render(request, 'index.html', {'books': random_books})


def submitComment(request, book_id):
    def ip_to_int(from_ip):
        # 将 IP 地址转换为二进制形式
        packed_ip = socket.inet_aton(from_ip)
        # 使用 struct.unpack 解包为整数
        return struct.unpack("!I", packed_ip)[0]

    if request.method == "POST":
        ip = request.META["REMOTE_ADDR"]
        if cache.get(ip) is not None:
            messages.warning(request, "您最近已经评论过了，请稍后评论!")
            return redirect(f"/book/{book_id}")
        content = request.POST.get("comment")
        sig = ip_to_int(ip)
        Review.objects.create(user_id=sig, book_id=book_id, content=content)
        cache.set(ip, 1, 600)
        return redirect(f"/book/{book_id}")


def accessBookCode(request, book_id):
    if request.method == "POST":
        secret = request.POST.get("secret")
        access_code = AccessCode.objects.get(book_id=book_id)
        if access_code.secret != secret:
            # 提示访问码错误
            messages.warning(request, "访问码错误")
            return redirect(f"/book/{book_id}#webdisk")
            pass
        else:
            # 弹出访问码
            messages.success(request, f"获取成功,访问码为{access_code.accessCode}")
            return redirect(f"/book/{book_id}?access={access_code.accessCode}#webdisk")
