# Width Newton constructor: source comparison1824

TARGET: Assess whether a rational Newton inverse-square-root constructor can replace C033z's width bisections on 1<=w<=2^30 with absolute error <=2^-60 in at most100 defined operations per width.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact rational inverse-square-root Newton convergence, reciprocal-square-root100-operation bounds and2^-60 accuracy; inspected Brent-Zimmermann's exact error theorem and Kornerup-Muller's seed-analysis qualifications. Scoped local searches found C033z's bisections and execution1823, but no prior Newton width-constructor proof in the searched route files.
SOURCE_EVIDENCE: Brent-Zimmermann, Modern Computer Arithmetic, v0.5.9(2010-10-07), Lemma3.14 and proof, printed p112, Algorithm3.9/Lemma3.15 pp112-114, and Section4.2.3(4.9), p129; Kornerup-Muller, DOI10.1016/j.tcs.2005.09.056, author-hosted uncorrected proof, Section1 pp2-3 and Section2 pp3-4, especially(3)-(6).
COMPARISON: The inverse-root Newton method and a rigorous exact one-step error theorem are established inputs. Neither inspected source supplies this notebook's uniform rational initialization, absolute2^-60 bound and complete<=100-operation ledger; the integer/rounded implementation and approximate seed optimization cannot be imported as that certificate.
GAP: Specialize the cited exact error theorem using an explicitly charged rational initializer and normalization, prove all iterates satisfy its hypotheses, and give a uniform stopping index and complete ledger. No initializer, iteration count, uniform error or<=100-operation theorem is proved in this literature turn.
REASON: Essential coverage was missing for a changed constructor outside unchanged-GMP/Ihat-only assessments. The source comparison now supports one bounded numerical specialization attempt, without claiming new numerical mathematics, runtime improvement or an RH advance.
SCOPE: Exact positive rational widths in[1,2^30]; rational +,-,*,/,comparison model of C033z. Only width inverse roots and their existing input-perturbation/clamping interface are covered; rounding other quantities, running the evaluator and a new global cost theorem are outside scope.
COVERED_TARGET: Construct and prove a rational Newton inverse-square-root replacement for C033z's width bisections on 1<=w<=2^30 with absolute error <=2^-60 using at most100 defined operations per width, including initialization and comparisons.

## Inspected primary results

[Richard P. Brent and Paul Zimmermann, *Modern Computer Arithmetic*,
version0.5.9](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf),
Lemma3.14, printed p112 (PDF p128): for a,x>0, rho=a^(-1/2),
and x'=x+(x/2)(1-a*x^2),

    0 <= rho-x' <= (3*x^3/(2*theta^4))*(rho-x)^2,
    theta in[min(x,rho),max(x,rho)].

Its proof uses Taylor's theorem for f(t)=a-t^(-2). Section4.2.3,
(4.9), p129, identifies the same iteration. This is an exact-arithmetic
input, with no assumed floating-point precision. Algorithm3.9 and
Lemma3.15, pp112-114, instead concern integer radix data, beta>=38,
floor/rounding operations and a base case containing a square root.
Those algorithmic hypotheses and primitives do not match our model.

