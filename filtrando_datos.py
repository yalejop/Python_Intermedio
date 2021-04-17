DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    all_python_devs2 = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs2 = list(map(lambda worker: worker['name'], all_python_devs2))

    all_Platzi_workers2 = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_Platzi_workers2 = list(map(lambda worker: worker['name'], all_Platzi_workers2))

    adults2 = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_people2 = [worker['name'] for worker in DATA if worker['age'] > 70]



    # for worker in old_people:
    #     print(worker)

    for worker in all_python_devs2:
        print(worker)


    for worker in all_Platzi_workers2:
        print('\n' + worker)

    for worker in adults2:
        print(worker)

    for worker in old_people2:
        print('\n' + worker)

if __name__ == '__main__':
    run()
