# Discrete Jensen weighting near a double zero — completed review2042

TARGET: Review whether C029m's discrete Jensen weighting has a compact-uniform first correction with an independently controlled splitting sign at a hypothetical real double Xi zero, comparing the Pollaczek spectral equation and the L611/L569 stops.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact Jensen/Pollaczek/collision searches and scoped comparisons with C029m/q/t/u, L611/L569/L530 and the existing multiplier, metric and residue assessments; queries and inspected passages below. No novelty or theorem-nonexistence inference.
SOURCE_EVIDENCE: Kuznetsov CMB51(2008), Section4 pp567-569 and (9) p564, https://doi.org/10.4153/CMB-2008-055-0 ; Romik arXiv:1902.06330v3, (3.26), Theorem3.8/full proof and Proposition3.9/reported example, printed pp27-29, https://arxiv.org/html/1902.06330v3 ; DLMF18.22.16-18, https://dlmf.nist.gov/18.22#ii ; reused the completed November1 perturbation comparison.
COMPARISON: The checked sources supply basis identities, convergence, conditional forward preservation and simple-root Poisson dynamics, not the required signed correction for the full discrete family. Romik's zero ODE divides by the root derivative, excluding the nominated double-zero case; its exponential coefficient weights also differ. None of these results pays the actual-data sign.
GAP: No independently controlled splitting sign was identified. A compact-uniform first correction for the exact discrete family remains unproved here, as do its sign, all-degree index, initialization, higher multiplicities and global zero transfer.
REASON: The nomination's continuation test fails within the inspected coverage; park this local-sign mechanism without an unsigned variation calculation. This is a source-scope negative that changes routing, not a mathematical impossibility theorem or progress beyond the sources.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED required comparison of the changed discrete-Jensen double-zero hypotheses; existing convergence and reciprocal-cutoff coverage did not assess them. Those ready assessments were reused, not repeated.
SCOPE: Completed literature-only review2042. No mathematical continuation for a local first-variation expansion is approved. No new identity, sign, zero theorem, lemma or mathematical script was derived. The separate endpoint-intertwining nomination is REVIEW_REQUIRED.

## Completed comparison2042

The gap, intermediate use and abandonment threshold are those of the
preserved nomination below. The test was whether a source supplies an
actual-data signed relation, rather than merely tools for writing down
an unknown correction. No such relation was identified in this bounded
review. Park the nomination; this does not prohibit reopening after a
materially new signed input.

Three mechanisms were compared:

1. **Jensen preservation in a different basis.** Kuznetsov's Section4
   distinguishes monomial multiplier preservation from his weighted
   Pollaczek experiment. Proposition4.1 requires a transformed
   coefficient polynomial to have only real zeros; Proposition4.2
   concerns differently damped auxiliary coefficients. The weighted
   full-family discussion asserts compact convergence and reports
   computations, without a signed correction theorem. Its sufficient
   premise cannot be supplied by assuming RH or auxiliary root reality.
   This confirms the scope comparison already recorded in discovery2026.

2. **Spectral equation and Poisson zero dynamics.** DLMF18.22.16-18
   gives the degree-dependent basis equation already specialized in
   C029t. A weighted sum does not acquire a common eigenvalue.
   Romik, *Orthogonal polynomial expansions for the Riemann xi
   function*, arXiv:1902.06330v3, 5 May2019, Section3.5, uses finite
   polynomials with distinct zeros and exponential weights exp(-k*tau).
   Read Theorem3.8's complete proof: implicit differentiation is followed
   by division by the nonzero derivative and products of root gaps.
   Its hypotheses exclude a double zero, and no theorem there identifies
   this flow with C029m's discrete weights. Proposition3.9's displayed
   example relies on reported root computation; it is comparison evidence,
   not a rigorous certificate imported here. Reuse audited L530 for its
   narrower certified moment-family obstruction. Neither result refutes
   a coefficient-specific law for the actual full family.

3. **Generic analytic perturbation or Gaussian preservation.** Reuse
   `2026-11-01-small-cutoff-multiple-zero-stability-review.md`: Rellich
   requires interval hyperbolicity, preparation requires a holomorphic
   parameter germ, and the Gaussian theorems concern specified weights.
   No analytic parameter family extending 1/N has been supplied.
   These sources do not pay the new sign or this family identification.
   L611 and L569 give the precise local reasons to reject another
   unsigned correction or absolute-error argument. No reproof is needed.

