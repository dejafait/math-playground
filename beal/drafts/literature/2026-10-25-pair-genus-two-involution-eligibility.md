# Genus-two quotient — rational involution eligibility source review

TARGET: Determine whether L110's genus-two curve admits a Q-defined involution other than its hyperelliptic involution, with a certified exhaustive branch-point test and the exact twist retained.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched genus-two rational automorphisms, binary-sextic/Mobius algorithms, elliptic subfields and the displayed sextic coefficients; compared local pair/decomposition assessments, L110/L127, history/469 and ATTEMPTS/050,053–055; found general complete methods but no inspected exact-instance certificate or local duplicate.
SOURCE_EVIDENCE: Read Lercier–Ritzenthaler–Sijsling, Open Book Series 1 (2013), Sections 2A–2B pp.465–468 and 2E1 p.474, including normalization/zero-diagonal qualifications and rational lifts; Shaska–Volklein arXiv:math/0107142v1 Sections 1–2 and 3.1, Lemma 2(a) and both proof cases p.7; official Magma handbook Isomorphisms and Transformations, representation and base-ring AutomorphismGroup contract.
COMPARISON: Known methods cover exhaustive branch-form testing and distinguish fixed-point-free reduced involutions, rational lifts and order-four lifts. They do not evaluate this sextic; geometric normal forms alone do not establish a rational automorphism of the actual Q-model.
GAP: In a separate research turn certify the rational branch set, prove a complete rational branch-pair parametrization, exhaust its coefficient equations and check rational lifts/order two on L110's proper model within the caps below.
REASON: Primary coverage now supports a bounded known-method specialization on the independent genus-two summand; import the general theorems and compute only the instance difference next turn.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; prior marked-cover/Prym assessments do not cover additional involutions of the genus-two base, exhaustive branch testing or lift order.
SCOPE: Exactly TARGET via rational branch-pair normalization and full binary-sextic identities, including conditional preprocessing, exhaustive rational-root certificates, proper extension, rational lifts and order checks; no quotient construction, rank bound, point completeness, larger boxes or backend reprobe.

## Relevance and local inputs

Essential mathematical input is audited L110: the smooth proper genus-two
curve B with exact sextic W²=f(T)=11(T²−4)Q4(T), where
Q4(T)=7+52T−6T²−64T³−25T⁴. Its entire infinity chart has
V²=−275 at h=0. L127's ordinary rank decomposition supplies the
plausible downstream use: an additional rational involution could
permit elliptic-subcover rank work on Jac(B). L130 and the prior
stops are routing evidence, not mathematical premises for eligibility.

The main gap remains numerical upper ranks and point control, followed
by marked lifts, degree-nine recovery, both L095 systems, minus-eleven
and the other signatures. A useful involution would leave these
independent gaps open. This literature-only turn establishes source
readiness; it does not calculate an involution or derive a new lemma.

## Primary inputs actually inspected

