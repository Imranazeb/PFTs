from os import system
import glob
import time
from calculations import *


cls = system('cls')

start_time = time.time()

pfts_toread = glob.glob('data/sample_PFT*')
with open('results/log.txt', 'w') as file:

    for index, eachPFT in enumerate(pfts_toread):
        result = read_pft(filename=eachPFT)
        file.write(f'Number {index}: INTERPRETATION: {result}\n{spacer}')
        print(f'Writing record {index + 1} of {len(pfts_toread)}')

file.close()

print(
    f'\nCode executed in {round(((time.time() - start_time)), 2)} sec\n')
