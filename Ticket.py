class Ticket:
    def __init__(self, ticket_id, path, path_lines, price):
        self.ticket_id = ticket_id
        self.path = path
        self.path_lines = path_lines
        self.price = price

    def __str__(self):
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Path: {' → '.join(self.path)}\n"
                f"Fare: {self.price}")
    
    def line_change_instructions(self):
        instructions = []
        for i in range(1, len(self.path)):
            if self.path_lines[i] != self.path_lines[i-1]:
                instructions.append(f"Change from {self.path_lines[i-1]} to {self.path_lines[i]} at {self.path[i-1]}")
        return instructions

    def display(self):
        print(f"\nTicket ID: {self.ticket_id}")
        print(f"Path: {' → '.join(self.path)}")
        print(f"Fare: {self.price}")

        instructions = self.line_change_instructions()
        if instructions:
            print("Line change instructions:")
            for step in instructions:
                print(f"- {step}")
        else:
            print("No line changes needed.")
