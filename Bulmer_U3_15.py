# Mark Bulmer - CIS 115 - 6-16-2021

noseconds=input('# of seconds: ')
time=int(noseconds)
days=int(time//86400)
a=time/86400-days
b=a*86400

hours=int(b//3600)
c=b/3600-hours
d=c*3600

minutes=int(d//60)
e=(d/60)-minutes
f=int((e+.0000001)*60)

seconds=int(f//1)

print(days, "days," ,hours, "hours," ,minutes, "minutes," ,seconds, "seconds.")
    
