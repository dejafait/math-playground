# Far-end Jensen: whole-circle heat-reference test1368

TARGET: Establish or refute uniform gamma-normalized o(1) agreement between (-1)^d*A_d(-q) and the proposed vanishing-time heat reference 8*H_{Y^2/(2*d)}(2*Y) on d<=q<=2*d, with the positive scale and exact definitions in assessment1368, by controlling the complete circle |u|=1/q without dividing by F or zeta.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Source comparison1368 completed exact unshifted/full-circle/negative-axis/Gaussian/heat-flow queries, checked the primary works and named local failures recorded in assessment1367, and found no matching uniform comparison. No novelty inference; this is a bounded proposed application of standard analytic tools.
SOURCE_EVIDENCE: https://arxiv.org/html/2610.38870v1 ; https://arxiv.org/html/1904.12438v2 ; https://dlmf.nist.gov/5.11 ; https://dlmf.nist.gov/5.2 ; Ono2610.38870v1 (2.8)-(2.10), Lemma12/(4.1)-(4.3), (4.8) and its whole-sector polynomial-bound proof; Polymath1904.12438v2 (1)/(4), Section4/(35) with Gaussian/Fubini derivation, Theorem1.5 and Proposition9.1(i) for the non-import warning; DLMF5.11.1/5.11.3 and 5.2(i). L018/L021 and C019c/C019i supply local conventions only. Primary read ranges and qualifications are in assessment1367/comparison1368.
COMPARISON: Exact Cauchy and heat integral formulas and unconditional gamma/zeta upper bounds are available; no inspected source identifies their coupled moving-scale specialization. This is a full-entire reference, not a nonzero separated saddle or a frozen critical-line value. The printed heat real-zero theorem supplies no signs on this proposed small-time regime.
GAP: Verify the proposed parity, factor8, time, positive prefactor and uniform absolute gamma-normalized error, including all complementary-circle and heat-integral tails; a wrong factor or nonvanishing error is an informative failure. Reference sign margins, c*sqrt(d) distinct roots, bulk separation and RH remain independent and unproved.
REASON: Coverage is sufficient for one bounded analytic comparison using standard cited integral formulas and bounds. Its uniform estimates are mathematical work; no result is derived in this literature turn. Source-URL recovery1369 directly checked the cited primary ranges and completes the separate literature approval; the mathematical target is unchanged.
SCOPE: K=Q, integer d tending to infinity, exact T from C019c, B=T^2, P_d=d!/d^d, q in the closed band [d,2d], actual entire F and A_d. No zeta nonvanishing, RH, root simplicity, effective onset, heat real-zero theorem or extended saddle formula is assumed.
LITERATURE_REASON: Supervisor recovery1369 requires direct source URLs in this ready assessment; inspect the cited primary ranges and repair access evidence only, retaining review1368 and the exact mathematical target.

## Exact proposed comparison

Use L018/L021's actual normalization and C019i's definitions of F,
J_d, R_d and A_d; they are unchanged. In particular

    F(z)=xi(1/2+sqrt(z)),
    d=T/(2*pi)*(log(T/(2*pi))-1), T>2*pi*e,
    P_d=d!/d^d, Y=Y_d(q)=T/sqrt(q), t=t_d(q)=Y^2/(2*d).

Define a gamma-only scale (s=1/2+iY) by

    m(Y)=|s*(s-1)*pi^(-s/2)*Gamma(s/2)/2|,
    N_d(q)=P_d*q^d*exp(d)*m(Y)/sqrt(2*pi*d).

Here pi^(-s/2) uses the real log(pi). The standard gamma
nonvanishing theorem ensures m(Y)>0 for Y>0, since Re(s/2)=1/4,
s and s-1 are nonzero. N_d(q)>0. This is a choice of normalization,
not a lower bound on xi or zeta.

Use precisely Polymath v2's H_t from (4), with H_0(z)=xi(1/2+iz/2)/8.
The proposed reference and observable are definitions:

    G_d(q)=8*H_{t_d(q)}(2*Y_d(q))/m(Y_d(q)),
    E_d(q)=(-1)^d*A_d(-q)/N_d(q)-G_d(q).

The one mathematical target is

    sup_{d<=q<=2*d} |E_d(q)| -> 0 as d -> infinity.

No equality or asymptotic connecting the two integral formulas has
been proved in this review. The time Y^2/(2*d), factor8, parity and
prefactor are part of the ansatz to test, not a derived result. If the
ansatz is wrong, preserve it and identify the discrepancy rather than
silently replacing it by a different theorem.

## Permitted bounded attempt and stopping test

