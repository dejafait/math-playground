# Rank-one Euler-product determinants — completed source scope

TARGET: Extract the determinant-convergence criterion and its unresolved finite-Euler-product estimate from Connes--Consani--Moscovici, Zeta Spectral Triples (arXiv:2511.22755v1), and determine one bounded arithmetic prerequisite distinct from the stopped Sonin-transport and Weil-converse routes.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact identifier/title and simple-even searches in local drafts/literature, ATTEMPTS and foundations found only the startup assessment and step356 lead for this construction; web queries and primary passages are recorded below. No novelty inference from search silence.
SOURCE_EVIDENCE: Connes--Consani--Moscovici 2511.22755v1, Lemma2.3, Proposition3.2, (3.10)-(3.22), Corollaries3.7-3.8, Section4 (4.1)-(4.14), Lemmas5.1-5.4 with proofs, Proposition5.7, Lemma5.8 with proof, Proposition5.9 and Theorem5.10 with complete proof, Sections7-8 including Lemmas7.1-7.3 and their proofs; Connes 2602.04022v1 Theorem6.1 statement and Sections6.4-6.6/Section7.4 opening comparison. Cited external prolate asymptotics and the infinite-dimensional real-zero theorem were not independently audited.
COMPARISON: The finite determinant/real-zero theorem assumes a simple-even minimum; shifting by that minimum makes the quotient form positive without proving Weil positivity. A stated trial-function transform limit leaves its comparison with the actual ground eigenfunction unresolved. Neither determinant convergence nor a quantitative arithmetic eigenfunction error follows by import.
GAP: Ground-state simplicity/parity, two limiting steps and a suitably normalized ground-state/trial-function comparison remain open; a single finite parity-gap certificate at lambda=sqrt(13), N=120 is independently testable, not their uniform solution.
REASON: Essential source scope is inspected. Retain one finite arithmetic-matrix hypothesis test as reproduction, while parking an unconditional determinant-to-Xi import. The separately nominated finite target needs next-turn approval before calculation.
SCOPE: One completed literature-only comparison; no determinant calculation, new lemma, source-proof repair or mathematical script. The finite continuation has its own exact-target assessment; no all-cutoff or infinite-operator claim is covered.
LITERATURE_REASON: At invocation start this distinct construction had REVIEW_REQUIRED coverage and essential primary passages were unread; this step completes that comparison.

## Sources, searches and overlap

Primary source: Alain Connes, Caterina Consani and Henri Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
27 November 2025. All numbered references below refer to that version.
Version-specific primary HTML supplies the statements and essential proof
cases; secondary reports supply no theorem or numerical certificate.

Queries: `"2511.22755" "simple" eigenvalue proof` and
`"Zeta Spectral Triples" "smallest" eigenvalue convergence`.
Results included numerical reproductions, informal claims and a primary
survey lead. Narrow local identifier/title/simple-even searches found no
matching prior assessment beyond step356; this establishes no originality.

