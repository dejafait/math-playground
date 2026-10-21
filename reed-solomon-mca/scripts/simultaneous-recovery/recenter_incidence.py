"""Bounded support-only test; no field-label or moment compatibility claim."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def partitions(points):
    if not points:
        yield ()
        return
    a, *rest = points
    for b, c in combinations(rest, 2):
        block = (a, b, c)
        for tail in partitions(tuple(x for x in rest if x not in (b, c))):
            yield (block,) + tail


PAIRS = {p: i for i, p in enumerate(combinations(range(10), 2))}


def pair_mask(blocks):
    return sum(1 << PAIRS[p] for block in blocks for p in combinations(block, 2))


def inspect_family(family):
    f = list(map(frozenset, family))
    degrees = Counter(x for a in f for x in a)
    pair_cases, tau_cases, failures = [], [], []
    for i, j in combinations(range(len(f)), 2):
        common = f[i] & f[j]
        if len(common) != 2:
            continue
        b, star = f[i] | f[j], f[i] ^ f[j]
        universal = next((k for k, a in enumerate(f) if a == star), None)
        forbidden = [k for k, a in enumerate(f)
                     if k not in (i, j, universal) and len(a & b) > 1]
        pair_cases.append(dict(pair=[i, j], B=sorted(b), universal=universal,
                               forbidden=forbidden))
        if forbidden:
            failures.append(dict(kind="six_lift", pair=[i, j], supports=forbidden))
        for k, a in enumerate(f):
            if k in (i, j) or len(a & b) != 1 or not (a & common):
                continue
            h = next(iter(a & common))
            d = next(iter(common - {h}))
            eligible = [l for l in range(len(f)) if l not in (i, j, k, universal)]
            d_tags = [l for l in eligible if f[l] & b == {d}]
            record = dict(triple=[i, j, k], h=h, d=d, B=sorted(b),
                          universal=universal, nonuniversal_count=len(eligible),
                          nonuniversal_indices=eligible, d_tags=d_tags,
                          excluded_by_L051=len(eligible) >= 12 and len(d_tags) >= 2)
            tau_cases.append(record)
            if record["excluded_by_L051"]:
                failures.append(dict(kind="L051", triple=[i, j, k]))
    if max(degrees.values()) > 4 or len(set(f)) != len(f):
        failures.append(dict(kind="capacity_or_duplicates"))
    return dict(supports=[sorted(a) for a in f], degrees=dict(sorted(degrees.items())),
                pair_cases=pair_cases, tau_cases=tau_cases, failures=failures)


def main():
    # Four classes of three disjoint triples, plus W. Fix the first class
    # by permutations of W and its seven-label complement. Two possible
    # fourth omissions cover the remaining symmetry cases in this subclass.
    w = (0, 1, 2)
    first = ((1, 3, 4), (2, 5, 6), (7, 8, 9))
    base_mask = pair_mask(first) | pair_mask((w,))
    classes = {o: [(p, pair_mask(p)) for p in partitions(tuple(x for x in range(10) if x != o))
                   if not (pair_mask(p) & pair_mask((w,)))] for o in (0, 1, 2, 3)}
    trials, witness = [], None
    for last_omit in (0, 3):
        count2 = count3 = count4 = 0
        for second, m2 in classes[1]:
            if m2 & base_mask:
                continue
            count2 += 1
            for third, m3 in classes[2]:
                if m3 & (base_mask | m2):
                    continue
                count3 += 1
                for fourth, m4 in classes[last_omit]:
                    count4 += 1
                    if m4 & (base_mask | m2 | m3):
                        continue
                    witness = [first, second, third, fourth]
                    break
                if witness:
                    break
            if witness:
                break
        trials.append(dict(last_omit=last_omit, compatible_second=count2,
                           compatible_third=count3, fourth_tests=count4,
                           found=witness is not None))
        if witness:
            break
    result = dict(scope="four disjoint-triple classes; support-only", trials=trials,
                  class_counts={o: len(a) for o, a in classes.items()}, witness=witness)
    if witness:
        # B: h=10,d=11,Y=12,13,Z=14,15; O:0,...,9.
        family = [(10, 11, 12, 13), (10, 11, 14, 15), (10, 0, 1, 2)]
        family += [tuple((tag,) + block) for tag, cls in zip((12, 13, 14, 15), witness)
                   for block in cls]
        result["verification"] = inspect_family(family)
    path = HERE / "recenter-incidence-result.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(found=witness is not None, trials=trials,
                          actual_count=15 if witness else None, required_count=15,
                          failures=result.get("verification", {}).get("failures", []),
                          certificate=str(path.relative_to(HERE.parent.parent)))))


if __name__ == "__main__":
    main()
