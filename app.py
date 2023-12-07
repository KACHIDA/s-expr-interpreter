def parse_expr(s: str, idx: int):
    idx = skip_space(s, idx)
    if s[idx] == '(':
        # list
        idx += 1
        l = []
        while True:
            idx = skip_space(s, idx)
            if idx >= len(s):
                raise Exception('Unbalanced paranthesis')
            if s[idx] == ')':
                idx += 1
                break
            idx, v = parse_expr(s, idx)
            l.append(v)
    elif s[idx] == ')':
        raise Exception('bad paranthesis')
    else:
        # atom
        start = idx
        while idx < len(s) and (not s[idx].isspace()) and s[idx] not in '()':
            idx += 1
        if start ==  idx:
            raise Exception('empty program')
        return idx, parse_atom(s[start:idx])



def skip_space():
    while idx < len(s) and s[idx].isspace():
        idx += 1
    return idx

def parse_atom(s):
    import json
    try:
        return ['val', json.loads(s)]
    except json.JSONDecodeError:
        return s

