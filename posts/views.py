from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ReviewForm, PostSearchForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from django import template
from .models import Review
from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt



import numpy as np
import pandas as pd
import joblib
model = joblib.load('price_Model/price_predictions')
preprocess = joblib.load('price_Model/preprocessor')
PCA = joblib.load('price_Model/PCA')


def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'posts/posts.html',context)


def Notifications(request):
    postsNotifications = Post.objects.all()
    return render(request, 'posts/base.html', {'postsNotifications': postsNotifications})




# class AllUsersView(TemplateView):
#     template_name = 'posts/chat_sidenav.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = User.objects.all()  # Pass all users to the template
#         return context

register = template.Library()
@register.inclusion_tag('posts/chat_sidenav.html')
def showAllUser():
    users = User.objects.all()  # Get all users
    return {'users': users}

def rentPosts(request):
    context = {
        'posts': Post.objects.filter(use_for=1)
    }
    return render(request,'posts/rent_posts.html',context)



class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        # Get only posts with use_for = 0
        return Post.objects.filter(use_for=0).order_by('-date_posted')


class RentPostListView(ListView):
    model = Post
    template_name = 'posts/rent_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        # Get only posts with use_for = 1
        return Post.objects.filter(use_for=1).order_by('-date_posted')

class MortgagePostListView(ListView):
    model = Post
    template_name = 'posts/morgage_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        # Get only posts with use_for = 2
        return Post.objects.filter(use_for=2).order_by('-date_posted')


class MortgageCardView(DetailView):
    model = Post
    template_name = 'posts/mortgage_card.html'
    context_object_name = 'mortgage_post'

class RentCardView(DetailView):
    model = Post
    template_name = 'posts/rent_card.html'
    context_object_name = 'rent_post'


class MyPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/my_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'posts/user_posts.html'    # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 3
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-date_posted')

class PostPayView(DetailView):
    model = Post
    template_name = 'posts/payment.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post.html'    # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']



def custom_login_required(additional_constraint):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if additional_constraint(request.user):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You don't have permission to access this section.")
        return _wrapped_view
    return decorator

def has_special_permission(user):
    return user.first_name == 'B' # Example constraint


