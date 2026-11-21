# Paired finite-convolution subdiagonal comparison: nomination1228/review1229

TARGET: Establish or refute an absolute bound |beta_(i,b)(x)-beta_(i,0)(x)|<=C*x*sum_l b_l^2 for C030r's subdiagonal beta_(i,b)=sqrt(D_(i+1,b)*D_(i-1,b))/D_(i,b), uniformly for 1<=i<d<=floor(n/2) in its full conjugate-rate family and closed phase window.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1229 completed the bounded exact/stronger-result and obstruction search documented below; reused1202/1213/1217/1225 and checked C030q/C030r plus stops1117/1181/1193/1200/1107. No matching uniform theorem or admissible counterexample was located in the inspected coverage; this does not establish novelty.
SOURCE_EVIDENCE: Inspected Sra author-v3 C.5/(C.9), C.9/(C.18)-(C.23), pp22-23,27-28, and C.17 statement/finite-window continuity case, pp38-39; Pozza--Pranic--Strakos ETNA50 Definitions1.1-1.2/Theorem1.3/(1.3), pp2-3; Gautschi Numer.Math.48(1986), Section1/(1.1)-(1.6), pp369-370; Celsus et al. arXiv1504.07297v4 (1.7)-(1.12), Proposition2.1 with proof and Proposition2.2, pp3,9-10. Exact applicability and unread leads below.
COMPARISON: The finite basis and determinant ratios are already covered. The real-rate variance bound and positive-measure sensitivity framework do not settle the conjugate-rate absolute perturbation target; the inspected complex Toda statements are identities for a different functional, without the required uniform estimate. No reproof of these known identities is authorized as a claimed advance.
GAP: The absolute constant independent of n,d,m and all real-rate contrasts remains unproved and unrefuted. C030q's first-response control and C030r's nonzero determinants do not state the needed subdiagonal estimate; shift evolution and actual-Xi signed-complement payment remain separate.
REASON: Essential source comparison is complete for one bounded mathematical attempt on the unchanged target, after separate approval of this newly ready assessment. This literature-only step derives no bound, specialization or counterexample; no essential source blocker remains.
SCOPE: C030r's finite m>=1,n>=2m,a_l,r>0,b_l real; A=sum_l|b_l|,M=sum_l b_l^2,x>0,x*A<=1/4; n>=4 and 2<=d<=floor(n/2) for a nonempty subdiagonal. Include arbitrary real-part contrasts, n=2m, zero phases, repeated rates and the closed boundary. beta_(i,0) uses the same n,m,a_l,r,x with every b_l set to zero. C must be independent of all these parameters.
LITERATURE_REASON: TARGET changes the audited basis/diagonal question to a quantitative subdiagonal estimate outside1225/1226; exact recurrence/variance and uniformity coverage was essential before dependent research. Unchanged orbital coverage is reused.

## Why this target follows the audit

The main gap is L030-L032/C032a actual-Xi positivity in every degree.
The audited finite interface C030r identifies the actual moving-basis
matrix, and C030q controls its diagonal phase response. The remaining
subdiagonal is a concrete place to test whether that scalar phase cost
can support quantitative control of the finite basis evolution. This is
a prospective use, not a derived perturbation or shift-norm theorem.
Even success would leave the real-reference evolution hypotheses,
degree/time and actual-Xi supply, signed-complement payment, all-degree
positivity, theta signing and graph realization unpaid.

The proposed test asks for an absolute constant at the same x*M scale.
Continue only if a source theorem or later approved argument controls
that scale uniformly. A rigorous admissible family with M>0 and
|beta_(i,b)-beta_(i,0)|/(x*M) unbounded would abandon this target while
preserving C030q and C030r. Finite samples would be diagnostic only.
The nomination required comparing finite exponential convolutions,
quasi-definite recurrence coefficients and adjacent orbital/Hankel
ratios before calculation. Review1229 completes that source screen below.

