# Coprime Mellin mechanism: source evidence2082

Literature-only comparison of assessment2081's unchanged TARGET, completed
2026-11-21. Outcome EXPLORATION: useful source coverage, no matching upper
or cancellation theorem found, no new mathematical result. No lemmas or
mathematical scripts were written. The next proposed attempt is specified
in that assessment, not performed here.

## Reuse, local scope and discriminator

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate target tests whether the exact signed GC12
covariance has pole cancellation strong enough to support its one-sided
subpower upper. C034r's conditional cumulative-energy lower threshold is
the potential downstream use; it is not a theorem about GC12 alone.
High primitive control and the mixed-form bridge remain independent.

Read comparison2079, source-notes2080, C034r's hypotheses/conclusion and
weighted multiplier proof passage, stops2076/2077/2079 and history2081.
Reuse the already inspected lcm/GCD/spectral comparisons. Their changed
kernels do not become applicable through an unsigned or entrywise bound.
The positive convolution-inverse stop C034q is contrast, not a premise.
A targeted search in these local assessments/stops found no existing
two-variable residue assessment. No other notebook was read.

The discriminator must involve the actual integrated principal part and
the finite square cutoff, not a generic Euler-product pole. Meromorphic
continuation, pole-neutral unweighted moments and C034r noncancellation
do not themselves decide this new question. These are scope distinctions,
not a derivation of a GC12 residue or a new obstruction theorem.

## Primary statements and essential cases actually inspected

### Bhowmik--Essouabri--Lichtin: known extraction, no cancellation theorem

