from django.shortcuts import redirect, render
from . models import Contact

# Create your views here.





   

def index(request):
    contact1 = Contact.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        itemname=request.POST.get('itemname','')
        description=request.POST.get('description','')
        contact=Contact(slno=slno,itemname=itemname,description=description)
        contact.save()
    
    
    return render(request,"index.html",{'contact1':contact1})

def delete(request,contactid):
    contact=Contact.objects.get(id=contactid)
    if request.method=='POST':
        contact.delete()
        return redirect('/')


    return render(request,'delete.html')


def update(request, id):
   
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        slno = request.POST['slno']
        itemname = request.POST['itemname']
        description = request.POST['description']

        contact.slno = slno
        contact.itemname = itemname
        contact.description = description
        contact.save()

        return redirect('/')
    
    return render(request, 'edit.html', { 'contact': contact})