# Step 545 — source scope for the L126 conceptual audit

Literature-only, 2026-10-28. The initial extraction checkpoint was saved
before further source reads; this is the completed source comparison.
No lemma, calculation, mathematical script or proof audit is performed
in this step. The saved exact target is the assessment's TARGET.

The main gap is ordinary uniform worst-case P versus NP. The intermediate
target is a critical audit of L126's full-relation generating-set support
obstruction. If sound, it rules out one full-relation common-source route
to the unary fourth comparison; it says nothing about smaller invariant
boundary-receiving subspaces or arbitrary chains. Continue to that audit
only after adequate source comparison. In the later audit, a failed
induction case, coordinate identification or basis charge requires repair
or withdrawal of that specific claim; success validates only its stated
restricted obstruction, not a main-problem solution.

## Local scope and preserved work

The supplied overview and DAG were used before detailed proof reads.
Notebook-scoped Git status showed substantial pre-existing work, preserved.
Read L126 hypotheses/conclusion and complete §§1–4 to identify the exact
source question, not to certify its proof; L125 §2's parameter passage;
the prior ready residual-relation assessment and its step-541 source note;
Attempt 059 and history 544. A targeted search of the 28-Oct assessments,
working notes, Attempts 058/059 and histories 543/544 found the explicit
support-product claim in L126/step 544 and its pending gate, with no
separate inspected source comparison. Earlier failure comparisons and
simulation/sparse-null-basis coverage are reused, not repeated.

The source question is: for nonzero multilinear f over F₂, with ordinary
total degree d and monomial count s, is s(f)s(f(1+X)) >= 2^d covered by
known results? The audit also needs the original-coordinate Pascal row
convention and a one-charge-per-row determinant argument. No derivation
of any of these is supplied by this literature step.

## Inspected primary sources

Inspected Forbes–Shpilka–Tzameret–Wigderson, *Proof Complexity Lower Bounds
from Algebraic Circuit Complexity*, author PDF dated 26-Sep-2021,
§6.3.3 Theorem 6.6/Corollary 6.7, pp.63–64, and §6.4 Proposition 6.8,
pp.64–65, with its full induction. [Author PDF](https://www.math.ias.edu/~avi/PUBLICATIONS/FSTW-toc21-ccc16.pdf).
Theorem 6.6 bounds the number of variables in the trailing monomial of
an s-sparse polynomial after a full-support translation by log₂(s).
Corollary 6.7 bounds sparsity of nonzero multiples of products of shifted
variables. Proposition 6.8 says a nonzero multiple of a nonzero
multilinear polynomial has at least its sparsity, over any field. Read
the nonzero-multiple qualification, translation/nonvanishing argument,
and induction's extreme-coefficient cases, including a zero end block.
These are not the displayed two-representation product bound or an
arbitrary E_N-basis theorem. No unproved reduction to them is assumed.

Followed its reference [20] to Michael A. Forbes, *Deterministic
Divisibility Testing via Shifted Partial Derivatives*, author manuscript
16-Apr-2015, [primary PDF](https://www.ias.edu/sites/default/files/math/csdm/14-15/Forbes2015.pdf).
Inspected Corollary 5.6, Lemma 5.11 and Theorem 5.13 with its proof,
pp.25–29. Theorem 5.13 is the full-support translated trailing-monomial
bound quoted above, not a statement about an arbitrary highest-degree
monomial. Its proof compares a shifted differential-operator space with
the derivative space of that trailing monomial. No transfer to the
particular L126 weight filtration is imported. Supporting lemmas were
read to identify scope, not independently certified.

Bläser–Dutta–Dutta–Jindal, *Deterministic Shift Equivalence Testing for
Sparse Polynomials*, [arXiv:2610.27168v1](https://arxiv.org/pdf/2610.27168v1):
read Theorem 1.3, p.4, its field restriction on p.4, Lemma 3.1 and its
complete cone-closed interpolation proof, and Lemma 3.2's complete
shifted-Euler-operator isolation/support-count proof, pp.14–17. Theorem
1.3 states that f(X+a)=g(X), with sparsities s,t, implies
product_{i in supp(a)}(γ_i+1)<=st for every monomial X^γ of f or g.
Its stated extension is characteristic zero or characteristic greater
than the total degree; it does not cover all degrees over F₂.
This is a close overlap, not an import for L126. No small-characteristic
extension is derived here. Whether multilinearity permits such an
extension is outside the approved audit target. Thus no originality
claim for the support-product mechanism is warranted.

Borello–Solé, *The uncertainty principle over finite fields*,
[arXiv:2007.04159v2](https://arxiv.org/pdf/2007.04159v2), 23-Mar-2021:
read §§2.2–2.3, pp.3–4, and §5 Proposition 2 and its full proof, p.7.
For nonzero f in F_q^n, it gives wt(f)wt(f-hat)>=n with gcd(n,q)=1;
f-hat is Mattson–Solomon evaluation at primitive n-th roots. The proof
uses the BCH exclusion of consecutive zero intervals, separately when
wt(f) divides n and when it does not. The transform and coprimality
requirements differ from the dyadic characteristic-two Pascal transform.
No application or contradiction to L126 follows from this source.

## Bounded search log and unread leads

Actual query strings, grouped in the order submitted:

- `multilinear polynomial sparsity f(x+1) uncertainty principle degree finite field monomials`
- `"polynomial" "sparsity" "translation" "uncertainty"`
- `"Sierpinski" "uncertainty" support`
- `"sparsity" "shift" "multilinear" "2" Forbes Shpilka Tzameret Wigderson`
- `"uncertainty" "Möbius" "Boolean" support polynomial`
- `"sparsity" "f(x+1)" polynomial degree`
- `"multilinear" "sparsity" "two" "shifts"`
- `polynomial "sparsity" "shift" "degree" "Volkovich"`
- `"multilinear" "sparsity" "translation" "product"`
- `"polynomial" "sparsity" "2^d" "shift"`
- `"polynomial" "sparsity" "support-product"`
- `"Deterministic divisibility testing via shifted partial derivatives" Forbes pdf`
- `"multilinear" "shift" "sparsity" "product" uncertainty principle`

Search also surfaced sparse-shift algorithms over Q, finite-field Fourier
sparsity of Boolean functions, and Bhargava–Sengupta ECCC TR26-283 on
sparse affine orbits. Their theorem/proof passages were not inspected;
none is a premise, present-day optimality assertion or claimed obstruction
here. No exhaustive literature coverage or novelty is asserted. No
essential source is inaccessible, and no cross-notebook theorem is used.
Full matching Mathlib coverage is not checked; previous supporting
linear algebra comparisons are not a matching quantitative theorem.

## Decision and precise audit obligations

The unchanged target's assessment becomes EXPLORE. This step supplies
the previously missing exact-claim comparison, including a close result
with a different field scope. The independent characteristic-two induction
in L126 remains necessary unless a matching citation is later established;
its rechecking is justified, not a claim of a new mathematical discovery.
No extra general simulation search is needed before that audit.

The audit must use complete L126 §§1–4, L125 §2 and L122 §2, together with
the complete relevant step-544 certificates (not bounded previews as
proof). Check all zero/degree cases in (4), simultaneous translation and
row orientation, cancellation in bP_N, and one determinant charge per
row, with six unit directions and the paired final direction. Retain
full E_N spanning, F₂, all original coordinates and S=16N+20. Finite
replay cannot certify the all-variable argument. No new proof or script
is supplied and no existing mathematical claim is accepted or retracted.
The source gate is ready for the next invocation's conceptual audit.
