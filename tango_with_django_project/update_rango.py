import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def update():
    
    category_list = Category.objects.all()
    page_list = Page.objects.all()
    n = 1
    m = 2
    for category in category_list:
        category.likes = n
        category.views = 2*n
        category.save()
        n *= 2
        
    for page in page_list:
        page.views = m
        page.save()
        m +=2
        
            

if __name__ == '__main__':
    print "Starting Rango update script..."
    update()
    
    