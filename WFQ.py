import queue

class Packet:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

# Read packets from a text file and enqueue them into separate queues based on priority levels
def enqueue_packets(file_path, queue_S, queue_P, queue_E):
    with open(file_path, 'r') as file:
        for line in file:
            priority, data = line.strip().split(' ', 1)
            packet = Packet(data, priority)
            if priority == 'S':
                queue_S.put(packet)
            elif priority == 'P':
                queue_P.put(packet)
            elif priority == 'E':
                queue_E.put(packet)
            else:
                print(f"Ignoring packet with unknown priority: {priority}")

# Fill a combined queue by pulling packets from individual queues in a specific order
def fill_combined_queue(queue_combined, queue_S, queue_P, queue_E):
    # Define the number of packets to pull from each queue
    counts = {'P': 3, 'S': 2, 'E': 1}
    
    # Loop until all queues are empty
    while not (queue_S.empty() and queue_P.empty() and queue_E.empty()):
        # Pull packets from each queue based on the specified counts
        for priority, count in counts.items():
            if count > 0:
                # Determine the queue based on priority
                if priority == 'P':
                    source_queue = queue_P
                elif priority == 'S':
                    source_queue = queue_S
                elif priority == 'E':
                    source_queue = queue_E
                
                # Pull packets from the source queue and add them to the combined queue
                for _ in range(count):
                    if not source_queue.empty():
                        packet = source_queue.get()
                        queue_combined.put(packet)

# Main function to demonstrate
def main():
    # Create three separate queues for each priority level
    queue_S = queue.Queue()
    queue_P = queue.Queue()
    queue_E = queue.Queue()

    # Enqueue packets from a text file into separate queues based on priority levels
    file_path = 'input_queue-1-1.txt'
    enqueue_packets(file_path, queue_S, queue_P, queue_E)

    # Create a combined queue
    queue_combined = queue.Queue()

    # Fill the combined queue by pulling packets from individual queues in a specific order
    fill_combined_queue(queue_combined, queue_S, queue_P, queue_E)

    # Process packets from the combined queue
    print("Processing packets from the combined queue:")
    while not queue_combined.empty():
        packet = queue_combined.get()
        print(f"Data: {packet.data}, Priority: {packet.priority}")

if __name__ == "__main__":
    main()
