# Gamma-compensated reciprocal theta moments — completed source comparison

TARGET: Assess whether the gamma-compensated reciprocal moments s_j=4^j(1/2)_j m_0/m_j for 0<=j<=5 admit a positive measure on [0,infinity), comparing exact truncated Stieltjes criteria and the two 3-by-3 Hankel tests, without assuming a sign-transfer theorem.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step637 inspected primary odd truncated-Stieltjes criteria and Bernstein-product/gamma-ratio theorems; narrowly compared L019/L021/L795/L796/L822, the step502/508/615 assessments and the product-compensation stop. Exact queries and read limits are recorded below; no actual Hankel matrix was evaluated and no novelty is inferred.
SOURCE_EVIDENCE: Curto–Fialkow, Houston J.Math.17(1991),603–635, Theorem5.1 p625, Section3 proof cases pp613–617 and Theorem4.1 proof pp622–623; Berg arXiv:math/0412340v1, Theorems1.1/1.2 pp3–4, proof pp9–11, Theorems5.1/5.2 pp14–15; KPS AIF74(2024), Theorem4.4 p396 and Section5.2.6 p416; paper23 v1 Section2 (3),(5),(9), conditional Theorem1. Links and qualifications below.
COMPARISON: The exact finite criterion is known, while its actual-theta data are untested. The compensated sequence also overlaps the Bernstein-product moments of the existing conditional Mellin construction; gamma-ratio results alone do not verify its theta denominator. This supports a finite consistency diagnostic, not automatic lower oscillation.
GAP: Determine the actual finite moment feasibility with all errors retained; infinite representation, actual Bernstein membership, a sufficient lower-oscillation interface, degree uniformity and mixed/shifted transfer remain unresolved.
REASON: Informative overlap negative: the nominated law is already conditionally covered by the existing actual Mellin/Bernstein construction, so it is not an independent new sign mechanism. Retain a bounded consistency diagnostic under known criteria; no actual moment feasibility or sign is established here.
LITERATURE_REASON: The saved REVIEW_REQUIRED nomination lacked the primary equality-moment criterion and the Bernstein-product overlap; existing endpoint/inverse coverage did not assess these changed multipliers.
SCOPE: Completed literature-only comparison for exactly s_0,...,s_5 with L795's moments. The original nomination below is retained as historical task specification; step637 supersedes its unreviewed status. The new finite-test assessment requires separate next-turn approval before research.

## Original nomination — retained, status superseded by step637

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate claim is existence of a positive measure on [0,infinity)
with the six displayed moments. The fixed gamma compensation comes from
the Laguerre coefficient normalization recorded in L795. Its plausible
use is a candidate positive dual averaging representation for a later,
separately justified lower-oscillation mechanism. Existence of such a
measure alone supplies no sign-transfer theorem; that independent gap
must not be replaced by an analogy with orthogonal polynomials.

The bounded future diagnostic would examine the complete matrices
(s_(i+j))_(i,j=0)^2 and (s_(i+j+1))_(i,j=0)^2 using actual theta moments.
The source review must first distinguish necessary positivity from any
sufficient truncated moment theorem, including singular cases, range
conditions, support at zero and all normalization assumptions. No matrix
has been evaluated in step636. A negative certified direction would stop
this representation premise. Passing necessary tests would retain only
that finite premise, and would not justify extrapolation in degree.

Before preparing research, search exact gamma-compensated reciprocal
theta moments, stronger Stieltjes/multiplicative-factorization results,
and relevant obstructions. Retrieve primary hypotheses and the essential
singular/nondegenerate proof cases. Narrowly compare the existing actual
Mellin/Levy assessments if they concern this same law; a shared word such
as Mellin is not a mathematical input or authorization to scan proofs.
If the source comparison shows the test duplicates a settled result,
import it precisely. If it has no independently identifiable downstream
use, abandon it rather than accumulating another finite sign check.

Three candidate mechanisms were compared for nomination only:

1. Extending Q_3 endpoint/compact positivity leaves the existing
   lower-oscillation direction gap unchanged; repeating endpoint approval
   is exhausted and is not the next action.
2. Universal inverse variation is refuted by the actual-law quadratic
   witness in L822. Restricting its inputs without a new premise would
   merely rename the stopped claim; it is not selected.
