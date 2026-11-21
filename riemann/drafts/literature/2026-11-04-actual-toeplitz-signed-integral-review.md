# Actual coefficient Toeplitz minors — signed integral source gate

TARGET: Assess signed multiple-integral representations of the actual coefficient Toeplitz minors with all factorial weights retained, and determine whether ordered-variable symmetrization offers one bounded theta-kernel sign test beyond L765.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step389 inspected Katkova math/0505174v1 Section2 Lemmas1–2/(10)–(13) and their complete proof, the fixed-order core/tail argument in Sections3–4, and Forrester 1806.10411v1 (1.7)/Sections2.2–2.3; reused step385's coefficient-PF comparison and L765's recorded stop. Exact queries and bounded local duplicate checks appear below; no novelty inference.
SOURCE_EVIDENCE: Katkova v1, pp.7–8, Lemmas1–2 supplies the exact signed angular coefficient-minor identity; pp.10–20 supplies its fixed-order application and the inverse-even-factorial SPF statement on p.10. Forrester v1 (1.7)/Sections2.2–2.3 supplies determinant integration, not a sign theorem. O'Sullivan v2 (1.2) and Michałowski v1 (1)–(3) identify G(z)=xi(1/2+sqrt(z)/2)/8 and the full factorial normalization.
COMPARISON: A factorial-exact signed angular representation is already known. Its nonnegative sine-Vandermonde weight does not remove the remaining real phase. The inspected fixed-order theorem and cubic wedge do not supply growing-order or actual-K pointwise signs; ordinary moment Gram positivity is a different statement. One symbolic test of the proposed real-variable pointwise mechanism is nominated below, without evaluating it.
GAP: The real-moment row-integral and permutation symmetrization must be justified with their factorials and convergence, then their actual-K integrand must pass the stated pointwise test. No sign, new identity, uniform cancellation estimate, or minor theorem is established in this literature turn.
REASON: The representation itself is covered; the independent unresolved issue is whether ordered real variables give a pointwise sign. Test that sufficient mechanism before seeking growing-order cancellation, without reopening L765's norm criterion or assuming PF/LP.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes from the stopped q-Pascal norm criterion to signed factorial-weighted integrals; prior Andreief coverage concerned another functional and did not assess this coefficient sequence.
SCOPE: Actual a_n=M_(2n)/(8*4^n*(2n)!), r>=2, k>=r-1, K of L019. Representation comparison and the single covered symbolic obstruction test only; no generic positive-measure replacement, matrix scan, altered ray of the q-Pascal criterion, or integrated sign claim.
COVERED_TARGET: Test whether the factorial-exact, permutation-symmetrized real-moment integrand for D_(r,r-1) is pointwise nonnegative on (1,...,1,t), for even integers r>=2 and t>=1, retaining the actual theta kernel K and checking any negative witness on an open ordered neighborhood.

## Proposed object and missing coverage

Use the actual kernel K of L019, moments M_(2n) of L021, and completion
of L018. The candidate observable is the existing consecutive determinant

    D_(r,k)=det[a_(k+j-i)]_(i,j=0)^(r-1),
    a_n=M_(2n)/(8*4^n*(2n)!),  r>=2, k>=r-1.

These are definitions, not a new integral formula. L765 is the contrast
and stopping evidence, not a sign input. The review must retain the
index-dependent factorials, real integration domain and actual K. It
must distinguish a determinant of moments, a Gram determinant, and a
coefficient Toeplitz minor; signs for one do not identify the others.

The precise question is whether a known integration/symmetrization
identity provides a signed integrand whose positive and negative parts
can be compared using an established property of this K. Retrieve the
primary hypotheses and essential proof cases first; reuse the earlier
Andreief coverage only for the identity it actually covers. Search for
stronger coefficient total-positivity results and counterexamples before
nominating a calculation. The inspected local search excerpts do not
establish absence of duplicates or novelty.

Continuation test: nominate at most one concrete finite/symbolic signed
kernel test, with exact domain and decisive inequality, if the source
comparison identifies a missing but independently testable estimate.
A low-order minor already known positive is not such a test. If the
representation requires the desired PF/LP property or merely renames
the determinant sign, record that obstruction and reject this mechanism.
No mathematical derivation is authorized during the source review.

