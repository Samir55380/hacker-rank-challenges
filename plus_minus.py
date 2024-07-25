arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(round((positive / len(arr)), 6))
    print(round((negative / len(arr)), 6))
    print(round((zero / len(arr)), 6))
    
plusMinus(arr)