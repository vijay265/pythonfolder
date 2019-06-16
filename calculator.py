print("calculator")
print("enter what operation to perform +,-,*,/,%,**//")
a=(input())
print("enter first no.")
b=float(input())
print("enter second no.")
c=float(input())
if a=='+':
    print(b,'+',c,"=",b+c)
elif a=='-':
    print(b,'-',c,"=",b-c)
elif a=='*':
    print(b,'*',c,"=",b*c)
elif a=='/':
    print(b,'/',c,"=",b/c)
elif a=='%':
    print(b,'%',c,"=",b%c)
elif a=='**':
    print(b,'**',c,"=",b**c)
elif a=='//':
    print(b,'//',c,"=",b//c)
else:
    print("wrong operator")