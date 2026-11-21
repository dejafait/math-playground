# Suzuki generator-energy source comparison

TARGET: Assess whether the causal Suzuki parameter generator admits a window-uniform relative quadratic-form bound of its arithmetic part by its archimedean part in the original L2 norm, specifying domains, boundary terms and a sufficient contraction threshold.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed three chains: exact Suzuki generator/semigroup searches and local composition failures; primary finite-interval fractional-integral generator and perturbation theorems; arithmetic/archimedean signed-input comparisons including the new 2607.24830 lead. No matching window-uniform signed bound was located; no absence or novelty claim follows.
SOURCE_EVIDENCE: Read Suzuki 1907.07302v2 Theorem 1.2, (1.1),(1.10)–(1.13), Proposition 3.2 and (3.13)–(3.15); Lumer–Phillips (1961) Theorem 3.1 and proof pp.686–687; Carvalho-Neto–Fehlberg 2108.02291v2 Theorems 22,27,28 and relevant p=2 proof cases pp.17–27; Schnaubelt Evolution Equations (19 March 2026) Theorem 3.4 and proof pp.74–76; DLMF 5.9.13; Kim et al. 2607.24830 Sections 2.2,3.1,4 and stated limitations pp.3–5,13–14.
COMPARISON: The sources provide a finite-interval logarithmic generator domain and bounded-perturbation machinery, but no realization theorem for this exact Suzuki family or independent arithmetic domination in the original norm. The new spectral lead supplies neither the requisite remainder bounds nor an unconditional global sign. L618 and L739 remain qualified as before.
GAP: Realize the causal finite-window family down to parameter zero and identify its domain before any energy calculation; thereafter total dissipativity in the original norm, uniformly over windows, remains unproved. An exponential-weight bound, finite-window boundedness or a relative bound with unpaid additive loss does not meet that threshold.
REASON: Complete the broad source question without importing an unavailable sign theorem. A concrete bounded domain-construction specialization is now supported and nominated separately; it is not a proof of the relative inequality. No creative signed target is approved while the actual generator and an independent favourable estimate remain unestablished.
SCOPE: Completed source comparison only; no new lemma, generator formula for Xi, semigroup identity or energy inequality is proved. EXPLORE does not approve arbitrary-window signed estimates; the single later domain-construction target has its own assessment below.
LITERATURE_REASON: Essential generator/domain and relative-energy coverage was missing at invocation; the existing square-defect and compact-norm assessments do not cover it.

## Initial bounded-review nomination (preserved)

The main gap is unconditional actual-Xi mixed positivity. The
intermediate source question is whether infinitesimal energy offers
an independently testable sufficient contraction estimate. If it did,
it could address the missing fixed-parameter all-window control;
the further implications to actual-Xi signs and RH remain separate
and must retain their exact hypotheses. No such estimate is claimed.

Use L018 for the completion, L618 for the actual kernel/operator
setup and the already audited compact norm limit, and L739 only as
the now verified obstruction to square order. No cross-notebook input
is proposed. Reuse the parameter-descent source comparison for its
reflection/domain warnings; do not reopen its direct scalar-product
implementation or reproduce L618's bound.

Limit discovery to three source chains: the Suzuki parameter family
and its precise causal domains; primary semigroup or quadratic-form
criteria applicable to this compression; and known arithmetic versus
archimedean positivity/relative-bound obstructions. Retrieve theorem
hypotheses and essential proof cases before broad extracts. Compare
with the existing construction/screw signed-input stops. At most one
later concrete energy inequality may be nominated after that review.

Continue only if sources identify a well-defined form comparison
with a stated sufficient threshold and a bounded test independent of
assuming RH, innerness or global contraction. Park this mechanism if
the required comparison is only equivalent positivity with no
independently accessible estimate, or if domains/compression defeat
the generator implementation. An inaccessible essential source must
be recorded as such, rather than filled by an invented theorem.

That nomination was the source gate for step 270. The completed comparison
below records its result; no mathematical specialization was executed.
A later creative target still needs an exact inequality, source assessment
and bounded discriminator. Mathlib coverage is unknown.

## Completed review, step 270

The main gap remains unconditional actual-Xi mixed positivity. The proposed
use was a sufficient fixed-parameter all-window contraction estimate.
The search does not supply it. It does supply a specific domain lead that
can be tested before any signed estimate. This is literature exploration,
not mathematical progress beyond the checked sources.

### Exact family and prior failures

