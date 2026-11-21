# Single finite extension at a logarithmic Hankel contact — review2127

TARGET: Assess whether positivity of the single finite extension H_3(lambda_*) forces c^T H_2'(lambda_*)c<=0 under H_2(lambda_*)c=0 for the actual L058 logarithmic coefficients, at 0<lambda_*<=1/8, without assuming positivity at any higher degree.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review2127 checked truncated Hamburger, singular Hankel extension and heat/null-vector terminology; read the primary Curto-Fialkow theorem and the relevant singular proof case below. Reused the November6 heat/contact and score comparisons and checked the recorded finite-contact root and finite-block stops. No inspected theorem directly signs this heat contraction; failed searches imply no novelty.
SOURCE_EVIDENCE: Curto-Fialkow, Houston J. Math.17(4)(1991),603-635, Lemma2.3 pp607-608, Theorem2.4 pp608-609, Theorem2.6/Remark2.7 pp609-611, Theorem3.1 pp611-612, Corollary3.4/proof pp615-616, and Theorem3.9/proof pp619-620; primary journal PDF. L058/L874 fix the analytic normalization and recurrence; their ready source assessments are reused.
COMPARISON: For S_2>0, Theorem3.1 applies with k=2 and gamma_j=S_(j+2): the given H_3 is precisely the positive extension in (vi), and the theorem represents the prescribed S_2,...,S_7. This covers L874's required coefficient range without H_4 or flatness of the given H_3. It does not sign the nonlinear heat contraction or represent the prescribed S_8. S_2=0 remains outside this positive-mass theorem.
GAP: The only proposed mathematical difference is the exact finite contact sign from L874 under the additional single-extension premise, including zero mass and all lower-degree null vectors. Actual-family realizability, actual H_3 positivity, initialization, equality handling, global and all-degree continuation remain separate; no actual-theta sign or counterexample is supplied.
REASON: The changed premise has usable finite-moment coverage through the highest required coefficient. Import that theorem rather than reconstructing moment theory; permit one bounded algebraic specialization, subject to separate approval, to decide whether this finite-premise mechanism signs the contraction. Do not assume a positive infinite hierarchy or increase the extension degree if this test fails.
SCOPE: One slice 0<lambda_*<=1/8; L058/L874 logarithmic S_k; H_3>=0 and H_2 c=0 for every real nonzero c in R^3, including c_2=0 and S_2=0. Later work may use the cited theorem for S_2>0 and elementary PSD algebra for excluded zero mass, and evaluate L874's finite contraction. A generic finite-data obstruction tests only sufficiency of these premises, not actual theta or RH. No density realization, higher-degree sweep or global positivity proof is covered.
LITERATURE_REASON: This turn supplies essential missing coverage for one positive H_3 extension, which the reused bare-contact assessments excluded; no unchanged heat/score source review was repeated.

## Completed source comparison, 21 November 2026, step2127

The main gap remains L030-L032/C032a, actual-Xi all-degree algebraic
mixed positivity. The intermediate target is the unchanged TARGET above.
A conditional contact sign could contribute to decreasing-parameter
continuation, while leaving the independent obligations in GAP unpaid.
The discriminant for later mathematics is an exact contraction proof
under precisely the finite premises, or an exact obstruction showing
that those premises alone do not supply it. The latter would leave
the actual-theta conditional question open unless separately realized.

### Primary theorem and essential proof case

Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity, and
Truncated Moment Problems*, Houston Journal of Mathematics **17**(4)
(1991), 603-635, [primary journal PDF](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf).
Theorem3.1, pp611-612: for real gamma_0,...,gamma_(2k+1) with gamma_0>0,
a positive representing measure on R is equivalent to A(k)>=0 and
v_(k+1) in Ran A(k), and to a positive Hankel extension with the
specified gamma_(2k+1). A finitely atomic measure can be chosen.
Lemma2.3 provides the block-matrix range criterion. Read Corollary3.4's
singular proof, pp615-616: reduce to the first invertible corner, use
Proposition3.3, and propagate its moments by the forced recurrence.
Thus singularity does not invalidate the odd theorem. Theorem3.9,
pp619-620, treats the even truncation. Theorem2.4 and Remark2.7 retain
a possible excess in the last diagonal entry of a positive extension;
positivity does not assert flatness of that extension. No heat
derivative sign or nonnegative-support conclusion occurs in these
statements. The paper assumes positive initial mass; zero mass needs
separate treatment. These are imported tools, not a new moment theorem.

The primary text was read at the cited theorem/proof ranges; OCR
inequality artifacts were not used to infer extra rank equalities.
Screenshot requests did not expose inspectable page images in this
session. The selected equivalences and moment ranges are legible in
the text. A direct shell download failed DNS, but the journal PDF was
accessible through the web tool; this is not a source blocker.

### Exact applicability interface, without a contact calculation

Keep the original definitions below. At the fixed slice, the proposed
source substitution is

    gamma_j = S_(j+2),  0<=j<=6,
    A(2) = H_2,
    v_3 = (S_5,S_6,S_7)^T,
    A(3) = H_3 = [[H_2,v_3],[v_3^T,S_8]].

