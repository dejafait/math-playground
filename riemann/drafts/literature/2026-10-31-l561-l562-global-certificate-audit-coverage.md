# Coverage nomination for the fixed-model certificate audit

TARGET: Review the Schur-identity and causal-factor hypotheses needed for an independent audit of L561-L562's fixed-model strict-PF256 and negative-first-sign certificate.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the fixed-model and finite-order transform assessments; searched Macdonald Schur Jacobi-Trudi/branching/dimension sources and inspected the primary textbook passages listed below. No broader novelty search or new model calculation.
SOURCE_EVIDENCE: Macdonald, Symmetric Functions and Hall Polynomials, second edition (1995), I.1 p.5, I.3 (3.1)/(3.4) pp.40-42 and Examples 1/4 pp.44-45, I.5 (5.9)/(5.12) pp.71-73, https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf; reuse Sra v2 C.1/C.6 pp.18,21 and their proofs from the two prior assessments linked below.
COMPARISON: The standard finite-polynomial identities match L562 (4)-(6); the reused interval Wronskian criterion covers the proposed open-half-line use without asserting strictness across the causal support edge. Neither source supplies the model's uniform estimates or convolution assembly.
GAP: Essential source coverage is ready; independent verification of L562's all-partition bound, matrix signs, infinite expansion, distributed derivatives and ordered integral, plus L561's retained density/transform/regularity/first-sign inputs, remains undone.
REASON: Newly inspected exact standard-algebra inputs close the source gap for a separate conceptual audit of an existing certificate; this is local source progress, with no new mathematical result or originality finding.
LITERATURE_REASON: The newly completed L562 certificate introduces Schur identities and a causal support-boundary application outside the preceding model-attempt assessment's inspected algebra scope; these essential passages were previously unread.
SCOPE: Exactly P_* of L561-L562, m=270, r=256, A=2^20, b=1/4; approve scrutiny of the existing proof and necessary standard specializations only. No parameter search, replacement mechanism, Xi transfer or general finite-order classification.
COVERED_TARGET: Independently audit L561-L562's fixed-model strict-PF256 and negative-first-sign certificate, including its Schur comparison, infinite determinant expansion, causal convolution and retained density inputs.

## Original nomination (historical; completed review follows)

The preceding ready assessment remains unchanged at
`2026-10-31-high-rank-pf256-fixed-model.md`. It authorized the mathematical
attempt that produced L562, not an independent audit of a proof that did
not yet exist. This nomination is deliberately REVIEW_REQUIRED.

The next source step should retrieve the exact primary hypotheses for
Jacobi--Trudi, tableau branching with two extra variables, and the
all-ones dimension specialization. Check finite alphabets, partitions
of length at most 256 inside 270 real letters, zero padding and complex
evaluation. Reuse the already inspected Sra C.1/C.6 unless a changed
hypothesis is found. A named textbook identity is distinguished here
from a newly inspected primary passage; no novelty follows from the
absence of an inspected source for this fixed model.

Essential input IDs are L561 and L562. The future audit must inspect
the canonical proofs completely where load-bearing, rather than infer
global positivity from the nine scalar checks. The latter certificate
only checks the rational margin and regularity/index thresholds.

The decisive mathematical audit test will be whether (11)--(23) of
L562 are valid uniformly for all partitions, all k<=256 and all real
centers, with the causal factor differentiated only through 255 across
its support boundary. Any failed identity or unlicensed interchange
must be localized before the model is used as a reviewed obstruction.
The first-sign input at A and its location outside |Re z|<1 must remain
explicit. These are future audit requirements, not checks completed by
this nomination. Actual-Xi realization, the complete signed remainder
and higher polynomial signs remain independent unresolved questions.

Mathlib coverage for the full certificate and its algebraic/analytic
components remains unchecked; availability is unknown.

## Completed source comparison — 31 October 2026

Main gap: actual-Xi all-degree positivity and the uncontrolled complete
first-sign signed remainder at unbounded heights. The intermediate target
is source coverage for auditing this one finite-order model obstruction.
Downstream use is to determine whether strict PF256 alone can supply a
generic first-sign transfer; it supplies no realization of Xi.

### Inspected algebra and applicability

Primary reference: I. G. Macdonald, *Symmetric Functions and Hall
Polynomials*, second edition, Oxford University Press, 1995,
[university-hosted scan](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf).
Printed pages differ from PDF pages by ten. The following statements
and the indicated proof cases were read, rather than inferred from snippets:

- I.3 (3.1), p.40, and (3.4) with proof, pp.41-42: bialternant and
  Jacobi--Trudi, matching L562 (4).
