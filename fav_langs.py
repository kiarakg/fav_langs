# create a dictionary with "Name", "Age", and "Years" keys
data_scientist = {
    "Name" : None,
    "Age" : None,
    "Years" : None
}

data_scientist["Name"] = input("Please enter you name: ")
data_scientist["Age"] = input("Please enter you age: ")
data_scientist["Years"] = input("How long have you been coding? ")

print(data_scientist)


# Prompt the user to enter their first three programming languages
#   - store them as a tuple ()
first_languages = input("Enter the first three programming language you have learned (separated by commas): ")
lang_list = first_languages.split(",")
lang_tuple = tuple (lang_list)

data_scientist["First Languages"] = lang_tuple


# Prompt the user to enter their three favorite programming languages
#   - store them as a list []
fav_lang = input("Enter your favorite programming languages: ")
fav_list = fav_lang.split(",")
data_scientist["Favorite Languages"] = fav_list


# Create a set that is an intersection of their first programming languages
# and their favorite programming languages
first_set = set(lang_list)
fav_set = set(fav_list)
consistant_fav = first_set.intersection(fav_set)
data_scientist["Consitant Favorites"] = consistant_fav

# Add all of these collections as keys to the dictionary created
#   - format a print statement to print the relevant data to the console
print(data_scientist)