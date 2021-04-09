data_scientist = {
    "Name" : None,
    "Age" : None,
    "Years" : None
}

data_scientist["Name"] = input("Please enter you name: ")
data_scientist["Age"] = input("Please enter you age: ")
data_scientist["Years"] = input("How long have you been coding? ")

print(data_scientist)


first_languages = input("Enter the first three programming language you have learned (separated by commas): ")
lang_list = first_languages.split(",")
lang_tuple = tuple (lang_list)

data_scientist["First Languages"] = lang_tuple


fav_lang = input("Enter your favorite programming languages: ")
fav_list = fav_lang.split(",")
data_scientist["Favorite Languages"] = fav_list


first_set = set(lang_list)
fav_set = set(fav_list)
consistant_fav = first_set.intersection(fav_set)
data_scientist["Consitant Favorites"] = consistant_fav

print(data_scientist)