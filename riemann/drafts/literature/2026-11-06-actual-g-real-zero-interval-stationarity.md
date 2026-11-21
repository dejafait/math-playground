# Real-zero interval stationary-point test — source assessment

TARGET: Test whether for every r>=2 and k=r-1 the actual-G angular density has a nonzero stationary point with z_j=-4t_j^2 and t_j in r pairwise separated intervals between consecutive positive real zeros of Xi.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact actual-G/Xi/Vandermonde/stationarity and Stieltjes–Fekete searches and notebook-local duplicate/failure checks; no inspected theorem states this exact density's all-r assertion. Reused the sector and joint-contour assessments; new primary and author-textbook passages are identified below. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Conrey, J. reine angew. Math. 399 (1989), Theorem 1, p.4, with positive-ordinate simple-zero definition (11), p.3; Lebl Basic Analysis I v6.3, Theorem 7.5.6 and Lemma 4.2.2 with proofs; Basic Analysis II v6.3, Theorem 8.3.7 and Exercise 8.3.9; Lebl Guide to Cultivating Complex Analysis v1.10, Proposition 2.1.4 and Theorem 2.4.7. L844 (1)–(4) supplies the unchanged density convention. Exact inspected ranges and qualifications follow.
COMPARISON: Known unconditional real-zero results and standard extremum/differentiation theorems cover the general inputs. The remaining work is an actual-density specialization checking separated consecutive-zero boxes, endpoint vanishing, a nonzero interior value, real or constant phase, and all complex partials. Rational-field electrostatics is unnecessary and is not imported; no stationary family is established in this review.
GAP: Apply the cited inputs to this exact H_r for every r>=2, with k=r-1 and the L775 radius, retaining its denominator powers and normalization. All boundary, nonvanishing, phase and coordinate-transfer checks remain proof obligations; no Hessian or contour conclusion is covered.
REASON: Essential source coverage is now adequate for a bounded specialization attempt, subject to the separate next-turn approval of this changed assessment. This is established theorem application, not a proposed new general extremum theorem or a novelty claim; contour participation, summed phases, signed remainders and Xi mixed signs remain independent gaps.
SCOPE: Covers exactly TARGET and its necessary finite-dimensional applicability checks using the specified actual G and H_r. This completed turn is literature-only; a later approved research turn may specialize the sources, but may not assume a stationary family, simple endpoints, nondegeneracy, a uniform height/spacing bound or an integration-measure change.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential unconditional distinct-real-zero and real-to-complex variational coverage. This review fills that named source gap; no further browsing on the unchanged target is nominated.

## Completed source review — 6 November 2026

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is exactly TARGET. Its plausible
use is an alternative stationary geometry for a later contour study;
existence alone would not determine a contribution or a minor sign.
This assessment authorizes only a later specialization attempt, after
separate approval. It contains no construction of a stationary point.

### Unconditional real zeros: inspected primary theorem

