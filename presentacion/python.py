class Students:
    def __init__(self, names):
        self.names = names
    
    def count(self):
        return len(self.names)
    
    def __str__(self):
        return ', '.join(self.names)

names = ['Alice', 'Bob', 'Charlie']
students = Students(names)

print(students.count())  # Output: 3
print(students)  
