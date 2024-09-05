from django.shortcuts import render,redirect
from . models import login_tbl
from shopping.models import product_tbl
# Create your views here.
def sellerreg(request):
    if request.method=='POST':
        username=request.POST.get('username')
        mobilenumber=request.POST.get('mobilenumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        obj=login_tbl.objects.create(confirmpassword=confirmpassword,password=password,email=email,mobilenumber=mobilenumber,username=username)
        obj.save()
        if obj:
            msg='Account created successfully'
            return render(request,"signin.html",{"success":msg})
        else:
            return render(request,"sellerreg.html")
    else:
        return render(request,"sellerreg.html")

def logout(request):
    del request.session['ema']
    del request.session['idl']
    del request.session['psa']
    return render(request,"index.html")
def data(request):
    if request.method=='POST':
        im=request.FILES.get('im')
        cg=request.POST.get('cg')
        br=request.POST.get('br')
        nm=request.POST.get('nm')
        pr=request.POST.get('pr')
        of=request.POST.get('of')
        opr=request.POST.get('opr')
        obj=product_tbl.objects.create(im=im,cg=cg,br=br,nm=nm,pr=pr,of=of,opr=opr)
        obj.save()
        if obj:
            msg='data successfully'
            return render(request,"data.html",{"data":msg})
        else:
            return render(request,"data.html")
    else:
        return render(request,"data.html")