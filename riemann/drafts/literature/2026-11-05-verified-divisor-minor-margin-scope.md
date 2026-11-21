# Verified zero divisor and an actual minor margin — source comparison

TARGET: Assess whether a finite verified negative-real-zero divisor and Cauchy–Binet give an explicit positive lower bound for the actual D_(6001,6000), without assuming hybrid regularity.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step663 searched finite-zero-divisor/Toeplitz lower bounds, PF convolution and strict minors, and Cauchy–Binet total positivity; inspected Pinkus's publisher excerpt and the exact Platt–Trudgian count. Narrow local duplicate/failure comparisons and ready sector/product and Jacobi–Trudi assessments are recorded below; no novelty inference is made.
SOURCE_EVIDENCE: Pinkus, Totally Positive Matrices (2010), Definition1.1 and finite Cauchy–Binet formula Section1.1 pp.2–3, Proposition1.4 p.6, https://assets.cambridge.org/97805211/94082/excerpt/9780521194082_excerpt.pdf ; Platt–Trudgian 2004.09765v1 Theorem1 and Section2 pp.2–3, https://arxiv.org/pdf/2004.09765v1 ; Katkova math/0505174v1 Definition2/(8), Theorem B and full short Theorem1 product passage pp.4–6, https://arxiv.org/pdf/math/0505174v1 .
COMPARISON: Standard finite Cauchy–Binet and sector-product coverage supply the needed method, and the published positive-height count exceeds6000; individual zero enclosures are unnecessary for a floor depending only on the certified common height. No inspected source states the exact local quantitative floor. L832 supplies signs only; the existing reciprocal-duality import and hybrid-ratio stop do not supply this margin.
GAP: A separate application must verify finite convolution support, ordered index sets, a degree6000 genuine divisor without reflection double-counting, sector/product applicability to its entire residual, positive constant and the selected summand's explicit floor. No inequality for this actual minor is proved in this review.
REASON: Essential source coverage is now adequate for one bounded standard specialization. An actual-minor floor could anchor a later absolute perturbation test; it neither establishes the parked reference/cofactor ratio nor addresses all orders.
LITERATURE_REASON: The changed target asks for strictness and an explicit lower bound from a finite zero divisor; the ready PF6001 assessment covers only nonnegative signs and excludes determinant margins.
SCOPE: Completed literature comparison only. The new mathematical continuation is nominated separately in 2026-11-05-verified-divisor-minor-margin-application.md and requires separate next-turn approval. No lemma, mathematical script or source reproof is authorized by this completed review.

## Completed source review — step663

The main gap remains actual-Xi all-degree mixed positivity. The bounded
intermediate question is a strict actual D_(6001,6000) floor. Its plausible
downstream use is a comparison with an independently proved absolute
perturbation error. No such error or adequate comparison is established.
Continue only to a fully specified positive floor under verified inputs;
stop on an unpaid residual sign, factor certification or support case.

**Finite composition input.** Allan Pinkus, *Totally Positive Matrices*,
Cambridge Tracts in Mathematics181 (Cambridge University Press, 2010),
Section1.1, pp.2–3, gives finite Cauchy–Binet for arbitrary rectangular
factors with increasing equal-size row, column and intermediate sets.
The minor size cannot exceed any relevant dimension; an empty
intermediate-set collection gives zero. Definition1.1 uses TP for
nonnegative minors and STP for strictly positive minors. Proposition1.4,
p.6, imports preservation under products; its strict branches assume
an STP factor and specified rank/dimension conditions. They cannot be
invoked merely from two nonnegative factors. The relevant complete
formula, dimension/empty cases and both strict branches were read.
Use the finite formula itself and verify one positive summand; no
strict-factor or invertibility assumption is needed for that formula.
No infinite Cauchy–Binet identity is imported.

**Enough certified factors.** Dave Platt and Tim Trudgian, *The Riemann
hypothesis is true up to 3 times10^12*, Bull. London Math. Soc.53
(2021), 792–797; inspected arXiv:2004.09765v1, Theorem1, printed p.2,
states the height H=3,000,175,332,800 and the count
12,363,153,437,138 lowest nontrivial zeros on the critical line.
The introduction defines this as positive heights 0<gamma<=H.
Section2, pp.2–3, explains sign-change detection with Turing counting
and interval/ball arithmetic, including why high-precision individual
zero locations were not retained. This aggregate theorem supplies
more than6000 positive-height zeros. The future application may select
6000 with multiplicity and use their common upper height, rather than
claiming certified decimal ordinates. It must verify that positive
heights supply G factors once each, and not count the reflected
negative-height xi zeros as additional factors. Simplicity is unnecessary.

