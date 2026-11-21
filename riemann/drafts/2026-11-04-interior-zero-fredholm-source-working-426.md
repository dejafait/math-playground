# Interior-zero norm-compression source review — step426

Literature-only working notes for the unchanged TARGET in
`literature/2026-11-04-interior-zero-fredholm-norm-compression.md`.
No lemma, operator specialization or mathematical script is being written.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
question is an exact finite norm certificate for L776, with repeated complex
interior zeros and the remaining zero-free factor retained. Its downstream
use would be to pay the sufficient norm hypothesis for one admissible pair;
all radii/orders and other minor indices remain independent gaps.

Local reads: complete L776 and its approved specialization assessment;
step423 comparison, its boundary-sign ATTEMPTS record, and step425 working
record/history. Targeted searches in those Fredholm records found no prior
rational/confluent norm certificate. Existing work is preserved. No
cross-notebook input is proposed.

Primary sources retrieved through the web tool:

- Peller, *An excursion into the theory of Hankel operators*, MSRI33
  (1998), Section4, Theorem4.1, printed pp.76–77: rational generating
  functions characterize finite-rank Hankel matrices. Read both proof
  directions, including the recurrence spanning the rows. Section6,
  Theorems6.1–6.2, printed p.81: optimal rational approximation is an
  existence statement; it supplies no actual-G effective norm budget.
- Perfekt–Pushnitski, arXiv:1611.03772v2 (30 August2017), Section6.2,
  Theorem6.1, PDF pp.18–19: derivative-evaluation formulation includes
  confluent nodes and rank counted with multiplicity. Read the full
  statement and the boundedness qualification: every node must lie
  strictly in the disk. This is a recalled classical theorem, not their
  novel Helson result; no Helson theorem is used.
- Yafaev, arXiv:1304.2677v1 (9 April2013), Section5.1, (5.2) and
  (5.6)–(5.7), PDF pp.22–23: arbitrary pole orders give polynomial times
  exponential matrix entries. The selfadjoint inertia results later in
  Section5.2 are not norm certificates for the nonselfadjoint product.
- Gragg–Reichel, *On singular values of Hankel operators of finite rank*,
  NPS-53-89-003 (November1988), primary Calhoun report retrieved; initial
  hypotheses explicitly require coprime numerator/denominator and
  initially distinct poles, deferring repeated poles to Remark1.1.
  The relevant theorem and that remark still need their full read.

Shell download failed at DNS; web primary retrieval works, so this is
not a source blocker. PDF screenshot calls returned no inspectable images;
the read evidence above is the extracted primary text. No claim relies on
a screenshot preview or search snippet.

Comparison during review: the full product and the Hilbert-space metric matter.
A finite-rank Hankel factor alone does not prove that its product with the
other factor has small norm. A nonorthogonal coefficient matrix's ordinary
singular values cannot silently replace the original l2 norm. Need a
source-backed finite metric/SVD reduction and an explicit, conditional
analytic-remainder budget before a mathematical continuation is ready.

Completed comparison and exact qualifications are in the assessment above.
Gragg–Reichel Section1 (1.11)–(1.17) and full Remark1.1 were read: QR
retains the original norm, repeated poles use Jordan/confluent data, and
the authors omit the general multiplicity details. Shapiro MAT520 (2024)
Theorem9.25 and its proof, pp.90–91, supply the standard polar-decomposition
input without an inverse-Gram hypothesis. The assessment specifies the
future full-product matrix and conditional error obligations; none is
asserted proved here. SPECIALIZE now covers the unchanged exact target.
Outcome is a source-coverage ADVANCE, NOVELTY_UNCHECKED, with no discovery
beyond the cited sources and no actual norm bound. No change to PROOF or
DAG is warranted. A bounded application attempt is the next action.
