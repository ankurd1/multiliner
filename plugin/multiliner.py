import re

COMMA = ','
OPEN_PAREN = '('
CLOSE_PAREN = ')'

def multiline(line, start_index = 0, ts = 4, extra_comma = False):
    start, end, commas = _parse(line, start_index)
    if start == -1:
        return [line]

    ## break up lines
    result = []
    result.append(line[:start + 1])

    last = start
    for index in commas:
        result.append(line[last + 1:index + 1])
        last = index

    if last != end - 1:
        result.append(line[last + 1:end])
    result.append(line[end:])

    ## clean up
    result = [l.strip() for l in result]

    ## indentation
    initial_indent = re.match('\s*', line).end()
    result[0] = initial_indent*' ' + result[0]

    for i in range(1, len(result) - 1):
        result[i] = (initial_indent + ts)*' ' + result[i]

    result[-1] = initial_indent*' ' + result[-1]

    ## add extra_comma
    if extra_comma and len(result) > 2 and result[-2][-1] != COMMA:
        result[-2][-1] = COMMA

    return result


def _parse(txt, start):
    outermost_paren_start = -1
    outermost_paren_end = -1
    commas = []

    paren_count = 0
    for i in range(start, len(txt)):
        if txt[i] == OPEN_PAREN:
            paren_count -= 1
            if paren_count == -1:
                outermost_paren_start = i
        elif txt[i] == CLOSE_PAREN:
            paren_count += 1
            if paren_count > 0:
                break
            elif paren_count == 0:
                outermost_paren_end = i
                break
        elif txt[i] == COMMA:
            if paren_count == -1:
                commas.append(i)

    if paren_count != 0:
        return (-1, -1, [])
    if outermost_paren_start == -1 and outermost_paren_end == -1:
        return (-1, -1, [])
    return (outermost_paren_start, outermost_paren_end, commas)

def unmultiline(lines, cur_col):
    pass