@csrf_exempt
@custom_login_required(has_special_permission)
def PostCreateView(request):
    if request.method == "POST":
        use_for = int(request.POST.get('use_for'))
        price = int(request.POST.get('price'))
        address = str(request.POST.get('address'))

        post_pic1 = request.FILES.get('post_pic1')
        post_pic2 = request.FILES.get('post_pic2')
        post_pic3 = request.FILES.get('post_pic3')
        post_pic4 = request.FILES.get('post_pic4')
        post_pic5 = request.FILES.get('post_pic5')
        post_pic6 = request.FILES.get('post_pic6')


        MSZoning = str(request.POST.get('MSZoning'))
        LotFrontage = int(request.POST.get('LotFrontage'))
        LotArea = int(request.POST.get('LotArea'))


        BldgType = str(request.POST.get('BldgType'))
        OverallQual = str(request.POST.get('OverallQual'))
        OverallCond = str(request.POST.get('OverallCond'))
        YearBuilt = int(request.POST.get('YearBuilt'))
        Foundation = str(request.POST.get('Foundation'))
        BsmtCond = str(request.POST.get('BsmtCond'))
        TotalBsmtSF = int(request.POST.get('TotalBsmtSF'))


        FirstFlrSF = int(request.POST.get('FirstFlrSF'))

        SecondFlrSF = int(request.POST.get('SecondFlrSF'))


        GrLivArea = int(request.POST.get('GrLivArea'))


        KitchenQual = str(request.POST.get('KitchenQual'))
        TotRmsAbvGrd = int(request.POST.get('TotRmsAbvGrd'))


        GarageType = str(request.POST.get('GarageType'))

        GarageCars = int(request.POST.get('GarageCars'))

        GarageArea = int(request.POST.get('GarageArea'))


        GarageQual = str(request.POST.get('GarageQual'))
        GarageCond = str(request.POST.get('GarageCond'))
        MiscVal = int(request.POST.get('MiscVal'))
        Exterior1st = str(request.POST.get("Exterior1st"))
        Exterior2nd = str(request.POST.get("Exterior2nd"))


        PoolArea = int(request.POST.get('PoolArea'))


        SaleType = str(request.POST.get('SaleType'))
        SaleCondition = str(request.POST.get('SaleConditionRoofStyle'))
        RoofStyle = str(request.POST.get('RoofStyle'))
        RoofMatl = str(request.POST.get('RoofMatl'))
        ExterQual = str(request.POST.get('ExterQual'))
        ExterCond = str(request.POST.get('ExterCond'))
        BsmtQual = str(request.POST.get('BsmtQual'))
        CentralAir = str(request.POST.get('CentralAir'))

        newData = [MSZoning, LotFrontage, LotArea, BldgType, OverallQual, OverallCond, YearBuilt, RoofStyle, RoofMatl, ExterQual, ExterQual, ExterCond, Foundation, BsmtQual, BsmtCond, TotalBsmtSF, CentralAir, FirstFlrSF, SecondFlrSF, GrLivArea, KitchenQual, TotRmsAbvGrd, GarageType, GarageCars, GarageArea, GarageQual, GarageCond, PoolArea, MiscVal, SaleType, SaleCondition]

        print(newData)
        post = Post.objects.create(
            MSZoning=MSZoning,
            LotFrontage=LotFrontage,
            LotArea=LotArea,
            BldgType=BldgType,
            OverallQual=OverallQual,
            OverallCond=OverallCond,
            YearBuilt=YearBuilt,
            RoofStyle=RoofStyle,
            RoofMatl=RoofMatl,
            ExterQual=ExterQual,
            ExterCond=ExterCond,
            Foundation=Foundation,
            BsmtQual=BsmtQual,
            BsmtCond=BsmtCond,
            TotalBsmtSF=TotalBsmtSF,
            CentralAir=CentralAir,
            FirstFlrSF=FirstFlrSF,
            SecondFlrSF=SecondFlrSF,
            GrLivArea=GrLivArea,
            KitchenQual=KitchenQual,
            TotRmsAbvGrd=TotRmsAbvGrd,
            GarageType=GarageType,
            GarageCars=GarageCars,
            GarageArea=GarageArea,
            GarageQual=GarageQual,
            GarageCond=GarageCond,
            PoolArea=PoolArea,
            MiscVal=MiscVal,
            SaleType=SaleType,
            SaleCondition=SaleCondition,
            author = request.user,
            use_for=use_for,
            price=price,
            address=address,
            post_pic1=post_pic1,
            post_pic2=post_pic2,
            post_pic3=post_pic3,
            post_pic4=post_pic4,
            post_pic5=post_pic5,
            post_pic6=post_pic6,
            Exterior1st=Exterior1st,
            Exterior2nd=Exterior2nd,
            map=map,
        )
        if post is not None:
            return redirect('posts-home')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request,'posts/create_post.html')


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'posts/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'posts/about.html')

