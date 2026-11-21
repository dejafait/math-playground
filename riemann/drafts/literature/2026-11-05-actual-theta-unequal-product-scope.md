# Actual theta unequal-argument products — completed source comparison

TARGET: Assess the unequal-argument Macdonald product formula for a modularly paired representation of the actual-theta first Laguerre form, retaining off-diagonal scale terms; park it unless the representation supplies a signed kernel test independent of RH.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step590 retrieved the unequal-argument identity and its primary Whittaker specialization; searched Macdonald/product/theta/Laguerre and convolution terminology, and reused November1 mechanism3 and step589's fixed-family failures. No inspected source supplies the nominated actual-theta representation or independent signed-kernel test; search limits below, no novelty inference.
SOURCE_EVIDENCE: NIST DLMF 10.32.9 and 10.32.17--18, including phase conditions; Sousa--Guerra--Yakubovich arXiv:1802.06657v2, Theorem3.1/(17), pp4--8, restricted-case Fubini and endpoint passage (24)--(26), continuation bounds (27)--(29), and Remark3.5(b,c), p9. Actual input L019/L020 read completely; L814 normalization/failure context and ready Gasper scope reused. Citations and access qualifications below.
COMPARISON: The known unequal-argument formula concerns same-order Bessel products. Its positive integration weight and the Whittaker positivity-preserving convolution do not identify the actual-theta transform with an admissible scale law or sign its first Laguerre form. Different-order/equal-argument identities are separate. The actual modular pairing, subtractions and scale-law hypotheses remain unpaid.
GAP: No exact actual-law representation with retained off-diagonal scales, controlled modular boundary/subtraction terms and an independently testable signed coupling was found. No first-sign or all-degree implication was established.
REASON: Park this nomination under its stated discriminator: the newly inspected product theorem does not supply the required representation/sign test. This is an informative source-scope limit, not an impossibility theorem, a source reproof or progress beyond the checked sources.
SCOPE: Completed literature-only comparison, not approval for a product-formula calculation or a claim of actual-theta positivity. Preserve all earlier reference/equal-scale stops; no lemma, mathematical script, numerical census or real-zero premise is added.
LITERATURE_REASON: Essential primary product-formula hypotheses and the actual-theta representation are missing for this changed mechanism; fixed-scale sources cannot cover them.

## Completed comparison — step590, 5 November 2026

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target was a source-backed, modularly paired unequal-scale representation
of F'(x)^2-F(x)F''(x), with F=Xi in L020's frequency convention.
Its plausible use was to expose a signed coupling for a later bounded
test; neither this first form nor a positive reference kernel supplies
the independent all-degree bridge. The continuation test required the
exact actual-law representation and an explicit sign condition testable
without assuming the desired Fourier sign. The inspected sources fail
that test, so this proposal is parked rather than approved for research.

### Exact known identity and domains

