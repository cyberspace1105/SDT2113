import simulus


def print_message():
    print("Hello World at time", sim.now)
    sim.sched(print_message, offset=20)


# Initialize the simulator
sim = simulus.simulator()

# Schedule the first call to print_message
sim.sched(print_message, offset=20)

# Run the simulation until time 100
sim.run(until=100)
