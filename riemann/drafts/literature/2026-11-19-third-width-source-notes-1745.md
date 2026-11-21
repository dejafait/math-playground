# Third-width determinant source review1745

Literature-only working record, 19 November 2026. Target: review1744's
normalized three-width determinant, including coalescing widths. No
determinant sign, new lemma or mathematical script is produced here.

## Saved scope before further source work

Main gap: L030-L032/C032a actual-Xi all-degree positivity. A strict
third-order width sign could support a later exclusion for two ordered
sign changes, but does not pay full cancellation, output positivity,
moments or Xi realization. Continue only to a bounded full-divisor
sign test with all coalescent cases; a rigorous zero or opposite signs
would refute strictness. An inconclusive enclosure must be retained
and parked, not replaced by repeated grids.

Reused source-notes1709/1731 and source-working1726, and inspected
C032j, C032m's statement and common-envelope argument, C032n's
statement and differentiated-integral argument, and C033g's statement,
relative-error/E sections and audit1730. C033g pays the ratio for
arguments 1/8 and 1/4, not the three-test determinant. Its explicit
relative bounds are for the profile and first width derivative.
C032n's stated width regularity is C^1, with arbitrary complex
derivatives; C^2 width regularity must not be silently attributed to
that statement. No result has yet been derived to fill this difference.

Targeted searches of November19 width assessments, first-zero1726
coverage and width/1730 stop records found no matching third-order
certificate. This is a local duplicate screen, not an archive-wide
novelty claim. The recurrence/direct-transform/absolute-envelope stops
and residual-range audit closure remain in force for their own routes.

The following completes that working record. No kernel-specific
mathematics was derived during this review.

## Primary statements and essential proof cases inspected

1. Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
   1 (2005), 46-69; author PDF dated21 December2004,
   [primary PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf).
   Read Proposition32 and its construction pp56-57, Proposition35 and
   Definition37 pp58-59, Proposition43 and its Rolle/interlacing proof
   pp60-61, determinant formula(45) p61, and Genocchi--Hermite(52)
   with its induction setup pp63-64. Hermite interpolation includes
   repeated sites and their required derivatives. For a C^k function,
   (52) represents its kth divided difference by the simplex integral
   of its kth derivative, including repeated sites. For k=2 the
   simplex has volume1/2. This supplies the classical tool for
   controlling second divided differences of a C^2 error, uniformly
   near collisions. Formula(45) uses polynomial columns followed by
   one general function; it is not directly the proposed determinant
   with two general ratio columns. Its Newton/Hermite reduction must
   be checked in the later application. No sign of either ratio or
   of their mixed determinant follows from this source alone.