These are identifications of entries, not a new evolution law.
For S_2>0 the hypotheses of Theorem3.1(vi), with k=2, match the
assumed single extension exactly. Its conclusion concerns the odd
prefix gamma_0,...,gamma_5, namely S_2,...,S_7. No positivity of H_4
is needed. Conversely, applying an even theorem directly to all seven
entries gamma_0,...,gamma_6 would require additional extension coverage;
that is not authorized here. No representing measure for prescribed
S_8, no equality of ranks H_2 and H_3, and no support in [0,infinity)
is inferred. S_1 is not a moment in this substitution.

L874 already proves that for d=2 the contact contraction uses no
coefficient beyond S_7. Its cancellation of S_1 uses H_2 c=0.
Therefore the odd theorem covers the entire coefficient range needed
in the positive-mass case. This is the useful source-scope finding,
not a proof that the resulting expression is nonpositive. The theorem
does not connect its auxiliary measure to the positive density in u
from L058; those are different moment problems.

The later bounded test must retain every null direction, all singular
ranks, and the S_2=0 branch without dividing by it. It may import
Theorem3.1 and Lemma2.3 with their hypotheses; reproof of truncated
moment theory is unnecessary. It must distinguish a universal
finite-sequence implication from a claim restricted to the actual
theta trajectory. Generic finite data, if used to obstruct the former,
are not certified logarithmic coefficients of actual F. No such
example, contraction expansion, zero-mass conclusion or lemma is
derived in this literature turn.

### Search, duplicates and stopping decision

Queries included `truncated Hamburger moment problem positive
semidefinite Hankel extension singular Curto Fialkow theorem`,
`Hankel moment matrix kernel positive extension recursively generated
univariate truncated moment theorem`, the exact Curto-Fialkow title,
and combinations of Hankel, heat, logarithmic, null vector and Burgers.
The journal PDF was followed from the title search. Other matrix,
multivariate and full-hierarchy results were leads, not imported inputs.
Unrelated RH syntheses and search snippets are not theorem evidence.

The ready assessments `2026-11-06-reciprocal-hankel-heat-contact.md`
and `2026-11-06-actual-theta-contact-score-pairing.md` were reused for
the unchanged heat/score tools. The recorded bare contact stop is
`ATTEMPTS/2026-11-06-reciprocal-hankel-contact-sign-unpaid.md`;
its conclusion explicitly leaves extra finite equations available.
The kernel-root assessment `2026-11-14-contact-kernel-polynomial-root-test-889.md`
and its C466c stop use signed minors with a negative raw minor,
so they do not refute the present full-PSD extension premise.
`ATTEMPTS/2026-11-16-finite-block-only-extension-source-stop-1117.md`
concerns a different finite-sign-to-global inference and supplies no
answer to this contact contraction. These scoped checks found no
duplicate result for the changed target; no claim of novelty follows.

Coverage is SPECIALIZE for one bounded finite algebra test. Continue
only if it gives the stated sign under exact premises or identifies
a precise obstruction; stop this finite-premise mechanism if it
requires an unprovided actual-theta sign or an infinite positive
hierarchy. No generic failure would justify declaring actual theta
false, and no conditional success would establish actual H_3 positivity.
Full matching Mathlib coverage is unchecked; no absence is claimed.
The separate approval of this changed ready assessment belongs to the
next invocation. No protected creative mechanism is justified yet:
the independent actual-theta signed input is still missing.

## Original nomination2126 body, preserved as historical scope

The following records the prior nomination, not a claim that its source
leads remain unread after the completed comparison above.

Use L874's notation exactly:

    log(F(lambda,z)/F(lambda,0))
        =-sum_(k>=1) S_k(lambda) z^(2k)/k,
    H_j(lambda)=(S_(a+b+2)(lambda))_(0<=a,b<=j).

This does not use nomination2125's distinct full-zero z^(-k) sums.
The time is notebook lambda, not Polymath's source t. Essential local
inputs are L058,L874 and L030/L032/C032a for the downstream gap;
L024/L025 supply only the established zero-time interpretation.
No cross-notebook input is needed. Full matching Mathlib coverage
is unchecked.

Review existing contact and finite-moment/extension failures before
loading additional proofs. Retrieve the precise primary moment-theorem
hypotheses, especially whether PSD alone suffices at a singular finite
truncation, before invoking a positive atomic measure. Check whether
the required polynomial relation includes exactly the coefficients
appearing in L874; do not silently require H_4, arbitrary extensions,
or real-root support. A standard theorem that covers the statement
should be imported, not reproved as new mathematics.

The discriminant is a precise theorem-level conditional implication,
or a specific failure of the finite-extension hypotheses. Continue
to one bounded algebraic attempt only if source coverage is ready
and the contraction test is well defined under exactly these premises.
Park this target if it only restates an assumed infinite positive
moment hierarchy or requires an unprovided actual-theta sign. A
generic finite-sequence obstruction, if later authorized, would
refute only the finite-premise implication, not actual theta or RH.

This nomination establishes no mathematical implication. A favorable
conditional result would identify one finite degree of signed closure;
it would not prove the stronger premise for actual theta or eliminate
the unbounded-degree/global-continuation gaps. There is presently no
justified creative invocation: an independent actual-theta signed
input or a noncircular explicit K is still missing. Do not label
standard finite moment specialization as creative to meet a schedule.
