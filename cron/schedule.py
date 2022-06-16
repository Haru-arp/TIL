from datetime import datetime
import threading
# import time

# print(current_time)
def print_time():
    
    current_time = datetime.now()
    print(current_time)
    
    threading.Timer(60, print_time).start()
    
print_time()
