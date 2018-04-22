from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from .models import banner
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name='solarpanel/admin.html'


class ContentListView(ListView):
    model = banner
    template_name = 'solarpanel/content.html'
    context_object_name = 'con'

    def get_queryset(self):
        return banner.objects.order_by('type')


class ContentDetailView(DetailView):
    model = banner
    template_name='solarpanel/contentdetail.html'
    context_object_name='c'

class BannerDetailView(LoginRequiredMixin,CreateView):
    #login_url = '/'
    #redirect_field_name = 'blog/post_detail.html
    template_name='solarpanel/banner.html'
    context_object_name='banner'
    model=banner
    fields = ('type','heading', 'photo','description')
    #success_url =  reverse_lazy('solarpanel:list')

    def post(self, request, *args, **kwargs):
        type=1
        photo = self.request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        url = fs.url(filename)

        heading = self.request.POST.get('heading')
        description = self.request.POST.get('description')


        #form = self.get_form(type=type, photo=url, heading=heading, description=description)

        form = banner(type=type, photo=url, heading=heading, description=description)
        #super(BannerDetailView, self).form_valid(form)
         #messages.success(request, 'Item created successfully!')
        form.save()

        return HttpResponseRedirect(reverse('solarpanel:list'))



class ProjectDetailView(LoginRequiredMixin,CreateView):
        template_name = 'solarpanel/project.html'
        context_object_name = 'project'
        model = banner
        fields = ('type', 'heading', 'photo', 'description')

        # success_url =  reverse('content')

        def post(self, request, *args, **kwargs):
            type = 2
            photo = self.request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            url = fs.url(filename)

            heading = self.request.POST.get('heading')
            description = self.request.POST.get('description')
            form = banner(type=type, photo=url, heading=heading, description=description)
            #super(ProjectDetailView, self).form_valid(form)
            # messages.success(request, 'Item created successfully!')
            form.save()

            return HttpResponseRedirect(reverse('solarpanel:list'))

class CareerDetailView(LoginRequiredMixin,CreateView):
    template_name='solarpanel/career.html'
    context_object_name='career'
    model=banner
    fields = ('type','heading', 'photo','description','openings')
    #success_url =  reverse('content')

    def post(self, request, *args, **kwargs):
        type=3
        photo = self.request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        url = fs.url(filename)

        heading = self.request.POST.get('heading')
        description = self.request.POST.get('description')
        openings = self.request.POST.get('openings')

        #form = self.get_form(type=type, photo=url, heading=heading, description=description)

        form = banner(type=type, photo=url, heading=heading, description=description, openings=openings)
        #super(CareerDetailView, self).form_valid(form)
         #messages.success(request, 'Item created successfully!')
        form.save()

        return HttpResponseRedirect(reverse('solarpanel:list'))



class TeamDetailView(LoginRequiredMixin,CreateView):
    template_name='solarpanel/team.html'
    context_object_name='team'
    model=banner
    fields = ('type','name','linkfb','linkinsta','linklin', 'photo','description','designation')
    #success_url =  reverse('content')

    def post(self, request, *args, **kwargs):
        type=4
        photo = self.request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        url = fs.url(filename)

        name = self.request.POST.get('name')
        description = self.request.POST.get('description')
        designation = self.request.POST.get('designation')
        linkfb = self.request.POST.get('linkfb')
        linkinsta = self.request.POST.get('linkinsta')
        linklin = self.request.POST.get('linklin')

        #form = self.get_form(type=type, photo=url, heading=heading, description=description)

        form = banner(type=type, photo=url, designation=designation,linkfb=linkfb,linkinsta=linkinsta,linklin=linklin,name=name, description=description)
        #super(TeamDetailView, self).form_valid(form)
         #messages.success(request, 'Item created successfully!')
        form.save()

        return HttpResponseRedirect(reverse('solarpanel:list'))


class MediaDetailView(LoginRequiredMixin,CreateView):
    template_name='solarpanel/media.html'
    context_object_name='media'
    model=banner
    fields = ('type','heading', 'photo','description')
    #success_url =  reverse('content')

    def post(self, request, *args, **kwargs):
        type=5
        photo = self.request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        url = fs.url(filename)

        heading = self.request.POST.get('heading')
        description = self.request.POST.get('description')


        #form = self.get_form(type=type, photo=url, heading=heading, description=description)

        form = banner(type=type, photo=url, heading=heading, description=description)
        #super(MediaDetailView, self).form_valid(form)
         #messages.success(request, 'Item created successfully!')
        form.save()

        return HttpResponseRedirect(reverse('solarpanel:list'))

class BannerUpdateView(LoginRequiredMixin,UpdateView):
    fields=('photo','heading','description')
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class ProjectsUpdateView(LoginRequiredMixin,UpdateView):
    fields=('photo','heading','description')
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class CareerUpdateView(LoginRequiredMixin,UpdateView):
    fields=('photo','heading','description','openings')
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class TeamUpdateView(LoginRequiredMixin,UpdateView):
    fields=('photo','description','name','designation','linkfb','linkinsta','linklin')
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class MediaUpdateView(LoginRequiredMixin,UpdateView):
    fields=('photo','heading','description')
    model = banner
    success_url = reverse_lazy('solarpanel:list')


class BannerDeleteView(LoginRequiredMixin,DeleteView):
    model = banner
    success_url = reverse_lazy('solarpanel:list')


class ProjectsDeleteView(LoginRequiredMixin,DeleteView):
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class CareerDeleteView(LoginRequiredMixin,DeleteView):
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class TeamDeleteView(LoginRequiredMixin,DeleteView):
    model = banner
    success_url = reverse_lazy('solarpanel:list')

class MediaDeleteView(LoginRequiredMixin,DeleteView):
    model = banner
    success_url = reverse_lazy('solarpanel:list')