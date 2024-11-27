from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import ArticlePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ArticlePost
from django.views.generic import DetailView
from django.views.generic import DeleteView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage



class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 8
    queryset = ArticlePost.objects.order_by('-posted_at')

@method_decorator(login_required, name='dispatch')
class CreateArticleView(CreateView):
    form_class = ArticlePostForm
    template_name = "post_article.html"
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)


class PostSuccessView(TemplateView):
    template_name ='post_success.html'

class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 8

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ArticlePost.objects.filter(
        category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name ='index.html'
    paginate_by = 8

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = ArticlePost.objects.filter(
        user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name ='detail.html'
    model = ArticlePost

class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = ArticlePost.objects.filter(
        user=self.request.user).order_by('-posted_at')
        return queryset
    
class ArticleDeleteView(DeleteView):
    model = ArticlePost
    template_name ='article_delete.html'
    success_url = reverse_lazy('article:mypage')

    def delete(self, request, *args, **kwargs):
      return super().delete(request, *args, **kwargs)
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('article:contact')
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ：{}'.format(title)
        message = \
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}'\
            .format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')

        return super().form_valid(form)
    
    