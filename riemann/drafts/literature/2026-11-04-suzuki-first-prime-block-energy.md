# First arithmetic window: proposed signed block test

TARGET: Test whether L740's total energy on L=log(3) admits a lossless two-block estimate across equal prime-free subintervals, retaining the complete cross-block coupling and the log(2) delay.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 275 searched exact Suzuki/logarithmic quadratic-form, Weil positivity support log(3)/log(2), first-prime-window Schur and logarithmic interface terminology; primary Zhu and Li Hongmin positivity theorems cover larger windows. Scoped L740/Suzuki assessments and attempt records contain no completed causal-energy/form-domain identification. No originality claim.
SOURCE_EVIDENCE: Reuse L740, L018/L618 and step-270 sources; inspect Suzuki 2606.09096v3 Thm1.1, Sections2.3-2.5,3.1-3.2; Zhu 2608.24827v2 Thms1.1-1.2, Sections4-6, Cor6.3 and retraction/Section17; Li Hongmin rStation paper45 v1 Thm1.1, (2.1), Sections3-8; Perfekt-Pushnitski Ark.Mat.56(2018),163-183, Lemma2.1 p166 and its complete proof. Exact links and limitations below.
COMPARISON: Zhu Cor6.3 supplies full complex-test localized Weil positivity at half-width 0.8, already beyond log(3)/2; Li Hongmin states the stronger log(11)/2 result. Thus seeking a new sign theorem at this window duplicates known coverage. The remaining specialization is identification with L740's nonsymmetric generator energy and valid block/domain extension, not reproof of these certificates or generic Schur algebra.
GAP: Prove the finite-window causal-energy/Weil-form identity with every scalar, pole, digamma and delay coefficient, then justify block restrictions and passage from smooth tests to D(A_L) and the closed form domain. No equality of those distinct domains, trace condition at the interface or full-line critical-axis multiplier is imported.
REASON: Complete the missing source gate and change the route to a bounded known-result specialization. Exact-window sign coverage is now available; Carleman domination and Suzuki's smooth core provide concrete interface inputs. No local energy inequality is derived or approved as proved this turn.
SCOPE: Exactly the saved target, L=log(3), equal spatial halves, complex unweighted L2 and the complete L740 generator. A later attempt may establish the identification/domain specialization and apply the cited finite-window sign theorem; no new positivity certificate, larger-window iteration, all-window bound or RH implication is covered.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED: exact-window positivity and essential continuum/interface source coverage had not been inspected. This review supplies that coverage rather than repeating the ready causal-realization audit.

## Initial nomination and test (preserved)

The central gap is still unconditional actual-Xi mixed positivity.
Let ell=L/2. The intended test concerns the Hermitian form
H_L(f,g)=-(<A_L f,g>+<f,A_L g>)/2, with inner product linear
in its first argument, and E_L(f)=H_L(f,f).
Start with smooth inputs supported separately in (0,ell) and (ell,L).
Seek nonnegative diagonal energies and the bound

    |H_L(f_0,f_1)| <= kappa sqrt(E_L(f_0) E_L(f_1)), kappa <= 1,

uniformly for that class, with a justified extension to the full
generator/form domain. All scalars, the logarithmic term, q and the
arithmetic part must be retained. No diagonal positivity, existence of
a closed semibounded form, or validity of splitting the domain at the
interface is assumed. These are proposed obligations, not results.

At this chosen window the arithmetic sum in L740 contains n=2;
n=3 is an endpoint delay acting as zero. Each half is shorter than
log(2). This makes the first signed coupling test concrete without a
prime truncation. Estimates must include the continuous cross-block
kernel and its possible interface singularity as well as the discrete
delay. A finite matrix or a test on constant vectors does not certify
the continuum inequality.

A certified lossless estimate would give a seed for a later block
extension mechanism in the original norm. It would not justify
iteration to larger windows, where more delays enter, and would not
by itself yield Xi signs. Those remain independent gaps.

Continuation test for the source review: locate applicable primary
domain/block-form results and either a known exact-window sign theorem
or a concrete quantitative coupling estimate to attempt. Generic Schur
complement algebra without an independently estimable coupling is
insufficient. Do not approve a target consisting only of restating
positivity. For the eventual mathematical test, require kappa<=1 with
all costs paid; kappa>1 from a majorant abandons that majorant, not
positivity itself. A rigorously positive generator-energy witness
would refute the proposed local dissipation, not automatically RH.

