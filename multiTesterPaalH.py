import client
import time
import multiprocessing
# Lagert av Pål Hodahl for å teste flere klienter samtidig
# To run multiTesterPaalH.py, comment the three lines using sys.argv, and uncomment the host, port and file variables
# in client.py

# Standard python start command
if __name__ == '__main__':
    st = time.time()                                                        # st, StartTime variable
    num = 10                                                                # num, number of clients to run
    processes = []                                                          # Process list
    for i in range(num):                                                    # for loop
        p = multiprocessing.Process(target=client.testingMultipleClients())                   # p, what process to start
        p.start()                                                           # start process
        processes.append(p)                                                 # append to processes list

    for process in processes:                                               # for loop process in processes
        process.join()                                                      # join() the processes

    # After all the processes have run
    et = time.time()                                                        # et, EndTime variable
    tt = et - st                                                            # tt, TotalTime

    # Print statement
    print(f"Running {num} clients at the same time with multiprocessing took: {tt:.3f} seconds.")