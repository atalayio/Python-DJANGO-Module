from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'home/index.html',)




def index2(request):

    c=''
    n1=''
    n2=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            
            c=n1+n2;
            
           

    except:
        c="hatalı sayı girdiniz."


    print(c)
    return render(request,"home/index2.html",{'c':c,'n1':n1,'n2':n2})




def alan(request):
    n1=''
    n2=''
    kr=request.POST.get(('kare'))
    dk=request.POST.get(('dikdortgen'))
    uc=request.POST.get(('ucgen'))   
    sonuc=''
    

    sonuc=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            if request.POST.get(('kare')):
                sonuc = n1*n2;
            elif request.POST.get(('dikdortgen')):
                sonuc= n1*n2;
            elif request.POST.get(('ucgen')):
                sonuc= (n1*n2)/2;
    except:
        sonuc="hatalı sayı girdiniz."

                

    




    return render(request, 'home/alanhesap.html',{'sonuc':sonuc,'n1':n1,'n2':n2})



def indirim(request):
    n1=""
    n2=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))

            sonuc = (n1) - (n1*n2/100);
    except:
        sonuc="hatalı sayı girdiniz."


    return render(request, 'home/indirimhesapla.html',{'sonuc':sonuc,'n1':n1,'n2':n2})




def inc(request):
    n1=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))

            sonuc = n1 * 2.54;
    except:
        sonuc="Hatalı sayı girdiniz."


    return render(request, 'home/inchesap.html',{'sonuc':sonuc,'n1':n1})


def aks(request):
    n1=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            if n1 < 60:
                sonuc="Sınavınız geçersizdir."
            elif n1 > 60:
                sonuc= float(n1* 100);
    except:
        sonuc="hatalı sayı girdiniz."


            






    return render(request, 'home/akshesap.html',{'sonuc':sonuc,'n1':n1})



def creatin(request):
    n1=""
    sonuc=""
    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        if 34 < n1 < 40:
            sonuc="Günlük creatin ihtiyacınız 2 - 4 gram arasındadır."
        elif 41 < n1 < 60:
            sonuc="Günlük creatin ihtiyacınız 3 - 5 gram arasındadır."
        elif 61 < n1 < 80:
            sonuc="Günlük creatin ihtiyacınız 4 - 6 gram arasındadır."
        elif 81 < n1 < 100:
            sonuc="Günlük creatin ihtiyacınız 5 - 7 gram arasındadır."
        elif 100 < n1 < 250:
            sonuc="Günlük creatin ihtiyacınız 6 - 8 gram arasındadır."
        elif n1 < 35:
            sonuc="Günlük creatin ihtiyacınız için hesaplanabilecek değer 35 - 250 kilogram arasındadır."
        elif n1 > 249:
            sonuc="Günlük creatin ihtiyacınız için hesaplanabilecek değer 35 - 250 kilogram arasındadır."
        





    return render(request, 'home/creatinhesap.html',{'sonuc':sonuc,'n1':n1})


#<option value="secim">Seçim Yap*</option>
#<option value="yüzdebir">%1</option>
#<option value="yüzdesekiz">%8</option>
#<option value="yüzdeonsekiz">%18</option>


def kdv(request):
    n1=""
    opr=""
    sonuc=""
    try:
        if request.method =="POST":
            n1=eval(request.POST.get('num1'))
            opr= request.POST.get('opr')
            if opr=="secim":
                sonuc="Lütfen hesaplanabilecek bir seçimi seçiniz!"
            elif opr=="yüzdebir":
                sonuc= n1 + (n1*1/100)
            elif opr=="yüzdesekiz":
                sonuc= n1 + (n1*8/100)
            elif opr=="yüzdeonsekiz":
                sonuc = n1 + (n1*18/100)


    except:
        sonuc="hatalı sayı girdiniz."






    return render(request, 'home/kdvhesap.html',{'sonuc':sonuc,'n1':n1})



"""
                                        <option value="secim">Kağıt Türü Seçiniz*</option>
                                        <option value="kefilsiz">Kefilsiz Kira Sözleşmesi</option>
                                        <option value="adli">Adli Kefil Kira Sözleşmesi</option>
                                        <option value="müteselsil">Müteselsil Kefili Kira Sözleşmesi</option>
                                        <option value="ikinciel">2.EL Satış Ve Devir Sözleşmesi</option>
"""


def damgavergi(request):

    n1=""
    opr=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            opr=request.POST.get('opr')
            if opr=="secim":
                sonuc="Lütfen hesaplanabilecek bir seçimi seçiniz!"
            elif opr=="kefilsiz":
                sonuc= n1 + (n1* 1.89/1000)
            elif opr=="adli":
                sonuc= n1 + (n1 * 11.37/1000)
            elif opr=="müteselsil":
                sonuc= n1 + ( n1 * 9.48/1000)
            elif opr=="ikinciel":
                sonuc= n1 + (n1 * 1.89/1000)
    except:
        sonuc="hatalı sayı girdiniz."

    return render(request, 'home/damgavergisi.html',{'sonuc':sonuc})


