from django.shortcuts import render
from.froms import ProductForm

# Create your views here
def add_product(request):
    if request.method=="GET":
       form= form.ProductForm(request.GET,instance=p)
       if form.is.valid():
           form.save()
           return HttpResponse('add successful')

       else:
           form=forms.ProductForm(instance=p)
        return render(request,template_name='forms.html',context{
           "form": form,
       })

       def update_product(request,p_id):
           product.objects.get(pk=p_id)

