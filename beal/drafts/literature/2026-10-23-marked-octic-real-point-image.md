# Marked-octic exact real point image — source approval

TARGET: Determine the exact real fake two-cover point image of L113's marked octic under Bruin–Stoll's even-degree descent map, retaining every real embedding and both rational infinity points.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the active notebook's marked-octic assessments, L113–L115, ATTEMPTS/052 and history/413 for a prior real-image computation; none was identified. Web queries included Bruin Stoll two cover descent hyperelliptic curves real local image 0803.2052, "Two-cover descent" "real" "Section 5", and "275" "2860" "6930" hyperelliptic; the coefficient query returned irrelevant hits, not an instance certificate.
SOURCE_EVIDENCE: Directly read Bruin–Stoll arXiv:0803.2052v2 (21 October 2008), Section 2 printed p.3 (map, norm fiber, branch and infinity evaluations), entire Section 5 p.11 (real-image rule and scalar quotient), and Remark 6.1 p.13 (global localization warning); reused the inspected support assessment for unrelated finite-support prerequisites.
COMPARISON: Section 5 already supplies the general exact real-image algorithm; this is a specialization of known mathematics, not an uncovered general lemma. The source does not supply the ordered real roots, exact sign list or ambient comparison for L113's polynomial.
GAP: Certify this instance's complete ordered real-root data, apply the source rule, account for each real branch point and both infinity points, and compare the resulting quotient image with the norm-admissible ambient classes; no such instance calculation ran here.
REASON: Essential primary coverage is complete for this unchanged bounded target; approve one later mathematical calculation, importing the general method without reproof.
LITERATURE_REASON: Startup REVIEW_REQUIRED concerned the newly selected exact archimedean image, explicitly outside the older support assessment; Section 5 and its exceptional-point compatibility had not been assessed for this target.
SCOPE: Exactly TARGET on the unchanged smooth proper model of L113, entire algebra of L115 and actual even-degree map of L114; exact root/sign certification and exceptional-point bookkeeping only, without supported representatives, finite-place tests, class/unit arithmetic or rational-point completeness.

## Imported method

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8).
Numbering here refers to the inspected primary manuscript
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008, not inferred journal pagination.

Section 2 p.3 assumes characteristic zero and a squarefree even-degree
model on its nonsingular projective curve. It defines
H_k={delta in A*/(A*² k*): N(delta) in f_n k*²}, A=k[x]/(f).
Ordinary points map to [x−theta]. At (a,0), with f=(x−a)f_tilde,
use [(a−theta)+f_tilde(theta)]. Both infinity points have identity
image when f_n is square.

Section 5 p.11 orders real roots theta_1>...>theta_r. Complex factors
contribute no square-class coordinates. For positive leading coefficient,
the image consists of sign vectors with an even initial block of negative
entries and remaining entries positive; for negative leading coefficient
the initial block is odd. For even degree, quotient by simultaneous sign
reversal. The argument uses root order and f(x)>=0, giving equality,
not sampled containment. Use the explicit vectors, not the apparent
printed exponent typo in its intermediate vector-space isomorphism.
Remark 6.1 p.13 distinguishes this local computation from localization
of global supported representatives, whose signs can require high precision.

## Applicability and finite research contract

The main gap remains zero positive primitive integer solutions in the
residual Beal signatures. The intermediate target is the exact real image
of the marked genus-three curve. Its plausible downstream use is an
archimedean filter on later supported classes. No complete route through
the independent remaining gaps is assumed.

L113 supplies the smooth proper curve and squarefree octic

    G(t)=3025t^8−31460t^6+76230t^4−39204t^2+2673.

L114 fixes the actual scalar quotient and its norm fiber, rather than an
odd-degree descent convention. Its already proved infinity rows are the
two distinct points q=0, Z=−55 and +55, both with fake image [1]. L115
identifies the entire rational algebra with a degree-eight field. This
rational irreducibility is not a claim that the real algebra is a field.
The leading coefficient, degree and squarefreeness in these inputs meet
the imported method's hypotheses. Do not replace G by G/11 as a curve.

The approved next calculation must provide exact ordered real-root
certificates exhausting degree eight, recording every nonreal conjugate
pair as well if present. Rational isolating intervals with exact signs
and a proved count suffice; no floating-point root list alone suffices.
Since the degree is only eight and squarefreeness is already certified,
one may instead certify eight disjoint sign-changing intervals if that
succeeds; this is a proposed test, not a root count established here.
No general root-isolation algorithm needs to be reproved.

Apply the imported rule with the actual order and retain sign labels for
every real embedding. Give interval realizations, cover all components,
and explicitly evaluate each real branch point by Section 2's invertible
replacement. Check the two infinity rows separately on L113's q chart;
never evaluate the affine expression at infinity or identify the two
points because their fake images coincide. Rational exceptions of the
transport to older models do not remove real points of this smooth model.
Only use the actual entire algebra and even-degree scalar quotient.

Compute the norm-admissible ambient sign classes from H_R under that
same quotient, and compare sets, rather than assuming the point image
is a subgroup or counting samples. Record the exact resulting image,
its size, ambient size and any collisions. A proper image supports this
pruning mechanism; full ambient equality stops additional pruning at
this place. Failure to certify complete root/component/endpoint coverage
leaves the target unresolved. No root signs, counts, image dimensions or
new instance lemma were calculated during this literature turn.

## Reuse, failures and limits

The existing support assessment
`drafts/literature/2026-10-21-marked-octic-two-cover-support.md`
explicitly excludes full local images, so its support proof is not a
duplicate solution. The pending assessment and history/413 selected this
independent target; ATTEMPTS/052 records the class-backend blocker and
is preserved. Do not renew backend probes for this calculation.
ATTEMPTS/050–051 concern other point mechanisms and are not global bans.
The search did not locate an exact instance image; that is not evidence
of novelty. The general algorithm is already covered by the source.

No unread lead is needed to authorize this target. Full matching Mathlib
coverage was not checked; no absence assertion is made. Supported units,
ordinary S-class two-torsion, finite point images, surviving-cover points,
degree-nine root recovery, remaining factors, both L095 integer systems
and minus-eleven remain unresolved. L108's unfinished work is preserved.
Known rational infinity points preclude an empty fake-Selmer shortcut.
No cross-notebook input is used. No lemma or mathematical script was
written, and PROOF.md and DAG.md require no change.
