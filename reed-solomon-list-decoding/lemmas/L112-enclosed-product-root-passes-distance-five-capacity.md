# L112 — Enclosed positive product root passes the distance-five capacity

## Hypotheses

Use the exact fixed-pair data of L021 and L098 on all 68-subsets of a
1024-point set:

    N=floor(65537^28/2^128)+1, H=binomial(1024,68),
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i) for 5<=i<=68.

Here a_i is L021's canonical exact rational primal vector, with
sum a_i=U-1 and every a_i>0. Put d_i=(N-2)c_i>0 for i>=5.
Use L111's full 64 polynomial equations (7), with every actual source
orbit and D from L098/L109. Upper capacities, Boolean lower scalar
rows, PSD, a representing distribution and RS realization are not
assumptions. The factors below are an enclosed root, without an assertion
that all positive roots have been enclosed.

## Conclusion

There is a finite positive real root x=(x_5,...,x_68) of all 64 original
distinct-edge contractions, in the explicit rational box specified below.
It is unique in that box. For every equilateral distance-five triangle,
its product weight satisfies

    0 < x_5^3/c_5 <= B_5 < 1,

where B_5 is the exact rational `capacity.upper_cube_ratio` in
`scripts/finite-support/positive-factor-enclosure-verification.json`.
Numerically both enclosing cube ratios are approximately
1.0717885622052142*10^-11; these decimals are descriptive only.
This passes exactly this one upper-capacity test. Restoring repetitions
and null cases gives all 69 original contractions as in L111.

This is a REPRODUCTION of a standard validated-enclosure method for this
finite system, a local quantitative advance without an originality claim.
It does not certify any other capacity, Boolean lower row, full source
lift, PSD, packing or RS list. Global positive-root uniqueness is not
claimed. The 955–957 bracket and the separate stops of L110 and
ATTEMPTS/082,093 remain unchanged. A dedicated critical proof audit of
this application is not claimed by its independent arithmetic check.

## Proof

