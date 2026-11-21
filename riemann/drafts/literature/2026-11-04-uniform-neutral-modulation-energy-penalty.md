# Uniform complete-energy penalty for exactly corrected modulations

TARGET: Establish a uniform logarithmic complete-energy penalty for L743's exactly corrected modulations of unit smooth cell trains with a fixed H2 envelope bound, retaining every prime power and both pole moments.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 286 compared joint frequency reduction, neutral Schur estimates and resonance penalties; exact searches and rejected direct imports are in the parent assessment. No full matching corrected-family theorem was located; no novelty claim. This new assessment requires separate approval before research.
SOURCE_EVIDENCE: DLMF5.11.2 and 5.11(ii) complex remainder paragraph; Zhu2608.24827v2 Lem3.1, Thm1.1/Section4 and Lem6.1/proof; audited L740 complete generator, L741 scalar/pole/archimedean identities and L743(9)-(12) exact correction. The SRFP311T1 core-form theorem is a contrast, not an input.
COMPARISON: Known symbol asymptotics and finite prime norm bounds cover the basic high-frequency mechanism. Only uniform integration over the specified bounded-H2 family, full finite-window energy specialization and exact correction/normalization remain to justify. Import known results; do not reprove asymptotic expansions or known finite-window positivity.
GAP: The proposed uniform inequality below is unproved. No assertion for arbitrary envelope complexity, growing support, complete neutral/complement splitting, bounded-frequency positivity or RH is covered.
REASON: L743 preserves prime-only Rayleigh values by modulation but does not estimate the complete logarithmic energy. This bounded supported-family test would quantify that cost and prevent an invalid energy-normalized extension, without reopening signed-slope or summable-beta routes.
SCOPE: Fixed K>=2, L=K log(3)/2, fixed H2 bound M with nonempty smooth family, fixed L743 smooth correction. Complex tests; original unweighted L2 norm. No RH or source positivity computation, no limit in K or M, no full energy-norm equality. Planned classification REPRODUCTION, not a creative central-sign mechanism.

## Precise proposed inequality, not a result

Use ell=log(3)/2, L=K ell and L743's entire bounded Hermitian
prime-delay operator B_L. Put

    Cprime = 2 sum_(2<=n<exp(L)) Lambda(n)/sqrt(n).

This is a coefficient bound, not an asserted exact operator norm.
The notation A_L is reserved for L740's nonsymmetric generator.

Let F_(K,M) be all complex functions

    w(x)=sum_(j=0)^(K-1) w_j(x-j ell),
    w_j in C_c^infinity(0,ell),
    ||w||_2=1,   ||w||_(H2(R))<=M,
    ||w||_(H2(R))^2=||w||_2^2+||w'||_2^2+||w''||_2^2.

Zero extensions are intended. Fix K and M for which this family is
nonempty. There is no claim of a bound uniform in M or K, and no
assumption that an arbitrary supported unit vector belongs to this
family. Smooth cell interiors avoid any unproved cell-boundary traces.

Fix once and for all the chi, b_+, b_- and invertible moment matrix G
of L743 (9). For every real t and w in this family, use its exact
correction (11)-(12), with t replacing t_r:

    d_(j,sigma)(t,w) = exp(it j ell)
                  integral_0^ell exp(sigma s/2) exp(it s) w_j(s) ds,
    h_(t,w)(x) = sum_j sum_(tau=+1,-1)
                  [G^(-1)d_j(t,w)]_tau b_tau(x-j ell),
    v_(t,w)(x) = exp(itx)w(x)-h_(t,w)(x).

These definitions are inherited from the audited construction; no
new correction is derived here. Its exact moments must be retained
when evaluating both poles, and not replaced by an asymptotic zero.

The proposed single target is: there are t0 and a nonnegative function
epsilon_(K,M,chi)(t)->0 as |t|->infinity, independent of w, such that
v_(t,w) is nonzero and, for all |t|>=t0 and w in F_(K,M),

    E_L(v_(t,w))/||v_(t,w)||_2^2
       >= log(|t|/(2pi)) - Cprime - epsilon_(K,M,chi)(t).   (P)

Here E_L=-Re<A_L v,v> uses L740's complete generator, not a truncated
archimedean-minus-half-prime core. All finite prime powers, the scalar,
the signed continuous kernel and both pole moments must be accounted
for. No phase-return hypothesis is needed for (P). L743's recurrence
sequence is an eventual application, not a further target approved here.
The sought threshold is coefficient one on log|t| and a uniform o(1)
error beyond the paid constant Cprime. Eventual positivity requires
log(|t|/(2pi))>Cprime+epsilon; no finite t0 is asserted now.

## Coverage, specialization and qualifications

[NIST DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11)
was read at the expansion, its sector condition and complex error
paragraph. Apply only at z=1/4+i xi/2, with the principal logarithm.
The known remainder has a sector factor bounded on this line. Compact
xi must be handled by continuity away from the digamma poles. This
source is an imported scalar estimate, not the varying-family integral
bound (P). Plancherel and the standard Fourier derivative identity on
smooth zero-extended tests are the named Fourier inputs.

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
Lemma 3.1, is a supporting one-sided high-frequency estimate. The
parent assessment records its finite-band reduction and why it does
not prove (P)'s uniform correction statement. Its even-test pole formula
must never replace the complex pole product. No new sign theorem at
the already covered small windows is sought.

Audited L740 (4)/(5) fixes the complete finite-window operator. L741's
Section 2 kernel/symbol identities and finite-square pole calculation
are the local normalization input. Its closed-form domain theorem is
only asserted at L=log(3); this target uses smooth tests for other
fixed L and must justify that specialization directly from L740,
not extend that closed-domain conclusion without proof. Use only
L742 (2) for neutrality and no other conclusion of L742. L743 (9)-(12)
fixes the finite-dimensional complex correction and its exact moments;
its unweighted smallness alone is insufficient for this energy estimate.

Essential obligations are a uniform bound for the shifted logarithmic
Fourier integral over F_(K,M), correction size in the logarithmic form
as well as L2, a uniform nonzero denominator, exact evaluation of pole
moments, and the whole finite arithmetic cost Cprime. These are proposed
application checks, not a proof sketch claiming that they pass. No
source assertion is used to interchange a limit with the unbounded
multiplier. No local positivity seed or RH premise is needed.

The [parent comparison](2026-11-04-joint-energy-mechanism-nomination.md)
records the source-version discrepancy in the external envelope lead,
its different prime/pole normalization and the retained local stops.
It is not an essential inaccessible source, and is not retried here.
Full matching Mathlib coverage is unchecked; supporting Fourier facts
do not constitute a matching full theorem.

## Bounded continuation and abandonment test

After separate approval, make one quantitative proof attempt at (P).
Continue only if the complete paid inequality holds uniformly over the
stated family, with denominator and correction controlled. A bound
depending on the individual w, a preserved L2 prime Rayleigh quotient,
or a core-form estimate missing poles fails this test. If uniformity
fails, save the exact failing estimate or a rigorous violating family
and reassess; do not broaden to higher derivatives, growing K or full
positivity without a new gate.

If obtained, (P) supplies a supported-family high-carrier penalty showing
why recurrence does not transfer L743 to a favorable energy quotient.
It could serve as a paid component of a finite-window lower certificate.
It leaves bounded-frequency signs, unrestricted envelope complexity,
moment complements and support-uniform assembly unresolved. It is a
standard-mechanism specialization, not a new creative route to RH.
