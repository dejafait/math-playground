# L030 — Guarded residue-290 depth-12 ancestor cover is false

## Hypotheses

On positive integers let T(x)=x/2 for even x and
T(x)=(3x+1)/2 for odd x. O and E denote actual input branches.
Set W=(OOEO)^2 O^3 E^2, of length 13, and n=3616859.
An ancestor is a positive integer p with T^t(p)=n;
the tested horizon is the fixed set 1<=t<=12.

## Conclusion

The positive root n is 290 modulo 729, has actual prefix W and an odd
endpoint, but has no positive p=20 modulo 27 with p<n and T^t(p)=n
for 1<=t<=12. Thus the universal cover on precisely this guarded
cylinder is false. This is a finite ancestor obstruction, not a
nonconvergent orbit or a disproof of Collatz. It makes no least-root
admissibility assumption and no statement about longer horizons.

## Proof

### Imported inputs and specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-06-guarded-residue290-ancestor-cover.md`.
Import Sodelin, *L4 — General inverse-word coalescence semantics*,
dated 2026-08-23, [sections 1–5](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/L4_General_Inverse_Word_Coalescence.md),
especially the positive inverse branches in section 1 and the
guarded prefix semantics in sections 2–4. At a positive integer y,
the complete positive predecessor set is

    I(y) = {2y} union {(2y-1)/3 if y=2 modulo 3}.

No rational or unguarded inverse is admitted. The odd inverse is
positive and odd under its stated integer guard; the even inverse is
positive and even. The cited semantics therefore apply at every node.
The source was inspected from live main on 2026-10-06 as recorded in
the assessment; there is no immutable revision or local Lean audit.
No general inverse-word reproof is needed here. The specialization is
the exact finite tree at the displayed root.

For root selection, L020's cited finite parity coding applies to the
13 input bits of W and one further odd bit at its endpoint. It gives
n=12379 modulo 16384. The complete one-bit lifts and CRT arithmetic
are saved in the certificate. Since

    3616859 = 12379 + 16384*220 = 290 + 729*4961,
    16384*729 = 11943936,

the smallest positive guarded root selected by CRT is n. Coding is
only a way to select the test root; its actual guards are checked
independently below. This is a REPRODUCTION of inspected machinery
with a new local negative test, not a claim of originality.

### Full actual forward check

The successive states, with the branch at each input, are:

| i | T^i(n) | Branch |
|---|---:|---|
| 0 | 3616859 | O |
| 1 | 5425289 | O |
| 2 | 8137934 | E |
| 3 | 4068967 | O |
| 4 | 6103451 | O |
| 5 | 9155177 | O |
| 6 | 13732766 | E |
| 7 | 6866383 | O |
| 8 | 10299575 | O |
| 9 | 15449363 | O |
| 10 | 23174045 | O |
| 11 | 34761068 | E |
| 12 | 17380534 | E |
| 13 | 8690267 | endpoint |

Each entry has the prescribed input parity and each next entry is
the shortcut image by direct integer substitution. The last entry is
odd, so both final E steps are exact. This proves all forward guards
without inferring them from final integrality alone.

### Exhaustive finite inverse certificate

Set S_0={n} and S_{d+1}=union of I(y) for y in S_d.
The imported positive inverse semantics imply that S_d is exactly
the set of all positive p with T^d(p)=n, by finite induction on d.
There is no bound on the intermediate values and no pruning by size:
a large inverse endpoint may later have a shrinking odd inverse.

The complete sets appear below. They were evaluated with integer
arithmetic using the displayed recurrence. Their only members below
n, across depths 1 through 12, are

| Depth | p | p modulo 27 |
|---|---:|---:|
| 1 | 2411239 | 4 |
| 3 | 3214985 | 14 |
| 4 | 2143323 | 9 |

In particular, none is 20 modulo 27. As a separate full check of the
membership filter, all residue-20 hits are

| Depth | p |
|---|---:|
| 6 | 77159648 |
| 7 | 17146586 |
| 9 | 205759082 |
| 10 | 411518144 |
| 11 | 823036160 |
| 12 | 60965642 |
| 12 | 182896940 |

Each is strictly greater than n. Exhaustiveness of S_d, rather than
a sampled search for p, proves the conclusion.

The executable finite certificate is
`scripts/guarded-ancestor/check_depth12.py`, reproduced by
`python3 scripts/guarded-ancestor/check_depth12.py`.
Its complete output is
`scripts/guarded-ancestor/depth12_certificate.json`.
It stores all nodes, parent indices, inverse words, odd-inverse guards,
root-relative comparisons, residue filters, forward states and coding
lifts. It checks every stored node by direct forward iteration and
checks both possible inverse branches for every nonterminal node.
The complete level sets, forward states, coding lifts and both
load-bearing endpoint filters were inspected in full, rather than
from a JSON preview. The following explicit sets make the finite
arithmetic independently checkable without treating a script assertion
as an unexplained theorem.

