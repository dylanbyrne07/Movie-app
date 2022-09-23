name_searched_not_encoded = "Jack Reacher"
name_searched_words = name_searched_not_encoded.split()
name_searched = ""
for word in name_searched_words:
    name_searched = name_searched + word + "+"
name_searched = name_searched.rstrip(name_searched[-1])
print (name_searched)

