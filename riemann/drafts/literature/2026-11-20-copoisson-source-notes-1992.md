# Co-Poisson coefficient-interface source review1992

20 November 2026. Literature only; no theorem imported or reproved.
Main gap: L030-L032/C032a; this branch requires C028b's H_d=o(d).
The intermediate test was an actual-coefficient identity with a controlled
signed remainder, potentially paying C029j's window upper estimate.

## Primary source and relevant proof cases

Burnol, *Two complete and minimal systems associated with the zeros of
the Riemann zeta function*, JTNB16(1)(2004),65-94,
[arXiv math/0203120v7, 25 February2004](https://arxiv.org/html/math/0203120v7).
Read Sections1-3; Section5 Theorem5.2 and complete proof; Section6
Propositions6.1-6.4 and its reference for the complement identification.

Here K=L2(0,infinity;dt); L_a consists of functions and cosine transforms
constant on (0,a); K_a requires both to vanish there. Right Mellin
transform is integral f(t)t^(-s)dt; completion multiplies by
pi^(-s/2)Gamma(s/2). Proposition2.2 allows poles at0,1.
For 0<a<1, Definition4 uses integrable g supported in [a,1/a]
whose co-Poisson sum is L2. Theorem3.1 identifies P_a=Y_a perpendicular;
Y_a spans completed zero evaluators, including all k<m_rho.
Theorem5.2 assumes rapid decrease in vertical strips. Note13 groups
zeros by special heights before absolute values/norms; multiple zeros
mean residues. Its proof controls horizontal contours and then vertical
integrals, not individual absolute residue summability.
Proposition6.1 treats a>1 by negative exponential type, a=1 by
minimal type and Paley-Wiener. Section6 refers the complement proof
upstream. These are source statements/cases, not a new local proof.

Burnol, *On Fourier and Zeta(s)*, final version for Forum Mathematicum,
[arXiv math/0112254v6, 11 March2003](https://arxiv.org/html/math/0112254v6).
Read Theorems6.24-6.25 with complete proofs, Note6.26 and Proposition6.27.
For 0<lambda<1, Lambda=1/lambda, Theorem6.25 identifies the orthogonal
complement inside K_lambda with L2 sums A(u)=sum g(u/n)/n,
g supported in [lambda,Lambda], integral g=0. Necessarily g is L2
and integral g(u)/u du=0. Forward proof divides the Mellin transform
by zeta, uses finite exponential type, Theorem6.24 and Paley-Wiener;
Fubini is used in Re(s)>1. Converse removes a delta at0 using L2,
then uses the second moment condition and co-Poisson identity.
Theorem6.24 converts zeta-weighted L2 integrability to unweighted L2
for an entire finite-exponential-type function; its proof uses Hardy
Cauchy projections. Proposition6.27 gives bounded division at fixed
support via finite Mobius inversion. Earlier supporting proofs remain
cited, not independently audited. No uniform shrinking-support bound
is imported.

## Local applicability and decisive missing interface

Read C029j in full, C028d's hypotheses/conclusion and centering proof,
and C028e's hypotheses/conclusion and coefficient interface. Reuse their
existing audits and the earlier source-notes1991 failure comparison.
The original construction review of October31 was read for its exact
conditional direct-pair stop and its explicitly unread Burnol lead.
No cross-notebook input is used.

The actual family is b_j=gamma_j/gamma_0,
P_d(x)=sum binom(d,j)b_j x^(d-j), Q_d(y)=P_d(y-b_1),
t_d(y)=d^(-1)log|Q_d(y)/y^d|. C029j pays the difference between
(L/q)log Z and integral_[-Ad,Ad]t_d, with d>=3,A>=1,
q=1/(4d), L=2Ad; its error is at most C/(8d).
The missing threshold is ordered limsup_A limsup_d (L/q)log Z<=0.
C028e supplies only the exterior contract. These facts are reused,
not rederived or strengthened here.

Neither inspected source theorem identifies b_j or Q_d as the transform
or projection of a specified admissible vector. The Gaussian Mellin
formula in Section1 is not such an identification for the centered
finite polynomial and its logarithm. There is no source theorem here
transferring a Hilbert norm, evaluator completeness, or fixed-support
inverse bound to that signed integral with its growing L/q factor.
Even Theorem5.2 requires a specified rapidly decreasing member of its
space; membership for a desired local observable has not been supplied.
Its grouped series cannot silently be differentiated, logged, or
integrated in this degree-dependent observable. This is an applicability
failure, not a new mathematical counterexample or a global no-go result.

Continue this interface only upon a specified actual vector/coefficient
identification plus an independently bounded signed transfer. That test
fails for automatic import from the inspected statements. Park dependent
work; retain all multiplicities, endpoints, null sets, external
qualifications and the ordered limits. No RH, simplicity, real roots,
positive actual-pair kernel or signed-mean sign is assumed. Full matching
Mathlib coverage is unchecked. No lemma, script, PROOF or DAG change.

## Decision and continuation

Outcome NEGATIVE: primary theorem/proof scope now resolves an unread
lead and changes the route from possible import to parked interface.
This is local source progress only; no advance beyond those sources.
No justified creative target emerged: an independent signed input is
still absent. The next prerequisite uses prime-power explicit-formula
cancellation rather than a co-Poisson norm or projection. It remains
REVIEW_REQUIRED, with no same-turn derivation or approval.
