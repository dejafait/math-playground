# L171 — An exact-rank-one survivor for saved span 274

## Hypotheses

Let E be any extension field of F_97, including its algebraic closure.
Use the increasing coordinate sets

    S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96).

Index supports A=I union K by the lexicographic pairs in S (outer)
and J (inner), zero-based: label a has I at index floor(a/36) and
K at index a modulo 36. Select exactly the history

    T=(0,51,98,177,318).

Use L109's original maps. Namely O_a=S minus I_a, z_a=min(O_a),
g_a(X)=product_{y in J minus K_a}(X-y), and

    c_ax(w)=g_a(z_a) w_x-g_a(x) w_z_a   (x in O_a minus {z_a}).

The rows of Q_a are these covectors in increasing x order; N_a has
entries c_ax,i c_ay,j-c_ax,j c_ay,i for increasing covector pairs x<y
and increasing S-coordinate pairs i<j. All coefficients lie in F_97.
No coding realization, recovered-weight, finite-chart or extension-degree
condition is assumed.

## Conclusion

The plane L=span_E(e_1,e_22) supplies a nonzero decomposable wedge
p=e_1 wedge e_22 with N_a p=0 and rank_E(Q_a restricted to L)=1
for every a in T. In particular the exact-rank-one geometric locus
for this history is nonempty over F_97 and over its algebraic closure.
It cannot be excluded by proving that locus empty.

The point is the third saved kernel basis vector of span 274, and the
selected node 1006 has history T and span 274. This conclusion neither
identifies the full locus nor supplies full-weight recoveries, twelve
rows, a coding event or a challenge counterexample. It removes no
saved-cover obligation. Classification: REPRODUCTION of the approved
geometric gate on one instance, with an informative negative outcome
for the proposed exclusion route; no source-level novelty is claimed.

## Proof

### Exact label binding and known method

Lexicographic indexing gives the following complete selected table.
Here output coordinates of Q_a are indexed by the displayed increasing
O_a minus {z_a}, and arithmetic is modulo 97.

| a | I_a | K_a | z_a | O_a minus {z_a} | Q_a e_1 | Q_a e_22 |
|---|---|---|---|---|---|---|
| 0 | {1,8} | {47,50} | 12 | (18,22,27,33) | (0,0,0,0) | (0,44,0,0) |
| 51 | {1,12} | {64,70} | 8 | (18,22,27,33) | (0,0,0,0) | (0,59,0,0) |
| 98 | {1,18} | {75,79} | 8 | (12,22,27,33) | (0,0,0,0) | (0,93,0,0) |
| 177 | {1,27} | {85,89} | 8 | (12,18,22,33) | (0,0,0,0) | (0,0,63,0) |
| 318 | {8,22} | {79,85} | 1 | (12,18,27,33) | (75,8,25,44) | (0,0,0,0) |

L109 supplies the exterior-minor identity and nonzero-wedge
reconstruction. The ready assessment imports the standard minor/rank
criterion, as in Stacks Project, Lemmas 15.8.4(3) and 15.8.7,
[Tags 07ZA](https://stacks.math.columbia.edu/tag/07ZA) and
[07ZC](https://stacks.math.columbia.edu/tag/07ZC).
The specialization is to these five four-by-two restriction matrices
over the field E; ranks zero and one must still be separated. No
general rank, Grassmannian or Nullstellensatz theorem is reproved.
No source in the reused comparison disposes of this numerical history,
so its explicit point and original-map identities need checking.

### Point and all five open conditions

The vectors e_1 and e_22 are independent over E. Their wedge has
p_(1,22)=1 and all other increasing exterior coordinates zero. Thus
it is nonzero, decomposable, and satisfies every one of the 35
Plucker equations. This is already a normalized exterior chart; no
other chart is needed to demonstrate existence.

For each of the first four rows, 1 belongs to I_a, so Q_a e_1=0.
The label 22 belongs to O_a minus {z_a}, and the z_a coordinate of
e_22 is zero. Therefore Q_a e_22 has precisely the one entry g_a(z_a)
at x=22. That entry is nonzero because S and J are disjoint, so every
factor z_a-y in its defining product is nonzero. In particular these
four restrictions each have rank exactly one over every E, not zero.
The values 44,59,93,63 in the table are direct product evaluations;
the nonvanishing proof does not depend on trusting those computations.

For row 318, 22 belongs to I_318, so Q_318 e_22=0. Its pivot is 1,
and for x in (12,18,27,33) the e_1 image is -g_318(x). Each entry is
nonzero by the same disjointness argument. Its values are (75,8,25,44).
This restriction also has rank exactly one.

In each row one of the two image columns is zero. Thus every two-by-two
restriction minor vanishes, and L109's identity gives every entry of
N_a p=0. The displayed nonzero entry in the other column witnesses an
allowed principal open for each row. All five opens hold at this same
point. There is no saturation, finite-field equation, discarded zero
branch or unproved ideal-properness inference. The point already lies
over the prime field; no irreducible extension polynomial or descent
argument is required. This proves the conclusion.

### Saved-input provenance and certificate verification

The complete selected values in `scripts/pair-free-envelope/cover.json`
give node 1006's history T and span 274. The span's generating history
is instead (0,51,98,143,318); no inference about row gates is made by
replacing T with that history. Its third saved basis vector is exactly p.
The selected basis agrees with `scripts/pair-free-envelope/verification.json`,
whose certificate hash binds the saved cover. The separate selected
occurrence in `scripts/residual-domination/verification.json` agrees
with node 1006. L170's domination result is not used. Completeness of
the saved kernel is not needed for this existence proof: the original
five N_a p identities and five rank-one tests are checked directly.

Run `make -C scripts/span-274-geometry check`. The producer writes
`scripts/span-274-geometry/survivor.json`, including the exact selected
Q/N maps, g evaluations, wedge, all 35 Plucker residuals, all 30 block
residuals, five restriction matrices and nonzero-entry witnesses, plus
input hashes. It compares the complete selected maps with the saved
original blocks. The verifier imports no producer code: it expands
each product polynomial, uses Horner evaluation, reconstructs every
selected Q/N coefficient and verifies every equation and nonzero entry.
Its full evidence is `scripts/span-274-geometry/verification.json`.
All 35/35 Plucker equations, 30/30 block equations and 5/5 exact-rank-one
gates pass, with no failures. Both implementations share Python and
F_97 arithmetic; no proof assistant verification or later critical
audit is claimed. The symbolic argument above independently covers
nonvanishing and extension fields. No new stack/extension rank test,
traversal, cover edit or pruning was performed; all 1665 frontier
obligations remain. The historical block-test cap stays exhausted.

The invocation-start assessment is
`drafts/literature/2026-10-28-span-274-rank-one-emptiness-test-review.md`.
This satisfies its prescribed survivor stopping test. The omitted
full-weight and chart conditions remain separate unresolved gates;
nonemptiness of this weaker locus is not coding feasibility. Uniform
twelve-row exclusion and the main challenge remain unresolved.

## Mathlib

Full matching theorem for this history and saved span: **not checked**.
Supporting finite-field, exterior-coordinate, Plucker and matrix-rank
coverage: **not checked**. Unknown coverage is not evidence of absence.
The precise known rank inputs and their local specialization are recorded
above; no matching Mathlib result is claimed.
