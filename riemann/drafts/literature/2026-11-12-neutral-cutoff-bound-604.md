# Quantitative neutral cutoff specialization nomination604

TARGET: Derive an explicit epsilon_N tending to zero for the norm error between C744z(4) and its exact neutral cosine compression extended by identity, retaining actual U and all induced middle products.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed source review603/step604 and its recorded compact-operator, quantitative Galerkin and logarithmic-Laplacian searches; exact local higher-endpoint duplicate/failure screening is recorded in drafts/2026-11-12-high-endpoint-source-review-604.md. This is a new continuation for separate next-turn approval, not mathematics performed in604.
SOURCE_EVIDENCE: Teschl GSM99 version12February2009, direct primary URL https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf ; Theorem1.3(iii) p41, Theorem1.7 pp43-44, Lemma5.5 p128, Theorem6.7 p137 and Lemma6.8/proof pp137-138. Step605 verified access/version and reread projection/Parseval and compactness proof cases. Existing form/inverse coverage of C744z Sections1-3, C744v(5), C744w(8), C999k Section1 and nonmatching DNR/FEM comparisons in the604 source-review note are reused.
COMPARISON: Standard Hilbert projection, Parseval and form calculus cover the method. Qualitative compactness has no explicit cutoff rate. The local difference is a quantified neutral approximation of A0^-1/2 and a complete product/block error bound; prior fixed-profile tails and finite free-coordinate margins do not supply it. No originality is claimed.
GAP: Establish a fully explicit cutoff remainder, including the moment correction, noncommuting projections, both mixed blocks and products crossing the cutoff; no local compactness/rate theorem, finite normalized entry enclosure or sign is currently proved.
REASON: This is a bounded development of an established approximation mechanism using available primary coverage and explicit local diagonal/moment data; it leaves finite signs and independent RH gaps unresolved. A direct theorem import cannot supply the missing effective constants.
SCOPE: ell=log(3)/2; H0=ker(C), H_N=H0 intersect span(e_0,...,e_(N-1)), N>=512; P_N the exact L2 orthogonal projection; Pi_N=P_N direct-sum P_N; S3 exactly C744z(4), E=A0^-1/2, K=P0T|H0,J=P0U|H0,R=EKE,V14=EJE; original qualified c_* and form/core contracts. No symmetry restriction, new floor, finite sign assumption, changed reference operator or cross-notebook input.

Required target: a displayed explicit epsilon_N->0 with

    ||S3-[I+Pi_N(S3-I)Pi_N]|| <= epsilon_N.

This displayed inequality specifies the desired result; it is unproved.
Attempt one analytic bound using the local logarithmic diagonal envelope,
exact low-mode moment correction, and Hilbert best approximation of E.
Then account for every block of S3 and every product crossing the cutoff.
Record all constants and their dependence on the qualified c_*. A generic
O-symbol or compactness assertion alone does not meet the target.

Prove the neutral approximation/domain facts needed; do not commute P_N
with A0 or E. Retain both adjoints and independent complex endpoints.
No need to reproduce Teschl's general theorems. The point of the local
proof is effective constants for these particular projections/operators,
which are absent from the checked source conclusions.

Downstream use would require a certified finite normalized margin gamma_N,
with total norm and finite-entry error below min(1,gamma_N). No such margin
is assumed; C999l/q's unnormalized free-profile margins do not transfer.
Computing/enclosing the exact finite compression still involves the full
E; replacing it by a finite inverse square root needs another justification
and is outside this target. No implementation or sign search is proposed.

Continue if one explicit remainder pays all terms and tends to zero;
report honestly if constants make it useless at accessible cutoffs.
Abandon this attempt if an uncontrolled projection/product term remains
or if it needs S3 positivity; save the exact failed estimate. No fixed
finite map tuning, repeated scalar-tail allowance or RH-equivalent premise.
Main-gap limitations: finite signs, c_*/core/source validation, C744q, H2,
non-neutral directions, higher/global actual-Xi assembly remain open.
Full matching Mathlib coverage is not checked.

## Source-gate repair605

On 12November2026 the direct author PDF above returned the complete
317-page first edition; its title verso identifies 12February2009.
Read Theorem1.3(iii), Theorem1.7 and its proof/best-approximation passage,
and Lemma6.8 with its full proof and following shift counterexample.
The latter requires compact K and strong operator convergence; its
finite-rank reduction is qualitative, and the counterexample cautions
against arbitrary right multiplication. These statements supply no
local cutoff rate. Their application still needs the local hypotheses
and quantitative estimates already specified above.

This completes direct-source approval for the unchanged SPECIALIZE
target, repairing the supervisor's missing-URL report. No new theorem,
rate, sign, or expanded target is approved or proved. The duplicate and
failure comparison in the604 source-review note remains applicable;
no new search is needed for unchanged scope.
