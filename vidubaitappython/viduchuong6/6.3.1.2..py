
import threading
def print_cube(num):
 # function to print cube of given num
 print("Cube: {}".format(num * num * num))
def print_square(num):
 # function to print square of given num
 print("Square: {}".format(num * num))
if __name__ == "__main__":
 # creating thread
 t1 = threading.Thread(target=print_square, args=(10,))  
 t2 = threading.Thread(target=print_cube, args=(10,))  # start the threads
 t1.start()
 t2.start()
 # wait until both threads finish
 t1.join()
 t2.join()
 # continue with the main loop
for i in range(5):
 print("Main loop: {}".format(i))
 print("Done!") 