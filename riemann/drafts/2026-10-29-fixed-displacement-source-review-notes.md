# Fixed-displacement source review — completed evidence

Literature-only recovery step. Main gap: unbounded-height actual-Xi
initial signs and global mixed positivity. The reviewed intermediate
target is the original L471 pair sum restricted to d_j>=1/16, at the
o(T(log T)^3) threshold. A saving would remove only that sector.

Local inputs read: L471 definitions, conclusions and Sections 3–4;
L018's exact zero correspondence; complete L467 shell proof and its
critical audit; the October 27 L471 moment/application assessments.
Preserved stops: displacement-free separate-pair summation, L475's
scale-adapted global-norm envelope, and duplicate C464c audit replay.

## Primary density input

Shashi Chourasiya and Aleksander Simonič, *An explicit form of
Ingham's zero density estimate*,
[arXiv:2507.15184v1, 21 July 2025](https://arxiv.org/html/2507.15184v1),
Introduction p. 1 and Corollary 1/(3), Table 1 p. 2: N(sigma,U)
counts beta>=sigma and 0<gamma<=U **with multiplicity**. The displayed
common bound is

    N(sigma,U) <= 8.604 U^[3(1-sigma)/(2-sigma)] log^3 U
                 + 9.461 log^2 U + 167.8 log U,
    0.500<=sigma<=0.625, U>=3*10^12.

Read the proof pp. 4–5, the Section 4 Littlewood-lemma inequality
(32), and concluding proof p. 14 removing boundary nonvanishing by
perturbation. Equality at a cutoff is included. The finite verified
height used in Corollary 1 is a cited computational theorem, not full
RH. Its constants/computations and full manuscript are not independently
audited. The proof's opening “Theorem 2” reference conflicts with its
following “conditions of Theorem 1”; use the explicit Corollary 1
statement, not that cross-reference as a fourth-moment implication.

## Reused coverage and unused leads

Bui–Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1), Theorem 3,
defining asymptotic and Section 7, already directly inspected in
`drafts/literature/2026-10-27-l471-majorant-critical-audit-coverage.md`
and `drafts/literature/2026-10-27-hardy-jet-moment-feasibility-coverage.md`.
Reuse their coverage of fixed ordinary orders (0,0,0,0):
integral_T^(2T)|Z(t)|^4 dt=O(T(log T)^4). L471 Section 4 records
the same application. This is a continuous dyadic moment, with no
zero-conditioned, discrete or short-interval assertion. Its shifted
Proposition 3 has an omitted proof, but no shifted moment is needed
for the nominated test. No reason to reread unchanged moment sources.

Reuse L467's closed [v,v+1] bound 18 log(v+2), including multiplicity
and both endpoints. Its complete proof and audit were read, along with
`drafts/literature/2026-10-25-l467-critical-audit-coverage.md` and the
count assessment it names. The source is Bellotti–Wong,
[arXiv:2412.15470v2](https://arxiv.org/pdf/2412.15470v2), Theorem 1.1
p. 1, Section 3 argument principle p. 9 and Section 5 pp. 23–24;
those primary passages have ready coverage, not a fresh full-manuscript
audit. No independent local-count theorem needs to be invented.

The near-line Simonič theorem already inspected in
`drafts/literature/2026-10-28-zero-selected-disk-energy-coverage.md`,
pp. 1–2 of arXiv:1910.08274v2, is a reusable weaker alternative. Its
beta>sigma convention requires a threshold margin for equality and its
dyadic count requires padding. The former assessment's microscopic
selection-energy stop remains in force; it did not test this fixed
cutoff. Do not mistake that stop for a ban on fixed-sigma applications.

Directly inspected Guth–Maynard, *New large value estimates for
Dirichlet polynomials*,
[arXiv:2405.20552v1](https://arxiv.org/html/2405.20552v1), Theorem 1.2
and (1.2)–(1.4). Their comparison retains Ingham below 7/10. This
stronger-result lead is unnecessary for the present cutoff; its full
zero-density proof is not independently audited or imported here.
The original Ingham publisher record (Q. J. Math. os-11 (1940),
201–202, DOI 10.1093/qmath/os-11.1.201) was located; its full proof
was not retrieved. The accessible primary corollary above supplies the
needed input, so dependent work is not source-blocked on that original.

## Hypothesis matching and bounded test

The fixed source range includes sigma=1/2+1/16. Use L018's existing
zero correspondence to assign one right-side zeta zero to each selected
Xi pair, retaining its full m_j. The attempt must check injectivity
when different pairs share an ordinate. Plan to use a cumulative count
at 3T to cover all P_T centers, rather than presume a dyadic density
formula for clipped windows. Likewise L467 controls local overlap
without spacing or simplicity. These are hypothesis checks to carry
out in the specialization, not an asserted sector estimate.

Candidate for a later attempt: aggregate the original nonnegative
window kernel first, and test its L2 norm using both a density count
and local overlap. Do not sum the old separate-pair Cauchy–Schwarz
bounds. No aggregate norm, resulting exponent or sector saving has
been derived in this literature step. Continue only with an aggregate
norm that yields the required little-o, or an explicit quantified
failure of this comparison. Abandon it if it needs an unproved
selected-amplitude bound. No full N(T) saving, individual-height sign,
higher positivity or Mathlib theorem is established.

## Bounded search and duplicate comparison

Queries included `Riemann zeta zero density Ingham N sigma T
3(1-sigma)/(2-sigma) log 5 theorem pdf`; `zero density estimates zeta
weighted integral neighborhoods zeros fourth moment critical line fixed
sigma`; `An explicit form of Ingham multiplicity zeros 2025`;
`Guth Maynard zero density 1/2 7/10 Ingham theorem 2024`;
`Ingham On the estimation 201 pdf 1940`; and the exact combinations
`xi Laguerre zero density`, `zeta negative part fourth moment`,
`Riemann Laguerre displacement`. An overly literal L471/fixed-displacement
query gave no useful theorem lead. Search snippets are not proof.

The last queries rediscovered already assessed rStation papers 41 and
50. Reuse the October 27 majorant comparison of their theorem scope;
their growing-order and pointwise-window statements are not an import
of this restricted amplitude-weighted sum. Unrelated results were not
used. No inspected theorem directly states the requested B-sector
bound; this is not an exhaustive search or a novelty certification.

Local searches were restricted to L471/L467, the named recent moment,
selected-energy and complementary-mass assessments, and their failure
records. L471's separate-pair loss and L475's exponential-cost stop
do not supply the proposed aggregate norm. C464c's prior audit is
complete, so repeating it is independently unproductive. The recovery
comparison and selection are preserved in
`ATTEMPTS/2026-10-29-c464c-duplicate-audit-recovery.md`.
