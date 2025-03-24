from sample_madlibs import code, hungergames, madlibs
import random

if __name__ == '__main__':
    m = random.choice([code, hungergames, madlibs])
    m.madlib()
