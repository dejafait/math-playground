# Finite conjugate-rate basis evolution: nomination1238/review1239

TARGET: Establish or refute ||C_b(t)C_b(s)^(-1)||_2<=exp(q_max*(t-s)/2+C*M*(t^2-s^2)) with an absolute C, for C030r's fixed conjugate-rate family, 0<s<=t, t*A<=1/4 and (n-2*d+1)/2>=sqrt((d-1)*(n-d+1)), where q_max=max_j Re(q_j).
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1239 reused1228/1229,1232/1233,1236/1237; searched the paired finite-basis assessments/working notes and C030q-u for evolution duplicates, retained stops1117/1181/1193/1200/1107, and performed the bounded exact/stronger-result search recorded below. No inspected source states TARGET for the conjugate-rate family; no novelty claim follows.
SOURCE_EVIDENCE: Refreshed Sra arXiv2611.02944v1 C.8/(C.15)-(C.17), printed pp26-27, and C.9/(C.18)-(C.23) with its right-evolution energy/Gronwall proof and support-boundary case, pp27-29; read Higham, What Is the Logarithmic Norm? (18 January2022), Lemma2, Theorems3 and6 with their displayed proofs. C030q/r/t/u supply the audited finite local interface; scope and access qualifications below.
COMPARISON: Sra covers the zero-phase reference under exactly the retained degree condition; Higham covers norm perturbation of finite matrices, while Sra supplies a nonautonomous energy argument. These known inputs authorize only the identified conjugate-rate specialization, not an import of TARGET or of global signed smoothing.
GAP: The remaining mathematical work is a dimension-independent passage from the audited diagonal/subdiagonal differences to the actual nonautonomous propagator, with the correct factor order and time integral. No absolute C or counterexample is established in this literature turn.
REASON: Essential changed norm/evolution coverage is complete for one bounded specialization attempt on the unchanged TARGET, after separate approval of this newly ready assessment. No new lemma, calculation, mathematical script or proof of TARGET is supplied here.
SCOPE: Finite m>=1,n>=max(4,2m),2<=d<=floor(n/2); fixed a_l,r>0 and real b_l; A=sum_l|b_l|,M=sum_l b_l^2; C_b is exactly C030r's real signed-orthogonal coefficient matrix, and ||.||_2 is the Euclidean operator norm. Retain the displayed additional degree condition, repeated rates, zero phases, n=2m, all real contrasts, s=t and the closed phase boundary. q_max ranges over the actual n rates, so r is omitted if n=2m.
LITERATURE_REASON: This is a new finite-evolution target with a restricted degree range and an exact time-dependent norm conclusion; prior ready coverage concerns coefficient comparisons only. Reuse the existing orbital and determinant assessments, and inspect only the additional essential evolution hypotheses and proof cases.

## Original nomination1238 (historical; reviewed below)

The main gap remains L030-L032/C032a actual-Xi Q>=0 in every degree.
C030r identifies the finite moving basis. C030q and now audited C030t
control its diagonal and subdiagonal phase responses. The displayed
estimate is proposed as their concrete downstream use: a finite shift
budget with phase cost controlled independently of the dimension and
real-rate contrasts. No bound for that evolution is derived in this
nomination. In particular a coefficient estimate alone must not be
called a relative-propagator estimate without its matrix argument.

The next invocation is literature-only. Reuse the source notes in
[assessment1228/review1229](2026-11-17-paired-subdiagonal-comparison-nomination-1228.md)
and [assessment1232/review1233](2026-11-17-real-subdiagonal-scale-comparison-nomination-1232.md),
then retrieve the exact real evolution statement and its load-bearing
degree, rate, norm and endpoint hypotheses before broader extracts.
Sra's Theorem C.9 is a source lead with recorded inspected coverage;
do not silently drop its extra degree restriction or infer that its
positive-law variance argument extends to the conjugate derivative
functional. Find an exact standard matrix logarithmic-norm/evolution
statement if needed, recording a primary citation and its applicability.
An elementary specialization needs assessed coverage rather than a
claim of novelty. Check relevant local evolution duplicates and stops
within this finite-basis route before any later mathematical attempt.

Continue only if the exact source review supports an import or a bounded
specialization/test of TARGET. The later mathematical success criterion
is a single finite absolute C for all the stated parameters; an admissible
rigorous family defeating every such C would refute it. Zero phases must
recover the stated real-reference bound. A source requiring an additional
unpaid hypothesis does not establish the displayed estimate. Failure
would concern this norm budget, not C030t's coefficient comparison or RH.

