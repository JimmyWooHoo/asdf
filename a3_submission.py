class Queue:
    """
    A priority-based queue implemented using a binary min-heap.

    The queue internally stores QueueNode objects in an array-based
    binary heap. Lower priority values correspond to objects that
    are removed earlier.
    """

    class QueueNode:
        """
        A container storing an object and its associated priority.
    
        Args:
        obj (object): The object to store in the queue.
        pri (int): The priority associated with the object. Lower values
            indicate higher priority.
    
        Returns:
        None
        """
        def __init__(self, obj, pri):
            self.obj = obj
            self.pri = pri

    """
    Initialize the Queue data structure.

    Args:
    cap (int): The initial capacity of the queue.

    Returns:
    None
    """
    def __init__(self, cap):
        self.cap = cap

    def add(self, obj, pri):
        """
        Add a new object to the queue with the given priority.

        A new QueueNode is created and appended to the internal heap
        array. The method then restores the min-heap property by
        performing a heap-up operation.

        Args:
        obj (object): The object to insert.
        pri (int): The priority associated with the object. Lower values
            indicate higher priority.
        """
        pass

    def pop(self):
        """
        Remove and return the object with the largest priority value.

        The root of the heap is removed. The last element in the heap is
        moved to the root position, and a heap-down operation is
        performed to restore the heap property.

        Args:
        None

        Returns:
        object: The object stored in the QueueNode with the largest
            priority value (or None if the Queue is empty).
        """
        pass

class Tower:
    def __init__(self):
        # Initialize any internal state here
        self.time = 0
        pass

    def process(self, new_packets):
        """
        Called once per time step.

        Parameters:
            new_packets: a list of packets that arrived at this time step

        Returns:
            read_packets: packets that were read/received this step
            sent_packets: packets that were sent out this step
            acked_packets: packets that were acknowledged this step
        """

        # Step 1: advance time
        self.time += 1

        # Step 2: record or process newly arrived packets
        read_packets = []

        # Step 3: logic determining which packets get acknowledged
        acked_packets = []

        # Step 4: logic determining which packets get sent this step
        sent_packets = []

        return read_packets, sent_packets, acked_packets