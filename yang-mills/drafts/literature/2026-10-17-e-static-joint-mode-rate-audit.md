# L223 static-replacement rate — audit source scope

TARGET: Critically audit L223's O(N^(5/2)) full-prefix static-replacement bound for both actual probes, including the Abel endpoint term, joint spectral count and complete heat-summed signed pairing.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the unchanged quantitative-rate assessment's bounded external searches and theorem comparison; searched L101/L097's precise spectral, coefficient and heat statements, L223, its attempt draft, histories 286–287 and ATTEMPTS/024–025/030/045 for scope changes, duplicates and stopped shortcuts. No new broad search was needed for this audit.
SOURCE_EVIDENCE: Reinspected Dowker arXiv:1207.2096v2, section 7, printed pp. 10–11, (29)–(31), including both endpoint conditions and the normalized modes; read L101 hypotheses and proof sections 1–2, L097(9)–(13), L065 hypotheses and scalar-form statement, L008's exact probes and heat bounds, and L028's scope and lifted-column qualifications.
COMPARISON: The inspected primary source covers the axial scalar diagonalization; L101 supplies the cochain multiplier and exact pairing, coefficient variation and heat envelope. It supplies only the earlier O(N^(27/10)) error. No matching full-probe O(N^(5/2)) theorem was established in the reused search; L223's stronger claim requires its own critical audit.
GAP: Check L223's finite Abel row estimate, N input-block count, joint co-closed trace identification, exterior-circulation errors and complete signed heat sum against the imported hypotheses; the static trace's continuum rate is outside this audit.
REASON: The new audit target stays within the earlier assessed fixed-box spectrum and deterministic coefficient scope, uses no additional essential external theorem, and is ready for one separate mathematical audit. Source-scope approval does not certify L223.
LITERATURE_REASON: Mandatory separate approval of the newly proposed L223 audit continuation; compare its actual Abel/joint-mode proof scope with the already inspected inputs rather than repeat discovery for the ready rate target.
SCOPE: Fixed-box SU(2), straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, both actual probes i=3,6, every axial increment and transverse end row, allowed constant coordinate modes, upper prefix endpoint and complete exterior heat sum; audit L223 only, relative to its imported inputs.

Essential inputs: L008 L028 L065 L097 L101 L223. L101's exact
L085/L088/L091/L092 contraction and covariance identities remain
imported through L101; no upstream re-audit is silently claimed.
The earlier [rate assessment](2026-10-17-e-static-replacement-quantitative-rate.md)
remains unchanged. Its inspected Chung–Yau and Adams–Lee comparisons
are reused as recorded there; neither is an additional theorem needed
by L223's displayed proof. Unread leads in that assessment have not
been promoted to inputs. No essential source blocker is identified.

This separate literature turn changes the proposed REVIEW_REQUIRED
scope to EXPLORE for the exact TARGET. It establishes readiness to
audit, not the rate, its correctness or originality. The earlier
completed research and its pending audit status are preserved. No
lemma, mathematical script, PROOF.md or DAG.md is changed here.

## Primary source and applicability boundary

