# Degree24 tilted-Pollaczek source review2001

20 November 2026. Literature only. No polynomial, determinant, inertia,
root or new lemma was calculated. Main gap: L030-L032/C032a actual-Xi
all-degree mixed positivity. C028b's multiplicity-weighted H_d=o(d)
and C029j's signed payment remain unresolved branch context.

The intermediate target remains the exact degree24 diagnostic nominated
in assessment2000. A certified negative index at most one would retain
the proposed uniform one-pair mechanism for investigation; at least two
would stop that proposed bound. Neither outcome decides RH. A uniform
bound, compact convergence for the weighted family, multiplicities and
actual-Xi symmetry transfer are separate unpaid steps.

## Exact source data

Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008), 561-569,
[DOI](https://doi.org/10.4153/CMB-2008-055-0),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-3-function-in-meixner-pollaczek-polynomials.pdf).
Reused discovery2000's Theorem2.1 proof inspection; reaccessed the
definition p562, (2)-(5) p563, (13)-(14) p566, and the full weighted
truncation/numerical qualification pp568-569. The indexed primary text
is legible for these formulas; a search-engine extract separately
misrenders the basis parameter, so that extract is not the input.
Screenshot requests returned references without image payloads; no
visual inspection is claimed. Direct shell retrieval failed DNS, but
the publisher's primary indexed PDF was accessible through web tools.

Use source b_n renamed beta_n, and source tilde-b_n renamed u_n.
The exact normalization is p_n(t)=P_n^(3/4)(t/2;pi/2), with p_0=1,
p_(-1)=0 and source recurrence (2)

    (n+1)p_(n+1)(t) = t p_n(t) - (n+1/2)p_(n-1)(t).

Source (13), a finite formula rather than an asymptotic approximation,
reads

    u_n = -n!/sqrt(2) * sum_(k=0)^n
      [4^k (4^(k+1)-1) B_(2k+2) (2pi)^(k+1)
       * sin(pi(n-k)/2+pi/8) / ((n-k)! (2k+2)!)].

Source (4) reads

    beta_n = 4n(n-1)u_(n-2) + (8n^2+12n+7)u_n
             + (2n+3)(2n+5)u_(n+2).

For n=0,1 omit the first term, whose coefficient is zero; do not
evaluate a negative-index u. Formula (3) defines the same u as the
n-th derivative at zero of

    -1/4 * sqrt(pi/x) * sin(x+pi/8) * tanh(sqrt(2pi*x)).

Equation (14) is an alternate recurrence, not required by this method.
The author explicitly warns of cancellation in (13) and instability
in (14); ordinary high-precision agreement is not certification.
Use all beta_0,...,beta_24, requiring u_0,...,u_26 and even Bernoulli
numbers through B_54. The source weights on p568 are exactly
m_(24,k)=24!/((24-k)!24^k), k=0,...,24. The finite target is

    T_24(t) = sum_(k=0)^24 m_(24,k) beta_k p_k(t).

Its degree must be certified, not inferred from its name. Source p569
reports one conjugate pair only numerically at degrees6-20; no degree24
certificate or uniform bound is supplied. The weighted convergence
remark and ordinary Jensen multiplier theorem are not imported here.

## Multiplicities, rank and inertia

Michel Coste, *An Introduction to Semialgebraic Geometry*, October2002,
[author PDF](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf),
Section1.4.1 pp17-18, Exercise1.13, Theorem1.14 and its complete proof,
and Section1.4.2 p19, Jacobi's theorem/Exercise1.16 were inspected.
Hypothesis: a nonconstant real polynomial of actual degree d. Newton
sums count roots with algebraic multiplicity; H=(s_(i+j)) for
0<=i,j<d. Rank counts distinct complex roots; signature counts distinct
real roots. The theorem permits repeated roots and singular H.

For an explicit multiplicity-aware proof, also inspected Daniel Plaumann,
*Real Algebraic Geometry*, IHP lectures (2023), Section1,
[primary lecture notes](https://rtca2023.github.io/pages_Paris/files_m5/rag-ihp.pdf),
Theorem1.1 and full proof, slides3-4. With r distinct real roots and c
distinct nonreal conjugate pairs, that proof gives inertia
(r+c,c,d-r-2c); the positive multiplicity factors do not change the
signs. This is a cited standard result, not a new local derivation.
Thus negative index means distinct conjugate pairs. A nonsingular H
also certifies simplicity; a singular H does not bound nonreal
algebraic multiplicity merely by its negative index.

Reuse notes1601's Nathanson1911.01745v2 Theorem1/Lemmas1-2 and its
repeated/distinct-root cases for the PSD baseline; it alone was not
the full inertia source. No reproof or RH-dependent premise is needed.

## Approved finite certificate method and failure policy

Coste p19's Jacobi theorem applies when **every** leading determinant
Delta_j=det(H[0:j,0:j]) is nonzero. Count changes of sign in
(1,Delta_1,...,Delta_d) for the negative index. This condition must be
proved by enclosures for the actual coefficients, not a rounded matrix.
Coste's general zero-minor rules are outside the approved implementation;
a zero-containing enclosure gives an unresolved result, not a zero sign.

The primary [Arb2.23 matrix manual](https://www.arblib.org/arb_mat.html),
LU/determinant and LDL sections, and
[FLINT arb_mat reference](https://flintlib.org/doc/arb_mat/index.html),
arb_mat_det/arb_mat_det_lu and module enclosure convention, were read.
These determinant routines enclose the exact determinant, including
indefinite/singular inputs. The documented arb_mat_ldl success criterion
is positive definiteness; it is not a general indefinite-inertia API.
Approximate linear algebra and midpoint-only conversions cannot certify
the result. Current FLINT docs label parts LLM-generated; the older
Arb manual provides an independent version of the relevant contract.

[python-flint0.9 arb_mat.det](https://python-flint.readthedocs.io/en/latest/arb_mat.html#flint.arb_mat.det)
and [arb](https://python-flint.readthedocs.io/en/latest/arb.html),
constructor, pi, sin, sqrt, Bernoulli and endpoint/containment sections,
identify a suitable binding. Use exact integer/rational inputs and
enclosing elementary functions throughout. Do not convert an ordinary
floating approximation into an alleged exact input. Newton identities
are recorded in Coste Exercise1.13, with different formulas at j<=d
and j>d. For d=24 all sums through s_46 are needed.

The next calculation must save every coefficient enclosure, verified
degree, s_0,...,s_46, all 24 determinant enclosures/signs and the full
inertia/nullity conclusion, together with precision, library versions,
method, reproduction command and any failed separation. Bound precision
escalation in advance (for example 256,512,1024,2048 bits), retaining
failed runs. If a leading coefficient or minor still contains zero,
report incomplete certification; do not assume simplicity, drop terms,
or substitute a root plot. A different zero-minor method needs its own
source approval. A passing nonsingular certificate is a finite test only.

Operational qualification: default python3 has no flint, mpmath or sympy
module (read-only import-spec check). No package was installed. A usable
Arb binding/runtime must be located or provisioned within authorized
paths before calculation; mathematical source coverage is ready, runtime
availability is not asserted. mpmath documentation was a fallback lead,
not an approved replacement for this certificate method.

## Comparison, novelty and routing

Local searches/readings were limited to discovery2000, source-notes1601,
the October30 weighted-family overlap stop, and universal discrete-step
stop111. The latter cites L955's generic obstruction; the former cites
L530's two-atom family. Neither supplies this actual tilted coefficient
calculation or prohibits it. Their proofs were not re-audited. No exact
degree24 result was found in the recorded searches; that is not novelty.
Queries this turn included Hermite trace-form/rank/signature/Coste,
Kuznetsov Jensen-weighted degree24 zeros, and certified Arb inertia.
Only primary texts/manuals above support the approval.

Decision: SPECIALIZE, limited to the fixed finite diagnostic by these
known algorithms. No original uniform mechanism has been identified;
routine coefficient evaluation is REPRODUCTION, not creative proof.
No relevant Mathlib coverage was checked. No lemma or script writes;
PROOF/DAG unchanged. Source coverage now changes the route from missing
essential theorem hypotheses to a source-ready calculation, subject to
the supervisor's separate approval of this changed assessment.
