# Gaussian compensation and endpoint zeros — source assessment

TARGET: Assess source coverage for Gaussian-compensating polynomial packets with growing-order endpoint zeros, retaining original TV, the complete target response and uniform closed-band costs.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step345 searched truncated-exponential/Jacobi asymptotics, partial exponential sums/Szego/incomplete gamma, exact Laguerre/Gaussian/endpoint packets and Gaussian-compensation Fourier terminology; reused reviews329/332 and compared C997f/g/i/l and failures340/341. No inspected theorem decides the exact normalized complete response; no novelty inferred.
SOURCE_EVIDENCE: Read NIST DLMF8.2.1-5,8.4.7-11,8.11.13-19 with real-uniformity clause,1.10.1-2 and10.9.4 with order condition; read Charpentier-Levenberg-Wielonsky arXiv2401.11955v1 Theorem2.4 and full proof pp6-7 with preceding assumptions pp4-6. Reuse review329's weighted L1/complex-growth contracts, review332's Cauchy/measure contracts and audited C997c/e.
COMPARISON: Exact incomplete-gamma identities and Taylor/Cauchy tools cover finite-exponential errors without assuming compensation on complex contours. Poisson's Bessel integral covers a plain endpoint weight only; weighted best-approximation theory does not evaluate this prescribed packet. C997i applies whenever its actual degree<=n and fixed A>=max{A_0,6553600}; C997f/g/l do not automatically apply to endpoint zeros in c.
GAP: The fixed-parameter family's original M_n normalization, complete target noncancellation and uniform closed-J response rates remain mathematical work. Neither real-axis compensation nor endpoint vanishing supplies these estimates by citation.
REASON: Essential elementary truncation and contour tools are accessible; broader asymptotics are nonessential to a bounded explicit-family test. EXPLORE permits that test without claiming a successful rate, a parameter choice or coverage by a matching theorem. The separate continuation assessment345 preserves the exact family.
LITERATURE_REASON: The new nomination couples a growing-order endpoint factor to a truncated exponential intended to compensate the Gaussian; its exact complex truncation and cutoff costs have not received theorem-level comparison. Reuse ready sources and inspect only the missing contracts.
SCOPE: The single prospective family below with fixed positive theta and lambda, fixed admissible A before n, kappa=2(theta+lambda), original TV normalization, C997c's complete response, J=[15/8,17/8] and z_star=1+i/8. No varying parameters, all-packet claim or actual-zero transfer.

## Exact proposed family, not a mathematical conclusion

The nomination below was REVIEW_REQUIRED at step344. The separate
literature-only step345 completes its tool/obstruction comparison in
the final section; the family and simultaneous-rate test are unchanged.

Write x=c-2. Choose fixed theta>0, lambda>0 and one A in C997e's
admissible range before n. Set kappa=2(theta+lambda) and prescribe

    q_n=floor(theta*n), r_n=floor(lambda*n),
    E_r(u)=sum_(j=0)^r u^j/j!,
    P_n(c)=(1-64*x^2)^q_n * E_(r_n)(A*n*x^2),
    M_n=integral_J exp(-A*n*x^2)*|P_n(c)|dc,
    dmu_n(c)=M_n^(-1)*1_J(c)*exp(-A*n*x^2)*P_n(c)
                                      *exp(i*n*(phi(c)-c))dc.

Here phi is exactly C997e's real phase and the intended degree budget
is floor(kappa*n), within review329's general polynomial class.
No response derivatives are prescribed at 2. The finite exponential
is intended to reduce the Gaussian localization; the endpoint factor
is intended to pay the truncation-boundary contribution in the
oscillatory data integral. These are motivations, not verified effects.
Neither E_r(u)~exp(u) on a complex contour nor any weighted norm
equivalence may be asserted without a uniform error and its charge.
No parameter choice or successful sequence is claimed in this file.

The later bounded mathematical test, only after coverage is ready, is
whether some fixed admissible parameters give both

    |H_n^+(1+i/8;mu_n)| >= exp(-a_n), a_n>=0, a_n/n->0,
    sup_(gamma in J)|H_n^+(gamma;mu_n)| <= exp(-sigma*n), sigma>0,

on an unbounded integer subsequence, or whether a rigorous conflicting
rate stops this specified family. Failure to prove an upper estimate
is inconclusive. Original M_n, both endpoints, both Laguerre branches,
both beta terms, both short intervals and K's -1 must all be retained.

## Source review and comparison boundary

Reuse review329's inspected weighted-polynomial contracts and C997e's
audited exact analytic amplitudes. Search the exact family and standard
finite exponential, incomplete gamma and growing endpoint-weight
terminology; those are currently unread leads, not theorem inputs.
Retrieve precise primary hypotheses and essential proof cases only
where existing contracts do not suffice. A whole-line Gaussian or a
Fourier transform of a Jacobi weight cannot silently replace this
complete response. No fresh broad survey or repeat access attempt for
the old nonessential blocked references is requested.

