# Contact-conditioned seventh-moment extension: completed source comparison

TARGET: Assess source coverage for a single contact-conditioned seventh-moment test on L917's saved first parameter panel: decide whether its full moment enclosures, strict H1 bounds, all H2 null rows and raw Stieltjes positivity force L874's d=2 flux to be nonpositive, or permit one certified violating tuple.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step37 reused the completed weighted-cubic and actual-box-origin comparisons, compared L874/L917/L921/L922/L923 and automatic-score/logarithmic-Schur stops, and searched exact seventh-moment/flux, odd truncated Stieltjes, singular range and stronger cumulant terminology; queries and read limits below. No inspected matching sign theorem or duplicate fixed-panel S7 test; no novelty claim.
SOURCE_EVIDENCE: Curto-Fialkow, Houston J.Math.17(1991)603-635, Theorem5.1 p625, Corollary3.4 pp615-616 and Theorem4.1 proof pp622-623, https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf ; reuse Laurent updated2010 Lemma4.2 pp54-55 and Theorem3.15 p36 https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf and Gallier2019 Proposition4.2/Theorem4.3 pp9-12 https://www.cis.upenn.edu/~jean/schur-comp.pdf . Primary odd statement and relevant singular cases inspected; prior full certificate-source coverage reused.
COMPARISON: The raw PSD constraints are necessary, not the singular-case representing-measure criterion: Curto-Fialkow also requires (y4,y5,y6,y7) in Ran M3. No converse or automatic logarithmic sign is used. L921 tests J without these bounds; L923's Gaussian has S2=0; L922 tests a determinant enclosure. None decides this common-mass contact-conditioned S7 class.
GAP: Sources cover the finite necessary-moment, singular-Schur and exact certificate tools but do not decide Phi<=0 or feasibility for the saved class. A single bounded mathematical test remains; actual realization, extra tilt relations, initialization/tangency, other panels/degrees and global continuation remain independent gaps.
REASON: Essential changed-target coverage is complete; nominate one fixed-class flux certificate-or-witness attempt, subject to separate next-turn approval. This is source readiness, not a new lemma, calculation, sign, contact or advance beyond inspected sources.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified essential missing degree-seven and singular truncated-Stieltjes comparison; reuse ready older coverage and fill only that changed scope before mathematics.
SCOPE: Completed step37 is literature-only. The preserved step36 nomination below is historical; the exact bounded mathematical continuation is specified separately in 2026-11-09-contact-conditioned-seventh-moment-test-37.md. No tuple, elimination, new bound, lemma or mathematical script was produced.

## Purpose and comparison of three mechanisms

The main gap is L030--L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a boundary direction at full-degree d=2
contacts. A proved sign on the finite class below would be usable for
actual contacts in this one panel, after checking inclusion; proved
emptiness would instead exclude those contacts. Neither would handle
initialization, equality/tangency, other panels/degrees or global
continuation. A violating relaxed tuple would stop this particular
finite-data mechanism, not refute the actual flux or RH.

Three alternatives were compared, without executing a second attempt:

1. The L935 prescribed Mobius form still needs its signed eigenvalue
   separation. Its now-verified transfer is not a new sign input or
   reason to repeat the parked attempt.
2. L923's fixed density/Legendre floor leaves its exact deficit unpaid.
   The recorded Gaussian comparison has S2=0, so it does not test a
   mechanism retaining the available strict H1 data. No interval
   tuning, extra quadrature or new norm floor is nominated.
3. Select a contact-conditioned seventh-moment extension using those
   strict data and the *existing* complete lower-moment enclosures.
   This tests a finite sufficient condition for the flux itself,
   rather than another origin residual or unconditional determinant box.

The generic covariance-to-logarithmic-Schur and automatic-score imports
remain stopped at their missing sign interfaces. Their source blockers
are not prerequisites here, and no retrieval retry is requested.

## Exact proposed finite test — not yet performed

Use only panel p=0, [0,1/5120], of L917's
`scripts/heat/low-time-h2-uniform-195.json`. The later work must inspect
the complete relevant intervals and their field meanings, including
both theta and spatial tails, with the bounded JSON inspector. Do not
infer values from a preview or run a new quadrature. Let m_j, 0<=j<=6,
be real variables in those saved full enclosures of M_(2j), with m0>0,
and put y0=1, y_j=m_j/m0 for 1<=j<=6. Keep this common normalization;
do not silently replace it by independently rescaled data. Introduce
one real variable y7. No other new moment or free tail bound is allowed.

Define the finite local logarithmic S1,...,S7 from
g(t)=sum_(j=0)^7 (-1)^j y_j t^j/(2j)! and
log g(t)=-sum_(j=1)^7 S_j t^j/j modulo t^8, exactly as in L874/L923.
Require all of the following simultaneously:

- M3=(y_(i+j))_(0<=i,j<=3) and N3=(y_(i+j+1))_(0<=i,j<=3)
  are positive semidefinite. These are necessary raw-moment conditions;
  no representing measure, strict full support or converse is assumed.
