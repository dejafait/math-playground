# Approved source scope for the finite scalar conceptual audit

TARGET: Independently audit L696's centered-gap exponential bound for L666's finite c_0(1), including the prescribed center, Gaussian pairing, zero half-density and both finite endpoints.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 118 reuses the completed step-116 searches and comparisons in drafts/literature/2026-11-03-fourier-gap-positive-convolution-transfer.md; read L696 completely to delimit the audit, L666's exact product and finite indices, L694's prescription/limit identification and completed audit, and the L695 absolute-tail stop. No new general theorem search or originality inference.
SOURCE_EVIDENCE: Reuse Durrett version 5 (11 January 2019), Thms 3.3.1--3.3.2 p.126, Example 3.3.8 and Lemma 3.3.9 p.128, and Lev arXiv:2007.09930v3 Lemma 4.3/Section 4.10 through audited L694; directly rechecked Vershynin first-edition author version (20 May 2024), Definition 2.7.5 p.33 and Theorem 2.8.1 with proof pp.36--37, and Miller (15 January 2006), Thms 4.1--4.2 with proofs and Section 6 (6.1)--(6.2), pp.7--9.
COMPARISON: Known mixture/product rules, non-iid Bernstein and Schwartz Poisson supply the standard inputs. L696's prescribed-center specialization, actual mixture, non-Schwartz Gaussian limit and finite-tail estimate remain local proof obligations; no inspected matching theorem makes the independent audit redundant. L695's absolute angular/spatial cost does not decide this signed scalar bound.
GAP: The separate conceptual audit must verify L696 Sections 2--6, including all constants, the zero half-density, reflected Fourier multiplier, fixed-n regularization limit and both finite endpoints; no correctness judgment on those cases is made here.
REASON: This separate literature turn approves the saved audit scope using adequate existing coverage and exact primary statements. No essential source blocker remains; proceed to the conceptual audit, not another unchanged search. Gate completion supplies no new mathematical evidence.
LITERATURE_REASON: The invocation explicitly requires separate source approval of the newly written L696 audit scope; reuse the ready scalar assessment while checking its interface with the written proof.
SCOPE: The exact TARGET only, under the fixed-profile, center, gap, anchor, unit-mass, finite-index and progression hypotheses below. No angular interval, higher moment, complete logarithm, H/support, Xi or RH claim is covered.

## Review scope and inputs

Reuse `2026-11-03-fourier-gap-positive-convolution-transfer.md` for the
precise primary source statements and their reading limits. Do not
repeat unchanged searches merely for balance. Review the new canonical
`lemmas/L696-centered-fourier-gap-finite-scalar-decay.md` against that
coverage and L694's audited proof before setting any ready audit target.
The necessary mathematical inputs are L666 and L694; L693 is inherited
through L694. L690/L695 are qualified comparisons, not premises.

Retain fixed real e in l1(Z), sup |e|<=1/8, one fixed anchor, all unit
masses, n=12q+3, h=27/(10n), t_j=j/n including j=0, u=1 and denominator
angle 1/u. omega_* is L696's specified integral, not an adjustable
center after the profile has been selected. Its construction must
produce a fixed g>0 before n varies. The desired bound is C exp(-c*n)
with C,c and onset independent of n for that fixed profile and gap.

Critical obligations for the later audit are: verify the center remains
inside the original annulus and every Picard norm hypothesis survives;
verify all mixture weights and the Bernstein centering/scaling; justify
the Gaussian regularization with its zero half-density and reflected
Fourier signs; check L1 interval integration by parts and the polynomial
multiplier bound; replay the symmetric m -> -m-1 tails, shifted segment
clearance and constants in (21)--(26). No numerical evidence is used.

The separate conceptual audit should accept the scalar result only if
these checks retain a positive exponential rate after every error, or
record the exact error and repair/stop decision. It must not infer
angular, higher-moment, complete-logarithmic, H/support, Xi or RH
conclusions. No independent conceptual audit or full matching Mathlib
coverage is asserted by this source-scope approval.

## Separate scope approval — step 118, 3 November 2026

