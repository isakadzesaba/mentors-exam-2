#  Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.

# ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"

def longest_prefix(stri):
    if not stri:
        return ""
    prefix = stri[0] # პირველი სტრინგი რო გამოიყენოს პრეფიქსად

    for i in stri[1:]:# აქ რო შეადაროს პრეფიქსი ყველა სხვა  სტრინგთან :))             
        while not i.startswith(prefix):  # ამცირებს პრეფიქსის სიგრძეს სანამ არ გაუტოლდება ამ სტრინგის დასაწყისს
            prefix = prefix[:-1] # აქ პრეფიქსიდან ბოლო "ჩარაქთერი" პრეფიქსიდანნ 
            if not prefix:
                return "" # თუ პრეფიქსი არ აქ
            
    return prefix # ამას რათუნდა ახსნა ;დდ

print(longest_prefix(["flower", "flow", "flight"]))  #test casee
print(longest_prefix(["dog", "racecar", "car"]))  #test casee
print(longest_prefix(["apple", "apple", "apple"]))   #test casee

# AFK 5 min