The essential local inputs for the prospective attempt are C030q's
response/floor, C030r's actual basis system and C030t's full phase bound;
C030u supplies the real-reference premise inside C030t. The additional
degree restriction is explicit. Actual-Xi supply within the phase window,
degree/time choice, signed-complement payment, theta signing, realization
and all-degree positivity remain unresolved even if this estimate holds.
No positive derivative functional, uniform beta floor or family-uniform
endpoint onset is assumed. Full matching Mathlib coverage is unchecked.

Joint-route parking1232 and stops1117/1181/1193/1200/1107 retain their
evidence; this nomination does not reopen their automatic transfers.
No justified central creative target is presently prepared: the specific
signed actual-Xi mechanism and its essential coverage are missing.
This concrete finite continuation is a specialization candidate, not
creative work relabeled to meet a schedule. No cross-notebook input.

Recommend literature_comparison, standard/high, to settle the changed
scope. This nomination is REVIEW_REQUIRED and cannot approve itself;
the completed C030t audit is unaffected by its pending review.

## Completed literature-only review1239

17 November 2026. The preceding nomination is preserved as historical
context. The current single-line fields above supersede its pending
review language. SPECIALIZE approves source scope for a later attempt;
it does not approve the truth of TARGET. This assessment became ready
during1239 and receives its separate gate approval on a later invocation.

### Exact primary inputs and scope

