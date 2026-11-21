# Compact signed convolution: nomination1242/review1243

TARGET: Establish or refute that C030v's family obeys D_k(g;t)>0 for 1<=k<=d, where g=f_b+nu*f_b, whenever a real finite signed measure nu is supported on [0,t-s_*], 0<s_*<=t, and integral B_t(u)^2 d|nu|(u)<1, with B_t(u) equal to C030v's bound at (t,t-u).
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1243 reused1238/1239 and1240/1241; searched C030-family proofs and the named finite/global stops for signed smoothing, convolution, inertia and variation; bounded external exact/stronger-result queries are recorded below. No inspected theorem states the complete conjugate-rate TARGET; no novelty claim follows.
SOURCE_EVIDENCE: Read Sra arXiv2611.02944v1 Theorem C.9/(C.18)-(C.20), printed pp27-28, and its shifted-congruence, support-boundary, differentiation, leading-compression and strict-inertia proof on p29; read Higham, Eigenvalue Inequalities for Hermitian Matrices (9 March2021), Courant-Fischer, equation(1), its ensuing norm perturbation bound, Weyl and Cauchy statements. Reuse prior evolution coverage and C030r/v.
COMPARISON: Sra supplies the signed-measure and every-leading-block mechanism for positive real rates; Higham supplies the finite Hermitian perturbation bound. C030r/v supply the assessed conjugate-rate basis/evolution interfaces. A later specialization must assemble these with the exact B_t and interior support; TARGET is not a verbatim source import.
GAP: The conjugate-rate shifted-Hankel estimate, signed differentiation/integration and triangular leading-block application remain to be written and checked. The strict criterion itself is unproved here; actual-Xi representation, weighted payment and all-degree transfer remain independent.
REASON: Essential source scope is now ready for one later source-based specialization on unchanged TARGET, after separate approval of this newly ready assessment. This literature turn proves no new lemma and supplies no mathematical script or counterexample.
SCOPE: Retain C030v's fixed finite rates, positive real parts, m>=1,n>=max(4,2m),2<=d<=floor(n/2),degree inequality,t*A<=1/4,all contrasts,repeats,n=2m and zero phases; s_*>0; nu is real and finite with finite total variation and fixed under differentiation; no s_*=0 or infinite/global assertion.
LITERATURE_REASON: The target changes from coefficient-basis evolution to signed convolution and strict signs of every leading derivative-Hankel determinant. The shifted-Hankel and inertia hypotheses are essential coverage absent from the prior evolution-only assessment.

## Original nomination1242 (historical; reviewed below)

The original pending-review discussion below is preserved as nomination
history. The single-line fields above and completed review1243 below
supersede that pending status; SPECIALIZE concerns source coverage,
not correctness of the proposed criterion.

## Exact proposed test

Use C030v's f_b, C_b, A, M and actual-list q_max with every one of its
restrictions. Fix t>0 and 0<s_*<=t. For 0<=u<=t-s_* define

    B_t(u)=exp(q_max*u/2+(37/4)*M*(t^2-(t-u)^2)).

This is the already proved right side of C030v(1) at s=t-u. Let nu
be a real finite signed Borel measure with support in [0,t-s_*],
independent of the differentiation variable x. Write |nu| for its
total variation. Near x=t define

    g(x)=f_b(x)+integral f_b(x-u) dnu(u),
    D_k(g;t)=(-1)^(k*(k-1)/2)
                    *det[g^(i+j)(t)]_(0<=i,j<k).

The proposed implication is

    integral B_t(u)^2 d|nu|(u)<1
       ==> D_k(g;t)>0 for every 1<=k<=d.

This is a conjectured sufficient test to assess, not a claimed theorem
in this nomination. No derivation, numerical screen or self-approval
is supplied. The strict threshold and positive interior margin s_*
are part of the target, not conclusions to be silently weakened.
Atoms, including an atom at zero, are allowed. At s_*=t the support
is {0}; retain that case. All source theorem conditions and the meaning
of these ordinary derivatives must be verified before an import.

## Relevance and bounded decision

The main gap is still L030-L032/C032a actual-Xi mixed positivity in
every degree. This intermediate test would specify one sufficient
finite signed-remainder budget for the newly audited evolution bound.
It is not an actual-Xi factorization or a proof that its proposed
weighted variation is small. Actual-Xi supply, degree/time choice,
signed-complement payment, theta signing and graph realization remain
unresolved, including the passage from any finite criterion to all
degrees. Useful finite progress does not discharge those interfaces.

