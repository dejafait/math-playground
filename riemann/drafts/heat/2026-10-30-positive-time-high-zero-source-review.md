# Positive-time uniform high-zero source comparison

2026-10-30. Literature only; no new derivation, lemma, script or numerical
certificate. Existing notebook changes preserved. Main gap: actual-Xi
all-degree mixed positivity. Intermediate question: a common real/simple
high-zero tail on compact positive-time intervals, independently of Lambda.
Its downstream use would be to remove escape to infinity before a separate
bounded-height collision argument. It would not exclude those collisions.

## Primary sources and exact scope

H. Ki, Y. O. Kim and J. Lee, *On the de Bruijn–Newman constant*,
Advances in Mathematics **222** (2009), 281–306,
[DOI 10.1016/j.aim.2009.04.003](https://doi.org/10.1016/j.aim.2009.04.003).
The [publisher abstract](https://www.sciencedirect.com/science/article/pii/S0001870809001133)
was inspected. Its finiteness assertion is for each positive parameter.
The original proof remains unread: publisher full text returned 403; the
original Yonsei PDF and ordinary/id_ archive URLs were inaccessible.
An apparent Citeseer link in Tao's proposal did not yield the paper through
this interface. Do not count that link or search excerpts as proof coverage.

Rodgers–Tao [v3 Remark 1.2](https://arxiv.org/html/1801.05914v3)
cites KKL Theorem 1.14. The later source below instead cites KKL
Theorems 1.3 and 1.4. The numbering discrepancy remains unresolved;
no silent identification of the original numbered statements is made.

D. H. J. Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31;
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2)
([PDF](https://arxiv.org/pdf/1904.12438v2)). Read Theorem 1.5(i)–(iv),
pp.9–10; Proposition 9.1 and its proof, pp.56–58; Lemma 9.2 and proof,
pp.58–59; proof of Theorem 1.5(i)–(ii), pp.59–60, equations (102)–(104).
Also inspected Proposition 3.1(ii) and Theorem 3.2. No full manuscript audit.
Theorem 1.5 uses absolute constants, with 0<t<=1/2 and x>=exp(C/t).
Part (i) exhausts all zeros there; part (ii) states uniqueness in small
complex disks. The proof uses an argument-principle count and the global
strip |Im z|<=1. Neither a density-one conclusion nor t>Lambda is assumed.

## Applicability and audit obligations

Reuse the normalization already checked in
[the preceding source note](2026-10-30-positive-endpoint-source-comparison.md):
L019 and L058 identify F(lambda,z)=8 H_(4lambda)(2z).
The proposed application is restricted to 0<a<=lambda<=b<=1/8,
corresponding to 0<4a<=t<=4b<=1/2. This covers the part relevant to
a possible positive Newman obstruction. The full all-positive-time
extension is not imported by this review, nor is any limit a down to zero.

A later mathematical step must explicitly reconcile the threshold in x
in (i) with the threshold in n in (ii), show that every high zero enters
one of the counted disks, retain multiplicities, reflect to negative real
parts, and choose one height for the entire compact time interval. None
of those specializations is proved in this literature-only turn.

A specific reason for a focused proof audit was found: (104) displays an
O(|y| log x_n + x_n^(-ct)) error, in both PDF text and HTML, followed by a
one-winding assertion on a circle of radius proportional to 1/log n.
The displayed estimate alone does not state a strict comparison constant
there. Check the earlier two-exponential expression (102) and phase
relation (103), rather than treating a coarse O estimate as a certified
Rouche inequality. No error in Theorem 1.5, repair, or refutation of its
proof is established here. The PDF screenshot produced no inspectable
image; the agreement claimed is between the two text extractions.
The audit may accept Proposition 9.1(i) and Lemma 9.2 as cited inputs;
it must not claim an independent audit of their Riemann–Siegel foundations.

## Reuse, negative records and bounded decision

Narrow exact-title/author searches in drafts/literature, foundations,
ATTEMPTS and drafts/heat found no completed Polymath uniform-tail
assessment. Searches in the heat lemma ranges L05*, L06*, L12* found
local splitting/continuation and uniform-growth limitations, not this
import. Read L058, L019, L126 and L128 for the exact local family and
obstruction. L126's analytic moving-supremum counterexample remains
valid; L128 only controls bounded domains. The September 20 heat-route
failure is preserved. No global ban on renewed heat work is inferred.

Queries included the exact KKL title with Theorem 1.14, p23-reprint.pdf,
S0001870809001133, and positive-time uniform zeros. Tao's proposal and
Ki's survey were discovery leads only, not replacements for a primary
uniform theorem. No novelty is inferred from failed searches.

Decision: direct KKL proof access remains blocked, but the independently
accessible stronger primary theorem removes that blocker for the restricted
compact-time application. Nominate a separate conceptual audit of its
localization/count and normalization before recording a canonical lemma.
Continue if (102)–(103) support a uniform multiplicity-one count and the
thresholds can be reconciled; otherwise preserve the exact failing estimate
and park that application. This is local source progress beyond the prior
coverage, not progress beyond Polymath's published result. Finite and higher
collisions, all-height signs, t=0, and full Mathlib matching coverage remain
unresolved. A creative collision mechanism is not yet ready.
