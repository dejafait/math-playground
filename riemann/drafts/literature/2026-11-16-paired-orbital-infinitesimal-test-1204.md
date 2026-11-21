# Two-real-level infinitesimal orbital response — continuation1204

TARGET: Attempt the two-real-level infinitesimal phase-response test: determine whether |lim_(b->0) E_(k,b)(x)/(x*b^2)| has an absolute bound for D_b=diag(a+i*b,a-i*b,r,...,r), finite n>=2, 0<=k<n and a,r,x>0, justifying the local positive branch and separate normalizers; seek an explicit uniform bound or a rigorous unbounded family.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed review1204 searched the exact one-pair defect, stronger complex HCIZ/zero-free/logarithmic-derivative statements and finite-complex-spectrum obstructions; no matching dimension/rate-uniform adjacent-rank response theorem was found. Scoped local duplicate/stop comparison and query record are in drafts/working/2026-11-16-paired-orbital-source-review-1204.md; no novelty inference from failed searches.
SOURCE_EVIDENCE: Reuse completed review1204; primary URLs: McSwiggen arXiv1712.03995v4 https://arxiv.org/pdf/1712.03995v4 Theorem1 p4/(2) p2/continuation p10; Novak arXiv2203.10746v1 https://arxiv.org/pdf/2203.10746v1 Theorem1.2 p6/domain pp2-3/Theorem4.7 p34; GGN2014 https://www.numdam.org/article/AMBP_2014__21_1_71_0.pdf Theorem5.1 pp84-86/Section5.2 pp86-87; corrected Guionnet--Maida https://perso.ens-lyon.fr/aguionne/rgfend.pdf Theorem4 p5/Hypothesis1.1. C030l and assessment1202 cover only the real-rate reference.
COMPARISON: Known complex identities and bounded-field small-coupling asymptotics do not directly imply this unnormalized adjacent-rank response under unrestricted real contrast. General imaginary-zero examples do not refute this paired/projection local diagnostic. No matching coefficient estimate was located; this is a bounded investigation without an originality claim.
GAP: Existence and uniform size of the b^2 response with independent rank normalizers are unproved. Even a uniform answer here leaves finite-b response, arbitrary real background spectra, the whole positive-branch window, pair summation and actual-Xi scale/all-degree transfer unresolved.
REASON: This diagnostic tests the first nontrivial phase response after positive corner-law comparison fails. A uniform bound would keep a signed-reference mechanism viable; an unbounded family would reject its proposed universal full bound. Source-link recovery1205 approves this exact bounded target for a later mathematical attempt; no mathematics has been performed in this assessment.
SCOPE: One finite conjugate pair with common real part a; all other rates equal r>0; normalized Haar on U(n); x>0; local b->0 response only, retaining b=0, n=2, repeated rates and k=0,n-1. Does not cover finite-b inequalities, arbitrary remaining rates or actual Xi.

## Exact proposed test, not an established formula

Use the definitions already fixed by nomination1203. For every j=0,...,n,

    Z_(j,b)(x)=integral exp(-x tr(D_b V P_j V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_(k,b)(x)=(G_(k+1,b)-G_(k,b))
                  -(G_(k+1,0)-G_(k,0)).

The proposed diagnostic is the existence and uniform absolute boundedness
of the limit in TARGET. No expression for it is asserted in this file.
Justify differentiation/limits and the positive local branch for each
finite set of parameters. Do not silently replace separate normalizers
by one tilted law or assume a dimension-uniform radius from fixed-n
analyticity. The finite-b condition x|b|<=1/4 from1203 is compatible with
the diagnostic but does not make its uniform estimate an established input.

Use Haar integration and the cited standard orbital identities as needed;
do not reprove general HCIZ/corner theory. If a confluent determinant
formula is used, its repeated eigenvalues must be handled by justified
limits. A Taylor coefficient identity alone or a finite numerical sample
does not establish the requested supremum bound. Meaningful computation
may guide the attempt, with complete certificates saved under scripts/;
a rigorous violating parameter family is required for a mathematical stop.

One coherent attempt: obtain the exact response with all hypotheses,
and pursue either a uniform constant or an unbounded family. If neither
is completed, preserve the formula/obstruction and identify a genuinely
discriminating remaining estimate; report EXPLORATION honestly. Do not
expand to independent mechanisms or claim a sign from absolute values.

## Relevance, test and independent gaps

Main gap: L030-L032/C032a actual-Xi Q(q)>=0 in every polynomial degree.
Plausible use: control a signed conjugate-pair perturbation of the finite
real-rate reference used near source (C.17). The diagnostic is only a
necessary small-phase test of the stronger1203 proposal. Its negative
answer would abandon that universal bound, not RH or every signed route.
Its positive answer would retain only this restricted response mechanism;
it would not pay nonlinear phase errors, arbitrary spectra, summation,
growing finite cores, actual-Xi degree/time scales or graph realization.

Essential inputs: C030l; Sra author v3 C.6-C.9 pp23-29 for scope;
the precise source comparison1204. Stops1117/1181/1193/1200/1107 and
finite-core overlap884 retain their recorded limitations. They are
context, not premises of an unproved phase bound. No cross-notebook input.
Source-link recovery1205 completes the separate literature approval; a
later research turn may attempt only this exact assessed target. Full matching Mathlib coverage is unchecked.

Proposed route: proof_attempt/creative, deep_research/max. The obstruction
is the loss of positive orbital order under conjugate rates at a possible
signed-reference input to all-degree Xi positivity. The bounded test is
this exact second-order supremum in a two-real-level family; an explicit
uniform bound or a rigorous unbounded family is the decisive evidence.
This is a new phase-response mechanism, not another real scalar audit,
finite-PF enlargement or relabeling of a stopped transfer.


## Source-link recovery and separate approval1205 (2026-11-16)

The supervisor reported a missing direct source URL in this ready
assessment. Added primary URLs directly to SOURCE_EVIDENCE, preserving
TARGET, EXPLORE and the exact finite-n/two-real-level scope. Reused the
completed comparison in assessment1203 and its working record1204,
including their duplicate and failure checks; no new discovery search
was needed. Reopened McSwiggen1712.03995v4 (2), p2, and Novak2203.10746v1
(1.2), p2, and Theorem4.7's nonvanishing reduction, p34, through the
primary PDF URLs. Other detailed theorem coverage is reused from1204,
not claimed as newly read. This is source traceability repair and
separate approval, not a new mathematical finding or a new source
comparison outcome.

The restricted domain and normalization comparison remains exactly the
one recorded in assessment1203: complex orbital identities do not
provide an adjacent-rank inequality; the inspected nonvanishing theorem
requires bounded spectral parameters and small coupling, whereas this
target allows unrestricted real contrast. No stronger theorem is
imported. Repeated projection eigenvalues, local positive branch, both
normalizers and all endpoint ranks remain obligations of the later
attempt. The full matching Mathlib theorem remains unchecked.

Decision: ready EXPLORE coverage for the unchanged TARGET. A rigorous
uniform response bound or an unbounded family is still required; no
response formula, inequality, counterexample or source-proof audit was
produced. No new lemma or mathematical script was written.
