import threading
class PrintThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
    def run(self):
        self .print_square()
        self.print_cube()
    def print_cube(self):
 # function to print cube of given num
        print("Cube: {}".format(self.num * self.num * self.num))  
    def print_square(self):
 # function to print square of given num
        print("Square: {}".format(self.num * self.num)) 
if __name__ == "__main__":
 # creating thread
    t = PrintThread(10)
 # start the thread
    t.start()
# wait until the thread finishes
    t.join()
# continue with the main loop
    for i in range(5):
        print("Main loop: {}".format(i))
        print("Done!")