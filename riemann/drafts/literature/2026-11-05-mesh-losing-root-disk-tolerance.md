# Mesh-losing root-disk tolerance — source comparison, step490

TARGET: Assess whether disjoint-root-disk Rouche bounds give an explicit tolerance epsilon(d,Q)>0 for relative coefficient perturbations of every degree-d positive-rooted polynomial with consecutive root ratios at least Q>1, allowing mesh loss.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded coefficientwise root-perturbation, pseudozero and Rouche searches; inspected Graillat--Langlois Theorem3/Corollary5, Toh--Trefethen Proposition2.1 and Alexanderian Theorems2.2/3.2/3.5, with relevant proofs and norm conventions. Exact queries and local overlap below.
SOURCE_EVIDENCE: Graillat--Langlois, P32 preprint (6 January 2004), pp.6--9, gives the finite all-coefficient weighted-maximum-norm certificate; Alexanderian (28 January 2022), pp.1--5, supplies disk counting and real-simple-root retention. Original Mosier access failed; the inspected full proof suffices without that unread source.
COMPARISON: Known finite perturbation inputs cover the required coefficient norm and root-count mechanism; the inspected cases do not state a uniform epsilon(d,Q). C792a/C792b concern stronger preservation requirements, not this mesh-losing certificate. No novelty claim.
GAP: A separate mathematical specialization must choose relative root disks and lower-bound the boundary certificate uniformly in all root scales using only d,Q; include varying leading coefficient, positivity, simplicity and degree exhaustion. No such bound or actual residual comparison is proved here.
REASON: Essential finite, rather than infinitesimal, source coverage is now available; only the quantitative mesh specialization remains. Continue with one bounded conventional calculation after separate approval of its new assessment.
LITERATURE_REASON: The output requirement changes from retaining the same mesh to retaining simple positive roots; essential quantitative root-perturbation cases are unread. Prior ready coverage does not cover a new tolerance derivation.
SCOPE: Completed literature-only comparison for exactly TARGET. No lemma/script writes or new tolerance derivation. The separate proposed calculation assessment is newly written and requires the supervisor's next-turn approval.

## Inspected sources and exact applicability

