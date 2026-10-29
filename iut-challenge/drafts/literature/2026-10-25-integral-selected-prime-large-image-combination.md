# Integral selected prime and large image — source comparison

TARGET: Test whether L105's fixed P4-exception argument gives large image over G_o and C_o for the same integral prime selected by L117.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step481 searched the specific step419/420/423 coverage, L089/L090/L092/L101/L104/L105/L116/L117 and ATTEMPTS/035–036 for uniform P4 exceptions, prime-selection dependence and full-image hypotheses; reused step419's exact-statement/stronger-result searches. Fresh primary passage lookups located IV P2/P4/P6 and Dupuy–Hilado Lemma 5.4.1. No new broad discovery search or novelty inference.
SOURCE_EVIDENCE: Freshly read IUT IV April 2020 reproduction https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf Corollary 2.2(ii) setup pp.41–42 and P1–P6 pp.45–46, and Dupuy–Hilado https://arxiv.org/pdf/2004.13228v1 Lemma 5.4.1 statement/full split and reduction proof p.27 and transvection interpretation p.28. Reuse step419/420/422 primary GenEll February 2009 https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf Example 1.3 pp.5–6, Lemma 3.1(iii) p.14, Proposition 3.4/Lemma 3.5 p.17, Theorem 3.8(b)/proof pp.19–20; July 2016 comments, Silverman Northcott and L104's Milne/Conrad coverage are specified below.
COMPARISON: The inspected component method uses P2 and fixed-domain height bounds for P4, then a local transvection and absence of an invariant line; its statements do not depend on which admissible-prime selector produced ell. L117 allows any fixed finite parameter exception before R and supplies P1+/P2/P3 at its integral prime. This is coverage for a new same-witness application, not an inference identifying the existing existential conclusions of L105 and L117.
GAP: No essential source gap remains for this bounded component-method application. Mathematics must still place L105's fixed exception before the L117 construction, check the actual H and local/full-representation hypotheses at its selected prime, and justify L104's unchanged-field application. No joint witness is established by this review.
REASON: Approve the saved target as a known-method specialization using the existing component coverage; the changed selector requires an applicability proof, not a general theorem reproof or another source-authentication attempt.
SCOPE: L089 fixed family/domains/closure, d=6, epsilon_d=1, L090 literal full-coordinate F=G_o and C=C_o, L092 relative degree four, L117 arbitrary fixed Exc and actual H, L116 integral ell>=7 with P1+/P2/P3; one unchanged member/order/prime throughout. No direct new-domain application of GenEll Theorem 3.8(b), full native P5/P7 or full repair.

LITERATURE_REASON: The invocation-start target changes from L105's existential image witness and L117's separate integrality witness to a joint witness; this quantified scope was explicitly excluded by the ready L117 assessment and required the present separate comparison.

## Completed comparison — 2026-10-25, step481

The main gap is original finite B>=A under the original IUT hypotheses.
The intermediate target remains exactly TARGET. Its plausible downstream
use is a common integrality/support and large-image prerequisite before
native assembly. Approval concerns source coverage only. No new lemma,
mathematical calculation, application or correctness audit is performed.

### Primary statements and qualifications

The fresh IV read identifies April 2020, 87 pages. Corollary 2.2(ii),
pp.41–42, fixes the compact bounding set, bounded parameter degree and
Legendre-adjunction setup, including level-15 rationality. On p.45,
P4's cyclic-subgroup implication is

    ((ell-2)/24) H <= 2 log(ell)+T_K.

The text explicitly invokes (i), P2 and GenEll Proposition 3.4/Lemma
3.5 with epsilon=1; T_K depends only on the fixed bounding set. Its
prime lower bound is ell>=5. The finite-exception enlargement precedes
the chosen curve. P6 on p.46 invokes P2, P4 and GenEll Lemma 3.1(iii).
These passages do not impose an additional predicate that ell was
obtained by exactly S1–S3 rather than a larger exclusion set. Import
these implications, not the corollary's later P7 assertion.

The fresh Dupuy–Hilado v1 read identifies 28 April 2020 in the arXiv
header (manuscript dated 29 April). Lemma 5.4.1, p.27, assumes a finite
p-adic field, negative normalized integer j-valuation and an odd prime
not dividing that valuation. Its proof uses Tate/Kummer uniformization
and reduction by a splitting/cyclotomic extension of degree dividing
2(ell-1); p.28 identifies the resulting full-torsion transvection.
The proposed application retains the safer ell!=p case, specifically
p=3. No global pre-theta-data hypotheses from their Definition 5.3.1
are imported with this local lemma.

Reuse, without another blocked retrieval, the primary GenEll readings
recorded in the step419 source-scope assessment and the step420/422
application/audit assessments. The February 2009 author version has
25 pages. Lemma 3.1(iii), p.14, is the prime-field group input: a
transvection and a non-upper-triangular element in the same basis
force SL_2 containment. Proposition 3.4/Lemma 3.5 and their proofs,
p.17, supply the height/isogeny input used above. The stronger Theorem
3.8(b), pp.19–20, has a compact moduli-set and Galois-finite exception
scope. A new direct application would need an additional domain
comparison and is unnecessary for this component method.

Keep the [July 2016 comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position%20(comments).pdf),
(8),(13)–(16), pp.1–2, as recorded in step419: open bounding domains
and extension/level-structure qualifications remain in force.
Journal pagination/byte identity and current author/journal identity
of the IV reproduction are not certified. L091's def= qualification
is retained. No authentication endpoint or timed-out GenEll refresh
is retried.

### Exact scope of the later specialization

| Obligation for the same witness | Coverage and remaining mathematical check |
| --- | --- |
| Exception fixed before R | L105's audited proof supplies the fixed finite Exc_4 and B_4, not an image theorem for an arbitrary earlier witness. Reuse its Northcott input: Silverman, AWS notes, 13 February 2024, Theorem 4.8(d), p.15, with Definitions 4.4–4.5/Proposition 4.6 pp.13–14, https://swc-math.github.io/aws/2024/2024SilvermanNotes.pdf. L117 hypotheses and its fixed-parameter-exception argument allow an arbitrary fixed finite Exc. A proof must incorporate Exc_4 before its one construction and retain all six parameters' avoidance. |
| Actual height and P4 | L101 identifies H with the rational reduced-denominator height for these survivors. L105's fixed-domain cutoff and source prerequisites are separately audited. Check their applicability to the L117 member and its ell, rather than invoking L105's existential conclusion with a renamed witness. P2 is the full all-place nonzero integer-height condition, not merely avoidance of rational pole primes. |
| Literal fields and domains | L089 fixes the domains before R; L090 gives the full-coordinate Legendre fields. L101's actual-field semistability and torsion facts are available before selecting ell. Keep these qualifications when using the source height implication; do not assume F/Q normality or initial theta-data. |
| Local inertia at three | L089 retains its split height-30 original condition; L101's all-place calculation supplies the actual F-completion heights. Check this retained local input, P2, ell>=7 and the normalized j-order for the chosen F-place before the cited local theorem. Nonsplit F-reduction is within the covered cases. This verifies only the local input needed for image, not native P5. |
| Full downstairs image | Characteristic-zero finite-etale descent identifies invariant lines in the entire E_o[ell] with F-defined cyclic subgroup schemes, as used and audited in L105. Check P4 and the local transvection on that same module before the cited GenEll group theorem. No inference from the original Q-curve's mod-seven image is approved. |
| Restriction to C_o | Reuse L104 and its step418 audit, including Milne, Fields and Galois Theory v5.10 (September 2022), Theorem 3.17(b,d), Propositions 3.19/3.21 pp.39–42 and 7.3/7.4/7.7 pp.95–96, https://www.jmilne.org/math/CourseNotes/FT.pdf; Conrad, Simplicity of PSLn(F), Theorem 3.3 p.4, https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf. Match the new selection to L104's actual hypotheses explicitly; L090/L092's normal closure and relative degree four are unchanged. No new restriction theorem is needed. |

These are applicability obligations, not derivations in this literature
turn. SPECIALIZE approves exactly TARGET for a later RESEARCH /
REPRODUCTION attempt. The discriminating test is one construction with
the exception fixed first, followed by checks at its same ell. A need
to select another member or prime, or an unmet source hypothesis, stops
the combination. In particular, L105 and L117 as currently concluded
remain two separate existential results; this review does not merge them.

### Duplicate/failure screen and decision

L105 already establishes occurrence by the component method but excludes
integrality; L117 already establishes integrality but excludes image
at the selected prime. L104 is conditional transfer. None is a theorem
asserting this joint conclusion as written. Their source methods can
be reused, so no general isogeny, sieve, inertia or group theorem should
be reproved. This comparison makes no novelty claim. L047/L083's other
prime-seven witnesses remain irrelevant as replacement witnesses.

ATTEMPTS/035's repeated authentication/approval route and ATTEMPTS/036's
scalar-only pole cap remain stopped. The present changed-target review
does not reopen either, or the directed-module extraction blocker.
No new mathematical input or informative obstruction has been proved:
record STALLED / LITERATURE / NOVELTY_UNCHECKED, with ready coverage
and mathematics next. No mathematical exploration turn is spent.

Essential IDs are L089,L090,L092,L101,L104,L105,L116,L117; L101 already
includes L100's local-height input. L098 is downstream only. Full
(a)–(c)/initial data/III/P7, directed (*), generation/full repair,
factor-four excess, actual action/factorization/pilot, authentication/
def=, essentiality and finite B>=A remain unresolved. No U/B descent,
full B[ell] rationality or global theta splitting is assumed. Matching
and supporting Mathlib coverage remain unchecked. STATUS is IN_PROGRESS;
there is no candidate solution. PROOF.md and DAG.md do not change.

## Invocation-start proposal — historical, superseded by the review above

Main gap: original finite B>=A under the original IUT hypotheses.
Intermediate target: TARGET. A common witness for integrality/support
and image would help before any reuse of the native assembly; it would
not alone repair initial data.

Essential input IDs: L089,L090,L101,L104,L105,L116,L117; L092's actual
relative degree is already an input to the image-transfer argument.
Keep the fixed family and domains, constants fixed before R, literal
full-coordinate G_o and C_o and the actual downstairs H. L098 is
downstream only. An arbitrary earlier L105 witness cannot be substituted
for the member selected in L117.

The test is whether the inspected P4 implication and finite exception
are uniform before the L117 member and prime are chosen, using only
hypotheses preserved by that selection. Check the full-representation
and local multiplicative-place premises before using L104. A required
change of member or prime, or an unmet extra source hypothesis, fails
this combination test. Do not identify existential witnesses by notation.
This is a proposed test, not a derivation or approval in this turn.

Reuse step419/420/423 coverage where adequate. Primary locators:
[IUT IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
pp.45–46; [GenEll February 2009 author version](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf),
pp.14,17; [Dupuy–Hilado v1](https://arxiv.org/pdf/2004.13228v1),
Lemma 5.4.1 pp.27–28. These identify reusable evidence, not certification
of the changed combination. No authentication retrieval is proposed.

Recovery compared joint image/integrality, exact-generation repair and
the directed module action. The first has a concrete quantifier test
and reusable source leads. No comparably bounded exact-generation test
was selected. The directed module remains blocked by the symbol
extraction recorded in its assessment. ATTEMPTS/035 and /036 remain
valid; neither repeated authentication nor a scalar-only pole-cost cap
supplies this representation-theoretic comparison.

Unresolved: full (a)–(c)/initial data/III/P7, directed (*), generation/
full repair, factor-four excess, action/factorization/pilot,
authentication/def=, essentiality and finite B>=A. No U/B descent,
full B[ell] rationality, global theta splitting or common prime for
six orderings is assumed. Mathlib matching/supporting coverage is
unchecked. STATUS remains IN_PROGRESS; no candidate is claimed.
