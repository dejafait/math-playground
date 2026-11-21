# Newton-contour bound — audit coverage review

TARGET: Assess source and hypothesis coverage for a conceptual audit of L835's Newton-contour relative bound, including similarity orientation, the origin residue and the finite-PF overlap condition.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step673 read L835 in full, the relevant L834/L832 hypotheses and proof passages, step671's primary-source assessment, the earlier exact-projection assessment and step659/667/672 records. Reused their exact interpolation/residue, finite-duality and height/sector coverage; no external search was repeated and no novelty inference is made.
SOURCE_EVIDENCE: Reused inspected statements/proofs: de Boor, Divided Differences, Surveys in Approximation Theory 1 (2005), 46–69, Proposition25/(24)–(26) pp.53–54, Proposition35/Definition37 pp.58–59, Example9/(41)–(42) p.60, (49)–(51) pp.62–63 https://arxiv.org/pdf/math/0502036v1 ; Beck et al., A First Course in Complex Analysis, Section8.1 Theorem8.1.5/full proof https://complexanalysis.org/web/sec_residue-thm.html ; L834/L832's qualified imported inputs as specified below. No new primary passage was inspected in step673.
COMPARISON: The sources cover finite interpolation with analytic function data and residues retaining all isolated singularities. They do not assert L835's inverse, genuine similarity, weighted norm or overlap. These are explicit local claims suitable for a separate conceptual audit; the independent sampled-data norm in de Boor (42) cannot replace the analytic contour argument.
GAP: Coverage is adequate for the audit, but L835 remains unaudited. Its matrix orientation, coupled inverse and contour/norm bookkeeping must be verified; actual M_s/m_1, effective geometry, any enlarged finite-PF cutoff and the strict overlap inequality remain unpaid.
REASON: Approve one bounded audit of the existing standard-method specialization using unchanged ready sources. No essential additional source is required for this audit; this review neither verifies the lemma nor derives or approves a quantitative extension.
LITERATURE_REASON: The saved REVIEW_REQUIRED continuation required a separate comparison of the newly written L835 with the reusable source hypotheses. This turn supplies that comparison without repeating the ready literature search or executing the audit.
SCOPE: Completed literature-only step673. The single COVERED_TARGET is ready for separate next-turn approval; no lemma, script, mathematical identity, enlarged PF theorem or numerical threshold is established here. Actual distinct simple poles, r>=6001 and q<s<1 are retained; no confluent actual packet or growing-shift conclusion is covered.
COVERED_TARGET: Audit L835's Newton-contour relative bound at fixed k=6002, checking the genuine similarity, coupled inverse, origin residue, all norm factors and conditional finite-PF overlap.

## Original proposed scope and continuation inputs — step672

Read the new L835 proof and only the relevant L834/L832 passages. The
essential mathematical input is L834's actual simple packet, separation,
reciprocal coefficient identity and positive leading determinant. L832
supplies the already justified PF6001 range and the qualified statement
of the larger sector cutoff; it does not supply a numerical overlap.
L018/L021/L776 enter through these existing inputs. No cross-notebook
theorem is proposed.

The intended later conceptual audit must check the column reversal,
R^N scaling, Newton coefficient orientation, exact similarity and extra
positive diagonal weighting. It must check that the two factors of
pi'(x_l) in inverse interpolation combine with the residue inverse as
claimed, giving one coupled holomorphic divided difference. It must
retain the origin residue in the outer contour and distinguish the
inner contour, whose numerator has positive power N+1 and no origin
pole. It must inspect the cancellation of |pi(0)|, both circle lengths,
the exponent r+k+1, the row-sum bound and the strict floor-plus-one
onset. It must retain r>=k-1, q<s<1 and the actual simple-pole packet.

The continuation test is whether those exact claims follow from the
reused primary inputs and explicit algebra, with no extra gap assumption,
unpaid sampled-data estimate, omitted singularity or asserted PF
extension. A failure should identify and repair the mathematical error
or downgrade the result. Passing a source review merely makes that
audit ready; it does not verify the lemma or its actual contour values.

Plausible downstream use is a certified contour estimate and eventual
overlap for one fixed-shift ray. The M_s/m_1 bound, effective geometry,
any enlarged finite-PF applicability, all other mixed signs and RH
remain unresolved. This is established-route development and conceptual
checking; no justified creative central mechanism is nominated by a
basis change alone. Mathlib full matching coverage remains unchecked.

## Completed source and hypothesis comparison — step673

The main gap is actual-Xi all-degree mixed positivity, as in
L030–L032/C032a. The intermediate target is the correctness audit of
L835, not another estimate or a proof of overlap. A verified analytic
relative bound could subsequently support a certified contour estimate
connecting one fixed-shift ray to a finite-PF range. Other shifts, other
mixed minors and RH would remain independent gaps.

### Exact source reuse and applicability boundaries

