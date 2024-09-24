# Task 1

movie = {
    'movies_name':{
        "Qashqirlar makoni":{
            "Bosh rollarda":{
                "name": "Polat Alemdar",
                "name": "Memati Bash",
                "name": "Elif Aygul"
            },
            "Kino yili": 2006,
            "Davlati": 'Turkiya',
            "Til": "Turkish"
        },
        "Chuqur":{
            "Bosh rollarda":{
                "name": "Yamach Kochavali",
                "name": "Selim Kochavali",
                "name": "Salih Kochavali"
            },
            "Kino yili": 2020,
            "Davlati": 'Turkiya',
            "Til": "Turkish"
        },
        "Yunus Emro": {
            "Bosh rollarda":{
                "name": "Yunus afandi",
                "name": "Toptiq Emro"
            },
            "Kino yili": 2022,
            "Davlati": 'Turkiya',
            "Til": "Turkish"
        }
    }
}
# Task 2
# print(movie.get("movies_name"))

# Task 3
# for name, description in movie['movies_name'].items():
#     description.setdefault('Til', "O'zbek")

# print(movie['movies_name'])
# Task 4
# movie_copy = movie.copy()

# print(movie_copy)

# Task 5
# chuqur_film = movie['movies_name']['Chuqur'].pop('Kino yili')
# print(f"'Chuqur' filmidagi 'Kino yili' o'chirildi: {chuqur_film}")

# oxirgi_element = movie['movies_name'].popitem()
# print(f"Oxirgi film o'chirildi: {oxirgi_element}")

# print(movie)
# Task 6
# movie['movies_name'].clear()

# print(movie['movies_name'])  

# Task 7
# print("Nusxalangan lug'at:")
# print(movie_copy)