```text
S_0 = 3616859
S_1 = 2411239, 7233718
S_2 = 4822478, 14467436
S_3 = 3214985, 9644956, 9644957, 28934872
S_4 = 2143323, 6429970, 6429971, 19289912, 19289914, 57869744
S_5 = 4286646, 4286647, 12859940, 12859941, 12859942, 38579824, 38579828, 38579829, 115739488
S_6 = 8573292, 8573293, 8573294, 25719880, 25719882, 25719884, 25719885, 77159648, 77159656,
    77159658, 231478976
S_7 = 5715529, 17146584, 17146586, 17146588, 17146589, 51439760, 51439764, 51439765, 51439768,
    51439770, 154319296, 154319312, 154319316, 154319317, 462957952
S_8 = 11431057, 11431058, 11431059, 34293168, 34293172, 34293173, 34293176, 34293178, 102879520,
    102879528, 102879530, 102879536, 102879540, 102879541, 308638592, 308638624, 308638632,
    308638634, 925915904
S_9 = 7620705, 22862114, 22862115, 22862116, 22862117, 22862118, 68586336, 68586344, 68586346,
    68586352, 68586353, 68586356, 68586357, 205759040, 205759056, 205759060, 205759061, 205759072,
    205759080, 205759082, 205759089, 617277184, 617277248, 617277264, 617277268, 617277269,
    1851831808
S_10 = 15241409, 15241410, 15241411, 45724228, 45724229, 45724230, 45724232, 45724234, 45724235,
    45724236, 45724237, 137172672, 137172688, 137172692, 137172693, 137172704, 137172706, 137172707,
    137172712, 137172714, 137172721, 411518080, 411518112, 411518120, 411518122, 411518144,
    411518160, 411518164, 411518165, 411518178, 411518179, 1234554368, 1234554496, 1234554528,
    1234554536, 1234554538, 3703663616
S_11 = 10160939, 30482818, 30482819, 30482820, 30482821, 30482822, 30482823, 91448456, 91448458,
    91448460, 91448461, 91448464, 91448468, 91448469, 91448470, 91448471, 91448472, 91448474,
    274345344, 274345376, 274345384, 274345386, 274345408, 274345412, 274345413, 274345414,
    274345424, 274345428, 274345429, 274345442, 274345443, 823036160, 823036224, 823036240,
    823036244, 823036245, 823036288, 823036320, 823036328, 823036330, 823036356, 823036357,
    823036358, 2469108736, 2469108992, 2469109056, 2469109072, 2469109076, 2469109077, 7407327232
S_12 = 6773959, 20321878, 20321879, 20321881, 60965636, 60965637, 60965638, 60965640, 60965642,
    60965644, 60965645, 60965646, 60965647, 60965649, 182896912, 182896916, 182896917, 182896920,
    182896922, 182896928, 182896936, 182896938, 182896940, 182896941, 182896942, 182896944,
    182896948, 182896949, 182896961, 548690688, 548690752, 548690768, 548690772, 548690773,
    548690816, 548690824, 548690826, 548690828, 548690829, 548690848, 548690856, 548690858,
    548690884, 548690885, 548690886, 548690905, 1646072320, 1646072448, 1646072480, 1646072488,
    1646072490, 1646072576, 1646072640, 1646072656, 1646072660, 1646072661, 1646072712, 1646072714,
    1646072716, 1646072717, 4938217472, 4938217984, 4938218112, 4938218144, 4938218152, 4938218154,
    14814654464
```

### Independent critical audit, 2026-10-06

The separate audit approved by
`drafts/literature/2026-10-06-guarded-ancestor-refutation-audit.md`
is complete. No numerical or logical correction was required. The
checker `scripts/guarded-ancestor/audit_depth12.py` neither imports the
original generator nor overwrites its certificate. Run it with
`python3 scripts/guarded-ancestor/audit_depth12.py`; its full evidence is
`scripts/guarded-ancestor/depth12_audit_certificate.json`.

For independence from inverse-tree generation, the checker enumerates
every forward branch word of each length d=1,...,12. Using the cited
finite affine semantics, a word has formal endpoint (a*p+b)/2^d.
Its only possible ancestor of n is p=(2^d*n-b)/a. The checker tests
integrality and positivity, then replays every input parity and the
endpoint using the actual shortcut map. Every actual d-step ancestor
has one of these words and must equal its solved p, so the enumeration
is complete. Conversely, every accepted p is an actual positive
ancestor by its full replay. This is a finite application of the
imported semantics, not a new general inverse-word theorem.

All 8190 words were examined; 249 positive words were accepted across
depths 1–12. The counts, including depth zero, are

    1, 2, 2, 4, 6, 9, 11, 15, 19, 27, 37, 50, 67.

The complete independently reconstructed JSON agrees with the original,
including all node values, reversed word order, parent indices, branch
labels, nonterminal odd-inverse guards, depth counts, both filters and
forward states. Every nonterminal node also has exactly both legal
positive branches (or just doubling when the odd branch is illegal).
No size filter is applied to this enumeration. The audit directly
exhausts the residue representatives for all fourteen coding prefixes,
checks the unique CRT representative, and parses and compares every
entry of this lemma's forward table, inverse sets and filter tables.
All 469 checks pass; the required smaller residue-20 ancestor count
is at least one and the actual count is zero.

The original certificate was read in full and left byte-for-byte
unchanged; its SHA-256 is
`4430cee1432acd584ca4ebe3f96204b1b8cefc75cb4e2b3b4414d85d02d8663f`.
Full-object equality and exhaustive node/word checks, rather than a
certificate preview, underlie this audit. In particular, all three
below-root endpoints and all seven residue-20 endpoints agree with
the displayed tables. The induction identifying S_d with actual
d-step ancestors uses the positive inverse semantics at every node,
not endpoint integrality without guards. The fourteenth coding bit
and the odd forward endpoint are retained. No least-root condition,
unbounded horizon, infinite-orbit conclusion or external formal
verification has been introduced. This validates the recorded local
finite refutation using known machinery; it claims no new general
result beyond the inspected sources.

## Mathlib

Full matching guarded-cover refutation, inverse-word and parity-coding
coverage: **not checked**. No library absence is asserted. Supporting
congruence and iteration declarations are not essential inputs here;
external Lean claims for other ancestor theorems do not verify this
finite certificate. The completed independent audit above is an exact
integer and informal proof audit, not a Mathlib or Lean verification.
