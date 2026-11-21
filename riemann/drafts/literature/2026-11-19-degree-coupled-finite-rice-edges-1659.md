# Degree-dependent finite Rice edges — completed source comparison1660

TARGET: Test whether the actual finite Rice rectangle at height h_d=d/log(d) has total absolute top, right and bottom edge contribution at most exp(-d/(log(d))^2) for all sufficiently large integers d, retaining its left segment for J_d(-1)/gamma_0.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1660 searched Rice/Norlund-Rice/Jensen/Mellin uniform-contour terminology and the named local Mellin/Jensen/Rice records; reused source-notes1656 and edge comparison1344/1345. Queries, inspected passages and unread leads are recorded in 2026-11-19-degree-coupled-rice-source-notes-1660.md; no matching three-edge bound was located in the sources inspected and no novelty is inferred.
SOURCE_EVIDENCE: Flajolet--Sedgewick TCS144(1995),101--124, Section2 Lemma1/(6) and kernel identities pp104--105, Section4 Theorem2/both proof cases pp110--111, https://algo.inria.fr/flajolet/Publications/FlSe95.pdf ; NIST DLMF1.2.8 (2026-09-15),5.11.1/5.11(ii) first complex-remainder paragraph,5.11.9--13, https://dlmf.nist.gov/5.11 ,5.5.1/5.5.3 https://dlmf.nist.gov/5.5 ,5.2(i) https://dlmf.nist.gov/5.2 . Reuse audited C048k and C048j rather than their reproof.
COMPARISON: The finite representation and sectorial gamma tools are known; unlike5.11.9 or fixed-shift ratio asymptotics they cover growing real arguments. C048j supplies uniform I/S only. Combining the actual E with the full degree-dependent kernel and integrating all three closing edges is the unproved specialization, not an imported estimate. The fixed-d C048k stop and the distinct L718/Cauchy-circle records do not decide it.
GAP: The proposed A_d<=exp(-d/(log(d))^2) is entirely unproved. A later attempt must control the full horizontal ranges and right edge (including bounded auxiliary gamma arguments), all normalization factors and integration lengths, or give an integrated lower bound contradicting the threshold. Signed margins, x-range and H_d transfer remain independent.
REASON: Essential source coverage is now sufficient for this bounded established-route test. Import the finite Rice and uniform gamma inputs by citation; only their actual joint-limit specialization is authorized for a later REPRODUCTION attempt, following separate approval of this changed assessment.
SCOPE: Integers d>=3 tending to infinity; actual E and B_d of C048k, c=-1/4, h_d=d/log(d), right edge d+1/2; all three closing edges and every corner. A uniform upper bound or rigorous obstruction to the stated integral budget is covered. No new contour, unbounded opening, signed reference, interpolation class or Xi-sign premise is covered; full matching Mathlib coverage unchecked.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified essential missing uniform gamma coverage and duplicate comparison for the changed joint degree/height limit; this turn completes that review without calculating A_d.

## Exact proposed observable

Use precisely the actual E and B_d of C048k, c=-1/4 and
h_d=d/log(d) for integers d>=3. Let R_(d,h_d) be its finite
rectangle with right edge Re(s)=d+1/2 and heights +-h_d. Define

    A_d = (1/(2*pi)) integral over the top, right and bottom edges
                         of |E(s)B_d(s)| |ds|.

The proposed test is A_d<=exp(-d/(log(d))^2) for all sufficiently
large d. This line specifies a desired bound, not an established
asymptotic, a conjectured source theorem or an approved calculation.
The left segment is excluded from A_d and retained exactly in the
finite identity. All corners and all points of the other edges count.
In particular no infinite vertical integral is opened at any fixed d.

The possible downstream use is a controlled finite signed integral
with an explicitly small closing error, against which a separately
proved signed margin could later be compared. A pass would not give
that margin, any extension from x=-1 to a zero-producing x-range,
root counting, C028b's H_d=o(d), C028g's S_F=0, or mixed positivity.
These independent gaps must remain stated. This is an established
contour-method viability test, not a creative central sign mechanism.

## Original review contract1659 (retained; completed below)

The next invocation is literature-only. Preserve the proposed bound
while checking primary finite Rice statements and uniform gamma
asymptotic hypotheses on the exact moving edges. Reuse the inspected
finite residue theorem and C048j's quantitative I/S contract; do not
reprove either. DLMF5.11.9 alone is insufficient because Re(s) is not
bounded on the top, bottom and right edges as d grows. An appropriate
uniform substitute and its remainder/domain must be read before use.

Compare the exact target with the notebook's Rice/Mellin contour
records, including the L718 distinction and the existing Cauchy-circle
route identified in source-notes1656. An overlap must be imported or
specialized, not relabeled. Do not treat old stops as a global ban;
record whether their hypotheses actually cover this joint limit.
No duplicate assessment for this proposed bound was completed1659.

If adequate coverage is obtained, a subsequent mathematical attempt
must bound all three edges, including their entire parameter ranges,
or give a rigorous obstruction to the proposed threshold. A test only
at the left corners, a fixed-real-part Stirling estimate, or a grid
preview is insufficient. An informative lower bound incompatible with
the threshold stops this proposed error budget; it does not disprove
RH or rule out every finite contour. Failure to decide must name the
unpaid uniform estimate without repeatedly increasing d.

Essential local inputs for that later attempt are C048k's exact finite
identity, C048a/C048j's domain and normalization, L828 Section2/L829's
actual E, and L019/L021/C028b's samples. No Bernstein membership,
interpolation uniqueness, unbounded Rice theorem, degree-uniform
signed margin or actual-Xi positivity is assumed. Full matching
Mathlib coverage is unchecked. The source gate was unapproved at
nomination1659.

## Completed review1660

The source ledger is
[source-notes1660](2026-11-19-degree-coupled-rice-source-notes-1660.md).
It records the primary theorem hypotheses, uniform remainder, moving-edge
applicability and exact scope of the comparisons. No bound on A_d, new
asymptotic or lemma was derived in this literature-only turn.

Reuse C048k's already audited finite identity and actual normalization.
Rice Section2 permits the finite contour; Section2/(7) and Theorem2's
polynomial-growth openings do not discard any of its edges here.
Use sectorial Stirling with the complex-remainder statement, retaining
each full gamma argument rather than treating d as a fixed shift.
The original exact product for B_d also remains available. If a reflected
kernel is used, its algebra, signs and any sine factors must be retained
and checked in the subsequent attempt. Bounded auxiliary arguments on
the middle of the right edge require exact/compact control rather than
a large-argument substitution.

This assessment covers only the stated finite-edge test, including a
rigorous negative outcome. No source theorem was found that already
decides its exponential threshold. The exact combination with actual
I/S, uniform optimization over the edges, and integration remain the
mathematical work. Reproving Stirling, the finite residue theorem or
C048j would add no relevant input. No essential source access blocker
remains for this attempt.

Continue if a complete uniform upper bound meets the stated budget;
abandon this proposed budget if a rigorous lower bound on a set of
positive arc length contradicts it. An upper envelope exceeding the
budget establishes only failure of that envelope. An isolated value,
fixed-d tail or grid does not establish either conclusion. If undecided,
record the exact unpaid estimate rather than increasing d repeatedly.
The independent sign and height gaps in the exact observable section
remain. The main proof argument and DAG are unchanged.

The ready SPECIALIZE assessment is newly changed this turn and needs
separate next-turn approval. Thereafter the default is the covered
mathematical attempt, not another generic source search. It is an
established contour specialization. A justified central creative target
is still blocked by the absent signed reference and sufficient
Mellin-to-height implication; this review does not manufacture one.
