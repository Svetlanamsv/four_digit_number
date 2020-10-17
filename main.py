print("Enter four-digit number: ", end=" ")
a=int(input())
a_th=a//1000
print(a_th)
a_h=(a%1000)//100
print(a_h)
a_dez=((a%1000)%100)//10
print(a_dez)
a_num=((a%1000)%100)%10
print(a_num)

