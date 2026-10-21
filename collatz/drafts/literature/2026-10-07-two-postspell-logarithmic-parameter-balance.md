# Two-postspell logarithmic parameter balance — completed source assessment

TARGET: Assess a conditional logarithmic upper bound on min(J_1,J_2) in terms of N for closed two-postspell words, using L035, actual-prefix congruences and an explicit lower bound for N log(2)-K log(3).
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted two-logarithm, cycle run-length and repeated-word searches completed; relevant L020/L024/L031/L034/L035 ranges, Attempt 019, history 069 and prior cycle/reciprocal assessments checked; queries and inspection limits below.
SOURCE_EVIDENCE: Simons–de Weger, Acta Arith. 117 (2005), 51–70, section 1.2 p. 52, Lemma 8 and full proof p. 59, Lemma 12 and full proof plus Corollary 13 p. 61; author v1.44 (2010-08-31), sections 1.2–1.3, Lemmas 7/8/12/14 and relevant proofs, Theorem 3(d); Rozier–Terracol v2 (2025-02-13), Proposition 6.3 and surrounding conditional application; Hercher coverage reused.
COMPARISON: The published Lemma 12 supplies the needed explicit positive linear-form lower bound for the same cycle counts, including nonminimal periods; no inspected source states the proposed two-postspell min(J_1,J_2) restriction. L031 already supplies the general-tail boundary valuation missing from L024's E^2 scope. The remaining combination is a specialization of known estimates, without an originality claim.
GAP: Establish explicit absolute A,B for the proposed necessary bound by combining the cited lower estimate with L035 and a justified positive-height consequence of L031's valuation identities; retain offsets, independent tails and repeated periods. This bound is not proved in this assessment.
REASON: Missing lower-bound and actual-tail scope coverage is now resolved through a published Collatz lemma and canonical L031; approve one later guarded mathematical test at the unchanged target, without redoing transcendence theory or general parity coding.
SCOPE: Actual closed two-postspell language of L035, J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n,x, n>1 and exact tails, N=4(J_1+J_2)+H_1+H_2+a_1+a_2; allow repeated periods and independent unbounded parameters. Coverage is for a necessary logarithmic min-parameter bound, not cycle exclusion or a total-length cutoff.

The main gap is universal eventual descent. The intermediate target remains
an explicit conditional restriction min(J_1,J_2)<=A log(N)+B. Its plausible
use is to narrow the parameter regimes relevant to integer closure.
Unbounded asymmetric words, positive integer closure, other cycles,
divergence, entry into this language and descent would remain unresolved.
This literature turn establishes source readiness only: no constants for
that restriction, new lemma, mathematical calculation or script are supplied.

## Exact source input and applicability

