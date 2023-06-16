import networkx as nx
import matplotlib.pyplot as plt
import csv




def edit_database():
    edgelist = []
    with open('cities.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            str = row[0]
            edgelist.append(str.split(';'))
    return edgelist



def create_graph():
    g = nx.Graph()
    for edge in edit_database():
        g.add_edge(edge[0], edge[1], weight = int(edge[2]))
    return g

def show_database():
    pos = nx.spring_layout(create_graph())
    nx.draw_networkx(create_graph(), pos)
    plt.title('Map of Ukraine')
    plt.show()


def shortest_way():
    start_point = input('Enter start point: ')
    end_point = input('Enter end point: ')
    print("Shortest route: ", nx.shortest_path(create_graph(),start_point, end_point, weight='weight'))
    print("Route distance: ", nx.shortest_path_length(create_graph(),start_point, end_point, weight='weight'))


def main():
    shortest_way()
    show_database()

if __name__ == "__main__" :
    main()
