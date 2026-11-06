from ex1 import DR_LEN, IR_LEN, TRANSPOSONS, build_sequence, reverse_complement


def find_transposons(seq):
    found = []
    for start in range(DR_LEN, len(seq)):
        left_dr = seq[start - DR_LEN:start]
        left_ir = seq[start:start + IR_LEN]

        for end in range(start + 2 * IR_LEN, len(seq) - DR_LEN + 1):
            right_ir = seq[end - IR_LEN:end]
            right_dr = seq[end:end + DR_LEN]

            if right_ir == reverse_complement(left_ir) and right_dr == left_dr:
                found.append((start, end))
    return found


if __name__ == "__main__":
    dna = build_sequence()
    detected = find_transposons(dna)

    print("Detected transposons (positions start at 1):")
    for start, end in detected:
        print(f"start={start + 1}, end={end}, length={end - start}")

    expected = set(TRANSPOSONS.values())
    print(f"\nExpected: {len(expected)}, detected: {len(detected)}, "
          f"correct: {len(expected & set(detected))}")