- I.5 (5.9), pp.71-72, and (5.12), pp.72-73, including the intervening
  one-letter/horizontal-strip argument: alphabet splitting and skew
  tableau expansion. The tableau convention is I.1, p.5.
- I.3 Example 1, p.44: finite principal specialization via Vandermonde;
  Example 4, p.45: all-ones hook-content specialization.

For applicability, distinguish determinant size k from alphabet size m.
Zero-pad lambda to m=270, with length(lambda)<=k<=256. In Example 1's
Vandermonde quotient take q to 1: each factor ratio has limit
(lambda_i-lambda_j+j-i)/(j-i), precisely L562 (6).
This is a standard finite specialization, consistent with Example 4,
not a new bound. Polynomial identities admit repeated and complex
letters, including the two-letter alphabet in L562 (5).
The tableau rows are weakly increasing and columns strictly increasing.

No reproof of these identities is needed. In particular the sources do
not prove the proposed box-removal estimate (7), its uniform summation,
or the positive lower bound (11). Those are part of the future audit.
The source comparison approves their algebraic inputs, not their truth.

### Reused Wronskian scope and causal qualifications

Reuse the inspected C.1/C.6 statements and complete short proofs in
[the finite-order comparison](2026-10-31-strict-pf256-reciprocal-polynomial-transfer.md),
especially its usable-strictness section, and
[the direct-URL recovery](2026-10-31-high-rank-pf256-fixed-model.md),
final section. Primary citation: S. Sra, *On some positivity properties
of the Riemann Xi function*, v2, 29 October 2026,
[C.1, printed p.18](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf#page=18),
[C.6, printed p.21](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf#page=21).
No changed theorem hypothesis or source update was found that requires
reopening the same PDF.

C.1 is an interval criterion for real functions with positive initial
Wronskians and the necessary derivatives; its evaluation points are
strictly increasing. Its scope therefore allows (0,infinity). The
certificate proposes analytic functions there. The audit must establish
every prefix Wronskian with the displayed signs before invoking it.
No global strictness theorem is being applied to the zero-extended q.
C.6 instead needs p in C^(2r-2)(R) and strictly positive signed
differential determinants for every real center and every k<=r.
Here that means C^510 and all centers; L561's claimed C^542 regularity
must be checked independently. Sra C.7's Xi certificate is excluded.

### Exact remaining audit and stop test

Audit the canonical L562 in full and L561's load-bearing density,
normalization, transform, regularity and negative-first-sign proofs.
L561's earlier middle-range gap is addressed only by the proposed L562
argument; its tail/local determinant estimates are not substitutes for
that argument or essential inputs to the new global assembly.

The audit must check (7)-(11) uniformly over every partition of length
at most 256; the row reversals and partitions in (14)-(16); finite
Cauchy--Binet followed by a justified limit; exponential decay and zero
traces at the support edge; distributed derivatives through total order
510 with no factor differentiated beyond 255; the Fourier identification
and constants; and every sign, absolute-integrability requirement and
strictness assertion in (20)-(23). Cauchy--Binet is finite algebra;
the ordered Andreief identity is explicitly expanded and justified by
Fubini in the proposed proof. These local justifications, rather than an
unread infinite-dimensional identity, are what the audit must verify.
No analytic interchange or new causal-factor lemma was proved here.

Continue only if those claims and L561's first sign at A survive a
separate conceptual audit. A failed identity, interchange or support-edge
hypothesis must be localized and preserved before the model is relied on.
A source mismatch discovered during that audit reopens coverage for
that exact dependency. The current comparison finds no essential source
blocker; a shell download failed DNS, but the textbook passages were
accessible through the web PDF text. Search hits and screenshot requests
were not used as a substitute for reading the theorem text.

Queries used included `Schur functions Jacobi Trudi branching rule Weyl
dimension formula Macdonald symmetric functions pdf`, `site.math.mit.edu
Stanley symmetric functions skew Schur branching Jacobi Trudi pdf`,
`Macdonald Symmetric Functions Hall polynomials pdf I 5 9 3 6 n lambda
ones`, and `site.math Berkeley Macdonald symmetric functions pdf`.
Other returned lecture notes and classification papers add no essential
input and were not promoted to inspected theorem evidence. Reuse the
parent transform comparison for Schoenberg/Khare limitations and the
recorded PF2 and actual-theta transfer failures; no novelty follows from
this source search.

Outcome: local source-coverage ADVANCE only. The covered audit is a
separate mathematical step, subject to the supervisor's approval of this
newly completed assessment. No lemma, mathematical script, DAG or PROOF
change occurred. Actual-Xi realization, higher polynomial signs and RH
remain open. Mathlib matching coverage remains unchecked, not absent.
