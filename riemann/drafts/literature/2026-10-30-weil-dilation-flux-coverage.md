# Signed dilation identity and near-null flux — completed source comparison

TARGET: Assess source coverage for a dilation/Pohozaev identity for the complete localized Weil form targeting |tau_L(u)|^2+|tau_R(u)|^2<=C lambda, locally uniformly for normalized simple eigenvectors as lambda decreases to zero.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Queried logarithmic Laplacian Pohozaev identity boundary trace eigenfunctions; logarithmic Laplacian Pohozaev signed convolution potential dilation; exact Pohozaev/Pohožaev variants; withdrawn/corrected variants; and general Fourier-multiplier Pohozaev identities. Narrow Weil literature/ATTEMPTS searches found no duplicate signed dilation test. Searches led to the withdrawn arXiv:2411.15985, its authors' later arXiv:2504.18907, Ros-Oton–Serra arXiv:1207.5986, and Grubb JDE 2016; no adequate signed-atomic logarithmic identity was established by this bounded search, and no novelty follows.
SOURCE_EVIDENCE: Inspected arXiv:2411.15985 withdrawal notice/v2 history, v1 Theorem 2.3 and entire relevant Section 3.2 proof (3.8)–(3.11) and approximation; arXiv:2504.18907v3 contents/main-results opening and Section 6; Ros-Oton–Serra Theorem 1.1, Proposition 1.6 with all (a)–(c), dilation reduction (1.9)–(1.10), and Proposition 1.10; Grubb JDE 261 (2016), 1835–1879, Theorem 4.7 (4.23)–(4.27), pp. 1871–1872, plus its positive-order restriction. Paper 67 v1 (2.1)–(2.8), (3.4)–(3.5), Section 9 and reference [9] were checked; prior support/trace assessments are reused. Direct URLs and scope are below.
COMPARISON: The directly relevant logarithmic Pohozaev manuscript was withdrawn for a crucial proof error. The valid positive-order identities require different boundary data and do not supply the signed atomic logarithmic specialization. Paper 67 already supplies a support derivative, including activations, but expressly lacks the relative arithmetic flux estimate. A direct finite-dilation weak-form test is an uncovered mathematical gap, not a cited theorem or a reproof of its known support law.
GAP: Justify a one-sided weak dilation limit at logarithmic boundary regularity, retain the signed pole and every prime-power correlation, and identify a signed remainder criterion capable of flux<=C lambda locally uniformly. No such limit, remainder or sign has been proved. Full-Weil identification, collar proofs, branch uniformity, multiple-eigenvalue continuation and Xi transfer remain separate obligations.
REASON: Close the source review with informative NEGATIVE evidence against importing the withdrawn identity. Park that import and the unproved fractional-order boundary-limit shortcut. A direct finite-dilation comparison remains independently testable without either source; its precise proposed scope is in the separate continuation assessment and requires next-turn approval before mathematics.
LITERATURE_REASON: The target changes from fixed-operator domain and smoothing assembly to dilation variation of the complete Weil form, including endpoint flux and signed prime-power contributions; that technique and its hypotheses are outside the saved assembly coverage.
SCOPE: Complete form (2.1) recorded in L512, including the signed pole term and every active prime power, on a one-sided compact range of support radii approaching a hypothetical finite first zero; normalized simple eigenvectors with lambda>0 tending to zero. The desired C is independent of lambda on that range. Neither existence of such a branch nor an off-line zeta zero is asserted.

## Primary statements and the failed import

