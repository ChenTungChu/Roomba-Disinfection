from time import *
from threading import Thread

def task(id):
    global i
    print(f'Starting task num: {id}') 
    sleep(1)
    print(f'Task num {id} finished')


start_time = perf_counter()

# create and start 10 threads
threads = []
for i in range(1, 11):
    t = Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

# wait for threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} sec to complete.')
