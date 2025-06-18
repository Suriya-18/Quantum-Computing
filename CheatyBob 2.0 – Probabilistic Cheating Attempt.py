def probabilistic_bob(qc, cheat_prob=0.5):
    if random.random() < cheat_prob:
        print("Bob: Attempting to cheat with X gate...")
        qc.x(0)
    else:
        print("Bob: Behaving honestly this time...")
    return qc
