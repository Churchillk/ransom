import os
ac_n = []
for x in range(10):
    fname = f'chu{x}.txt'
    os.system(f"echo -n 'hello again motherfucker' > {fname}")
    ac_n.append(fname)