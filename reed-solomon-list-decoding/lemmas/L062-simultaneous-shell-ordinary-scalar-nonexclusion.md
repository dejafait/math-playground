# L062 — Ordinary scalar rows retain the simultaneous-shell witness

## Hypotheses

Use L053's 1024-point set H, all 68-subsets, positive singleton
rho=M/binomial(1024,68), M=(U+1)/2 and U=binomial(1024,64)/binomial(68,64).
Use precisely L021's a_i and L053's unchanged pairs:
p_0=1, p_1=...=p_4=0 and
p_i=a_i/(2 binomial(68,i)binomial(956,i)) for 5<=i<=68.
Fix a 68-subset D. Retain L056's complete anchored five-shell and
every L060 minimizing column at its unchanged parameter. Retain exactly
L061's anchored five/six-shell matrix and its 28-coordinate completion.

In addition impose every ordinary Schrijver scalar inequality on every
represented unordered triple, at all six ordered presentations, including
Boolean repetitions and presentations whose incident distances are
outside {5,6}. Preserve source permutation equalities, original t-s and
zeros for every forbidden nonzero half-distance 1,...,4.
Only these represented triples and this PSD matrix are considered;
no other conditioned/complement matrix, label constraint or global
moment extension is assumed. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-simultaneous-shell-ordinary-scalars.md`.

## Conclusion

L061's unchanged rational witness satisfies all these additional scalar
rows. Hence the prescribed simultaneous scalar-plus-PSD slice is feasible.
There are 121 relation types, 726 ordered presentations and 2178 scalar
rows. All pass. For distinct permitted triples, its largest ratio

  y/min(p_a,p_b,p_h) = 8015622621372853/4480701311136656929120 < 2/1000000,

where (a,b,h) are the three half-distances and y=x(triple)/rho.
Boolean and forbidden cases attain zero slack and are included.
The complete PSD remainder retains 20 positive and 29 zero modes.

This parks exclusion by these particular added ordinary rows at the
unchanged assignment. It is a finite reproduction of assessed methods,
not progress beyond the checked source results claimed as original.
Other ordinary rows on unrepresented triples, global PSD/moments,
actual labels, measures, packings and RS realization remain unresolved.
The 955–957 bracket and 67/68-agreement safety gap are unchanged.
The separate critical proof review below retains this strengthened conclusion.

## Proof

**Imported scalar theorem and normalization.** Import Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE Trans. Inform. Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p. 7, including the indicator explanation
after (65). Cross-check Hyun Kwang Kim and Phan Thanh Toan,
*Improved Semidefinite Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, III.A Remark 11 and III.B (31)–(35), conditions
(i)–(iv), printed pp. 8–9. The hypotheses even d>=4 and d<2w<=n
hold for d=10,w=68,n=1024. Foundations/04 retains the canonical theorem
and qualifications; no general theorem is reproved here.

At an actual ordered orbit (a,b,t,s), put h=a+b-t-s. Its conditional
pair-of-supports multiplicity is the positive integer

  O=multinomial(68;a-t,b-t,t) multinomial(956;a-s,b-s,s).

There are N*O ordered ground-set triples, N=binomial(1024,68).
For an invariant triple moment T, its linear ordered-count coordinate
is N*O*T. The source divides this by M*O, and M=N*rho.
Thus its coefficient is y=T/rho. This is an identity between the
normalizations, not an assertion that the moments have a measure.
Boolean repetition instead uses its pair moment, so y=p_h when two
supports coincide. The ordinary rows are exactly

  y>=0, p_a-y>=0, 1+y-p_a-p_b>=0.

All six presentations enforce all three pair upper bounds and all three
lower bounds. Source equalities preserve t-s and the distance triple.
Impossible multinomial orbits are not scalar variables. The suspect
complement prefactor in Schrijver (61) is unused. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof,
printed p. 2, supplies the union-index interpretation with the
constant-weight qualification in foundations/12. No hierarchy result
is reproved or strengthened program claimed feasible.

**Exhaustive finite dictionary.** For layers (l,m)=(5,5),(5,6),(6,6)
and 0<=i,j<=min(l,m), use L061's atom tuple in mask order 0,...,7,
with support bits D,E,G of weights 4,2,1:

  (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

All entries are nonnegative, sum to 1024 and give three 68-subsets.
The half-distances are l,m,l+m-i-j. The atom-bijection argument in
L061 proves that these 36+36+49 types exhaust the retained entries;
swapping the shells supplies the six/five rectangle. All distances
0,...,12 occur, so precisely p_0,...,p_12 are needed for these scalar
rows. The full pair prescription is retained without retuning.

Let d5 be exactly L056's normalized coefficients and t be exactly
L059's affine column evaluated at L060's unique minimizer s_*.
Let d6 be exactly L061's complete witness. Its 28 free coefficients
are z_(r,q)/v_(r,q), r+q>=6, with the exact z specified there and
v_(r,q)=binomial(6,r)binomial(62,r)binomial(6,q)binomial(950,q).
The diagonal is d6_(0,0)=1, forbidden coefficients are zero, and
d6_(r,5-r)=(p5/p6)*t_(5-r,r). The actual conditional moments are

  y=p5*d5_(5-i,5-j) on five/five,
  y=p5*t_(i,j) on five/six,
  y=p6*d6_(6-i,6-j) on six/six.

These are the same entries used in L061's PSD proof. In particular
d5,d6 themselves are not compared with p_a.

For each support order regenerate all eight atoms by permuting their
bits. Then a=atom4+atom5, b=atom4+atom6, h=atom2+atom6,
t=atom4 and s=atom3. Every presentation is an actual source orbit;
h=a+b-t-s and t-s=i-j in all six orders. Canonical minimum atom
tuples over the six orders identify unordered orbits; equal keys have
equal y across all types. This verifies closure even when the new
anchor has incident distances outside {5,6}, without adding a free
moment or another PSD matrix. Point permutations fixing D preserve
these full-region types, all pair distances, the ordinary rows and
the imported matrix. The witness is explicitly invariant; no averaging
of a labeled feasible point is used.

There are no further source equalities hidden by the full-atom check:
for a fixed ordered (a,b,h) and delta=t-s, the equations
t+s=a+b-h and t-s=delta uniquely determine t and s. These four
indices determine all eight atoms for three equal-weight supports.
Permuting (a,b,h) with unchanged delta therefore produces exactly the
six presentations already checked, including cross-type coincidences.

**Complete rational scalar check.** The finite recipes above specify
every rational quantity. All a_i are independently substituted into
L021's 64 defining equations Ax=1; all equations agree. Every required
p_i is regenerated from those a_i, including p_10,p_11,p_12.
They obey 0<=p_i<=p5 for 1<=i<=12, with p5=1/68881143660.

There are 12 Boolean presentations. Their pair coordinates give y=p_h;
all three ordinary rows pass, including zero upper/lower slacks at
coincident anchors. There are 228 forbidden presentations, all with
y=0. Each required upper row is therefore nonnegative. Their supports
are distinct, so all incident pairs have p_i<=p5 and the lower row
is at least 1-2p5>0. For every remaining distinct presentation,
exact substitution gives 0<=y/min(p_a,p_b,p_h)<= the displayed maximum.
All three upper rows thus pass. Moreover the lower row is at least

  1-2p5 = 34440571829/34440571830 > 0,

using y>=0. This covers every presentation. The overall minimum scalar
slack is exactly zero, and all 2178 saved slacks are nonnegative.

Run `python3 scripts/finite-support/simultaneous_shell_ordinary_scalars.py`.
Its complete certificate
`scripts/finite-support/simultaneous-shell-ordinary-scalars-results.json`
contains all 121 values, all 726 source indices, atom representatives,
positive orbit sizes, pairs, slacks, source hashes and all failures.
It constructs actual supports and checks the normalization identity
(N*O*rho*y)/(M*O)=y at every presentation. All 2530 reconstruction
checks pass; neither a sample nor an approximate solver is used.

Independently run
`python3 scripts/finite-support/verify_simultaneous_shell_ordinary_scalars.py`.
This imports no constructor or optimizer. It uses bit-permuted atom
formulas, extracts L056's manuscript coefficients, rebuilds L059's affine
column at the stationary point specified by L060's manuscript quadratic,
and consumes L061's unchanged complete rational z. It checks every
entry and every saved row, all Boolean/forbidden cases, all three pair
upper bounds and the uniform distinct lower bound. The exact largest
upper ratio above is taken over the complete permitted distinct set.
All 3191 independent checks pass. Full rows, exact extrema, complete
check names and failures are saved in
`scripts/finite-support/simultaneous-shell-ordinary-scalars-verification.json`.

**Same complete PSD witness.** Import audited L061's full finite PSD
extension, including its complete unequal-layer decomposition, transported
anchor and singular-Schur criterion. Rerun
`python3 scripts/finite-support/verify_simultaneous_five_six_shell.py`:
all 1928 independent substitutions pass. The new scalar verifier compares
every one of its 121 moments with this complete PSD certificate and all
28 z coordinates with the same witness. It consumes all 49 source
blocks, checks C55>=0, C56=0 when C55=0, and checks
C66-C56^2/C55>=0 when C55>0, otherwise C66>=0.
Every exact remainder agrees with the saved PSD certificate, retaining
20 positive and 29 zero modes. Thus scalar and PSD feasibility hold for
one assignment, rather than separate incompatible witnesses.

This finite nonexclusion does not imply a global extension, measure, code or list.
ATTEMPTS/015's old scalar pass is a different prescription; ATTEMPTS/043's
audited PSD-only stop is retained and now strengthened only on these rows.

**Separate critical proof review — step 209, 2026-10-14.** Reuse exactly
the supplied SPECIALIZE assessment
`drafts/literature/2026-10-14-simultaneous-shell-ordinary-scalar-critical-review.md`.
Its TARGET agrees literally with the startup Next action. This audit
retains the statement without a coefficient, hypothesis or scope repair;
it verifies a local reproduction, without asserting originality.

The source normalization is checked against foundations/04: the
invariant singleton is rho=M/N, each orbit has N*O ordered ground-set
triples, and its assigned ordered count is N*O*rho*y. Dividing by M*O
gives y, including zero moments. For every concrete ordered support
triple in the complete audited L061 representatives, direct set
operations recover a=|A\\B|, b=|A\\C|, h=|B\\C|,
t=|A\\(B union C)| and s=|(B intersection C)\\A|.
These are the source indices because
(A\\B) intersection (A\\C)=A\\(B union C).
They reconstruct the full mask-ordered atom vector as

  (956-a-b+s,b-s,a-s,s,t,a-t,b-t,68-a-b+t).

Independently count O by 68!*956! divided by the product of all eight
atom factorials. The quotient is a positive integer in every case and
agrees with the constructor's binomial count. This verifies the orbit
denominator instead of relying only on a cancelling normalization test.

To check every source equality, group all presentations by
(sorted(a,b,h),t-s). For each such key, minimizing its full atom vector
over support orders gives the same canonical vector and the same y,
including coincidences across layer types. Completeness follows from
t+s=a+b-h: for any ordering of the distances and fixed t-s, t and s
are unique, hence all atoms are unique. The six orders exhaust exactly
these possibilities, even when the new anchor lies outside the retained
five/six-shell matrix. Such presentations add scalar rows only; no PSD
or moment extension at that new anchor is inferred.

Every field of each constructor presentation and independent scalar row
is compared with fresh direct set counts and rational slacks. The independent largest distinct upper
ratio is the displayed fraction, attained at type (5,5,0,5) in all six
orders. The 12 Boolean and 228 forbidden presentations have the stated
lower-order values and zeros. All 2178 scalar rows pass; their minimum
slack is zero, and the uniform distinct lower bound agrees exactly.

Rerun the full L061 verifier and critical audit before the scalar audit.
L061's critical audit freshly solves the manuscript witness system, recovers all
28 coordinates and checks the unequal-layer normalization. The present
audit compares each of its 121 moments with that identical assignment,
compares every complete block with the PSD verifier, and rechecks all
49 singular-Schur remainders. The 20 old zero-mode cross entries vanish;
the remainders retain 20 positive and 29 zero values. Every weighted
two-layer bilinear Schur form has precisely the positive rescaling
N6/D6 of the corresponding source remainder. All 36 load-bearing
energy contributions also agree with the complete audited L060
quadratic at the same parameter; their sum, including p6^2, is E_min.
Thus source normalization, scalar signs and PSD belong to one witness.

Run `python3 scripts/finite-support/verify_simultaneous_five_six_shell.py`,
then `python3 scripts/finite-support/critical_audit_simultaneous_five_six_shell.py`,
then `python3 scripts/finite-support/verify_simultaneous_shell_ordinary_scalars.py`,
then `python3 scripts/finite-support/critical_audit_simultaneous_shell_ordinary_scalars.py`.
The first three reruns pass 1928, 3011 and 3191 checks respectively.
All 5884 additional critical checks pass. Full reconstructed rows,
extremal presentations, the identical witness, all PSD blocks, input
hashes and failure lists are saved in
`scripts/finite-support/simultaneous-shell-ordinary-scalars-critical-audit.json`.
The exact summary, failure list and extremal presentations were inspected
in full; the audit consumes every load-bearing row and block, not samples.
No repair was required. Only this fixed scalar-plus-PSD diagnostic is
parked; every previously stated global and realization gap remains open.

## Mathlib

Full matching finite scalar-plus-PSD certificate and its exact extrema:
not checked. Supporting finite-set, rational arithmetic, orbit and PSD
coverage: not checked. Unknown coverage is not evidence of absence.
