# Six-coordinate twelve-incidence bound — completed scope review

TARGET: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-target, secant/line-decoding and finite-field incidence searches on 2026-10-07; compared local inputs and ATTEMPTS/017, /019, /020; inspected Tamo's primary incidence statement and RS proof, and Chojecki's newly accessible author TeX quantitative statements and exact ray-compiler proof; no adequate twelve-incidence import established.
SOURCE_EVIDENCE: Tamo, arXiv:2312.12962v1 (2023-12-20), Theorem 1.2 and section 5.2 Theorem 5.1 with proof, printed pp. 2 and 15–16, https://arxiv.org/pdf/2312.12962; Chojecki, RS_MCA_Paving_v9.2.tex, inspected 2026-10-07, named results/equation labels below, https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex; reuse primary shortening/distance and BCHKS coverage in 2026-10-07-six-coordinate-triple-equality-obstruction.md and 2026-10-07-six-coordinate-shortening-reduction-scope.md.
COMPARISON: L033 supplies the exact projective configuration and valid finite-parameter accounting. Inspected general estimates are quantitatively inadequate or require absent hypotheses; the exact ray compiler supplies a criterion without the needed zero-fiber bound. L015's five-coordinate maximum and rational-point descent do not apply. No inspected source closes N_ext<=12 for arbitrary extension-field weights.
GAP: Bound the valid additional incidences by twelve, or produce thirteen for an actual L033 pencil with N_3=0; neither the bound nor a refutation nor extension-field descent is established.
REASON: The missing quantitative assertion has now received its separate bounded source comparison; essential standard inputs and the exact local reduction are available, justifying one analytic attempt without asserting novelty or importing unread stronger claims.
SCOPE: L033's complete hypotheses, including F=F_(97^20), H of order sixteen in F_97^*, k=8, pinned cell, nonzero polynomial D and every locator, explicit union-six affine lift with three distinct finite full-weight errors, and N_3=0.

This completes the separate review requested by step 072, preserving
its exact target. EXPLORE approves an attempt, not the assertion. The
earlier REVIEW_REQUIRED stub and its source limitation are superseded
by the comparison below; no mathematics was derived during this review.
Shortening and distance coverage is reused without repeating its proofs.

Essential local inputs are L010, L032 and L033. Retain all eight shifted
moments, arbitrary F weights and parameters, possible cancellations,
shared intersections, full-weight tests, original parameter infinity and
same-support badness. Equality is an additional hypothesis whenever its
coordinate balance or locator saturation is used. The numbers 210 and
720 count indexed lines, not distinct points; rational defining lines
do not imply rationality of the pencil. No L015 enumeration or finite
sample bound may substitute for the extension-field assertion.

The main gap remains arbitrary-family sixteen-count equality. This
conditional bound would settle the union-six branch: L033 already
handles N_3>0 via L010, while N_3=0 gives |B|=3+N_ext. Universal
extraction, other support families, ABF26 identification, stronger-source
overlap and Mathlib coverage remain unresolved. ATTEMPTS/017, /019 and
/020 are preserved; this is not a restart of their failed criteria or
positive-only sampling mechanisms.

For a later approved mathematical attempt, continue on an analytic
bound uniform in the specified hypotheses or a rigorous obstruction
that narrows the possible equality configuration. A refutation must
produce thirteen valid additional finite incidences for an actual L033
pencil and verify all L010 hypotheses; abstract line intersections alone
do not refute the statement. An intermediate constraint may leave the
bound open and must be reported as such. If the source review reveals
essential missing coverage, keep the dependent claim parked instead of
deriving and approving it in the same turn.

## Completed bounded comparison, step 073

### Exact scope and local overlap

Read L033's hypotheses, conclusions and proof through its complete finite
accounting; L032's statement and affine/rank justification; and L010's
hypotheses, count and equality statements with its moment-kernel passage.
These establish the local question being assessed, rather than a new
derivation. The configuration is in P^5(F), with 210 disjoint-support
lines and 720 one-coordinate-overlap lines. It retains a particular finite
chart and full-weight tests. N_3=0 makes the required comparison twelve
versus the equality requirement thirteen; 930 indexed lines is not a bound
on the actual parameter count.

Reuse the inspected primary GRS formula and Hall distance proof with their
precise citations in L033 and the two prior assessments named above.
Reuse the prior BCHKS Theorems 1.3/4.6 applicability comparison: the first
ends at 7/32, below 1/4, and the second's displayed coefficient exceeds
sixteen. This does not require a fresh general MCA survey. L015's
five-coordinate configuration is a contrast only. Its rational-point
descent does not apply to intersections with rational lines, and its
enumeration maximum is not an input. L031 excludes a six-support cluster;
it supplies no universal extraction or completion of this triple.

