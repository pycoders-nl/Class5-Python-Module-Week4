import re

def vali():
    while True:
        pw = input('enter your password:')
        nummer = re.search(r'\d+', pw)
        kucuk_harf =  re.search(r'[a-z]+', pw)
        buyuk_harif= re.search(r'[A-Z]+', pw)
        ozel_karakter=re.search(r'[@#$]+', pw)
        if (len(pw)<6 or len(pw)>16):
            print('sifre 6~16 hane arasi olmali')
        elif nummer == None:
            print('en az bir sayi olmali')
        elif kucuk_harf ==None:
            print("enz az bir kucuk harif olmali")
        elif buyuk_harif==None:
            print("enz az bir buyuk harif olmali")
        elif ozel_karakter == None:
            print("enz az bir ozel karakter olmali")
        else:
            print('tebrikler guclu bir sifre olusturdunuz')
            break

vali()
