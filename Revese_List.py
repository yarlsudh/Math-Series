a = [1,2,3,4,5,6,7,8,9,10]
print(len(a))

def reverse_the_list(a):
   reversed_list = []
   for i in range(0, len(a)):
     reversed_list.append(a[len(a) - i - 1])
   return reversed_list

new_list = reverse_the_list(a)
print (new_list)