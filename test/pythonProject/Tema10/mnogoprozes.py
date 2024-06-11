import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        name, status, quantity = request
        if status == 'receipt':
            if name in self.data:
                self.data[name] += quantity
            else:
                self.data[name] = quantity
        elif status == 'shipment':
            if name in self.data and self.data[name] > 0:
                self.data[name] -= quantity

    def runs(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request, ))
            processes.append(process)
            process.run()

if __name__ == '__main__':

    manager = WarehouseManager()
    requests = [("product1", "receipt", 100), ("product2", "receipt", 150),
                    ("product1", "shipment", 30),
                    ("product3", "receipt", 200),
                    ("product2", "shipment", 50)]
    manager.runs(requests)
    print(manager.data)