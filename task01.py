import re
txt = "Today is our first day learning Regex"
search_text = re.search("^Today.*Regex$",txt)

if search_text:
  print("match!")
else:
  print("No match")