3. The specified gamma-compensated moment law is a different finite
   positive-representation premise, with two concrete necessary matrices.
   It is selected for review, with no presumption that it is true or useful.

The common-Favard stop L796 and the automatic adjoint/AT/Lee-Yang import
stops remain intact. No common three-term recurrence, signed forcing
bound or automatic representation theorem is asserted here.

Essential inputs for the review are L019/L021/L795's actual positive
moments and Laguerre normalization; L796/L822 are contrasts, not premises
establishing the proposed measure. If a later approved calculation uses
L778/L791 numerical moment data, its exact data and analytic/software
contracts must be read and retained then. No cross-notebook input is
proposed. Candidate moment existence, a positive dual representation
identity, lower oscillation, degree uniformity and sufficient mixed-sign
transfer all remain unresolved.

This assessment does not approve new mathematics. No creative proof
attempt is routed yet: the missing primary criterion and downstream
representation comparison are essential coverage blockers. A later
creative nomination must name a precise sign-transfer obstruction and
a bounded test; this source nomination is not relabeled creative.
Full matching Mathlib coverage is unchecked.

## Completed comparison — step637, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
target is the six-moment representation premise, with a possible later
positive dual averaging use. The source comparison supplies a second,
concrete use: testing a necessary finite premise of the existing conditional
Mellin/Bernstein construction. Neither use supplies the missing lower sign
count. No determinant, witness, representing measure or new implication
about actual Xi has been proved in this literature turn.

### Exact equality-moment criterion and proof cases

R. E. Curto and L. A. Fialkow, *Recursiveness, positivity, and truncated
moment problems*, Houston Journal of Mathematics **17**(4) (1991),603–635,
[Theorem5.1, p625](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf).
For real data gamma_0,...,gamma_(2k+1), gamma_0>0, existence of a positive
Borel measure on [0,infinity) with **all** these moments equal to the data
is equivalent to

    A(k)=(gamma_(i+j))_(i,j=0)^k >=0,
    B(k)=(gamma_(i+j+1))_(i,j=0)^k >=0,
    v(k+1,k)=(gamma_(k+1),...,gamma_(2k+1))^T in Ran A(k).

Here >=0 means positive semidefinite. For the nominated data k=2,
A=H_0, B=H_1, v=(s_3,s_4,s_5)^T, s_0=1. An atom at zero is allowed.
This is the equality problem, not the variant bounding the last moment.
Invertible H_0 makes the range condition automatic; singular H_0 does not.

Read Proposition3.3's nonsingular construction pp613–615, Corollary3.4's
singular recurrence reduction pp615–616, Theorem3.1's necessity pp616–617,
and Theorem4.1's support restriction pp622–623. Theorem5.1 invokes that
argument rather than supplying a separate detailed proof. No reproof is
needed. No strict-positive support or nonsingularity assumption is imported.

### Gamma results and the precise Bernstein overlap