The invocation-start target was: “Review coverage and proof obligations
for an independent conceptual audit of L696's centered-gap exponential
bound for L666's finite c_0(1).” That review is now complete. The TARGET
above names the resulting audit exactly; it narrows the saved proposed
scope without adding a mathematical hypothesis or transfer conclusion.
The original pending status is historical, not an outstanding source gate.

Reused the primary-source search, versions and reading limits in the
[step-116 assessment](2026-11-03-fourier-gap-positive-convolution-transfer.md).
Durrett and Lev were not fetched again: their inspected statements and
L694's independent audit cover the unchanged imported rules. Directly
reopened [Vershynin's first-edition author PDF](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf),
Definition 2.7.5 (printed p.33) and Theorem 2.8.1 with its complete proof
(printed pp.36--37). Independence, mean zero and finite sub-exponential
norms are essential; identical distribution is unnecessary. The proof
uses the constrained MGF parameter and both tails. This is a probability
bound; L696 must separately justify its centered norms and the pairing.
No centering exercise is imported as a proved application.

Directly reopened [Miller's notes](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf),
Theorems 4.1--4.2 and their complete proofs (printed pp.7--8), and
Section 6, equations (6.1)--(6.2) (p.9). The stated Poisson formula
requires a Schwartz test. The duality definition has the same test
restriction and gives the comb identity, not a rational-test extension.
The later auditor must verify the Gaussian-regularized functions meet
that restriction and the entire limiting argument. The earlier note's
page range is thus retained; no broader source theorem is asserted.

### Exact obligations, rather than a proof audit

1. Section 2: compare the prescribed integral center with the old
   annulus; check all unchanged kernel constants and the new cutoff's
   support, Hermitian symmetry, coefficient-smallness and finite Wiener
   norm against L694. Existence of a fixed positive gap and the
   conditional assertion for every admissible fixed profile are separate
   claims and both require checking.
2. Section 3: compare every product factor with L666, especially j=0
   and the denominator angle; check positive mixture weights, uniform
   centered norms, mean approximation, onset and Bernstein scaling.
   Do not infer density-sample bounds directly from concentration.
3. Sections 4--5: check the density representation, its right limit at
   zero, positive comb samples and exponential majorant. At fixed n,
   verify the symmetric pairing, Schwartz regularization, Fourier
   normalization, approximate-identity limit at every comb sample and
   domination of the full sample series. In particular the zero sample
   must retain pi*p_n(0+). No n-uniform regularization limit is assumed.
4. Section 5: check the L1 signed intervals, their derivative sign,
   absolute displacement sum and Fubini integrability. Verify how the
   gap gives a continuous multiplier identity and how reality reflects
   it to H(v); check the moment-weighted error outside the gap and the
   anchor in the exact sum. A small probability alone is insufficient.
5. Section 6: verify the telescoping identity also supplies the real
   series bound used earlier, without circular dependence. Replay
   (21)--(26), both omitted endpoints, the m -> -m-1 pairing, all
   displaced segments, the entire infinite tail and absorption of
   polynomial factors into a positive exponential rate. Constants and
   onset may depend on E and g, never on n for a fixed profile.

These obligations identify what the cited theorems do not supply. No
new identity, estimate, lemma, script or audit verdict was derived in
this literature-only turn. The finite scalar source search remains a
bounded comparison, not a novelty certification. The inspected sources
do not supply angular/moment/logarithmic transfer or actual-Xi data.

Continue with one conceptual audit retaining C*exp(-c*n), c>0, after
all errors. If an essential case fails, identify the unsupported line
and preserve the original argument before a repair or route decision;
qualitative cancellation does not pass. The old absolute-tail stop and
parked step-105 screen remain in force for their specific mechanisms,
not as a ban on this signed scalar test. Full matching Mathlib coverage
remains unchecked and is not an essential source blocker.

Outcome STALLED: separate gate approval and source confirmation add
no mathematical advance or informative negative result. Coverage is
ready; the next action is the audit, with no further literature needed
unless its hypotheses or essential inputs change.
