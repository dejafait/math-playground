# Low-time degree-one contact admissibility — completed source comparison

TARGET: Assess known results on strict positivity of the actual heat-deformed degree-one logarithmic Hankel matrix for 0<lambda<11/200, to decide whether any nonvacuous d=1 contact pilot remains.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step179 reused the October30 transition and November6/9 GHS assessments; inspected L019/L058/L063/L488/L874/C874a and L033/L035-L038; searched exact heat/logarithmic-Hankel/cumulant-determinant and stronger real-zero bounds. No inspected theorem covers strict H1 throughout the requested interval. The new primary bound and the exact minor mismatch are recorded below; unsuccessful searches establish no novelty.
SOURCE_EVIDENCE: Platt-Trudgian, Bull. Lond. Math. Soc.53(2021)792-797, arXiv:2004.09765v1 Section3.4 Corollary2 and its preceding argument, https://arxiv.org/html/2004.09765v1 ; Polymath arXiv:1904.12438v2 (4 August2019), (1)-(4), transition paragraph and Theorem1.1, https://arxiv.org/html/1904.12438v2 ; Choi arXiv:2611.04359v1 (3 November2026), (5)-(10), Theorem4.1/proof and (19)-(20), Proposition5.1 and AppendixB, https://arxiv.org/html/2611.04359v1 . Exact inspection limits and qualifications follow.
COMPARISON: The primary bound Lambda<=1/5 is stronger than the pilot's retained 11/50 input; Choi explicitly records unconditional matrix structure for a>=0.05. The existing t=4lambda interface makes this relevant to the top of the requested interval. Choi's unconditional zero-time gap is S1*S3-S2^2, not det H1=S2*S4-S3^2. Neither scalar signs, raw moment positivity nor the inspected statements settle H1 on 0<lambda<1/20.
GAP: The exact remaining admissibility question is strict positivity of S2 and S2*S4-S3^2 for the actual L874 coefficients on 0<lambda<1/20. L038 covers only lambda=0 under its arithmetic contracts. No contact existence, uniform certificate, flux sign or new noncontact theorem is proved in this literature turn.
REASON: Correct the source scope and replace a residual search with a bounded direct finite-moment admissibility test. The known top-of-band input is reusable; a direct certificate can bypass the parked four-copy sources. A separate newly prepared assessment specifies that calculation and awaits next-turn approval.
LITERATURE_REASON: The new question concerns contact admissibility below the known real-zero cutoff, outside the fixed pilot's assessed band; essential theorem-level coverage of this low-order matrix sign is missing.
SCOPE: Completed literature-only comparison for the actual L019/L058/L874 family and H1=[[S2,S3],[S3,S4]], retaining both null rows and S2=0. No lemma, mathematical script, coefficient optimization or replacement residual was written. Known-source applicability is compared here; a new uniform determinant proof is deferred.

## Completed comparison — 9 November 2026, step179

The main gap remains L030-L032/C032a. The intermediate question is
whether degree one has any admissible contacts in the specified low-time
range. Strict positivity would retire that proposed contact mechanism
on the certified range; lack of a sign theorem would not establish a
contact. Higher degrees, initialization and equality/continuation remain
independent. This is local source progress, not progress beyond the
sources checked or an RH candidate.

### Stronger applicable real-zero input

