# Coverage for critical review of the fixed-point specialization

TARGET: Audit L959's fixed-point terminal splitting, checking the s-to-w orientation, all finite-order root counts, common-zero divisor and absence of an independent signed term.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact local-completion target search and known-obstruction comparison saved in 2026-11-10-xi-completion-terminal-splitting-128.md; the audit introduces no different family or hypotheses. The scoped step129 duplicate check found no earlier completed terminal branch allocation in the relevant L95x files and completion-index records.
SOURCE_EVIDENCE: Step130 directly checked Gantumur2015 Theorem15 p8 with its complete homotopy proof, Theorem18 p8 and Section5 p9 local multiplicity argument; reused L018 completion and L958 published Kim citation/critical-multiplicity conventions. L959 is the object of the future audit, not an imported theorem.
COMPARISON: Standard Rouche and Taylor factorization cover the local tools; the audit must independently check the actual coordinate sign, exhaustive multiplicity counts and parity comparison rather than invoke a new theorem or claim novelty.
GAP: L959 is complete as an informal local proof but has not had a separate critical audit. Its explicit Re(H'/H)>0 hypothesis, point-dependent scales, retained boundary factors and absence of global consequences must survive review.
REASON: Source coverage is sufficient for this bounded audit; approval does not certify L959. Its orientation and common-divisor conventions must still be independently checked before using the local stop.
LITERATURE_REASON: The supervisor explicitly requires separate approval of the continuation saved during step129; this turn completes that gate without reopening an unchanged mathematical target or source search.
SCOPE: Audit only L959 with L018 and L958; no endpoint analysis, large-height removal of the sign hypothesis, uniform perturbation limit, global sum, K bound or new lemma is approved by this assessment.

## Reused source scope

The source content and inspected cases are recorded in the saved
[pre-step assessment](2026-11-10-xi-completion-terminal-splitting-128.md).
Gantumur, *Isolated singularities and meromorphic functions*,
16 April 2015, [Theorem15 p8 and Section5 p9](https://www.math.mcgill.ca/gantumur/math249w15/residue.pdf)
counts full orders on small circles where the strict boundary
inequality is verified. It does not itself assign sides of the
critical line. Kim's critical multiplicity is imported in L958 with
its precise published citation; common roots are excluded from K
and retained in original counts. The review must check that L959
retains these conventions without using any global count theorem.
No new literature search or unread lead is essential to this audit.

## Bounded audit and decision

Check the exact identity i H G_(1-epsilon)=F'-i epsilon h F and
Re(s)<1/2 iff Im(w)>0. Verify both the fixed-disk total count and
all scaled root disks, including m=1 and both odd-order signs.
Check that the common factor has order r-1, its quotient stays
nonzero, and no boundary branch is assigned a noncommon weight.
If these checks pass, accept the fixed-point identity and its local
mechanism stop only. A countercase or omitted branch requires a
specific correction; no generic-transversality replacement is allowed.

This continuation was saved during research step129. Separate source
approval was completed in literature step130 on 10 November 2026.
The next turn may perform exactly the stated audit without another
literature approval. No new mathematics or proof certification was
performed here. Full matching Mathlib coverage remains unknown; no
cross-notebook input is involved.


## Separate source approval — step130

Directly inspected the author PDF dated 16 April 2015, Theorem15 and
its entire homotopy proof (p8), Theorem18 including its disk proof
(p8), and the complete opening local-multiplicity argument of Section5
(p9). The strict contour inequality preserves the full weighted order;
the holomorphic circle case is sufficient. The local mapping paragraph
treats constant shifts, not the variable completion perturbation. Thus
the future audit must check each actual boundary estimate; it cannot
import simplicity or half-plane allocation from that paragraph.

The theorem comparison requires no further general root-branch theorem.
L018 supplies the actual completion and real coordinate, and L958
supplies the precise weight to compare; no re-import of Kim's global
theorem is needed for a fixed-point audit. The relevant step128
assessment and step129 failure record contain the existing overlap and
local route stop. Reuse them unchanged. The Re(H'/H)>0 hypothesis is
retained, so digamma estimates and an effective onset are not essential
coverage for this target. This is coverage approval only: all parity,
orientation, exhaustiveness and persistent-divisor checks remain for
the next mathematical turn. No independent signed datum or RH progress
is established by this source review.
