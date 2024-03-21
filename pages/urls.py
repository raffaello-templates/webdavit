from django.urls import path

from .views import HomePageView, AboutPageView, MobiledevPageView, SoftwaredevPageView, OffshoreSWdevPageView, GraphicsdevPageView, WebdevPageView, WordpressdevPageView, basecontactView, quoteView, successView, HireDrupaldevPageView, HireJoomladevPageView, HireLaraveldevPageView, HirePhpdevPageView, HireWebdevPageView, HireWordpressdevPageView, PhpdevPageView, PythondevPageView, LaraveldevPageView, ReactjsdevPageView, AngularjsdevPageView, DrupaldevPageView, JoomladevPageView, MagentodevPageView, Html5devPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('mobile_dev/', MobiledevPageView.as_view(), name='mobiledev'),
    path('software_dev/', SoftwaredevPageView.as_view(), name='softwaredev'),
    path('offshore_sw_dev/', OffshoreSWdevPageView.as_view(), name='offshoreswdev'),
    path('web_dev/', WebdevPageView.as_view(), name='webdev'),
    path('wordpress_dev/', WordpressdevPageView.as_view(), name='wordpressdev'),
    path('graphics_dev/', GraphicsdevPageView.as_view(), name='graphicsdev'),

    path('hire_drupal_dev/', HireDrupaldevPageView.as_view(), name='hiredrupaldev'),
    path('hire_joomla_dev/', HireJoomladevPageView.as_view(), name='hirejoomladev'),
    path('hire_laravel_dev/', HireLaraveldevPageView.as_view(), name='hirelaraveldev'),
    path('hire_php_dev/', HirePhpdevPageView.as_view(), name='hirephpdev'),
    path('hire_web_dev/', HireWebdevPageView.as_view(), name='hirewebdev'),
    path('hire_wordpress_dev/', HireWordpressdevPageView.as_view(), name='hirewordpressdev'),

    path('php_dev/', PhpdevPageView.as_view(), name='phpdev'),
    path('python_dev/', PythondevPageView.as_view(), name='pythondev'),
    path('laravel_dev/', LaraveldevPageView.as_view(), name='laraveldev'),
    path('reactjs_dev/', ReactjsdevPageView.as_view(), name='reactjsdev'),
    path('angularjs_dev/', AngularjsdevPageView.as_view(), name='angularjsdev'),
    path('drupal_dev/', DrupaldevPageView.as_view(), name='drupaldev'),
    path('joomla_dev/', JoomladevPageView.as_view(), name='joomladev'),
    path('magento_dev/', MagentodevPageView.as_view(), name='magentodev'),
    path('html5_dev/', Html5devPageView.as_view(), name='html5dev'),

    path('contact/', basecontactView, name='basecontact'),
    path('quote/', quoteView, name='quote'),
    path('success/', successView, name='success'),
]