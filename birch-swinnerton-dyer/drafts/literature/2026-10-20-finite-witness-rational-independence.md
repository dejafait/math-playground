# Rational independence from the finite witnesses — source assessment

TARGET: Certify the rational independence of P=(0,0) and Q=(1,0) on E=[0,1,1,-2,0] from L081, L096 and L097 without published rank, saturation or Sha premises.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-curve independence, reduction/saturation and abelian-group independence-modulo-p searches located Datta–Smith Lemma 5.5 and Milne's group structure theorem; local L034, L081, L083, L096, L097, histories 376/381–384 and ATTEMPTS/045 checked for overlap and restrictions. Queries and inspected ranges below.
SOURCE_EVIDENCE: Datta–Smith (2016), Lemma 5.5 and its complete independence argument, p.1073; their 2017 correction Section 1, pp.1003–1004, explicitly retaining Lemma 5.5; Milne Group Theory v4.01, Theorems 1.54/1.57 and relevant proofs, pp.25–26; Silverman (2009) VIII.6.7 p.239 and IV.6.4/Remark 6.5 p.132 inspected, with prior assessed VII.2.1–2.2 coverage reused.
COMPARISON: L034 already imports the stronger published independent basis. The general independence passage is known, including a directly matching torsion-free criterion in Datta–Smith's proof. The difference to reproduce is its applicability to these finite witnesses after torsion removal, without importing the published basis, rank, saturation or Sha computation.
GAP: No essential source is missing. The next research step must prove the finite two-class independence test, justify passage through the rational torsion quotient, and apply the cited criterion to these exact points; none of those fixed-target conclusions is established by this literature turn.
REASON: Primary comparison now covers the previously unassessed group and torsion hypotheses; a separate known-method specialization is justified, without a new general lemma or arithmetic search.
LITERATURE_REASON: The saved REVIEW_REQUIRED target moves beyond the finite-class audit to rational independence; its essential independence and torsion coverage was missing at invocation start.
SCOPE: Only E=[0,1,1,-2,0], P=(0,0), Q=(1,0), R=Q-4P and p=7, using L081/L096/L097, L030/L033 arithmetic and only L083's local quotient/torsion argument. No new arithmetic search, published rank, saturation, Sha premise or full-kernel claim.

The main gap remains arbitrary-curve rank equality at analytic order at
least two. This proposed intermediate target asks for independent point
input from the existing finite certificates. Its plausible downstream
use is the rational-direction premise in the existing L004/L005 route,
with all other hypotheses retained. L098 alone is only finite strictness.

Essential inputs for the approved specialization are L081's primitive local
value, L096's complete local relation and L097's global nondivisibility
of R=Q-4P; L083's local torsion argument may be inspected in its restricted
scope. Do not use L034's global basis or L082's Sha conclusion as a
hidden premise. The fixed group-theoretic passage and its torsion treatment
remain research obligations, not conclusions of this source assessment.

Continue with a separate proof attempt if the finite witnesses establish
injectivity of F_7^2 -> E(Q)/7E(Q) on the specified pair and the torsion
quotient preserves that test. Reject an argument needing unprovided
saturation, rational rank or Sha data, or substituting the published basis.
This approves source coverage, not the proof of independence. Preserve
ATTEMPTS/045 and all stopped order-table work.

## Primary results and their precise scope

