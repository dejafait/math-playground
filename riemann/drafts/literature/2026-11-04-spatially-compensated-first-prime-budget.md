# Spatial compensation for the first-prime resource — source comparison

TARGET: Assess source coverage for the spatially compensated bound Q_2(f)<=W_b(h)/2 on every complex globally neutral f in C_c^infinity(0,4log3), with W_b(h)=R(h)+integral log(b/|y|)|h(y)|^2dy and b=2log3.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step306 searched support-volume logarithmic-Laplacian eigenvalue bounds, compact-support Fourier-density estimates and compensated Beckner/translation comparisons; inspected Laptev--Weth's primary theorem and relevant proof, and reused the assessed Beckner/sector inputs. Exact queries and local failure comparisons are below; no matching arithmetic-delay theorem or novelty certification was found.
SOURCE_EVIDENCE: Laptev--Weth, arXiv:2009.03395v2 (21 September2020), form/convention/domain (1.1)-(1.3) pp.1-2, support-density (2.3) p.3, Thm3.1/proof pp.6-7, Cor3.2 and Thm4.1/(4.1) p.7, and explicit d=1 comparison p.10. Reuse Beckner math/0701939v6 Thm4/(12) and L746 (4); L743 fixes the delay coefficient and L747 supplies only the odd comparison.
COMPARISON: Known support-volume coercivity for the logarithmic Fourier form is available in dimension one; it needs no parity or neutral moments. This supplies the missing known input for a routine normalization and constant comparison with the added spatial cost. Neither the target allocation nor payment of that cost in complete Weil energy is a source theorem inspected here.
GAP: Specialize the known lower bound to the exact centered interval and complex class, match the entire Beckner resource plus the stated spatial cost, and compare with the actual first-prime coefficient. The whole-class half allocation, complete-energy payment, other primes, signed corrections and support propagation remain unproved here.
REASON: Essential changed-resource coverage is now adequate for one REPRODUCTION attempt; a novel coercivity mechanism or numerical search is not currently justified. Import the existing theorem, explaining the interval, complexification and constants rather than reproving the spectral theorem.
SCOPE: Only the unchanged compensated bound at b=2log3 on the full complex globally neutral smooth class, with all exterior pairs and both exact moments retained. Permitted next work is source specialization, Fourier normalization, integrability, elementary constant bounds and the bounded-delay comparison. A direct density replay is justified only to settle a specific normalization or complex-scope issue; no full-energy sign or spatial-cost payment is approved.
COVERED_TARGET: Prove or refute Q_2(f)<=W_b(h)/2 for every complex globally neutral f in C_c^infinity(0,4log3), with h(y)=f(y+b), b=2log3, and W_b(h)=R(h)+integral log(b/|y|)|h(y)|^2dy.
LITERATURE_REASON: The invocation began REVIEW_REQUIRED for an added spatial resource. Step306 performs its first theorem-level support-dependent comparison, reusing the ready Beckner and odd-sector assessments; further unchanged-scope literature is unnecessary before the mathematical specialization.

## Original nomination retained — step305

The following scope and test were written before the separate source
comparison. Its statements that coverage is missing or unapproved describe
that nomination, superseded only by the step306 assessment below. No
mathematical conclusion is being retrospectively attributed to step305.

## Exact proposed scope

Keep L743's actual coefficient and L746's original class: a=log2,
b=2log3, L=2b, h(y)=f(y+b), zero extension to R, and

    integral_0^L exp(x/2)f(x)dx = integral_0^L exp(-x/2)f(x)dx = 0,
    Q_2(f)=sqrt(2)log2 Re integral_R h(y-a) conjugate(h(y))dy.

R(h) is precisely the whole-line nonnegative double integral in
L746 (1), coefficient 1/4, retaining all exterior pairs. The proposed
additional cost is the integral over (-b,b) of
log(b/|y|)|h(y)|^2; its value at y=0 is interpreted through the
Lebesgue integral. The definition is only a nominated resource, not
an identity with a complete Weil form. No parity restriction, cellwise
constraint, profile restriction or singular limiting function is allowed.

Essential input IDs for a future assessment are L743, L746 and L747.
L744 (6) provides possible downstream energy context, not a premise
or an established way to pay this added cost. Any use of that formula
must retain its actual digamma symbol, pole term and all prime powers.

The source comparison should check exact statements and stronger
known support-dependent logarithmic uncertainty/logarithmic-Laplacian
bounds, including elementary Fourier support-density estimates and
their constants, before deciding whether any mathematical attempt is
needed. It must inspect hypotheses and compare the coefficient 1/2,
the length, complex scope and both moments. This is a proposed search
scope; none of those bounds has been derived or approved in step305.
Do not reprove Beckner's identity or the audited odd specialization.

