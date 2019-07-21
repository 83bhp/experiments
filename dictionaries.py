student = {'name': 'Pritam', 'age': 35, 'class': 'compsci', 'marks': 69, 'subjects':['history','physics','electronics']}

print(student)
print(student.values())
print ("\nstudent[subjects]: {0}".format(student['subjects']))
print("\nstudent[age]: {0}".format(student.get('age')))
age = student.pop('age') #remove age key value
print("\nStudent after poping the age kv")
print(student)

print("\nStudent.items(): {0}".format(student.items()))

for k, v in student.items():
  print("\n[k:v]:{0}{1}".format(k,v))

print("\n Using update function")
st1 = {'name1': 'Sharayu'}
student.update(st1)
st1.update(student)
print(student)
print(st1)

print("\n Using fromkeys function")
student1 = {'name': 'Pritam1', 'age': 351, 'class': 'compsci1', 'marks': 691, 'subjects':['history1','physics1','electronics1']}
class1 = dict.fromkeys(student, student1)
print(class1)
print("\n deleting subjects from student dictionary")
del student['subjects']
print(student)

print("\n Clearing dict elements")
student.clear()
print(student)

StarWars = ['Luke', 'Vader', 'Rey', 'Yoda']
StarTrek = ['Spock', 'Loki']
universe = dict.fromkeys(StarWars, StarTrek)
universe1 = { key : list(StarTrek) for key in StarWars }
print("\nuniverse:{0}".format(universe))
print("\nuniverse1:{0}".format(universe1))
StarTrek.append('James')
print(StarTrek)

#pillar = {'eoscore':'ceph', 'ha':'hare', 'provisioner':'chef'}
pillar = {'eoscore':'ceph', 'ha':'hare', 'hw': ['pods', 'gallium']}
config = {'eoscore':'mero', 'ha':'halon', 'provisioner':'salt', 'load_balancer':'haproxy', 'hw': ['vm', 'vagrant', 'sati']}

print("pillar{0}".format(pillar))
print("config{0}".format(config))

print("Merging two dictionaries")

print("Classic pythonic way")
m1 = config.copy()
m1.update(pillar)
print("pillar{0}".format(pillar))
print("config{0}".format(config))
print("m1{0}".format(m1))