### Primary incidence lead

Read [Tamo, arXiv:2312.12962v1](https://arxiv.org/html/2312.12962v1),
Theorem 1.2 (printed p. 2) and Theorem 5.1 with its full proof (printed
pp. 15–16). For any finite field of size Q, polynomial set L of degrees
less than k, and planar point set P, Theorem 1.2 gives
|I-|L||P|/Q| <= sqrt(|L||P|(Q+|L|(k-1))(1-1/Q)). Theorem 5.1 states
the RS average-radius list bound ceil(Q/(2 epsilon n sqrt(R))) at
radius 1-sqrt(R)-epsilon; its proof uses a sufficiently-large-Q
qualification and an o(1) term. No finite-constant repair is attempted.

Neither statement is the projective line-intersection assertion here.
No incidence-preserving planar transformation is supplied, and a list
around one word is not a count along this syndrome pencil. At n=16,
R=1/2, Q=97^20, the displayed list-size certificate is far larger than
twelve. This is a scope/size comparison, not an MCA application. The
inspected theorem is not an essential blocked input. A guessed v3 HTML
URL failed; the actual source has only v1 in its inspected version history.

### Newly accessible coding lead

Read [Chojecki's author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex):
MO3–MO4, OP/OP5–OP6 with proof, LC1–LC2, and DR2/DR6–DRC with proofs.
At n=16,k=8,r=4, MO3 fails: 144<192. OP fails: binom(16,4)=1820>5;
OP6 gives only 1820. LC1 requires 2r<R, whereas 8=R. Thus these claims
supply no fifteen-count certificate.

The exact ray compiler treats weighted Vandermonde parity columns over
any field and transverse support intersections; its pivot formula counts
zero fibers but does not bound them by twelve. Its proof handles v_E=0
as a common intersection, not a finite transverse slope. This overlaps
the compatibility criterion rather than closing L033's quantitative gap.
Subfield confinement requires subfield-valued received words, absent here.

This live author file is not certified identical to ePrint 2026/1463:
its landing-page title differs, its PDF returned HTTP 403, and the GitHub
PDF format was unsupported. Jo26 (2026/1432) is an unread reference lead,
not imported coverage. No stronger-source priority or correctness claim
is made.

### Search record, failures and decision test

Actual queries on 2026-10-07:

- `"Reed Solomon" "secant" "list decoding" pencil`
- `"Reed Solomon" "line" "list size" half distance correlated agreement`
- `"finite" "projective" "line" "incidence" "Reed-Solomon"`
- `"Reed Solomon" "six" "mutual correlated agreement"`
- `"line" "six" "MDS Paving Bounds"`

These located the inspected primary sources above, broad finite-geometry
and random-domain leads, and campaign pages. Unread discovery hits are
not theorem evidence. The already recorded campaign-artifact and
2025/1712 blockers remain parked; there was no new exact access lead for
those inputs. This is not a claim that all relevant literature is absent.
The author TeX was an independently accessible new lead, not a repeated
attempt to retrieve the parked campaign artifacts.

Read ATTEMPTS/017, /019 and /020 in full. They stop, respectively, the
universal six-edge small-union criterion, exhausted seven-block cyclic
containment, and positive-only finite rank sampling. None resolves or
bans the present conditional incidence count; none is reopened. No
mathematical script, finite sample or new lemma was written in this turn.

Continue with one analytic attempt on the exact TARGET, using L010,
L032 and L033. A useful outcome is a uniform bound or a proved constraint
that eliminates a specified thirteen-incidence equality configuration;
the latter must leave the full twelve bound explicitly open. Abandon the
asserted bound only for thirteen valid finite additional incidences of
an actual pencil with N_3=0, verifying D/locator nonpersistence and all
actual weights and moments. Abstract intersections or base-field-only
sampling do not meet that test. If the proposed mechanism merely
repackages L033 or needs unjustified descent, save the precise obstruction
and reassess rather than claim a bound.

Mathlib coverage of this exact incidence bound is not checked; unknown
coverage is not absence. The global fifteen bound, universal cluster
extraction, extension-field control, ABF26 identification and unread
stronger-source overlap remain unresolved. This completed step is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. EXPLORE reflects adequate
ingredient coverage and an unmatched quantitative target in the bounded
search, not certified originality or a mathematical advance.