**Imported criterion and applicability.** Import Siegfried M. Rump,
*Verification methods: Rigorous results using floating-point arithmetic*,
Acta Numerica **19** (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Theorem 13.3 and full proof, author p.89; interval arithmetic is covered
by §5.3–5.5, (5.14)–(5.17), author pp.27–28. The inspected source and
qualifications are recorded in foundations/14. If J encloses the full
Jacobian on a+E, then

    -R F(a)+(I-R J)E contained in int(E)

gives a root unique in a+E and nonsingularity of R and all enclosed
Jacobians. Failed inclusion has no converse. We import this theorem
without reproof. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-positive-factor-enclosure-implementation.md`.
Our F below is a rational polynomial on R^64, hence continuously
differentiable on every box. All interval endpoints and arithmetic
bounds are rational. No numerical inverse is assumed nonsingular.

**Exact polynomial and invertible scaling.** Let K be the positive
integer satisfying K^3(N-1)<=H<(K+1)^3(N-1). For each i>=5 choose
the integer p_i such that 10^p_i<=K*c_i<10^(p_i+1), set s_i=10^p_i,
and write x_i=s_i*u_i. These rational positive scales are fixed by
`scale_powers` in `scripts/finite-support/positive-factor-enclosure.json.gz`.
They give an invertible diagonal change of all 64 coordinates.

For fixed i, aggregate D over identical product monomials u_j*u_h,
where h=i+j-t-s, only j,h>=5 and the full original t,s ranges occur.
Store A_(i,j,h) for j<=h as the sum of D from all ordered source entries
with that unordered pair. In particular unequal j,h include both orders
when they occur; equal indices are counted with their actual multiplicity.
The resulting normalized system is

    F_i(u)=-1+sum_(j<=h) b_(i,j,h)*u_i*u_j*u_h,
    b_(i,j,h)=A_(i,j,h)*s_i*s_j*s_h/d_i.                 (1)

There are 81,355 nonzero coefficient entries. All b are positive rational
numbers, represented exactly by the saved integers A and the rational
scales and demands. This is precisely each original equation (7), divided
by its positive d_i. No equation, gauge or variable is removed. The
source row is recovered by multiplying F_i by d_i and substituting
u_i=x_i/s_i. Aggregation is legitimate for this product polynomial;
it asserts no equality of general source variables at different t-s.

**Full source reconstruction.** The independent checker reconstructs
all coefficients from four-region occupancies. For a fixed edge at
distance i let Z contain r points from its common region, p from A\\B,
v from B\\A and o from the outside region, where

    0<=r<=68-i, 0<=p,v<=i, o=68-r-p-v, 0<=o<=956-i.
    j=68-r-p, h=68-r-v, t=i-p, s=v,
    D=binomial(68-i,r)binomial(i,p)binomial(i,v)binomial(956-i,o).

The inverse r=68-i-j+t, p=i-t, v=s, o=j-s gives a bijection with the
original ranges. The checker compares each D to the original formula.
At each entry it verifies nonnegative eight-atom sizes, all three anchor
multiplicities g_i*D and all three singleton-minus-opposite-pair values
t-s. Swapping the two nonanchor supports preserves the symmetric
multinomial count, so these checks cover six presentations, including
repeated distances. No division by six is used in a fixed-edge equation.

All 1,500,625 actual entries are reconstructed: 205 repeated entries,
10,220 distinct null-edge entries and 1,490,200 permitted distinct
entries. Their complete aggregated coefficients equal the constructor's
array. For every i,j their total D is g_j, including omitted null and
repeated entries. At i>0 the two repetitions are exactly (j,t,s)=(0,0,0)
and (i,i,i), D=1 each, and restore 2*c_i. Null-edge rows are zero
identities. At i=0, all entries are repeated, D=g_j and the row is
sum_j g_j*c_j=N. The checker verifies this normalization exactly.
Thus the source conversion preserves all 69 contractions as soon as
(1) has a positive root; no scalar inequality or PSD follows from it.

**One proposed point and box.** The saved working record is
`drafts/2026-10-23-positive-factor-enclosure-working.md`. Before computation
it fixed Decimal precision 90, initial x_i=K*c_i, at most 100 damped
Newton iterations with at most 20 step halvings, residual target 10^-65,
and execution budgets. Exactly one trajectory ran. It reached the target
in four iterations, with maximum normalized numerical residual about
2.289*10^-68. This only proposed a candidate and preconditioner.

Put Q=10^70. The certificate stores 64 integers q_i (`point`) and
4096 integers r_ik (`preconditioner`). Define exactly

    a_i=q_i/Q, R_ik=r_ik/Q,
    E_i=[-10^-45,10^-45] for every i,
    B_i=[(q_i-10^25)/Q,(q_i+10^25)/Q].                  (2)

The candidate and its proposed inverse were rounded once to this common
denominator. Only this one rational box and preconditioner were used.
Every B_i has strictly positive lower endpoint. Its x-image is
s_i*B_i; positivity and the invertible scaling have been checked exactly.

**Complete rational enclosure.** Each coefficient b is enclosed by
[floor(Q*b)/Q,ceil(Q*b)/Q]. Addition uses endpoint sums. For multiplication
of intervals with endpoints in integer Q-units, form all four integer
endpoint products, divide their minimum downward and their maximum
upward by Q. These operations enclose the exact rational operation,
including at negative endpoints; no floating-point rounding is used.

Evaluate every monomial of (1) at a to enclose F(a). Enclose its derivative
on B by the product rule on all three factor occurrences. In particular
if indices repeat, each occurrence contributes separately. The saved
full residual, 64-by-64 Jacobian interval J, -R F(a), I-R J and Krawczyk
image are checked entry by entry. Each operation is independently
reconstructed by a checker importing no constructor routines. Its
coefficient reconstruction uses the separate occupancy enumeration above.
The complete 64 strict margins are saved, without sampling. In units 1/Q,

    min_i min(S_i.lower+10^25,10^25-S_i.upper)
      = 9999999999999999999196016 > 0.                (3)

Here S=-R F(a)+(I-R J)E. As an additional recorded bound, the largest
row sum of maximum absolute endpoints of I-R J is exactly bounded by

    21421458450760567325986134 / 10^70.

The strict inclusion (3), the complete derivative enclosure and positive
box meet every hypothesis of the imported theorem. Consequently F has
a unique root in B, and its diagonal image x solves all original
positive-distance equations. This establishes a local enclosure, not
a classification of roots in the positive orthant.

**The single capacity comparison.** The box yields rational endpoints

    l=s_5*(q_5-10^25)/Q > 0,
    u=s_5*(q_5+10^25)/Q.

(The first saved array index corresponds to distance 5.) The checker
reconstructs the complete fractions l^3/c_5 and u^3/c_5 from the canonical
c_5 and the box; these are saved in full as `capacity.lower_cube_ratio`
and `capacity.upper_cube_ratio` in its regular JSON certificate. It
compares them exactly with one. Both are positive and the upper is
strictly below one. Cubing is increasing on positive reals, so the
root satisfies 0<x_5^3/c_5<=u^3/c_5<1. This uses the full root enclosure,
not L110's equilateral-only marginal allowance. It concerns just the
actual equilateral side class (5,5,5), whose realizability is retained
in the full source enumeration. Other side classes were not tested
against capacities in this step.

Reproduce from this notebook, respecting the one-trajectory contract:

    python3 scripts/finite-support/positive_factor_enclosure.py
    python3 scripts/finite-support/verify_positive_factor_enclosure.py

The complete construction artifact is
`scripts/finite-support/positive-factor-enclosure.json.gz`; the independent
check is `scripts/finite-support/positive-factor-enclosure-verification.json`.
The latter binds its input by SHA-256, reports 4,100,192 checks and zero
failures, and retains all 64 margins and exact capacity fractions. Its
arithmetic check finished within the predeclared budget. The complete
relevant exact evidence, including both full capacity fractions, was
inspected; a preview or numerical residual is not the proof.

No capacity for another side class, Boolean lower row, omitted source
condition or global uniqueness is inferred. This result does not resolve
L098's shared capacitated feasibility or arbitrary-center safety.

## Mathlib

Full matching Krawczyk theorem and this 64-factor enclosure: not checked.
Supporting rational interval arithmetic, polynomial differentiation,
finite subset counts and fixed-point results: not checked. Unknown
coverage is not absence; no uninspected Mathlib theorem is used.
