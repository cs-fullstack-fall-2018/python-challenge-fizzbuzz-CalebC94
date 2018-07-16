import os

os.system("clear")


# If the current number is evenly divisible by 3 you should print "FIZZ" and the number
# If the current number is evenly divisible by 5 you should print "BUZZ" and the number
# If the current number is evenly divisible by both 3 and 5 you should print "FIZZBUZZ"
#  and the number BOTH to the screen and to the file 'fizzbuzz.txt'
# Otherwise, just print the number

my_file = open("FIZZBIZZ.txt", "w+")

evenNumber = int(input("What number?"))

for num in range(evenNumber):
    if num%3==0 and num%5==0:
        my_file.write(str(num)+ "\n")
        print("FIZZBIZZ", num)
    elif num%3==0:
        print("FIZZ:", num)
    elif num%5==0:
        print("BIZZ:", num)
    else:
        print(num)


#num%3==0 and num%5==0 must start at the beginning of if/else statement to be true