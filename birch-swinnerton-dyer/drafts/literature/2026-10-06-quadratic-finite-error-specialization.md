# Conditional finite-error specialization: ready scope for separate approval

TARGET: Prove a conditional quadratic-coefficient enclosure from Stein--Wuthrich's P_n using exact Neron-normalized symbols with uniform denominator bound C, certified unit-root precision M and kappa(gamma)=1+p, testing N=min(n-1-C,M-C)>v_p(b).
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact searches and primary source inspection in drafts/literature/2026-10-06-primitive-quadratic-coefficient-error-bounds.md; this is its explicitly identified finite-precision specialization, with no claim of novelty or further search.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Propositions 3.1/3.5 and monic-divisor proof, pp. 1763--1765, Section 3.3 p. 1766, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=7 (rechecked 2026-10-06); Keith Conrad, Hensel's Lemma, Theorem 4.1 p. 6, https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6 (inspected 2026-10-06, undated live version); reused Sage 10.8 _prec_bounds comparison, https://raw.githubusercontent.com/sagemath/sage/10.8/src/sage/schemes/elliptic_curves/padic_lseries.py.
COMPARISON: Convergence and adjacent errors are imported; only conservative tail control, the degree-two binomial specialization and finite-root error bookkeeping remain to reproduce. Exact symbol normalization and a uniform denominator bound are granted finite-data certification inputs, not conclusions from L026's arithmetic hypotheses alone.
GAP: The proposed enclosure below has not been proved in this literature turn. No actual normalized symbol data, coefficient witness or uniform nonvanishing theorem is supplied; producing the certification inputs is outside this approval.
REASON: A short conditional proof makes the finite precision obligations explicit and avoids an unproved sharp tail constant or rounded period scale. Reproof is restricted to this elementary bookkeeping; the established modular-symbol convergence theorem is cited.
SCOPE: Non-CM E/Q, good ordinary p>=5; trivial branch, primitive untwisted series, real Neron period, kappa(gamma)=1+p; exact symbol values and a certified integer C>=0 bounding all relevant symbol denominators at every level; depth n>=2; certified root precision M>=1. Downstream L026 hypotheses remain separate.

## Inputs and exact proposed test

Use the reviewed construction and qualifications in
[the source assessment](2026-10-06-primitive-quadratic-coefficient-error-bounds.md),
foundations/05, L004's enclosure criterion, and L026's fixed primitive
coefficient hypothesis. This is a ready continuation recorded after a
literature step; the supervisor retains its separate approval/routing.

The exact symbol map must already equal the real-Neron-period normalized
plus map used by Stein--Wuthrich. A raw eigensymbol or an uncertified
rounded period ratio does not meet this input. Supply a proved C with
v_p([r]^+) >= -C for all symbol arguments at all levels in the
construction, not just sampled arguments at depths n,n+1. A checked
finite integral modular-symbol presentation can be supporting evidence,
but its normalization and denominator bound must themselves be certified.

Form P_n in the source's coordinate. Supply the exact integer
Teichmuller representatives modulo p^n (root equation and residue class
checked); do not use a low-precision lift to choose modular-symbol
arguments. Let u be an exact rational p-adic unit with u congruent to
the Frobenius trace modulo p and
v_p(u^2-trace_p(E)u+p) >= M. Use **the simple-root Hensel lemma**:
for an integral polynomial, an approximate root with unit derivative
and residual valuation at least M has a unique root in its residue
class and distance valuation at least M. Its exact hypotheses must be
checked here. The same named lemma certifies the Teichmuller residues.

Define the exact rational b as [T^2] of P_n with alpha replaced by u,
using those integer residues and the exact normalized symbol values.
The proposed bound, still unproved here, is

\[
v_p(a_2-b)\ \ge\ N=\min\{n-1-C,\ M-C\}.
\]

The next proof must justify the infinite tail from the **uniform** C,
the degree-two binomial valuation for p>=5, and replacement of inverse
unit-root powers in every finite summand. It must check that discarding
terms of degree greater than two does not affect b. No assumption that
the lower coefficients vanish is authorized. If N>v_p(b), L004 then
supplies the known nonvanishing implication. This paragraph specifies
the threshold to test; it does not establish it.

## Relevance, limits and route decision

Main gap: rational rank equals complex analytic order when the latter
is at least two. This conditional finite-error lemma could supply
L026's independent coefficient premise once certified data exist.
Continue if all stated errors yield the displayed enclosure. If the
proof needs an unstated period scale, only observed denominators,
uncontrolled root precision or a different series, stop that inference
and record the exact failed obligation. An enclosure containing zero
supplies no nonvanishing evidence and no exact-vanishing conclusion.

Retain L026's non-anomalous prime, residual surjectivity, prime-to-p
Manin/Tamagawa factors, E(Q_p)[p]=0, residual-family nonvanishing,
central vanishing and sign +1 for downstream corank use. This step does
not prove uniform coefficient production, rational Kummer membership,
finite Sha or complex-order equality. It removes neither the finite
quotient F nor possible divisible Sha. It reopens no inference stopped
in ATTEMPTS/021. Mathlib coverage: not checked; no absence claim.

## Source-link recovery review, 2026-10-06

The direct publisher offprint above was accessed and the statements of
Propositions 3.1/3.5, Corollary 3.3 and the essential monic-divisor proof
were rechecked. Section 3.3 fixes the ordinary unit root. The existing
source assessment remains the normalization and implementation comparison;
no new search or novelty claim replaces it. The warned two-depth tail
constant and Lemma 3.6 wording remain outside the accepted inputs.

[Conrad, Theorem 4.1, p. 6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6)
states: for f in Z_p[X] and a in Z_p with
|f(a)|_p < |f'(a)|_p^2, there is a unique root alpha satisfying
|alpha-a|_p < |f'(a)|_p, and
|alpha-a|_p = |f(a)/f'(a)|_p. This is the precise
root-distance input; the proof attempt must verify the unit derivative
and residual precision for both polynomials, rather than citing existence
alone. This review imports no new coefficient enclosure.

The process repair adds accessible direct URLs and a numbered precision
reference. SPECIALIZE and the exact TARGET remain unchanged. No new lemma,
mathematical script, actual coefficient or rank consequence is supplied.
The next bounded proof retains the previously stated continuation/stop
test and all independent gaps. Mathlib coverage remains not checked.
