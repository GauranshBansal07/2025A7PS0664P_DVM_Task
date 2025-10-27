import csv

from Station import Station
from Ticket import Ticket

def loading_stations_file(filepath):
    station_dict = {}
    with open(filepath, 'r') as stations_file:
        csv_reader = csv.DictReader(stations_file)

        for line in csv_reader:
            station_name = line['station_name']
            line_name = line['line_name']

            if station_name not in station_dict:
                station_dict[station_name] = Station(station_name)
            station_dict[station_name].add_lines(line_name)
    return station_dict

def loading_lines_file(filepath):
    lines_dict = {}
    with open(filepath, 'r') as lines_file:
        csv_reader = csv.DictReader(lines_file)

        for line in csv_reader:
            line_name = line['line_name']
            stations_list = line['stations_list'].split(',')
            lines_dict[line_name] = stations_list
    return lines_dict
