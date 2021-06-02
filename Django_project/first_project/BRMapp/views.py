from django.shortcuts import render
import BRMapp.models as mod
from BRMapp.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


##GET & post = dictionary

@login_required(login_url="BRMapp/userlogin")
def fun_add_new_book(request):  # Add book
    obj_form = New_book_form()
    data = {"obj_form": obj_form}
    res = render(request, "BRMapp/new_book.html", data)
    return res


@login_required(login_url="BRMapp/userlogin")
def fun_add(request):  # save:
    if request.method == "POST":  # both edit & new recoed
        form = New_book_form(request.POST)
        obj_book = mod.Book()

        if "book_id" in request.POST:  # for editing #it won't make new record
            obj_book.id = request.POST['book_id']

        obj_book.title = form.data["title"]
        obj_book.price = form.data["price"]
        obj_book.pbr = form.data["pbr"]
        obj_book.author = form.data["author"]
        obj_book.dpt = form.data["dpt"]
        obj_book.save()
        res = render(request, "BRMapp/message.html", {"message": "stored"})
        return res


@login_required(login_url="BRMapp/userlogin")
def fun_EditBook(request):
    book = mod.Book.objects.get(id=request.GET["bookid"])
    fields = {"title": book.title, "price": book.price, "dpt": book.dpt, "author": book.author, "pbr": book.pbr}
    form = New_book_form(initial=fields)
    res = render(request, "BRMapp/edit.html", {"form": form, "book": book})
    return res


@login_required(login_url="BRMapp/userlogin")
def fun_delete_book(request):
    book = mod.Book.objects.get(id=request.GET["bookid"])
    book.delete()
    res = render(request, "BRMapp/message.html", {"message": "deleted"})
    return res


@login_required(login_url="BRMapp/userlogin")
def fun_view_books(request):
    username = request.session["username"]  # session is a dictionary
    books = mod.Book.objects.all()
    res = render(request, "BRMapp/view.html", {"books": books, "username": username})
    return (res)


@login_required(login_url="BRMapp/userlogin")
def fun_SearchBook(request):
    res = render(request, "BRMapp/searchbase.html")
    return (res)


@login_required(login_url="BRMapp/userlogin")
def fun_basesearch(request):
    if request.method == "POST":
        ans = request.POST["searchbase"]
        if ans == "title":
            obj_form = Search_form_T()
        elif ans == "dpt":
            obj_form = Search_form_D()
        elif ans == "pbr":
            obj_form = Search_form_P()
        elif ans == "author":
            obj_form = Search_form_A()

        data = {'obj_form': obj_form, "search_by": ans}
        res = render(request, "BRMapp/search.html", data)
        return res


@login_required(login_url="BRMapp/userlogin")
def fun_find(request):
    if request.method == "POST":
        searchby = request.POST['searchby']  # searchby= title or dpt or pbr or author

        if searchby == "title":
            obj_form = Search_form_T(request.POST)
            books = mod.Book.objects.filter(title=obj_form.data["title"])
        elif searchby == "dpt":
            obj_form = Search_form_D(request.POST)
            books = mod.Book.objects.filter(dpt=obj_form.data["dpt"])
        elif searchby == "pbr":
            obj_form = Search_form_P(request.POST)
            books = mod.Book.objects.filter(pbr=obj_form.data["pbr"])
        elif searchby == "author":
            obj_form = Search_form_A(request.POST)
            books = mod.Book.objects.filter(author=obj_form.data["author"])

        data = {'books': books, 'obj_form': obj_form}
        res = render(request, 'BRMapp/search.html', data)
        return res


def fun_userlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        userpassword = request.POST["userpassword"]
        user = authenticate(request, username=username, password=userpassword)
        if user is not None:
            login(request, user)
            request.session[
                "username"] = username.capitalize()  # session variable remain till logout and can be used in any function.
            return HttpResponseRedirect("BRMapp/view_books")  # it is a dictionary.
        else:
            data = {"error": "username or userpassword is incorrect"}
            res = render(request, "BRMapp/user_login.html", data)
            return res
    else:
        res = render(request, "BRMapp/user_login.html")
        return res


def fun_userlogout(request):
    logout(request)
    return HttpResponseRedirect("BRMapp/userlogin")