Primary links: [Kuznetsov, publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf),
[Romik, Section3.5](https://arxiv.org/html/1902.06330v3#S3.SS5),
[DLMF18.22](https://dlmf.nist.gov/18.22#ii).
PDF screenshots returned references without inspectable image payloads;
the relevant primary text and complete ODE proof were readable. No
visual formula audit or independent verification of upstream[9] is claimed.

Queries used: `"Meixner Pollaczek" "Jensen" zeros correction`;
`"Kuznetsov" "Xi" "double" zeros Jensen`;
`"Meixner-Pollaczek" zeros deformation collision Jensen`;
`"Jensen" "Meixner" "hyperbolicity" multiplier`;
`"Meixner-Pollaczek" "Jensen" "asymptotic"`;
`"Meixner-Pollaczek" "multiple zeros"`.
Search hits about zeros of individual orthogonal polynomials and their
parameter interlacing were not read as theorems about the full sum.
They remain nonessential unread leads. Search failure establishes no
absence or originality claim. Full matching Mathlib coverage is unchecked.

Local comparison also rejected a generic negative-square/metric restart:
discovery2008/2026 and post-residue2028 already cover that route and its
unpaid actual-coefficient premises. No such duplicate is nominated.
A narrowly different prerequisite is whether the source's exact
quadratic multiplication identity survives the discrete weighting with
only endpoint corrections. Equation(9) motivates this question, but
no commutator or endpoint assertion was computed here. Its separate
review nomination2042 makes the exact finite discriminator explicit.
It is not an approval of creative mathematics: no uniform signed law
is available yet, which blocks a justified creative central-gap attempt.

Outcome NEGATIVE: the new primary hypothesis comparison fails the
nomination's continuation gate and parks dependent calculations.
No mathematical exploration budget was spent or reset. Essential
qualifications remain C029m's full coefficients/tilt, C029u's upstream[9]
qualification, hypothetical multiplicity, and missing actual/global signs.
No cross-notebook input, canonical proof change or RH candidate.

## Invocation-start nomination2041, preserved

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity;
C029m's eventual index premise remains unpaid. A possible intermediate
input is control of spurious conjugate pairs near a real multiple zero
under polynomial approximation. Such control could clarify the local
obstacles to an index/zero-transfer argument; it would not exclude an
actual off-line zero or prove the eventual index bound.

Use precisely C029m's full T_N and F(t)=exp(-pi*t/4)Xi(t), with all
odd coefficients and exact N!/((N-k)!N^k) weights. The proposed base
point is hypothetical: a in R, Xi(a)=Xi'(a)=0, Xi''(a)!=0. Neither
existence of such a nor RH nor simplicity of other zeros is assumed.
The parameter is the discrete sequence 1/N; do not silently replace
it by an analytic parameter family to apply a preparation theorem.
Compact-uniform differentiated estimates and all shifts in a proposed
operator formula would have to be justified for this actual family.

The selected question is whether primary results supply, or suggest a
concrete independently testable source of, the **sign** of the first
nonzero local correction relative to the quadratic zero coefficient.
A known uniform convergence theorem or a formal expansion of individual
weights is not that input. A signed joint relation from actual Xi data
could be useful; a positive spatial envelope, arbitrary moment model,
assumed Laguerre-Polya membership, or generic small C^2 error cannot
be used as a substitute. No candidate correction is derived here.

Three routes were compared for continuation. The type-II route is now
stopped by audited C029u under its qualification. Global PSD transport
through the prescribed affine quotient retains C029q's finite stop;
no new embedding or eventual hypothesis is supplied. The local signed
correction question is different from both and is selected only for
source review. C029t's basis eigenidentity is a possible computational
input, not its failed fixed inverse zero-count premise.

Duplicate/obstruction checks also include the October30 L530 moment
flow stop, the L569 absolute-error stop and L611's reciprocal-cutoff
sign stop. The change to a full actual discrete family is explicit,
but is not itself evidence that a useful sign mechanism exists. The
review must compare the resulting hypotheses with those stops before
approving any calculation. Reuse standard perturbation coverage; do
not reopen inaccessible original collision scans for routine machinery.

Continue only if a source theorem actually pays the required sign
under independently verifiable hypotheses, or a specific new actual-data
relation has a bounded discriminator distinct from those failed rules.
Record the exact expected inequality and failure test before nominating
research. If all available tools leave only an unspecified shifted-Xi
sign, park this proposal; no equality-case expansion, degree sweep or
generic first-variation lemma is warranted. This is a discovery gate,
not a promise that the proposed mechanism works.

Essential local inputs for the review: C029m, audited C029u and the
spectral equation portion of C029t. L611/L569/L530 and C029q are failure
comparisons, not premises of a new theorem. The Kuznetsov upstream[9]
qualification, global signs, all-degree bounds, initialization, higher
multiplicities, vanishing leading correction and zero-location transfer
remain unresolved. Full matching Mathlib coverage is unchecked. No
cross-notebook input is proposed.

Routing: literature_comparison, standard/high. A uniform asymptotic
specialization alone is not creative. A later proof_attempt/creative
would require an identified new signed actual-Xi mechanism and its
bounded test; missing essential comparison is the current blocker.
