#Harry Vines
#22/09/2014
#Currency Extension


print("This program will tell you how many £20,£10,£5,£2's and £1's go into a certain amount")
amount = int(input("Please enter the amount: "))
div_result1 = amount//20
mod_result = amount%20
div_result2 = mod_result//10
mod_result = mod_result%10
div_result3 = mod_result//5
mod_result = mod_result%5
div_result4 = mod_result//2
mod_result = mod_result%2
div_result5 = mod_result//1

print("The amount of £20's that go into {0} is {1}, The amount of £10's is {2}, The amount of £5's is {3}, The amount of £2's is {4} and the amount of £1's is {5}".format(amount,div_result1,div_result2,div_result3,div_result4,div_result5))
