# Endpoint-subtracted sharp-block zero tail — completed source review

TARGET: Test whether subtracting the exact two endpoint terms from the sharp-block zero transform gives an absolutely summable zero tail above exp(n) of size o(exp(n/2)*n^(-3/2)), retaining the removed terms explicitly.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step250 searched sharp-weight explicit formulas, endpoint/Mellin boundary subtraction, Laguerre derivative bounds and multiplicity-counting zero tails; reused reviews214/216/243/244/245/246 and their scoped stops. No matching theorem for this exact moving remainder was inspected; no novelty inference. Queries and primary passages are recorded below.
SOURCE_EVIDENCE: Inspected DLMF1.2.8 (15September2026),18.9.23 and18.14.8 including parameter ranges; Hasanalizade-Shen-Wong arXiv2107.06506v1, Cor1.2/(1.5), pp1-2 and Section2/(2.3), p3, reusing review214's proof assessment; Tao 246B Notes4 (12February2021), Theorem8 and Section2/Exercises20-21, including the sharp pointwise limit and summation cases. Reuse review243's complete Proposition7.2 comparison; no unread theorem is imported.
COMPARISON: Exact polynomial differentiation and the global Laguerre bound avoid differentiating L987's O remainder and need no growing-height bulk expansion. The zero-count theorem covers the actual multiplicity multiset and all real cutoffs. These known tools cover an attempt at the remainder specialization, but no source directly states its displayed little-o bound or pays the restored endpoints.
GAP: Prove the finite integration-by-parts specialization, n-uniform first/second polynomial-derivative bounds, absolute high-zero summation and comparison with the benchmark. Keep E_n explicit at finite symmetric heights; convergence, identification and signed control of its restored sums and of actual B_n remain separate obligations.
REASON: Separate literature-only approval of the unchanged step249 target is complete. Permit one REPRODUCTION specialization attempt, with no bound derived here, no RH input and no claim of new mathematics beyond the sources.
LITERATURE_REASON: The incoming REVIEW_REQUIRED gate lacked essential coverage for actual infinite zeros, the growing cutoff exp(n), exact polynomial derivatives and sharp endpoint subtraction. That coverage is now adequate for the saved test; further browsing is not needed for this unchanged scope.
SCOPE: Integers n>=2, actual zeta nontrivial zeros counted with multiplicity, the original K_n and block (exp(n),exp(2n)], no RH, zero simplicity, rightmost-zero hypothesis, isolation, new zero-free estimate or differentiated asymptotic remainder.

The initial nomination below is preserved as the pre-review question.
The completed step250 comparison at the end supersedes its source gaps.

## Exact target to assess

Keep L985's kernel K_n and actual compensated B_n. For s!=1 define

    T_n(s)=integral_n^(2*n) exp((s-1)*u)*K_n(u)du,
    E_n(s)=[exp((s-1)*u)*K_n(u)/(s-1)]_n^(2*n),
    R_n(s)=T_n(s)-E_n(s).

The proposed test is

    sum_(rho nontrivial zeta zero, |Im rho|>exp(n)) |R_n(rho)|
                  =o(exp(n/2)*n^(-3/2)).

These definitions nominate a question; no convergence, inequality,
explicit formula or passage to an infinite zero sum is proved here.
E_n here is an exact boundary expression, not L987's kernel error.
The height exp(n) is prescribed, not a fitted numerical parameter.

Essential local inputs for a later attempt: L985's finite connection
and bulk normalization, L987's audited scale, and L981/L982 for any
actual-Lambda identification. Their remaining arithmetic assertions
are not assumed. The source review must identify the exact derivative
identities and uniform estimates needed, rather than differentiate
L987's O remainder. The usual multiplicity-counting zero theorem
must have an inspected citation before summing the tail. No new
zero-free region or parked arithmetic estimate is proposed.

## Use and discrimination

This would test whether the high-zero remainder can be separated at
a scale smaller than the fixed-mode benchmark. The removed E_n terms
must stay explicit: their conditional sums, sharp endpoint correction
and signed size may contain the original arithmetic difficulty.
Neither tail smallness nor an exact formula pays those terms or
proves dominance of a chosen zero. Low-zero cancellation, realization
of the synthetic quartet, actual B_n upper control, both complements
and L984(H) remain independent gaps.