The next source review should compare the exact conclusion first with
Sra's C.9 and its signed-smoothing use, retaining the distinction between
positive real reference rates and this conjugate-rate family. Reuse
the already inspected evolution proof; retrieve only the additional
statement and essential proof cases for the changed conclusion. Check
the finite symmetric-matrix perturbation result needed for inertia,
and whether it supplies signs of every leading block rather than
only the inertia of the full matrix. A known matching theorem should
be imported with an applicability check, not rederived as new work.
Check relevant local finite-smoothing duplicates before approving a
specialization. No search failure may be treated as novelty evidence.

Continue if the source comparison provides IMPORT, SPECIALIZE or an
adequate bounded EXPLORE assessment for exactly TARGET. In a later
mathematical turn, success means the full strict criterion with every
listed boundary case; a counterexample must satisfy its strict budget
and all finite-family hypotheses. A failed proof step or an unbounded
support example would not refute this target. If a source adds an
unpaid positivity or uniform inverse-basis hypothesis, record that
mismatch instead of assuming it.

Essential local input is audited C030v together with C030r's signed
coefficient normalization and determinant identities; C030q/t enter
through C030v, with C030u internal to C030t. No new assumption that the
derivative functional is positive is allowed. Preserve unfinished1218,
joint-route parking1232 and scoped stops1117/1181/1193/1200/1107. This
compactly supported finite test does not reopen their automatic global
transfers. Its new ingredient is the verified phase-dependent evolution
budget, not a claim that any of those stops has disappeared.

No justified central creative attempt is nominated: an explicit signed
actual-Xi input remains missing. This is a concrete finite specialization
candidate, not creative work to meet a scheduling target. Full matching
Mathlib coverage is unchecked; no cross-notebook input is proposed.
Recommend literature_comparison, standard/high for this exact changed
scope, followed by mathematics if coverage becomes ready.

## Completed literature-only review1243

17 November2026. The exact TARGET and its hypotheses are unchanged.
No new inequality, determinant sign or counterexample is established
in this review. The result is an adequate source assessment for a
later RESEARCH specialization, not approval of a proof supplied here.

### Primary source statements and essential cases read

