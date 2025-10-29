import uuid
from Station import Station
from Ticket import Ticket
from loading import Loading
from path import Path
from Ticket import Ticket


def main():
    stations_dict = Loading.loading_stations_file('stations.csv')
    lines_dict = Loading.loading_lines_file('lines.csv')
    tickets_list = []

    while True:
        print("\nOptions:")
        print("1. List all stations")
        print("2. Purchase ticket")
        print("3. View purchased tickets")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            Station.list_stations(stations_dict)

        elif choice == "2":
            start = input("Enter departing station: ").strip()
            end = input("Enter arriving station: ").strip()

            if start == end:
                print("Not possible — departure and destination stations are the same.")
                continue

            if start not in stations_dict or end not in stations_dict:
                print("Invalid station name(s). Please try again.")
                continue

            path, path_lines = Path.shortest_path(start, end, stations_dict, lines_dict)

            ticket_id = str(uuid.uuid4())
            fare = Path.compute_fare(path)
            ticket = Ticket(ticket_id, path, path_lines, fare)
            tickets_list.append(ticket)

            print("\nTicket purchased successfully!")
            Ticket.display(ticket)

        elif choice == "3":
            if not tickets_list:
                print("No tickets purchased yet.")
            else:
                print("\nPurchased Tickets:")

                for i, t in enumerate(tickets_list, start = 1):
                    print(f"\n[{i}]")
                    Ticket.display(t)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