- H2=(S_(i+j+2))_(0<=i,j<=2) is positive semidefinite, with a real
  unit c=(c0,c1,c2), c2!=0, and every row of H2*c=0.
- Retain the saved actual bounds S2>3.714*10^(-5) and
  9.7*10^(-16)<S2*S4-S3^2<7.026*10^(-15). Their use carries
  L917's stated directed-arithmetic contract. No new theta value is
  presumed. c0 or c1 may vanish; no uniform lower bound for |c2| is given.

The output to test is exactly Phi=-156*c2^2*S7+B from L874(2), with
d=r=2 and its original b_n and B, or its already proved L923 expression.
The source review must verify that this change to degree seven and the
singular PSD cases have adequate coverage. It must not derive a new
elimination, evaluate the data or construct a tuple during review.
The degree-seven constraints are deliberately a finite relaxation of
actual theta: exponential-tilt relations beyond the saved enclosures
and existence of an actual lambda are not assumed for a test tuple.

After separate approval, the bounded discriminator would be either a
proof of Phi<=0 on this exact class (or its emptiness), or one exact/
rigorously enclosed tuple satisfying *every* condition with Phi>0.
An approximate optimizer or a witness outside the saved intervals does
not pass. If neither is obtained in one bounded attempt, retain the
first unresolved inequality and stop; do not widen the intervals,
drop a null row, add a new moment, change the panel or launch a sweep.

## Continuation qualifications and routing

Essential prospective inputs are L019/L058 for actual-law inclusion,
L874 for the exact contact flux, L917 for the complete first-panel
intervals and strict bounds, and L923 for the already proved S7/norm
interface if used. L921 and L922 are contrasts only. No cross-notebook
input. The canonical input proofs and exact certificate fields must be
read at their needed ranges in the later attempt. Full matching Mathlib
coverage is unchecked, not asserted absent. No standard Schur or moment
theorem needs a new proof.

The step36 immediate action was literature_comparison/standard/high because
this changed exact target has no completed assessment. Reuse the source
coverage above, inspect only genuinely missing primary cases, and check
duplicates before approving mathematics. No source-access campaign is
authorized by this nomination. If adequate scope is confirmed and the
mechanism survives comparison, its mathematical purpose would be a
creative proof attempt: the precise obstruction is the unpaid S7
boundary coefficient, and the bounded test is the fixed finite class
above. That future routing would require its own exact approved target;
it was not an approval or second mathematical step in step36.

## Completed comparison — step37, 9 November 2026

The invocation-start review target is unchanged. This review preserves
the finite class above, including one common m0 and the strict H1
information; it has not solved a feasibility problem or introduced an
extra constraint. The next mathematical target is recorded in
`2026-11-09-contact-conditioned-seventh-moment-test-37.md` and awaits
the supervisor's separate approval.

### Primary odd-degree result and singular cases

Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, positivity, and
truncated moment problems*, Houston Journal of Mathematics 17(4)
(1991), 603-635, [Theorem5.1, printed p625](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf),
characterizes representation on [0,infinity) for real gamma0,...,
gamma_(2k+1), gamma0>0. Its conditions are A(k)>=0, B(k)>=0 and
v(k+1,k) in Ran A(k); finite atomic representation is equivalent.
Here A(k)=(gamma_(i+j)), B(k)=(gamma_(i+j+1)), and
v(k+1,k)=(gamma_(k+1),...,gamma_(2k+1)). With k=3 these are exactly
M3, N3 and (y4,y5,y6,y7). The theorem adds a range hypothesis to
the proposed necessary-only class. That class remains unchanged;
representation and strict support cannot be asserted from it.

Read p625 visually to resolve the OCR's inequality signs. The authors
omit a separate proof of Theorem5.1, referring to Theorem4.1. Inspected
its proof pp622-623 and Corollary3.4 pp615-616: singular Hamburger
data are reduced to a nonsingular leading block and extended by
recursion; the support restriction uses finite atomic representation
and interpolation. No reconstruction or proof of that theorem is
performed here. Only necessary PSD conditions are needed for the test.

Reuse the completed [weighted-cubic review](2026-11-09-d2-flux-weighted-cubic-norm-review.md)
for Laurent's Lemma4.2(i)-(iii), updated6February2010, pp54-55.
For the actual law, the x=u^2 pushforward has all finite moments by
L058, so the raw moment and x-localizing conditions apply. N3 uses
moments only through y7. If using Laurent's even-truncation statement
literally, t=4, g(x)=x gives its order-three localizing matrix; the
actual law has the required higher moments. No y8 variable or
extension premise is being added to the finite relaxation. The
odd-degree theorem above independently supplies the needed necessity.
Raw kernel-support statements do not apply to the logarithmic H2.

Reuse Gallier's author version24August2019, Proposition4.2 and
Theorem4.3, pp9-12, from that same completed review. Theorem4.3 states
that a real symmetric block [[A,B],[B^T,C]] is PSD exactly when A is
PSD, (I-AA^dagger)B=0 and C-B^T A^dagger B is PSD. The singular
quadratic proof distinguishes a nonzero linear term on the null space
from minimization on the positive subspace. Rechecked those relevant
cases and the theorem statement. A future Schur reduction must retain
the range condition; logarithmic contact information does not license
an inverse of a raw block. The safe unreduced matrix conditions in
the nominated target require no inverse at all.

