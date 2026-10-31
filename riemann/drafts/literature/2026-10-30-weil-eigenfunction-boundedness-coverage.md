# Fixed-interval Weil eigenfunction boundedness — primary coverage

TARGET: Assess source coverage for fixed-interval L-infinity bounds on eigenfunctions of A_I=G_I-cI-K_mu with finite real even signed measure mu, sufficient to apply L513 using L514.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact eigenfunction/measure-perturbation and geometric-stable smoothing searches locate paper 67's existing bound; Dyson-Phillips searches locate Engel–Nagel's primary theorem. Narrow local Weil searches find the prior boundedness exclusion and no duplicate application audit; a small-time ultracontractivity warning was compared below.
SOURCE_EVIDENCE: Read bramble_trace paper 67 v1 Sections 3.1–3.2 (3.4)–(3.10) and Section 7 (7.1)–(7.3); Engel–Nagel (2000) III.1.3 p.158, III.1.9–1.10 pp.162–163 including convergence topology; Grzywny–Ryznar arXiv:1107.0745v1 Section 2 killed-semigroup formulas following (2.4); Chen–Weth arXiv:1710.03416v6 Theorems 3.4/1.11; Tsuchida arXiv:2606.17501v1 Introduction's definition of ultracontractivity.
COMPARISON: The requested fixed-operator regularity is already asserted for the source's signed atomic Weil measure; standard perturbation and killed-semigroup inputs cover a later application to arbitrary finite real even signed mu. It is known mathematics. The manuscript's compressed domination needs a local specialization, not a new smoothing mechanism.
GAP: Audit arbitrary-mu Dyson domination and convergence from L2 into L-infinity at time one, then bounded G_I u and the exact L513/L514 applicability. No such specialization or premise removal is proved in this literature turn.
REASON: Primary coverage changes the route from uncovered regularity to a bounded reproduction audit. Fixed-operator regularity may supply the trace premise but supplies no eigenvalue-relative arithmetic flux saving.
LITERATURE_REASON: The hypotheses change from arbitrary reference-operator domain data with boundedness assumed to eigenfunctions of a full bounded signed convolution perturbation with boundedness to be proved; that coverage was explicitly excluded from the prior assessment.
SCOPE: Fixed ell>0, c real, I=(0,ell), G_I the smooth-core killed part operator for Psi(xi)=(1/2)log(1+xi^2), finite real even signed Borel mu including atoms, K_mu f=(mu*E_I f)|_I, A_I=G_I-cI-K_mu on Dom(G_I). Complex eigenvectors and all multiplicities are included; positivity of A_I or u is not assumed. Full-Weil identification, collars and arithmetic uniformity are excluded.
COVERED_TARGET: Audit the fixed-interval signed-measure eigenfunction bound in paper 67 v1 (3.7)–(3.8), including atomic Dyson domination, bounded G_I u, and applicability of L513–L514.

## Preserved proposed scope and test

Fix ell>0, I=(0,ell), c real, and a finite real even signed Borel
measure mu on R. Set K_mu f=(mu*E_I f)|_I and
A_I=G_I-cI-K_mu on Dom(G_I). This definition retains both signs
and any atoms of mu. The prospective statement is that each
eigenfunction A_I u=lambda u lies in L-infinity(I), with a bound
||u||_infinity<=C(ell,c,||mu||_TV,lambda)||u||_2, and that G_I u
is bounded as required in L513. The operator here is fixed; no
uniformity in a family of measures, supports or approaching spectral
zeros is included. Identifying the actual Weil realization with this
model remains a separately cited hypothesis from L512.

Essential local inputs for a later application are L513 and L514;
L512 supplies the intended activation use. The old collar and
near-null arithmetic flux assumptions remain unresolved. This
assessment proves no eigenfunction bound or new lemma. It is not a
creative central-gap mechanism; the split itself supplies no arithmetic
cancellation, so none is ready to nominate on its evidence alone.
Mathlib coverage for the proposed statement is unchecked.

## Inspected theorem coverage

[bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
(3.4)–(3.8), retains both a signed density and prime-power atoms.
Section 3.2 gives ||exp(-A)||_(2->infinity)<=exp(c+M)/sqrt(2)
and ||u||_infinity<=exp(lambda+c+M)||u||_2/sqrt(2), with M a
total-variation bound. Its argument replaces the measure by its
variation and dominates killed semigroups by whole-line convolutions;
the time-one kernel has squared L2 norm 1/2. Section 7 (7.1) also
bounds h=G_I u; (7.3) explicitly distinguishes an absolute trace
bound from an eigenvalue-relative one. These are existing manuscript
claims, not independently verified conclusions of this turn.

[Engel–Nagel, *One-Parameter Semigroups for Linear Evolution
Equations*, GTM 194, Springer, 2000](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf),
III.1.3 p.158, assumes a C0-semigroup generator H on a Banach space
and B bounded on that space; H+B has domain Dom(H) and generates
a C0-semigroup. III.1.9–1.10 pp.162–163 gives the Dyson–Phillips
recursion S_0(t)=T(t), S_(j+1)(t)=integral_0^t T(t-s)B S_j(s)ds.
The integrals are strong-operator integrals, while the series converges
in operator norm, uniformly on compact time intervals. Positivity and
absolute continuity of a perturbing measure are not hypotheses. This
theorem on X=L2(I) supplies the expansion, not an L2-to-L-infinity
bound by itself. Passage to that stronger norm must be justified
separately in the future application.

[Grzywny–Ryznar, *Potential theory of one-dimensional geometric stable
processes*, arXiv:1107.0745v1, 4 July 2011](https://arxiv.org/html/1107.0745v1),
Section 2, gives the transition density by gamma subordination and,
following (2.4), defines killing by
P_t^D f(x)=E^x[1_(t<tau_D) f(X_t)]. The displayed transition-kernel
formula there gives 0<=p_t^D(x,y)<=p_t(x-y). The parameter-two
Levy density is exp(-|t|)/|t|; the notebook's exponent and density
are half of these. The needed reference is therefore the process
at half speed, killed on exit. This is not subordination of killed
Brownian motion. The time normalization is a required application
check; L513 already uses this same convention.

[Chen–Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
arXiv:1710.03416v6](https://arxiv.org/html/1710.03416v6),
Theorem 3.4 supplies the unperturbed variational spectrum, not the
needed arbitrary-mu bound. Theorem 1.11 assumes u and its forcing
are already bounded, so applying boundary regularity first would be
circular. L513 retains the later optimal boundary theorem and its
weak-form comparison; their assessed scope is reused, not broadened.

## Obstruction screen and the remaining specialization

[Tsuchida, *Critical spectral behavior and large deviations for
geometric alpha-stable processes*, arXiv:2606.17501v1, 16 June
2026](https://arxiv.org/html/2606.17501v1), Introduction, explicitly
defines the missing ultracontractivity as L2-to-L-infinity smoothing
for every t>0. This warning concerns small times and does not refute
the time-one calculation in the inspected source. Its perturbations
are measure potentials, a different operation from convolution;
no theorem about those potentials is imported here. Only the
Introduction's relevant scope was inspected, not its later proofs.

The later audit is limited to checking the already published method:
finite-measure convolution on L2 and L-infinity (including the
well-defined a.e. action of atomic translations); total-variation
domination of each Dyson term; extension/restriction contractions;
whole-line commutation only after domination; and the summed
time-one bound with M=||mu||_TV. A bounded L2 perturbation alone
does not imply smoothing, nor do the compressed operators commute.
Use the standard Minkowski integral inequality for finite-measure
convolution and Plancherel/Young at the specified time. No new
kernel estimate is nominated.

If that audit succeeds, check the eigen-equation for bounded
G_I u and then apply L513 with L514 supplying both reflected domain
splits. It must work for every eigenvector, not only a positive or
simple ground state. If any domination/convergence step fails,
retain the original boundedness premise and record that exact failure.
Do not infer a vanishing trace as lambda approaches zero, a uniform
collar remainder, or positivity of the actual Weil operator. Its
identification with this model remains the independent L512 premise.

Queries used: “geometric stable process logarithmic laplacian
eigenfunctions bounded signed measure perturbation semigroup L2
Linfinity”; “logarithmic Laplacian eigenfunctions bounded”; “geometric
stable semigroup bounded signed convolution perturbation eigenfunction
L infinity”; “Engel Nagel one parameter semigroups pdf Dyson Phillips
III.1.10”; “symmetric Levy killed semigroup dominated whole space
semigroup”; “finite measure convolution Lp norm total variation Young
inequality Folland theorem 8.7”. The last query supplied no inspected
book theorem for measures; no precise Folland attribution is claimed.
Search snippets, secondary mirrors and unrelated spectral results
were not used as theorem evidence. No novelty follows from the search.

This completed assessment nominates a ready reproduction audit;
the newly written continuation requires the supervisor's separate
approval before research. No lemma, mathematical script or argument
overview was changed in this source-only step.