def prediction(request):
    if request.method == "POST":
        MSZoning = str(request.POST.get('MSZoning'))
        LotFrontage = int(request.POST.get('LotFrontage'))
        LotArea = int(request.POST.get('LotArea'))
        BldgType = str(request.POST.get('BldgType'))
        OverallQual = str(request.POST.get('OverallQual'))
        OverallCond = str(request.POST.get('OverallCond'))
        YearBuilt = int(request.POST.get('YearBuilt'))
        Foundation = str(request.POST.get('Foundation'))
        BsmtCond = str(request.POST.get('BsmtCond'))
        TotalBsmtSF = int(request.POST.get('TotalBsmtSF'))

        FirstFlrSF = int(request.POST.get('FirstFlrSF'))

        SecondFlrSF = int(request.POST.get('SecondFlrSF'))


        GrLivArea = int(request.POST.get('GrLivArea'))


        KitchenQual = str(request.POST.get('KitchenQual'))
        TotRmsAbvGrd = int(request.POST.get('TotRmsAbvGrd'))


        GarageType = str(request.POST.get('GarageType'))

        GarageCars = int(request.POST.get('GarageCars'))


        GarageArea =int(request.POST.get('GarageArea'))


        GarageQual = str(request.POST.get('GarageQual'))
        GarageCond = str(request.POST.get('GarageCond'))
        MiscVal = int(request.POST.get('MiscVal'))


        PoolArea = int(request.POST.get('PoolArea'))


        SaleType = str(request.POST.get('SaleType'))
        SaleCondition = str(request.POST.get('SaleCondition'))
        RoofStyle = str(request.POST.get('RoofStyle'))
        RoofMatl = str(request.POST.get('RoofMatl'))

        Exterior1st = str(request.POST.get('Exterior1st'))
        Exterior2nd = str(request.POST.get('Exterior2nd'))

        ExterQual = str(request.POST.get('ExterQual'))
        ExterCond = str(request.POST.get('ExterCond'))
        BsmtQual = str(request.POST.get('BsmtQual'))
        CentralAir = str(request.POST.get('CentralAir'))

        newData = [MSZoning,LotFrontage,LotArea,BldgType,OverallQual,OverallCond, YearBuilt,RoofStyle,RoofMatl,Exterior1st,Exterior2nd,ExterQual,ExterCond,Foundation,BsmtQual,BsmtCond,TotalBsmtSF,CentralAir,FirstFlrSF,SecondFlrSF,GrLivArea,KitchenQual,TotRmsAbvGrd,GarageType,GarageCars,GarageArea,GarageQual,GarageCond,PoolArea,MiscVal,SaleType,SaleCondition]

        column_names = ['MSZoning', 'LotFrontage', 'LotArea', 'BldgType', 'OverallQual', 'OverallCond',
                        'YearBuilt', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual',
                        'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'TotalBsmtSF', 'CentralAir',
                        '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'KitchenQual', 'TotRmsAbvGrd',
                        'GarageType', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PoolArea',
                        'MiscVal', 'SaleType', 'SaleCondition']

        # Convert the list newData into a DataFrame
        newData_df = pd.DataFrame([newData], columns=column_names)

        # Transform the data using the preprocessor
        newDataTrf = preprocess.transform(newData_df)

        newDataPCA = PCA.transform(newDataTrf)

        pred = model.predict(newDataPCA)

        print(pred)

        output = {
            'output':pred
        }

        return render(request,'posts/prediction.html',output)

    else:
        return render(request, 'posts/prediction.html')






def add_review(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Filter reviews by post and count distinct users who reviewed
    post_review = Review.objects.filter(post=post).values('user').distinct().count()
    average_rating_for_post = Review.objects.filter(post=post).aggregate(average_rating=Avg('rating'))
    one = Review.objects.filter(rating=1,post=post).values('user').distinct().count()
    two = Review.objects.filter(rating=2,post=post).values('user').distinct().count()
    three = Review.objects.filter(rating=3,post=post).values('user').distinct().count()
    four = Review.objects.filter(rating=4,post=post).values('user').distinct().count()
    five = Review.objects.filter(rating=5,post=post).values('user').distinct().count()
    all_review  = Review.objects.filter(post=post).order_by('-created_at')[:5]

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Attach the logged-in user
            review.post = post  # Attach the post being reviewed
            review.save()
            return redirect('post-detail', post.id)  # Redirect to post detail page after submission
    else:
        form = ReviewForm()

    return render(request, 'posts/add_review.html', {'form': form, 'post': post, 'data': post_review,'avg_rating':average_rating_for_post,'one':one,'two':two,'three':three,'four':four,'five':five,'all_review':all_review})




class PostSearchView(ListView):
    model = Post
    template_name = 'posts/post_search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Override the get_queryset method to filter posts by address using the search query.
        The search is case-insensitive and returns results where the address contains the search term.
        """
        queryset = Post.objects.all()
        form = PostSearchForm(self.request.GET or None)

        if form.is_valid():
            address = form.cleaned_data.get('address')
            if address:
                # Filter posts where the address contains the search term (case-insensitive)
                queryset = queryset.filter(address__icontains=address)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Pass the search form into the context so it can be rendered in the template.
        """
        context = super().get_context_data(**kwargs)
        context['form_x'] = PostSearchForm(self.request.GET)
        return context








