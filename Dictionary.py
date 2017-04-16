person=dict(Name="hussein",Age=27,Salary=80000) # mutable
print(person)
print(person["Name"])
print("update name")
person["Name"]="Hussein Alrubaye"
print(person["Name"])
print("add Insurance key")
person["Insurance"]="Yes"
print(person)
print("delete age")
del person["Age"]
print(person)
#print Salary
print(person["Salary"])

