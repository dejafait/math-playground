# Finite-support threshold audit — 2026-09-25

## Gap and bounded target

The main gap is a sharp worst-case interleaved list bound for a specified
smooth-domain code, compared with epsilon* q. The source task at entry was
recovery of the July ABF definitions. Direct recovery failed; the
[pinned list model](../foundations/02-pinned-list-model.md) instead fixes readable
primary definitions and explicitly retains the ABF comparison as unresolved.
Only a source locator was read from the adjacent MCA notebook; no mathematical
result was imported from it. Existing work and inactive branches were preserved.

The one mathematical test in this audit is the field-size hypothesis needed by
elementary common-support counting. For a list with at least k simultaneous
agreements, a k-subset should determine the entire polynomial tuple. Test the
bound binomial(n,k)/binomial(n-t,k), uniformly in interleaving width, against
epsilon* q. At the next grid point after t=n-k, test the family of m-tuples
of scalar multiples of a polynomial vanishing on k-1 evaluation points.

Continue this as a useful partial input if both a uniform upper bound and an
explicit next-grid failure can be proved, with the extra q condition stated.
Abandon any claim of general completion if that condition is stronger than
mere existence of a safe radius. The plausible downstream use is an exact
large-field baseline and a quantitative target for bounds in smaller fields.
Sharp bounds there and the ABF source comparison would still be needed.

## Redundancy and prior failure

The active DAG had no lemmas. The previous attempt rejected direct transfer
from q^{O(1)}; this test uses an explicit bound independent of q instead.
ArkLib already supplies closed-ball floor cells and adjacent-grid semantics,
so those are cited as supporting facts rather than advertised as new research.
The finite-support count is elementary and no originality is claimed. It does
not duplicate or verify TR26-169's substantially stronger claimed polynomial
dependence on n at fixed slack. The cited preprints remain unreviewed.

## Result and threshold comparison

The reasoning was saved here before completion and then developed into the
full proof in [L001](../lemmas/L001-common-support-list-bound.md). The support
count and the q^m-word witness both pass the symbolic test. In particular,
q >= epsilon^{-1} binomial(n,k) certifies the adjacent pair t=n-k (safe) and
t+1=n-k+1 (unsafe), for every m>=1 and every finite-field characteristic.

The result also quantifies the gap left by this method. Existence of any safe
radius is equivalent to epsilon q>=1, whereas this sufficient capacity-grid
certificate requires an extra binomial factor. At fixed positive rate that
factor is exponential in n; L001 gives an elementary inequality proving this.
Neither the website's existence proviso nor a field-polynomial decoder bound
implies the new condition. The n-polynomial claim in TR26-169 is materially
stronger at fixed slack and is not established by this argument.

For the pinned closed-ball convention, a grid boundary is not an attained
largest safe real radius: the latter safe set has an open right endpoint.
ArkLib already states that distinction. The unresolved ABF comparison prevents
treating it as a disproof of the source challenge, and the unknown boundary
for the remaining fields prevents a complete grid resolution.

## Checks and assessment

Reproduction: `python3 scripts/finite-support/verify.py`.
The saved [exact results](../scripts/finite-support/results.json) cover seven
prime-field cases, all received words up to a justified code-translation
symmetry, interleaving widths 1 and 2, k=1, k=n, a nonintegral threshold, and
epsilon q<1. All checks passed. For n=4, k=2 over F_5, the maxima at integer
radii 0 through 4 are [1,1,6,17,25] for m=1 and [1,1,6,97,625] for m=2.
Over the multiplicative subgroup {1,5,12,8} of F_13, m=1 and epsilon=1/2
give t_star=2, as the sufficient condition predicts. These are toy checks,
not evidence at epsilon*=2^-128 or a substitute for the proof.

The informal review checked positivity of binomial(n-t,k), uniqueness of the
whole tuple on a common k-subset, distinctness and degree of all q^m witness
tuples, inclusion of zero, and all endpoint inequalities. The DAG gains one
node with no local lemma inputs; the proof uses only elementary field and
polynomial facts. No original-result or global Mathlib-coverage claim is made.

This step is ADVANCE because it establishes a quantitative partial input and
an exact restricted grid boundary. It is not a complete candidate resolution.
The exploration streak is zero. The assessment is to retain this exponential
baseline and direct subsequent work toward the claimed geometric improvement
in field-independent list size, rather than infer a stronger q condition from
the website or repeat failed PDF retrieval indefinitely.
