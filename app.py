MENU_PROMPT = "\n Enter 'a' to add movie, 'f' to find movie, 'l' to show movie or 'q' to quit: "
movies = []


def add_movies():
    title = input(f"Enter the movie name: ")
    director = input(f"Enter the movie director: ")
    year = input("Enter the release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    search_title = input("Enter the title of the movie: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


def menu():
  selection = input(MENU_PROMPT)
  while selection != 'q':
        if selection == 'a':
            add_movies()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Known command. Please try again")

        selection = input(MENU_PROMPT)

menu()