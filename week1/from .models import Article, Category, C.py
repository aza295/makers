from .models import Article, Category, Comment, ArticleViews
from .froms import CommentForm, CustomCreateForm
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_objeect_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import View
from Django.views.generic import listView, DetailView
from Django.core.exceptions import PermissionDenied
from Django.contrib.auth.mixins import LoginRequiredMixin
from Django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.utils.translation import gettext
from limon_project. mixins import DispatchFunchMixin
from Django.db.models import Q



class CategortyList(LIstView):
     template_name = 'category.html'
     model = Category
     context_object_name = 'categories'
      

class ArticleSearchView(ListView):
    template_name = 'includes/article_search-result.html'
    model = Article 

    def get_queryset(self):
        query_result = self.request,GET.get('search title')
        filter_category = self.request.GET.getlist ('category')
        if query_result:
            queryset = Article.objects.filter(
                Q(title_icontains=query_result)
                Q (description__icontains=query_result)
            )


class ArticlePageView(ListView):
    """Вывод всех объектов """
# template-name = 'articles/article_list.html'
  tempalate_name = 'index1.html'
  paginnate_by = 3
  context_object_name = 'posts'

  """"
  example code to change session key
  """
  #def dispatch(self,request,*args, **kwargs)
  #    from dajngo.utils import translatiom
  #    user_language = 'ru'
  #    translation.activate(user_language)
  #    request.session [translation.LANGUAGE_SESSION_KEY] = user_language
  #    return super(). dispatch(request,*args.**kwargs)

  def get_queryset(self):
      queryset = Article.objects.all()
      query_result = self.request.GET.get('search_title')
      filter_category = self.request.GET.getlist('category')
      if query_result:
          queryset = Article.object.filter
          Q (title_icontains=query_result)
          Q(description_icontains=query_result)


          )  
      if filter category:
          queryset = Article.objects.filter(
              Q(category_in=filter_category)    
          )
      return queryset

  def get_context_data(self, **kwargs):
      context = super ().get_context_data (*kwargs) 
      some_text = gettext('Hello World')
      context['some_text'] = some_texyt
      return context







class ArticleDetasilview(Formview,DetailView):
       """Детализация объекта """
       model = Article
       form_class = CommentForm
       template_name = 'articles?article_detail.html'
       context_object_name = 'post'    

       def dispatch (self,request,*args,**kwargs):
           article= get_object_or_404(Article, id=self. kwargs['pk'])
           context = {}
           obj, created = ArticleiIews.objects.get_or_create(
               defaults={
                   'article':article,
               },
           )
           if created:
               obj.views += 1
               obj.save(update_fields=['views'])
            else
            obj.views += 1
            obj.save(update_fields=['views'])
            return super (ArticleDetailView, self).dispatch (request, *args, **kwargs)



        def get_success_url(self,*args,**kwargs):
            return reverse_lazy('article_detail',kwargs={'pk':self.get_object(.pk)})



        def form_valid(self,form):
            form= form.save(commit=false)    
            reply = self.request.POST.get('comment_id',None)
            comment_qs = None
            if reply:
                comment-qs = Comment.objects.get(id=reply)
                form.reply = comment-qs
                form.article = self.get_object()
                form.author = self.request.user
                form.save()
                return super().form_valid(form)
class ArticleUpdateView(LoginRequiredMixin, DispatchFunchMixin, Updateview):
     """Обновление объекта """ 
     model = Article
     fields = ('title','description','immage','category')
     template_name = 'articles/article_deit.html'
     login_url='login'

        def get_context_data(self, *args,**kwargs):
            some_list = ["john", "raychel"]
            context = super().get_context_data()#{"object":"object_detail"}
            context['some_lists']
            return context


class ArticleDeleteView(LoginRequiredMixin,DispatchFunchMixin,DeleteView):
    """Удаление объекта """
    model = Article
    template_name = 'articles/article-delete.html'
    success_url = reverse-lazy('article_list')
    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Создание объекта """
    model = Article
    form_class = CustomCreateForm
    tempalate_name = 'articles/article_create.html'
    login_url = 'login'

    form.instance.author= self.request.user
    def from_vaild(self,form)