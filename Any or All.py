# Enter your code here. Read input from STDIN. Print output to STDOUT

N= int(input())
a=input().split()
print(all(int(i)>=0 for i in a) and any(i==i[::-1] for i in a))