C. Berg, *On powers of Stieltjes moment sequences, II*,
[arXiv:math/0412340v1](https://arxiv.org/pdf/math/0412340v1),
arXiv header 17 December2004; accessed PDF internally dated 27 August2018.
Theorems1.1/1.2, printed pp3–4, assume a nonzero Bernstein function f,
alpha>=0, beta>0, f(alpha)>0. They give moments
f(alpha)...f(alpha+(n-1)beta), including a probability law on (0,infinity).
Read the proof pp9–11, including its alpha=0 qualification; no such
boundary specialization is needed here. Theorems5.1/5.2 pp14–15 cover
(a)_n and (a)_n/(b)_n for a>0 and 0<a<b respectively. They do not cover an
arbitrary positive theta moment denominator. Remark1.7's Hausdorff
transformation requires its Hausdorff input, also not established here.

Reuse [step508's actual construction comparison](2026-11-05-actual-xi-levy-certificate-comparison.md).
bramble_trace, *A continuum certificate for the decreasing Lévy factor
associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October2026, Section2 (3),(5),(9), was checked narrowly against the
present normalization. Its P=K/2 and M(n)=m_n/2, so the constant cancels.
Its (9) specifies the product (2n)!M(0)/M(n); the present s_n is that
product divided by n!. The source's Psi(s)=s phi(s) and KPS's product
normalization in Section5.2.6 identify this as the product sequence of phi
used by Berg with alpha=beta=1. This is comparison of existing coefficient
conventions, not a new construction or a verification of phi's hypotheses.
Thus the proposed moments have known conditional coverage if the claimed
actual phi is a nonzero Bernstein function. That essential hypothesis is
still conditional on paper23's analytic and evaluator enclosures. No
supplement was retrieved or reapproved here. Finite moment feasibility
would be strictly less than a verification of those global hypotheses.

T. Konstantopoulos, P. Patie and R. Sarkar,
*A new class of solutions to the van Dantzig problem, the Lee–Yang
property, and the Riemann hypothesis*, AIF **74**(1) (2024),377–421,
[Theorem4.4 p396; Section5.2.6 p416](https://www.numdam.org/item/10.5802/aif.3600.pdf),
retains the separated Bernstein-Pick hypothesis for its real-zero result
and explicitly gives nonreal-zero examples in the broader class. Reuse
the earlier inspected theorem/proof comparison. Neither the finite
moment criterion nor ordinary Bernstein membership supplies the missing
real-zero or mixed-sign conclusion.

### Duplicates, relevance, and the bounded continuation

L822 uses bare m_0/m_j; its exact quadratic witness does not decide these
gamma-compensated multipliers. L796 excludes a common Favard measure for
the P_d family, a different claim from representing six specified numbers.
L795's actual normalization and support remain unchanged. Step502's
variation-diminishing theorem supplies an upper count; it does not provide
the desired lower count. The step391 actual-theta product-compensation
stop concerns a signed cofactor integral, not this moment problem.
The step508 overlap is substantial: an unconditional all-degree law must
not be advertised as a wholly unrelated new mechanism. The independent
finite test remains useful because a certified failure would reject a
necessary representation premise without assuming any Xi zero signs.

The next test is limited to the two complete 3-by-3 matrices. A certified
negative quadratic direction or negative principal minor stops the moment
premise. A pass requires the full cited criterion, including the range
condition if singular; numerical near-zero intervals are inconclusive.
Even a complete pass establishes only six-moment feasibility. Do not grow
the degree, infer total positivity, or revive universal inverse variation.
No independently justified creative sign-transfer mechanism emerges here;
its blocker remains the missing lower-oscillation interface, not a ban on
theta work. This calculation is routine specialization of known criteria.

L791's saved gamma list ends at j=4. It is not a sixth-moment certificate.
A future test may use L778's full polynomial evaluator and its complex
uniform error (5) on |w|<=1600, together with the named Cauchy coefficient
estimate and L791's normalization. It must extract/enclose index5 as well,
retain the coefficient-error enlargement and all software/provenance
contracts, and inspect complete load-bearing intervals. The ready
[finite-test assessment](2026-11-05-theta-gamma-six-moment-test.md) scopes
that work; supervisor approval remains separate. No numerical data were
loaded or calculated here. Full matching Mathlib coverage is unchecked.

### Search and access record

Queries included `Curto Fialkow truncated Stieltjes moment problem odd
2k+1 range A(k) B(k) theorem 5.1`; `"Riemann" "theta" "reciprocal moments"
gamma Stieltjes`; `"reciprocal" "Jensen polynomials" "moments"`;
`"gamma" "quotient" "Stieltjes moment sequence" Berg`;
`"gamma-compensated" moments theta`; `"Stieltjes" "A(k)" "B(k)"
"v(k + 1"`; and `"Riemann xi" "Stieltjes" "Berg" moments`.
No inspected theorem directly decides the actual six values; failed exact
searches are not novelty evidence. The Berg–Durán paper was an initial
lead; Berg's primary Theorem1.1/Remark1.7 supplies the comparison used.
Other generalized-gamma, reciprocal-Xi/Thorin and search-only leads were
not imported. The latter reciprocal-Xi law is not the law nominated here.

Primary PDFs were accessible through the web reader. Curto–Fialkow OCR
in (iv) is degraded; its same-page Theorem5.2 and the publisher's indexed
Theorem5.1 text corroborate the range condition and semidefinite symbols.
Screenshot requests yielded no inspectable image in this tool interface;
none is counted as visual verification. Optional shell download failed DNS,
the author's presentation URL returned404, and the Berg homepage timed
out. These are not essential source blockers: the primary papers and
their needed theorem/proof ranges were read. No API key or installation
was used. No source is imported solely from a search snippet.
