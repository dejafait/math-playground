# Fixed-input detector: bounded conceptual audit coverage

TARGET: Audit van Hemert v1.0.0 FB1-FB8 for q=2 and h=(-d^2/dy^2+1/4)g with g(y)=exp(-1/(1-y^2)) on |y|<1 and zero otherwise, checking actual theta normalization, vector Mellin convergence, multiplicity and the cumulative limsup lower bound while leaving both primitive-sector upper bounds unpaid.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2080's exact-label local duplicate search found no canonical fixed-band detector import; the primary theorem and full proof were read during the GC12 comparison alongside the theta reconstruction. Details and other-source boundaries are in source-notes2080; no new theorem is claimed.
SOURCE_EVIDENCE: Leonard van Hemert, Exact Zero Detection and Compact Arithmetic Realizations for the Riemann Xi Function, v1.0.0,11October2026, DOI10.5281/zenodo.23295277; tagged paper.tex lines802-838 and11124-11317, labels lem:log-source-mellin and thm:fixed-band-cumulative, FB1-FB8 including the compact-height case. Complete relevant proofs inspected, not independently certified.
COMPARISON: The source explicitly states and proves the detector for every nonzero compact smooth input, and its pole-neutral input construction includes the fixed bump. Audit this known manuscript specialization because its actual-kernel and detection dependencies remain unverified locally; do not reprove standard Fourier or complex-analysis theorems.
GAP: Check actual normalization, all interchanges, nonvanishing numerator, exact-order Laurent coefficient, infinite/finite limsup cases and finite-height uniformity. No source-energy upper, GC12 signed upper, high-sector upper or mixed-form transfer follows from source reading alone.
REASON: This accessible, independently testable input to the proposed downstream use requires no conjectural cancellation after the new primary comparisons failed to supply an upper. Newly ready continuation awaits separate next-turn approval.
SCOPE: Fixed input, q=2, FB1-FB8 and their stated theta/Fourier foundations only. The Fourier band is a positive constant chosen as in FB7, not GC12's primitive cutoff. No gamma completion, arithmetic upper, exceptional-set theorem, semilocal positivity or RH conclusion is authorized.

Primary source:
[tagged paper.tex](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex).
The complete relevant read and qualifications are recorded in
[source-notes2080](2026-11-21-fixed-coprime-covariance-source-notes-2080.md).
Reuse that reading; retrieve a passage again only for an exact audit
obligation, rather than repeating source discovery.

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. This audit would verify the claimed growth cost forced
by a hypothetical off-line zero for one actual fixed source, if correct.
It would establish a reliable threshold against which a future complete
arithmetic upper could be compared. Neither primitive upper is assumed;
the full source-energy upper and any link back to the mixed form remain
independent gaps. Do not use C032a's RH-equivalent condition as a premise.

Audit the following as one argument, without declaring it proved here:

- The theta series and chosen Fourier convention yield precisely the
  weighted multiplier used in FB3, with Plancherel constants retained.
- The fixed bump yields a nonzero compact smooth h in the stated
  weighted space and satisfies the source's two pole conditions.
- Absolute Bochner Fubini is paid for Re(z)>1/2; holomorphy on the
  later energy-controlled half-plane follows from an explicit compact
  majorant, rather than an assumed zero-free region.
- Projection does not kill the numerator; a zeta zero of exact order m
  produces the stated Laurent vector m!Pi A_q(z_rho)h/zeta^(m)(rho).
- The finite-limsup contradiction, Stieltjes boundary terms, epsilon
  exponents and factorial constant in FB6 hold; the infinite-limsup case
  is retained. No rightmost-zero assumption is permitted.
- Both the large-height G_Q estimate and compact-rectangle nonvanishing
  argument are valid for the same fixed band and input.

Continue if the entire stated input survives; document any repair or
qualification precisely, with canonical proof/citation only after the
audit. Abandon an invalid application if an interchange, cancellation
or limsup step fails without a paid repair. An arithmetic upper staying
open does not count as a failure of this audit.
This is REPRODUCTION of an unreviewed source argument, not a creative
discovery or an UNVERIFIED CANDIDATE resolution of RH.
Use proof_audit/conceptual_audit, deep_research/xhigh: vector Mellin
continuation across possible poles and the quantitative limsup
contradiction require delicate analytic scrutiny. No cross-notebook
input; full matching Mathlib coverage is unchecked. Named standard
tools in source-notes2080 may be cited with hypotheses checked locally.