S. Sra, *On some positivity properties of the Riemann Xi function*,
2 November2026, [arXiv2611.02944v1](https://arxiv.org/pdf/2611.02944v1),
the accessible version used in reviews1233/1237. Refreshed Theorem C.8,
(C.15)-(C.17), printed pp26-27; Theorem C.9, (C.18)-(C.23), pp27-28;
and the ensuing right-evolution energy/Gronwall and support-boundary
arguments, pp28-29. Page numbers here are printed pages, not zero-based
PDF page indices. The prior determinant and orbital assessments remain
reusable; their unchanged HCIZ and tilted-array proofs were not reread.

In C.9 rename the source's basis dimension m to d; its m is not our
pair count. Positive real rates satisfy 0<q_j<=Q, with repeats allowed;
the restrictions are n>=2d and exactly TARGET's displayed degree
inequality. The source's C_y uses the same signed-orthogonal polynomial
coefficient convention already identified in C030r. Its generator is
lower bidiagonal (C.21). For the real reference, (C.23) gives
lambda_max((K_y+K_y^T)/2)<=Q/2. The proof then bounds
R_x(u)=C_x*C_(x-u)^(-1) by exp(Q*u/2), 0<=u<x, using
R_x'=R_x*K_(x-u), evolved row vectors and Gronwall. This is the
relevant propagator result inside the proof, rather than merely the
different shifted-Hankel conclusion (C.19).

The zero-phase list in TARGET consists of positive a_l (twice each)
and the n-2m copies of r. Taking Q=q_max is within the source's rate
hypothesis: q_max is the maximum of this actual list of real parts.
If n=2m, r is absent from that list and must not enlarge Q. With
x=t and u=t-s the source range is exactly 0<s<=t. Repeats and zero
phases are explicit permitted cases, with no distinct-rate approximation.
Its Euclidean operator norm matches TARGET's norm. This records the
applicability of an already inspected real theorem, not a proof of the
phase extension. In particular C.23 is not continued analytically to
complex rates. The source's support-boundary and global smoothing
conclusions are outside TARGET, which keeps s>0.

N. J. Higham, [*What Is the Logarithmic Norm?*](https://nhigham.com/2022/01/18/what-is-the-logarithmic-norm/),
18 January2022, is an inspected author exposition of the standard
finite-matrix facts used here. Read Lemma2 and Theorem6, together with
the displayed derivation of the Euclidean formula; also read Theorem3
and its proof to distinguish autonomous and nonautonomous statements.
For finite complex square matrices with the same subordinate norm,
Lemma2 states |mu(A)-mu(B)|<=||A-B|| and subadditivity. Theorem6 gives
mu_2(A)=lambda_max((A+A*)/2). These are known inputs, not new lemmas
to reprove. Theorem3 bounds exp(t*A) for constant A; it does not license
replacing a time-dependent propagator by exp of an integrated generator.
For the nonautonomous passage use the energy identity and Gronwall
argument actually read in Sra's proof, with all continuity and factor
ordering checks supplied in the later specialization. No commutation
of K at different times is assumed.

The required specialization is to assemble C030q's phase response and
C030t's phase subdiagonal comparison in C030r's real, smooth,
lower-bidiagonal generator, then use these standard norm/evolution
inputs. The task is still to justify that assembly with a single absolute
constant and the displayed time cost. No generator-difference estimate,
integrated phase constant, new inequality or counterexample is derived
in this review. No matching external theorem for that full conjugate-rate
statement was located; SPECIALIZE reflects the known real theorem and
standard perturbation machinery, not certified originality of the remainder.

### Reuse, duplicates, recorded failures and searches

Read C030r's hypotheses, conclusion, source normalization and parameter
system/scope ranges; C030q's family, floor, response and physical
derivative ranges; C030t's hypotheses/conclusion and determinant-ratio
setup; and C030u's hypotheses/conclusion/source scope. The coefficient
proofs passed their recorded audits and are not reaudited in this turn.
C030s is still pending and is not an essential input. Reused the primary
comparisons in assessments1228/1229,1232/1233 and1236/1237. Read
working1232's parked joint-moment route and the short stop records
1117/1181/1193/1200/1107. Their finite-to-global, class, degree/time,
theta-propagation and graph-transfer obstructions do not refute this
finite evolution question; they do bar automatic downstream transfers.

Scoped searches for evolution, propagator, logarithmic norm, C.23 and
shift norm in the paired finite-basis assessments/working notes,
assessment1232 and C030q-u found explicit exclusions of evolution
coverage, not an existing completed phase-evolution theorem in those
files. This is not a notebook-wide originality claim or a reopening of
the parked joint-moment route.

The bounded external queries included:

- `"Sra" "Xi" "moving frame" evolution`
- `"moving-frame" "conjugate" "Sra"`
- `"moving-frame signed smoothing" perturbation`
- `"finite convolution" "moving" "perturbation" norm`
- `"hypoexponential" "fundamental matrix" perturbation`
- `logarithmic norm nonautonomous linear differential equation fundamental matrix bound Soderlind 2006`
- `"logarithmic norm" "Söderlind" "2006" pdf`

Relevant inspected statements are those above; unrelated search hits,
snippets and mirrors are not theorem evidence. The earlier Gautschi,
Pozza--Pranic--Strakos, Celsus et al. and Hirschman--Widder comparisons
retain the functional and conclusion differences recorded in1229/1233;
no additional rereading was needed for this norm target.

A Söderlind lead was checked: *The logarithmic norm. History and modern
theory*, BIT46(2006),631-652,
[DOI10.1007/s10543-006-0069-9](https://doi.org/10.1007/s10543-006-0069-9).
The Lund institutional record confirms the bibliography, but is not
theorem evidence. A linked author-upload PDF gave garbled text and
screenshot calls supplied no inspectable images. No exact theorem from
that unread text is imported. This is nonessential after the readable
Higham statements and Sra's exact nonautonomous energy proof; further
access attempts are unnecessary for TARGET. No essential source blocker
remains. Full matching Mathlib coverage is unchecked, not asserted absent.
No cross-notebook input was used.

### Bounded mathematical continuation after separate approval

Keep TARGET and SCOPE unchanged. A later RESEARCH specialization may
use C030q, C030r and C030t, the real-reference source result and the
standard matrix facts just assessed; C030u supplies C030t's internal
premise. It must justify the sparse operator norm without a factor
depending on d,n,m or the real-rate spread, retain the factor 1/2 on
the real-reference exponent, and handle s=t, M=0, repeats, n=2m and
t*A=1/4. Smoothness at that closed phase boundary is already part of
C030r's audited interface. No uniform inverse-basis bound, positive
derivative functional, beta floor or endpoint s=0 is added.

Continue on a proved absolute C, or on a concrete paid intermediate
estimate with an explicit unresolved obstruction. Abandon the displayed
claim only on a rigorous admissible family defeating every C; inability
to close one comparison or a finite numerical sample is insufficient.
This specialization is source-based development, not a central creative
mechanism. Actual-Xi supply within the phase window, degree/time choice,
signed-complement payment, theta signing, realization and all-degree
positivity remain independent even if it succeeds. A justified central
creative nomination is still blocked by the missing specific signed
actual-Xi mechanism and essential coverage. Outcome EXPLORATION records
new scope assessment and readiness, with no mathematical advance claimed.