## Comparison with retained stops

Three mechanisms were compared when selecting this nomination:

1. Direct parameter composition/square ordering: parked by the
   [composition scope limit](../../ATTEMPTS/2026-11-04-suzuki-parameter-descent-source-limit.md)
   and the [actual square-order witness](../../ATTEMPTS/2026-11-04-suzuki-small-window-square-order-stop.md).
   No new compressed identity or order input warrants repeating them.
2. All-window total dissipativity from generation alone: no signed
   estimate follows from L740's finite-L bounds. The repeated analytic
   approval/audit continuation is closed in the
   [realization-only limit](../../ATTEMPTS/2026-11-04-suzuki-realization-only-sign-gap.md).
3. The selected fixed-window block energy test: a different signed
   inequality with explicit arithmetic support. It neither assumes a
   nullvector nor imports the slope bound left unpaid by L523.

The [generic signed-pole resolvent stop](../../ATTEMPTS/2026-10-30-weil-generic-pole-resolvent-source-stop.md)
warns that a standard block reduction alone supplies no favorable
arithmetic comparison. This nomination needs the actual coupling bound,
not that stopped finite-rank reduction under a new name. The blocked
scalar-tail report in the screw assessment is not needed and is not
retried. No cross-notebook input is proposed.

The finite-window discriminator is not yet a justified creative global
mechanism. Its missing signed estimate and source coverage block that
nomination; resolve them before choosing proof purpose. Full Mathlib
coverage is not checked.

## Completed source review, step 275

The main gap remains actual-Xi all-degree mixed positivity. The exact
intermediate target is unchanged. Its sign component has known coverage
on a larger support; its identification and domain specialization remain
local work. This review derives no new identity, form-domain theorem or
inequality. In particular it does not infer a new signed result from L740.

### Precise positivity inputs and overlap

[Xuefeng Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2)
(arXiv stamp 2 September 2026; manuscript date 3 September), Theorem 1.2
and **Corollary 6.3**, states

    Q(f) >= 8.9*10^(-18) ||f||_2^2,
    supp(f) contained in [-0.8,0.8], f complex.

Read (2)--(3), Section 4's complete-complement estimate, Sections 5.2--5.4,
6.1--6.3 and 17. The even-only theorem requires the corollary for this
target. The odd pole is negative; its certificate is retained. The proof
controls quadrature, rounding, and both infinite-tail and coupling costs,
not just a principal matrix. Treat this as a cited computer-assisted
theorem, not a locally replayed certificate. Its supplementary files
were not inspected here. Apply only on the finite form domain (or read
the lower bound with energy +infinity); arbitrary L2 inputs need not
have finite logarithmic energy. The earlier support-2.38 certification
is explicitly retracted in Section 7/Remark 3.3 and is not an input.

