# Adjacent-shift propagation — bounded obstruction nomination

TARGET: Assess whether a rational degree-five PF2 polynomial with eventual D_(r,3)>0 but infinitely many D_(r,4)<0 obstructs adjacent-shift propagation from finite-PF and fixed-shift inputs.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded primary-source comparison on 2026-11-06: exact eventual-positivity/adjacent-condensation/PF2-degree-five and banded-Toeplitz/rectangular-Schur searches; targeted L791/L792/L825/L834, L772 statement, reciprocal-duality assessments and step659/667 failure records. No matching exact counterexample or transfer theorem was identified; this is not a novelty claim.
SOURCE_EVIDENCE: Alexandersson arXiv:1208.5607v1 Theorems1/6, equation(6), Lemma15/Proposition16 and complete Section3.2 proof, pp.2,5,11–12, https://arxiv.org/html/1208.5607v1 ; Zeilberger math/9808079v1 equation(Alice) and complete two-page proof, https://arxiv.org/pdf/math/9808079v1 ; reused Katkova math/0505174v1 Definition2/(8)/TheoremB pp.4–5, https://arxiv.org/pdf/math/0505174v1 ; Branden–Chasse arXiv:1405.6378v1 Section1/Theorem2.1/Example2.1 pp.1–3, https://arxiv.org/html/1405.6378v1 . Exact applicability and nonmatching stronger results below.
COMPARISON: Known exact fixed-band formulas cover arbitrary distinct complex roots without PF_infinity and permit an infinite-rank sign test by a finite exponential sum. Condensation is a difference identity, not a sign-transfer theorem. The exact rational PF2 model and both infinite-rank signs remain unproved; a PF2 obstruction would not refute an implication requiring C832a's much higher finite order.
GAP: Specialize the cited formula to one degree-five rational polynomial, certify all ordered minors through rank2 by an applicable criterion, prove eventual shift3 positivity and infinitely many negative shift4 ranks with complete dominant-term/error or exact recurrence evidence. No construction, sign calculation or new result was performed in this literature turn.
REASON: Essential source coverage is now available for a separate bounded known-method model test. No inspected theorem settles the exact model, and no repeated source access or actual-Xi numerical setup is needed. The next ready continuation still receives separate supervisor approval.
LITERATURE_REASON: The next target changes from a ready finite-PF audit to an uncovered adjacency obstruction question; primary theorem comparison and duplicate coverage are essential before mathematical work.
SCOPE: Completed literature-only review. The unchanged model class has positive rational ordinary coefficients in degrees0–5 and zero elsewhere; PF2 means every ordered minor of size at most2. Source coverage permits a later distinct-root fixed-band specialization at shifts3/4; it does not establish a model or approve mathematics during this turn.

## Completed source comparison: 2026-11-06

The main gap remains L030–L032/C032a's actual-Xi all-degree mixed
positivity. The intermediate target is the exact model question in TARGET.
Its downstream use is to test a proposed abstract adjacency bridge before
requiring another Xi sign estimate. Even success would concern PF2, not
arbitrary prescribed PF_m or C832a's entire large finite band. It would
neither disprove RH nor resolve L836's finite/eventual overlap.

### Primary hypotheses and essential cases

**Exact fixed-band input.** Per Alexandersson, *Schur polynomials, banded
Toeplitz matrices and Widom's formula*, EJC 19(4) (2012), P22,
[arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1), Theorems1/6
pp.2/5 and Section3.2 pp.11–12. The normalized finite sequence has s_0=1;
D_c^k deletes the first c columns of (s_(j-i)) and takes a leading
k-square. Theorem6 assumes distinct roots x_i of the polynomial in (6):
chi(t)=prod(t-x_i)=(-1)^n sum_i(-t)^(n-i)s_i. It expresses det D_c^k
as a sum over c-element subsets of powers of their root products, with
the explicit cross-difference coefficients in Theorem6. Complex x_i
are allowed. Lemma15 checks reciprocal signs; Proposition16 and the
rectangular-partition argument prove the formula. This supplies an exact
formula, not an automatic sign. Repeated roots require separate treatment;
the proposed bounded test will avoid them. The general recurrence's
Theorem4 has inconsistent tuple inequalities in its printed statement;
the continuation can use Theorem6 directly and need not repair it.