The nomination is distinct from C997f's linear binomial phase and
C997l's exact complete-response jets. The large-A C997i obstruction
must be applied whenever its degree and parameter hypotheses hold;
allowing a different fixed kappa is not evidence that its mechanism
has been overcome. If review finds an already stopped regime, record
that overlap rather than rederive it. Do not optimize the quarter-jet
fraction or reopen dual340/341 without their missing actual-tail input.
Historical stops293/316/327/331 and the full-jet stop remain evidence
on their stated scopes. No absence of a theorem or novelty is inferred.

Main gap remains L030-L032/C032a actual-Xi positivity and L966/L968
signed forcing, with L984(H) unpaid. An actual target-retaining packet
with suppressed band data would test the point bridge following
C997c branch recovery; an incompatible rate would instead close this
specified candidate. Neither would establish the signed assay or RH.

Essential local inputs for any later attempt are C997c(1),(4)-(6) and
C997e(4),(15)-(16), with L997(4),(7) through those imported contracts.
C997l/C997g/C997f/C997i are comparison results, not positivity premises.
All normalization, compensation, noncancellation, uniform-band and
parameter-existence estimates for the proposed family are unresolved.
Independent point-bridge, selected/both-sign transfer, C997a(8),
original assay, reconstruction, signed recovery, complements,
regulators, L993 and L984(H) remain unpaid. Full matching Mathlib
coverage is unchecked; no cross-notebook input is proposed.

At step344 this file nominated a separate literature-only comparison,
without deriving a lemma or approving mathematics. Step345 below
supersedes that source gate only. The accepted quarter-jet audit does
not depend on the proposed family or this review.

## Separate literature-only comparison — step345, 11 November 2026

### Exact finite exponential: inspected primary contracts

NIST DLMF, live sections retrieved 11 November 2026; release identifier
not independently checked in this step. In the following source formulas
the integer index is r, not the packet index n.

