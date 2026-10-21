# Nonunitary-cusp enclosure production — source coverage completed

TARGET: Implement and independently replay L049's certified enclosure layer for the path {1/6,infinity} on y^2=x^3+1, after certifying minimality, conductor and local factors, with normalized interval width below 2^-20.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact 36a1/model/path and numerical-symbol implementations; inspected Cremona's exact data row and format, newform recurrences and small-prime Tate branches, Wuthrich's unitary criterion and Sage's numerical-symbol contract; compared L049, fixed enclosure code and ATTEMPTS/022--024. LMFDB browser challenges are nonessential after primary alternatives.
SOURCE_EVIDENCE: Cremona ecdata allcurves.00000-09999 row 36 a 1 [0,0,0,0,1] 0 6 and Table One documentation (2020-11-27); corrected second edition (1997), Section 3.1 pp.62--63, Section 3.2 pp.65--67 Tate lines 1--28, Section 2.6 equations (2.6.1)--(2.6.2) p.25; Wuthrich arXiv:1608.06423v2 p.3 unitary definition; reused BCDT Theorem A and audited L049 analytic/AGM coverage; current Sage numerical-symbol documentation inspected 2026-10-11.
COMPARISON: Known arithmetic and enclosure methods cover this CM/additive-reduction example and its nonunitary cusp. Published arithmetic data provide an independent comparison, not a finite replay; Sage's numerical return does not supply the requested complete certificate. No new method or originality claim is made.
GAP: Exact local arithmetic reproduction, all transporting matrices and Fourier coefficients, finite-function/tail and target-period enclosures, and a separate full replay remain unexecuted. No normalized interval or exact value is established.
REASON: Missing fixed arithmetic and implementation coverage is now adequate for one SPECIALIZE/REPRODUCTION attempt at unchanged TARGET; the review imports source statements and assesses applicability without deriving arithmetic or creating mathematical scripts.
LITERATURE_REASON: The start target was REVIEW_REQUIRED for this exact equation, small-prime arithmetic and first nonunitary-cusp executable enclosure; reuse ready analytic coverage rather than repeat the completed recovery audit.
SCOPE: Only [0,0,0,0,1] and the single oriented path {1/6,infinity}; independent minimality/conductor reproduction using the inspected early Tate branches, exact coefficient generation, L049 enclosure-layer production and separate finite replay. No full generator table, rational reconstruction, coefficient nonvanishing or generic implementation theorem.

## Initial proposal retained

The following proposal is historical; its pending-approval statements are
superseded by the completed comparison below.

This is a proposal, not an approved calculation. Reuse L049's approved
analytic comparison rather than repeat broad searches. The next review
must inspect primary evidence for the exact supplied equation, its
minimality, conductor (36 is a lead to verify), associated coefficients
and bad-prime factors. Check the actual cusp's nonunitary status at the
verified level. No arithmetic statement about this model is imported by
this proposal. Compare relevant fixed-case enclosure implementations
and failures narrowly; do not scan sibling notebooks or all checkpoints.

Essential mathematical input is audited L049, retaining L048's named
import qualifications if any exact-denominator conclusion is used.
L048's enormous clearing integer is not a promise of practical exact
recovery. The proposed test asks only for an outward interval of width
strictly below 2^-20, after division by the target's total minimal real
period, with complete separate replay of matrices, coefficients, all
finite errors and period branches. It must not round that interval to
a rational value without independent denominator/existence evidence.
Neither a complete integral generating list nor a normalized table is
claimed from this single path.

Potential downstream use is testing the executable enclosure component
of L049's general recovery algorithm on a nonunitary cusp. This example
does not supply an application of L027; its non-CM hypotheses and coefficient requirement remain separate.
The proposed finite target is independent of the parked twist-source
blocker and does not repeat a conditional audit as production. Continue
if source coverage supports exact arithmetic and complete finite replay;
narrow or change the target if either is unavailable. Preserve main rank,
rational-direction, Sha and complex-order gaps. No cross-notebook input.

Do not approve this new target merely because the preceding audit passed.
The completed mathematical audit remains valid while this continuation
receives its own literature approval next turn.

## Completed comparison — 2026-10-11, BSD-166

The main gap is still rank E(Q)=m(E) for arbitrary m(E)>=2. TARGET is
one executable test of the audited normalization machinery, potentially
useful before producing normalized inputs on other curves. It supplies no
rank-two application on this example. Continue on a complete independent
replay with normalized width strictly below 2^-20; diagnose or park on
unsupported arithmetic, failed enclosure inclusion or failed replay.
Do not replace this test with rounded numerical agreement.

### Primary arithmetic coverage