D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
3×10^12*, Bull. London Math. Soc. **53** (2021), 792-797,
DOI [10.1112/blms.12460](https://doi.org/10.1112/blms.12460),
[arXiv:2004.09765v1, 21 April 2020](https://arxiv.org/html/2004.09765v1),
Section 3.4, Corollary 2: Lambda<=0.2 unconditionally. Read its full
preceding argument: Polymath Table 1's second row requires verified
height H>2.51*10^12, and Theorem 1 supplies 3,000,175,332,800.
The footnote identifies the table's X as 2H. The stronger proposed
<0.19 improvement is explicitly conditional on a height not supplied.
The computation and the underlying barrier certificates are accepted
by citation, not independently replayed. This is not a new bound.

The existing transition assessment already covers Newman's threshold,
as precisely restated after Polymath (4): all zeros real iff t>=Lambda.
L488 (11), read in its proof, gives F(lambda,z)=8H_(4lambda)(2z).
This normalization identity is not restricted by L488's separate tail
theorem's compact time range. Consequently 1/20 is the local parameter
corresponding to source time 1/5. C874a's existing all-real/product Gram
argument is the relevant downstream specialization; no reproof or
newly extended lemma is made here. Its independent audit remains pending.
The source bound does not give reality below its cutoff, and its failure
to do so says nothing about the existence of low-degree contacts.

### Nearby matrix result: exact hypotheses and minor

U. J. Choi, *RH-Conditional Positivity in a Theta-Kernel Langevin
Model*, [arXiv:2611.04359v1](https://arxiv.org/html/2611.04359v1),
3 November 2026, is an unreviewed preprint. Read (5)-(10), Theorem 4.1
and its real-zero/Gram proof, (19)-(20), Proposition 5.1 and Appendix B.
Its kernel is L019's divided by four; normalization cancels that factor,
and its tilt a is lambda. Theorem 4.1 explicitly includes unconditional
structure for a>=0.05 using Platt-Trudgian, correcting the earlier
comparison's incomplete scope description. Below that range the full
hierarchy assumes RH. Equation (20)'s strict minor and Proposition 5.1's
zero-time certificate concern S1*S3-S2^2, not S2*S4-S3^2. The latter
requires eighth moments. Appendix B's interval-box proof handles its
stated unweighted kernel moments and tails; its positive-quadratic-tilt
extension is not supplied. No reported certificate was replayed.

### Other leads and access limits

Exact searches included `Riemann Xi heat deformation logarithmic Hankel
cumulants positivity S2 S3 S4`, `deformed Riemann xi function generalized
Laguerre inequalities logarithmic derivatives Hankel determinants`,
`Riemann logarithmic Hankel heat positivity`, `Riemann cumulant determinant
theta`, the exact S2/S3/S4 combinations, and de Bruijn-Newman upper bounds.
These were bounded discovery queries, not an exhaustive theorem census.

Csordas-Varga, *Moment inequalities and the Riemann hypothesis*, Constr.
Approx. **4** (1988), 175-198, Theorem 2.4, remains an incompletely read
lead in this review: the [author-hosted scan](https://www.math.kent.edu/~varga/pub/paper_161.pdf)
returned no readable text, screenshots exposed no inspectable image, and
one shell retrieval failed DNS. Indexed primary passages and the abstract
describe tilted raw-moment Turan inequalities; they are not accepted as
a full theorem inspection or a bridge to the logarithmic determinant.
No new access campaign or source-dependent GHS work is nominated.

Wang-Yang's 2024 coefficient-Laguerre paper was located through its
[primary manuscript](https://cfc.nankai.edu.cn/_upload/article/files/81/18/f83d37e449ebaf1b2f4141fa59be/9323c2fc-4d6a-4610-a747-1bd985a7be41.pdf).
Only its title/abstract/introduction start was readable before theorem
retrieval timed out; it is an unread theorem lead, not an imported result.
Sra's v3 author page describes PF and generalized Laguerre results for
undeformed Xi. Its theorem proof was not loaded; no deformed H1 inference
is accepted. Search hits for later certified Lambda records were not
adopted without primary theorem/certificate inspection. The selected
direct moment test does not require any of these leads or the blocked
EMN/Newman1991 displays. Full/supporting Mathlib coverage is unchecked.

### Direct test that avoids those source blockers

L033 already supplies the finite moment polynomial for this determinant;
L038 certifies positivity only at lambda=0, subject to L037's arithmetic
contracts. Neither gives a uniform positive-time interval. L035's tail
is for the untilted moments; it must not simply be reused after inserting
exp(lambda*u^2). L036's Taylor enclosure is for any C8 integrand, and
L058 supplies the required compact smoothness and domination.

The [official Decimal documentation](https://docs.python.org/3/library/decimal.html),
Decimal.exp, next_minus/next_plus and rounding modes, was checked for
L037's directed-arithmetic contract. Correctly rounded exp uses
ROUND_HALF_EVEN and must still be widened; nearest rounding alone is
not an interval enclosure. New parameter panels, tilted tails and the
complete determinant enclosures remain research obligations. No saved
certificate was rerun or new tail inequality derived in this review.

Nominate exactly one bounded uniform test on [0,1/20], including zero
as the existing calibration endpoint. Its new assessment is
`2026-11-09-low-time-h1-uniform-moment-test.md`; separate approval is
required before invocation. Continue only on strict lower enclosures
for both S2 and det H1 on every closed parameter panel. If any panel
is inconclusive, report its exact interval and the outstanding tail or
arithmetic bound; an enclosure containing zero is not a contact.
Do not return to residual coefficients or silently widen the mesh budget.

## Original nomination (archival; completed comparison above controls)

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The downstream purpose of this source review is to decide
whether degree one is a meaningful contact-sign target near the
undeformed endpoint at all. An empty domain supplies no boundary
mechanism. A failure to find a theorem does not establish that a
contact exists, and higher degrees remain independent.

Reuse the inspected global-transition source assessments and the
unchanged density-rule coverage. Start with narrow local searches for
actual heat-deformed logarithmic H1 positivity and its exact moment or
cumulant formulation, including any previously certified low-degree
noncontact interval. Then retrieve primary theorem hypotheses and
relevant proof cases for any exact or stronger match. L056's comparison
kernel is not actual theta, and the local positive-atomic argument
requires a separately justified real-zero hypothesis.

Essential local inputs for comparison are L019/L058/L063/L488/L874
and C874a, whose new empty-domain specialization remains independently
unaudited. C489a's conditional collision conclusion is not an input.
No cross-notebook theorem is used. The source theorem cutoff is a
nomination guide, not a claim of a new lower-time positivity range.

Continue only with a precisely applicable known strict-positivity
result or an explicit, separately reviewable test of the remaining
contact-admissibility gap. If known results rule out the whole
degree-one target, retire it and nominate a materially different
target; do not invent contacts or expand the degree during this
review. Preserve the old pilot's empty-domain evidence and all prior
scoped failures. Full/supporting Mathlib coverage remains unchecked.
