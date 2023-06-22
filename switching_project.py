import math
size=eval(input("city size: "))
density=eval(input("enter the population desity in KM2: "))
lamda=eval(input("enter average number of calls per user: "))
duration=eval(input("enter the average call duration in seconds: "))
channels=eval(input("enter the number of channels: "))
max_channels=eval(input("enter the maximum number of channels: "))
Pb=eval(input("enter the blocking probability: "))
ci=eval(input("enter the interference ratio: "))
tdm=eval(input("enter the TDM slots: "))
sectoring_level=eval(input("choose a sectoring level(10,120,180,360): "))
n=360/sectoring_level
N=(ci*n)/3
cluster_number=(size*density)/(max_channels*math.sqrt(3))
channels_cluster=channels/cluster_number
Number_trunks=math.floor((channels_cluster/N)*tdm)
a_user=lamda*duration
Number_trunks_sectoring=Number_trunks*n


def erlang(A, m):
    L = (A ** m) / math.factorial(m)
    sum_ = 0
    for n in range(m + 1): sum_ += (A ** n) / math.factorial(n)
    block=(L / sum_)
    return block 
    
    
def a_cell(Pb, Number_trunks_sectoring):
    left = 0
    right = 1000

    while True:
        mid = (left + right) / 2
        b = erlang(mid, Number_trunks)
        if abs(b - Pb) < 0.0001:
            return mid
        elif b > Pb:
            right = mid
        else:
            left=mid

a_cell=(a_cell(Pb, Number_trunks_sectoring))/n
subs_cell=a_user/a_cell
total_subs=size/density
total_cells=total_subs/subs_cell
print(total_cells)