Start with cited Ono (2.9) on the entire circle |u|=1/q, traversed
counterclockwise. Keep both sides of the negative-real junction in
one angular parameter and retain F itself. Compare with the cited
Gaussian integral Polymath (35), including its tails. Check angular
orientation, integer powers and the complete prefactor before any
estimate. No general Cauchy, Gaussian or Stirling theorem needs reproof.
An angular localization, Taylor estimates with explicit remainders,
functional-equation reflection and cited absolute zeta/gamma bounds
are permissible tools; no nonzero local amplitude may be substituted.

All growth controls needed for this one test have inspected sources:
Ono Lemma12's sectorial factorization and (4.8) absolute polynomial
bound, standard complex Stirling in DLMF5.11, and the functional
equation/entire symmetry in L018. They must be specialized with their
actual domains, including both branches and any tail leaving a fixed
vertical strip. Lemma13's ratios and its Euler logarithm are unavailable
here. The circle and the heat integral have different tails; both need
payment relative to the displayed gamma-only scale. An absolute error
before division by m(Y) is not the desired estimate.

Continue if a complete error decomposition gives a uniform majorant
epsilon_d tending to zero on the closed band. An eventual bound
epsilon_d<1/20 is a useful weaker milestone but does not prove the
limit. A rigorous discrepancy disproves this ansatz only. An unpaid
tail or failed majorant is inconclusive; save it, name the exact missing
bound and do not claim the target false. Stop after this one test;
any changed reference, scale or band requires separate source coverage.

## Relevance, downstream signs and limits

Main gap: L030-L032/C032a actual-Xi all-degree positivity; the Jensen
route permits an unbounded deficit. This comparison would give a
reference through possible critical-line zeros, avoiding the particular
nonvanishing-amplitude obstruction in the printed bulk argument.
It supplies no root count by itself.

For the original c*sqrt(d) objective a later, independently assessed
argument must produce ordered samples strictly inside (d,2d), at least
c*sqrt(d)+1 of them, alternating reference signs of magnitude >=m_d>0,
and comparison error <m_d/2. Distinct intervening open intervals and
exact bulk separation then still need checking. No such signs, count,
effective onset or simplicity are assumed. The heat reference can
vanish and is not asserted hyperbolic. Polymath Theorem1.5's
x>=exp(C/t) regime must be checked before any future import; t>0 alone
does not pay that hypothesis. No heat real-zero theorem is used here.

The analytic comparison is development of standard integral methods,
not certified originality or a claim of a creative sign mechanism.
Independent signed margins are the blocker to a justified creative
root-count attempt. Essential inputs are L018/L021 and the exact
C019c/C019i conventions, plus the named external formulas; C019h/i's
near-edge estimates are not inputs on this band. No cross-notebook
input or mathematical script is required. Full matching Mathlib
coverage is unchecked; gamma/Gaussian support is not a matching theorem.

## Direct-source approval1369 — 17 November 2026

This is a source-access repair, not a new search or mathematical result.
Reuse comparison1368 and its recorded duplicate/failure checks; no new
match, obstruction or novelty claim is inferred.

- [Ken Ono, v1, 28 October 2026](https://arxiv.org/html/2610.38870v1#S2):
  (2.9) allows every positively oriented circle. Section4,
  Lemma12/(4.2)-(4.3) uses principal powers and large w in
  |arg w|<=pi/2. Its proof uses a larger sector and Cauchy estimates.
  Read (4.8) and its full proof: Re(s)>=1/2, |s|>=2; strip
  Phragmen–Lindelof handles the pole via (s-1), then the Euler
  product handles larger real parts. This absolute bound is distinct
  from Lemma13's restricted saddle ratios. No far-end estimate is imported.
- [D.H.J. Polymath, v2, 4 August 2019, Section4/(35)](https://arxiv.org/html/1904.12438v2#S4):
  read the Gaussian identity, cosine averaging and Fubini derivation.
  The representation holds for t>0 and every complex z, with xi/8
  and Gaussian weight exp(-v^2)/sqrt(pi). Read Theorem1.5(i)-(iv):
  regular real-zero assertions retain the exp(C/t) threshold;
  its all-real-parts counting statement supplies no reference signs.
- [DLMF5.11.1](https://dlmf.nist.gov/5.11.E1) and
  [5.11.3](https://dlmf.nist.gov/5.11.E3): inspected the common
  |ph z|<=pi-delta sector condition, delta fixed positive, and
  logarithm convention. These do not grant uniformity near the
  excluded negative-real direction.
- [DLMF5.2(i)](https://dlmf.nist.gov/5.2#i): inspected gamma's
  absence of zeros and poles at nonpositive integers. This is
  the cited gamma input only, not a bound for xi or zeta.

All four primary pages were directly accessible on the check date.
The saved scope and EXPLORE decision remain sufficient for one bounded
attempt; branch/reflection applicability, normalization and both tails
are obligations of that attempt. No lemma proof or mathematical script
was edited. Full matching Mathlib coverage remains unchecked.