John Simons and Benne de Weger, *Theoretical and computational bounds for
m-cycles of the 3n+1 problem*, [Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
Lemma 12, printed p. 61, gives

\[
\Lambda=(K+L)\log 2-K\log 3
 >\exp[-13.3(0.46057+\log K)].
\]

Here K,L count odd/even inputs of a positive nontrivial shortcut cycle.
Section 1.2, p. 52, explicitly permits a nonminimal period. Lemma 8 and
its proof, p. 59, use the source's computational cycle-height input;
Lemma 12's proof invokes Rhin's Proposition, p. 160, with coefficients
u_0=0,u_1=K+L,u_2=-K, together with Lemma 8. These complete proof
passages were inspected. Import Lemma 12 itself, including its published
inputs; no independent verification of those computations is claimed.
The [author manuscript v1.44, dated 2010-08-31](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
pp. 2–3/9–11, has the same Lemma 12 and records X_0=5*2^60.

L035 already identifies the same K,L and N=K+L, with K>0. Its actual
closure is positive and nontrivial; n is an odd residue-20 integer greater
than 1, outside {1,2}. Its represented starting boundary is a local
minimum, as checked in L034. Thus the source applies with the represented
counts; no primitive-period or distinct-junction hypothesis is added.
One may retain L034's primitive-period convention for other imported
cycle theorems, but must not replace the represented N or K silently.

The decimal constants above are the stated theorem constants. The later
proof must keep the distinction between K and N and preserve strict signs.
It may invoke this bound directly by citation. Reproving Rhin's theorem,
Matveev's theorem or general cycle-product inequalities is unnecessary.
The desired min-parameter restriction is still an unproved specialization.

## Primary source limits and stronger-result comparison

Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, in
*Séminaire de Théorie des Nombres, Paris 1985–86*, Progress in Mathematics
71 (1987), 155–164, Proposition p. 160, is the cited original input.
The [publisher chapter record](https://link.springer.com/chapter/10.1007/978-1-4757-4267-1_11)
was read; the full PDF required unavailable access. The author-uploaded
ResearchGate PDF link also failed. The original proposition and its proof
remain unread. This does not block importing the fully stated published
Collatz Lemma 12; it precludes claiming a fresh audit of Rhin's proof.

Rozier–Terracol, [*Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2#S6),
13 February 2025, Proposition 6.3, reproduces Rhin's integer-coefficient
bound |u_0+u_1 log2+u_2 log3|>=H^(-13.3), with
H=max(|u_1|,|u_2|)>=2. Its 7.616 variant has a further effectively
computable threshold whose numerical value is not supplied there.
The proposition and its surrounding application were read. That application
assumes their Conjecture 6.2 on delay and excursion: those assumptions are
not imported. The 7.616 estimate is not needed for this target. Use the
published Lemma 12 above as the load-bearing input, rather than treating
this restatement as an independent inspection of Rhin's original proof.

Simons–de Weger's v1.44 Corollary 13, Lemmas 7/14 and relevant proofs,
and Theorem 3(d) were checked against the prior assessment. Their bounds
retain the full local-minimum count m and m-dependent constants/ranges;
they do not give the requested parameter balance by simply setting m=2.
Hercher's Theorem 23 supplies L034's existing cutoff, while Theorem 16
supplies L035's existing upper inequality. Reuse their ready assessments;
no further Hercher reproof or source refresh is necessary.
No inspected theorem was found to state the exact min(J_1,J_2) target.
This bounded comparison neither certifies novelty nor asserts that a
sharper theorem does not exist.

## Local scope, duplicates and recorded failures

L020's affine-prefix formulas and L035's complete reciprocal estimate are
ready inputs. L024's exact-transport proof was read through its valuation
argument: its endpoint formulas assume exact E^2 tails. They must not be
used unchanged for independent a_i. L031's conclusion (2) and complete
section "Exact boundary valuations, without assuming E^2 transport" were
read: in the current closed language they already establish
v_2(11n+23)=4J_1+2 and v_2(11x+23)=4J_2+2 with general exact tails.
The next proof should use that canonical statement, with L020's formulas
as needed, instead of deriving and assuming an unreviewed tail extension.
Deriving the needed quantitative positive-height bounds from these
identities is part of the approved later test, not completed work here.

Attempt 019 and L031 show that boundary guards alone give no independent
closure contradiction. The present target combines their established
consequences with a different, effective lower-bound input; it does not
reopen the failed guard-only test. History 069 preserves the mismatch
between two longer tails and the full cycle minimum/descending count.
The local overview also records L005's fixed-word repetition budget;
a height-dependent repetition bound is not the requested closed-word
period bound, and supplies no missing global descent claim.
No cross-notebook input or sibling proof was read.

## Bounded discovery and inspection limits

Queries included `Rhin 1987 log 2 log 3 13.3 Collatz lower bound`,
`Collatz cycles logarithmic bound odd runs exponents linear forms logarithms`,
`Georges Rhin 1987 Approximants de Padé ... pdf`,
`Collatz min log 13.3 cycle`, `Collatz OOEO logarithmic cycle`,
`Collatz cycle repeated word logarithmic`, `Collatz postspell logarithmic`,
and `Collatz cycles run lengths logarithmic bound`.
Primary theorem passages were followed before larger extracts.
Search snippets and discussion pages were discovery aids only.
Waldschmidt's author-hosted *Linear Independence of Logarithms* was located
but its relevant full passage was not inspected; it is not an input.
Sodelin's *SymbolicNotes* fixed-word budget, an unreviewed binary-structure
preprint and the already parked m<=95 lead appeared in search results;
no new theorem-level coverage or proof verification is attributed to them.

## Continuation and abandonment test

A later research turn may perform exactly this specialization: seek
explicit absolute A,B at the unchanged target using L035, L031's exact
boundary valuations, L020 as needed and the cited Lemma 12; retain L034's
period conventions. Classify a successful combination as REPRODUCTION.
Do not assert cycle existence, least-root status, relative parameter growth,
distinct junctions, primitiveness or a finite all-parameter exclusion.

Continue if the full guarded calculation proves the stated logarithmic
restriction uniformly for the independent parameters and records its
constants. Abandon this mechanism if it needs an unsupported comparison
between parameters/heights or produces only a reformulation of closure;
record the exact failure without inferring nonconvergence or a global stop.
No approved scope includes bounding max(J_1,J_2), all H_i/a_i or total N.

Mathlib: full parameter-balance result and the cited transcendence bounds
are **not checked**. No matching declaration or absence claim is made.
