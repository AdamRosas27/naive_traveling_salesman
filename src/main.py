""" Adam Rosas CSC 401: Assignment - Traveling Salesman Problem """

from itertools import permutations

# Create a main class that will be used to hold my routes function, my function that executes the traveling salesman algorithm, and my main function that will run the program


class Main:

    # Create function that will determine each possible route and holds some key logic for determining the shortest route

    # Should take in the adj_matrix and the route as parameters
    def distances(self, route, adj_matrix):
        # Initialize a variable that will hold the total distance of the route
        total_distance = 0

        # Create a for loop that will iterate through the route and add the distance between each city to the total distance
        for i in range(len(route) - 1):
            total_distance += adj_matrix[route[i]][route[i + 1]]
        # Return to the starting city
        total_distance += adj_matrix[route[-1]][route[0]]
        return total_distance

# Create a helper function that will receive the possible routes from the routes method and execute the traveling salesman algorithm
    def tsp(self, distances, adj_matrix):

        # Initialize some variables that will be used to hold the best route and all possible routes using permutations from the itertools library

        shortest_route = None
        cities = len(adj_matrix)
        all_routes = permutations(range(cities))

        # Add a for loop that will go through all the possible routes in all_routes and call the distance function to determine the shortest route
        for route in all_routes:
            # If the shortest route is still uninitialized then it will be set to the first route in all_routes
            if shortest_route == None:
                shortest_route = route
            else:
                # Otherwise, call the distance function to determine the shortest route and then update the shortest_route variable to represent the new value
                if distances(route, adj_matrix) < distances(shortest_route, adj_matrix):
                    shortest_route = route
        return shortest_route

# Create a main function that will run the program
    def main(self):

        # Add my 2D matrix that will represent my graph and the elements within will represent the distance between each city
        adj_matrix = [
            [0, 0, 3, 0, 2, 10],
            [0, 0, 0, 0, 15, 1],
            [3, 0, 0, 7, 6, 0],
            [0, 0, 7, 0, 2, 0],
            [2, 15, 6, 2, 0, 4],
            [10, 1, 0, 0, 4, 0]
        ]

        # Call the tsp function to execute the traveling salesman algorithm
        shortest_possible_route = self.tsp(self.distances, adj_matrix)
        route_distance = self.distances(shortest_possible_route, adj_matrix)
        # Print the shortest route
        print(f"Shortest Route: {shortest_possible_route}")
        # Print the distance of the shortest route
        print(f"Distance: {route_distance}")


if __name__ == "__main__":
    main = Main()
    main.main()
