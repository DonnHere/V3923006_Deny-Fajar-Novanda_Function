#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fpb(a, b):
    while b:
        a, b = b, a % b
    return a

def kpk(a, b):
    return a * b // gcd(a, b)

print("Pilihan:")
print("1. FPB")
print("2. KPK")
print("3. Other")

while True:
    choice = int(input("Masukkan pilihan anda (1/2/3): "))

    if choice == 1:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        print("Hasil FPB dari", a, "dan", b, "adalah", fpb(a, b))
        break

    elif choice == 2:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        print("Hasil KPK dari", a, "dan", b, "adalah", kpk(a, b))
        break

    elif choice == 3:
        print("Program dihentikan.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


# In[ ]:





# In[ ]:




