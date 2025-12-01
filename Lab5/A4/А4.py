def decode_rle(sequence):
    result = []
    i = 0
    while i < len(sequence):
        if sequence[i].isdigit():
            count = int(sequence[i])
            amino_acid = sequence[i + 1]
            result.append(amino_acid * count)
            i += 2
        else:
            result.append(sequence[i])
            i += 1
    return ''.join(result)

def read_sequences(filename):
    sequences_data = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 3:
                protein_name = parts[0].strip()
                organism = parts[1].strip()
                sequence = parts[2].strip()

                if any(c.isdigit() for c in sequence):
                    sequence = decode_rle(sequence)
                sequences_data[protein_name] = {
                    'organism': organism,
                    'sequence': sequence
                }
    return sequences_data

def read_commands(filename):
    commands = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 1:
                operation = parts[0].strip()
                params = [p.strip() for p in parts[1:]]
                commands.append((operation, params))
    return commands

def search_operation(sequences_data, pattern):
    results = []
    for protein_name, data in sequences_data.items():
        if pattern in data['sequence']:
            results.append((data['organism'], protein_name))
    return results

def diff_operation(sequences_data, protein1, protein2):
    if protein1 not in sequences_data:
        return f"MISSING: {protein1}"
    if protein2 not in sequences_data:
        return f"MISSING: {protein2}"

    seq1 = sequences_data[protein1]['sequence']
    seq2 = sequences_data[protein2]['sequence']

    min_len = min(len(seq1), len(seq2))
    differences = 0
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            differences += 1

    differences += abs(len(seq1) - len(seq2))
    return str(differences)

def mode_operation(sequences_data, protein_name):
    if protein_name not in sequences_data:
        return f"MISSING: {protein_name}"

    sequence = sequences_data[protein_name]['sequence']

    amino_count = {}
    for amino in sequence:
        amino_count[amino] = amino_count.get(amino, 0) + 1

    if not amino_count:
        return "A 0"
    max_count = max(amino_count.values())

    max_aminos = [amino for amino, count in amino_count.items() if count == max_count]
    max_aminos.sort()

    return f"{max_aminos[0]} {max_count}"

def main():
    sequeces_data = read_sequences('sequences.txt')
    commands = read_commands('commands.txt')

    with open('genedata.txt', 'w', encoding='utf-8') as f:
        f.write("VKSUG\n")
        f.write("Genetic Searching\n")

        for i, (operation, params) in enumerate(commands, 1):
            operation_num = f"{i:03d}"

            f.write(f"\n{operation_num}\t{operation}\t{' '.join(params)}\n")
            f.write("-" * 50 + "\n")

            if operation == 'search':
                if params:
                    pattern = params[0]
                    results = search_operation(sequeces_data, pattern)

                    f.write("organism\tprotein\n")
                    if results:
                        for organism, protein in results:
                            f.write(f"{organism}\t{protein}\n")
                    else:
                        f.write("NOT FOUND\n")

            elif operation == 'diff':
                if len(params) >= 2:
                    protein1, protein2 = params[0], params[1]
                    result = diff_operation(sequeces_data, protein1, protein2)

                    f.write("amino-acids difference:\n")
                    f.write(f"{result}\n")

            elif operation == 'mode':
                if params:
                    protein_name = params[0]
                    result = mode_operation(sequeces_data, protein_name)

                    f.write("amino-acid occurs:\n")
                    f.write(f"{result}\n")

            f.write("-" * 50 + "\n")

if __name__ == "__main__":
    main()