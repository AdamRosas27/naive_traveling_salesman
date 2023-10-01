# Create a main class that will be used to hold my routes function, my function that executes the traveling salesman algorithm, and my main function that will run the program
class Main:

    # Create function that will determine each possible route and holds some key logic for determining the shortest route
    def routes(self):
        pass

# Create a helper function that will receive the possible routes from the routes method and execute the traveling salesman algorithm
    def tsp(self):

        # Add my 2D matrix that will represent my graph and the elements within will represent the distance between each city
        adj_matrix = [
            [0, 0, 3, 0, 2, 10],
            [0, 0, 0, 0, 15, 1],
            [3, 0, 0, 7, 6, 0],
            [0, 0, 7, 0, 2, 0],
            [2, 15, 6, 2, 0, 4],
            [10, 1, 0, 0, 4, 0],
        ]

# Create a main function that will run the program
    def main(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.main()
