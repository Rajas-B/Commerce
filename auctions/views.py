from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User
import datetime
import django.utils.timezone as tz
from .models import *

def index(request):
    productlist = Product.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "products" : productlist
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'auctions/login.html', {
                "message": "Invalid credentails"
            })
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def prof(request, username):
    if request.user.is_authenticated:
        productlist = Product.objects.filter(uid=request.user)
        bids = Bids.objects.filter(user_id=request.user)
        return render(request, "auctions/user.html",{
            "products": productlist, "bids": bids
        })
    else:
        return HttpResponseRedirect(reverse("index"))

def category(request):
    return render(request, "auctions/category.html")

def categoryprods(request, category):
    productlist = Product.objects.filter(category=category)
    return render(request, "auctions/categoryprods.html",{
        "products":productlist
    })
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            prodname = request.POST["prodname"]
            category1 = request.POST["prodcatg"]
            description = request.POST["proddesc"]
            image = request.POST["prodimg"]
            baseprice = request.POST["baseprice"]
            product1 = Product(uid=request.user, name=prodname, category=category1, description=description, image=image, baseprice=baseprice, date=tz.localtime(), active = True)
            product1.save()
            return HttpResponseRedirect(reverse('prof', args=(request.user.get_username(), )))
        return render(request, "auctions/create.html")
    else:
        return HttpResponseRedirect(reverse("index"))

def prod1(request, id):
    prod = Product.objects.get(id=id)
    bidders = Bids.objects.filter(prod_id=prod)
    try:
        my_bid = Bids.objects.get(prod_id=prod, user_id=request.user)
    except:
        my_bid=None
    try:
        watchlist = Watchlist.objects.get(user_id=request.user, product_id=prod)
    except:
        watchlist = None
    highest_bidder = bidders.order_by('amount').last()
    comments = Comments.objects.filter(product_id=prod)
    message1 = ""
    message2 = ""
    message3 = ""
    if request.method == "POST":
        if 'place_bid' in request.POST:
            try:
                new_bid = Bids(user_id=request.user, prod_id=prod, amount = request.POST["bid_amount"])
                new_bid.save()
                prod.baseprice = request.POST["bid_amount"]
                prod.save()
                return HttpResponseRedirect(reverse("prod1", args=(id, )))
            except:
                message1 = "Couldn't place bid"
        if 'increase_bid' in request.POST:
            try:
                my_bid.amount=request.POST["increased_bid"]
                my_bid.save()
                prod.baseprice = request.POST["increased_bid"]
                prod.save()
                return HttpResponseRedirect(reverse("prod1", args=(id, )))
            except:
                message1 = "Could not place bid"
        if 'post_comment' in request.POST:
            try:
                new_comment = Comments(user_id=request.user, product_id = prod, comment = request.POST["prod_comment"])
                new_comment.save()
                return HttpResponseRedirect(reverse("prod1", args=(id, )))
            except:
                message2 = "Could not post comment"
        if 'add_to_watch' in request.POST:
            try:
                watchlist1 = Watchlist(user_id=request.user, product_id=prod)
                watchlist1.save()
                return HttpResponseRedirect(reverse("prod1", args=(id, )))
            except:
                message3 = "Something went wrong"
        if 'remove_from_watch' in request.POST:
            try:
                watchlist.delete()
                return HttpResponseRedirect(reverse("prod1", args=(id, )))
            except:
                message3 = "Something went wrong"
        if 'close_bid' in request.POST:
            try:
                prod.active = False
                prod.save()
            except:
                pass
    return render(request, "auctions/prod.html",{
        "product": prod, "bidders": bidders, "highest_bidder": highest_bidder, "comments": comments,
        "message1": message1, "message2": message2, "message3": message3, "my_bid": my_bid, "watchlist": watchlist
    })

def watchlist(request):
    if request.user.is_authenticated:
        user_watchlist = Watchlist.objects.filter(user_id=request.user)
        return render(request, "auctions/watchlist.html", {
            "user_watchlist": user_watchlist
        })
    else:
        return HttpResponseRedirect(reverse('index'))