J. S. Dowker, [*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, section 7, printed pp. 10–11: (29) places
Dirichlet endpoints at 0,p with p-1 interior vertices; (30) and
the following normalized sine modes give the spectrum used in (31).
Setting p=N matches L101's axial L_D in dimensionless stored
coordinates. This covers the scalar input to L223, including its
normalization. It does not prescribe boundary conditions on every
gauge component or estimate a variable-coefficient prefix trace.
The auxiliary display (32), excluded by the earlier assessment,
is still unused. No kernel reproof or image estimate is needed.

L101 section 2 is the local source for transporting this scalar
spectrum to curvature modes using the co-closed partial isometry,
and for its null curvature complement. Its exact spectral comparison
is imported; a scalar source alone cannot justify that identification.
The audit must check that L223 uses this same domain and range.

## Load-bearing coverage map for the later audit

| Item to audit | Existing coverage and qualification |
| --- | --- |
| Scalar sine normalization and partial sums in L223(3) | Dowker (30)–(31) supplies the normalized basis. The finite geometric sum is elementary algebra to verify in the audit, not a new spectral theorem. |
| Abel row and N increment blocks in (4)–(7) | L101 defines B on all N increments and gives neighboring-level operator bounds in (8). Finite Abel summation is a standard named identity; its actual endpoint and operator-row application remain audit questions. |
| Deterministic coefficient regularity | L097(9) explicitly includes levels N-2,N-1. L028's smooth pre-retraction fields do not supply smoothness of the forest potential across the upper pin; L223 may use only the stated existing-level bounds. |
| Joint spectral identification and trace in (8)–(9) | L101(9) supplies the co-closed/curvature correspondence and vanishing complement; L101 section 1 and L097(10) import the full relative inverse trace. The audit must check multiplicities, positive joint energies and allowed constant coordinate modes. No new scalar boundary condition is authorized. |
| Exterior-circulation errors and signed residual pairing | L101(6)–(10) keeps both F_k terms; L065(1) bounds the scalar residual form with every axial input. Neither positivity nor level diagonality of the residual is available. |
| Both probes and complete heat sum | L008(2) fixes the triplet average of squares and the clover shear; its (15)–(18) gives the full heat framework. L101(8) is the precise polynomial envelope used by L223. Check that the audit's modal estimates fit that unchanged envelope. |
| Identification of the finite static expression | L101 section 2, following (12), identifies the complete symmetric heat pairing with its (3). Its cumulative insertion, including the moving-cut endpoint, is imported unchanged, not replaced by a local layer. |

This map locates the necessary inputs without checking the new
inequalities or deriving their consequence. Verification of those
inequalities is the saved mathematical task. No extra endpoint
smoothness, residual commutation or quantitative continuum limit has
been added to its assumptions. Mathlib coverage for the matching
actual-probe theorem and supporting summation/trace results remains
not checked; unknown coverage is not absence.

## Duplicates, failures and decision test

Histories 286–287 and the existing attempt draft identify L223 as
the completed local rate proof; no separate audit is recorded there.
The earlier external comparison did not establish a matching theorem,
which is neither a novelty finding nor a reason to reprove the scalar
spectrum. L097/L101's coarse split is already documented and weaker;
this audit must inspect the actual joint-mode argument.

ATTEMPTS/024 retains a genuine upper Dirichlet correction for another
trace, and 025 stops an axial-profile/absolute-norm gain there. Neither
refutes an error after subtracting L101's exact static expression.
ATTEMPTS/030 stops using a fixed-mass limit at varying mass; L223's
finite spectral argument makes no such invocation. ATTEMPTS/045
stops treating a rough projection-side prefix as uniformly smooth;
it is not a ban on variation estimates for the deterministic Zeta
already stated in L101. Preserve these obstructions and check their
distinctions during the audit rather than infer correctness from them.

The later audit must check the N increment blocks in L223(4)–(7), the
nonzero upper term in Abel summation, normalization of the axial
sines, the curvature/co-closed spectral identification in (8)–(9),
the full trace bound including relative end rows and constant allowed
coordinate modes, both exterior-circulation terms, and the unchanged
polynomial heat envelope. Continue only if all of these close at
O(N^(5/2)); retain a specific failed step if they do not. Do not
infer a rate for the static expression's continuum limit or for any
other response component. L220's separate audit, the interacting
reflected bound <=c_box/2, continuum axioms and finite positive mass
remain unresolved. No cross-notebook input is used.

Downstream use: a validated component rate could support a later
complete quantitative perturbative remainder; it does not itself
bound that remainder. Mathematical exploration usage remains zero;
this is a source-scope review only. Next work defaults to the exact
mathematical audit above, with no further literature turn needed
unless an essential new hypothesis or source is actually identified.
