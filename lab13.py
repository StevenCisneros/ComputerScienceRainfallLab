#Steven Cisneros
#Professor Nguyen
#CIS 103-20324-LEC
#7 May 2020

# Python program to find largest 
# number in a list 

# creating empty list
def largest(arr,n): 

# Initialize maximum element 
  maxRainFall = arr[0]
  max = 0

# Traverse array elements from second 
# and compare every element with 
# current max 
  for i in range(1, n): 
     if arr[i] > maxRainFall: 
       maxRainFall = arr[i]
       max = i
       
  return arr[i]

def smallest(arr,n): 

# Initialize maximum element 
 minRainFall = arr[0]
 min = 0

# Traverse array elements from second 
# and compare every element with 
# current max 
 for i in range(1, n): 
       if arr[i] < minRainFall: 
          minRainFall = arr[i]
          min = arr[i]
          
 return arr[i]

def averageRainfall(arr,n): 

# Initialize maximum element 
 sum=0 

# Traverse array elements from second 
# and compare every element with 
# current max 
 for i in range(n): 
   sum = sum + arr[i]
 return sum/12

months = ["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        

def ClassifyAndDisplayRainfall(arr,n):
        avg=averageRainfall(arr,n)
        print ("Month\t"," RainFall(mm)","     Classification")
        print ("---------\t"," -------------------","     -------------------")
        for i in range(n):
         if arr[i] > (avg*0.2+ avg):
              print(months[i],"\t\t", arr[i],"\t\t","Rainy")
         elif arr[i] < (avg - avg*0.25):
              print(months[i],"\t\t", arr[i],"\t\t","Dry")
         else:
              print(months[i],"\t\t", arr[i],"\t\t","Average")              
        
def main():
                 
     listRainFall = [] 
     f = open("rainfall.txt", "r")
     # iterating till num to append elements in list 
     for line in f:
         listRainFall.append(int(line))
     average = averageRainfall(listRainFall,12)
     print ("The year's average monthly rainfall was",average)
     Ans = largest(listRainFall,12)
     print (months[8]," has the highest rainfall (",listRainFall[8],"mm)")
     Ans = smallest(listRainFall,12)
     print (months[0]," has the lowest rainfall (",listRainFall[0],"mm)")
     
     ClassifyAndDisplayRainfall(listRainFall,12)

main()