[Peter Kornerup and Jean-Michel Muller, *Choosing starting values for
certain Newton-Raphson iterations*](https://perso.ens-lyon.fr/jean-michel.muller/TCSNewton.pdf),
DOI10.1016/j.tcs.2005.09.056, author-hosted **uncorrected proof**;
published in *Theoretical Computer Science*351(1)(2006),101-110.
Inspected Section1, proof pp2-3, and Section2, proof pp3-4. The paper
includes inverse-square-root iteration as p=-2 in(3). For p!=-1,
its optimization analysis following(4) discards higher-order terms
under a small-interval assumption; its ensuing error model is approximate.
These inspected passages do not certify our uniform bound. The paper's
bit-addressed seed-table discussion is also outside the permitted primitives.
No later optimal-seed theorem is imported.

## Local comparison, duplicates and failure evidence

The required local mathematical inputs are C033z's input contract and
operation model, and its1802 width construction(15)-(17). At each of260
outer nodes it forms three rational widths what=sigma+Ehat/4. The existing
proof bounds the width-input error by2^-122, its contribution to the
inverse-root error by2^-123, and the64-bisection error by2^-65. The original
contract requires only absolute error2^-60; panel-dependent clamps must
still preserve the final contract. The endpoint/range premise1<=what<=2^30
must be justified from that construction in the later specialization,
including any equality case. This review does not alter(17) or assert a
new total error margin; using the whole2^-60 allowance on what alone
would leave its input perturbation unpaid.

Scoped searches covered lemmas/C033*, drafts/literature/*direct-positive*,
drafts/literature/*width*, ATTEMPTS/*direct-positive*, and history/*gmp*;
the further reading was C033z's hypotheses and1802 width ranges, plus
history/2026-11-19-gmp-remaining-execution-1823.md. The other local Newton
mentions concern interpolation/Hermite methods, not inverse roots. This
bounded search establishes no novelty claim.

The recorded execution stop is operational:15/780 profiles,0/8 scalars,
and only six profiles independently replayed in1823b. It is neither a
Newton impossibility theorem nor a bit-complexity lower bound. Preserve
all1816/1823/a/b evidence and leave the unreplayed suffix unverified.
The proposed constructor uses the width contract, never those saved
numerical values. Its purpose is possible algebraic-operation slack for
a later separately assessed rounding scheme; an operation saving alone
does not control denominator growth or runtime.

## Search scope and unread leads

Queries included “reciprocal square root Newton iteration convergence
initial approximation”, “inverse square root exact rational Newton
convergence”, “reciprocal square root Newton100 operations”,
“reciprocal square root Newton2^-60”, and the Kornerup-Muller title.
No exact matching<=100-operation theorem was established by this search.
Generalizing the fast reciprocal square root(arXiv:2307.15600), correctly
rounded Newton steps(arXiv:2112.14321), and seed-hardware papers appeared
as leads only; their theorem statements/proofs were not inspected or used.
The MDPI secure-fixed-point article URL returned a non-theorem page to
the browser; its appendix is unread and nonessential because the exact
error input above is accessible. Search snippets supply no premise.

## Approved scope and bounded continuation test

The newly covered continuation is a **specialization attempt**, not a
proved construction. It receives the supervisor's separate approval on
the next turn. Import Lemma3.14 by precise citation; prove only the local
initialization, invariant, accuracy propagation and counted-operation
specialization that the sources do not supply. Do not reprove Newton's
general theorem. Retain the original accuracy target, but reserve/pay
the existing width-input perturbation when using the result in C033z.

Required decisive evidence is a uniform proof on the whole rational
interval, including normalization boundaries, and a ledger counting
every required arithmetic operation/comparison, constants formed at
runtime, rescaling, and clamping needed by the stated interface. Bit
access, floor, integer quotient, library sqrt and fused operations are
not free primitives. Continue only if the simultaneous error/cost test
passes. If a proposed initializer fails its invariant or the complete
ledger exceeds100, reject that proposed implementation without weakening
the target or reopening repetitive unrounded execution. A failed choice
does not establish that every Newton constructor is impossible.

Essential downstream inputs remain C033y(1)-(8), C033z(1)-(37),
C033w/u and C032s/q/w/j. Conditioning, weights, TV<=2, observation
coverage, signed-height cancellation and actual-Xi realization remain
independent gaps. Preserve divisor/conjugation/multiplicity, excluded
ordinate0, strict strip/gamma>14, counting/real-zero/tail assumptions,
heat positivity and separate errors, both fixed-v1 qualifications,
zero drift/killing and Gaussian half-variance. Source-wide correctness
and Mathlib coverage of the larger construction remain unverified.
The full matching Mathlib theorem for this new finite-operation contract
was not checked. This routine numerical specialization is not a central
creative RH mechanism; no independently justified signed-height/actual-Xi
input was found in this narrowly scoped source review.