S. Sra, *On some positivity properties of the Riemann Xi function*,
2 November2026, [arXiv2611.02944v1](https://arxiv.org/pdf/2611.02944v1),
Theorem C.9/(C.18)-(C.20), printed pp27-28, proof p29.
Here the source's dimension m is our d, not our conjugate-pair count.
C.9 assumes positive real rates bounded by Q, permits repeats, and
retains exactly our degree inequality. It gives a lower triangular
normalization and a shifted-Hankel norm bound exp(Q*u). Weighted
variation strictly below one yields differential determinant signs
at every leading size. The proof explicitly treats leading
compressions and their triangular congruences, differentiation against
total variation, and the zero-extended support boundary. Its later
PF closure is outside TARGET. The source is not a conjugate-rate
theorem. Reuse1238/1239 for the unchanged real evolution proof.

N. J. Higham,
[*Eigenvalue Inequalities for Hermitian Matrices*, 9 March2021](https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/),
is the inspected author exposition of the standard finite matrix
input. The Courant--Fischer statement and equation(1) give, for
Hermitian matrices U,V of the same size with eigenvalues ordered
nonincreasingly,

    max_j |lambda_j(U+V)-lambda_j(U)| <= ||V||_2.

Read also the named Weyl inequalities and Cauchy interlace theorem.
This is an additive Hermitian eigenvalue bound, with no positive
definiteness premise on U and no simplicity requirement. Sra's
explicit leading-compression argument, rather than a claim about
the full matrix alone, is the appropriate model for the later proof.
Neither source is being independently reproved. No matrix exponential
or noncommuting evolution calculation is needed in this new step:
C030v has already supplied that interface.

### Exact comparison and permitted specialization

The real-reference coverage is adequate but does not import the full
target. Actual rates with b_l nonzero fall outside C.9's real-rate
hypothesis. C030r supplies the real signed normalization for precisely
this changed finite family, and C030v supplies its phase-dependent
propagator budget. Both are audited local inputs. Reuse them without
rederiving their orbital, subdiagonal or evolution proofs.

The later task is to apply the cited perturbation mechanism with the
saved B_t, rather than establish a new matrix perturbation principle.
It must justify the shifted-Hankel estimate in this basis, integrate
against the fixed real signed measure, and check that the leading
compressions correspond to the requested ordinary derivative blocks.
These are proof obligations, not derived conclusions of this review.
No extra assumption that L_x is positive, or that all full-matrix
inertia data determine leading determinant signs, is authorized.

Interior support and C030r's analytic finite convolution supply the
right regularity interface for a compact-domination check. The next
proof must actually give a common neighborhood of t, derivative
bounds through order 2d-2 against |nu|, and explain why no derivative
of nu occurs. It may use the standard dominated convergence theorem.
It need not prove a zero-boundary or infinite-support extension. This
is a local ordinary-derivative criterion, with no PF closure claimed.

Retain strict integral B_t^2 d|nu|<1, all 1<=k<=d including k=1,
atoms at zero and at t-s_*, s_*=t, nu=0, M=0, repeated rates,
n=2m, arbitrary real contrasts and t*A=1/4. There is no positivity
or unit-total-mass assumption on nu or delta_0+nu. Do not replace
the measure by a moving truncation during differentiation. No bound
at s_*=0, threshold equality or larger phase window is preapproved.

The exact local input for the attempt is C030v and C030r; C030q/t
and C030u enter only through their already audited interfaces. No
pending C030s input, real-functional variance inequality or uniform
inverse-basis assumption is added. Full matching Mathlib coverage is
unchecked; no absence claim or cross-notebook input is made.

### Searches, duplicates and recorded failures

Scoped local queries used signed smoothing, signed convolution,
inertia, total variation and moving frame in C030-family lemmas,
the finite-basis assessments1238/1240, and relevant November17
working notes. Read C030r's full hypotheses/conclusions and its
analyticity/real-normalization proof ranges, C030v's complete bound
and evolution proof, and C030l's source-scope paragraph. C030l records
the real C.9 statement only; C030r expressly excludes smoothing, and
C030v expressly excludes the signed/global conclusion. No completed
duplicate of the exact new criterion was found in these paths.
This is a bounded comparison, not a notebook-wide originality claim.

Read the short ATTEMPTS records1117/1181/1193/1200/1107 and1232.
Their automatic finite-to-global, class, degree/time, propagation,
graph-transfer and unpaid joint-moment stops remain scoped. None
provides a counterexample satisfying this finite compact criterion.
No stop is removed and no actual-Xi supply is inferred from this review.

External queries included:

- `"signed smoothing" "Sra"`
- `"signed convolution" "Hankel" inertia`
- `"Sra" "C.9" convolution positivity`
- `symmetric matrix inertia perturbation spectral norm minimum absolute eigenvalue Weyl Higham`
- `"moving-frame signed smoothing" conjugate rates`
- `"Hankel" "signed smoothing" "measure"`
- `"conjugate" "Hankel" "weighted variation"`

The inspected sources are the primary arXiv paper and Higham's author
article above. Search hits on separated-rate total positivity,
reshaped-Hankel sign consistency and unrelated Hankel transforms are
uninspected leads, not theorem evidence or reasons to assert novelty.
The older Söderlind access issue recorded in1239 is nonessential:
no new evolution source is required. No essential source blocker remains.

### Bounded next attempt and routing

Keep the exact TARGET and NEXT_REVIEW unchanged. After the supervisor's
separate approval of this newly ready assessment, attempt only that
finite specialization. Success is a full proof of its strict criterion
covering every leading size and boundary case above. Refutation requires
an admissible family and measure meeting the strict budget; a failed
derivation or an unbounded-support example does not refute TARGET.
An unpaid additional premise must be reported as a remaining gap.

Downstream use remains a sufficient finite signed-remainder budget.
Actual-Xi representation, degree/time choice, payment of this budget,
global complement, theta signing, graph realization and all-degree
positivity remain unresolved. The central creative-route blocker is
still the absence of a specific signed actual-Xi input; this routine
source specialization is not relabeled creative to satisfy a schedule.
Recommend proof_attempt/development, deep_research/xhigh, for the
signed analytic assembly and all-leading-block checks. The completed
turn is literature_comparison with no mathematical exploration usage.
