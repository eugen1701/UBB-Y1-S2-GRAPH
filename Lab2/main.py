from graph import Graph


def read_from_file():
    with open("readfile.txt", "r") as file:
        line = file.readline()
        line = line.split(" ")
        vertices = int(line[0])
        edges = int(line[1])
        graph = Graph(vertices)
        for line in file:
            line = line.split(" ")
            graph.insert_new_edge(int(line[0]), int(line[1]), int(line[2]))
        return graph


def print_menu():
    print(
        "1. Add Edge\n"
        "2. Print Graph\n"
        "3. Remove Vertex\n"
        "4. Insert Vertex\n"
        "5. Delete Edge\n"
        "6. Check if Edge Exists\n"
    )


def read_command():
    graph = read_from_file()
    print_menu()
    while True:
        read_value = input("Enter Option: ")
        if read_value == "1":
            source_vertex = int(input("Enter Source vertex:"))
            target_vertex = int(input("Enter Target vertex:"))
            edge_value = int(input("Enter Edge value: "))
            if graph.has_edge(source_vertex, target_vertex):
                print("Already has edge!")
                continue
            graph.insert_new_edge(source_vertex, target_vertex, edge_value)
        elif read_value == "2":
            print(graph.count_vertex())
            for vertex in graph.get_vertex_iterator():
                for outbound_edge in vertex.get_outbound_iterator():
                    print(outbound_edge.source.id, outbound_edge.target.id, outbound_edge.value)
        elif read_value == "3":
            vertex_to_remove = int(input("Enter Vertex to remove: "))
            graph.remove_vertex(vertex_to_remove)
        elif read_value == "4":
            graph.insert_vertex()
            print("New Vertex Inserted\n")
        elif read_value == "5":
            source_vertex = int(input("Enter Source vertex:"))
            target_vertex = int(input("Enter Target vertex:"))
            if not graph.has_edge(source_vertex, target_vertex):
                print("Doesn't have edge to remove")
                continue
            graph.delete_edge(source_vertex, target_vertex)
        elif read_value == "6":
            source_vertex = int(input("Enter Source vertex:"))
            target_vertex = int(input("Enter Target vertex:"))
            if not graph.has_edge(source_vertex, target_vertex):
                print("Doesn't have edge")
            else:
                print("Graph has edge")


read_command()
