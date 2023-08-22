# Objectives:
# Practice writing functions and looping over dictionaries
# Achieve a better understanding of how to traverse through a list of dictionaries
# or through a dictionary of lists

# 1 Update Values in Dictionaries and Lists:

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
for val in x:
    for i in range (len(val)):
       if 10 == val[i]:
          val[i] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

# 2 Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key 
# and the associated value. For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary(students):
    text = ''
    for val in students:
        text += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return text
print(iterateDictionary(students))

# 3 Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example,
# iterateDictionary2('first_name', students) should output:

def iterateDictionary2(some_list):
    text =''
    for val in some_list:
        text += f"{val['first_name']}\n"
    return text
print(iterateDictionary2(students))

# 4 Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list.

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_list):
    text =''
    for key in some_list:
        print(len(some_list[key]),key)
        for val in some_list[key]:
            print(val)
printInfo(dojo)

