# Companion logarithmic regularization: source review1994

Literature-only work for assessment1993. No new degree-uniform estimate,
counterexample, lemma, or mathematical program is established here.
The proposed fixed-interval obstruction below is unproved and reserved
for a separately approved mathematical turn.

## Question and local contracts

The main gap remains actual-Xi all-degree mixed positivity, and on this
branch C028b's RH-equivalent H_d=o(d). The intermediate question is
whether the specified monomial companion permits polynomial-scale
regularization before estimating C029j's signed window. Even successful
regularization would not pay that signed estimate.

Read C028b, C028d's hypotheses, conclusions and finite centered
coefficients, C028e, C029i's hypotheses and common growth contract,
and C029j. These fix every integer d>=3, b_j=gamma_j/gamma_0,
P_d(x)=sum binom(d,j)b_j*x^(d-j), Q_d(y)=P_d(y-b_1),
t_d=d^(-1)log|Q_d(y)|-log|y| and the finite null-set convention.
C029i records the existing actual-family bound log F(r)<=K_0*r^(3/4)
for r>=1, with fixed K_0, and b_j>0. This is an existing contract,
not a growth estimate derived in this source review. Its proof was not
re-audited. C028d retains all real-root multiplicities.

Read the complete stop records1525/1588/1713, and the relevant
source-notes1523 passage already assessing the companion convention.
The stopped costs are Hermitian-imaginary-part trace norms under specified
similarities. They neither bound this regularization error nor supply its
small-singular-value hypotheses. Scoped searches of C028*/C029*, the
companion stop records and companion assessments found no existing
Cauchy-Binet/unit-minor regularization test in those paths. This is a
bounded overlap check, not a novelty claim or an archive-wide search.

## Primary statements inspected

### Determinantal Hermitization