**Residual coverage, not PF division closure.** Reuse the ready
[sector comparison](2026-11-05-verified-height-pf6001-scope.md) and L832.
Rechecked Katkova's versioned Definition2/(8), Theorem B and the whole
short Theorem1 product-limit argument on printed pp.4–6. Theorem B
requires a real polynomial, positive constant and exclusion of the open
sector of angle pi*m/(m+1). The product passage uses positive constant,
order one-half, reciprocal-zero summability, compact product convergence
and fixed coefficient minors. This supplies the standard method for
the residual after deleting finitely many actual negative-real factors;
the application must check its hypotheses afresh, retain multiplicities
and conjugate grouping, and retain the positive constant. PF6001 of G
alone is not a quotient-closure theorem. Do not import the printed
PF44 index inference, already excluded by L832. Schoenberg's original
proof remains unread; cite its theorem as reproduced in Katkova.

**Comparison and scope.** Narrow searches in November5 literature,
L8xx files and named attempts found the assessed reciprocal
Jacobi–Trudi identity, not a matching actual divisor margin. Reuse
[that comparison](2026-11-05-reciprocal-minor-duality-comparison.md):
its scalar duality supplies no independent positive alphabet. No new
Jacobi–Trudi derivation is needed for the proposed finite composition.
[Step659](../../ATTEMPTS/2026-11-05-first-hybrid-corner-unpaid-ratio.md)
remains an unpaid hybrid ratio, so an actual floor cannot close it alone.

Queries included `total positivity Cauchy Binet product Toeplitz Polya
frequency finite zeros strict positivity Schur polynomial`, `Toeplitz
minors lower bound zeros Cauchy frequency`, `Polya frequency convolution
strict minors`, and `xi Toeplitz divisor lower bound`. Broader symmetric
function hits were unnecessary once the finite composition source was
available. A secondary hit titled *Coefficient Dynamics and Consecutive
Toeplitz Minors for the de Bruijn–Newman Family* linked identifier
2610.00521v1; the primary arXiv page is instead a quantum-simulation
paper. Discard that mismatched lead; no theorem is imported from it.
Failure to find an exact quantitative theorem establishes no novelty.

The publisher's Pinkus excerpt was accessible after a separate book
landing-page error. No essential source remains blocked. A coarse floor
using H and G(0)=xi(1/2)/8 is the next proposed threshold, not a theorem
proved here. Its finite support/index and quantitative calculation are
reserved for the separate specialization. Mathlib matching coverage is
unchecked. No all-order signed mechanism is ready; this is routine
specialization, not a creative central-gap attempt. Earlier exploration
and stop evidence remain unchanged.

## Original nomination (historical; source gate completed above)

The main gap remains actual-Xi all-degree mixed positivity. The proposed
intermediate target concerns only the actual D_(6001,6000) with the
ordinary coefficients of L018/L021/L776 and L832. A source comparison
must first determine whether the proposed divisor method is a standard
quantitative specialization, has a stronger ready substitute, or fails
its residual/sign hypotheses. There is no mathematical claim here that
the residual is PF6001 or that the proposed lower bound is useful.

Inspect exact primary hypotheses before any derivation. Check the
Toeplitz orientation, allowable Cauchy–Binet index sets, coefficient
convolution, repeated roots, a finite certified negative-real divisor,
and the entire residual with its positive constant. Never enumerate
both reflection-related xi zeros as different G zeros. Record whether
verified-height coverage alone supplies sufficient explicit factors,
or whether additional certified zero enclosures are essential.

Continue to an applicability attempt only if a precise known theorem
or an assessed difference can produce a fully specified L>0 with
D_(6001,6000)>=L under verified inputs. Abandon this target if its
argument needs an unknown minor sign, an uncontrolled residual, or
uncertified factors; record an informative obstruction rather than
calculating a dense determinant. A very small bound may establish
strictness but does not on its own meet any perturbation threshold.

Essential inputs for that future comparison are L832, the definitions
in L018/L021/L776, and the precise step659 stop in
ATTEMPTS/2026-11-05-first-hybrid-corner-unpaid-ratio.md. No use of a
hybrid-matrix sign, nonvanishing, cofactor size or regularity is allowed
as an established assumption. Strict bounds for that reference,
cofactor comparison, all higher-order signs and RH remain unresolved.
No cross-notebook input is proposed; Mathlib coverage is unchecked.

This nomination is not an approved creative mechanism at the central
all-order gap. Known quantitative coverage must be checked first;
an independent all-order signed mechanism is still missing.
