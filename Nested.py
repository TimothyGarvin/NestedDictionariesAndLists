x = [ 
    [5,2,3], #index 0
    [10,8,9]  #index 1
    ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

students[0]['last_name'] = 'Bryant'

sports_directory['soccer'][0] = 'Andres'

z[0]['y'] = 30

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'}, #index 0
        {'first_name' : 'John', 'last_name' : 'Rosales'}, #index 1
        {'first_name' : 'Mark', 'last_name' : 'Guillen'}, #index 2
        {'first_name' : 'KB', 'last_name' : 'Tonel'} #index 3
    ]

def iterateDictionary(list):
    for i in range (len(list)):
        print(f"First Name:" ,list[i]['first_name'] ,". Last Name:", students[i]['last_name'], ".")


iterateDictionary(students)

def iterateDictionary2 (key,list):
    for i in range (len(list)):
        print(students[i][key])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for i in (dict):
        print(len(dict[i]), i)
        print(*dict[i], sep= ", ")

printInfo(dojo)