Charles Bordenave and Djalil Chafai, *Around the circular law*,
arXiv:1109.3343v4 (13 March 2012), author PDF headed as an update of
Probability Surveys 9 (2012), compiled 27 November 2024:
[Section 4.1, (4.7), Lemma 4.3 and Remark 4.4, printed pp.15-17](https://arxiv.org/pdf/1109.3343).
For any finite complex matrix, (4.7) identifies its normalized
log-determinant with the singular-value logarithmic integral off its
spectrum. Lemma 4.3 assumes weak convergence of shifted singular-value
measures AND logarithmic uniform integrability, for planar-almost-every
shift, almost surely; its alternate version uses convergence in
probability. It concludes weak spectral convergence and a limiting
potential identity. Read its entire proof: Fubini fixes a realization,
Lemma 4.5 transfers logarithmic integrability by majorization, and
tightness/potential uniqueness identifies the limit. Read Lemma 4.5's
hypotheses and deterministic proof as well. Section 4.2's Lemmas
4.11-4.12 obtain small-singular-value estimates using an iid random
matrix, not an arbitrary deterministic perturbation alone. Section 1,
printed pp.5-6, also gives the nilpotent-shift/rank-one perturbation
example; the resulting limiting spectra differ despite small perturbation.

Applicability comparison: a deterministic sequence can be represented on
a one-point probability space; randomness is not itself an obstruction
to the conditional Hermitization lemma. Its hypotheses still must be
verified. In this notebook neither their singular-value convergence nor
their logarithmic uniform integrability has been supplied. Furthermore,
planar-almost-every-shift assertions do not justify restricting to the
real line, and fixed-shift convergence supplies no rate on [-Ad,Ad].
The nilpotent example is a warning against automatic transfer, not a
counterexample for the actual Jensen companions. No theorem here gives
the nominated error bound or its sign.

### Replacement principle

Terence Tao and Van Vu, with appendix by Manjunath Krishnapur,
*Random matrices: Universality of ESDs and the circular law*,
[arXiv:0807.4898v5, 23 April 2009, Theorem 2.1, (9)-(11), printed pp.13-14;
Lemma 3.1 and its proof, pp.15-16](https://arxiv.org/pdf/0807.4898).
Theorem 2.1 assumes n^(-2)(||A_n||_HS^2+||B_n||_HS^2) bounded
in probability (or almost surely), and convergence to zero of the
normalized shifted log-determinant difference for planar-almost-every z.
It concludes convergence of the corresponding normalized empirical
spectral-measure difference. Independence is not required by this
conditional principle. Lemma 3.1 works on a finite measure space,
assuming a uniform L^(1+delta) bound and a.e. pointwise convergence;
its proof truncates tails before bounded convergence. Equation (11)
gives the finite determinant/singular-value product identity.

Applicability comparison: this principle assumes the log-determinant
comparison rather than producing it. Its weak spectral conclusion is
not an unscaled real-window L1 estimate. C029i bounds t_d itself;
it does not bound the proposed regularized difference or prove that
difference tends to zero. No deterministic replacement theorem is
imported under an unverified norm or convergence hypothesis.

### A genuinely noisy deterministic-equivalence theorem

Martin Vogel and Ofer Zeitouni, *Deterministic equivalence for noisy
perturbations*, [arXiv:2001.09024v1, 24 January 2020, Assumption 2 and
Theorem 3/(1.3)-(1.6), pp.1-2](https://arxiv.org/pdf/2001.09024).
The deterministic A has ||A||=O(N^kappa_2). The random noise G needs
E||G||=O(N^kappa_1) and the stated anti-concentration bound for
s_N(D+G). The cutoff obeys C*N^(-L)<=alpha<=1 and the count below
alpha is at most nu_N*N/log N, nu_N=o(1). For tau>0 and sufficiently
large fixed gamma, N^(-gamma)<=delta<<N^(-kappa_1)*alpha/tau.
The conclusion compares N^(-1)log|det(A+delta G)| with
N^(-1)*sum_(s_j>alpha) log s_j, with error
O(nu_N+alpha^(-1)*N^kappa_1*delta*tau) and probability at least
1-epsilon_N(kappa_2+gamma)-1/tau. Theorem 1 is its Gaussian precursor.
Read these complete statements, not the probabilistic proof. Section 2,
(2.1)-(2.2), also states the finite singular-vector decomposition.

Applicability comparison: adding epsilon^2 I inside a deterministic Gram
determinant is not adding delta G to A. No noise or anti-concentration
is present here; the stated norm and cutoff-count assumptions have not
been verified either. This new lead does not remove the missing input.
The unnormalized introductory potential formula is not used; the
theorem's explicit 1/N factors are retained. No theorem imported.

### Companion convention, already covered

Nicholas J. Higham, *What Is a Companion Matrix?*, 23 March 2021,
[opening definition, determinant identity (*) and the transposed/permuted
conventions](https://nhigham.com/2021/03/23/what-is-a-companion-matrix/).
Reuse source-notes1523; rechecked only the relevant convention. The
monic polynomial y^d+c_(d,1)y^(d-1)+...+c_(d,d) has the Frobenius
companion with subdiagonal ones and last column
(-c_(d,d),...,-c_(d,1))^T. Its characteristic polynomial in the
det(yI-A_d) convention is Q_d, including algebraic multiplicities.
The real coefficients make yI-A_d real for real y. Distinct roots,
normality and invertibility of A_d are unnecessary for this identity.
The source's formulas for singular values of A_d alone do not give the
shifted family yI-A_d. No such inference is made.

### Finite minor expansion for a discriminating test

Oliver Knill, *Cauchy-Binet for pseudo-determinants*, author manuscript
dated 10 June 2014,
[Section 5, Theorem 7 and Corollaries 8-9, printed pp.16-17;
Section 6, Lemmas 11-13 and proof of Theorem 7, pp.18-19](https://people.math.harvard.edu/~knill/graphgeometry/papers/bi.pdf).
For real n-by-m F, the ordinary determinant identity is
det(I+z F^T F)=sum_P z^|P| det(F_P)^2, over square minors of all
sizes, including the empty minor with determinant 1. Read the complete
exterior-power proof, including the k=0 convention. No rank,
diagonalizability, root-separation or positivity assumption on F is
required. Only this ordinary determinant identity is relevant; no
pseudo-determinant claim is used.

Applicability comparison: the required Gram determinant has a real
matrix at real y and epsilon>0. Scaling the cited identity is within
its hypotheses. A future attempt may isolate a single (d-1)-minor
and compare its contribution with the actual polynomial. The value of
that minor, the epsilon powers, the actual coefficient upper bound and
the integrated asymptotic remain to be checked in that attempt. No
regularization obstruction or degree-uniform estimate is proved here.

## Precise missing estimate and disposition

Put M_d(y)=yI-A_d and s_j=s_j(M_d(y)). The imported finite
singular-value decomposition and determinant product identify the
proposed regularization discrepancy, off det M_d=0, with the standard
scalar spectral expression

    D_(d,epsilon)(y)=(1/(2d))*sum_(j=1)^d log(1+epsilon^2/s_j^2).

This is the finite spectral-calculus dictionary, not a new estimate or
an assertion of uniform convergence. The reference -log|y| cancels in
this difference. Its value on the finite exceptional set is immaterial.
The original target requires integral_[-Ad,Ad] D_(d,d^-K)->0 for every
fixed A>=1 and one fixed finite K>0. Positive summands require control
of the full small-singular-value logarithmic contribution, not just a
weak singular-value law or an unweighted count. Pointwise convergence
at each fixed degree, a cutoff chosen separately in each degree, and
bounded error after dividing the window integral by its length all
miss this target. No sufficient quantitative estimate is claimed here.

Decision: park automatic Hermitization/noisy-equivalence import. The
primary sources do not establish the target under the existing
contracts; this is a source-scope negative, not a universal no-go.
Knill's identity isolates an independent deterministic obstruction test:
on I=[b_1+1/4,b_1+1/2], compare the specified subdiagonal minor with
the polynomial using the already recorded entire-growth bound.
Seek a positive lower liminf for the integrated discrepancy on I for
every fixed K>0, or identify exactly why this comparison fails. I is
fixed, avoids zero since b_1>0, and is eventually contained in each
[-Ad,Ad]. These are parameter checks, not the sought lower bound.
No interval estimate or new actual-family asymptotic is derived here.

If successful, the test rejects this polynomial-cutoff prerequisite
without lower-bounding H_d or refuting RH. If it fails, retain the
unpaid integrated logarithmic tail; do not restart random-matrix
browsing without a changed essential hypothesis. No justified creative
signed-payment target is ready: this prerequisite is a standard-method
specialization, and no independent signed cancellation input is known.

Queries actually run included Girko/Hermitization/log-uniform-integrability,
deterministic shifted companions/polynomial small singular values,
Tao-Vu replacement principle, regularized log determinant, and
Cauchy-Binet Gram/minor expansions. The relevant primary statements
above were opened. Search snippets, unrelated regularization algorithms,
and inaccessible Meyer PDF follow-ups are not theorem evidence. The
Meyer alternative is nonessential because ready Higham coverage suffices.
Full matching Mathlib coverage was not checked; no absence is claimed.
