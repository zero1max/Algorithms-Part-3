# Task 1

baxo = {
    'subjects': {
        'math': 4,
        'english': 5,
        'python': 5
    }
}

baxo2 = {
    'subjects': {
        'math': 5,
        'english': 5,
        'python': 5
    }
}

baxo['subjects']['math']=5
# Task 2
baxo['subjects']['ona tili'] = 5
# Task 3
for fan, grade in baxo['subjects'].items():
    print(f"{fan}: {grade}")
#Task 4
print(baxo == baxo2)

# print(baxo)