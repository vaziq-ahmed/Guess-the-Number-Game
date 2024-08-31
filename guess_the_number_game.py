import random
n = random.randint(0,100);

a = -1

no_guess = 0
while(n!=a):
    no_guess+=1
    a = int(input("Guess the number(number is between 0 and 100)"));
    if(a>n):
        print("Your guess is too high, lower number please");
    elif(a<n):
        print("Your  guess is too low, higher number please");
        
print(f"Yayy..! You Guessed the number {n}");
print(f"You took {no_guess} attempts");
print("Thank you...");