[Arora–Giacomoni–Vaishnavi, arXiv:2411.15985](https://arxiv.org/abs/2411.15985),
v2, 26 April 2025, is withdrawn: the authors report a crucial error
in the Pohozaev proof. The inspected [v1, Theorem 2.3 and Section 3.2](https://arxiv.org/html/2411.15985v1)
claims the following for a bounded C^{1,1} domain, real
u in H(Omega) intersect L-infinity with zero exterior data, bounded
pointwise L_Delta u, and weak equation L_Delta u=f(x,u).
It requires f(.,t) Lipschitz on the closure a.e. t, f(x,.) locally
continuous a.e. x, existence of the boundary limit
b=lim u(y)^2 log(delta(y)^(-2)), and finite weighted boundary integral.
With F(x,t)=integral_0^t f(x,s) ds, its claimed identity is

    integral_boundary b(x)(x.nu) d sigma
      = N integral_Omega (2F(x,u)-u f(x,u)) dx
        +2 integral_Omega x.F_x(x,u) dx +2 integral_Omega u^2 dx.

This is recorded as a withdrawn claim, not imported. The proof exchanges
the s->0 and boundary limits after (3.10), then passes by compactly
supported approximation in (3.11). Neither passage supplies usable
trace convergence here. No corrected proof or atomic-convolution
extension was inspected.

The same authors' [arXiv:2504.18907v3](https://arxiv.org/html/2504.18907v3),
17 September 2025, was checked at its contents, main-results opening
and Section 6. The latter still lists the critical/supercritical
existence question as open; its Pohozaev comparison concerns the
ordinary/fractional Laplacian, not a corrected logarithmic identity.
This is a scope check, not an audit of its existence results.

## Valid adjacent identities and their scope

[Ros-Oton–Serra, *The Pohozaev identity for the fractional Laplacian*,
Arch. Ration. Mech. Anal. 213 (2014), 587–628](https://arxiv.org/html/1207.5986),
Theorem 1.1, treats 0<s<1, bounded C^{1,1} Omega, bounded solutions
of (-Delta)^s u=f(u), zero exterior data, and locally Lipschitz f.
Proposition 1.6 requires u in H^s, global C^s regularity, all weighted
interior C^beta estimates for s<=beta<1+2s, a C^alpha extension of
u/delta^s with its weighted estimates for alpha<=beta<=s+alpha,
and bounded pointwise (-Delta)^s u. It gives the exact boundary term
Gamma(1+s)^2 integral (u/delta^s)^2 (x.nu).
The dilation reduction (1.9)–(1.10) explicitly retains the boundary
singularity of (-Delta)^(s/2)u; Proposition 1.10 supplies that behavior.
No uniform s->0 boundary-limit theorem is supplied by these statements.
The L513 logarithmic traces and L515 bounded forcing do not verify
these positive-order hypotheses. No specialization is asserted.

[Grubb, *Integration by parts and Pohozaev identities for
space-dependent fractional-order operators*, JDE 261 (2016),
1835–1879](https://web.math.ku.dk/~grubb/JDE16.pdf), Theorem 4.7,
pp. 1871–1872, requires a classical elliptic even-symbol operator of
order 2a with 0<a<1 and the transmission-space regularity of
Theorem 4.5/Corollary 4.6. Its commutator calculation (4.23)–(4.27)
was inspected. This positive-order theorem is not a logarithmic-order
or translated-atom boundary identity. No application is claimed;
the lower-regularity alternatives are not being used here.

## Reused arithmetic coverage and decision

[bramble_trace paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67),
27 October 2026, Theorems 2.1–2.2 supply a fixed-cluster support law
and lambda'(a)=-|tau_-(u)|^2-|tau_+(u)|^2 for normalized simple
branches, including prime activations. Its form (2.1), common signed
measure (3.4)–(3.5), and Section 9 (9.5) retain the missing relative
arithmetic bound. Reference [9] excludes the withdrawn proof. These
are source claims; the unaudited realization/collar qualifications
remain. L512 and L513–L515 do not settle them.

The scalar-shift contrast from the earlier support assessment still
excludes obtaining the vanishing factor from regularity alone. The
new source evidence excludes an attractive import, not the desired
arithmetic bound. A direct one-sided finite-dilation test would use
weak pairings and the complete signed correlations, avoiding the
withdrawn fractional-order limit. Its purpose is an explicit arithmetic
remainder criterion, not another absolute smoothing estimate or a
reproduction of the support derivative. No formula is derived here.
Mathlib matching coverage remains unchecked; no cross-notebook input.

The independently testable continuation and its decisive failure cases
are recorded in [the finite-dilation assessment](2026-10-30-weil-finite-dilation-remainder-test.md).
That newly written nomination awaits a separate source approval turn.

## Initial nomination (historical; source gate superseded above)

## Proposed intermediate target and downstream use

The main gap is actual-Xi all-degree positivity. A locally uniform
eigenvalue-relative flux bound could address the specific missing
estimate in paper 67 Section 9, which prevents automatic support
continuation near a first zero. The proposed new mechanism is to keep
signed arithmetic terms in a dilation identity rather than replace
the measure by its total variation as in the completed smoothing proof.
This is a question to assess, not a claim that the identity exists or
has a favorable sign. The later support-continuation implication,
multiple eigenvalues, global realization and Xi transfer would still
need their own proofs even if this intermediate target succeeded.

Use L512 for the precise complete form and the qualifications of its
activation comparison, and L513–L515 for the established fixed-model
trace/domain input. The explicit-form Fourier multiplier is
Re psi(1/4+i xi/2)-log(pi); its pole term and full prime-power sum
must remain as recorded there. The model identification with that
form is retained, not silently discharged by L515. No cross-notebook
input is proposed. Mathlib coverage has not been checked.

## Source-only continuation and bounded future test

First locate primary logarithmic-Laplacian Pohozaev or support-dilation
identities and inspect their exact theorem hypotheses and load-bearing
boundary cases. Compare the Fourier normalization, zero-exterior
smooth-core form, and the trace normalization in L513. If a result
requires classical derivatives or H1 data, it cannot be applied to
these logarithmic-energy eigenvectors without an additional justified
argument. Retain signed atoms; do not replace their variation by a
smooth-density derivative or assume differentiability at an activation
radius. Check duplicates and the scalar-shift contrast before approving
any changed mathematical target. Previously read source passages may
be reused, but they do not cover this identity.

For a later, separately approved proof attempt, the discriminating
test is whether a justified identity retains an arithmetic remainder
whose sign or cancellation can actually supply the factor lambda,
uniformly near a hypothetical simple first zero. Merely recovering an
absolute trace bound, introducing unproved H1 regularity, or dropping
the pole or prime contributions fails this test and parks that version.
A usable signed remainder would justify a narrowly formulated creative
attempt; presently no formula or sign is established. Source review
must determine the concrete formula and covered proof scope first.

The automatic-support and rank-trace stops remain at their recorded
scopes. This nomination does not restart either stopped implementation
or reset exploration usage. It prepares discovery rather than another
routine audit, with the essential source gate still closed.