[Suzuki, arXiv:1907.07302v2](https://arxiv.org/pdf/1907.07302v2),
6 March 2020, printed pp.1–3,6–8, assumes theta>1 in Theorem 1.2.
Proposition 3.2 treats its auxiliary kernel for theta>0. Equations
(1.11)–(1.13) split arithmetic and archimedean factors; causality makes
the arithmetic sum finite on bounded spatial ranges. None of these
statements identifies a parameter-zero generator domain. Equation (3.15)
is a shifted-transform statement with reflection; the proof explicitly
does not assert that the untruncated output is L2. Thus it supplies no
unweighted full-line multiplier realization. Reading (3.13)'s construction
and (3.15)'s support/Fubini cases does not repair this missing hypothesis.

Read L018, L618's operator setup and L739's statement. Reused the completed
parameter-descent comparison, its source-limit attempt, and the
construction/screw stops. The later square-order audit is not reopened.
The new causal formulation must retain the reflection when compared with
the original Hankel operator; it must not identify their parameter products.

### Domain and contraction criteria

[Lumer and Phillips, *Dissipative operators in a Banach space*, Pacific
J. Math. 11 (1961), 679–698](https://msp.org/pjm/1961/11-2/pjm-v11-n2-p19-s.pdf),
Theorem 3.1, pp.686–687, requires a dense domain, dissipativity and
range(I-A)=X. The necessity and resolvent/Hille–Yosida sufficiency cases
were read. On a Hilbert space the required sign is Re<Af,f><=0 on the
generator domain. A relative arithmetic/archimedean bound must pay every
scalar and boundary term so that the **total** form meets zero, in the
original norm. A positive additive norm loss only supplies a shifted
condition. No relative coefficient or sign is asserted for Xi here.

[Carvalho-Neto and Fehlberg Júnior, arXiv:2108.02291v2](https://arxiv.org/pdf/2108.02291v2),
5 December 2021, Theorems 22,27,28, printed pp.19,22–27, give the
finite-interval Riemann–Liouville semigroup and its logarithmic generator.
For the needed scalar complex p=2 case, set

    Phi_f(x) = integral_0^x log(x-y) f(y) dy.

Theorem 28 specifies absolute continuity of Phi_f on [0,L] and
Phi_f' in L2; its generator is -psi(1)f+Phi_f'. Read both domain
directions, including the convolution/Fubini identity (19), the zero
left-endpoint trace and the strong-limit step. The p=2 specialization
requires finite L and the L2 topology; it supplies no Suzuki identity.
The printed p=infinity claims are not imported: the density step in
Theorem 22 is not justified there by the stated smooth approximation.
This qualification does not enlarge or change the p=2 target.

[Schnaubelt, *Evolution Equations*](https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf),
version 19 March 2026, Theorem 3.4, printed pp.74–76, gives generation
on D(A) after adding a bounded B to a C0 generator A. Its original-norm
growth bound is M exp((omega+M||B||)theta), and its Dyson–Phillips
series converges in operator norm on compact parameter ranges. Read
the resolvent, uniqueness and series cases. Generation by this theorem
does not assert contraction. An equivalent norm used inside its proof
does not authorize changing the target norm.

[DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13), Re(z)>0 with principal
logarithm, separates psi(z) into log(z) and a Laplace integral. Together
these are usable source inputs for testing a logarithmic-generator plus
bounded-perturbation realization. The actual shifted/scaled kernels,
arithmetic translations, domain preservation and endpoint accounting
have deliberately **not** been derived this turn.

### Signed-input comparison and new lead

The existing screw/construction assessments already distinguish a
Friedrichs extension bounded below on each window from a nonnegative
form on every window. Their small-window and restricted-space results
do not supply the missing uniform comparison. No essential blocked
scalar-tail report was retried.

[Kim et al., arXiv:2607.24830](https://arxiv.org/pdf/2607.24830),
current unversioned PDF retrieved 4 November 2026 (immutable version not
attested), Sections 2.2,3.1,4, pp.3–5,13–14, is a new
primary lead. Its prime-free regime is 2a<log 2. Its stated limitations
leave pseudodifferential remainders and Mellin tails unproved for the
symbol-to-spectrum passage. Its global residual argument explicitly
assumes RH. Neither finite-element spectra nor that conditional
residual estimate supplies this target's unconditional relative bound.
No result from the paper is imported; companion rigor documents remain
unread, nonessential leads for this target.

### Search coverage and decision

Queries included `Suzuki "1907.07302" generator semigroup`,
`"Integral operators arising from the Riemann zeta function" generator`,
`Suzuki "xi" "dissipative" operator`, `"Suzuki" "causal" "generator"
Riemann`, `"Riemann Liouville" "semigroup" "infinitesimal generator"
logarithm`, and `"Suzuki" "archimedean" "quadratic" zeta`.
The three chains were the exact family, finite-interval generator criteria,
and signed arithmetic comparisons. Scoped local searches of
drafts/literature, ATTEMPTS and foundations for Riemann–Liouville and
causal/Volterra semigroups found no earlier matching assessment.
Search silence establishes neither originality nor nonexistence.

Do not attempt or assume the broad relative bound yet. The single
next specialization is specified in
`2026-11-04-suzuki-causal-generator-realization.md`.
Continue only if the actual finite-window domain and reflected relation
can be proved with finite-L perturbation bounds and retained endpoint
terms. Abandon this implementation if it requires an unproved global
L2 multiplier or loses the original norm. Even success leaves uniform
dissipativity, all-window signs and Xi transfer unpaid. This is one new
source review, not a persistent access blocker or an exhausted domain
construction attempt. Full Mathlib coverage was not checked.
