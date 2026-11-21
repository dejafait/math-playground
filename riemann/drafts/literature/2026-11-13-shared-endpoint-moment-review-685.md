# Shared endpoint moments — source comparison completed686

TARGET: Test shared Taylor moments on z in [0,1/8] for C998i's fourteen moment families, joined to interior Gauss quadrature, against square error<=1e-10 and total work<=20000000.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review686 searched product integration/shared logarithmic moments,Taylor remainders,oscillatory stability and dilogarithm branches; narrowly compared C998i,C998j,assessment682/source-notes683,652/662 source scope and660/662/672 stops. Queries,read primary passages and unread/blocked nonessential leads are recorded in drafts/literature/2026-11-13-shared-endpoint-moment-source-notes-686.md. No matching fixed-data service or novelty conclusion.
SOURCE_EVIDENCE: Conrad Theorems1.1/1.2 and complete proofs pp1-4 https://kconrad.math.uconn.edu/blurbs/analysis/TaylorRemainder.pdf ; DLMF4.19.1-2 https://dlmf.nist.gov/4.19 and4.6.1-7 https://dlmf.nist.gov/4.6 ; Milovanovic-Igic-Toncev2011 Section2.2 eq(5)/conditioning remark pp3-4 https://www.mi.sanu.ac.rs/~gvm/radovi/GVM-TI-NT.pdf ; Dominguez1305.1365v3 eq(1.1)-(1.6),Theorem2.4/nonoscillatory proof,Theorem4.1/proof https://arxiv.org/pdf/1305.1365v3 ; Maximon2003 Sections2-3(a)(i),eq(2.1)-(3.10) https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=150847 ; reuse683's Trefethen19.3/(19.8) https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf and Johansson integration https://arxiv.org/pdf/1802.07942v1 ,interval arithmetic,node and primitive coverage. Source-notes686 states all domains and import limits.
COMPARISON: Shared singular-weight moments and Taylor remainder control are established tools; log-only Chebyshev stability does not transfer to Qbar or a monomial bank. Reused validated one-dimensional integration permits bank enclosures with fully charged setup; closed formulas are not assumed. Neither known convergence rates nor C998j's unaudited ideal bound certify the complete square/error/work service. Earlier direct summation stops remain prescription-specific.
GAP: Prove ONE finite bank construction and simultaneous weighted Taylor remainders for both densities,including integrable zero-axis powers,primitive branches,cancellation,precision,interior join,nodes,exact unchanged Z and every C998i entry/contraction; establish complete square error<=1e-10 and total scalar work<=20000000. No local formula,degree,precision,bound or success is supplied by this review.
REASON: Missing essential method/source coverage is now inspected; the remaining difference is effective finite specialization of known tools,not an assumed custom moment theorem. One separate REPRODUCTION feasibility attempt is source-ready,subject to supervisor approval of this changed assessment. No general theorem reproof or inaccessible source is essential.
LITERATURE_REASON: Nomination685 explicitly excluded shared endpoint power-moment construction/stability from ready682/683. This invocation completes that missing comparison rather than repeating ready interior coverage.
SCOPE: Fixed endpoint[0,1/8],interior[1/8,1],all fourteen C998i families and modes0..255,both W/V endpoints,every same-parity case and all unchanged three-column products with C999q exact Z,C998g coefficient1/4. Only the bounded method family and obligations in source-notes686 are covered; no Filon/Oliver/DE fallback,coefficient retuning,parameter sweep or signed-S3 conclusion.

Comparison686 completes the invocation-start nomination's missing source
review. Its primary-source details and mandatory finite-error/work test
are in `drafts/literature/2026-11-13-shared-endpoint-moment-source-notes-686.md`.
No mathematics is performed in this literature-only turn. The exact
TARGET is unchanged; this newly ready assessment receives the supervisor's
separate approval before a mathematical invocation. The paragraphs below
preserve the nomination's quantitative scope and unresolved obligations.

Reuse682/683 for interior Gauss,
primitive branches and finite arithmetic where their hypotheses really
apply. Search standard product integration, analytic singularity
subtraction and simultaneous oscillatory moments; inspect relevant
primary theorem hypotheses and proof cases, rather than transferring
an asymptotic rate or a library tolerance.

The intended difference is to construct a finite shared bank of power
moments for the weights Qbar,Abar1,Abar2,1/z,-1/z^2,1/(1+z),-1/(1+z)^2
on the fixed endpoint interval, then reuse it for the two densities in
each positive frequency. No formula, truncation degree, cost saving,
precision or successful enclosure is asserted here. In particular, the
zero-axis reciprocal weights require the vanishing factors in both
densities, and the primitive Q cannot be assumed numerically harmless.
The interior and endpoint pieces must reconstruct the same independent
moments and BOTH W/V brackets, including every positive diagonal class.

Bounded test after separate coverage: fix one shared-moment prescription;
pay its truncation, primitive, node, rounding, assembly and coefficient
costs; propagate error through all three-column square entries. Continue
only with complete error<=1e-10 and total work<=20000000 before a batch.
An unpaid setup/error term or excessive sufficient cost stops that
prescription without a universal lower-bound claim. No threshold sweep,
parameter retuning of685 or automatic repetition of660 is proposed.

Essential local inputs are C998i/audit682, C998h/audit678, C998a(4)/audit655,
C998g Section1/audit674, C999q exact Z and the new unaudited C998j
specialization/work stop. The witness652 and its hash remain unchanged;
use its binary-rational free modes and exact completion. C998j's ideal
entry bound and direct work count may be inspected as comparison
evidence, not treated as a certificate for this unconstructed method.

The main gap is actual-Xi positivity L030-L032/C032a and signed S3
remote-plus-induced coupling. A successful square service could pay
one full-residual component, leaving A-square, both mixed terms,
projection, the full100000000 work bound, reference inverse debt,
higher/mixed signs, C744q/H2, non-neutral and global assembly open.
It supplies no new signed coupling inequality. Thus no justified
creative central mechanism is identified by this negative calculation;
this numerical proposal is not relabeled creative to meet routing aims.
Full matching Mathlib coverage is unchecked; no cross-notebook input.
