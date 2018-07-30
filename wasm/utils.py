
def varuint(num):
    return varuint_(num)

def varuint(num):
    binstr = ''
    pad = '0'
    if num < 0:
        p_binstr = '{:b}'.format(-num);
        binstr = '{:b}'.format(~num + 1);
        binstr.rjust(len(p_binstr), '0')
        pad = '1'
    else:
        binstr = '{:b}'.format(num);

    bits_multiple_of_7 = ((len(binstr) + 6) / 7) * 7
    binstr = binstr.rjust(bits_multiple_of_7, pad)
    group = [binstr[i:i+7] for i in range(0, len(binstr), 7)]
    for i in xrange(len(group)):
        if i == 0:
            group[i] = '0' + group[i]
        else:
            group[i] = '1' + group[i]
    return ''.join([chr(int(bs, 2)) for bs in group][::-1])

