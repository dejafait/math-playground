# Finite local factor coefficient comparison — source-scope approval

TARGET: Critically audit the uniform finite-local-factor coefficient comparison in bramble_trace v4 Section 4.3, equations (18e)-(18h), including central zeros and repeated roots.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the initial-sign and L463 application assessments; searched local audit notes, L255/L260 and the finite-sign failure records. Two targeted external query pairs located the source and discussion but no inspected stronger substitute. Complete Section 4.3 and the primary local-count statement/proof were read for this scope.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, https://rstation.ai/problems/riemann_hypothesis/papers/41, displayed v4, 24 October 2026 07:18 UTC, definitions (1)-(2), Section 4.3 (18c)-(18h), Section 4.4; Titchmarsh, second edition (1986), Theorem 9.2, (9.2.1), printed p. 211, statement and Jensen proof; canonical L018/L024/L026/L027/L255 read on 25 October 2026.
COMPARISON: The exact source already states the comparison and an unconditional log-squared coefficient tail. L255 covers the conjugate-factor algebra on a compact interval, not this arbitrary-center split; L463 checks only application of the broader conditional theorem. Independent verification of the source's uniform product estimates is the sole justified reproduction, not a new positivity theorem.
GAP: Source coverage is sufficient for the exact saved audit. Its mathematical checks remain undone: coefficient-limit passage, finite-factor remainder, positive normalization at central zeros, multiplicity counts, uniform shell estimates and common absolute tail constant. Growing-radius saddles and the external zero-free theorem remain outside scope.
REASON: Approve one separate critical audit as REPRODUCTION to check a previously unaudited load-bearing source estimate. No source blocker or missing sign premise was found in the stated hypotheses; this is source-scope approval, not an audit verdict.
SCOPE: Exactly the saved TARGET; actual Xi, real t>=2, all multiplicities and central zeros, every integer p in (18h), no simplicity or central-value denominator. Section 4.3 itself is unconditional. Retain L463's separate strict Re(s)>7/8 premise and unaudited manuscript/import-closure qualification for its broader conclusion.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination lacked the exact finite-factor estimate and essential primary local-count citation. Existing application coverage expressly excluded verification of those estimates, so this turn resolves that source scope without repeating the earlier import audit.

## Gap, intermediate target and decision test

The main gap remains initial actual-Xi signs at unbounded heights,
effective overlap with bounded heights, and global mixed positivity.
The intermediate target is the exact audit named above. Its downstream
use would be a checked product-tail component of L463, with the other
analytic components still unaudited. Continue if the complete uniform
comparison can be audited from named inputs; report a precise failure
or narrow the conclusion if normalization, multiplicity, limits or
uniformity fail. Do not infer initial signs from an eventual order tail.

The source-access test passes. This completes the missing literature
gate for the unchanged saved target; the next invocation may perform
the mathematical audit. No new lemma, proof verdict or calculation is
produced in this turn. The earlier nomination's REVIEW_REQUIRED state
is superseded by this separate source review, not retrospectively treated
as prior permission to do mathematics.

## Exact source case for the later audit

