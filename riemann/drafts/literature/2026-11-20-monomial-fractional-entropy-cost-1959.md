# Monomial fractional-entropy cost nomination1959

TARGET: Evaluate the numerator-only fractional-moment upper-payment cost on T_d(y)=y^d over [-Ad,Ad], for q=q_d in (0,1], and determine exactly when its excess divided by d vanishes before the large-A limit.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1959 checked scoped entropy/height/theta/Jensen records, C028a/c, and monomial/fractional filenames; existing reference-cost stops concern different norms. Exact source queries and qualifications are in drafts/literature/2026-11-20-theta-entropy-source-notes-1959.md. No novelty is claimed.
SOURCE_EVIDENCE: Lacker-Mukherjee-Yeung [arXiv:2206.01260v1](https://arxiv.org/pdf/2206.01260v1) (2 June2022), Theorem3.3/(3.1)-(3.2), full proof printed pp13-14, provides the bounded-above variational interface; use ordinary Jensen's inequality for log and elementary power/log integrals, not its quantitative strong-concavity theorem. No Carbery-Wright theorem is needed or approved.
COMPARISON: Finite scalar specialization of known inequalities tests whether a numerator-only entropy bound creates an excessive baseline cost before actual theta coefficients enter. C028d's identity and C028e's exterior estimate do not evaluate that cost; C028a/c's orthogonal norms are distinct. A small reference cost would not bound the actual-family partition function.
GAP: Compute exact finite-degree excess and its dependence on q_d, d and A, treating the logarithmic singularity. Nothing is evaluated in this nomination; source coverage asserts neither vanishing nor an actual-theta bound.
REASON: Independently test the generic comparison after parking automatic entropy transfer. No signed-polynomial representation, real-root theorem, numerical theta data or inaccessible source is required. Newly written assessment requires separate approval before mathematical invocation.
SCOPE: Integers d>=3, fixed real A>=max(1,2sqrt(M)) with M from C028e, q_d in (0,1], uniform probability nu_(A,d) on [-Ad,Ad], and reference T_d=y^d only. REPRODUCTION; no creative or actual-Xi bound is preapproved.

## Exact proposed diagnostic and discriminator

Define, without evaluating,

    E_(d,A)(q) = (2 A d^2/q)
                  log(integral |T_d(y)|^(q/d) dnu_(A,d)(y))
                - integral_(-Ad)^(Ad) d log|y| dy.

Values at zero are understood almost everywhere. Verify the numerator-only
upper-comparison direction using Jensen, the probability normalization
and all factors of d, and integrate the logarithm across zero as an
ordinary improper/Lebesgue integral. Evaluate E exactly and classify
sequences q_d for which E/d -> 0 for every fixed A, with outer A last.
Do not reprove source theorems. No script or lemma is required unless
the resulting argument warrants a canonical record.

If fixed positive q leaves a nonvanishing normalized reference cost,
close only that fixed-q rule. If shrinking q escapes, state the precise
rate and additional actual-polynomial estimate still needed. Escaping
reference cost does not pay C028d. A large upper-bound cost does not
lower-bound actual H_d. Stop after this diagnostic; actual-family
optimization needs separate coverage. No formula is evaluated here.

Full matching Mathlib coverage is unchecked/unknown. No new theorem,
actual positivity or RH conclusion is asserted.

## Separate source-link approval1960

20 November2026; literature-only recovery for the unchanged TARGET.
The primary versioned PDF above was opened successfully; its arXiv
record https://arxiv.org/abs/2206.01260 confirms the authors, title,
submission date and sole v1. Reuse the full Theorem3.3 statement/proof
inspection recorded in source-notes1959, rather than repeating it.
The missing direct URL is now in SOURCE_EVIDENCE itself.

For the diagnostic's actual inequality input, the author-written
textbook appendix [Marco Taboga, Jensen's inequality (2021), Statement
and Example](https://www.statlect.com/fundamentals-of-probability/Jensen-inequality)
was read: integrability of the variable and its transform is required;
concave functions reverse the convex inequality, and the logarithm is
its stated positive-variable example. This is ordinary Jensen coverage,
not an actual-polynomial partition estimate. The future calculation must
check positivity almost everywhere, the zero's null measure, logarithmic
integrability and normalization; none is calculated in this repair.
Elementary power/log integration remains a routine specialization, not
a claim imported from the quantitative entropy theorem.

Approval: retain SPECIALIZE for the exact saved target and scope. This
separate review repairs source traceability and approves only the
reference diagnostic. No cost formula, sequence threshold, new lemma,
actual-family estimate or Mathlib matching theorem is established.
The ready-target comparison itself is unchanged; outcome STALLED for
this process repair, without claiming new mathematical evidence.