Reuse the [actual-box-origin comparison](2026-11-09-actual-box-origin-contact-test.md)
for Laurent Theorem3.15, p36: its polynomial feasibility alternative
allows inequalities, equations and disequalities. Its exact certificate
soundness therefore covers nonzero c2 and strict inequalities after
legitimate denominator clearing. It gives no practical degree bound
or guaranteed rational certificate. Theorem3.16's compact strict
positivity conclusion does not automatically certify a nonstrict flux
inequality here. A numerical solver output is not such a certificate.
No general moment, Schur or Positivstellensatz theorem needs reproof.

### Saved data and normalization scope

Read L917's hypotheses, conclusion, full-moment inclusion argument and
relevant step197 audit ranges. The complete fourteen endpoint strings
at `/panels/0/moments` and the complete `/panels/0/lambda` value in
`scripts/heat/low-time-h2-uniform-195.json` were inspected using
`python3 ../scripts/loop/inspect_json.py` with the selected pointers
and `--full`. These are the full M0,M2,...,M12 intervals, including
both nonnegative tail contributions, not finite-integrand or
factorial-normalized coefficients. The panel is [0,1/5120]. The
earlier assessment's full endpoint inspection is corroborated; no
quadrature, replay, ratio, extremum or logarithmic coefficient was
computed in this turn.

The common-mass formulation m_j in the saved interval for M_(2j),
y_j=m_j/m0, m0>0, is retained exactly. It is not replaced by the
independent quotient boxes of the older J test. The actual law lies
in this necessary enclosure conditional on L917/L037's stated
directed-arithmetic assumptions. The full-band strict bounds for S2
and S2*S4-S3^2 may be retained on this panel under the same contract.
They are constraints on the relaxed class, not an assertion that every
tuple in the moment box satisfies them. The saved endpoint decimals
are exact rationals for defining the finite test; do not round them.

For the future actual-family inclusion, L019/L058 supply the law and
its finite moments; L874 supplies the germ and exact flux. L923's
already proved finite S7 formula may be used, but its full-support
raw inverse and density floor are not premises for arbitrary tuples.
No new analytic or algebraic reduction has been derived in this review.

### Searches, stronger results, duplicates and stops

New queries were `truncated Stieltjes moment problem odd degree 2n+1
positive semidefinite range condition Curto Fialkow`; `Curto Fialkow
1991 Recursiveness Stieltjes pdf`; `"theta" "contact" "seventh
moment" flux`; `"Hankel" "cumulants" "heat flow" positivity null
vector`; `"Riemann" "cumulants" "Hankel" "heat flow" positivity`;
`"Riemann" "seventh" "moment" "Hankel"`; `"logarithmic" "Hankel"
"contact" positivity theta`; and `"truncated Stieltjes" "cumulants"`.
The inspected primary statements above, not search snippets, support
the scope decision. No bounded search proves novelty.

Reuse step220's inspected Choi comparison and Gaussian/orthogonal-norm
sources; its conditional low-time hierarchy and unconditional results
in other ranges do not supply the present sign. The third-party
cumulant-lifting lead associated with arXiv2611.03208 was checked
against [the official abstract/version record](https://arxiv.org/abs/2611.03208v1):
it instead identifies Luc Rey-Bellet's matrix trace Stieltjes
representation paper, submitted2November2026. The purported lifting
theorem was not verified there; no theorem from that lead is imported.
Thorin/SSRN and web-project hits remain uninspected, nonessential
leads. No conclusion of applicability or novelty rests on them.

Narrow local searches/readings covered the weighted-cubic and original
d2-flux assessments, the actual-box J nomination, L921/L922/L923,
and the automatic-variation/logarithmic-Schur attempt records. L921
addresses J, omits the numerical boxes and strict actual bounds, and
uses N2 rather than this N3. L922's fixed shared-parameter determinant
enclosure is inconclusive, not a conditional S7 decision. L923's
Gaussian invalidates only its enlarged floor comparison, with S2=0.
Automatic score or raw covariance positivity still supplies no flux
sign. These stops remain preserved; no duplicate of the exact
common-mass S7 test was located in the compared paths.

### Coverage decision and bounded discriminator

EXPLORE: enough essential standard-source coverage is available for
one test of the unchanged finite class. No source decides its sign,
nonemptiness, actual contacts or realization. The creative purpose of
the proposed attempt is the quantitative interaction between the
actual lower-moment enclosures, all null rows and the unpaid S7
coefficient, rather than a new general moment or Schur theorem.
After separate approval, require a rigorous Phi<=0/emptiness proof
or one certified Phi>0 tuple satisfying every retained constraint.
If neither is obtained, save the first unresolved comparison and stop
without changing the class, panel, evaluator or budget. Full matching
Mathlib coverage remains unchecked; supporting matrix theorems are
not a full theta-flux theorem. No mathematical scripts or lemmas were
written; PROOF and DAG need no change because the argument is unchanged.
