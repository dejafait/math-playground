# Three-support constrained actual-pencil test

Date: 2026-10-04. One mathematical attempt on the exact saved actual-pencil
COVERED_TARGET in the [ready SPECIALIZE assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).
Its adequate algebraic coverage is reused; no further literature is needed.

## Gap, intermediate target and stopping test

The pinned four-omission interval remains 11/q–16/q against an allowable
fifteen. The previous five-coordinate generator is stopped. This test
starts with two four-error supports whose union has six, seven or eight
coordinates and solves a third support constraint. Six explicit triples
have total unions of size nine through twelve. This changes the generator
from sampling unconditioned weights to solving sparse-syndrome incidence.

For each triple, a fourth support will produce a small determinantal
candidate equation. Every retained actual pencil must pass L010's
nonpersistent hypotheses and the complete L014 coefficient, simplicity,
determinant and exact F_(97^20) splitting gates. An equality witness would
settle unsafety for this pinned cell. A restriction valid for arbitrary
coefficients would narrow its equality case. A search with no such result
is EXPLORATION, even if it finds many four-point pencils. It cannot prove
a global fifteen bound. July correspondence and other radii remain open.

## Saved unfinished calculation

Write V_A for the eight-by-four matrix with columns
(x,x^2,...,x^8) at x in A. If e_0,e_1,e_2 have prescribed four-element
supports A_0,A_1,A_2 at parameters 0,1,2, their weights satisfy

    -V_(A_0) e_0 + 2 V_(A_1) e_1 - V_(A_2) e_2 = 0.

The twelve-variable matrix has rank eight when the union contains at
least eight coordinates, by L010's Vandermonde argument. Its kernel
therefore has dimension four over the base field and every extension.
For a kernel vector z, put s(T)=(1-T)V_(A_0)e_0+T V_(A_1)e_1.
All twelve weights must be nonzero to realize the specified supports.

For a proposed fourth four-set K with polynomial f_K(X)=product_(x in K)
(X-x)=sum_j f_j X^j, membership s(t) in its four-dimensional moment
space is exactly the four recurrence equations

    sum_(j=0)^4 f_j s_(i+j)(t)=0, i=1,...,4.

Necessity follows by evaluating f_K on its roots. For sufficiency,
solve the first four moments by the invertible Vandermonde matrix on K;
the recurrence then gives all eight moments. Applied to the four kernel
coordinates, this gives M_K(T)=M_0+T M_1, a four-by-four matrix.
Its determinant has degree at most four. A root with one-dimensional
kernel gives a single projective choice of the twelve weights. Zero
determinants and larger kernels must be recorded separately, rather than
silently treated as excluded. This is a direct implementation of the
already covered moment/locator tools, not a new general obstruction.

The bounded computation will enumerate all fourth supports for the six
fixed triples, solve determinant roots in F_97, retain one-dimensional
kernels with all prescribed weights nonzero, and deduplicate actual
projective moment lines. It does not enumerate the four-parameter family
over F_(97^20). Nonrational roots, identically zero determinants and larger
kernels are unsearched branches. Prime-field candidates nevertheless
receive exact extension-field splitting tests.

This file saves the setup before the longer computation. No candidate,
bound improvement or class exclusion is asserted at this point.

## Completed finite test

`python3 scripts/coefficient-feasibility/three_support.py` records
[the exact results](../scripts/coefficient-feasibility/three-support-result.json).
Each layout tests all 1817 fourth supports different from its first three.
Five scalar determinant evaluations, computed independently by elimination,
check every coefficient of each degree-at-most-four determinant. Every
retained root is checked by solving the fourth support's Vandermonde
system and comparing all eight moments, with all sixteen error weights
nonzero. Projective moment lines are deduplicated by normalized minors.

| Layout | First two union | Triple union | Zero determinants | New lines | Unsearched nonprime target-field roots |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 6 | 9 | 1817 | 0 | 0 |
| 1 | 6 | 10 | 858 | 519 | 172 |
| 2 | 7 | 9 | 1109 | 427 | 0 |
| 3 | 7 | 11 | 469 | 896 | 400 |
| 4 | 8 | 10 | 826 | 623 | 258 |
| 5 | 8 | 12 | 4 | 1105 | 402 |

The 10902 matrices generate 3570 distinct actual nonpersistent moment
lines. To avoid a loss of degree caused only by a sparse point at infinity,
choose an old parameter tau with D(tau) and all ell_x(tau) nonzero.
There are at most 68 excluded prime-field values, so such a tau exists.
Replace a,b by a,a+tau*b. The homogeneous minor identity gives
L_new(T,X)=(1+T)^4 L_old(tau*T/(1+T),X), interpreted as a polynomial;
every new coordinate locator has degree four. This change keeps the
projective syndrome line and chooses a nondecodable point at infinity.