The reusable source is S. Sra, *On some positivity properties of the
Riemann Xi function*, [author-v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
C.6/(C.10), pp23-25, and C.9/(C.21)-(C.23), pp27-28, as recorded in
[assessment1225](2026-11-17-paired-finite-convolution-basis-review-1225.md).
That record describes inspected source passages; it does not establish
the proposed comparison. General quasi-definite existence remains a
known input and need not be rediscovered.

Stops1117/1181/1193/1200/1107 retain their automatic-transfer scopes.
This target makes no such transfer and does not reopen those stopped
mechanisms without new inputs. The scoped local comparison performed
for the completed audit did not itself assess the new estimate; review1229
adds the bounded target-specific comparison below.
Mathlib matching for this new estimate is unchecked. No cross-notebook
input, numerical certificate or mathematical derivation is supplied.

## Completed source review1229 (17 November 2026)

This is one literature-only step. No new estimate, specialization,
counterexample, lemma or mathematical script was derived. EXPLORE
records a bounded search with no adequate match, not a truth or novelty
judgment. The assessment is newly ready and requires separate approval
before the proposed mathematical attempt.

### Duplicate and recorded-failure scope

Read assessment1225 and C030r's hypotheses/conclusion/source-use ranges;
read C030q's hypotheses, conclusions and physical-response proof through
its series setup. Reused source notes1202/1213/1217 for unchanged orbital
inputs and their prior searches. Scoped searches in the paired basis
assessments/working notes and C030q/C030r found the nomination and the
explicit off-diagonal exclusions, with no completed matching bound in
that coverage. This is not a notebook-wide originality claim.

Read the short stop records1117/1181/1193/1200/1107. They concern,
respectively, finite-block automatic transfer, a quantitative class
bridge, degree/time signed transfer, theta propagation and graph-to-Q
transfer. None supplies this bound or refutes its finite family. Their
unpaid hypotheses remain unchanged; a successful finite estimate alone
would not reopen those stopped implications.

### Primary statements and applicability

**Finite reference.** S. Sra, *On some positivity properties of the
Riemann Xi function*, author-v3, 2 November 2026,
[primary PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf).
Reused1225's determinant assessment; inspected C.5/(C.9), pp22-23,
and C.9/(C.18)-(C.23), pp27-28, including the variance and matrix-bound
steps. For positive real rates, the source gives

    beta_(i,0)^2=-(log D_(i,0))''<=i*(n-i)/x^2.

The inequality uses the nonnegative variance in (C.9). C.9 additionally
assumes bounded positive real rates and its displayed degree condition.
Its estimate is an individual real-reference bound, not a difference
estimate for the paired complex family. Analytic continuation of an
identity does not continue that variance inequality. C030r already
establishes the changed-rate basis; no reproof of that construction is
needed. This review does not assert complex variance positivity or a
shift norm.

Also inspected C.17, pp38-39: for each finite window and fixed order,
its family has positive local minors for sufficiently small nonreal
phase, despite global PF failure. The continuity case fixes its real
rates and window; it gives no uniform beta perturbation bound. Its
distinct real background is not identified with TARGET's family, and
its separate C.14 global-obstruction input was not reaudited here.

**Quasi-definite recurrence.** S. Pozza, M. S. Pranic and Z. Strakos,
*The Lanczos algorithm and complex Gauss quadrature*, ETNA50 (2018),
1-19, DOI10.1553/etna_vol50s1,
[publisher PDF](https://epub.oeaw.ac.at/0xc1aa5572%200x0039ff98.pdf).
Refreshed Definitions1.1-1.2, Theorem1.3 and (1.3), pp2-3. Nonzero
leading Hankel determinants give finite bilinear orthogonal polynomials
and nonzero recurrence coefficients. The statement gives no uniform
perturbation constant. The cited Chihara book proof was not newly read.
These algebraic inputs are already used in C030r; existence alone does
not cover TARGET.

**Sensitivity terminology and hypotheses.** W. Gautschi, *On the
Sensitivity of Orthogonal Polynomials to Perturbations in the Moments*,
Numerische Mathematik48 (1986), 369-382,
[author-hosted PDF](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/098.pdf).
Read Section1, (1.1)-(1.6), pp369-370, and the opening factorization
(2.1)-(2.5), p371. The setup maps ordinary or modified moments of a
positive measure on the real line to recurrence coefficients. Its
dimension is finite when support is finite. This is different from
C030r's alternating signed derivative-moment functional. The source
discusses conditioning depending on the measure and chosen moments;
it does not state the proposed dimension- and contrast-uniform bound.
No condition-number formula or instability counterexample is imported
here, and no new coefficient-perturbation result is inferred.

**Complex exponential deformations.** A. F. Celsus, A. Deano,
D. Huybrechs and A. Iserles, *The kissing polynomials and their Hankel
determinants*, [arXiv1504.07297v4](https://arxiv.org/pdf/1504.07297v4),
6 December 2021 (PDF title date7 December), later Trans. Math. Appl.6
(2022), tnab005, DOI10.1093/imatrm/tnab005. Read (1.7)-(1.12), p3,
Proposition2.1 and its proof, p9, and Proposition2.2, p10. The weight is
exp(i*omega*z) on [-1,1]; recurrence identities require the relevant
polynomials and nonzero norms to exist. Proposition2.1 expresses the
monic recurrence coefficient as a Hankel ratio; Proposition2.2 states
complex Toda equations. The latter's appendix proof was not inspected
or imported. The monic coefficient is not the positive square-root
coefficient beta in TARGET. These identities do not state an absolute
uniform perturbation bound for heterogeneous exponential convolutions.
No identification of these two families is claimed; no kissing-point
phenomenon is asserted inside C030r's nonvanishing window.

### Queries, source access and unread leads

Queries issued for this changed target included:

- orthogonal polynomials Hankel determinant recurrence coefficients perturbation complex weights stability
- "exponential convolutions" "recurrence" Sra
- "Riemann Xi" "C.22" Sra
- site:suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf "variance"
- site:suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf "C.22"
- recurrence coefficients perturbation orthogonal polynomials positive measure Gautschi condition numbers
- "conjugate" "exponential" "convolution" "Hankel" perturbation
- "Harish-Chandra" "Hankel" "recurrence" coefficients variance
- "quasi-definite" "perturbation" "recurrence coefficients" bounds
- Celsus Deano Huybrechs Iserles kissing polynomials recurrence coefficients 2022
- "recurrence coefficients" "complex weights" "perturbation" bound
- "Sra" "subdiagonal" "conjugate"
- "orbital integral" "rank" "ratio" "perturbation"
- "HCIZ" "Turán" inequality
- "Hankel" "conjugate" "rates" "bound" convolution

The direct Sra PDF initially failed; opening the indexed primary URL
then exposed the relevant passages. The OUP kissing-polynomial page
redirect failed; the primary arXiv-v4 PDF worked. Gautschi's extracted
later formulas were garbled; no such formula is used. Screenshot
requests did not supply inspectable image content and are not evidence.
No essential source remains inaccessible.

Targeted within-source searches for `conjugate`, `imaginary` and
`perturbation` located the additional C.17 comparison just recorded;
no uninspected passage is being used as a theorem input.

Searches also surfaced indefinite-metric asymptotics, antidiagonal
Hankel perturbations, complex Laguerre/Painleve asymptotics and the
large-degree kissing-polynomial phase portrait. Their full theorem
statements were not read and are not inputs or claimed exclusions.
They do not replace the inspected statements above. No exact-family
uniform estimate was located; a failed search is not proof of absence.
Mathlib coverage of the full bound is unchecked, with no absence claim.
No cross-notebook mathematical input was read.

### Bounded continuation after separate approval

Keep TARGET and SCOPE unchanged. A later attempt may use C030r's exact
determinant interface, C030q's orbital floor/response, and the standard
Hankel/Jacobi identities with their signs and differentiation hypotheses
justified for the actual finite family. Do not treat a first-derivative
bound as a second-derivative bound or a relative determinant comparison
as the requested absolute coefficient comparison without proof. Do not
assume a lower bound on beta_(i,0), a positive complex law, or constants
depending on real-rate spread. No new intermediate formula is derived
or certified in this review.

Continue on an explicit absolute constant on the full closed window,
or a paid intermediate estimate with a precise remaining obstruction.
Abandon the universal bound on a rigorous admissible M>0 sequence with
unbounded |beta_(i,b)-beta_(i,0)|/(x*M). A diagnostic sample is not that
certificate. Save a partial attempt and reassess after the shared
bounded-exploration limits; changing the estimate's name does not renew
them. No justified new central actual-Xi mechanism is prepared by this
review, so the planned work remains development, not creative work.
