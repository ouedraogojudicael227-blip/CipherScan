from config import MIN_PORT, MAX_PORT


def get_port(message):
    while True:

        try:
            port = int(input(message))

            if MIN_PORT <= port <= MAX_PORT:
                return port

            print(f"The port must be between {MIN_PORT} and {MAX_PORT}.")

        except ValueError:
            print("Please enter a valid integer.")


def get_port_range():
    while True:

        start_port = get_port("Enter the first port : ")
        end_port = get_port("Enter the last port : ")

        if start_port <= end_port:
            return start_port, end_port

        print("The first port must be less than or equal to the last port.")