def dibsinav(request):
    n1=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            sonuc = (n1 * 1.33333) + 20
            if n1 > 60:
                sonuc="Lütfen geçerli bir doğru sayısı giriniz."
    except:
        sonuc="hatalı sayı girdiniz."
    
    return render(request, 'home/dib.html',{'sonuc':sonuc,'n1':n1})


def ehliyet(request):
    n1=""
    sonuc=""
    sonuc2=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            sonuc= n1 * 2
            if n1 > 50:
                sonuc = "Toplam doğru sayısı en fazla 50 olabilir. Lütfen girdiğiniz bilgileri kontrol edip tekrar deneyin."
            elif n1 < 35:
                sonuc2="Kaldınız."
            elif n1 >= 35:
                sonuc2="Geçtiniz."


    except:
        sonuc="hatalı sayı girdiniz."

    return render(request, 'home/ehliyet.html',{'sonuc':sonuc,'n1':n1,'sonuc2':sonuc2})


def jana(request):
    n1=""
    sonuc=""
    sonuc2=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            sonuc = n1
            if n1 >= 60:
                sonuc2="Geçtiniz."
            elif n1 < 60:
                sonuc2="Kaldınız."
    except:
        sonuc="hatalı sayı girdiniz."





    return render(request, 'home/jana.html',{'sonuc':sonuc,'n1':n1,'sonuc2':sonuc2})


def kombiya(request):
    n1=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            sonuc = (n1 * 0.002) + n1
    except:
        sonuc="hatalı sayı girdiniz."
    
    return render(request, 'home/kombiya.html',{'sonuc':sonuc,'n1':n1})



def kurumlar(request):
    n1=""
    sonuc=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            sonuc = (n1 * 23/100)
    except:
        sonuc="hatalı sayı girdiniz."



    return render(request, 'home/kurumlar.html',{'sonuc':sonuc,'n1':n1})



def vucutk(request):
    c=''
    n1=''
    n2=''
    d=''
    b=''
    a=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('n1'))
            n2=eval(request.POST.get('n2'))
            
            c=n2/(n1*n1);
            b="Vücut Kitle Endeksiniz (BMI): "
            a=int(c)
            if c<18.5: 
                c="Zayıfsınız"
                d="Boyunuza göre uygun ağırlıkta olmadığınızı, zayıf olduğunuzu gösterir. Zayıflık, bazı hastalıklar için risk oluşturan ve istenmeyen bir durumdur. Boyunuza uygun ağırlığa erişmeniz için yeterli ve dengeli beslenmeli, beslenme alışkanlıklarınızı geliştirmeye özen göstermelisiniz."
            elif c>18.5 and c<24.9: 
                c="Normal"
                d="Boyunuza göre uygun ağırlıkta olduğunuzu gösterir. Yeterli ve dengeli beslenerek ve düzenli fiziksel aktivite yaparak bu ağırlığınızı korumaya özen gösteriniz."
            elif c>25 and c<29.9: 
                c="Kilolu"
                d="Boyunuza göre vücut ağırlığınızın fazla olduğunu gösterir. Fazla kilolu olma durumu gerekli önlemler alınmadığı takdirde pek çok hastalık için risk faktörü olan obeziteye (şişmanlık) yol açar."
            elif c>30 and c<34.9: 
                c="Obez"
                d="Boyunuza göre vücut ağırlığınızın fazla olduğunu bir başka deyişle şişman olduğunuzun bir göstergesidir. Şişmanlık, kalp-damar hastalıkları, diyabet, hipertansiyon v.b. kronik hastalıklar için risk faktörüdür. Bir sağlık kuruluşuna başvurarak hekim / diyetisyen kontrolünde zayıflayarak normal ağırlığa inmeniz sağlığınız açısından çok önemlidir. Lütfen, sağlık kuruluşuna başvurunuz."
            elif c>35: 
                c="Morbid obez"
                d="Boyunuza göre vücut ağırlığınızın fazla olduğunu bir başka deyişle şişman olduğunuzun bir göstergesidir. Şişmanlık, kalp-damar hastalıkları, diyabet, hipertansiyon v.b. kronik hastalıklar için risk faktörüdür. Bir sağlık kuruluşuna başvurarak hekim / diyetisyen kontrolünde zayıflayarak normal ağırlığa inmeniz sağlığınız açısından çok önemlidir. Lütfen, sağlık kuruluşuna başvurunuz."

            
           

    except:
        c="hatalı değerler girdiniz."

    return render(request,'home/vucutk.html',{'c':c,'n1':n1,'n2':n2,'d':d,'b':b,'a':a})

