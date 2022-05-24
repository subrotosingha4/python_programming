ls_dict={'name1':'subroto','name2':'priyangka','name3':'singha','name4':'roy'}
#use tuple unpacking to print out key and value from dictionary
for key,name in ls_dict.items():
    print(key,name)

#use in to see if a key exists in a dictionary

if 'name1' in ls_dict:
    print('Subroto is there')
else:
    print('Subroto is not there')

#if you want to check the values
if 'Subroto' in ls_dict.values():
    print('Subroto is there')
else:
    print('Subroto is not there')