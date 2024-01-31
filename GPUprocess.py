from numba import jit

# to measure exec time
from timeit import default_timer as timer

from ImageSize import main


@jit
def func():
    main("D:\Imagens\CozinhaArmario01")


if __name__ == "__main__":
    start = timer()
    func()
    print("3 with GPU:", timer() - start)
