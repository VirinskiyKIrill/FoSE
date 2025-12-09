def rle(seq):
    res = []
    i = 0
    while i < len(seq):
        if seq[i].isdigit():
            count = int(seq[i])
            acid = seq[i + 1]
            res.append(acid * count)
            i += 2
        else:
            res.append(seq[i])
            i += 1
    return ''.join(res)

def read_seq(filename):
    seq_data = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 3:
                name = parts[0].strip()
                org = parts[1].strip()
                seq = parts[2].strip()

                if any(c.isdigit() for c in sequence):
                    sequence = rle(sequence)
                seq_data[name] = {
                    'org': org,
                    'seq': seq
                }
    return seq_data

def read_com(filename):
    com = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 1:
                oper = parts[0].strip()
                par = [p.strip() for p in parts[1:]]
                com.append((oper, par))
    return com

def diff_oper(seq_data, prot1, prot2):
    if prot1 not in seq_data:
        return f"MISSING: {prot1}"
    if prot2 not in seq_data:
        return f"MISSING: {prot2}"

    seq1 = seq_data[prot1]['seq']
    seq2 = seq_data[prot2]['seq']

    min_len = min(len(seq1), len(seq2))
    diff = 0
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            diff += 1

    diff += abs(len(seq1) - len(seq2))
    return str(diff)

def search_oper(seq_data, pat):
    res = []
    for name, data in seq_data.items():
        if pat in data['seq']:
            res.append((data['org'], name))
    return res

def mode_oper(seq_data, name):
    if name not in seq_data:
        return f"MISSING: {name}"

    seq = seq_data[name]['seq']

    count = {}
    for a in seq:
        count[a] = count.get(a, 0) + 1

    if not count:
        return "A 0"
    max = max(count.values())

    max = [a for a, count in count.items() if count == count]
    max.sort()

    return f"{max[0]} {count}"


seq_data = read_seq('sequences.txt')
com = read_com('commands.txt')

with open('genedata.txt', 'w', encoding='utf-8') as f:
    f.write("VKSUG\n")
    f.write("Genetic Searching\n")

    for i, (oper, par) in enumerate(com, 1):
        oper_num = f"{i:03d}"

        f.write(f"\n{oper_num}\t{oper}\t{' '.join(par)}\n")
        f.write("-" * 50 + "\n")

        if oper == 'search':
            if par:
                pat = par[0]
                res = search_oper(seq_data, pat)

                f.write("organism\tprotein\n")
                if res:
                    for org, prot in res:
                        f.write(f"{org}\t{prot}\n")
                else:
                    f.write("NOT FOUND\n")

        elif oper == 'diff':
            if len(par) >= 2:
                prot1, prot2 = par[0], par[1]
                res = diff_oper(seq_data, prot1, prot2)

                f.write("amino-acids difference:\n")
                f.write(f"{res}\n")

        elif oper == 'mode':
            if par:
                name = par[0]
                res = mode_oper(seq_data, name)

                f.write("amino-acid occurs:\n")
                f.write(f"{res}\n")

        f.write("-" * 50 + "\n")