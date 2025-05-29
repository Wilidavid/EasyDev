import variables as v
import random
import json

for problem in v.archivos:
    maxrange=random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)+random.randint(1,50)
    maxrange*=1.5
    maxrange=int(maxrange)
    problem[3]=maxrange
    with open('archivos.json', 'w') as f:
        json.dump(v.archivos, f, indent=4)