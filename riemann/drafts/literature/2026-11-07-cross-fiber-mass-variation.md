# Crossing an odd-contact fiber — completed source comparison

TARGET: Assess source coverage for the leading mass variation of a compactly supported real radial perturbation crossing one simple off-diagonal odd G-zero fiber under L879's hypotheses.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded local duplicate/failure comparison and external searches for complex-modulus integral variations, regular-zero L1 second variations, second epi-derivatives and contour minima; exact queries and inspected versus unread leads are below. No inspected theorem settles the actual-G variation; this is not a novelty claim.
SOURCE_EVIDENCE: Wachsmuth-Wachsmuth, JNSAO3(2022),8733, https://jnsao.episciences.org/9596/pdf , Section3.2 Lemma3.3/Theorem3.4/Lemma3.5/Example3.6, pp10-14, including compact-support proof cases; NIST DLMF live pages inspected 2026-11-07, https://dlmf.nist.gov/19.2 equations19.2.5/19.2.8 and https://dlmf.nist.gov/19.12 equations19.12.2/19.12.3 with domain and convergence statements; reuse L879's unchanged off-zero source assessment only in that scope.
COMPARISON: The scalar theorem controls a real kink with uniform compactly supported perturbations, not a complex density. The DLMF convergent model expansion explicitly contains a complementary-modulus-squared logarithm, not the actual-F coefficient or remainder. The constrained nonlinear pullback application remains a bounded test; no general instability or minimizer theorem is imported.
GAP: Justify the full-J density variation at a simple isolated fiber, distinguish motion transverse to its phase line from a real sign crossing, and control the integrated remainder below the first nonzero signed term. No actual-G sign, admissible lowering direction or branch exclusion has been established.
REASON: Source comparison now covers the real crossing and a complex-modulus singular model sufficiently for one bounded EXPLORE application attempt. Its geometric coefficient and remainder are the uncovered application difference, not a result derived or approved in this literature turn; a newly ready continuation receives separate approval next turn.
LITERATURE_REASON: Changed mechanism and support: perturbations now cross Q=0, whereas L879's stationarity and the ready chord comparison do not cover the needed mass expansion.
SCOPE: L847 actual G,R,C,F and full angular density; L879 smooth real periodic u, J nowhere zero, off-zero stationarity and its audited phase line; conditionally one simple off-diagonal G-zero fiber, with a compact coordinate rectangle avoiding every other divisor and contact intersection. Exactly one local real radial bump crossing that fiber is tested; no minimizer, existence, global descent, other multiplicities, higher signs or Xi transfer is covered.
COVERED_TARGET: Determine the leading mass change with a sign-deciding remainder for a compactly supported real radial bump moving one simple off-diagonal G-zero fiber under L879's hypotheses, retaining the full Jacobian.

## Scope and decision after the source review

The original REVIEW_REQUIRED nomination is completed by this source-only
comparison. No new expansion, sign, lemma, mathematical script or source
theorem application was produced. The EXPLORE decision prepares exactly
the COVERED_TARGET for separate next-turn approval; it does not repeat
the stopped chord test or certify its proposed continuation.

The main gap remains L030-L032/C032a actual-Xi mixed positivity. The
proposed intermediate target is a sign-resolved local mass variation
at a simple off-diagonal odd fiber. A lowering direction could exclude
that contact from a mass minimizer under appropriate hypotheses; a
proved opposite sign could stop this proposed local instability
mechanism. Neither outcome is asserted. Stationarity alone is not
minimality, and existence/compactness of a minimizing stationary graph
must not be assumed or inferred from a local variation.

Retain L847's actual G and full oriented density, L879's smooth real
periodic u and J!=0, and, when selecting the simple fiber, L882's
matched conjugate branch and census. Work in a compact coordinate
rectangle centered on an off-diagonal point with exactly one simple
G-zero factor, away from simultaneous contacts and fiber intersections.
Such a local choice must be justified from the conditional branch;
no global deletion of the other contacts or multiplicities is allowed.
The proposed variation is real radial and supported in this rectangle,
with support meeting the fiber. Retain the variation of J as well as
G and the Vandermonde factor. Other branches, global existence, the
sharp L868 bound, higher signs and Xi transfer remain unresolved.