[Cremona's primary ecdata row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)
is `36 a 1 [0,0,0,0,1] 0 6` (retrieved 2026-10-11, zero-based line 72).
[Table One's format](https://johncremona.github.io/ecdata/), page updated
2020-11-27, identifies conductor and minimal Weierstrass coefficients.
Thus the published arithmetic matches the proposed equation exactly and
records conductor 36. This is a computational-source import; neither its
rank nor torsion column is needed. The data file was read narrowly at the
exact row, without a local download of the full collection. LMFDB curve,
class, newform and download pages returned challenges/errors; no theorem
or coefficient was inferred from their search snippets.

[Cremona Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf),
Sections 3.1--3.2, pp.62--67, supplies invariant/coordinate formulas,
discriminant scaling and Tate's algorithm for an integral model and a
prime. Inspected lines 1--28, including both p=2,3 coordinate branches
and exits I0, In, II, III, IV with their conductor exponents. The later
certificate must retain transformed coefficients, divisibility tests and
valuations. Minimality requires its own scaling check; small-prime
additive exponents cannot be taken from the p>3 shortcut. No Tate branch
has been executed here. If an uninspected later branch is reached,
dependent work needs renewed coverage. The published row is a comparison,
not a substitute for this requested arithmetic replay.

Reuse BCDT, *On the modularity of elliptic curves over Q*, JAMS 14 (2001),
843--939, [Theorem A and Introduction (1)--(2)](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf),
already inspected in `2026-10-10-conductor-eleven-general-adapter-replay.md`.
Its every-E/Q conductor-level association also covers the present equation;
the earlier implementation's non-CM restriction is not a theorem hypothesis.
No eta-product identification is needed or approved. Once the conductor is
certified, exact good-prime point counts and recurrences specify the
associated normalized newform; an LMFDB form label is unnecessary.

[Cremona Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Section 2.6, (2.6.1)--(2.6.2), p.25, was read through multiplicativity.
For a normalized newform, a(q)=0 if q^2 divides its level; prime-power
recurrence uses delta_N(p)=0 at bad primes and 1 otherwise. At imported
level 36 this covers q=2,3 and supplies their trivial Euler factors.
Good coefficients use the target's exact reduction counts. The later
certificate must generate every needed coefficient and replay all
factorizations/recurrences; singular-model point counts at bad primes must
not be mistaken for good-prime traces. This is applicability of a known
formula, not a newly derived local arithmetic result.

[Wuthrich v2](https://arxiv.org/pdf/1608.06423v2), 23 March 2017,
p.3, defines M=gcd(m,N), Q=N/M and unitary by gcd(M,Q)=1.
For the proposed denominator m=6 at the published level N=36, both M,Q
are 6, so this is a nonunitary-cusp test. No Atkin--Lehner unitary shortcut
is justified. Its conditional Proposition 1 normalization is not imported.

### Reuse, duplicate comparison and executable difference

The full L049 proof was read, including its independent minimal-target
period, finite-function refinement and division steps. Reuse the ready
`2026-10-11-arbitrary-relative-recovery-critical-audit.md` and construction
assessment for Wuthrich Lemma 4/Section 5.1, Cremona cusp/Hecke identities
and positive-AGM cases. These already cover CM, additive reduction, zeros
and arbitrary cusp endpoints. No new analytic lemma or reproof is needed.
The separately audited L049 orientation and matrix sign control the
implementation; do not copy the flagged source closing display unchecked.

Local searches in literature, foundations, ATTEMPTS and history found only
the present proposal and general nonunitary-cusp discussions for this exact
example. This is a duplicate check, not a claim that no published exact
symbol value exists. Exact-model/path and stronger implementation searches
included `36a1 modular_symbol 1/6`, `36a1 eta 6`, and
`site.doc.sagemath.org mod_sym_num 36a`. Unrelated hits and the OEIS
eta-product lead were not used as theorem evidence.

The [current Sage numerical-symbol documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html),
read 2026-10-11, documents `approximative_value` returning a real number at
requested binary precision and optional twist reduction. Its convention
uses the infinity-to-r integral and least positive real period. This
differs from the target's r-to-infinity orientation and total minimal
period. It is relevant existing algorithm coverage, not the required
outward endpoints, finite evidence or separate replay; no software value
was requested or imported.

Read the interval primitives, finite exponential checks and coefficient
checks in `scripts/conductor-eleven/twist-five/certify.py` and `verify.py`,
plus the distinct endpoint audit design in `audit.py`. They are method
comparisons only: their twist-specific positive real exponential, model,
bad-prime recurrence and scale cannot be transferred unchanged. The new
transport points require certified complex exponential rectangles and
every ell+1 term. No such adapter currently exists for this example.
ATTEMPTS/022--024 were read: their stop evidence concerns repeating
conditional audits without actual inputs. This finite production target
is different, and the independent uniform-twist blocker stays parked.

### Approved bounded attempt and remaining assumptions

SPECIALIZE approves exactly TARGET for one REPRODUCTION turn. Essential
local input is audited L049. L048 is needed only if exact-denominator or
integer-isolation claims are later made; those claims are outside this
single-interval test and retain L048's named-import qualifications.
No complete generating list is needed to evaluate one actual path using
L049's enclosure layer. A successful result must have a canonical proof
of source applicability and complete certificate files, not only a summary.

First reproduce minimality/conductor with the inspected arithmetic cases,
compare with the primary row, and bind exact associated coefficients.
Then implement the L049 transport and independent target-period layer.
Retain cusp reduction, Bezout/congruence witnesses, each matrix and image,
the good-prime closing scalar, every coefficient, truncation tail, all
finite errors, positive square-root/AGM branches, component factor and
final outward division. Independently replay all evidence using separate
arithmetic code, with the actual rational width and required threshold
printed alongside failures and certificate paths. A preview is not replay.

Width below 2^-20 alone licenses neither rational rounding nor exact
recovery, nonvanishing, a normalized generator table or L027 applicability.
Runtime remains unbounded theoretically; a failed finite schedule is an
implementation result, not a failure of L049. Preserve unfinished evidence
and diagnose the specific failure before enlarging a schedule. The rational
direction, Sha and complex-order gaps remain. No cross-notebook input is
used. Full matching Mathlib coverage and supporting arithmetic/interval
formalization were not checked; no absence is asserted.
