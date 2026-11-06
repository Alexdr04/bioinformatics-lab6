import random

LENGTH = 300
IR_LEN = 8
DR_LEN = 5

TRANSPOSONS = {
    "T1": (20, 70),
    "T2": (100, 220),
    "T3": (130, 180),
    "T4": (155, 260),
}


def random_dna(length):
    return "".join(random.choice("ACGT") for _ in range(length))


def reverse_complement(dna):
    return dna.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def build_sequence():
    random.seed(42)
    seq = list(random_dna(LENGTH))

    for start, end in TRANSPOSONS.values():
        ir = random_dna(IR_LEN)
        dr = random_dna(DR_LEN)
        seq[start - DR_LEN:start + IR_LEN] = dr + ir
        seq[end - IR_LEN:end + DR_LEN] = reverse_complement(ir) + dr

    return "".join(seq)


if __name__ == "__main__":
    dna = build_sequence()
    print(f"DNA sequence ({len(dna)} b):")
    print(dna)
    print("\nInserted transposons (positions start at 1):")
    for name, (start, end) in TRANSPOSONS.items():
        print(f"{name}: start={start + 1}, end={end}")
