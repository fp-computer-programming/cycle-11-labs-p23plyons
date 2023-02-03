#There was not a single function I have written for this class or in general that I needed 15 lines for so I took these from code wars

#1
def nearest_sq(n):
    if n == 1 or n == 2:
        return 1
    if n%2==0:
        temp1 = n/2
    else:
        temp1 = (n+1)/2
    temp2 = 0
    temp3 = 0
    while 1:
        if temp1*temp1 >= n:
            temp2 = temp1
        else:
            while 1:
                temp0 = temp2 - temp1
                if temp0 == 1:
                    break
                if temp0%2==0:
                    temp3 = temp0/2 + temp1
                else:
                    temp3 = (temp0+1)/2 + temp1
                if temp3*temp3 > n:
                    if temp3 <= temp1:
                        break
                    temp2 = temp3
                elif temp3*temp3 <n:
                    if temp3 <= temp1:
                        break
                    temp1 = temp3
                else: 
                    return temp3*temp3
            
            if(n - temp1*temp1 >= temp2*temp2 - n):
                return temp2*temp2
            else: 
                return temp1*temp1
        if temp1%2==0:
            temp1 = temp1/2
        else:
            temp1 = (temp1+1)/2

#2
def sum_of_integers_in_string(s):
    result = 0
    current = ""
    for i,char in enumerate(s):
        if i != len(s) - 1:
            if char.isnumeric():
                current += char
            else:
                if len(current) >= 1:
                    result += int(current)
                    current = ""
        else:
            if char.isnumeric():
                if current:
                    current += char
                    result += int(current)
                else:
                    result += int(char)
            else:
                if current:
                    result += int(current)
               
    return result

#3
def solution(number):
    sum=0
    if number%3==0:
        nearest_three=number-3
    else:
        nearest_three=number-(number%3)
    if number%5==0:
        nearest_five=number-5
    else:
        nearest_five=number-(number%5)
    for x in range(nearest_three, 0, -3):
        sum+=x
    for y in range(nearest_five, 0, -5):
        if y%3==0:
            continue
        else:
            sum+=y
    return sum

#4
def find_it(seq):
    passes = 0
    odd_appearance_amount = 0

    answer = 0

    # takes all numbers in the range of the list
    for cardinal_num in range(min(seq), max(seq) + 2):
        passes += 1
        if passes == 2:
            passes = 1

            if not odd_appearance_amount % 2 == 0:
                return answer

            odd_appearance_amount = 0

        # checks if any numbers in the range of the list matches a number in that list
        for num in seq:
            if num == cardinal_num:
                if passes == 1:
                    odd_appearance_amount += 1
                    answer = num

#5
def count_bits(n):
    out=""
    count=0
    while(1):
        div=n//2
        mod=n%2        
        out+=str(mod)
        if(div==0):
            break
        n=div  
    for x in out:
        if x=='1':
            count+=1
        else:
            pass
    return count