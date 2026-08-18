import time,random
from tabulate import tabulate
def merge_sort(arr):
    if len(arr)<=1:return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left)and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def quick_sort(arr):
    if len(arr)<=1:return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
def time_complexity_test():
    sizes=[100,500,1000]
    results=[]
    print("TIME COMPLEXITY ANALYSIS: Merge Sort vs Quick Sort")
    print("="*60)
    for n in sizes:
        data_best=list(range(n))
        data_avg=[random.randint(1,n*2)for _ in range(n)]
        data_worst=list(range(n,0,-1))
        t1=time.time()
        merge_sort(data_avg.copy())
        t_merge=time.time()-t1
        t2=time.time()
        quick_sort(data_best.copy())
        t_quick_best=time.time()-t2
        t3=time.time()
        quick_sort(data_avg.copy())
        t_quick_avg=time.time()-t3
        t4=time.time()
        quick_sort(data_worst.copy())
        t_quick_worst=time.time()-t4
        results.append([n,f"{t_merge:.4f}s",f"{t_quick_best:.4f}s",f"{t_quick_avg:.4f}s",f"{t_quick_worst:.4f}s"])
    print(tabulate(results,headers=["Size(n)","Merge Sort","Quick Best","Quick Avg","Quick Worst"],tablefmt="grid"))
    print("\nNOTATION MEANING:")
    print("• O=Upper bound (Worst case)")
    print("• Ω=Lower bound (Best case)")
    print("• Θ=Tight bound (Average case)")
if __name__=="__main__":
    time_complexity_test()
