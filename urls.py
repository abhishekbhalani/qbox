from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    	# Examples:
	url(r'^$', 'box.views.list_questions', name='home'), # match urls of type http://urlname - and hook to listq function in views.py
	url(r'^question/(\d+)/$', 'box.views.list_answers', name='list of answers'), #match urls of type http://urlname/question/10 - and hoot to lista function in views.py
    	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'qbox/login.html'}),
	# url(r'^qbox/', include('qbox.foo.urls')),

    
		# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