Plausible downstream use is an actual-kernel sign estimate for coefficient
minors that does not require a small unsigned perturbation. Even a useful
intermediate estimate would leave uniform growing-order control, other
indices (including k<r-1), all-degree positivity and RH unresolved.
The main gap must not be assumed in an integration or total-positivity
hypothesis. No cross-notebook input is proposed. Mathlib matching coverage
is unchecked. This REVIEW_REQUIRED nomination has not approved itself.

Primary lead at nomination, now inspected for this target:
[Forrester, arXiv:1806.10411v1](https://arxiv.org/pdf/1806.10411v1).

## Completed source comparison — step389

The nomination above is preserved as the question asked at startup.
The completed fields and this section supersede its pending source status.
No mathematical calculation or sign test was performed. The newly ready
covered continuation needs separate supervisor approval before invocation.

### Exact known representation, with its hypotheses

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1, Section2, Lemmas1–2, (10)–(13), pp.7–8](https://arxiv.org/pdf/math/0505174v1#page=7).
The PDF carries the v1 identifier and a later generated title-page date;
the inspected version is identified by arXiv ID and equation numbers.
For a nonzero entire f with nonnegative coefficients, integers k>=0,
nu>=1 and radius R>0, Lemma1 is the formula

    nu! (2pi)^nu R^(k nu) A_k^nu(f)
      = integral_[-pi,pi]^nu product_j[e^(-ik theta_j) f(R e^(i theta_j))]
                   product_(alpha<beta)4 sin^2((theta_alpha-theta_beta)/2) dtheta.

Read the complete Cauchy-coefficient/composition/Vandermonde proof.
Lemma2 records the sign equivalence after division by f(R)^nu and
taking the real part. These are coefficient identities, not positivity
premises. Compact angular domains and entire f ensure absolute
integrability of the expanded products here.

For applicability use precisely the existing source interface
G(z)=xi(1/2+sqrt(z)/2)/8, which is entire despite its square-root notation.
[Michałowski v1, (1)–(3)](https://arxiv.org/html/2607.16795v1#S1.SS1)
and [O'Sullivan v2, (1.2)](https://arxiv.org/html/2007.13582v2#S1)
identify its ordinary coefficients with the a_n of this assessment;
L018/L021 identify the same actual completion and moments locally.
Thus f=G and nu=r satisfy the cited hypotheses, with G(R)>0. No
factorial is stripped from a_n. No new representation proof is needed
for this angular interface; it should be cited in any later canonical use.

### What the available sign results actually cover

Reuse step385's precise comparison of Katkova TheoremsC/2/3 and
Michałowski Theorem1.1 in
`2026-11-04-actual-jensen-mechanism-discovery.md`. The former gives
fixed-order eventual positivity; the latter states k>=10^18 r^3.
Neither is an all-order sign theorem on k=r-1. No finite low-order
minor experiment is nominated: inspected Michałowski Section1.2 also
discusses the far stronger finite-order consequence of verified zeros.

For the changed signed-integral scope, additionally read Katkova's
Sections3–4: (19), (32)–(48), and (49)–(62), including the local logarithm,
cubic phase bound, cutoff choice, near-angle and far-angle cases.
The proof keeps nu fixed: its positive core constant in (48), tail
constants in (49)/(57), and onset depend on nu. It cannot be used as
a uniform growing-order estimate. The phase-containing product in
(13) remains part of the integrand. Ordering variables is not a cited
method of eliminating that phase. Suspect transcription/generic-C
steps in the auxiliary estimates were not repaired or imported;
the paper's full analytic proof has not received an independent audit.

### Real moments and the Gram mismatch

P. J. Forrester, *Meet Andreief, Bordeaux 1886, and Andreev, Kharkov
1882–83*, [arXiv:1806.10411v1, (1.7), Sections2.2–2.3](https://arxiv.org/html/1806.10411v1#S2.SS2):
two function families give a bilinear integral determinant. Read the
permutation proof, row-by-row integration and discrete Cauchy–Binet
comparison; reuse the earlier assessment only for this identity.
For any noncompact specialization require absolute integrability of
every expanded product. The L019 decay and L021 finite moments are
available to check this for a finite polynomial integrand, but the
proposed row-integral identity has not yet been written or proved.

The matrix here contains a different (2(k+j-i))! in each entry.
Neither the cited identity nor L021 supplies conjugate-matched factors
for that matrix. A claimed Gram replacement must reproduce these
entries, not just their unfactored moments. No impossibility theorem
for all possible factorizations is asserted. The finite determinant
expansion and permutation averaging are the available toolkit for
testing the proposed real-variable representation; they are not an
imported positivity result.

### Single bounded continuation and its limits

Test the exact COVERED_TARGET above. First write and justify the
row-by-row real-moment representation, with all constants and factorials,
then average its integrand over assignments of the real variables.
This constructs the proposed object rather than assuming a Gram identity.
Use the fixed ordered family u_1=...=u_(r-1)=1, u_r=t>=1 and k=r-1,
for even r>=2. The desired test inequality is pointwise nonnegativity
of that fully symmetrized integrand. No value or sign is supplied here.
The actual factor product_j K(u_j) must remain present; K is not replaced
by atomic data or a generic measure. No theta tail is discarded.

A possible algebraic input, if the future calculation needs it, is
Katkova p.10's statement that cosh(sqrt(z)) belongs to SPF_infinity,
with coefficients 1/(2n)!; its paragraph gives the submatrix comparison
with the exponential coefficient matrix. This concerns a different
sequence and can only justify a specifically identified factorial
subdeterminant, not actual xi minors. Cite it rather than reprove its
total-positivity conclusion. Retain zero-index conventions and verify
that any selected minor falls within the source's strictness scope.

A rigorous negative value, or a signed leading coefficient giving one,
must extend by continuity to a nonempty open subset of strictly ordered
positive variables; a coincident-variable boundary example alone is
insufficient evidence about the integral. Such a witness abandons the
direct pointwise-positivity mechanism only. It cannot imply a negative
minor, because signed compensation is still possible. If this family
is nonnegative, that merely admits a better targeted test; it proves
neither global integrand positivity nor a determinant sign. Do not
turn finite success into an all-degree claim or start a parameter scan.

This is a symbolic sufficient-mechanism test across an unbounded order
family, not recomputation of an already positive low-order minor. Its
downstream use is to decide whether pointwise ordered-variable signing
can be pursued at all, before investing in theta-specific cancellation.
It leaves integrated compensation, uniform order control, k<r-1,
all-degree mixed signs and RH open. It is routine determinant development,
not a new central creative mechanism; no justified creative cancellation
target emerged from the inspected sources. That missing mechanism is
the current creative-routing blocker, not a historical global ban.

## Search, overlap and access record

Queries included `Riemann xi Taylor coefficients Toeplitz determinants
multiple integral factorial total positivity`, `Katkova Multiple
positivity Riemann hypothesis pdf`, `Riemann xi coefficient determinant
Michalowski total positivity O Sullivan`, `Riemann factorial Andreief`,
`Riemann Toeplitz symmetrization`, `xi coefficient multiple integral
positivity kernel factorial`, `Toeplitz symmetrized moments factorial`,
and `Riemann symmetrized integrand coefficients`. Follow-up exact
factorial/symmetrization/one-outlier queries returned no inspected
matching theorem; mostly irrelevant hits do not establish absence.
No novelty is claimed for the prospective symbolic test.

Local searches covered only this notebook's literature, ATTEMPTS and
foundations for Andreief, Katkova, factorial/Toeplitz, ordered variables,
symmetrization and one-outlier terms. Read the relevant L018/L019/L021
definitions/proofs, step385/386/387 assessments and L765 ATTEMPTS stop;
the supplied L765 audit conclusion was reused. Other signed arithmetic
or contour kernels were contrasts, not mathematical inputs. No sibling
notebook was read. L765 stops the unchanged unsigned norm comparison;
it says nothing about the sign test proposed here.

Shell retrieval of arXiv failed DNS resolution; browser HTML and PDF
were accessible and supplied the essential statements and proof cases.
This is not a SOURCE_BLOCKED assessment. No shell source file was saved.
Matching Mathlib coverage for the full factorial-weighted real-integrand
claim is not checked and remains unknown. No lemmas, scripts, DAG or
PROOF argument were modified in this literature-only step.
