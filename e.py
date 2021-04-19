c="*" ; z=10
for i in range(z): print((c*(i+1)).ljust(z-1))
for i in range(z-1,-1,-1): print((c*(i+1)).ljust(z-1))