Continue only with an inspected source scope sufficient to attempt
the displayed absolute tail, and an explicit account of what restoring
E_n requires. A bound at least as large as the benchmark, a hidden
psi endpoint estimate, or failed convergence is negative or unfinished
evidence as appropriate, never payment of B_n. If the construction
only renames the original unpaid boundary problem and has no useful
separable remainder, park this test. Do not repeat the already checked
smooth-weight absolute-tail import or full-Li criterion as a solution.

This is a proposed established-method transfer test, not a justified
creative arithmetic mechanism. Missing signed input blocks creative
escalation; the source turn should compare stronger known results and
import a matching one if available. Full matching Mathlib coverage is
unchecked. No mathematical work on this target occurred in step249.

## Completed comparison — step250, 10 November 2026

This turn approves the exact TARGET above, unchanged from startup.
It is literature-only: no specialized remainder identity, derivative
estimate, tail bound or lemma has been derived. Source availability
is adequate for an attempt; it is not a proof of the target.

### Exact differentiation and a sufficient global source scope

[NIST DLMF18.9.23](https://dlmf.nist.gov/18.9.E23), version1.2.8,
released15September2026, states

    d/dx L_d^(alpha)(x) = -L_(d-1)^(alpha+1)(x).

Use this for d>=1; a constant polynomial has zero derivative.
The notes attribute it to G. Szego, *Orthogonal Polynomials*, 4th ed.,
AMS1975, (5.1.14). The full displayed identity was inspected in HTML.
Repeated use at fixed integer derivative orders is available; handling
degrees below the derivative order remains explicit. No asymptotic
remainder may be differentiated.

[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), same version,
states for integers d>=0, alpha>=0 and all real x>=0,

    exp(-x/2)*|L_d^(alpha)(x)| <= (alpha+1)_d/d!.

It attributes the proof to T.H. Koornwinder, *The addition formula
for Laguerre polynomials*, SIAM J. Math. Anal.8 (1977),535-540,
Remark4.1. This is the inspected global inequality already used in
review244, now checked for the shifted fixed parameters needed by
exact differentiation. It has no bulk-onset or turning-point exception.

L985's already-established finite connection expresses K_n using
degree n-1 and alpha=2, with its constant correction retained.
The source derivative rule and bound cover first and second derivatives
through fixed shifted parameters3 and4. The small n cases, including
derivatives of constants, need separate explicit treatment. The later
attempt must calculate all normalization factors and their n dependence;
no such estimate is asserted here. A global polynomial bound is an
alternative to re-establishing the sharper bulk asymptotic for each
derivative. Import the general results without reproof. Reprove only
the finite-kernel specialization and its uniform comparison, which
these sources do not state. L987's fixed-height O estimate licenses
neither growing-height uniformity nor derivative bounds.

### Actual zero counting and the sharp-formula restriction

Reuse reviews214/216's assessment and re-inspect E. Hasanalizade,
Q. Shen and P.-J. Wong, *Counting zeros of the Riemann zeta function*,
[arXiv2107.06506v1,14July2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), printed p2. For every real T>=e it gives

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
                  <=0.1038*log T+0.2573*log log T+9.3675.

The p1 definition counts zeros with 0<Re(rho)<1 and
0<Im(rho)<=T. Section2/(2.3), p3, implements the symmetric count
by the argument principle, hence with orders; its initial rectangle
avoids zeros. The corollary has the all-T count as stated, not an
assumption of zero clearance. The earlier review inspected the p15
large/bounded-height proof split; its external numerical inputs remain
imported, not independently replayed here. Conjugate negative heights
are included in the requested tail. This is unconditional coverage;
no simplicity, isolation, off-line zero or RH is assumed. Only an
upper counting bound is needed, with the lower cutoff strictly excluded.

T. Tao, [*246B Notes4*,12February2021](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/),
Theorem8, states for noninteger x>1 the classical formula

    psi(x)=x-lim_(H->infinity) sum_(|Im rho|<=H) x^rho/rho
                     -log(2*pi)-log(1-x^(-2))/2.

Section2/Exercises20-21 describes the local zero count, Perron terms,
pole, trivial zeros, near/far nontrivial-zero cases and summed errors.
Those cases were inspected, not only the opening statement. The source
explicitly says the zero series is not absolutely convergent. Its local
uniformity is restricted to noninteger x, as the author's25May2024
clarification confirms; it gives no uniformity across prime-power jumps
or n-uniform constants for a moving block. Theorem8 is cited only for
this pointwise sharp-formula contract. Exercise21(iv)'s displayed
regularizing sign differs from (16); do not use that individual exercise
integrand as a separately imported identity. None of its exercise
estimates is needed to prove the standalone R_n tail.

Thus the sharp formula does not itself license inserting K_n into a
full zero sum, differentiating a conditional series or passing its limit
through an interval containing jumps. Any future arithmetic restoration
needs its own justified finite-height formula and limit passage.
The prescribed endpoints and right-endpoint weights must be kept;
Theorem8 supplies no integer-endpoint half-weight rule.

### Permitted attempt and what it cannot pay

The exact T_n,E_n,R_n definitions remain as nominated. At finite
symmetric zero height keep E_n as its original boundary expression.
Use ordinary finite-interval integration by parts with the exact
polynomial, retaining every endpoint at each application. Test the
remaining integral using the first/second derivative source scope above.
Establish uniformity for the whole strip0<Re(rho)<1, both signs of
Im(rho), every integer n>=2 and multiplicities. Then justify the
improper absolute zero tail from the counting theorem, including
the excluded lower cutoff and the vanishing upper remainder. A dyadic
positive-sum comparison is sufficient as a tool; no signed cancellation
or unproved zero-density gain is licensed. Compute the resulting bound
and compare its full n dependence with exp(n/2)*n^(-3/2).

This is a planned specialization, not its derivation. Retain the -1
correction in K_n and its contribution to T_n and E_n. Do not discard
it merely because a later exact derivative might vanish. No numerical
experiment or new mathematical script is needed for this test.

A successful absolute remainder estimate would isolate one summable
component. It would not establish convergence or a signed bound for
the removed E_n sums. Keep those sums at finite symmetric heights
unless separately justified; do not assign arbitrary summation orders.
Low-zero cancellation, actual B_n identification and upper control,
both complements, L984(H) and the L030-L032/C032a positivity gap stay
open. L981/L982 normalization assertions are not needed or assumed
to test this standalone tail. No cross-notebook input is used.

Continue to one calculation under SPECIALIZE. If the available uniform
bound misses the benchmark, or success requires an unpaid psi endpoint
estimate, preserve that precise loss and stop this payment claim. A
separable remainder can be useful despite unpaid endpoint terms;
its existence alone must not trigger further routine refinements in
place of a signed arithmetic mechanism. All earlier centered-Vaughan,
automatic-average, full-Li and fixed-quartet qualifications survive.
Creative escalation is currently blocked by the absence of a proposed
independently testable signed gain; this source specialization is not
creative. Full matching Mathlib coverage is unchecked and unknown.

### Search and reuse record

Queries included `Riemann zeta explicit formula sharp weight endpoints
integration by parts zero sum absolute convergence`, `Laguerre polynomial
derivative formula uniform bulk asymptotics varying degree fixed alpha`,
`Riemann von Mangoldt N(T) multiplicity O(T log T) explicit bound
Trudgian`, `site.terrytao.wordpress.com von Mangoldt explicit formula
psi discontinuities half zeros symmetric`, `"Laguerre" "explicit
formula" "endpoint" zeros`, `"Laguerre" "zero tail" zeta`, and
`"Mellin" "boundary terms" "explicit formula" primes zeros`.
General hits, snippets and unrelated Laguerre-zero papers supplied no
import. No failure to locate a match is treated as evidence of novelty.

Reuse review243's fully inspected Tao1201.6656v4 Proposition7.2,
pp34-36, low/high-zero split: fixed verified height and smooth
nonnegative weight leave a linear-in-x cost. That theorem is not a
direct import for the present sharp signed weight. Reuse reviews245/246
for the finite quartet/full-Li distinction, review244 for the global
Laguerre bound, and reviews214/216 for multiplicity and cutoff scope.
The narrow local search of November10 zero-tail and sharp-block
assessments/attempts found the nomination, not a completed exact-tail
duplicate. The L985 and centered-Vaughan stops were read at their stated
scope; none forbids this independent remainder test.

The DLMF TeX endpoints returned unsupported content-type errors; the
complete relevant formulas and hypotheses were available in HTML.
There is no essential source-access blocker or pending retrieval retry.
Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. New essential
coverage is complete; the mathematical conclusion is still unproved.
