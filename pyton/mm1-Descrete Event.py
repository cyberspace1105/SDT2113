
import random
import matplotlib.pyplot as plt
import simulus

servicerate = 40
loads = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Define a function to store throughput performance
def store_throughput(loads, throughput):
    """
    This function stores the throughput performance for each load.

    Args:
        loads: A list of loads for the simulation.
        throughput: A list to store the throughput performance.
    """
    for load in loads:
        num_in_system = 0  # Current number of tasks in the system
        nta = 8  # Number of tasks arrived
        ntd = 0  # Number of tasks departed

        # Create a simulator instance
        sim = simulus.simulator()

        def generate_expon(rate):
            while True:
                yield random.expovariate(rate)

        inter_arrival_time = generate_expon(load)
        service_time = generate_expon(servicerate)

        def arrive():
            nonlocal num_in_system, nta
            num_in_system += 1
            nta += 1
            sim.sched(arrive, offset=next(inter_arrival_time))
            if num_in_system == 1:
                sim.sched(depart, offset=next(service_time))

        def depart():
            nonlocal num_in_system, ntd
            num_in_system -= 1
            ntd += 1
            if num_in_system > 0:
                sim.sched(depart, offset=next(service_time))

        # Schedule the first arrival event
        sim.sched(arrive, offset=next(inter_arrival_time))

        # Run the simulation for a specific duration
        sim.run(until=10000)

        # Calculate throughput
        throughput_value = (ntd / nta) * 100
        print('Load:', load, 'Throughput:', throughput_value)

        # Append throughput to the throughput list
        throughput.append(throughput_value)

    # Visualize the results
    visualize_output(loads, throughput)

# Visualization function
def visualize_output(loads, throughput):
    plt.plot(loads, throughput, marker='o')
    plt.xlabel('Load')
    plt.ylabel('Throughput (%)')
    plt.title('Throughput of M/M/1')
    plt.grid(True)
    plt.show()

# List to store throughput performance
throughput = []

# Set a global random seed
random.seed(13579)

# Call the function to store throughput for different loads
store_throughput(loads, throughput)