J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
function are on the critical line*, J. reine angew. Math. **399**
(1989), 1–26, [Theorem 1, printed p.4](https://www.maths.dur.ac.uk/users/herbert.gangl/morethan2_5.PDF#page=4).
Read the introduction, Section 2's counting conventions, (11) on p.3,
and the complete theorem on p.4. The theorem unconditionally gives a
proportion at least two fifths of zeros that are both simple and on
the critical line; the relevant count has positive ordinate. It is
stronger than the needed infinitely many distinct positive-ordinate
critical-line zeros. L018 supplies the nonvanishing completion factors
and multiplicity-preserving Xi correspondence for its local use.
No claim that all zeros are simple or real is imported. The
mollifier proof is not rederived or audited here. Hardy's original
1914 theorem was a search lead, not an inspected primary input; it is
not needed in addition to Conrey's stronger theorem.

The first AIM-hosted PDF link returned 404; the complete Durham scan
was accessible. OCR omits some displayed counting formulas. The
explicit definition of the simple positive-ordinate count and the
complete verbal conclusion of Theorem 1 are legible and suffice for
the input above; no numerical constant or unread formula is used to
certify a configuration. No essential source blocker remains.

### Standard variational and analytic inputs: exact scope

Jiří Lebl, *Basic Analysis I*, version 6.3, 15 May 2026:

- [Theorem 7.5.6, printed p.290](https://www.jirka.org/ra/realanal.pdf#page=290):
  a continuous real-valued function on a nonempty compact metric space
  attains a maximum and a minimum. Read the entire statement and proof.
- [Lemma 4.2.2, pp.162–163](https://www.jirka.org/ra/realanal.pdf#page=162):
  a real-valued function differentiable at an interior relative
  extremum of an interval has derivative zero. Read both extremum
  cases and the complete proof. This is the standard Fermat input.

Lebl, *Basic Analysis II*, version 6.3, 15 May 2026:
[Theorem 8.3.7, p.38](https://www.jirka.org/ra/realanal2.pdf#page=38)
states the finite-dimensional chain rule on open sets with the stated
domain inclusion and pointwise differentiability hypotheses. Read its
statement and proof setup, including the zero-increment case; no new
chain-rule theorem is required. [Exercise 8.3.9, p.45](https://www.jirka.org/ra/realanal2.pdf#page=45)
records the multivariable interior-extremum statement as an exercise,
not a proved theorem in that passage. Use the proved one-variable
Fermat lemma in coordinate directions rather than treating the
exercise as a separate source proof.

Lebl, *Guide to Cultivating Complex Analysis*, version 1.10,
5 November 2026:
[Proposition 2.1.4, p.28](https://www.jirka.org/ca/ca.pdf#page=28)
gives equivalence of complex differentiability with real
differentiability plus Cauchy–Riemann, and explicitly identifies the
complex derivative with the derivative in the real-coordinate
direction. Read the complete proposition and its preceding
real-linear explanation. [Theorem 2.4.7, p.49](https://www.jirka.org/ca/ca.pdf#page=49)
states the identity/isolated-zero theorem for an analytic function on
a domain unless it is identically zero. Its complete statement was
inspected; its proof was not audited. These are standard inputs, not
the target's real-to-complex application already performed. The failed
HTML links were replaced by the accessible author PDF.

These results do not by themselves assert the desired actual-G
configuration. A real restriction's modulus extremum cannot simply
be called holomorphic stationarity. The later proof must check its
real or constant-phase property, nonzero extremum and every
coordinate's derivative transfer for the original H_r. The maximum
is sought on a real product box; the holomorphic maximum principle
on an open complex domain is not the relevant theorem. No reproof
of any general theorem is justified or requested.

### Exact specialization obligations reserved for research

Use L018's entire real-even Xi, L775's positive finite scalar radius,
and L844's exact density, equations (1)–(4), read in full for this
comparison. In particular (4) has powers k+r-1 in its denominators;
no Jacobian is to be inserted into that function. No sector estimate
or asymptotic onset is required as an input to this finite-r target.

The future attempt must justify ordering distinct real zeros and
choosing r compact consecutive-zero intervals with positive pairwise
separation, allowing arbitrary multiplicities. It must verify
continuity up to every box face, no denominator singularity, an
interior nonzero value and boundary behavior sufficient to locate a
nonzero interior extremum. It must then establish the real/phase and
analytic coordinate hypotheses needed to obtain vanishing of all r
complex partial derivatives of the original density. These are
unperformed applicability checks, not conclusions of this review.
Do not infer simplicity of consecutive endpoints from Conrey's
existence of a simple subset, or use a real-zero product for all Xi
zeros. Off-line zeros remain allowed.

Continue if the exact all-r specialization satisfies those checks;
abandon this construction on a failure of boundary exclusion,
nonvanishing or complex stationarity. A successful result still gives
no uniqueness, Hessian nonsingularity, effective locations, uniform
spacing, accessible integration cycle, phase sum, signed error bound
or mixed-minor positivity. It would be a local application of known
results with classification REPRODUCTION, not a new general theorem.

### Search and recorded-failure comparison

Web queries included `Conrey 1989 more than two fifths zeros Riemann
zeta function critical line simple zeros pdf theorem`, `Hardy 1914
Sur les zeros de la fonction zeta de Riemann 1012 1014 pdf`,
`Stieltjes Fekete real intervals zeros analytic weight critical points
compact maximum holomorphic`, `"Riemann xi" "stationary"
"Vandermonde"`, `"actual-G" "stationary" Xi`, `"Riemann"
"Fekete points" zeros`, and `"Xi" "between consecutive zeros"
"electrostatic"`. No exact matching all-r theorem was inspected.
Search hits and snippets are not theorem evidence. The 2026
simple-zero proportion preprint returned by search was not inspected
or needed; no current-record claim is made.

Reused the existing sector and joint-angular-contour assessments for
the rational-field comparison. Rechecked Bertola–Chavez-Heredia–Grava,
[2206.06861v4, Section 1 (1.1)–(1.4)](https://arxiv.org/html/2206.06861v4#S1),
19 August 2023: its weighted-Fekete formulation supplies terminology,
while its orthogonality correspondence restricts the field derivative
to a rational function. That correspondence is not an existence
theorem for this prescribed density/box. No polynomial truncation,
semiclassical identification or uninspected Section 3 converse is used.

Notebook-scoped searches for real-zero interval stationarity,
consecutive-zero extrema and Stieltjes/Fekete terms found no exact
duplicate among the relevant claims. Read the L844 collar-stop
record and the earlier actual-Jacobi collision-factor assessment's
Stopple comparison: that global comparison assumes RH and consecutive
simple zeros and serves a different collision/Newman target. It is
not an input here. L775's absolute-complement stop, the automatic
contour source stop and L844's fixed-collar exclusion remain intact.
No cross-notebook input is used. Full matching and supporting Mathlib
coverage were not checked; unknown availability is not absence.

## Original nomination retained

## Proposed object and relevance

Keep exactly the H_r, G, k=r-1 and scalar R_k of L844. The proposed
coordinates are z_j=-4t_j^2 with t_j>0; for example the corresponding
angular coordinate is zeta_j=pi-i log(4t_j^2/R_k). This specifies where
to test the same function, not a changed integration measure. All r
complex partials must vanish and H_r must be nonzero. A saddle of a
modulus restricted to a real domain is not sufficient without a
justified implication for these complex partials.

For each r the proposed test allows choosing r closed intervals between
consecutive distinct positive real zeros of Xi, separated from one
another by a positive distance; each t_j must lie in its interval's
interior. No simplicity assumption, numerical indexing, predetermined
height, Hessian nonsingularity, bound on imaginary angular coordinates
or uniform asymptotic estimate is proposed. Availability of arbitrarily
many such real zeros must come from a precise unconditional theorem,
not RH or the finite verified-height result.

The source review should determine whether a standard compact
variational argument genuinely covers this actual analytic function
with its zeros, interaction factor and denominators. This is a proposed
mechanism and not an established application. It is different from
widening L844's asymptotic sector or repeating a collar search: the
prospective input is exact real-zero boundary geometry. No mathematical
consequence of that geometry is asserted in this nomination.

Continue only if known results or a separately approved specialization
can establish the quantified nonzero stationary family with all stated
hypotheses. Abandon this construction if the boundary, nonvanishing or
real-to-complex stationarity requirement fails; an inaccessible essential
source does not authorize dependent mathematics. A successful result
would supply a concrete alternative stationary geometry for a later
contour investigation, not a sign of its contribution or an RH argument.

Essential continuation inputs: L018/L775/L844 and a precisely sourced
unconditional real-zero theorem. The old L775 absolute-complement stop,
automatic-contour source stop and L844 collar exclusion remain intact.
No mathematical script, new lemma or cross-notebook input is proposed
in this review. Full matching Mathlib coverage remains unchecked.