The primary statements and proofs already read in
`2026-11-05-clustered-pole-overlap-scope.md` are adequate at unchanged
hypotheses. De Boor's Proposition25 fixes the polynomial Newton matrix
convention; it is not a holomorphic norm theorem. Proposition35 and
Definition37 require the appropriate Hermite data. Actual L835 uses
distinct nodes and entire function data, so no new actual multiplicity
claim or confluent-pole theorem is requested. Example9/(41) and
(49)–(51) supply the distinct-node sum and disk contour formula.
The latter requires a holomorphic numerator on the relevant disk and
nodes strictly inside an admissible contour. Its applicability to
L835's claimed inverse is an audit obligation, not a result of this
review. Formula(42) instead bounds a functional on arbitrary continuous
sampled values and retains inverse node derivatives. That source cannot
justify a gap-free estimate without the claimed analytic coupling.
The June2005 Corollary30 correction and the earlier unread/ambiguous
display(27) are not used. No general interpolation reproof is needed.

Beck, Marchesi, Pixton and Sabalka, Section8.1 Theorem8.1.5, requires a
simple positively oriented closed contour in a simply connected domain,
with finitely many isolated interior singularities and none on the
contour. Its proof retains every residue. This covers a review of the
outer meromorphic contour; it supplies no permission to apply the
holomorphic divided-difference formula across an origin pole. The audit
must distinguish those two uses and check all singularities. The source
needs no stronger version for the disks claimed in L835.

For the actual packet and sign transfer, reuse audited L834 at fixed
k=6002. Its external inputs remain Platt–Trudgian, arXiv:2004.09765v1,
Theorem1 and Section2 pp.2–3 (including sign-change/count evidence for
simplicity); Böttcher–Widom, arXiv:math/0604009v1, Theorem2.1 p.3,
Corollary2.3 and proof p.4; and Flajolet–Sedgewick's 27 November2003
ALCOMFT-TR-03-100, TheoremIV.7/(22), pp.29–30, both proofs. Versions,
links and qualifications are recorded in
`2026-11-05-fixed-shift-reciprocal-pole-test.md` and canonical L834.
These are inherited audited inputs, not newly imported or reproved here.
L834 supplies the selected simple poles, separating disk, exact real
coefficient identity and positive leading determinant. Its eventual
existence conclusion is not an effective contour bound or onset.

For the finite range reuse L832. Its primary basis is Platt–Trudgian's
closed verified-height statement; Katkova, arXiv:math/0505174v1,
Definition2/(8) p.4, TheoremB p.5 and the genus-zero product/finite-product
passage pp.3,5–6; and Michałowski, arXiv:2607.16795v1, Section1.2's
stated m+1<=pi H condition. L832 retains real products, positive constant,
compact convergence and the ordinary-coefficient normalization.
The original Schoenberg proof remains unread, as already qualified.
Only PF6001 is established locally. An enlarged cutoff requires its
own applicability argument; neither it nor strict finite signs is
needed as a premise of the analytic bound being audited. No larger
cutoff is chosen or derived in this review.

### What the subsequent audit must decide

The proposed specialization is genuinely different from merely invoking
the sources: it claims a particular relative-matrix similarity and all
constants in L835(1)–(4). Check the column reversal, R-scaling, Newton
coefficient orientation, transposes, r-independent invertibility and
positive diagonal weighting as exact finite matrix statements. Check
the inverse interpolation formula using the coupled residue data;
the saved two-node check in step672 is only a diagnostic, not an audit
of the general formula. Check the distinct roles of the positive-power
inner numerator and the outer negative-power coefficient integrand.
Retain the origin residue and every selected pole of the outer contour.

Then check the cancellation of the normalization factor, both contour
lengths, all finite products and the maximum row-sum norm. Verify the
claimed exponent, real determinant sign transfer, strict floor-plus-one
onset and conditional inequality at the first rank beyond PF_m.
These are claims to scrutinize, not calculations performed this turn.
No hypothesis about arbitrary independent nodewise perturbations,
unverified actual contour values or residual positivity is available.

Continuation test: an exact argument from the cited tools and inherited
hypotheses, retaining every constant and singularity, permits quantitative
use of the audited statement. A mismatch in similarity, omitted residue,
hidden inverse pole gap or unjustified PF extension requires correction
or downgrade and preservation of the failure. Passing would not bound
M_s/m_1, choose a larger m or prove the strict overlap threshold.

### Duplicates, failures and routing

Step659's hybrid determinant/cofactor ratio remains unpaid and is not
reopened. Step667's fixed-winding additive error does not supply the
growing-order comparison; its Bultheel and fifteen-shift source access
stops remain preserved and are not essential to this audit. The earlier
de Boor projection-weighting review concerns a different fixed pair;
its general coordinate convention is reusable, its specialized result
is not the target here. L834 already supplies fixed-shift eventual
positivity, so auditing L835 must not be reported as a new eventual-sign
theorem. No numerical sweep or neighboring-shift calculation is covered.

Outcome EXPLORATION records a completed new audit-scope comparison and
actionable source gate, with no mathematical advance or claim beyond
the sources. Next route is proof_audit/conceptual_audit: the subtle
matrix/analytic interface merits scrutiny before quantitative use.
No justified creative central mechanism has been identified; this
standard interpolation audit is an essential prerequisite for using
the existing bound, not a creative attempt selected to meet a quota.
Full matching Mathlib coverage remains unchecked. No cross-notebook
input is used, and no lemma, script, PROOF or DAG is changed.
