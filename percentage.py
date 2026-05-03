print("please enter the test scores for the following 4 tests: ")

math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("sum of maths, english, science and hindi: ", sum)

percentage = (sum/400)*100

print(end="percentage mark = ")
print(percentage)