def mezuniyet(request):

    c=''
    n1=''
    n2=''
    n3=''
    n4=''
    b=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('n1'))
            n2=eval(request.POST.get('n2'))
            n3=eval(request.POST.get('n3'))
            n4=eval(request.POST.get('n4'))
            
            c=(n1+n2+n3+n4)/4;
            b="Lise Mezuniyet Puanınız :"
           

    except:
        c="hatalı sayı girdiniz."


    
    return render(request,"home/mezuniyet.html",{'c':c,'n1':n1,'n2':n2,'n3':n3,'n4':n4,'b':b})
   
def stopaj(request):
    c=''
    n1=''
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            
            
            
            c=((n1*1.2)+n1)/5;
            
           

    except:
        c="hatalı sayı girdiniz."


    

    
    return render(request,'home/stopaj.html',{'c':c,'n1':n1})
     

def noth(request):
    
    b=''
    c=''
    n1=''
    n2=''
    n3=''
   
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            if request.POST.get('num3'):
                n3=eval(request.POST.get('num3'))
                c=(n1+n2+n3)/3;
                b="Hesaplanan notunuz : {0}".format(c)

            else:
                c=(n1+n2)/2;
 
                b="Hesaplanan notunuz : {0}".format(c)
                
        
                

    except:
        c="hatalı sayı girdiniz."

    return render(request,'home/noth.html',{'c':c,'n1':n1,'n2':n2,'n3':n3,'b':b})

def obph(request):
    c=''
    n1=''
    a=''
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
           
            
            c=n1*5;
            a="OBP Puanınız : {0}".format(c)

            
           

    except:
        c="hatalı sayı girdiniz."


   
    
    return render(request,'home/obph.html',{'c':c,'n1':n1,'a':a,})



def sigara(request):

     
    a=''
    b=''
    c=''
    n1=''
    n2=''
    d=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            a=float(n1/20);
            c=(n2*a)*7;
            d=" Bir haftalık sigara maliyetiniz : {0} TL".format(c)

            
            
            
           

    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/sigara.html",{'c':c,'n1':n1,'n2':n2,'d':d})
    
def su(request):
    c=''
    n1=''
    y=''
    y2=''
    
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
           
            
            c=n1*0.03;
            y2="Kilonuz {0} kgdir, ""bu kiloya uygun günlük su tüketimi {1} litredir.".format(n1,c)
            y="NOT: Burada belirtilen günlük su ihtiyacınızın bir kısmını yemeklerden alıyorsunuz. Bu nedenle burada belirtilenden daha az miktarda su içmeniz yeterli olacaktır."
            
            
            
           
        
    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/su.html",{'c':c,'n1':n1,'y2':y2,'y':y,})
    
def uslus(request):
    c=''
    n1=''
    n2=''
    a=''

    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            
            c=pow(n1,n2);
            a="{0} sayısının {1}. kuvveti = {2}".format(n1,n2,c)
        
        
        
            
           
    
    except:
         c="hatalı sayı girdiniz."

 
    return render(request,"home/uslus.html",{'c':c,'n1':n1,'n2':n2,'a':a})
    
def vucuty(request):
    c=''
    n1=''
    n2=''
    a=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            
            c=((pow(n2,0.425))*(pow(n1,0.725))*0.007184);
            a="Vücut yüzey alanınız {0} m2'dir" .format(round(c,1))
        
            
           
        c= round(c,2)
    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/vucuty.html",{'c':c,'n1':n1,'n2':n2,'a':a,})

# HATALI
def yas(request):
    
    return render(request,'home/yas.html',)

def yds(request):


    c=''
    n1=''
    a=''
    b=''
    d=''
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            
            
            c=n1*(1.25);
            
            a="YDS Net Sayısı = {0}".format(n1)
            b="YDS Puanı = {0}".format(c)
            if c>55:d="Barajı geçtiniz"
            else:d="Barajı geçemediniz"

    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/yds.html",{'c':c,'n1':n1,'a':a,'b':b,'d':d})

def yuzde(request):
    c=''
    n1=''
    n2=''
    a=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            
            c=((n1*n2)/100);
            a="{0} sayısının yüzde {1} kadarı {2} sayısına eşittir.".format(n1,n2,c)
            
        

    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/yuzde.html",{'c':c,'n1':n1,'n2':n2,'a':a,})

def zam(request):
    c=''
    n1=''
    n2=''
    a=''
    b=''
    d=''
    e=''
    f=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            c=(n1*(100+n2))/100;
           
            a="Normal Fiyat : {0} TL".format(n1)
            b="Zam Tutarı : {0} TL".format((c-n1))
            d="Zamlı Fiyat : {0}".format(c)
            e="Zam Oranı : % {0}".format(n2)
            f="Fiyatı {0} TL olan ürünün % {1} zamlı fiyatı {2} TL'dir.".format(n1,n2,c)
            
           

    except:
        c="hatalı sayı girdiniz."


   
    return render(request,"home/zam.html",{'c':c,'n1':n1,'n2':n2,'a':a,'b':b,'d':d,'e':e,'f':f,})




    




            