[R. Datta and K. E. Smith, *Frobenius and valuation rings*, Algebra &
Number Theory 10:5 (2016), 1057–1090, DOI 10.2140/ant.2016.10.1057,
Lemma 5.5, p.1073](https://msp.org/ant/2016/10-5/ant-v10-n5-p05-s.pdf#page=18)
states [Gamma:p Gamma] <= p^s for a torsion-free abelian group Gamma of
rational rank s. Its complete proof explicitly establishes the stronger
pointwise input needed here: elements independent in Gamma/p Gamma are
Z-independent in Gamma. The proof uses torsion-freeness to remove common
p-factors from a relation. This is a group result; no valuation-field,
F-finiteness or residue-characteristic hypothesis is part of the lemma.
Import this argument rather than present it as an original criterion.

The paper has a consequential correction. [Datta–Smith, *Correction to
the article Frobenius and valuation rings*, ANT 11:4 (2017), 1003–1007,
DOI 10.2140/ant.2017.11.1003, Section 1, pp.1003–1004](https://msp.org/ant/2017/11-4/ant-v11-n4-s.pdf#page=239)
was read through its complete list of affected statements. It explicitly
retains Lemma 5.5 because that lemma does not use the erroneous valuation
statement. No corrected valuation theorem is needed for this target.

[J. S. Milne, *Group Theory*, v4.01 (cover dated 6 November 2025),
Theorems 1.54 and 1.57, pp.25–26](https://www.jmilne.org/math/CourseNotes/GT.pdf#page=25)
give the finite-cyclic/free decomposition of a finitely generated abelian
group. The complete 1.54 proof and the 1.57 statement and proof of (a)
were inspected; the latter explicitly keeps the condition that p avoid
all finite cyclic orders when identifying M/pM with F_p^r. This is the
relevant torsion qualification, not a justification for ignoring torsion.

[J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition,
GTM 106 (2009), VIII Theorem 6.7, p.239](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=254)
gives finite generation over a number field; its full statement and proof
were inspected. IV Theorem 6.4(b) and Remark 6.5, p.132, give the strict-radius
formal-logarithm isomorphism and torsion-freeness, over a complete normalized
discrete valuation field of characteristic zero, for integer
r>v(p)/(p-1). The proof of (b) uses inverse logarithm/exponential series.
Here Q_7 and r=1 satisfy that strict inequality. The reused reduction
sequence and parameter sources are VII Propositions 2.1–2.2, pp.188–191,
already assessed in
`drafts/literature/2026-10-18-known-point-local-seven-test.md`.
The [author's 13 October 2022 errata](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf),
entries for pp.130–133 and 185–191, retain the previously recorded
convergence and special-fiber qualifications; the strict radius is essential.

## Applicability boundary for the next attempt

L081 supplies the nonzero local image of P. L096 supplies the entire
relation aP+bQ locally modulo seven, and L097 supplies nonzero global
quotient membership of the identical R. These are reused certified
inputs; no finite arithmetic is replayed in this review. The next proof
must use all of them to test linear combinations, not infer two global
directions merely from a nonzero finite strict class.

The inspected range of L083, from “The entire local quotient at every depth” through
the paragraph before “The actual point generates at every depth”
(lines 89–132 in the current file), proves absence of local and hence
rational seven-primary torsion from the order-13 reduction group and the
strict logarithm. That range uses L030/L033 and local theory, before the
global rank/Sha assembly. It is eligible for reuse; L083's full statement
is not an allowed substitute. The next proof must explicitly check that
the finite rational torsion subgroup is seven-divisible and that passing
to its quotient preserves the proposed finite independence test. Then
the torsion-free source criterion may be applied, with rational linear
independence and the change from (P,R) to (P,Q) justified there. These are
listed obligations, not a proof performed during this literature turn.

Independence would supply a rational-rank lower bound, not rank equality
by itself, a published basis replacement with saturation, or an actual
rational point of zero local logarithm. L004's independent analytic and
arithmetic hypotheses remain necessary for its upper-bound application.
Uniform certificate production and comparison with arbitrary complex
analytic order remain outside scope. Full matching Mathlib coverage and
supporting group/formal-group declarations were not checked.

## Search and overlap record

Queries included `elliptic curve rational points independence mod p
saturation torsion finitely generated abelian group`, `"389" "independent"
"0,0" "1,0" elliptic`, `"elliptic" "independent modulo" "torsion"
"reduction"`, and `"abelian group" "independent" "modulo p" "torsion"`.
The last located the precise Datta–Smith lemma; the publisher's original
article, its full lemma proof and the correction were inspected. Milne's
author-hosted text and Silverman's book provide the other primary inputs.
Magma's independence command and Müller's reduction-method lecture notes
were discovery leads only; neither implementation is used as evidence.

L034's already assessed Cremona second-edition Table 2, p.257, row 389A1,
is strictly stronger known fixed-curve coverage. Its precise citation and
model match were inspected locally, without refreshing or invoking its
published basis result. L083's stronger kernel assembly remains excluded.
The L098 audit assessment excludes rationalized upgrades, explaining why
this review was essential. Histories 376/381–384 preserve that distinction.
ATTEMPTS/045 concerns the stopped order-table adaptation and is unchanged;
it is no obstruction to this independent group-theoretic test. No novelty
is inferred from the searches, and no new lemma or script is written.
