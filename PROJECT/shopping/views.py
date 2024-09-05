from django.shortcuts import render,redirect
from sellerapp.models import login_tbl
from . models import shop_tbl,product_tbl,cart_tbl,wishlist_tbl,address_tbl,order_tbl
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def regform(request):
    if request.method=='POST':
        fn=request.POST.get('fn')
        mb=request.POST.get('mb')
        em=request.POST.get('em')
        ps=request.POST.get('ps')
        cps=request.POST.get('cps')
        state=request.POST.get('state')
        city=request.POST.get('city')
        road=request.POST.get('road')
        house=request.POST.get('house')
        pincode=request.POST.get('pincode')
        obj=shop_tbl.objects.create(fn=fn,mb=mb,em=em,ps=ps,cps=cps,state=state,city=city,road=road,house=house,pincode=pincode)
        obj.save()
        if obj:
            msg='Account created successfully'
            return render(request,"signin.html",{"success":msg})
        else:
            return render(request,"regform.html")
    else:
        return render(request,"regform.html")
def signin(request):
    if request.method=='POST':
        em=request.POST.get('em')
        ps=request.POST.get('ps')
        obj=shop_tbl.objects.filter(em=em,ps=ps)
        obb = login_tbl.objects.filter(email=em,password=ps)
        if obj:
            for ls in obj:
                idno = ls.id
            request.session['ema']=em
            request.session['idl']=idno
            request.session['psa']=ps
            return render (request,"index.html")
        elif obb:
            for ls in obb:
                idno = ls.id
            request.session['ema']=em
            request.session['idl']=idno
            request.session['psa']=ps
            return render (request,"data.html")
        else:
            msg='invalid data'
            request.session['ema']=''
            request.session['psa']=''
            return render(request,"signin.html",{"error":msg})
    else:
        return render(request,"signin.html")
def signout(request):
    del request.session['ema']
    del request.session['idl']
    del request.session['psa']
    return redirect("/index")
def search(request):
    if request.method=='POST':
        sr=request.POST['sr']
        sr=product_tbl.objects.filter(nm__icontains=sr) or product_tbl.objects.filter(br__icontains=sr) or product_tbl.objects.filter(cg__icontains=sr)
        if not sr:
            messages.success(request,"That Product Does Not Exist.. Please Try Again")
            return render(request,"search.html",{})
        else:
            return render(request,"alldata.html",{'key':sr})
        
    return render(request,"search.html")
def alldata(request):
    obj=product_tbl.objects.all()
    return render(request,"alldata.html",{"key":obj})
def addtocart(request):
    number=request.GET.get('idn')
    userid=request.session['idl']
    uobj=shop_tbl.objects.get(id=userid)
    pobj=product_tbl.objects.get(id=number)
    cartitem,created=cart_tbl.objects.get_or_create(customer=uobj,product=pobj)
    if not created:
        cartitem.quantity+=1
        cartitem.save()
        messages.success(request,"Item added to cart")
        return redirect('/viewcart')
    return redirect('/viewcart')
def viewcart(request):
    cid=request.session['idl']
    cusobj=shop_tbl.objects.get(id=cid)
    cartobj=cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price=0
        for i in cartobj:
            pro=i.product.pr*i.quantity
            total_price=total_price+pro

        return render(request,"viewcart.html",{'cartitems':cartobj,'total_price':int(total_price)})
    else:
        return render(request,"viewcart.html",{"info":"Your Cart Is Empty"})
def removefromcart(request):
    number=request.GET.get('idn')
    obj=cart_tbl.objects.filter(id=number)
    obj.delete()
    return redirect("/viewcart")
def addtowishlist(request):
    number=request.GET.get('idn')
    userid=request.session['idl']
    uobj=shop_tbl.objects.get(id=userid)
    pobj=product_tbl.objects.get(id=number)
    wishlistitem,created=wishlist_tbl.objects.get_or_create(product=pobj,customer=uobj)
    if not created:
        wishlistitem.save()
        messages.success(request,"Item added to Wishlist")
        return redirect('/wishlist')
    return redirect('/wishlist')
def wishlist(request):
    cid=request.session['idl']
    cusobj=shop_tbl.objects.get(id=cid)
    removeobj=wishlist_tbl.objects.filter(customer=cusobj)
    if removeobj:
        return render(request,"wishlist.html",{'wishlistitems':removeobj})
    else:
        return render(request,"wishlist.html",{"info":"Your wishlist Is Empty"})
def removefromwishlist(request):
    number=request.GET.get('idn')
    obj=wishlist_tbl.objects.filter(id=number)
    obj.delete()
    return redirect("/wishlist")
def address(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mob=request.POST.get('mob')
        amb=request.POST.get('amb')
        pin=request.POST.get('pin')
        st=request.POST.get('st')
        cty=request.POST.get('cty')
        hs=request.POST.get('hs')
        rd=request.POST.get('rd')
        obj=address_tbl.objects.create(name=name,mob=mob,amb=amb,pin=pin,st=st,cty=cty,hs=hs,rd=rd)
        obj.save()
        if obj:
            return redirect("/payment")
        else:
            return render(request,"address.html")
    else:
        idno=request.GET.get('idn')
        request.session['cartid']=idno
        return render(request,"address.html")
def details(request):
    cid=request.session['idl']
    cusobj=shop_tbl.objects.get(id=cid)
    cartobj=cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price=0
        for i in cartobj:
            pro=i.product.pr*i.quantity
            total_price=total_price+pro
        return render(request,"details.html",{'cartitems':cartobj,'total_price':int(total_price),"address":cusobj})
    return render(request,"viewcart.html")
def myorder(request):
    obj=order_tbl.objects.all()
    return render(request,"myorder.html",{"key":obj})      
def payment(request):
    return render(request,"payment.html")
def creditcard(request):
    if request.method=='POST':
        return render(request,"placed.html")
    return render(request,"creditcard.html")
def upi(request):
    if request.method=='POST':
        return render(request,"placed.html")
    return render(request,"upi.html")
def netbanking(request):
    if request.method=='POST':
        return render(request,"placed.html")
    return render(request,"netbanking.html")
def placed(request):
    if request.method == 'POST':
        # Get the total price from the form
        totalprice = request.POST.get('newprice')
        product= request.POST.get('')
        # Check if the user has provided a new address
        nm = request.POST.get('name') or request.POST.get('fn')
        mob = request.POST.get('mb') or request.POST.get('mb')
        stat = request.POST.get('st') or request.POST.get('state')
        city = request.POST.get('cty') or request.POST.get('city')
        road = request.POST.get('rd') or request.POST.get('road')
        hous = request.POST.get('hs') or request.POST.get('house')
        pin = request.POST.get('pin') or request.POST.get('pincode')

        # Create and save the order with correct field names
        obc = order_tbl.objects.create(
            nm=nm,
            mob=mob,
            stat=stat,
            city=city,
            road=road,
            hous=hous,
            pin=pin,
            totalprice=totalprice,
            orderstatus='Pending'  # Assuming default order status is 'Pending'
        )
        obc.save()
        # Render the payment page after creating the order
        return render(request, "payment.html")

    # In case of a GET request or other method, render the order form
    return render(request, "details.html")



    
    
    




    
