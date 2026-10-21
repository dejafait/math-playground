# L060 — fixed conductor-36 central value and rank zero

## Hypotheses

Let E/Q be the globally minimal model y^2=x^3+1, with minimal
differential dx/(2y), conductor 36 and normalized newform f as in L050.
Use L052's degree-one optimal identification and absolute differential
scale one. Let Omega(E)>0 be the total real minimal period, without
replacing it by a half-period. Use L056's audited functional
F({a,b})=Re(2*pi*i integral_a^b f(z) dz)/Omega(E) on the full relative
module, in its original 72-generator order. L028 supplies the orientation
convention; its non-CM twist-calibration hypotheses are not applied to E.

## Conclusion

For this fixed curve,

    L(E,1)/Omega(E)=F({infinity,0})=1/6,
    F({0,infinity})=-1/6,
    ord_(s=1) L(E,s)=rank E(Q)=0.

This is an application of known results, not a new rank theorem. It ends
higher-order production on this model. It supplies no refined leading
coefficient formula, Sha conclusion, arbitrary-curve rank comparison or
BSD candidate. The separate critical audit below passes for this fixed
extraction/application; L056's existing analytic audit remains an input.

## Proof

The prior IMPORT assessment is
`drafts/literature/2026-10-14-conductor36-central-value-diagnostic.md`,
whose COVERED_TARGET is exactly the completed extraction and conditional
rank-zero application. No new literature search or reproof is needed.

**Path identification and exact value.** In
`scripts/conductor36-table/presentation.json`, the complete selected
`/endpoints/1` and `/basepaths/1` records give start [1,0]=infinity and
end [0,1]=0. The start chain is empty. The end chain has one segment,
matrix h=[0,1,-1,0], coset 1, unit 35 and Gamma_0(36) witness
[-1,0,0,-1]. Its raw vector is the second standard basis vector of Z^72;
its quotient coordinates are the first standard basis vector of Z^13.
Thus this is the actual original generator g_1={infinity,0}, not a
similarly named absolute cycle or a sampled cusp path.

L056's exact table gives m_1=4 with F(g_1)=m_1/24=1/6.
The complete selected `/generators/1` certificate agrees, with containing
normalized interval [l,u] where

    l=13204693752377389598923991524/2^96,
    u=13204693752377389598923991922/2^96.

Exact arithmetic checks 3<24l<=4<=24u<5. Rational existence and analytic
containment are supplied by audited L056, not inferred from this width.
The width is 199/39614081257132168796771975168 < 2^-38.
The complete selected distinct-audit record has integer candidates [4],
the same interval, and zero for all four quotient cross-product residuals.
Its first quotient numerator is 4 at scale 24, so the full quotient
coordinates also reconstruct 1/6. These are checks of the existing
audited functional; no Fourier terms or entire table are recomputed.
Path reversal negates the integral with the same positive Omega(E),
giving F({0,infinity})=-1/6 without a component or period factor.

