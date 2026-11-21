# Variable-share allocation: four-demand necessary-cut discriminator

TARGET: Determine whether any Hall cut for the four negative lobes centered at ±pi/16 and ±3pi/16 fails at x=16,y=0 in L898's full marginal, retaining all allowed neighboring positive resources and complete theta/spatial errors.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step136's completed variable-share/weighted-Hall/Strassen comparison in 2026-11-08-lobe-dependent-resource-allocation-review.md, including its scoped duplicates and recorded failures. No inspected theorem signs these actual-theta cuts; no originality claim.
SOURCE_EVIDENCE: Koperberg https://arxiv.org/pdf/2202.02092v1 Theorem1 p2, Proposition4/proof pp5–6 and Lemma3 cases pp3–4; Barthe et al. https://lmcs.episciences.org/5989/pdf Theorems3.7/3.11/3.12 and main cut/flow proof pp18:7–9, Definitions2.1/3.2/3.8–3.10; Sokolova–Woracek https://drops.dagstuhl.de/storage/00lipics/lipics-vol211-calco2021/LIPIcs.CALCO.2021.23/LIPIcs.CALCO.2021.23.pdf Theorem2 p23:3 and Theorem15 pp23:12,14–15 qualify the infinite algorithm. Precise hypotheses and inspected proof cases are recorded in the completed comparison; reuse Johansson's finite-box method from step133/134.
COMPARISON: Exact weighted coupling/capacitated flow is known. Applying its necessary cuts to these four actual demands changes L904's fixed-half-share test. No amount from a nonadjacent positive lobe is allowed. A finite failure can reject the whole rule; passing all selected cuts cannot certify the infinitely many other demands.
GAP: Actual cut values, capacity specialization, localization of permitted resources and complete new-domain quadrature errors are unproved. Infinite feasibility, a signed global residual, nonzero heights and higher mixed signs remain open.
REASON: Specialize the inspected known resource theorem and existing rigorous quadrature method to one finite, independently falsifiable allocation test; do not reprove general Hall theory or use total-transform positivity.
SCOPE: Exactly x=16,y=0, four specified negative demands and their five complete positive neighbors, all 15 nonempty demand subsets. No frequency sweep, larger-prefix campaign, global-flow claim or infinite-tail signing is covered.
COVERED_TARGET: Determine whether any Hall cut for the four negative lobes centered at ±pi/16 and ±3pi/16 fails at x=16,y=0 in L898's full marginal, retaining all allowed neighboring positive resources and complete theta/spatial errors.

This assessment was first written in step136 and requires separate approval
next turn. No quantity below was evaluated, no specialization proved and no
mathematical script written in that literature-only step. General theorem
coverage is ready; this is a proposed mathematical application, not a result.

Use L898's full probability marginal mu of q=u-v under W_0/A_0(0).
Let a=pi/16. For integers k define the *proposed* resource and demand data
by their complete signed integrals:

    P_k=[(2k-1/2)a,(2k+1/2)a],
    N_k=[(2k+1/2)a,(2k+3/2)a],
    r_k=integral_{P_k} cos(16q) dmu(q),
    d_k=-integral_{N_k} cos(16q) dmu(q).

Select F={-2,-1,0,1}. For nonempty S subset F, define its permitted
neighbor set T(S)=union_{k in S}{k,k+1} and the proposed cut budget

    H(S)=sum_{j in T(S)} r_j - sum_{k in S} d_k.

The test is whether some H(S)<0. These are definitions for future work,
not an established application or derived criterion in this assessment.
The union convention forbids counting shared resources twice. Retain the
whole central lobe and both sides of q=0. All selected neighboring
resources are in P_-2,...,P_2. Cosine vanishes at the lobe boundaries;
endpoints and irrational pi uncertainty still require explicit handling.

First justify the capacitated resource model and the necessary-cut
implication from the inspected theorem; distinguish demand equality from
resource upper capacity. Conservation of positive mass means no resource
can be reused: any unused resource must remain a nonnegative surplus,
not be erased from a proposed global identity. Do not normalize positive
and negative totals separately. General Hall theory should be cited;
only its local applicability and new integration domain need proof.
If stating the infinite criterion, verify the countable layered-network
hypotheses and retain all cuts without claiming that this finite test
verifies them. Do not introduce an unknown signed surplus as a premise.

The key residual obligation for a *negative cut certificate* is to prove
that no positive lobe outside T(S) can supply these demands under the
nearest-neighbor rule. Thus a finite obstruction, if found, cannot be
rescued by an omitted infinite resource. This is not permission to assume
any sign for the remaining transform. A passing test leaves every other
negative demand and the complete signed infinite residual unpaid. That
limitation is part of the result, not an error term to suppress.

Evaluate this single finite collection with certified bounds. Reuse L898's
absolute domination and, if used, L904's density normalization/change of
variables after checking them, together with L312's theta/spatial envelopes
and L037's explicit arithmetic contracts. L904's old singleton certificate
cannot cover the larger q domain automatically. Prove complete omitted
bounds for every included lobe; keep all theta indices and both transverse
spatial directions. Retain Jacobians, reflected-kernel seams, irrational
endpoints and all resource multiplicities. Johansson's already assessed
whole-box inclusion is sufficient in principle; no new analytic quadrature
or infinite-flow algorithm is proposed. Reflection may reduce computation
only after an exact accounting proof.

A certified upper bound H(S)<0 for any one subset stops universal
nearest-neighbor variable sharing. A nonnegative lower bound for every
selected H(S) only means that this finite batch has no obstruction;
record that as such. Zero-containing intervals are inconclusive. Stop
once this bounded question is decided or its declared error budget is
exhausted. No larger block, mesh campaign beyond completing the stated
error budget, or height/frequency sweep follows automatically.

Save complete certificate values, actual/required bounds, error sources,
failures, reproduction command and implementation assumptions. Use bounded
JSON inspection and inspect complete load-bearing fields. Do not use
L313's known total sign, an RH-equivalent criterion or L904's negative
fixed-share value as an input to sign H(S). L904 motivates the changed
allocation only and remains unaudited. No new general resource theorem,
positive-definiteness theorem or all-degree Xi consequence is sought.

Essential local inputs: L898 and its L019/L020 interfaces; L312/L037 for
certified envelopes/arithmetic if used. L904 is a reusable construction
only after verification, not an essential sign premise. The inspected
primary resource theorems supply known methods, so reproduction or local
specialization is the appropriate description; no certified originality
is claimed. Supporting/full Mathlib coverage is unchecked, not absent.
No cross-notebook input is proposed.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
A finite obstruction would eliminate an entire flexible allocation rule;
a surviving finite block could guide later compensation work, but supplies
no complete signed margin. Independent residual control and higher mixed
forms remain open. This is ordinary calculation/theorem application, not
creative central-gap work. A new central mechanism still needs an
independently supported signed remainder before creative escalation.
