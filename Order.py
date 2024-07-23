class OrderStack:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        '''Add orders to the top of the stack'''
        self.orders.append(order)

    def remove_order(self):
        '''Removes and returns the last order from the stack'''
        if not self.is_empty():
            return self.orders.pop()
        print("No orders to remove")

    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.orders) == 0
    
    def size(self):
        '''Returns the number of orders in the stack'''
        return len(self.orders)
    
    def display_orders(self):
        '''Displays all orders currently in the stack'''
        if self.is_empty():
            print("No orders in the stack.")
        else:
            print("Orders in the stack (from top to bottom):")
            for order in reversed(self.orders):  # Display from top to bottom
                print(f"Order ID: {order['id']}, Priority: {order['priority']}, Order Items: {order['order_items']}")

class PriorityQueue:
    def __init__(self):
        self.orders = []

    def is_empty(self):
        '''Check if the priority queue is empty'''
        return len(self.orders) == 0

    def enqueue(self, priority, item):
        '''Add an order to the queue with a specific priority'''
        self.orders.append((priority, item))
        # Sort the list so that the highest priority item (lowest number) is at the front
        self.orders.sort(key=lambda x: x[0])

    def dequeue(self):
        '''Remove and return the order with the highest priority (lowest number)'''
        if self.is_empty():
            return None
        return self.orders.pop(0)[1]

    def size(self):
        '''Returns the number of orders in the queue'''
        return len(self.orders)

class CustomerOrderQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_order(self, order, priority):
        '''Add an order to the queue with the given priority'''
        self.queue.enqueue(priority, order)
        print(f"Customer order added: {order} with priority {priority}")

    def process_order(self):
        '''Process the order with the highest priority'''
        order = self.queue.dequeue()
        if order:
            print(f"Order processed: {order}")
        else:
            print("No orders to process")

    def notify_customer(self, order):
        '''Notify the customer that their order is ready'''
        print(f"Customer notified: Your order {order} is ready for pickup or delivery")

# Test the OrderStack class
order_stack = OrderStack()

order_stack.add_order({'id': 1, "priority": 4, "order_items": "Coke"})
order_stack.add_order({'id': 2, "priority": 6, "order_items": "Cake"})
order_stack.add_order({'id': 3, "priority": 7, "order_items": "Pizza"})

order_stack.display_orders()

removed_order = order_stack.remove_order()
print(f"Removed order: Order ID {removed_order['id']}")

order_stack.display_orders()

# Test the CustomerOrderQueue class
customer_queue = CustomerOrderQueue()

# Sample customer orders with priorities (lower number means higher priority)
customer_orders = [("Burger", 2), ("Pasta", 1), ("Pizza", 3)]
for order, priority in customer_orders:
    customer_queue.add_order(order, priority)

customer_queue.process_order()  # Should process Pasta first
customer_queue.notify_customer("Pasta")
customer_queue.process_order()  # Should process Burger next
customer_queue.notify_customer("Burger")
customer_queue.process_order()  # Should process Pizza last
customer_queue.notify_customer("Pizza")
customer_queue.process_order()  # No orders to process