Reynald Lercier, Christophe Ritzenthaler and Jeroen Sijsling,
*Fast computation of isomorphisms of hyperelliptic curves and explicit
Galois descent*, The Open Book Series **1** (2013), 463–486,
DOI [10.2140/obs.2013.1.463](https://doi.org/10.2140/obs.2013.1.463),
[published primary PDF](https://msp.org/obs/2013/1-1/obs-v1-n1-p23-p.pdf).
Read **Sections 2A–2B, pp.465–468**, Definition 2.1, Lemma 2.2,
equations (1)–(2) and the direct algorithm; **2E1, p.474**, the full
isomorphism representation. For squarefree even degree 2g+2>=6 in
characteristic different from two, all curve isomorphisms are represented
by (M,e), M in GL2(k), e in k*, modulo (M,e)~(rM,r^(g+1)e).
The binary-form multiplier determines the geometric lifts; a rational
lift requires its square root in Q. Section 2B uses univariate
coefficient equations, assuming characteristic prime to the degree and
a centered first form. Its scalar normalization may require a radical
extension; zero diagonal entries require further coordinate changes.
Thus a generic gcd or extension-field normalization alone is incomplete.
Import this framework; retain the multiplier and all parameter charts.

T. Shaska and H. Völklein, *Elliptic subfields and automorphisms of
genus 2 function fields*, inspected
[arXiv:math/0107142v1](https://arxiv.org/pdf/math/0107142v1),
19 July 2001, **Sections 1–2, pp.1–4**, and **Section 3.1, pp.6–7**,
especially **Lemma 2(a), both proof cases, and Remark 3, p.7**.
The constant field is algebraically closed of characteristic different
from two. The reduced group stabilizes the six branch points. A
reduced involution has order-two lifts precisely when it fixes no
branch point; if it fixes two, its lifts have order four. The proof
handles these alternatives using an even sextic and an odd quintic
respectively. Nonhyperelliptic involutions correspond to degree-two
genus-one subfields. These geometric criteria and Theorem 1's normal
form do not settle rational descent. Use Lemma 2 over Qbar and the
rational lift representation above. No normal form is computed here.

Official [Magma handbook, Isomorphisms and Transformations](https://magma.maths.usyd.edu.au/magma/handbook/text/1626),
accessed 2026-10-25, opening representation and **Automorphism Group
and Isomorphism Testing**, `AutomorphismGroup(C)`. It specifies
automorphisms over the base ring and distinguishes geometric base
extension. In genus at least two the preceding primary source gives
centrality of the hyperelliptic involution, so the handbook's commuting
condition omits none here. This corroborates the arithmetic distinction;
it is not evidence of software availability or an execution on B.

For proper extension reuse already assessed
[Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
from `2026-10-20-marked-pair-genus-one-quotient.md` in this directory.
L110 supplies its smooth proper hypotheses. Function-field maps must
be established first; finite formulas alone cannot discard infinity.

## Obligations for the separate research turn

The following is a proposed specialization to prove and execute later,
not a completed derivation or an eligibility finding.

1. Apply the rational-root theorem completely to Q4, recording all
   reduced candidates and exact residuals. This specialization requires
   that the only rational branch points are T=2 and T=−2; a bounded
   point search does not establish this. If preprocessing contradicts
   that condition, stop this specialization without an eligibility claim.
2. From the imported branch action and fixed-point-free criterion,
   justify that every sought involution is in the rational Mobius
   family exchanging those two points. Derive a complete projective
   parameter family, with every chart and singular-matrix exclusion.
   Do not fix the points individually or require rational fixed points
   of the Mobius transformation. This completeness argument remains
   to be written next turn.
3. Substitute that family into the **full homogeneous sextic**, retaining
   11, and solve all rational parameters for proportionality. Save every
   coefficient polynomial, exact gcd/Bezout or factorization evidence,
   exceptional parameter check and complete rational-root certificate.
   Verify surviving matrices by the full coefficient identity. A generic
   shortcut needs all omitted cases covered. No survivors gives a negative
   only after the family has been proved exhaustive for the target.
4. For every survivor determine the actual sextic multiplier, test its
   rational square root and square the resulting function-field map.
   Exclude the identity and hyperelliptic involution; verify order two
   rather than order four. Account for proper extension and L110's
   infinity fiber. A positive result establishes eligibility only;
   quotient equations, origins and rank comparison remain later work.

Feasibility rests on degree six and, conditional on the preprocessing,
a single projective parameter and univariate rational polynomial
arithmetic, rather than a height search or splitting-field construction.
This is a bounded proposal, not a measured workload or a completion
promise. Fixed whole-step caps, including preparation, certificate
creation, postprocessing and replay: **10000 integer divisor trials**
and **200000 charged work units**. A unit is one rational-candidate
test, univariate polynomial arithmetic operation, coefficient/matrix
check, or processed certificate row. Polynomial operations also require
degree <=64 and input/output rational numerator/denominator bit length
<=4096. Define and instrument these charges before execution; do not
claim to measure library-internal elementary operations. Charge repeated
executions cumulatively. Stop before a cap, saving full evidence and
unfinished reasoning; a cap stop is incomplete, never an exhaustive
negative. Do not enlarge caps or change mechanisms automatically.

Continue toward an elliptic subcover only with a certified additional
Q-defined order-two lift on B. An exhaustive negative stops only this
degree-two-subcover mechanism; it does not bound rank or exclude
higher-degree elliptic covers. Mathlib coverage is not checked; no
absence or Lean-verification claim is made. No cross-notebook input.

## Search, duplicates, failures and remaining leads

Queries used included `genus 2 automorphisms rational field binary
sextic Mobius transformations extra involution algorithm`,
`Shaska Volklein elliptic subfields genus 2 extra involutions sextic
automorphism`, `Lercier Ritzenthaler Sijsling isomorphisms hyperelliptic
curves algorithm rational automorphisms branch locus`, displayed
coefficient strings, and rational Weierstrass-point variants. No exact
instance was identified in inspected sources; this does not certify
novelty. Selected local searches covered `drafts/literature`, `ATTEMPTS`,
`history`, `foundations` for automorphisms, involutions and elliptic
subcovers. Relevant L110/L127 proof ranges, the marked-cover assessment,
history/469 and ATTEMPTS/050,053–055 were read. A narrow keyword search
of `scripts/pair-genus-two/*.py` found no matching routine. Earlier
rank-lower searches, quartic enumeration, seminvariant sieving and
three-isogeny exclusion do not exhaust this automorphism target.
Preserve those stops and unfinished L108.

Unread leads: J.W.S. Cassels and E.V. Flynn, *Prolegomena to a
Middlebrow Arithmetic of Curves of Genus 2* (1996), Theorem 14.1.1
(cited by Shaska–Volklein Remark 5 for a three-quadratic determinant
test), and the full invariant-locus route in that paper's Theorem 3.
Neither is essential here; no determinant or invariant implementation
is approved. Invariant reconstruction and database hits were not used
as exact-instance evidence. All essential coverage for the prescribed
coefficient method is accessible.

Primary target rechecked 2026-10-25: the nominated
[AMS page](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize)
returned HTTP 403 again. The accessible
[Mauldin primary statement](https://sites.math.unt.edu/~mauldin/beal.html)
again specifies positive integer bases and exponents greater than two,
with a common prime divisor conclusion, matching the existing foundation.
No current AMS wording or adjudication claim is made. This independent
administrative-source blocker does not obstruct the reviewed curve test.