**Known complex identity.** Import Balakrishnan–Muller–Stein,
*A p-adic analogue of the conjecture of Birch and Swinnerton-Dyer for
modular abelian varieties*, Math. Comp. 85 (2016), 983–1016,
DOI 10.1090/mcom/3029,
[Sections 2.1–2.2, pp.988–991, equation (2.4) and the identity following
the plus-symbol definition](https://wstein.org/papers/mcom3029.pdf#page=6).
For the normalized rational-coefficient weight-two form, the plus-symbol
identity is [0]^+_f=L(f,1)/Omega^+_f. Its numerator is
-pi*i times the sum of the two integrals from r and -r to infinity;
at r=0 it is -2*pi*i integral_0^infinity f(z)dz, namely the integral
from infinity to zero. L028's orientation passage identifies its real
value with F({infinity,0}). The source uses the total real period and
differential scale one, justified here by L052's optimal degree-one
identification and cube-free Manin theorem. CM is not excluded by this
identity. L050 identifies L(f,s) with L(E,s); at 2 and 3 its local factors
are trivial, so omitting bad-prime factors does not change this central
value or order. Therefore L(E,1)/Omega(E)=1/6.

**Known rank-zero implication.** Modularity supplies holomorphy near
s=1. Since Omega(E)>0 and 1/6 is nonzero, L(E,1)!=0 and its analytic
order is zero. Import the analytic-zero/one theorem in
[Wiles, *The Birch and Swinnerton-Dyer Conjecture*, official Clay
description, unnumbered theorem p.4](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=4),
as recorded in `foundations/02-standard-inputs.md`: for an elliptic curve
over Q with analytic order zero or one, rational rank equals that order.
E is over Q and meets the analytic-order-zero hypothesis. The theorem
has no non-CM, ordinary-prime or residual-surjectivity premise. It gives
rank E(Q)=0. No Sha or refined formula is imported from this statement.

**Finite evidence and limitations.** The extraction certificate is
`scripts/conductor36-table/central-value-extraction.json`; it binds the
three selected existing input files by SHA-256 and records exact interval,
scaled inequalities, quotient evaluation, reversal, value and nonzero
checks. All twelve checks pass with no failures. This is a bounded exact
extraction from L056, not a fresh replay of its 476280 finite terms.
ATTEMPTS/029's universal-source and repetition stops remain preserved.
The main arbitrary analytic-order-at-least-two gap is unchanged.

**Separate critical audit, 2026-10-14, BSD-209.** The prior IMPORT
assessment `drafts/literature/2026-10-14-conductor36-central-value-critical-audit.md`
covers this exact application. Its inspected primary statements are reused;
there is no new theorem hypothesis or source-access dependency.

The complete selected path, production row and distinct-audit row were
read, and independently checked by
`scripts/conductor36-table/audit_central_value.py`. The original extraction's
three input hashes agree with the actual files; the table's presentation
hash also agrees. Generator 1's lift is [0,-1,1,0]. Multiplication by
gamma=[-1,0,0,-1] gives its recorded h=[0,1,-1,0]; gamma has determinant
one and lower-left entry divisible by 36. Unit 35 sends the representative
[1,0] to the recorded residue [35,0]. The complete chain has endpoints
infinity and zero, raw vector e_1 in the original zero-based 72-generator
order and quotient vector (1,0,...,0) in dimension thirteen. Thus both
the path and its evaluation refer to the same full-relative element.

All eight signed occurrences were recomputed from the already certified
primitive intervals, including every partial sum, with exact rational
endpoints and separately with the saved outward rounding. Both complete
traces agree with the respective records. This checks selected interval
assembly, not the underlying Fourier terms or their analytic containment.
The independent positive total-period interval is exactly the one in
L056, with one real component. All four saved endpoint quotients agree
with exact division; the independently summed positive numerator divided
by the opposite period endpoints is contained in the saved normalized
interval. No sign, half-period or component rescaling is introduced.

For the displayed l,u, direct arithmetic gives

    24l = 4 - 149/2475880078570760549798248448,
    24u = 4 + 299/4951760157141521099596496896.

Hence ceil(24l)=floor(24u)=4, with strict adjacent-integer exclusion.
The narrower independently assembled interval also isolates 4. Existence
still uses L052's 24F-integrality and L056's analytic containment. All
thirteen quotient values agree at scale 24 with the distinct audit;
their dot product with the complete selected coordinate vector is 1/6,
agreeing with both reconstructed generator entries. Reversal gives -1/6
by linearity of the same integration functional and unchanged positive
period, not by taking an absolute value.

The source specialization also passes. L050 gives the globally minimal
Q-model, exact conductor and normalized rational newform. L052's pointed
degree-one identification makes E optimal, and its cited differential
theorem applies because 8 and 27 do not divide 36. Thus absolute Manin
scale one, and the choice of map sign giving scale +1, are justified
independently of the central value. In rational coefficient degree one,
the compatible plus period in BMS (2.4) is precisely the positive total
period used here. At r=0 its displayed plus-symbol definition has numerator
-2*pi*i integral_0^infinity f, equal to the infinity-to-zero numerator
of F. Real Fourier coefficients give a real central integral. CM is
allowed; none of L028's non-CM calibration premises is imported.
Both bad local factors are one since the reductions at 2 and 3 are
additive, so the official incomplete L-function has the same value here.
Holomorphy and the strictly nonzero value Omega(E)/6 establish analytic
order zero before invoking Wiles's p.4 theorem. That theorem applies to
elliptic curves over Q of analytic order zero or one, including this CM
curve, and yields rational rank zero. No Sha or leading-coefficient claim
is added.

Reproduce the bounded audit from this notebook with

    python3 scripts/conductor36-table/audit_central_value.py

The full certificate is `scripts/conductor36-table/central-value-critical-audit.json`:
43 exact checks, no failures, actual width
199/39614081257132168796771975168 < required 1/274877906944,
and all four original input files unchanged byte-for-byte. These checks
supplement the mathematical applicability audit; they do not prove the
imported theorems or repeat the full L056 analytic audit. The fixed
application passes and closes higher-order production on this model.
This is local validation of known mathematics, not progress beyond the
cited sources or a solution of the arbitrary-curve gap.

## Mathlib

Full matching coverage for the central-value identity, this normalized
fixed table and the analytic-rank-zero theorem was not checked. Exact
rational arithmetic support does not establish a matching arithmetic
theorem; no absence claim or formal verification is made.