## Relevance and discriminating test

The main gap remains unconditional actual-Xi mixed positivity.
The proposed intermediate estimate would test whether an explicit
spatial compensation can address the parity component left unpaid
by L747 without contradicting L746. A positive answer could pay one
arithmetic term only after this extra cost is paid in the actual
complete energy. Other primes, signed corrections and arbitrary
support propagation remain independent gaps.

Continue only after adequate source coverage, then seek a bound on
the whole stated class or a rigorous smooth exact-neutral witness
with Q_2>W_b/2. A trial-space bound, unproved spatial-cost budget,
or mere restatement of the odd result does not decide the question.
Failure would stop this particular modified allocation, not RH or
all joint-energy mechanisms. Preserve L746's R-only stop unchanged.

This is an unproved target definition, not new mathematics or a
creative result. No already-justified new central creative mechanism
was supplied by the L747 audit; essential changed-resource coverage
is the immediate blocker. If the comparison finds only a routine
known specialization, classify it accordingly rather than forcing a
creative label. Full matching Mathlib coverage is not checked.

The new assessment requires separate approval next turn. It does not
invalidate the completed audit. No mathematical script or new lemma
was created for this target.

## Step306: separate source comparison, 4 November2026

### Inspected known theorem

Ari Laptev and Tobias Weth, *Spectral properties of the logarithmic
Laplacian*, [arXiv:2009.03395v2](https://arxiv.org/pdf/2009.03395v2),
21 September2020, Theorem4.1/(4.1), printed p.7, states for an open
set Omega in R^d of finite measure:

    lambda_1(Omega) >= (1/d) log((2pi)^d/(e |Omega| |B_d|)).

Here B_d is the unit ball. Their operator is H=(1/2)log(-Delta),
with the zero-extension Fourier form

    q(u)=(2pi)^(-d) integral log|xi| |u_hat(xi)|^2 dxi,
    u_hat(xi)=integral exp(-i x.xi)u(x)dx.

Equations(1.1)-(1.3), pp.1-2, specify its form domain as the closure
of C_c^infinity(Omega) in the stated logarithmic Fourier norm.
Read (2.3), p.3, Theorem3.1 and its Fourier-density proof, pp.6-7,
Corollary3.2 and the complete Theorem4.1 proof, p.7. This is a
support-volume bound, without moments. Although the abstract says
d>=2, p.10 explicitly includes d=1 for (4.3), the unit-ball instance
of (4.1); only the improved (4.4) excludes it. No table value is used.
H is the zero-extension operator, not the spectral logarithm of the
Dirichlet Laplacian.

The [author-hosted revised manuscript](https://www.ma.imperial.ac.uk/~alaptev/Papers/laptev-weth-2020-revised.pdf)
was initially inspected at its pp.1-2,7-8,11. It has 22 pages;
the pinned v2 above has 21 and different page breaks. The final
citation and ranges above refer to v2, whose relevant statements and
proof were also retrieved. Do not mix its page numbers with the revised
file. The publication DOI is
[10.1007/s13324-021-00527-y](https://doi.org/10.1007/s13324-021-00527-y).
No claim is made to have audited all proofs of either version.

### Applicability and the exact difference still unproved

For the intended application take Omega=(-b,b), b=2log3. It is an
open bounded interval of finite measure, with the required zero
extension; the target functions lie in its smooth core. The source
imposes neither an odd restriction nor either global exponential
moment. Thus those moments can be retained without adding an
unassessed constraint to the source theorem. The full complex scope
must be justified explicitly in the next mathematical step: use
complexification of the real symmetric form (equivalently, real and
imaginary parts), checking the logarithmic form as well as the
norm. Do not silently use a real-only calculation for complex tests.

Reuse the already assessed Beckner identity, with exact source and
normalization canonical in L746 (4), and the ready assessments
`2026-11-04-beckner-first-prime-remainder-budget.md` and
`2026-11-04-odd-neutral-first-prime-remainder-budget.md` in this folder.
There is no new endpoint differentiation, sharp-Pitt proof or odd-sector
reproof to do. The sector theorem is useful comparison evidence, not a
premise for extending L747 to even functions.

The needed local work is to combine the *defined* added spatial
integral with the already written spatial-logarithm term of L746 (4),
verify all logarithmic integrals are finite, apply the cited Fourier
form bound in the correct normalization, and compare the resulting
norm coefficient with 2sqrt(2)log2. This last number is the required
threshold for the proposed norm-level sufficient test, not a computed
achieved bound. Check the Cauchy--Schwarz delay comparison on the
whole-line zero extension with coefficient fixed by L743 (1).
Neither a combined formula for W_b, its norm floor, a numerical value
for that floor nor the allocation is derived in this source-only turn.

This difference is routine specialization of known machinery and is
classified REPRODUCTION for the proposed mathematical continuation.
The source theorem is stronger in functional scope than the neutral
subclass but does not itself mention W_b or the arithmetic delay.
Hence SPECIALIZE, rather than an asserted direct import of the entire
allocation. Reproving Theorem4.1 or its spectral foundations would be
unnecessary. If a concrete normalization/scope discrepancy arises,
a narrowly justified replay of the inspected density argument is
available; it would also be reproduction, not a new uncertainty result.

### Search record and comparison with existing stops

Actual query strings included:

- `Laptev Weth logarithmic Laplacian eigenvalue lower bound first eigenvalue volume theorem`
- `logarithmic uncertainty compact support Fourier density lower bound logarithmic integral Beckner`
- `"logarithmic Laplacian" "N ≥ 1" "lower" eigenvalues`
- `"logarithmic Laplacian" "one-dimensional" "lower bound"`
- `"spatially compensated" "logarithmic" Beckner`
- `"Beckner" "translation" "logarithmic Laplacian"`
- `"logarithmic Laplacian" "first eigenvalue" "interval" lower bound`

Queries for the nominated terminology did not produce an inspected
matching delay theorem. That does not certify novelty. The positive
coverage is the explicit known support-volume theorem, not search
silence or an abstract. Chen--Veron,
[arXiv:2011.05692v2](https://arxiv.org/pdf/2011.05692v2), was opened
only through its first-page metadata/abstract as a related lead; no
numbered theorem or bound from it is imported. Other search-visible
fractional/logarithmic eigenvalue and antisymmetric maximum-principle
papers are unread leads, unnecessary for this fixed smooth-core target.
The older logarithmic-Hardy parameter-endpoint lead remains qualified
by the prior assessment's suspect cutoff; it is not needed here.

Local comparison inspected L743 (1), L746's hypotheses, (1)/(4) and
counterexample mechanism, L747's scope and source specialization, the
step299/303 working records, and these named failure records:
`ATTEMPTS/2026-11-04-first-prime-half-beckner-budget-stop.md`,
`ATTEMPTS/2026-11-04-neutral-prime-only-rayleigh-saving-stop.md`,
`ATTEMPTS/2026-11-04-carrier-span-general-sign-scope-limit.md`, and
`ATTEMPTS/2026-11-04-joint-energy-generic-source-scope-stop.md`.
No duplicate compensated allocation was identified in those specific
paths. This is not a claim of exhaustive archive search.

L746's audited finite smooth even witness refutes the R-only half
allocation, not the changed W_b resource. L747 controls only odd
functions with R. L743's unweighted prime supremum does not estimate
this logarithmic cost. The carrier and generic-energy stops forbid
assuming that a restricted positive family, a different prime
coefficient, or omitted poles establish complete-energy positivity.
All remain valid. This comparison neither repairs nor reopens them.

### Disposition, relevance and bounded continuation

The main gap is unconditional actual-Xi mixed positivity. The single
intermediate target remains exactly the compensated whole-class first
prime allocation defined above. If established, it could pay that
arithmetic term only after the added spatial cost has itself been
paid in the actual complete energy. L744 (6) is prospective downstream
context, not an input proving this cost is available. Other primes,
signed digamma/pole corrections and arbitrary support propagation
remain independent unresolved assumptions.

The concrete continuation is the COVERED_TARGET above, with essential
inputs L743, L746 and L747 as scope/obstruction evidence. A complete
bound on the stated complex class or a rigorous smooth exact-neutral
strict witness decides it. If the source-based norm floor misses the
required threshold, report that sufficient-test failure as inconclusive
for the allocation; do not manufacture a counterexample. A strict
witness would stop this changed allocation only. A trial-space result,
dropped exterior pairs or unpaid spatial cost cannot establish the
proposed downstream sign.

No central creative mechanism is justified merely by this source
comparison: a paid complete-energy identification remains absent.
Finish the concrete known-source specialization before nominating a
new mechanism. The changed continuation is source-ready under
SPECIALIZE and is recorded for the supervisor's separate approval;
this invocation does not execute it. No further unchanged-scope
literature search is proposed. Full matching Mathlib coverage is not
checked; no formalization or absence claim is made.

This completes one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step,
with zero mathematical exploration usage. The result is actionable
source coverage, not a proved compensated inequality or a mathematical
discovery. No lemma, mathematical script, PROOF or DAG was changed.
No source blocker remains for this literal target. A shell-download
attempt failed DNS; the theorem, hypotheses and relevant proof remained
accessible through the web tool, so no dependent source input is missing.
