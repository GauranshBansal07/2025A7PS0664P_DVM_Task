class Path:
    @staticmethod
    def shortest_path(start, end, stations_dict, lines_dict):
        travel = [(start, [start], [stations_dict[start].lines[0]])]
        while travel:
            current, path, path_lines = travel.pop(0)
            if current == end:
                return path, path_lines
    
            for line_name in stations_dict[current].lines:
                stations_on_line = lines_dict[line_name]
                index = stations_on_line.index(current)
    
                neighbours = []
                if index > 0:
                    neighbours.append(stations_on_line[index - 1])
                if index < len(stations_on_line) - 1:
                    neighbours.append(stations_on_line[index + 1])
    
                for neighbour in neighbours:
                    if neighbour not in path:
                        new_lines = path_lines + [line_name]
                        travel.append((neighbour, path + [neighbour], new_lines))
    
    @staticmethod                    
    def compute_fare(path):
        cost = "CA$" +  str(len(path)-1)
        return cost