The main gap, possible use and unresolved assumptions in the nomination
above remain unchanged. L847's density/homotopy statement, L879's
hypotheses and complete relevant variation/contact proof, and L882's
conditional simple-fiber hypotheses and conclusion were inspected.
L882 is an optional source of the simple-fiber branch, not an assertion
that a stationary graph exists. Its finite census is unnecessary once
an individual clean rectangle is justified.

Exact reuse pointers from L879 are
`2026-11-06-stationary-graph-phase-components.md` in this directory;
Lawrence-Yamauchi, *Convex optimization and contour deformations*,
arXiv:2311.13002v2 (14 August 2024),
[Section II B, equations (11)-(16), pp3-4](https://arxiv.org/pdf/2311.13002v2#page=3);
and Guillemin-Sternberg, *Semi-classical analysis* (13 January 2010),
[Sections 13.13-13.14.1, equations (13.7)-(13.9), pp449-455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
These are reused pointers, not new crossing-case coverage. The unchanged
`2026-11-06-stationary-graph-phase-components.md` and
`2026-11-06-finite-graph-mass-descent-audit.md` were checked before reuse.
The fresh contour search located the same paper; no additional claim
from its local stationarity calculation is imported.

## Primary results actually inspected

Daniel Wachsmuth and Gerd Wachsmuth, *Second-order conditions for
non-uniformly convex integrands: quadratic growth in L1*, published
version, J. Nonsmooth Anal. Optim. **3** (2022), 8733,
DOI10.46298/jnsao-2022-8733,
[Section3.2, pp10-14](https://jnsao.episciences.org/9596/pdf#page=10).
For bounded open Omega, real w in C1(Omega) with grad(w) nonzero on
{w=0}, real z_k converging uniformly to z, all supported in one compact
K inside Omega, and t_k decreasing to zero, Lemma3.5 states, for
j(r)=max(r,0),

\[
 \frac{2}{t_k^2}\int_\Omega
 [j(w+t_kz_k)-j(w)-t_kj'(w;z_k)]
 \longrightarrow\int_{\{w=0\}}\frac{z^2}{|\nabla w|}\,dH^{d-1}.
\]

Read Lemma3.3's zero/nonzero trace cases, Theorem3.4's sliced regular-level
charts and domination, and Lemma3.5's fixed/uniformly varying direction
proofs. Example3.6 shows loss of the claimed limit without common compact
support. The theorem is scalar; it does not cover a transverse complex
perturbation or the second-order acceleration of Q(u+tv). Those are
application obligations. No extension to those cases was derived here.

NIST DLMF, Chapter19, current online equations as accessed 2026-11-07:
[19.2.5/19.2.8](https://dlmf.nist.gov/19.2#E5) define
E(k)=integral from 0 to pi/2 of sqrt(1-k^2 sin^2(theta));
[19.12.2/19.12.3](https://dlmf.nist.gov/19.12#E2) give its convergent
series near k=1. For real 0<k'<1, k'=sqrt(1-k^2), the displayed series is

\[
 E(k)=1+\frac12\sum_{m=0}^{\infty}
 \frac{(1/2)_m(3/2)_m}{(2)_m m!}(k')^{2m+2}
 \left[\log(1/k')+d(m)-\frac1{(2m+1)(2m+2)}\right],
 \quad d(m)=\psi(1+m)-\psi(1/2+m),\quad d(0)=2\log2.
\]

The definitions, real domain, logarithm convention, convergence statement
and complete E-series were inspected. This supplies a source model of
a modulus degeneracy with an explicit logarithmic term. It supplies no
variable-coefficient, compact-cutoff or full-J remainder theorem for our
density. No transfer or new expansion is proved here. DLMF cites Cayley
(1895), p54, and Cazenave (1969), pp165-169; their original passages were
not inspected. The official displayed identity is the retained input.

## Search, stronger-result comparison and recorded failures

Exact search strings included:

- `integral absolute value complex function simple zero second variation t squared log t contour optimization`
- `"Convex optimization and contour deformations" zeros local minimum sign problem`
- `"L1 norm" "second" "zeros" "differentiability" integral`
- `"contour" "zeros" "locally perfect" minimum`
- `second order epi derivative L1 norm integral zero set Christof Wachsmuth`
- `"second-order epi-derivatives" "integral functionals" Levy 1993`
- `"complex modulus" "second-order" "integral" zeros`
- `"L1 norm" "complex-valued" "second" derivative`

Additional searches used the same integral/modulus/perturbation/logarithm
terms. Most hits concerned unrelated contour estimates, matrix norms or
applications; none is used as evidence. NIST was opened directly after
the integral-norm comparison identified the need for a singular model.

Adam B. Levy, *Second-order epi-derivatives of integral functionals*,
Set-Valued Analysis **1** (1993), 379-392, is an unread lead, identified
by the second-epi-derivative search and an
[author-publication-list search hit](https://www.bowdoin.edu/profiles/faculty/alevy/index.html).
The publication-list page itself was not inspected.
No theorem, interchange hypothesis or pathwise remainder from it is
claimed. Epi-limit statements alone must not be relabeled as a Taylor
expansion on the prescribed contour path. Michael Taylor's
`https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/asympt.pdf`
was an inaccessible search lead; no theorem was inspected or imported.
Neither is essential to the bounded direct application test below;
this is not a persistent essential-source blocker.

Reuse the nomination's narrow local failure search. This turn additionally
checked the stationary-phase and finite-descent assessments and the
named chord assessment for crossing, logarithm and mass claims. The
coordinate-torus result keeps support away from Q=0; it does not duplicate
this target. The attempt65 product-moment and attempt69 corrected-chord
stops remain preserved; L886 supplies no sign input. The inspected
`ATTEMPTS/2026-11-06-green-fixed-mass-joint-positivity-stop.md` concerns
an abstract profile package, not this actual-density crossing test.
No stopped mechanism is reopened and no search failure certifies novelty.

## One bounded continuation and its discriminating test

After separate approval, use one smooth real radial test field supported
in a clean rectangle around a vertical simple fiber (exchange coordinates
for a horizontal fiber). A concrete permitted class to test is
v=(chi,0), chi real smooth with compact support and nonzero trace on an
open part of the fiber. The selection of this rectangle, its unchanged
external zero set and small-parameter preservation of J!=0 must be
justified. Moving a radial coordinate is not yet a proved transverse
motion of the phase-normalized density; that coefficient must be checked.

The sign test is the first nonzero term of B(u+tv)-B(u), including any
logarithmic term, with an integrated remainder of strictly smaller order.
Account for the full nonlinear density and its Jacobian, both sides of
the fiber, the cutoff transition and normalization. The scalar theorem
cannot justify discarding an imaginary component; a frozen singular
model cannot justify discarding the geometric acceleration. A direct
application calculation is needed precisely for those differences, not
to reprove either cited general result.

A strictly negative leading term would give a local lowering direction
and exclude this contact from a local minimizer, conditional on the
stated hypotheses. A strictly positive leading term would stop the tested
bump as a lowering mechanism; stopping the whole transverse-bump class
requires proving the sign throughout that class. A zero coefficient
leaves the higher-order sign unresolved and does not justify repeating an
unchanged test. No result here asserts any of these outcomes. Even an
exclusion from minimizers would leave stationary graphs, existence and
compactness of minimizers, L868's sharp bound, other contacts and the RH
gap unresolved. Mathlib matching and supporting coverage are unchecked;
no absence is asserted.
