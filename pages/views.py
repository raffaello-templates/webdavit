from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm, QuoteForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class MobiledevPageView(TemplateView):
    template_name = 'mobile_dev.html'

class SoftwaredevPageView(TemplateView):
    template_name = 'software_dev.html'

class OffshoreSWdevPageView(TemplateView):
    template_name = 'offshore_sw_dev.html'

class GraphicsdevPageView(TemplateView):
    template_name = 'graphics_dev.html'

class WebdevPageView(TemplateView):
    template_name = 'web_dev.html'

class WordpressdevPageView(TemplateView):
    template_name = 'wordpress_dev.html'

class HireDrupaldevPageView(TemplateView):
    template_name = 'hire_drupal_dev.html'

class HireJoomladevPageView(TemplateView):
    template_name = 'hire_joomla_dev.html'

class HireLaraveldevPageView(TemplateView):
    template_name = 'hire_laravel_dev.html'

class HirePhpdevPageView(TemplateView):
    template_name = 'hire_php_dev.html'

class HireWebdevPageView(TemplateView):
    template_name = 'hire_web_dev.html'

class HireWordpressdevPageView(TemplateView):
    template_name = 'hire_wordpress_dev.html'

class PhpdevPageView(TemplateView):
    template_name = 'php_dev.html'

class PythondevPageView(TemplateView):
    template_name = 'python_dev.html'

class LaraveldevPageView(TemplateView):
    template_name = 'laravel_dev.html'

class ReactjsdevPageView(TemplateView):
    template_name = 'reactjs_dev.html'

class AngularjsdevPageView(TemplateView):
    template_name = 'angularjs_dev.html'

class DrupaldevPageView(TemplateView):
    template_name = 'drupal_dev.html'

class JoomladevPageView(TemplateView):
    template_name = 'joomla_dev.html'

class MagentodevPageView(TemplateView):
    template_name = 'magento_dev.html'

class Html5devPageView(TemplateView):
    template_name = 'html5_dev.html'

def inject_form(request):
    return {'form': ContactForm()}


def basecontactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'company': form.cleaned_data['company'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@webdavit.com', ['kennyokans@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent!')
            return redirect('home')
        messages.warning(request, 'Error. Message was not sent!')
    return render(request, "_base.html", {'form': form})


def quoteView(request):
    if request.method == 'GET':
        form = QuoteForm()
    else:
        form = QuoteForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'company': form.cleaned_data['company'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@webdavit.com', ['kennyokans@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent!')
            return redirect('quote')
        messages.warning(request, 'Error. Message was not sent!')
    return render(request, "quote.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')