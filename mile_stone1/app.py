movies = []

'''
movie = {
   'name' .. (str)
'''


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print("Stopping program...")
        else:
            print("Unknown command-please try again. ")
        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the Director name: ")
    year = input("Enter the Year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")


def find_movie():
    find_by = input("what part of the movie u are looking for: ")
    looking_for = input("what are u searching for? ")

    found_movies = find_by_attribute(movies, looking_for,lambda x: x[find_by])

    show_movie(found_movies)


def find_by_attribute(items,expected,finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found

menu()
print(movies)