Primary manuscript: [bramble_trace, v4, Section 4.3](https://rstation.ai/problems/riemann_hypothesis/papers/41),
version/date checked 25 October 2026. The following records its claims,
not independently established conclusions.

Set G=product_i(1+u_i x+v_i x^2)=sum_j g_j x^j, with infinitely
many positive-degree factors, u_i>0, 0<=2v_i<=u_i^2 and U=sum_i u_i<infinity.
For monic real B of degree M>=1 with root moduli <=R_0, (18e) asserts

    |coeff_p(BG)-g_(p-M)|
      <=g_(p-M)((1+R_0 U/(p-M+1))^M-1),  p>=M.

Its premise is j g_j<=U g_(j-1), (18d); positivity follows when
p-M+1>=2R_0 M U. M=0 is separate.

For x=y^2, (18f)-(18g) split the product as C_t B_t(x)G_t(x), C_t>0:
near factors have |gamma-t|<2, including multiplicities; all gamma+t
factors are far. Real factors are x+a^2; nonreal factors are

    x^2+2(a^2-d^2)x+(a^2+d^2)^2,  0<d<1/2.

The stated bounds are R_0=17/4 and M,U_t<<log(t+2). Far normalization gives

    u=2(a^2-d^2)/(a^2+d^2)^2, v=1/(a^2+d^2)^2,
    u/sqrt(v)>=30/17>sqrt(2).

Here coeff_p denotes the coefficient of x^p. The source claims positive
convergent C_t without dividing by Xi(t)^2, and one absolute C with
L_p(Xi;t)>0 for every p>=C log^2(t+2), t>=2,
in (18h). Repeated and zero local roots are permitted.

## Classical input and local overlap

[Titchmarsh, second edition, Theorem 9.2, (9.2.1), printed p. 211](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=110)
states N(T+1)-N(T)=O(log T) as T tends to infinity, where N counts
zeros in 0<=Re(s)<=1, 0<Im(s)<=T with multiplicity. The primary
definition, theorem, full Jensen-circle proof and following fixed-h
and multiplicity remarks were inspected. This is an unconditional
local count, not an off-line-zero density estimate. Readable text and
the PDF page were requested. Extension to bounded heights and the
shell summation remain checks for the mathematical audit, rather
than consequences silently added here.

L024 supplies the exact paired product and reciprocal-square
summability; its proof treats compact sets containing zeros without
a global logarithm. L018 supplies the completion and symmetries;
L026 excludes imaginary-axis zeros and supplies the strict strip.
L027 supplies infinitude. These were read as existing canonical inputs,
without re-auditing their foundations. L255 already reproduces the
conjugate-block algebra and a locally uniform coefficient-limit method.
The changed task is an arbitrary-center uniform finite/far comparison,
so compact L255 alone does not settle it.

The [initial-sign comparison](2026-10-25-initial-laguerre-sign-coverage.md)
and [L463 application assessment](2026-10-25-l463-import-audit-coverage.md)
remain valid within their narrower scopes. Recorded finite-level,
first-sign and count/gap failures were checked by targeted searches in
the September 23 and 27 attempt files. They block sufficiency shortcuts;
they are not inputs to this source comparison. The completed L260 audit
remains intact, including its simplicity obstruction.

## Bounded audit obligations and exclusions

The audit should verify the coefficient inequality through complete
finite products and the locally uniform limit, then the full finite-B
remainder including zero roots and M=0. It should verify the exact
paired-product constants without central-value division, the allocation
of both ordinate partners, and uniform control of every shell with
multiplicities before checking (18h)'s single absolute constant.
The source's reported participant checks and finite models are evidence
of prior attention, not substitutes for these proofs.

Only this product component is approved. Sections 4.2 and 4.5 require
their own uniform analytic estimates; no approval or reproof of those
or the September zero-free manuscript follows. Do not claim effective
overlap, endpoint uniformity, initial signs, mixed positivity or RH.
Full matching and supporting Mathlib coverage remain unchecked; no
absence assertion is made. A successful reproduction belongs in a
canonical lemma file in the later research turn, with precise source
citation and all qualifications.

## Search record and review outcome

External queries on 25 October 2026 were:
- coefficient polynomial positive tail G Laguerre zeros
- "Generalized Laguerre positivity at growing orders" "18e"
- "Titchmarsh" "Theorem 9.2" "N(T"
- "coefficient" "R_0" "bramble_trace"

The source discussion appeared as a lead; its independent-check report
was read only in the manuscript's closing notes. The discussion was not
independently inspected and supplies no mathematical input. Unrelated
search results supply no coverage; a failed search proves no novelty.
No all-notebook scan or cross-notebook input was used.

Outcome: EXPLORATION for new source-scope extraction and comparison,
not a mathematical advance or a repetition of an already adequate
audit assessment. The exact next target stays unchanged and is now
ready under SPECIALIZE for a bounded REPRODUCTION proof audit.
