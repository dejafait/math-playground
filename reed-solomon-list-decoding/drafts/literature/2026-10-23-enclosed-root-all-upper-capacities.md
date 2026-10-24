# Enclosed product root — proposed complete upper-capacity test

TARGET: Test L112's fixed enclosed root against all upper capacities x_i*x_j*x_h<=min(c_i,c_j,c_h) on the 28,215 actual permitted side classes.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused searches and theorem comparisons in 2026-10-23-positive-factor-interval-capacity.md and 2026-10-23-capacitated-triangle-multiplicative-scaling.md; checked L109/L110/L112 and ATTEMPTS/082,093 for overlap and failures. Directly reinspected the primary interval and scalar passages below; no repeated broad search or novelty inference.
SOURCE_EVIDENCE: Rump (2010), DOI 10.1017/S096249291000005X, corrected author PDF https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf , section 5.5 (5.16)–(5.17), author p.28, and Theorem 13.3 with full proof, author p.89; Schrijver (2005), DOI 10.1109/TIT.2005.851748, author manuscript https://homepages.cwi.nl/~lex/files/codes.pdf , III.B (62)–(65) and justification following (65), manuscript p.7. Reuse foundations/04,13,14 and L098/L109/L110/L111/L112 for existing normalization, actual classes and box.
COMPARISON: Standard interval inclusion covers products in an already certified box; Schrijver supplies scalar upper bounds and six-presentation conditions. L112 tests only (5,5,5); L110 exhausts actual classes but tests a different allowance. No inspected theorem or local result supplies all products' verdicts for this box.
GAP: Compute and independently verify exact endpoint product comparisons on all 28,215 actual permitted side classes, with original-orbit coverage. No capacity comparison is performed here. Global uniqueness, Boolean lower rows, full source feasibility, PSD and RS realization remain outside scope.
REASON: The expanded scope has adequate reused source coverage for a later standard interval-method specialization, without a new theorem or nonlinear solve. This step approves applicability only, not all-class feasibility.
SCOPE: Exactly TARGET, using L112's unchanged positive rational box and fixed pairs; no new trajectory, box refinement, parameter scan, global uniqueness proof or enlarged feasibility system.
LITERATURE_REASON: The preceding implementation approval covered one capacity only; the saved REVIEW_REQUIRED continuation expands to all actual permitted side classes and needs this separate source/scope comparison.

Approved scope: use exactly the fixed L112 box, canonical c_i, and all
actual classes reconstructed from the original orbits. No new trajectory,
smaller box, parameter scan or replacement factors. Upper products below
the class capacity pass that class only; lower products above it reject
only the enclosed root. Straddling comparisons are inconclusive. Preserve
all repetitions, null edges and six-presentation normalization; no
arbitrary t-s source variables are identified outside the product ansatz.
Independent Boolean lower rows, full source lift, PSD, global positive-root
uniqueness, packing and RS realization remain open. A complete upper-capacity
pass alone would not improve the 955–957 bracket. Source coverage is now
ready for this exact continuation; the calculation has not been run.


## Step 421 — comparison and bounded continuation

The main gap is arbitrary-center safety at 67/68 agreements; this route's
bottleneck is L098's shared capacitated-triangle feasibility. The
intermediate target is TARGET, using L021,L098,L109,L110,L111,L112 and
foundations/04,13,14. A full pass would support the upper-capacity portion
of this one product prescription; a failure would park this enclosed
root as an upper-capacitated witness. Neither closes the independent
source-lift or RS gaps.

Rump's corrected author PDF was directly reopened at section 5.5,
(5.16)–(5.17), p.28, and Theorem 13.3 with its full proof, p.89.
The first passage supplies interval inclusion, including repeated
variables in an arithmetic expression; overestimation is allowed.
The latter requires continuous differentiability, a zero-containing
error box and strict Krawczyk inclusion. Its proof uses Brouwer and
invertibility, giving local enclosure rather than global uniqueness.
L112 already applies that criterion to its rational polynomial system.
This continuation consumes the saved box, without reapplying or
reproving the root theorem. Exact rational endpoint operations need no
floating-point approximation. L112's dedicated critical audit remains
pending; source readiness does not discharge it.

Schrijver's manuscript was directly reopened at III.B (62)–(65) and
the ensuing justification, p.7. It concerns binary constant-weight
codes and normalized ordered triple counts. These passages impose
nonnegativity, pair upper bounds, permutation identities preserving
t-s, and forbidden-distance zeros. Reuse L109's existing minimum-of-three
specialization with the fixed c_i, rather than rederiving it or treating
scalar bounds as full SDP feasibility. Foundations/13 supplies the
cardinality framework, without asserting sufficiency for relaxed moments.

The overlap check distinguishes L112's single-capacity verdict from
L110's complete actual side-class enumeration and different sufficient
allowance. ATTEMPTS/093 stops that excessive allowance, not actual
products at this enclosed root. ATTEMPTS/082 concerns a failed
full-variable numerical prescription; no such solve is restarted.
L109's dual nonseparation is not primal membership. The reused scaling
assessment already compares entropy and capacity-constrained methods:
none supplies an automatic capacity guarantee. No new broad search is
essential and no novelty is claimed.

For the next calculation, reconstruct each positive endpoint in original
x coordinates from L112's complete saved certificate and rational
diagonal scales, and reconstruct canonical c_i. Bind input artifacts by
hashes. Keep N=floor(65537^28/2^128)+1. Enumerate actual source ranges,
not just formal triangle inequalities, preserving every D and t-s class.
Check their side-class projection against L110's independent realizability
criterion and count 28,215. Retain six presentations, repeated distances,
null edges, both endpoint repetitions and the coincident row under their
existing contracts. Do not divide a fixed-edge contraction by six or
identify arbitrary source variables by side lengths.

The approved tests are upper endpoint product <= minimum capacity for a
pass, lower endpoint product > minimum capacity for rejection of this
root, and otherwise inconclusive, including repeated indices. Do not
refine a straddling box. Save all class verdicts and exact ratios,
worst bounds, every failed/straddling class and complete input bindings
in a certificate. Independently reconstruct all endpoint comparisons
and full class coverage; a selected preview or decimal maximum is not
verification. No derivative calculation or nonlinear iteration is needed.

Continue only with this unchanged-box finite check. A violating class
stops this root as a capacitated witness without excluding another root;
straddling stops this box's decision on that class. Even a full upper
pass leaves Boolean lower rows, full source feasibility, PSD, packing,
RS realization and global positive-root uniqueness unresolved. The
955–957 bracket stays unchanged. This literature-only step produces no
calculation, new lemma or mathematical script.

Mathlib: matching interval-inclusion and full finite capacity-check
coverage not checked; unknown coverage is not absence. No new reproof
is justified or needed.