All 3570 products fail the fourth-power identity, hence none satisfies
L010's sixteen-count equality criterion. The implementation also calls
the full equality check, keeping coordinate simplicity, D-nonvanishing
and exact splitting separate. This is an exclusion of these supplied
pencils, not of their entire triple families or arbitrary extension inputs.

For an exact four-error count even when an unrelated coordinate root is
repeated, replace each ell_x by its squarefree radical and multiply those
sixteen radicals. A root's multiplicity in that product counts distinct
coordinate incidences. Its multiplicity-four factor, with D-roots removed,
is precisely the regular four-error parameter polynomial by L010. Take
its gcd with T^(97^20)-T by modular Frobenius. If the original locators
have gcd one, no weight-at-most-three parameter exists, since such a
parameter would vanish at all sixteen locators by L010.

This gives exact total counts for 3530 pencils: 3483 have four bad
parameters, 29 have five and 18 have seven. For the other 40 pencils,
lower-weight roots remain unclassified; only their four-error count is
reported. The largest fully counted pencil has seven bad parameters,
all already in F_97. Its independent actual-minor recomputation, affine
recurrence check and interpolation on all 2517 admissible supports agree
on parameters {0,2,21,27,28,40,49}. Seven improves no existing bound:
the certified eleven-count C013a witness remains stronger.

## Why the zero-determinant branch is essential

The first triple is
A_0={1,8,12,18}, A_1={1,8,22,27}, A_2={1,33,47,50}.
All three contain x=1. There is a nonzero polynomial weight vector in
the triple kernel supported only at x: take e_0(T)=T*delta_x,
e_1(T)=(T-1)*delta_x and e_2(T)=(T-2)*delta_x. The identity
-e_0+2e_1-e_2=0 holds. Evaluating the candidate syndrome at the same
indeterminate T gives

    (1-T)*sigma(e_0(T)) + T*sigma(e_1(T)) = 0.

The four-dimensional triple kernel has a constant base-field basis,
so this weight vector supplies a nonzero polynomial kernel vector of
every M_K(T). Thus every fourth determinant vanishes identically over
every extension, independent of K. This exactly explains the 1817 zero
determinants for layout 0. The control in the script checks both
polynomial identities for all eight moments.

These weights violate the full twelve-weight gate. Their existence does
not say whether the same matrix has an admissible vector. In particular,
zero determinant is neither a witness nor an impossibility result. The
full test leaves 5083 zero-determinant systems, one larger prime-field
kernel and 1232 nonprime determinant roots in F_(97^20) unsearched.
The last count is of root occurrences across matrices, not distinct
pencils. The determinant-only generator is blind to this shared-coordinate
family; larger kernels need full-support conditions after the compulsory
zero-syndrome kernel is removed. This diagnosis concerns the candidate
generator, not L010's locator bound or the MCA event.

## Outcome and continuation decision

Outcome: EXPLORATION. The test creates no new lemma, bound improvement,
arbitrary-coefficient exclusion or complete candidate. It implements the
covered moment/recurrence and resultant tools; no progress beyond the
checked literature or originality is claimed. The main gap remains
11/q–16/q against fifteen, with July correspondence independent and parked.

Stop repeating the one-dimensional prime-field determinant-root
enumeration. Within the same preapproved actual-pencil target, the next
direction is the saved common-coordinate triple: remove its compulsory
zero-syndrome kernel and impose the full-weight fourth-support conditions
through smaller minors before any resultant/equality audit. This is a
concrete untested branch, not a claim that it succeeds. No such calculation
is performed in this step. Consecutive uninformative mathematical turns
used: one; resultant-target mathematical attempts: four. Prior orbit,
two-block, five-coordinate and July/four-block stops are preserved.

## Mathlib

Full constrained candidate generation, root enumeration and shared-coordinate
kernel analysis: **not checked**. Supporting resultant product and
specialization coverage is **present** in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[Polynomial.resultant_prod_left](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[Polynomial.resultant_map_map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
These are supporting ingredients, not a full matching theorem. Kernel,
determinant and recurrence implementation coverage elsewhere is **not checked**.

The resultant identity is imported from Milne, *Fields and Galois Theory*,
v5.10, Proposition 4.35(b), [printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58);
exact-field splitting uses its finite-field discussion on printed p. 53.
Squarefree multiplicity recognition is covered by Volkovich,
*On Some Computations on Sparse Polynomials*, Lemmas 23–24,
[p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
These precise citations were already read in the saved assessment and are
reused here. No new source review or Lean verification was performed.