[Li Hongmin, *Cutoff-free positivity of localized Weil forms through the
(log 11)/2 threshold*, rStation paper 45 v1](https://rstation.ai/problems/riemann_hypothesis/papers/45),
23 October 2026, Theorem 1.1, states strict positivity for both parity
sectors up to half-width log(11)/2. Read its (2.1), Sections 3--8:
positive boundary responses, full Parseval covariance, infinite weighted
tail and signed odd pole are kept. The finite-to-closed-form comparison
is explicit. Its historical large matrices were not regenerated during
submission preparation; neither those matrices nor the supplement were
replayed here. This stronger overlap is nonessential: Zhu's smaller
window already covers the proposed support after the pending translation
and energy identification. Do not present a local sign at L=log(3) as
progress beyond these sources.

The common geometric normalization to match is, with zero extension,
F(t)=integral f(x)exp(-itx)dx and C_f(u)=integral f(x+u)conj(f(x))dx,

    Q(f) = (1/(2pi)) integral [Re psi(1/4+it/2)-log pi]|F(t)|^2 dt
           +2 Re(F(i/2) conj(F(-i/2)))
           -2 sum_n Lambda(n)/sqrt(n) Re C_f(log n).

This is Li's (2.1), with Zhu's (2)--(3) and Section 6 supplying its parity
cases. Writing this source formula does not identify it with L740's
energy. That equality, including all constants and boundary terms, is
an explicit obligation for the next attempt. No full-line multiplier
for xi'/xi on Re(s)=1/2 is asserted.

### Domain and quantitative interface inputs

[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
23 September 2026, Theorem 1.1 and Sections 2.3--2.5, 3.1--3.2:
the localized Weil operator is the Friedrichs realization of the
screw-function form initially on H_0^1(-a,a). Read the cutoff proof
(3.2)--(3.4) through its conclusion: endpoint errors converge in the
logarithmic form norm. Smooth compact functions are a form core. This
is not a statement that the causal generator equals that self-adjoint
operator, nor that their operator and form domains coincide. The
boundary logarithm in (2.3) cannot be omitted. Theorem 1.4/Section 5.1
is only an existential small-window sign, not a numerical log(3) bound.

[Perfekt and Pushnitski, *On the spectrum of the multiplicative Hilbert
matrix*, Ark. Mat. 56 (2018), 163--183](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2018/0056/0001/ARKIV-2018-0056-0001-a010.pdf),
Lemma 2.1, p.166, states: for a locally integrable kernel on R_+ with
|h(t)|<=A/t, the Hankel operator H(h) on L2(R_+) has norm <=A*pi.
Read its complete domination proof using the Carleman operator of norm
pi. This is an available bound for an interface kernel of the indicated
shape; the change of variables, exact coefficient and finite-interval
compression must still be justified. It supplies no kappa<=1 on its own.
Reproof of the classical norm theorem is unnecessary.

Reuse L740's exact domain and bounded perturbation, and its inspected
Carvalho-Neto--Fehlberg p=2 source in the step-270/271 assessments.
Possible later proof obligations are a block-domain decomposition and
extension of the energy identity in the appropriate graph/form topology.
These are specializations to attempt, not source theorems silently
imported here. No pointwise trace at the midpoint is imposed. Carleman
boundedness addresses the interface singularity concretely, rather than
assuming independent spatial blocks or vanishing cross terms.

### Bounded search, failures and decision

Queries included `Suzuki "xi" "logarithmic" "quadratic form" finite
interval`, `Weil quadratic form positivity support log 3 log 2 Suzuki`,
`logarithmic Laplacian interval quadratic form domain characteristic
function decomposition`, `"The Range of a Finite-Scale Weil Positivity
Method"`, and `"Carleman operator" "norm" "pi" Yafaev`.
The Laptev--Weth logarithmic-Laplacian paper's introductory form
definition was inspected as background only; no dimension-dependent
spectral estimate from it is imported.

Tao Lin's first-prime split-residual work was located through a secondary
abstract, DOI 10.5281/zenodo.21856509. Primary Zenodo landing/API retrievals
failed. Its reported endpoint limitation remains an **uninspected lead**,
not an obstruction theorem or accepted input. Park it; no dependent work
requires another access retry. Likewise the old blocked scalar-tail
source was not retried. Search silence is not evidence of originality.

Reused the parameter-composition, square-order, realization-only and
generic-pole stops cited above. No stopped mechanism is reopened.
The fixed-window positivity question now overlaps stronger cited
results, so an independent certificate is unnecessary. SPECIALIZE covers
only the actual causal-energy and block-domain bridge needed to use that
known result; a subsequent result would be REPRODUCTION, not a creative
sign mechanism. No justified creative all-window target follows merely
from this finite-support import. The missing independent extension
estimate remains the blocker to such a nomination.

Continue if the next attempt matches the displayed geometric form to
the full L740 energy in the original norm and validates the split and
closure, thereby legitimately applying a cited sign theorem to obtain
the requested kappa<=1. Stop the attempted transfer if a coefficient,
domain or boundary mismatch remains unpaid. Any direct majorant >1
stops that majorant only. Success supplies a known finite-window seed;
larger windows, fixed-parameter all-window control and Xi mixed signs
remain unresolved. Mathlib coverage of this specialization was not
checked. Full proof and canonical lemma documentation belong to a later
mathematical turn, not this literature-only review.
