import numpy as np
import os
import sys
from typing import List, Dict
from time import time
from collections import defaultdict
import readchar


def interactive_loop(sourcekeys: List[str]= list("1234qwerasdf"), nrounds: int=25) -> None:
    """Prompt the user to enter a sourcekey for nrounds, report on speed and accuracy"""

    accuracy: Dict[str, List[int]] = defaultdict(list)
    speed: Dict[str, List[int]] = defaultdict(list)
    os.system("clear")

    for k in np.random.choice(list(set(sourcekeys)), nrounds):
        print(k)
        
        start = time()
        user_input = readchar.readkey()

        speed[k].append(time() - start)
        accuracy[k].append(1 if user_input == k else 0)
        
        os.system("clear")
    
    print("key \tspeed \taccuracy")
    print("---- \t---- \t ------")
    for k in sourcekeys:
        print(f"{k} \t{np.average(speed[k]):.2f} \t{np.average(accuracy[k])*100:.0f}%")
    
    pass


if __name__ == "__main__":

    pass

    