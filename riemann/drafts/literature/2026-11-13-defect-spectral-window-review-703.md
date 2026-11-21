# Proposed central signed-coupling test: defect spectral windows

TARGET: Review source coverage and feasibility for the fixed tau=1/4 bound ||P_tau(V14+R^2)Q_tau||<=tau in C744z(4), where P_tau and Q_tau are the [0,tau] spectral projectors of I-RR* and I-R*R respectively, retaining the full neutral middle inverse and certified projector errors.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Comparison704 inspected Teschl's endpoint example,Yu--Wang--Samworth's separated-subspace theorem/proof and Colbrook--Horning--Townsend's regular-density theorem/proof;reused615/617,699/700 and compared C744z/y,C999u/C999 and exact617/603/635/640/652 stops. Queries and limits below;no matching inequality found or novelty inferred.
SOURCE_EVIDENCE: Teschl GSM99 version12February2009 https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf Lemma6.39 p156,Corollary6.40/example(6.53)-(6.54) p157;Yu--Wang--Samworth Biometrika102(2015)315-323 https://personal.lse.ac.uk/wangt60/publication/DKvariant.pdf Theorem2 p317/proof pp321-322;Colbrook--Horning--Townsend2006.01766v1 https://arxiv.org/pdf/2006.01766v1 Theorem5.3 p16/proof p27. Reuse615's Douglas Theorem1 and Dritschel--Rovnyak LemmaA.1 for bounded blocks only.
COMPARISON: Norm convergence alone does not pay sharp-projector approximation at an endpoint atom;the inspected perturbation/smoothing theorems need unpaid separation or density regularity. Existing inverse-action certificates are not global norm/projector enclosures. No source establishes the actual localized coupling. First nominate an independent no-projector norm/vacuity test.
GAP: Actual window relevance remains unknown;a strict normalized two-cell bound below sqrt(3)/2 has not been extracted. Direct localization still needs full actual inverse/square-root norm enclosures and endpoint handling or a justified outer enclosure,plus signed coupling. The original inequality remains unproved.
REASON: Completed source comparison changes the route:park direct sharp-projector approximation and test possible window vacuity from the existing two-cell certificate. This is a source-applicability negative,not a negative actual-window direction or an impossibility theorem for certified localization.
LITERATURE_REASON: This changes the target from a frozen residual certificate to actual defect spectral localization;existing inverse-order and band-certificate coverage does not assess sharp projector errors or feasibility here.
SCOPE: Source review only;fixed tau=1/4,actual C744z R,V14,H0,A0,full separation7/14 operators. No numerical calculation,new lemma,replacement reference,tau tuning,assumed spectral gap or discarded defect/kernel/cross term.

The main gap is the actual-Xi positivity of L030-L032/C032a and,
on this route,the signed remote-plus-induced block in C744z(4).
This nomination asks about one fixed window of the ACTUAL defects
I-R*R and I-RR*. Its proposed threshold is a target to assess,
not a derived theorem or a claim that spectral localization works.
It is not a raw cosine cutoff or another rank-two addition to598.

Potential downstream use: a paid bound could isolate whether coupling
between directions of small endpoint defect is an obstruction,or
supply one component for a full block estimate. Even success leaves
both mixed spectral windows and their complements,full S3 positivity,
H2/higher endpoints,non-neutral coverage and Xi/global assembly open.
The defect windows may be empty or inaccessible; neither possibility
is resolved here. A bare appeal to a general factorization criterion
or spectral calculus would not pay the actual coupling.

Continuation test for the source step: inspect exact theorem
hypotheses and essential proof cases,compare recorded failures,and
identify a finite,certified test of this fixed inequality that does
not presume an unknown spectral gap or full S3 positivity. If the
sharp windows cannot be controlled without new essential input,
record that precise obstacle and seek a materially different test;
do not replace them silently by a tuned cutoff or smooth window.
Further mathematics needs a separately saved ready assessment.

Essential inputs for the continuation: C744z(2)-(4),Section3 and its
reflection discussion in Section7;C744v/w/y for full operators and
two-cell contraction;C999u/audit619 for the stopped energy-image
majorant;C999k/C999/audit650 for qualified inverse comparisons;
C998q/audit703 solely as a validated partial saving,not a full debt.
Reuse source assessments615/617 and699/700 where their hypotheses
match. Retain617/603/635/640/652 stops and the original source/core/
arithmetic contracts and unreplayed c_*. Witness652 and X are not
retuned or replaced;they are not presumed to approximate a spectral
window. No cross-notebook theorem is involved. Full matching Mathlib
coverage has not been checked.

This source preparation takes priority over another routine audit.
It is not yet a source-ready creative proof attempt. If feasibility
and material novelty of the mechanism survive comparison,a later
proof_attempt/creative nomination must name its exact finite test
and decisive evidence. Do not label the completed703 specialization
creative or invent a successful lemma to satisfy scheduling.


## Completed source comparison704 — 13 November2026

The nomination's pending-coverage language above is superseded by this
section and the fields. This was LITERATURE only: no projector,inverse
action,norm bound or new mathematical result was derived or computed.

### Primary hypotheses and essential cases read

[Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Lemma6.39 p156/Corollary6.40 p157 require vanishing limiting endpoint
atoms for strong interval-projector convergence under strong-resolvent
convergence. The short proof uses converging scalar spectral measures
and interval masses. Read the complete example(6.53)-(6.54),p157:
A_n=diag(1,-1)/n converges in norm to zero,but its half-line projectors
fail to converge to the corresponding limiting projector for either
endpoint convention. This blocks a general continuity shortcut,not
this actual operator. No actual endpoint non-atomicity or quantitative
projector norm estimate has been established. Reuse699/700's earlier
closed-form/calculus coverage;no new spectral theorem is reproved.

[Yu,Wang and Samworth,*A useful variant of the Davis--Kahan theorem
for statisticians*,Biometrika102(2)(2015),315-323,
doi:10.1093/biomet/asv008](https://personal.lse.ac.uk/wangt60/publication/DKvariant.pdf),
Theorem2 p317/full proof pp321-322: real symmetric finite matrices,
a consecutive eigenvalue cluster and positive population separation
are required. Its sine-angle Frobenius bound is twice the minimum of
sqrt(d) times operator perturbation and Frobenius perturbation,divided
by separation. The proof bounds a residual in two ways,divides by
separation in(A4),and handles basis alignment in(A5). Removing the
sample-gap hypothesis does not remove every gap hypothesis. No complex
infinite-dimensional extension or actual separation is imported.

[Colbrook,Horning and Townsend,*Computing spectral measures of
self-adjoint operators*,arXiv2006.01766v1](https://arxiv.org/pdf/2006.01766v1),
Theorem5.3 p16/full concluding proof p27 assumes a normalized scalar
spectral measure,absolute continuity on an expanded interval,a W^(m,p)
density,1<=p<infinity,and an mth-order kernel. It bounds density error
in L^p. Read both terms of(A.19): the local-density term invokes
LemmaA.2;the remaining measure is separated from the inner interval
and bounded by kernel decay. LemmaA.2's earlier proof is not imported.
This is not a uniform operator-norm bound for a sharp projector;its
regularity hypotheses are unpaid here. Smooth-observable convergence
after the theorem does not certify an indicator. SpecSolve was not run.

### Local comparison and decision

Read C744z(1)-(4),Section3 and Section7's reflection discussion;
C744y hypotheses/conclusion/Section4;C999u's exact comparison and
audit qualification;C999's conclusion/effective-data contract.
Reuse615/617's inspected bounded-block and inverse-order results and
699/700's finite-band coverage. No general theorem needs reproof.
Full matching Mathlib coverage remains unchecked.

Compared exact ATTEMPTS617/603/635/640/652. The C999u reference
negative is not an actual S3 negative direction. Rank-two repair640
and implementation-budget failures603/635 concern other comparisons.
The652 grid prescription is not a complexity lower bound. C998q
pays one frozen debt component,not global inverse or projector error.
C999's terminating full-action procedure concerns its lower reference
B0 and specified L2 inputs,not an operator-norm enclosure of actual E.
Quantitative reference floors remain available with their hypotheses:
do not claim that only the original tiny c_* can be used. Reflection
alone is already in C744z and supplies no new sign.

Three possibilities were compared: sharp-projector perturbation,
resolvent smoothing,and a preliminary normalized two-cell norm test.
The first two lack the hypotheses above;no impossibility is claimed.
The third is independently testable without projectors and asks
whether the particular1/4 window is empty. Its exact target and
standard-method coverage are nominated in
[review704](2026-11-13-defect-window-vacuity-review-704.md).
No threshold crossing is presumed. Absolute head slack cannot simply
be called a relative energy margin;full metric conversion,mixed
covariance and infinite complement remain research obligations.

Park direct sharp-projector implementation. Preserve actual operators
and tau;no silent smooth replacement,assumed gap or witness change.
Even the requested localized norm <=1/4 would not alone pay the
defect-weighted criterion,mixed windows or full S3. A vacuous window
would settle only this test and motivate leaving this window mechanism.
Core/arithmetic/source contracts,C744q/H2 and Xi assembly remain open.
No cross-notebook input was read.

### Search record and limits

Queries included `spectral projections discontinuity no spectral gap
operator norm Davis Kahan theorem residual spectral pollution certified`;
`contraction defect operators spectral projections block positivity
localized off diagonal defect operator`;`computing spectral projections
self adjoint operators no spectral gap verified resolvent spectral
pollution Colbrook`;`Yu Wang Samworth useful variant Davis Kahan
theorem pdf 2015 theorem 2`;`Colbrook spectral measures spectral
projections endpoints atoms theorem computing spectral measures 2019
pdf`;`"defect" "spectral projections" "Weil" positivity`;
`"I-RR" "V14" spectral`;`"spectral projection" "operator norm"
"no gap" enclosure`;`"spectral subspace" "enclosure" "gap-free"
operators`;`"block operator" "strict contraction" "Schur" positive
matrix`;`"Weil" "separation" "defect" "spectral projectors"`;
`"localized Weil" "strict" contraction`.

Colbrook1908.06721/1908.09592,general spectral-pollution results,
recent AMW/Ritz and defect-theoretic RH search hits remain unread
leads,not theorem inputs or essential claimed coverage. No snippet
was imported. No exact match in this bounded search proves novelty.
Essential sources for the applicability rejection were accessible.
The new704 continuation receives separate approval next turn.
A creative coupling attempt is premature while window relevance and
a paid actual coupling test remain unresolved.
