import timeit
import matplotlib.pyplot as plt

def Input(Array,n):
    for i in range(0,n):
        ele=int(input("ele: "))
        Array.append(ele)

def lin_search(Array,key):
    for x in Array:
        if x==key:
            return True
    return False

N=[]
CPU=[]
trail=int(input("enter number of trails"))
for t in range(0,trail):
    Array=[]
    print("-->trail no:",t+1)
    n=int(input("enter number of elements"))
    Input(Array,n)
    print(Array)
    key=int(input("enter the key to search"))
    start=timeit.default_timer()
    s=lin_search(Array,key)
    print('element found=',s)
    times=timeit.default_timer()-start
    N.append(n)
    CPU.append(round(float(times)*1000000,2))
print("N CPU")
for t in range(0,trail):
    print(N[t] , CPU[t])

plt.plot(N, CPU)
plt.scatter(N,CPU,color="red",marker="*",s=50)
plt.xlabel("ARRAY SIZE N")
plt.ylabel("CPU RUN TIME")
plt.title("LINEAR SEARCH TIME EFFICIENCY")
plt.show()


