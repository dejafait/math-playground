# Actual-theta connected-partition cancellation: completed source comparison

TARGET: Assess whether cumulant-product partition identities support an actual-theta sign-producing cancellation for reciprocal Hankel forms in arbitrary degree, using H_2 as a fixed symbolic discriminator rather than repeating its known finite sign certificate.
CHECKED: 2026-11-06
DECISION: IMPORT
SEARCH_EVIDENCE: Step19 searched Leonov-Shiryaev product-cumulant/indecomposable partitions, theta/xi connected cumulants, reciprocal Hankel cumulants and stronger cumulant-Hankel results; checked local exact-name and stopped-transfer records. Primary passages and limits below; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Leonov-Shiryaev, Theory Probab.Appl.4(1959),319-329, DOI10.1137/1104031; Russian primary https://m.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=4894&what=fullt Sections1-3, (II.c)/(IV.d), printed pp343-351. Burchardt https://doi.org/10.1007/s10801-019-00898-3 Sections1.1-1.6, Theorems1.6/1.9. Lehner https://arxiv.org/pdf/math/0110031v2 Definition4.5/(4.5), Section6/Proposition6.1, pp5-6/8-10. Zhu https://arxiv.org/html/2611.01172v1 Theorems1.6-1.8, Section2.6 and Section3 Claim5; comparison scope only.
COMPARISON: The primary identities permit dependent and repeated arguments and prescribe exact partition sums, not nonnegative cumulants or an actual-theta cancellation. Hankel path cancellation retains crossing/permutation signs. Universal lifting requires shifted-cumulant moment positivity, not merely positive ordinary moments. No inspected source provides the missing actual-law sign input.
GAP: A correctly normalized reciprocal-power interface, independent arithmetic-theta signed cancellation and arbitrary-degree extension remain unproved. H_2 is an already-certified finite discriminator, not a new sign target; no partition representation or determinant expansion is derived here.
REASON: Import the known identities and their scope only; park direct connectedness-to-Hankel positivity. New source evidence fails the nominated continuation test without refuting any actual form or excluding every theta-dependent cancellation. No technical continuation is ready.
SCOPE: Completed literature-only applicability comparison. IMPORT authorizes only these known-source scope conclusions; no actual-Xi positivity, new lemma, mathematical script, symbolic H_2 expansion or unlisted mathematical continuation.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target lacked exact primary product-cumulant hypotheses and a theta-specific sign comparison; stronger directly relevant results were inspected once. Existing theta/Gram/Favard/Lorentzian and GHS source stops were reused.

## Original nomination, preserved

The main gap is L030-L032/C032a, positivity of the actual reciprocal
Hankel forms for arbitrary degree. Essential local inputs are L019/L021's
actual K and finite positive moments, L024/L025's normalized logarithmic
coefficients and L030's real algebraic-square convention. Use L033's
first determinant formula and the September20 theta-logarithm audit as
scope warnings. The latter already records H_1/H_2 finite certificates;
rechecking or extending those certificates is not this target.

The intermediate object sought is an exact partition-based integral
representation whose cancellation has a separately testable dependence
on the full arithmetic theta law. Its plausible use is an actual-law
sign mechanism capable of extending beyond a fixed Hankel cutoff.
This nomination supplies no representation and no independent sign.
First retrieve exact primary product-cumulant hypotheses and determine
whether they even address this proposed composition of operations.
Do not substitute cumulants of products for products of cumulants, or
assume connectedness implies positivity. Determine normalization and
any necessary number of copies from the sources before computation.

The fixed future discriminator is the representation for H_2 and whether
it exposes a theta-specific signed cancellation absent from the ordinary
Gram/positive-moment arguments. It is not a request for a new numerical
bound on det H_2. Continue toward a later mathematical target only if a
concrete pairing/cancellation and its independent sign test can be named.
If the sources furnish only the already available signed moment
polynomial or depend on real zeros/GHS cone membership, park this
mechanism without a determinant expansion or a new countermodel.

The September Gram/logarithm and finite-cutoff stops, L796 common-Favard
stop and current Lorentzian mismatch must be compared, not re-proved.
The parameter-wide four-copy GHS source blocker is preserved: no further
access campaign or assumed unread cone coefficients are permitted by
this nomination. Exact arithmetic theta constraints, not generic
positivity of a measure, must carry any proposed reopening.

