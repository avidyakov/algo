def get_neighbour_coordinates(index: int, coordinates, neighbour_coordinate: int) -> list:
    neighbour_coordinates = list(coordinates)
    neighbour_coordinates[index] = neighbour_coordinate
    return neighbour_coordinates


def get_coordinates_of_neighbors(coordinates, matrix_size) -> list:
    neighbors_coordinates = []
    for index, (coordinate, size) in enumerate(zip(coordinates, matrix_size)):
        neighbour1 = coordinate + 1
        if neighbour1 < size:
            neighbour_coordinates = get_neighbour_coordinates(index, coordinates, neighbour1)
            neighbors_coordinates.append(neighbour_coordinates)

        neighbour2 = coordinate - 1
        if 0 <= neighbour2:
            neighbour_coordinates = get_neighbour_coordinates(index, coordinates, neighbour2)
            neighbors_coordinates.append(neighbour_coordinates)

    return neighbors_coordinates


def get_neighbors(matrix, coordinates, matrix_size) -> list:
    coordinates_of_neighbors = get_coordinates_of_neighbors(coordinates, matrix_size)
    neighbors = []
    for neighbor_x, neighbor_y in coordinates_of_neighbors:
        neighbor = matrix[neighbor_x][neighbor_y]
        neighbors.append(neighbor)

    return neighbors


def main() -> None:
    matrix_size = int(input()), int(input())
    matrix = []
    for _ in range(matrix_size[0]):
        new_line = tuple(map(int, input().split()))
        matrix.append(new_line)
    coordinates = int(input()), int(input())

    neighbors = get_neighbors(matrix, coordinates, matrix_size)
    neighbors.sort()
    print(*neighbors)


if __name__ == '__main__':
    main()
