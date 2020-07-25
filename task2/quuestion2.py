# Solution of Question2
# No any input validations.
# Usage: $python3 question2.py
# Enter number of strings you will entered in the first line.
# Enter strings line by line starting from the second line.
# =============
# Example input:
# Number of strings you will entered: 2
# ababaa
# aa
# =============
# getPrefixes gets a string, and returns the list of its prefixes.
def getPrefixes(string):
    counter = 0
    result = []
    while counter < len(string):
        result.append(string[counter : len(string) + 1])
        counter += 1
    return result
# findSimilarity gets two strings, and returns the number of matched prefixes of two.
def findSimilarity(first, second):
    result = 0
    counter = 0
    while counter < len(first) and counter < len(second):
        if first[counter] == second[counter]:
            result += 1
        else:
            break
        counter += 1
    return result
# calculateSumOfString gets a string, and calculate the total similarity result with its prefixes.
def calculateSumOfString(string):
    prefixes = getPrefixes(string)
    result = 0
    for prefix in prefixes:
        result += findSimilarity(string, prefix)
    return result

# main calls calculateSumOfString n times where n will be the number of strings you will entered.
def main():
    n = int(input('Number of strings you will entered: '))
    stringList = []
    for i in range(n):
        stringList.append(input())
    # we get the strings above part, now calculate similarities for each below.
    print("== OUTPUT == ")
    for string in stringList:
        print(calculateSumOfString(string))
main()