**Condensation.** Doron Zeilberger, *Dodgson's Determinant-Evaluation Rule
Proved by Two-Timing Men and Women*, EJC 3(2) (1996), R22,
[math/9808079v1](https://arxiv.org/pdf/math/9808079v1), equation(Alice)
p.1 and the complete proof p.2. The identity is for an arbitrary square
matrix: full determinant times the central minor equals the product of
the two principal corner minors minus the product of the two other
corner minors. The proof pairs signed determinant terms and cancels the
unmatched terms; it assumes no positivity or minor invertibility. A
quotient form would require a nonzero central minor. Thus this source
does not itself assert that signs at one shift propagate to another.
The comparison does not derive a new Toeplitz recurrence or inequality.

**Finite PF input reused.** Katkova, *Multiple positivity and the Riemann
zeta-function*, [math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition2/(8), TheoremsA/B pp.4–5. PF_m concerns all ordered minors
through size m. TheoremB supplies polynomial PF_m from f(0)>0 and the
stated open zero-free sector |arg z|<pi*m/(m+1); boundary roots are
permitted. Any proposed specialization must check that precise sector,
not merely positive coefficients or selected contiguous 2-square minors.
TheoremA is a necessary sector bound; neither statement supplies the
desired shift3/4 signs. This ready assessment is reused, not reproved.

**Stronger but nonmatching preservation.** Branden–Chasse, *Infinite
log-concavity for polynomial Polya frequency sequences*,
[1405.6378v1](https://arxiv.org/html/1405.6378v1), Section1 and Theorem2.1/
Example2.1 pp.1–3. Here polynomial sequences mean infinite sequences
a_j=p(j), not coefficients of finite polynomials. Their theorem requires
PF (all minors), polynomial interpolation and the listed classes with
specified consecutive integer roots of p. Example2.1 concerns failure of
PF preservation by the Turan operator on such infinite sequences. Neither
the theorem nor its example matches a degree-five coefficient sequence,
PF2, or the two fixed-shift infinite-rank sign requirements. No use of
the preservation proof or this example as a model certificate is proposed.

### Search, local overlap and access record

Queries included “Toeplitz determinants rectangular Schur polynomial
asymptotics banded Widom formula roots”, “Polya frequency PF2 log concave
sequence contiguous minors Dodgson condensation positivity propagation”,
“Toeplitz determinants eventually positive polynomial”, “Polya frequency
eventually Toeplitz minors”, and “PF2 degree five polynomial”. Search
snippets and secondary summaries were leads only. The inspected primary
sources above do not contain the exact nominated obstruction. Alexandersson's
references identify the older Widom formula and Hall-polynomial identity;
its own complete formula proof was read, so unread original references
are not essential inputs. No assertion of novelty follows from the search.

L834's proof and its fixed-shift source assessments already supply
complementary-minor duality and meromorphic coefficient estimates.
They require a fixed simple pole packet and a separating contour and
give no adjacent-shift conclusion. Their ready coverage remains valid.
L791/L792 concern an actual-coefficient central Jensen matching model;
L825 concerns its additive Appell lowering defect. They are not this
ordinary-coefficient fixed-band test. L772's statement and its recorded
stop refute a bridge from all Turan iterates to one minor, but do not
certify the nominated eventual ray. Step659's unpaid hybrid cofactor
ratio and step667's growing-order source limitations remain untouched.
No sibling notebook, checkpoint scan or cross-notebook theorem was used.

Primary PDFs/HTML were available through the web tool. Direct shell PDF
downloads failed at DNS resolution; no PDF/text was cached. The attempted
Brenti Stan70 author URL returned404 and is not an input: the already
assessed Katkova criterion suffices. No persistent essential source blocker
remains. Matching Mathlib coverage was not checked; no absence is asserted.

### Bounded continuation and decision

Use the distinct-root exact formula, with positive normalization and the
source's rank/shift conventions explicitly checked. Seek one rational
degree-five model; do not initiate an unbounded parameter sweep. Establish
PF2 by a criterion covering every ordered minor. For the two sign claims,
retain all leading terms, possible conjugate ties, their coefficients and
an explicit smaller remainder. A periodic-phase subsequence can be used
only after its phase, strict negative margin and infinite ranks have been
proved exactly. Finite sign samples are diagnostic only.

Continue only upon a complete model certificate or a precise mathematical
obstruction to that bounded ansatz. Stop this particular attempt if
distinctness, PF2 or either infinite-rank sign remains unproved; preserve
partial reasoning and require a refined mechanism before repeating it.
Do not reprove Widom, condensation or the sector theorem. A local
specialization would be REPRODUCTION; no advance beyond the checked
sources or additional actual-Xi signed input is established by this review.

## Original nomination retained (superseded instructions)

The following text records the pre-review nomination. Its statements that
sources remain uninspected describe the earlier state only; the completed
comparison and the separate next-target assessment govern resumption.

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate question is whether two currently available types of
sign information can propagate to the next shift by a
Desnanot–Jacobi argument. A countermodel would block that abstract
inference and identify a needed extra Xi hypothesis; it would not
refute any actual-Xi sign or RH. A positive polynomial result alone
would not prove transfer for Xi either.

Use the ordinary convention D_(r,k)=det[a_(k+j-i)] for
0<=i,j<r, with a_n=0 for negative indices. The exact proposed model
has degree five and a_0,...,a_5 positive rational numbers. The target
properties are PF2, D_(r,3)>0 for every sufficiently large integer r,
and D_(r,4)<0 for infinitely many integer r. These are desired
properties, not conclusions or assumed available inputs. Degree five
bounds the later symbolic problem; a finite numerical sign sample
would not establish either infinite-rank property.

Start from the inspected sector theorem in the November5 verified-height
assessment and the fixed-duality/rational-pole sources assessed for
L834. Retrieve primary hypotheses and essential cases for any claimed
condensation transfer or dominance theorem. Check standard terminology
and stronger results. Inspect only specifically relevant failure records;
absence from the limited phrase search is no novelty evidence. L833's
canonical file already records its step666 audit, so a repeated audit
of that floor is not the continuation.

Continue to a separately approved bounded mathematical test only if
the source comparison leaves the exact model question justified.
Import a matching known counterexample or theorem with precise citation
instead of presenting it as a discovery. If a stronger theorem rules
out the proposed model under these exact hypotheses, record that and
its potential transfer conditions. If the generic implication is
already known to fail, use that negative information to require a
specific additional actual-Xi input before attempting propagation.
Do not weaken either infinite-rank sign condition to a finite sample.

Motivating local inputs are C832a's audited finite nonnegative band,
L834's audited eventual fixed-shift conclusion, and the L018/L021/L776
ordinary conventions as recorded in their proofs. No cross-notebook
input is proposed. Step659/667 and the L836 runtime/sign limitations
remain untouched. Full matching Mathlib coverage is unchecked.

This nomination does not approve its own changed scope or derive
previously uncovered mathematics. It prepares a source comparison,
not a creative proof attempt. A justified central creative continuation
still needs an actual-Xi estimate beyond these abstract sign inputs;
the proposed model test may clarify that missing hypothesis.
