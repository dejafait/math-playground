# Centered signed Hermite-extremum margin — source review

TARGET: Determine whether some fixed a>0 gives Q_d^(a)(2sqrt(a)r-gamma_1/gamma_0)H_d(r)>0 for every d>=2 and every zero r of H_(d-1), using the full actual coefficient sum.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step381 searched exact centered Hermite/Jensen interlacing, signed-extremum and residue formulations; reused the October31 signed-Hermite review and step379 primitive comparison; checked L763 and its stop. No inspected result supplies the actual fixed-a, n=0 all-degree signs. A bounded residue-moment obstruction test is specified below; no novelty inference.
SOURCE_EVIDENCE: O'Sullivan arXiv:2007.13582v2, Sections3.1–3.2/Lemma3.4/Theorem3.5 and proof, Theorems1.3/1.4/8.1 with (8.2)–(8.5) comparison reused; Liu–Wang arXiv:math/0509207v5 Theorem2.1 and complete strict/weak proof; Fisk arXiv:math/0612833v2 Section1.3 Lemma1.20(3)/(1.3.3) and proof, printed pp.12–14; DLMF18.2(vi), 18.9.1/Table18.9.1 Hermite row and 18.9.25 inspected.
COMPARISON: Known sign/interlacing and residue criteria provide an interface, not an actual-theta estimate. Large-shift hyperbolicity and the failed nonnegative budget do not settle this stronger prescribed-grid sign test. The source residue characterization permits a finite-coefficient necessary-condition diagnostic before attempting all-degree signed estimates.
GAP: The actual centered quotient has not been expanded or bounded. Neither its residue signs, its low-order moment feasibility nor any all-degree margin is established, including n=0 and every fixed a>0.
REASON: Coverage now supports one bounded symbolic obstruction test on the unchanged target: use the first three negative-power Laurent coefficients of the full centered quotient and necessary positivity of its putative negative-residue measure. Derive and test these conditions only in a later research turn; do not assume actual hyperbolicity.
SCOPE: Exactly TARGET, with Q from L763, actual coefficients from L018/L021/L028, one fixed a>0 and all d>=2. Next research may specialize the cited sign/residue interface and test the quotient through x^(-3), using gamma_0 through gamma_4 and justified actual-theta bounds. No higher-order hierarchy, changed grid, degree-dependent a, input root signs or numerical-only conclusion is covered.
LITERATURE_REASON: Essential interlacing and signed-residue comparison was absent from the preceding norm-budget assessment; its unchanged O'Sullivan and actual-coefficient coverage is reused.

## Completed source comparison — step381

The main gap remains actual-Xi all-degree positivity. The intermediate
target is exactly TARGET above. Successful signs could give a sufficient
all-degree hyperbolicity mechanism through the cited product interface;
failure would stop this prescribed Hermite grid, not RH or hyperbolicity.
The current review establishes neither alternative. This is literature
EXPLORATION, with a concrete test replacing the uncovered nomination.

### Imported interfaces and their limitations