Followed the lead to Alain Connes, *The Riemann Hypothesis: Past, Present
and a Letter Through Time*, [arXiv:2602.04022v1](https://arxiv.org/html/2602.04022v1),
3 February 2026. Theorem6.1 assumes a lower-bounded self-adjoint
convolution-kernel operator whose minimum is a simple isolated eigenvalue
with even eigenfunction. Section6.6 still lists simplicity/evenness and
accurate ground-state approximation as missing. Section6.5 Fact6.4
concerns trial functions; Section7.4's opening distinguishes their limit
from the needed eigenfunction comparison. This follow-up does not close
the gap. Its referenced Connes--van Suijlekom theorem was not independently
audited or used as another input.

Reused step356's packet/Gaussian/Sonin comparison. Read only the relevant
October30 nullvector-multiplier failure note and nodal-compression
assessment: a positive-ground-state or nonnegative-kernel theorem does
not pay the complete signed Weil form. No Perron property or modulus
contraction is imported. L758/L754 remain contrasts, not inputs.
No sibling notebook was consulted.

## Exact finite construction and qualifications

Fix lambda>1, L=2 log(lambda), integer N>=1. The source's orthonormal
basis on [lambda^(-1),lambda], extended by zero, is

    V_j(u)=L^(-1/2) exp(2 pi i j log(lambda u)/L), |j|<=N.

Put A=QW_lambda^N. Equations (3.10), (3.13), (4.1) specify

    A = W_(0,2) - W_R - sum_p W_p.

Lemma2.3 gives, for 0<=y<=L,

    q_nm(y) = [sin(2 pi m y/L)-sin(2 pi n y/L)]/[pi(n-m)] (n!=m),
    q_nn(y) = 2(1-y/L) cos(2 pi n y/L).

The point term is Lemma4.1 (4.2). The prime term is (4.3), the finite
sum of Lambda(k) k^(-1/2) q_nm(log k), 1<k<=exp(L). The archimedean
term is (4.4), with omega=q_nm:

    omega(0)/2 * [gamma + log(4 pi (exp(L)-1)/(exp(L)+1))]
    + integral_0^L [exp(y/2) omega(y)-omega(0)]/[exp(y)-exp(-y)] dy.

This retains zero-endpoint cancellation and the exterior principal-value
correction. Section4.3 also supplies special-function expressions and
their geometric-series proof. A future certificate may use the defining
regularized integral, avoiding a silent choice or repair of shorthand
normalization. No quadrature/error bound was calculated this turn.

Lemmas5.1-5.2 show A is real symmetric, commutes with j->-j, and has
the stated rank-two commutator with the diagonal scaling matrix.
Definition5.3 calls its minimum even-simple if it is simple with even
eigenvector. This is a hypothesis, not a conclusion of the displayed
matrix structure alone.

Theorem5.10 (=Theorem1.1) assumes that condition and normalizes xi by
delta_N(xi)=1, where delta_N=L^(-1/2) sum V_j. The paragraph before
Lemma5.4 proves nonzero overlap from the simple-even condition and
commutator, including the D xi=0 case; no positive-ground-function
or RH assumption is substituted for it.

The operator is self-adjoint on E'_N direct-sum E_N^perp, where
E'_N=E_N/C xi has the positive quotient form A-epsilon_N I. This
is not self-adjointness in the original unmodified E_N inner product
or a proof that epsilon_N>=0. For the spectral cut
(-1)^(-w)=exp(-i pi w), Lemma5.8 and Theorem5.10 give

    det_reg(D_log^(lambda,N)-z) = -i lambda^(-iz) xi_hat(z),
    xi_hat(z) = 2 L^(-1/2) sin(z L/2)
                * sum_{j=-N}^N xi_j/(z-2 pi j/L).

Proposition5.9 specifies pole cancellation, including zero coefficients.
The complete proof combines Lemma5.4's finite rank-one determinant
identity with direct-sum factorization into the finite self-adjoint
quotient and the unchanged outer lattice |j|>N. No original
self-adjointness or determinant reproof is attempted here.

## The two limits and the actual missing estimate

Section7 proposes N->infinity at fixed lambda, followed by
lambda->infinity with scalar normalization and the removable exponential
phase. The first limit is proposed locally uniformly in C toward the
transform of a boundary-normalized ground eigenfunction of full QW_lambda.
Proposition3.4's core convergence of lowest energies alone is not a
boundary-trace or eigenfunction convergence theorem.

The second proposed limit is a suitably scaled ground-eigenfunction
transform toward Xi. The opening outlook prints a one-sided strip
inequality; Lemma7.3 explicitly states |Im z|<1/2 and its proof uses
-1/2<alpha<1/2. Retain that symmetric open-strip scope, with compact
convergence sufficient for Hurwitz, not an extension to its boundary.
A nonzero normalized limit and simple-even hypotheses along the family
would still have to be established.

The source DOES give quantitative trial estimates: Lemma7.2 states
uniform O(lambda^(-2)) prolate-to-Hermite errors for suitably normalized
n=0,4, citing Meixner--Schaefke Satz9, p.243, and a compressed-Fourier
eigenvalue asymptotic. Lemma7.3 states convergence of the transform of
k_lambda=E(h_lambda); its proof displays the central comparison bound

    2 c lambda^(-1/2-alpha)/(1-2 alpha), -1/2<alpha<1/2,

followed by a kernel-tail argument. These complete passages were read;
external asymptotics and all truncation/normalization details were not
independently audited. This is a stated estimate for the trial function,
not for xi_lambda-k_lambda, and is not used for the finite continuation.

Section8 expressly leaves (a) simple-even ground states and (b) accurate
scalar-multiple approximation of xi_lambda by k_lambda open. Numerical
indications supply no norm, constant, spectral gap or all-parameter
estimate paying (b). Section6's 200-digit computations are not interval
certificates. Corollary3.8's zero limit of the decreasing full-form
minimum would already force Weil positivity/RH; it is not an independent
arithmetic shortcut.

## One retained prerequisite and its test

Retain only the source cell lambda=sqrt(13), N=120, used in Section6.
Seek certified separation of its lowest even eigenvalue from both the
second even and lowest odd eigenvalues. This pays one finite simple-even
hypothesis without assuming A>=0. No zeta zeros, prolate asymptotic,
spacing, zeta simplicity or positive Weil measure is an input.
The separate finite-parity assessment states the exact target/error test.

Continue only if rigorous enclosures give a positive separation after
all entry/spectral errors. Certified incompatible ordering/multiplicity
obstructs this cell; overlap is inconclusive. Do not sweep more cutoffs
for more numerical agreement. One successful cell leaves uniform
simplicity, both limits, eigenfunction approximation and RH open.
A creative residual/gap mechanism would need its own precise hypotheses
and source gate; no quantitative central comparison is ready here.

Mathlib: full matching and supporting coverage not checked; unknown is
not absent. No lemma or PROOF/DAG change is warranted by this review.
