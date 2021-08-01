import random

# psudo-random
def psudoRandom():
    # seed is the value used to produce psudo-random values
    random.seed(5);
    print(random.random());
    print(random.uniform(1,9));
    print(random.randint(0,6));
    print(random.randrange(0,11));
    # mean = 0, sd= 1
    print(random.normalvariate(0,1));
    print(random.choice(list("pick a letter")));
    print(random.choices(list("pick a array of letter"),k=2));
    print(random.sample(list('pick any 3 letters'),3));
    arr=list('shuffle and assign');
    random.shuffle(arr);
    print(arr);

import secrets

def trueRandom():
    print(secrets.randbelow(10));
    print(secrets.randbits(5));
    print(secrets.choice(list("pick a letter")));

import numpy as np
def numpyRandom():
    # seed is the value used to produce psudo-random values
    np.random.seed(4);
    print(np.random.rand(3,3));
    print(np.random.randint(1,11,(3,3)));
    arr=[np.random.randint(1,10,3) for _ in range(4)];
    print(arr);
    np.random.shuffle(arr);
    print(arr);

numpyRandom()