**Exact identities.** [DLMF8.4.7-11](https://dlmf.nist.gov/8.4#E7)
defines e_r(u)=sum_(j=0)^r u^j/j! for r=0,1,... and complex u, and states

    gamma(r+1,u)=r!*(1-exp(-u)*e_r(u)),
    Gamma(r+1,u)=r!*exp(-u)*e_r(u).

These are exact, not asymptotic. The nomination's E_r is this e_r,
not DLMF's generalized exponential integral E_p. They apply to
r=floor(lambda*n) and u=A*n*(c-2)^2, including complex c. This
identifies the compensation error; no smallness estimate is asserted.

**Integral representation and paths.**
[DLMF8.2.1-5](https://dlmf.nist.gov/8.2#E1) defines
gamma(a,u)=integral_0^u t^(a-1)*exp(-t)dt for Re(a)>0 and gives the
normalized P,Q and P+Q=1. Its principal-value/path qualifications were
read. Here a=r+1 is a positive integer, so the integrand is entire and
the straight finite segment is available, including the value at u=0.
A later proof can bound this exact finite integral on a specified
complex contour without invoking a uniform incomplete-gamma asymptotic.
The exponential size of that bound, its multiplication by the endpoint
factor and division by original M_n must all be calculated later.

**Real limits are insufficient.**
[DLMF8.11.13-19](https://dlmf.nist.gov/8.11#E13) states that
exp(-r*x)*e_r(r*x) tends to 1 for 0<=x<1, to 1/2 at x=1,
and to 0 for x>1. Its S_r expansion is uniform for real
x in (-infinity,1-delta], delta>0, not for a complex contour. The
transition is thus part of the known source landscape, not automatic
Gaussian compensation. No moving-argument or contour consequence of
these real statements is imported. Sections8.11(i)-(ii)'s fixed-a or
fixed-u asymptotics are also not a substitute for this coupled limit.

**Elementary complex tools.**
[DLMF1.10.1-2](https://dlmf.nist.gov/1.10#E1) states Taylor's theorem
on an analytic disk and the entire exponential series. Reuse
review332's inspected Cauchy derivative formula, with closed-contour
continuity and interior holomorphy. Finite E_r and the integer endpoint
factor are polynomials; contour deformation still requires C997e's
fixed amplitude domain. Neither a bounded analytic amplitude nor its
old Gaussian remainder absorbs a degree-growing multiplier for free.
No reproof of Taylor, Cauchy or incomplete-gamma theory is proposed.

### Endpoint transform and stronger approximation comparison

[DLMF10.9.4](https://dlmf.nist.gov/10.9#E4), Poisson's integral, states

    J_nu(z)=2*(z/2)^nu/(sqrt(pi)*Gamma(nu+1/2))
                *integral_0^1 (1-t^2)^(nu-1/2)*cos(z*t)dt,
    Re(nu)>-1/2, z complex.

The order condition and complex variable were read. This is an exact
identity for a plain endpoint-weight transform, valid at each allowed
order; it supplies no uniform growing-order asymptotic by itself.
The proposed integral also contains the finite exponential, Gaussian,
nonconstant analytic amplitudes and an additional Laguerre branch.
Replacing it by this Bessel transform would leave essential errors
unpaid. It is comparison evidence, not a packet response formula.

S. Charpentier, N. Levenberg and F. Wielonsky,
[*Weighted holomorphic polynomial approximation*, arXiv:2401.11955v1](https://arxiv.org/pdf/2401.11955v1),
22 January 2024 arXiv stamp, manuscript dated23 January2024,
Theorem2.4 and full proof, printed pp6-7, with preceding conventions
pp4-6: assume regular compact K subset G, C\\K connected, an
approximation pair (G,W), W entire and nonvanishing in G, f continuous
on K, R<0. Geometric best-approximation rate at most exp(R) is
equivalent to holomorphic extension to the component containing K of
K_R={U^(mu_(K,Q))+Q-F_(K,Q)>R}, Q=-log|W|. The forward construction
uses weighted Fekete interpolation/Hermite remainder; the converse
controls telescoping weighted approximants by polynomial approximation
of W. This is best approximation by freely chosen polynomials. It
does not establish the approximation-pair hypothesis for our weight,
evaluate our prescribed E_r product, charge M_n or bound the complete
response. It is not imported as a packet theorem or reproved. Even a
matching best slope-polynomial approximation would need a separate
integral-response realization argument.

### Duplicate/failure screen and access record

Reused review329's inspected Theorem4.13/(4.15), Example4.14 and
varying-field L1 qualifications; review332's coefficient and
finite-complex-measure contracts; audited C997c(1),(4)-(6) and
C997e(4),(15)-(16). These remain applicable tools with their original
hypotheses, rather than new external discoveries. Read the stated
hypotheses/conclusions of C997f/g/i/l, relevant exact-amplitude ranges
of C997e, and both failure340/341 records.

C997f's multiplier is (1+i*tau*(c-2))^floor(kappa*n), with
A>kappa*tau^2/2; its target-loss theorem is not about this even
endpoint/truncation product. C997g and C997l impose complete-response
jets at ordinate2. Zeros of the slope polynomial at c=15/8,17/8
are different constraints; those theorems are not applied without
their jet hypotheses. C997i's audited conclusion DOES apply whenever
the actual polynomial has degree<=n and fixed
A>=max{A_0,6553600}. Its obstruction already excludes simultaneous
retention and suppression there. A larger declared degree budget
alone does not remove this conditional overlap, nor authorize extending
its degree<=n proof. No smaller admissible-A interval is known nonempty.

Failures340/341 leave the actual target spectral tail unpaid; no new
algebraic dual regularization is proposed. Stops293/316/327 and the
quarter/full-jet stops remain on their recorded scopes. No historical
stop is promoted to an all-family exclusion.

Search queries included `"truncated exponential" "Jacobi" asymptotics
varying weight`, `"partial sums" "exponential function" "Szego"
uniform asymptotics incomplete gamma`, `"Laguerre" "Gaussian"
"endpoint zeros" polynomial packets`, and `Gaussian compensation
polynomial (1-x^2) truncated exponential Fourier exponential n varying
weight`. Also followed the Pritsker-Varga Szego/weighted-approximation
lead to the primary 2024 comparison above. Search snippets were used
only for discovery; no failed search establishes novelty.

Pritsker-Varga, *The Szego curve, zero distribution and weighted
approximation*, Trans. AMS349(1997),4085-4105: author PDF96a timed out
twice and the AMS PDF returned403. Its theorem/proof was not read;
no theorem from it is imported. Citeseer, book-chapter, Haimi-Hedenmalm
and other search hits remain unread/nonessential leads. These access
failures do not block the elementary exact remainder approach, so no
further access retry is scheduled. DLMF18.17 was located but no
specific Jacobi transform from that page is used. PDF screenshot
requests for the inspected 2024 paper failed; its complete relevant
proof text was accessible and read.

### Decision and bounded continuation

The source gate is EXPLORE: a bounded attempt on the unchanged
explicit family is supported by inspected exact formulas and reused
analytic/norm tools, without presuming any response estimate. No
indispensable source is missing for such an attempt. A stronger
incomplete-gamma asymptotic, growing-order Bessel asymptotic or
best-approximation theorem would be optional, not an excuse to repeat
literature instead of testing the exact finite integrals.

The single continuation is recorded with an exact mathematical TARGET
in [assessment345](2026-11-11-gaussian-compensation-endpoint-packet-test-review-345.md).
It must account for original M_n, both c endpoints, both analytic
Laguerre branches, both beta terms, both short intervals and K's -1.
Success means both specified rates for some fixed admissible parameters;
an actual conflicting rate stops only its proved parameter scope.
An inconclusive contour envelope is not a negative result. No parameter
feasibility, target lower bound or band upper bound was derived in this
literature turn. Full matching Mathlib coverage remains unchecked;
no cross-notebook input, new lemma or mathematical script was used.
