# Uniform finite-taper specialization nomination1443

TARGET: Derive |M(t)| >= c sqrt(L)/(log L)^(5/2), uniformly on |t| <= 1/5, for the original linearly tapered zeta^(-1/2) mollifier from the cited Selberg--Delange expansion.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1443 searched negative/complex-exponent Selberg--Delange expansions and tapered fractional mollifiers, and checked scoped November17/18 Jensen records and stops1407/1408/1431/1437. No directly matching tapered uniform theorem was inspected; no novelty inference. Full comparison: drafts/literature/2026-11-18-jensen-low-height-mollifier-nomination-1442.md.
SOURCE_EVIDENCE: https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf de la Breteche--Tenenbaum, Remarks on the Selberg--Delange method, Acta Arith.200.4(2021),349-369, author-corrected PDF: Section1/(1.9)-(1.13), internal pp2-3; Section3.3/(3.8), p7; relevant signed expansion/error proof cases Section4.4/(4.5)-(4.9), pp10-12. https://dlmf.nist.gov/5.4.E6 and https://dlmf.nist.gov/5.5.E1 supply standard half-integer Gamma data. Review1443 inspected these statements and cases.
COMPARISON: The source supplies the untwisted summatory expansion of tau_rho for fixed complex rho, arbitrary fixed order and a nonzero leading coefficient at rho=-1/2. The original alpha is this coefficient sequence with the Euler-product normalization. Abel summation with the finite linear taper and bounded-t uniform error is the identified specialization; no tapered asymptotic or lower bound is proved in the source review.
GAP: Establish the exact displayed lower bound with an absolute c>0 and one sufficiently large integer-L onset, retaining all coefficients, the n=L endpoint, the small-n terms and a relative error uniformly tending to zero. Do not apply the untwisted prime-mean condition to twisted coefficients without proof.
REASON: This is an independently testable necessary-condition component exposed by C020i. Source coverage is now available; a quantitative finite-weight specialization is needed before drawing an energy conclusion. It is ordinary reproduction/specialization, not a new central mechanism.
SCOPE: alpha(n) is the Euler-product coefficient of zeta(s)^(-1/2) on Re(s)>1; M(t)=sum_(n<=L) alpha(n) log(L/n)/log L n^(-1/2-it), L>=2 integer, real |t|<=1/5. In the witness L=floor(X^(1/1000)) and h=3pi/log X. No changed taper, reciprocal-series continuation, RH, random-phase law or actual-P approximation is permitted.

The complete primary theorem hypotheses, coefficients, branch comparison,
inspected proof cases and source limitations are recorded in
[review1443](2026-11-18-jensen-low-height-mollifier-nomination-1442.md).
Use the already stated expansion(3.8), citing its attribution to
Tenenbaum2015 TheoremII.5.2, rather than reprove Selberg--Delange.
The primary Theorem1.2 is an alternative only after checking all its
arithmetic hypotheses; no short-interval prime result is needed for
the direct tau_rho expansion. The book's full proof remains unread,
and no claim to have audited it is made.

One bounded mathematical attempt should apply the untwisted expansion
to the original weighted finite sum, identify its t-dependent main
term and obtain a uniform relative error. Keep enough expansion terms
for the needed error and control the small-n range separately. The
test succeeds only with a main term bounded away from zero after the
required scaling and a strictly smaller uniform error. If that test
fails, preserve the exact obstruction; an untapered leading term alone
does not establish the target. No new lemma is needed if no quantitative
result is obtained.

Plausible downstream use: the same compact t-range can accommodate
t and t+h on C020i's low-height interval once h is small. A later
H_L/q^6 comparison could test the sufficient full Gallagher energy
scale. That application is not part of this one-bound nomination,
and no stop is already asserted. C020i remains unaudited; its separate
audit is required before retaining an energy obstruction. Motion,
the real denominator, signed numerator, E_P, Xi transfer and the
main all-degree positivity gap remain unresolved.

This ready continuation was newly written in literature-only step1443;
it requires the supervisor's separate next-turn approval before its
mathematical invocation. No mathematical derivation is performed here.
Full matching Mathlib coverage is unchecked. No novelty is claimed.
