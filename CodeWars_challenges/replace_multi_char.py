import re
string = "There is a troll coming!"
string = re.sub('[aeiouAEIOU]', '', string)
print(string)