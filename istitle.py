
string = 'I want to Go to out as the Weather is amazing'
string_split = string.split(' ')
# .istitle() checks words start with capital letter

print([w for w in string_split if w.istitle()])