G. Bhowmik, D. Essouabri and B. Lichtin, *Meromorphic continuation of
multivariable Euler products*, Forum Math.19(2007), 1111-1139,
DOI[10.1515/FORUM.2007.044](https://doi.org/10.1515/FORUM.2007.044).
Read the [author proof PDF](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/multieuler.pdf),
Section1.1, Lemma1 and complete proof, Theorem1 and proof: PDF pp4-8.
The PDF has a 2006 proof-production header and placeholder DOI;
use these PDF locators rather than silently treating it as the final
pagination. The arXiv math/0502508 copy was also accessible; its longer
version's proofs were not substituted for this inspected version.

For analytic functions lambda_j on an open Lambda in C^n and fixed
integers a_j, Lemma1 treats

\[
 Z_\lambda(s)=\prod_p\left(1+\sum_{j=1}^r a_jp^{-\lambda_j(s)}\right),
 \quad W(\lambda,d)=\{s\in\Lambda:\Re\lambda_j(s)>d\ (1\le j\le r)\}.
\]

It continues the initially absolutely convergent product from W(lambda,1)
to W(lambda,0), with a finite product of zeta factors to integer powers
and a bounded, absolutely convergent holomorphic Euler remainder on
each W(lambda,d), d>0. Inspected proof cases: integer-binomial extraction,
uniform p^-2 remainders, repeated degree raising and final finite zeta
extraction. Theorem1 applies this to polynomial local factors using the
specified Newton-polyhedron inequalities.

This gives meromorphy, not cancellation or nonvanishing of all remaining
local factors. GC12's prime-dependent rational weight and integrated
ratio kernel are not the lemma's stated finite fixed-integer input.
A valid encoding or direct factor extraction still needs proof. No
application or boundary for GC12 is inferred here. The later natural-
boundary proof was not audited.

### Delabarre: stronger boundary result does not decide this slice

L. Delabarre, *Extension of Estermann's theorem to Euler products
associated to a multivariate polynomial*, Bull.Soc.Math.France141(2)
(2013), 225-265, DOI[10.24033/bsmf.2647](https://doi.org/10.24033/bsmf.2647),
[primary PDF](https://www.numdam.org/article/BSMF_2013__141_2_225_0.pdf).
Read Section1.1/1.2, printed pp226-230: integral polynomial setup,
Definition1/2/3, quoted continuation theorem, Main Theorem and Theorem1.1.

For nonconstant h in Z[X_1,...,X_n], h(0)=1, the domain uses all its
monomial exponent inequalities. The stronger obstruction assumes h
noncyclotomic and a nondegenerate face: the associated one-variable
face polynomial has no repeated root. It prohibits meromorphic extension
through the stated face; Theorem1.1 concerns real-analytic CR extension.
No hypothesis verification, boundary identification or applicability
to the fixed-parameter integrated GC12 expression was performed. Neither
this generic theorem nor the quoted continuation statement cancels an
individual interior reciprocal-zeta pole. The long natural-boundary
proof and its generic-point cases remain unread and are not premises.
No need to reproduce that theorem for the proposed local test.

### Ramaré: finite-cutoff errors are part of Perron inversion

O. Ramaré, *Modified truncated Perron formulae*, Ann.Math.Blaise Pascal
23(1)(2016), 109-128, DOI[10.5802/ambp.356](https://doi.org/10.5802/ambp.356),
[published PDF](https://numdam.org/item/10.5802/ambp.356.pdf).
Read Theorem1.1, printed pp109-110, Theorem2.1 setup pp112-113,
and the endpoint conversion proof of Theorem1.1 p116. Theorem1.1
allows complex a_n, requires kappa>0 strictly above absolute convergence
and T>=1. Near x, theta_n is real in [0,1] in the published theorem.
Its truncated integral has both an absolute-series error and an absolute
short-interval error. Both strict and inclusive endpoints are covered.
This supplies a possible cutoff tool, not a GC12 error estimate or a
contour-shift theorem. Applying it twice and integrating the actual ratio
kernel still requires absolute majorants and both boundary contributions.

The proof converts logarithmic neighborhoods into actual short intervals;
this case was read because the target has integer square endpoints.
No error constant or specialization was derived or imported.

Read the abstract, Theorem1.1, Note1 and proof's weighted-to-Lebesgue
measure passage (3.1) in the [author addendum](https://ramare-olivier.github.io/Maths/TruncatedPerron-5-Addendum-04.pdf),
dated 3 October2021, pp1-4. It flags the measure qualification for the
2016 good-height statements and a missing parameter dependence, naming
Theorems1.2/5.3. The new bounded-coefficient theorem assumes |a_n|<=1,
1<kappa<=3/2, 0<epsilon<=delta<=1/2 and x>=T>=2.
No such uniform coefficient normalization has been established for a
twice-inverted GC12 expression. Do not import a simultaneous good-height
choice from this result. The simpler fixed-height Theorem1.1 is enough
as a possible tool; its cutoff errors remain unpaid.

### Mellin inversion: smoothness must be checked on the actual kernel

E. Kowalski, [*Number Theory I*, author lecture notes](https://people.math.ethz.ch/~kowalski/number-theory.pdf),
AppendixA.3, PropositionsA.3.1-A.3.2 and their Fourier-change-of-variable
and integration-by-parts proofs, inspected 21 November2026 (printed
pp148-150 in the retrieved passage). The unversioned PDF returned
different page counts on successive retrievals; identify the propositions,
not an assumed stable PDF page number. No old source is silently refreshed.
The smooth rapidly decaying input gives inversion on positive vertical
lines; the rapid-decay result assumes the same decay for all derivatives.
No assertion near a Mellin pole is needed or imported.

The actual weight is exactly w_Q(r)C_h(r), with its |r| prescription,
support endpoints and unmodified correlation. Smooth compact support
of h does not itself verify every regularity or vertical-growth hypothesis
for that weight and its cutoff representation. Those checks belong to
the mathematical attempt. This theorem is supporting technique, not
coverage of cancellation, an arbitrary contour shift or a GC12 upper.

### Van Hemert: exact interface and remaining source-audit limits

L. van Hemert, *Exact Zero Detection and Compact Arithmetic Realizations
for the Riemann Xi Function*, v1.0.0, 11 October2026,
DOI10.5281/zenodo.23295277,
[tagged paper.tex](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex).
Reuse source-notes2080's full GC12-GC18 and fixed-band reading, and
C034r's audited FB specialization. Refreshed displayed portions of the
GC12/GC13 statement, GC15/GC16 square and cap formulas, GC17 squarefree
count and endpoint discussion in source lines11613-11702. A targeted text search
found no literal `two-variable` statement. It is not a proof of absence.

GC13 retains 1<=K<=X and its X^-1/2 K^3/2 log^2(2K) error;
GC18 leaves signed primitive-sector estimates open. That error does
not estimate a new Mellin contour truncation. No theorem of automatic
residue cancellation for GC12 was located in these inspected passages.
The source's arithmetic decomposition remains unaudited locally.

## Queries and access record

Queries included `"coprime" "Möbius" "double Dirichlet"`,
`"Mobius" "coprime" "Euler product" "zeta"`,
`"riemann-xi-zero-detection" "Mellin"`,
`multivariable Euler products Mobius coprime meromorphic continuation
Bhowmik Essouabri Lichtin theorem`,
`"coprime" "Möbius" "Mellin" "double"`,
`"coprime" "p+1" "Dirichlet" mobius`,
`"coprime" "Mobius" "two-variable" "zeta"`,
`"Möbius" "ratio" "double sum" Mellin`,
`"coprime" "Mobius" "Dirichlet series" "two" Mellin kernel`,
and targeted truncated-Perron/Mellin-inversion/addendum searches.
No adequate exact match emerged. Search snippets, generic RH claims,
aggregator summaries and other repositories were not theorem evidence.

The AMBP direct site returned403; the published Numdam PDF and author
addendum were accessible, so this is no persistent source blocker.
Newton's lec1.pdf returned404; accessible author Mellin notes supplied
the supporting comparison. No access campaign, API key or download
script was used. The already reviewed Ramaré--Zuniga-Alterman2603.25961
PDF was accessible; a `Perron` text search found no matching passage.
Its previously assessed lcm theorem was reused, not newly imported.

## Decision and continuation boundary

EXPLORE is justified by this bounded theorem comparison, without a
novelty claim. General zeta-factor extraction is covered known technique;
the proposed integrated cancellation is not established by the sources
checked. No original factor, residue, noncancellation or upper was proved.
This step adds source readiness, not mathematical progress beyond the
sources or a new partial proof of RH. No canonical input was imported;
PROOF.md and DAG.md therefore stay unchanged. Full matching Mathlib
coverage was not checked and is not claimed absent.

One later mathematical attempt is justified on the unchanged target.
It must first establish the exact arithmetic representation in an absolute
region, then track one hypothetical off-line zero with arbitrary finite
multiplicity through the actual ratio integration and square cutoff.
A proved surviving integrated principal part rejects automatic removal,
not RH or automatically the one-sided upper. A local arithmetic pole
without the integration/cutoff analysis is insufficient. Cancellation
without global contour error payment is partial progress only. The
high primitive complement, scale choice, full source-energy upper and
actual mixed positivity remain unresolved whatever this test finds.

No separate new ready target is introduced. Assessment2081 keeps its
exact TARGET and now records the inspected coverage for separate
supervisor approval next turn. Recommend creative proof work only for
the integrated cancellation question; routine factorization is a
preliminary calculation, not the claimed creative achievement.
