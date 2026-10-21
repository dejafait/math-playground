"""Instrument L062 using input/library data, never actual output sizes."""

def thresholds(d, packages, constants, term_stats, library_name_bytes):
    dimension = 2 + d['N'] + d['n'] + d['k']
    h = (dimension - 1).bit_length()
    V = 1 << (3*h + 4)
    H = 9*h + 20
    elementary = 10000 * V**2 * (H+1)**2
    generated = (constants['L'] + 1) * elementary
    imported = sum(len(a['rows']) for a in packages)
    lines = imported + generated
    framing = 256 + 64 * (lines+1).bit_length()
    result = {'lemma':'L062', 'dimension':dimension, 'h':h, 'V':V, 'H':H,
              'elementary_operations':elementary, 'generated_records':generated,
              'imported_records':imported, 'lines':lines, 'formats':{}}
    for mode, factor in [('native',3), ('not-or',6)]:
        t, depth, names = term_stats[mode]
        nodes = sum(a['node_sums'][mode] for a in packages)
        supplied_depth = max([a['depths'][mode] for a in packages]+[0])
        payload = max([1, names, library_name_bytes]+[a['name_bytes'] for a in packages])
        D, S = constants[mode]['D'], constants[mode]['S']
        argument_nodes = 8 * 4**(H+1) * (t+1)
        byte_bound = ((payload+4)*(nodes+(generated+1)*S*argument_nodes)
                      +(lines+2)*framing)
        result['formats'][mode] = {
            'input_term_nodes':t, 'input_term_depth':depth, 'payload_bytes':payload,
            'imported_nodes':nodes, 'imported_depth':supplied_depth,
            'argument_nodes':argument_nodes, 'argument_depth':factor*H+depth,
            'lines':lines, 'depth':max(supplied_depth,D+factor*H+depth),
            'record_nodes':max(nodes,S*argument_nodes),
            'bytes':byte_bound, 'bits':8*byte_bound,
            'basis':'L062 equation (1), supplied-input and checked-library data only'}
    return result

def check(measured, bound):
    checks = {'lines':measured['lines']<=bound['lines'],
              'depth':measured['max_line_depth']<=bound['depth'],
              'record_nodes':measured['max_record_nodes']<=bound['record_nodes'],
              'bytes':measured['bytes']<=bound['bytes']}
    if not all(checks.values()):
        raise AssertionError('L062 uniform threshold failed: '+str(checks))
    return checks