Use a,b for positive scale arguments and write K_nu for the modified
Bessel function, to distinguish it from L019's theta kernel K.
[NIST DLMF 10.32.18](https://dlmf.nist.gov/10.32#E18) states

    K_nu(a) K_nu(b) = (1/2) integral_0^infinity
      exp(-t/2-(a^2+b^2)/(2t)) K_nu(ab/t) dt/t.

The displayed complex-argument restrictions are |ph a|<pi,
|ph b|<pi and |ph(a+b)|<pi/4; positive real a,b satisfy them.
The order nu is complex. Do not confuse this with
[10.32.17](https://dlmf.nist.gov/10.32#E17), whose two arguments are
equal and whose orders may differ, under |ph a|<pi/2.
[10.32.9](https://dlmf.nist.gov/10.32#E9) gives the cosh integral
for Re a>0. No extension to an actual-theta scale measure follows
from these identities alone. DLMF Section10.32(iii) cites Watson1944,
pp439--441, and Erdelyi et al.1953b, pp97--98; those book pages were
not read and are not claimed as an independent proof audit.

A retrieved primary proof source is R. Sousa, M. Guerra and S. Yakubovich,
*On the product formula and convolution associated with the index
Whittaker transform*, J. Math. Anal. Appl.475(1) (2019),939--965,
[DOI10.1016/j.jmaa.2019.03.009](https://doi.org/10.1016/j.jmaa.2019.03.009).
Numbering here binds to [arXiv:1802.06657v2](https://arxiv.org/pdf/1802.06657v2),
submitted21 March2019, manuscript dated22 March2019. Theorem3.1/(17),
printed p4, permits x,y>0 and alpha,nu in C. Its explicit Bessel
specialization is **Remark3.5(b), printed p9**:

    K_nu(a) K_nu(b) = (1/2) integral_0^infinity K_nu(v)
      exp(-ab/(2v)-av/(2b)-bv/(2a)) dv/v.

This formula is quoted from the source, not derived here. The source
identifies the specialization through W_(0,nu)(2x) in (6) and D_0 in
(16); no additional theta specialization is justified. Read the theorem
statement and the relevant restricted-case proof passage (24)--(26),
printed p7: absolute convergence precedes Fubini, a Laplace-transform
injectivity step precedes identification, and the incomplete-gamma
integration by parts is performed for alpha<0, nu=i*tau, tau real.
Read the parameter-extension bounds (27)--(29) and closing continuation
argument, pp8--9; these supply the stated general parameter domain.
This is extraction of the theorem and essential convergence/endpoint
cases, not an independent audit of every preceding integral identity.

Remark3.5(c), p9, asserts q_a(x,y,v)>0 for a>=0 and x,y,v>0 and
positivity preservation of the induced convolution. The parameter a
in that remark is not our scale a above; Definition4.1 uses the weighted
space Lp((0,infinity);m_a(x)dx), m_a(x)=x^(-2a-1)exp(-x),
1<=p<=infinity. This positivity preserves signs of input functions in
that representation. It is not a theorem asserting positivity of every
Fourier transform or its Laguerre forms. No Banach-algebra or inversion
theorem from the unread later sections is used.

### Actual-law comparison and decision

L019's actual summands contain exp(-pi*n^2*exp(2u)), with their two
different exponential prefactors; L020's transform is the half-line
cosine integral of their full sum. L020 also records the nonzero
boundary derivative A'(0)=-1/4 in its integration-by-parts assembly.
The inspected Bessel product theorem supplies neither a representation
of these individual half-line transforms as K_nu(a), nor a modular
pairing of the summed expression with all boundary/subtraction terms.
Replacing exp(2u) by a cosh expression would change this exact input.
An integral or distribution over Bessel scales is a further hypothesis,
including its convergence and any parameter differentiation, not an
application already licensed by L019's superexponential tail estimate.
The product theorem is same-order; products needed after frequency
shifts/differentiation would also need their exact order bookkeeping.

Reuse November1's `2026-11-01-signed-theta-cancellation-discovery.md`,
mechanism3, for Gasper's equal-scale square comparison and its unequal-
scale limitation; no repeat square-identity derivation was performed.
L814 remains failure context only. Neither its normalized comparison
nor L815/L816's finite data is a premise for this review. The new
source evidence resolves what the unequal-argument formula actually
says, but leaves the actual-law and independent sign requirements
unmet. No pointwise sign of its Bessel factor, no domination of
off-diagonal scales, and no modular cancellation is imported.
No exact signed-kernel representation was derived on this literature turn.

**WHY THIS NOMINATION STOPS.** The available positive product weight
requires Bessel inputs; the asserted transfer to the unchanged actual
theta law has not been supplied. Even an admissible scale representation
would still need the specified signed-coupling estimate. Continuing with
just the known product identity would repeat the old unpaid transfer.
Reopen only with a concrete actual-law representation retaining every
scale pair and one independently quantified kernel test. This records
a source-scope failure, not proof that such a representation is impossible.

### Search/access limits and continuation

Queries included `Macdonald product formula K nu x K nu y unequal
arguments integral`, `Gasper Riemann xi function Bessel product formula
Laguerre inequality`, `"Macdonald" "product" "Riemann" theta kernel`,
`"Macdonald formula" "proof" convolution K`, and the exact
Sousa--Guerra--Yakubovich title. Generic Macdonald-polynomial/theta
results and unsupported RH claims were not mathematical inputs.
An Opuscula PDF failed on both hostnames; a later Yakubovich PDF
timed out. Yakubovich--Saigo1994's opening definitions were retrieved,
but its Theorems3.9/3.10 and complete proof passage could not be loaded;
their search snippets are not inputs. The accessible2019 primary paper
resolves the product theorem scope without depending on those leads.
An attempted local source download failed DNS; no source certificate
or mathematical program was produced. Full matching Mathlib coverage
is unchecked, not asserted absent. No new theorem is imported into
the proof assembly, so no canonical lemma, DAG or PROOF edit is needed.

No justified creative sign target emerges from this source. For an
independently testable continuation, nominate a separate scope review
of the still-pending C792b audit using its existing Lamprecht coverage;
do not repeat completed L803/L804/L809/L737 audits or L813's known
finite-cell import. C792b's source applications/closure quantifiers can
be independently checked without an actual-theta Bessel law. This
nomination is not a new obstruction or an approval of that audit;
its exact uncovered scope is recorded separately. All original stops,
unfinished work and numerical/backend qualifications remain intact.

## Original nomination retained (historical)

Main gap: actual-Xi all-degree mixed positivity. The intermediate source
target concerns F'(x)^2-F(x)F''(x), F=Xi in L020's convention. No sign
is asserted, and this first form alone is not claimed sufficient for RH.
A controlled mixed-scale representation could identify a signed coupling
for later work on higher forms.

Read the primary product theorem and relevant proof cases, then check
whether the exact theta transform fits without replacing
exp(-pi*n^2*exp(2u)) by a cosh model. Modularity must justify the paired
terms, including boundary and subtraction contributions.

Continue only with an exact actual-law representation and one explicit
kernel property, with quantifiers and a threshold, testable without the
desired Fourier sign. A model-only formula, dropped cross terms or an
unspecified signed remainder ends this mechanism. This is a new proposed
coupling, not permission to repeat November1's equal-scale squares.
No representation or discriminator is derived here.

Essential local inputs next turn: L019/L020, read as needed; L814 is
failure context only. L815/L816 and finite certificates are not inputs.
Unresolved: representation, modular pairing, boundary/convergence,
signed coupling, all real x and all degrees. No cross-notebook theorem
is proposed. Full matching Mathlib coverage is unchecked. Separate
source review is required before dependent mathematics.
