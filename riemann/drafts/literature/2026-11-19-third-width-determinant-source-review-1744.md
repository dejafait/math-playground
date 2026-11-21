# Third width determinant: source-review nomination1744

TARGET: Review source coverage for a uniform nonzero sign of the normalized third-order determinant built from k_sigma(1/8), k_sigma(3/16), and k_sigma(1/4) on [1,2], including coalescing widths.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact-kernel, divided-difference and extended-Chebyshev searches and scoped C032/C033 overlap/failure comparison in drafts/literature/2026-11-19-third-width-source-notes-1745.md; no matching three-test theorem found, without a novelty claim.
SOURCE_EVIDENCE: de Boor, Divided Differences (2005), Proposition35/Definition37, Proposition43, formulas(45)/(52), pp58-64 https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; Novaes--Torregrosa, UAB July2015, all-prefix criterion p2 and Section2 pp5-6 formulas(5)-(9)/Rolle proof https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf ; Sra fixed-v1 Proposition A.6(ii), pp15-16 and complete Cauchy--Binet proof https://hexagonmath.org/pdf/2611.00345v1 ; reuse first-zero/count/heat coverage1726 and source-notes1709/1731 with qualifications.
COMPARISON: Classical sources cover repeated-site divided differences and all-prefix Wronskian criteria, not this sign. Sra's all-order Hankel positivity fixes the smoothing kernel and orders Laplace variables; it is not width sign regularity. C033g gives only the two-test first-derivative margin.
GAP: The next mathematical attempt must prove C^2 width regularity, normalized signed core and full-divisor/E errors through second order, the applicable Newton/Hermite or Wronskian reduction, and a strict bound including every collision pattern. None is asserted by this review.
REASON: New third-order source scope has now been compared; no essential source blocker remains for one bounded EXPLORE attempt. Missing kernel estimates are the research target, not established assumptions. New ready continuation1745 receives separate next-turn approval.

The following preserves the nomination's target and limitations.
Source review1745 is complete; its evidence and precise applicability
obligations are in [source-notes1745](2026-11-19-third-width-source-notes-1745.md).
No determinant sign was derived. Full matching Mathlib coverage
remains unchecked and unknown. The exact mathematical continuation is
[assessment1745](2026-11-19-third-width-determinant-test-1745.md),
newly ready for separate next-turn approval by the supervisor.

## Exact proposed mathematical test

Use C032m/n and C033g's actual-divisor convention on W=[1,2]:

    k_sigma(y)=exp(-E_sigma(i*y))*sin(A_sigma(y)),
    A_sigma(y)=2*pi*integral_0^y p_sigma(x) dx,
    f(sigma)=k_sigma(1/8)>0,
    r_2(sigma)=k_sigma(3/16)/f(sigma),
    r_3(sigma)=k_sigma(1/4)/f(sigma).

For 1<=s_1<s_2<s_3<=2 define the prospective diagnostic

    Delta_3(s_1,s_2,s_3)
      =det[(1,r_2(s_i),r_3(s_i))_(i=1,2,3)]
          /[(s_2-s_1)*(s_3-s_1)*(s_3-s_2)].

The sought later result is a sign epsilon in {-1,1} and c>0 such
that epsilon*Delta_3>=c uniformly, with justified continuous confluent
values when widths coincide. No sign orientation, existence of that
extension or positive margin is asserted here. A fixed absolute error
for the unnormalized determinant cannot control the vanishing width
Vandermonde; a grid avoiding the diagonal cannot settle this target.

Essential local inputs for review are C032j/m/n and C033f/g; C033h/q
give the downstream question only. Retain actual divisor, conjugation,
multiplicities, Gaussian half-variance, corrected inclusive counting,
fixed-v1 heat inputs, V(3*10^12), and the externally certified first-zero
separation used in C033g. Do not assume RH, realness of the remaining
zeros, positivity of p_sigma, total positivity preserved by nonlinear
composition, a variation cap, or J_eta=0 as an established result.

The first-zero part and full-divisor remainder must be compared after
the required divided differences. C033g's first-order ratio estimate
alone is not second-order source coverage. Determine the minimum
additional derivative/error hypotheses from primary statements and
essential proof cases before reading broader source passages.

## Relevance, discriminator and limits

Main gap: L030-L032/C032a actual-Xi all-degree positivity; within the
width route C032q's full odd cancellation and output positivity remain
undecided. A strict third-order sign could support a later exclusion
of annihilators with two ordered sign changes, beyond C033h's one-cut
class. Any such Borel-measure application, especially cut atoms and
singular parts, needs its own assessed scope; it is not part of this
determinant nomination. Arbitrarily oscillating eta, moment/tail control
and unsmoothed Xi realization would still be open.

Continue to one mathematical test only if the necessary primary source
cases and a bounded signed divided-difference comparison are covered.
For that later test, a proved strict uniform margin is positive evidence;
a rigorous zero or change of sign of the normalized determinant refutes
the proposed strict-sign mechanism. Failure of a coarse enclosure to
choose a sign is merely inconclusive and cannot justify repeated grids.
Record a missing essential source as a blocker, and a missing local
estimate as an explicit mathematical obligation, without conflating them.

## Duplicate and stopping context

Audit1744 completes the residual-law range exclusion and closes its
approval sequence. C033g/h cover a pair and one sign cut, not this
third test. Review1730 previously mentioned higher minors but did not
test them or provide their sign estimates. The present nomination
specifies arguments, normalization, all coalescent cases and a strict
margin as the new discriminating test; it is not another two-point
audit. Stops1534/1536 and1711 retain their recurrence, direct-transform
and symmetric-modulus limitations. Park1725 still forbids a phase-only
completion inference.

The routing comparison also reused review1698: C028d/e already supply
the logarithmic-height identity and exterior estimate, with central
signed payment open; C028h/o/p's norm floors supply no replacement.
No new creative central mechanism is claimed. Source review must first
decide whether this narrower development warrants a mathematical turn.