2. Douglas D. Novaes and Joan Torregrosa, *On extended Chebyshev
   systems with positive accuracy*, UAB prepublication13, July2015,
   [primary PDF](https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf);
   later J. Math. Anal. Appl.448 (2017), 171-186,
   [DOI](https://doi.org/10.1016/j.jmaa.2016.10.076).
   Read the C^r, r>=n, closed-interval definitions and all-prefix
   Wronskian criterion p2; Section2 pp5-6, formulas(5)-(9), including
   the division-derivation/Rolle proof of the nonvanishing case.
   The criterion requires every initial Wronskian to be nonzero on
   the whole interval. It yields zero bounds counting multiplicity,
   including repeated sites. The last Wronskian alone is not the
   criterion used here. The division steps require the denominators
   to remain nonzero; a pointwise check at one width is insufficient.
   Theorem1.1's analytic/simple-Wronskian-zero extension was located,
   but its zero-containing cases are not needed or imported. No
   theorem here proves any Wronskian sign of the zeta width family
   or a quantitative lower bound for its normalized determinant.

3. Suvrit Sra, *Some positivity properties of Riemann Xi under
   smoothing*, fixed
   [2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1),
   first release11 November2026. Newly read Proposition A.6's full
   statement and proof pp15-16, especially (ii) and (A.12).
   For a fixed admissible K with P_K>0 on x>0 it proves STP_infinity
   of (u,v)->(-1)^j ell_K^(j)(u+v), j>=0. The proof uses a positive
   continuous Laplace weight, integrability at each positive parameter,
   and Cauchy--Binet with two exponential determinants of matching
   sign. The differential form is a positive Hankel moment matrix.
   An additional p_K>0 hypothesis permits H_K in place of ell_K.
   This is a stronger all-order statement in different variables:
   K stays fixed. No representation of (sigma,y)->exp(-E_sigma(i*y))
   sin(A_sigma(y)) by those positive-weight kernels is supplied.
   Its strictness therefore does not pay the requested width minor.
   Reuse source-working1726 for Theorem3.3 and AppendixC's relevant
   profile/displacement/counting proof cases, without reauditing them.

PDF screenshots returned no inspectable image content; shell downloads
failed DNS. The displayed primary textual statements and the complete
relevant proof passages above were inspectable. No image verification,
successful local PDF download or inaccessible historical proof is
claimed. No essential theorem source remains blocked for the bounded
test. Karlin--Studden is referenced by Novaes--Torregrosa; no fresh
book extraction is claimed or needed for their inspected nonvanishing
proof case.

## Reused source inputs and exact scope comparison

Retain source-working1726/assessment1726's first-zero separation from
the [FLINT API contract/example](https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html)
and [fixed-commit low-index implementation](https://github.com/flintlib/flint/blob/1d432c3bba36d1a29f6453ebfaa00e43f58c278f/src/acb_dirichlet/isolate_hardy_z_zero.c).
This is an external certified computational input, not a local replay;
its historical low-index and documentation qualifications persist.
Retain the corrected inclusive, multiplicity-counting
[Bellotti--Wong v2](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1/Section5, as already compared there. No new zero list,
uncertified truncation, older C032y count constant or RH is imported.
Retain fixed-v1 heat inputs, V(3*10^12), conjugation and half-variance.

C032m's entire compact-variable bounds and C032n's first-width
derivative estimates justify the existing pairwise work. C033g
Sections2-6 explicitly retain the full complex divisor, control the
noncompact spatial integral for E, and bound the profile and its first
width derivative relative to the retained first core. Audit1730
validates those statements at their stated order. They provide no
second-width relative error or three-test signed margin. No derivative
of an existing inequality is permitted.

The classical sources cover the analytical framework for a bounded
attempt, not the exact result. The minimum additional local work is:

- Justify C^2 width dependence of the relevant full profiles, removable
  quotients, primitives and normalized ratios on a neighborhood of
  [1,2], with joint continuity. The existing C^1 statement cannot be
  cited as this extension. Repeated Gaussian differentiation and new
  dominated envelopes must be written out, including the noncompact
  spatial integral. Reuse the known heat identity and the assessed
  [Haslinger Theorem2.39](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
  Section2.7 pp67-68, only with their actual integration hypotheses.
- Derive signed first-core information at the new order and bound
  the full remaining divisor and E correction through that order
  after normalization. Second divided differences of the error
  require derivative control at the same order; profile positivity,
  a first-order ratio margin and fixed absolute entry errors do not
  supply it. Keep the sine correction and tiny positive f in view.
- Verify the Newton/Hermite or all-prefix-Wronskian application to
  these two ratios, with column order, factors and multiplicity
  normalization explicit. In a future Wronskian test, ordering the
  functions as (1,r_3,r_2) would permit use of C033g for the already
  paid first-ratio derivative. This is a proposed applicability choice,
  not a newly proved Wronskian estimate or extension to r_2.
- Establish the extension and bound for every ordered triple and
  each collision pattern: the lower two equal, upper two equal,
  or all three equal, including widths1 and2. A nonzero unnormalized
  determinant at distinct nodes is weaker than the target. A strict
  confluent Wronskian sign could be used only after the full classical
  application and the quantitative or compactness argument are paid.

These are research obligations with available source tools, not
unread essential theorems or assumptions already established. A new
external analytic theorem, unassessed implementation or changed
divisor hypothesis would reopen review before dependent work.
There is no reason to reprove the cited general interpolation,
zero-counting, low-zero computation, heat identity or general ECT
theorems. Only their kernel-specific specialization is justified.

## Searches, failures and decision

New queries: `Carl de Boor Divided differences 2005 Hermite Genocchi
formula pdf`; `extended complete Chebyshev system Wronskians
nonvanishing theorem smooth functions pdf`; `"Riemann" "smoothing"
"width" "determinant" Gaussian`; `"Gaussian" "width" "Chebyshev"
"sinh"`; `"Riemann Xi" "smoothing" "Wronskian"`; and
`"normalized determinant" "divided differences" Chebyshev`.
The last group found the fixed-K Proposition A.6, which was checked
above rather than treated as a matching theorem from a search snippet.
No exact full-divisor third-width sign theorem was located in this
bounded screen. Failed queries do not establish novelty.

Reuse1709's inspected Gaussian composition and nonlinear-preserver
comparison: it requires a real ordered TN input kernel, which has not
been supplied for this width family. Reuse1731 only for the one-cut
application's scope; it supplies no two-cut Borel exclusion. Stops1534,
1536,1711 and park1725 do not refute this different normalized test,
but remain evidence against recurrence closure, direct transform,
absolute-envelope signing and phase-only completion. Closure1744
prevents replaying the residual-range audit as new progress.

Decision: EXPLORE for exactly one full-divisor three-test attempt,
with the new derivative/relative estimates above unpaid. A proved
uniform strict sign is positive evidence for this finite-order route;
a rigorous zero or sign change of the normalized determinant defeats
strictness. A failure to enclose a sign is inconclusive and parks the
attempt without a repeated grid. The subsequent two-sign-change Borel
application needs separate coverage. Arbitrarily oscillating measures,
full J_eta cancellation, output positivity, moments/tails and actual-Xi
realization stay open. Full matching Mathlib coverage is unchecked and
unknown, not claimed absent. This is literature exploration and local
source preparation, with no new mathematical result beyond the sources.