**Product interface.** Cormac O'Sullivan,
[*Zeros of Jensen polynomials and asymptotics for the Riemann xi function*,
v2, 9 December 2020](https://arxiv.org/html/2007.13582v2#S3),
Theorem3.5 assumes real entire Phi of genus1* and an LP multiplier Omega.
All-degree product-Jensen hyperbolicity characterizes hyperbolicity of
Phi. Its proof uses product genus, real multiplier zeros and Theorem3.1,
not a signed estimate. Section3.1 identifies actual Theta as order1/2.
The positive Gaussian scaling and actual normalization are in L763;
the later calculation must check the additional translation explicitly.
Theorem1.3 requires a large positive shift relative to degree; it does
not cover n=0. Theorem1.4's asymptotic has fixed expansion order and an
unspecified onset. Neither controls all summands of the signed evaluation
at the proposed grid. Sections3.2 and8 and the prior full application
comparison were checked/reused; no large-shift theorem is being reproved.
The previously recorded HTML Gaussian-power typo remains qualified by
L763's direct finite calculation. No theorem asserting actual signs is
imported.

**Sign test.** Lily L. Liu and Yi Wang,
[*A unified approach to polynomial sequences with only real zeros*,
arXiv:math/0509207v5, 27 November 2006](https://arxiv.org/html/math/0509207),
Advances in Applied Mathematics38(2007),542–560, Theorem2.1: for
F=A f+B g, real polynomials, deg F=deg f or deg f+1, f,g real-rooted
with g interlacing/alternating f, and matching leading signs of F,g,
B(r)<=0 at every root r of f suffices for real-rooted F and interlacing.
Strict input interlacing and strict signs give strict output interlacing.
The proof's interior intervals, exterior rays and weak-sign perturbation
case were read. No recurrence or B of the required sign for actual Q
is supplied. Only the strict, distinct-node interface is needed here;
specialization must retain both exterior intervals and leading signs.

**Quantitative residue test.** Steve Fisk,
[*Polynomials, roots, and interlacing*, arXiv:math/0612833v2](https://arxiv.org/pdf/math/0612833v2),
Section1.3, Lemma1.20(3), printed p.13, with basis construction p.12
and proof/continuation pp.13–14: if f has n distinct real roots a_i
and positive leading coefficient, and g has degree n+1 and positive
leading coefficient, write

    g(x)/f(x) = A x+B+sum_i c_i/(x-a_i).

Then A>0 and strict interlacing holds exactly when all c_i<0.
The source identifies c_i=g(a_i)/f'(a_i). Its third-case exterior-root
argument and converse sign argument were read in full. Distinct roots
are essential to this simple-pole representation. This supplies a
coefficient-accessible characterization, not the signs of actual Q.
The retrieved PDF labels itself version2 and carries the arXiv v2 stamp
11 March 2008, while its title-page date reads 26 November 2024;
the precise version URL and printed lemma/pages fix the inspected text.
The screenshot of PDF page25 timed out; the complete mathematical
statement and relevant proof were available in parsed text. No unread
image is treated as evidence.

**Hermite hypotheses.** [DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi)
gives simple real zeros and separation of successive orthogonal
polynomials. [18.9.1/Table18.9.1](https://dlmf.nist.gov/18.9#T1)
fixes the physicists' recurrence H_(m+1)=2x H_m-2m H_(m-1).
[18.9.25](https://dlmf.nist.gov/18.9.E25) gives
H_m'=2m H_(m-1). These establish the source ingredients for checking
orientation at the proposed H_(d-1) nodes in the later specialization.
They do not imply a sign for a general Hermite combination.

### One bounded continuation, with no calculation in this turn

For the next test define only the object

    P_d(x)=Q_d^(a)(2sqrt(a)x-gamma_1/gamma_0),
    R_d(x)=P_d(x)/H_(d-1)(x).

First justify the sign-to-residue direction using the cited identities
and matching positive leading coefficients. Then extract exactly the
x^(-1), x^(-2), x^(-3) coefficients after polynomial division of R_d.
Use the elementary finite-positive-measure square/Cauchy–Schwarz
conditions on the putative negative residues as necessary conditions,
with every weight and real support hypothesis explicit. The question is
whether these low-order conditions already contradict the proposed
signs for arbitrarily large d for every fixed a. This is a proposed
discriminating test, not a derived inequality or approved new result.
No formula for these coefficients or actual sign is asserted here.

Use the full polynomial: the later proof must explain exactly why the
selected Laurent coefficients depend only on its leading coefficients,
rather than silently dropping other summands at a Hermite node. Actual
gamma_j remain the factorial-scaled moments of L021/L028, not a raw
moment sequence. Any sign of a centered coefficient must be proved
from actual-theta information, with rigorous error bounds if needed;
L021's positive raw moments alone do not settle a centered sign.

Abandon this strict prescribed-grid method if one necessary condition
fails eventually for every fixed a, recording a symbolic threshold
and every unresolved actual-coefficient assumption. Continue only if
this test yields new sign-feasibility information or a concrete signed
estimate; passing finitely many degrees is insufficient. If the three
coefficients are inconclusive, park this test with the exact residual
condition; do not automatically extend to a higher hierarchy. All
other signs, actual RH and the independent source audits remain open.

The test is conventional finite algebra and necessary-condition
analysis, routed calculation/standard/high, not a creative RH proof.
No independently justified cancellation estimate currently warrants a
creative proof attempt; this is the precise discovery blocker. Newly
updated ready coverage receives the supervisor's separate approval
before mathematical invocation. No lemma or mathematical script is
written in this source-only turn. Mathlib coverage is not checked.

### Searches, overlap and noninputs

Queries included `O Sullivan 2007.13582 generalized Jensen polynomials
Hermite Turan Theorem 3.5`, `Jensen polynomials Riemann xi Hermite extrema
interlacing centered fixed Gaussian hyperbolicity`, `Hermite Jensen
polynomial sign at zeros H d-1 centered gamma interlacing O Sullivan`,
`polynomial interlacing residues partial fractions positive residues
theorem real roots`, `"Hermite" "Jensen" "interlacing" "centered"`,
`"Jensen" "Hermite" "residues"`, and exact Fisk-title searches.
Followed primary statements/proofs above rather than using snippets
as theorem evidence. No matching actual signed margin was found in
the sources inspected; this is not a novelty or impossibility claim.

Local comparison used L763, its fixed-Gaussian stop/working record,
the October31 `actual-hermite-signed-cross-term-review.md`, and
`2026-11-04-theta-jensen-prescribed-primitive-margin.md`. Narrow searches
of literature/attempts for Hermite Laurent/residue-moment formulations
found no prior exact diagnostic. Romik truncation/CD-cone results concern
different coefficients; their stops do not establish a result about R_d.
Prescribed-primitive descent remains parked; this test does not use it.

The GORZ large-shift comparison is reused from those reviews, not
claimed to prove the unshifted margin. Search hits for Planat2026,
Holland's high-shift wedge and a Jin centered-binomial/Jacobi family
are uninspected leads and are not inputs. A search excerpt explicitly
using computed cases/structural expectations supplies no all-degree
theorem. No new conclusion about those manuscripts is asserted.
Turan1959 access failures recorded in the October31 review were not
retried. DLMF .tex requests were unsupported, but its rendered formulas
and Hermite recurrence table were readable; no essential source remains
blocked for the selected finite-algebra test.

## Original nomination from step380 — historical, preserved

## Exact proposed object and purpose

Use Q_d^(a) exactly as defined in L763 and actual gamma_j as in L021/L028.
H_m is the physicists' Hermite polynomial. This is a nomination only:
neither the displayed signs nor a theorem transferring them to all-degree
hyperbolicity is proved in this assessment. No input Jensen hyperbolicity,
degree-dependent a, omitted higher summands or computed-zero premise is
authorized. L018 fixes the actual Xi normalization.

The possible downstream use is a full signed-extremum argument for real
zeros, independent of the squared norm that L763 excludes. The next turn
is literature-only: compare exact theorem hypotheses, duplicate tests and
recorded failures before approving any mathematical attempt. Primary
Hermite interlacing results and source applications must be inspected;
the product equivalence alone provides no actual signs.

Continue only if that comparison identifies a concrete independent
signed-estimate mechanism or a discriminating symbolic obstruction test.
Park the target if it merely restates desired positivity without such an
input. A finite sample alone does not meet an all-degree margin.

If coverage supports a genuinely new signed mechanism, nominate
proof_attempt/creative with the precise fixed-a extremum obstruction and a
bounded test, after the separate literature gate. Such a route could bear
on the central all-degree gap; it is not approved or claimed ready now.
Mathlib coverage is not checked.