Stef Graillat and Philippe Langlois, *More on pseudozeros for univariate
polynomials*, [author preprint P32](https://perso.lip6.fr/Stef.Graillat/papers/P32.pdf),
dated 6 January 2004: Section3.1, Theorem3 and its full proof, pp.6--7;
Section3.5, Corollary5, p.9, equation(8). Polynomials have complex
coefficients and degree at most n; the leading coefficient can vary.
For fixed positive weights f_j the perturbation norm is
max_j |p_j-b_j|/f_j. Its pseudozero set is exactly

    {z: |p(z)| <= epsilon sum_(j=0)^n f_j |z|^j}.

The proof uses the dual norm in both directions. Taking f_j=|p_j|
is explicitly allowed. Here these weights are positive. Real
perturbations form a subset of the source's complex perturbations;
only its sufficient exclusion direction is needed. No inference of
real-perturbation necessity from complex pseudozeros is authorized.
This is a finite certificate, not a linearized root condition number.

Alen Alexanderian, *On continuous dependence of roots of polynomials
on coefficients*, [author note](https://aalexan3.math.ncsu.edu/articles/polyroots.pdf),
last revised 28 January 2022. Theorem2.2, pp.1--2, is Rouche's theorem:
analytic f,g on a simply connected domain containing a simple closed
contour, |g|<|f| on it, give equal interior zero counts with multiplicity.
Theorem3.2/proof, p.3, uses disjoint disks and a positive boundary
minimum; its perturbations are monic and absolute, so that statement
alone does not cover the present norm or leading coefficient.
Theorem3.5/proof, pp.4--5, uses real coefficients, a real simple root
and conjugation: one zero counted with multiplicity in a disk centered
on the real axis must be real and simple. The proof's reference to
the conjugate as a root of p is a typo: its displayed identity uses q.
For positivity the later application must also keep each disk away
from the nonpositive real axis; the source does not supply our uniform
relative radii. The full relevant proofs were inspected.

Kim-Chuan Toh and Lloyd N. Trefethen, *Pseudozeros of polynomials and
pseudospectra of companion matrices*, Numer. Math.68 (1994), 403--425,
[author PDF](https://people.maths.ox.ac.uk/trefethen/publication/PDF/1994_61.pdf),
Section2, Proposition2.1/proof, pp.405--406. This original paper uses
monic degree-n polynomials, lower-coefficient weighted Euclidean norm
and its dual evaluation norm. Proposition2.2 is an infinitesimal
condition number. Neither is silently substituted for the all-coefficient
maximum norm. Its reference to Mosier motivated checking that source.

Ronald G. Mosier, *Root neighborhoods of a polynomial*, Math.Comp.47
(1986), 265--273, DOI10.1090/S0025-5718-1986-0842134-4: original AMS PDF
attempts returned a timeout/403. An earlier guessed checksum URL failed
and was corrected. Bibliographic/review hits are not theorem evidence;
Mosier remains unread and is not a load-bearing import. P32 supplies
the inspected complete proof of the needed finite norm statement.

## Search, overlap and bounded decision

Executed queries included `polynomial coefficientwise relative
perturbation simple real roots Rouche root separation bounds`;
`polynomial root perturbation componentwise relative coefficients
Rouche disks explicit bounds`; `polynomial pseudozeros componentwise
relative perturbations Rump Rouche disks weighted coefficients theorem`;
`Beauzamy relative perturbation roots polynomials 1999 theorem coefficients`;
`More on pseudozeros for univariate polynomials`; and `Pseudozeros of
Polynomials and Pseudospectra Toh Trefethen pdf`. Follow-up searches
located the author PDF and Mosier reference. Beauzamy/Bombieri-norm,
Hurwitz stability and algebraic separation hits remain unread leads;
none is treated as a matching theorem. This was a bounded search, not
a claim that the desired mesh specialization is absent from literature.

Reused step484/488 histories, step488's quantitative-source limitation,
and the relevant C792a/C792b hypotheses and preservation conclusions.
A targeted November5 search for pseudozeros/componentwise perturbations
found the two mesh nominations, not an existing completed tolerance.
No q-classification proof was repeated. The old universal and same-mesh
stops remain intact; neither supplies nor refutes the missing bound.

The source-backed difference is now narrow and independently testable:
bound the finite boundary ratio on relative disks, with constants
depending only on d,Q. This is conventional specialization; no Rouche,
pseudozero or conjugation theorem needs reproving. No quantitative
mesh bound is derived or approved by this literature step. A positive
bound would still require a separate actual residual comparison.
Mathlib matching coverage remains unchecked; no absence is inferred.

The proposed [calculation scope](2026-11-05-mesh-losing-root-disk-specialization.md)
requires separate approval next turn. Missing independent growing-degree
model/separation and signed residual control still blocks a justified
new central creative target. No mathematical exploration budget is
spent or reset by this review. PROOF/DAG are unchanged.

## Original nomination (historical; preserved)

The main gap remains actual-Xi all-degree mixed positivity. The proposed
intermediate statement concerns a degree-d model p with positive simple
roots rho_1<...<rho_d satisfying rho_(i+1)/rho_i>=Q>1. Write
p(x)=sum p_j x^j and a real perturbation e(x)=sum e_j x^j. Assess a
condition |e_j|<=epsilon(d,Q)|p_j| for every j, including the leading
and constant coefficients, that ensures p+e still has d simple positive
roots. The required output need not retain Q. All p_j are nonzero for
such p, so this relative coefficient condition is well-defined.
An overall nonzero scalar and positive change of variable must not
alter the conclusion. No compact bound on all root magnitudes or upper
bound on their ratios is available for free.

Inspect primary theorem statements and the proof cases needed for a
Rouche certificate on disjoint disks around the positive model roots.
Look for exact terminology, stronger existing bounds, scale invariance,
the coefficientwise norm used, degree dependence and limitations; a
qualitative fixed-polynomial openness theorem alone does not meet the
uniform target. A result needing further quantitative hypotheses may be
useful only if those hypotheses are stated and independently testable.
Do not infer novelty from missing hits or derive a new disk estimate
during this review. No further q-multiplier classification browsing is
needed unless it supplies a specific new quantitative weaker-output lead.

Continue only if the source review yields a precise usable quantitative
statement or a bounded, separately approvable difference. If only
same-mesh symbol admissibility or qualitative continuity is available,
park that import with the exact missing bound; do not repeat finite
degree sweeps. Any eventual tolerance must later be compared with the
actual residual, not merely shown positive. No such comparison is
performed or presumed here.

Essential local inputs/context: L791/L792, C792a and new unaudited C792b;
inherited L778/L018/L021/L776, exact F_j=R_j through4, S=B R1,
t_m,t_a,delta>0, complete original widths and analytic/software
contracts. C792b is route evidence, not a premise of the proposed
abstract perturbation theorem. No numerical replay or cross-notebook
input is proposed. Growing-degree model existence, quantitative model
separation and actual signed/relative residual estimates remain open.
A tolerance alone would not prove actual all-degree signs or RH.

This proposed method is conventional perturbation analysis, not a
creative central mechanism. A justified creative central target is
still blocked by the lack of independent growing-degree model/residual
control. The next review should determine whether this concrete
certificate can make that gap independently testable; it must not label
the routine tolerance derivation creative to meet scheduling preferences.
Mathlib matching coverage is unchecked.
