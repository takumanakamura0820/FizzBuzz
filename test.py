import sys
def main(input_line):
    m = int(input_line.pop(-2))
    input_line.pop(-1)
    pairs = []
    for pair in input_line:
        v, s = pair.split(':')
        pairs.append([int(v), s])
    pairs.sort()

    not_divied = True
    for v, s in pairs:
        if m % v == 0:
            print(s, end='')
            not_divied = False
            
    if not_divied:
        print(m)
    else:
        print()
        
if __name__ == '__main__':
    path = './input.txt'
    with open(path) as f:
        s = f.read()
        a = []
        for l in s.split("\n"):
            a.append(l)
        
    main(a)