No protected creative attempt is ready. A subsequent genuinely new
signed-cancellation mechanism would require proof_attempt/creative
routing with a precise obstruction and bounded test; a standard
partition-identity specialization remains reproduction. Full-result
Mathlib coverage is unchecked. No cross-notebook input is proposed.

## Completed comparison — 6 November 2026, step19

The main gap remains L030–L032/C032a: the actual reciprocal-node
algebraic-square forms must be nonnegative in every degree. The
intermediate question was whether connected-partition cancellation
supplies a sign from the exact arithmetic theta law. A successful
representation could support an all-degree mechanism while leaving
its extension and sign estimates as separate obligations. The test
was an explicit additional pairing/cancellation with an independently
justifiable sign. The inspected sources do not supply it. This is a
source-scope NEGATIVE, not a negative actual form, a new theorem or RH
progress beyond the sources checked.

### Exact primary identity and hypotheses

V. P. Leonov and A. N. Shiryaev, *On a Method of Calculation of
Semi-Invariants*, [Theory of Probability and its Applications 4(3)
(1959), 319–329](https://doi.org/10.1137/1104031). The accessible
[Russian primary](https://m.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=4894&what=fullt)
is printed pp342–355. Inspected Sections1–3, especially (II.c),
Section2's finite absolute-moment requirement, repeated-variable
convention, indecomposability definition and (IV.d), pp343–348.
Section3, pp349–351, cancels decomposable contributions by replacing
row groups with independent groups having the same marginals, then
exhausting the finitely many row splits. It proves an identity, not
a positivity statement; the original variables need not be independent.
For a fixed finite product-cumulant calculation it requires the
relevant absolute moments. No analytic logarithm outside a germ, theta
hypothesis, positive integrand or fixed replica count is supplied.
The English full text was not inspected. Russian PDF OCR has damaged
formula glyphs; the usable exact product formula is independently
stated in the following published primary paper, so no damaged scalar
coefficient is imported.

Adam Burchardt, [*Algebras with two multiplications and their
cumulants*, J. Algebraic Combinatorics 52 (2020), 157–186,
version of record 18 September 2019](https://doi.org/10.1007/s10801-019-00898-3),
Sections1.1–1.6, Definition1.8/Theorem1.9, gives

    kappa(Y_1,...,Y_r) = sum_(pi strongly mixing) product_(B in pi) kappa(X_j : j in B),
    Y_i = product_(j in A_i) X_j.

Strong mixing means that no nontrivial union of argument groups
separates every partition block. Variables with all finite moments
are allowed; independence and positivity are not hypotheses.
Equation(1) uses coefficient extraction in distinct labeled variables;
for repeated scalar arguments the convention is
log E exp(tX)=sum kappa_n(X)t^n/n!. Labels need not be independent
copies. Products of cumulants cannot simply be replaced by the
cumulant of a product. The two-commutative-unital-algebra extension
in Theorem1.6 has weights (-1)^(vertices minus leaves), not positive
weights. These stated identities are imported without reproof or a
new specialization.

### Stronger Hankel and lifting comparisons

Franz Lehner, [*Cumulants, Lattice Paths, and Orthogonal Polynomials*,
arXiv:math/0110031v2, 3 July 2002](https://arxiv.org/pdf/math/0110031v2),
Definition4.5 and (4.5), printed pp5–6, uses exponential classical
cumulants, with falling-step weights kappa_(k+1)/k! and rising-step
weights y+1. Section6, Proposition6.1/(6.2), pp8–10, assumes finitely
many nonzero-weight paths between each chosen endpoint pair and gives
a determinant as a permutation-signed sum over vertex-disjoint paths.
Edge crossings can remain. The following Lukasiewicz-path example
explicitly retains different signs and cancelling terms. Thus this
stronger determinant representation still needs additional weight
and crossing control; nonintersection alone is not a sign theorem.
It concerns moment Hankel matrices, not automatically L030's powers.
No general graph cancellation theorem or theta application is reproved.

Bao-Xuan Zhu, [*Coefficientwise Hankel-total positivity from a
universal cumulant lifting*, arXiv:2611.01172v1, 31 October 2026](https://arxiv.org/html/2611.01172v1),
Theorems1.6–1.8, uses formal exponential moment series. Stieltjes
lifting requires once-shifted cumulants to be a Stieltjes sequence;
Hamburger lifting requires twice-shifted cumulants to be a Hamburger
sequence. Section2.6/(2.74)–(2.83) and Section3 Claim5/(3.1)–(3.3)
recover these requirements from positivity at every nonnegative
intensity, including the limit to zero. Positivity at one intensity
is not that hypothesis. Proposition4.2 states a logarithm criterion
for an ordinary Stieltjes moment series; its full proof and referenced
Bernstein theorems were not inspected. It is only an unread-proof lead,
not an application to factorial-divided theta coefficients. The new
preprint supplies no inspected actual-theta application. Its universal
lifting conclusion is not imported into the argument.

### Actual-law interface and duplicate test

L019 and L021 give the exact K, positive finite moments, superexponential
tails and the cosine coefficients. L024/L025 give the locally normalized
logarithm and reciprocal powers. Their (2n)! normalization and the
logarithm coefficient factor 1/k must be matched to the sources'
exponential cumulants before any application. These operations are
not a cumulant-of-products operation merely because both use partitions.
The finite absolute-moment prerequisite is available; the required
signed reciprocal-power conclusion is not. This comparison derives
no conversion formula, replica count or actual-law integral identity.

In notebook notation H_d=(S_(i+j+2))_(i,j=0)^d. L033 concerns H_1,
the 2-by-2 determinant S_2 S_4-S_3^2. The nominated H_2 discriminator
is the 3-by-3 form, not that determinant. The September20 audit already
records finite H_1/H_2 certificates; neither is rechecked or extended.
Only an independently signed arithmetic cancellation would distinguish
a new representation from L040's already-stopped signed recurrence.

The September20 theta-logarithm audit retains L044's generic Gram
counterexample and L057's fixed-cutoff obstruction. They do not rule
out the full arithmetic theta law. L796's common-Favard construction
is separately stopped by its actual nonzero forbidden coefficient;
Lehner's path representation does not repair that coefficient or
supply a new positive measure. The ready Lorentzian comparison has
the wrong direct sign and a different coefficient transform. The
parameter-wide GHS assessment remains SOURCE_BLOCKED; no access
campaign, assumed cone coefficients or claimed cone implication is
used here. These are contrasts, not premises or a second DAG.

New queries were `Leonov Shiryaev 1959 cumulants products random
variables indecomposable partitions formula`, `theta Riemann xi
cumulants Hankel determinants connected partitions positivity`,
`Leonov Shiryaev 1959 On a method of calculation of semi-invariants
pdf Speed 1983 cumulants partition lattices`, `"Riemann xi"
"cumulants" "connected"`, `"theta" "Hankel" "Leonov"`, and
`"reciprocal" "Hankel" "cumulants" positivity`. Local exact-name
searches found no earlier completed Leonov–Shiryaev/Burchardt/Lehner
assessment beyond this nomination. Search snippets, Speed's abstract,
other xi preprints and free-probability leads were not treated as
verified theorem inputs. No failed search establishes originality.

### Decision and continuation contract

Park this direct connected-partition import: the surviving terms have
no inspected theta-specific independent sign. Do not expand H_2,
produce another generic countermodel, or infer all degrees from its
existing certificate. Reopening needs a specified signed pairing or
arithmetic estimate, correct factorial normalization and a bounded
test that can fail independently of RH. The result is not a theorem
excluding every future connected-partition approach.

No source-ready creative target emerges: the missing object is that
independent signed input, not an unavailable partition identity.
Bounded discovery must now consider a materially different mechanism,
compare at most three candidates with the retained stops and nominate
one independently falsifiable test. Its separate assessment is
REVIEW_REQUIRED, not mathematical approval. Existing completed endpoint,
finite-PF and Favard audits are not fresh continuations. No cross-notebook
input, lemma, mathematical script, DAG or assembly change is made.
Full-result Mathlib coverage is unchecked; no absence claim is made.
Mathematical exploration usage is zero in this literature step; no
cumulative exploration or supervisor recovery counter is reset.
