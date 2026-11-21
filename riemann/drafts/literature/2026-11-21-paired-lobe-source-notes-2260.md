# Paired-lobe marginal source comparison2260

21 November2026. LITERATURE only. This completes the exact source
target nominated2259. No pairing identity, new curvature assertion,
perturbation estimate or lemma is proved here.

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. A nonnegative marginal representation could help
with the first-zero-removal shape bridge. Joint log-concavity is a
proposed sufficient input, not an established consequence of pairing.
Actual-Xi applicability, repeated strictness and all-degree transfer
remain separate gaps even if that input succeeds.

## Primary statements and relevant proof cases inspected

E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral.
Math. Soc.74(2006),133-138, printed pp133-135, equations(1)-(4):
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf .
Reopened the initial convergence/endpoint conventions and the complete
successive-half-period proof on p134. It compares positive and negative
sine lobes using decreasing amplitudes. It establishes sine positivity;
neither a first cosine zero nor joint logarithmic curvature occurs in
that proof. The proposed translation by u, interchange with the series,
and normalization by x still need justification. No generalization is
performed here. The DOI endpoint failed; the publisher PDF was accessible.
Its equation(4) parsed poorly; the screenshot call returned no inspectable
image. The prose comparison and inspected2257 coverage suffice for this
scope comparison; do not call the screenshot visual verification.

A. Prékopa, *On logarithmic concave measures and functions*, Acta
Sci.Math.(Szeged)34(1973),335-343, introduction p335 and Theorems6-8,
complete proofs of6-7, pp342-343:
https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf .
Theorem6 integrates a jointly log-concave nonnegative function over a
convex set in the eliminated variables. Its proof zero-extends the
sections and applies the integral inequality. Theorem7 treats convolution
through a jointly log-concave product. Theorem8 states the probability
marginal consequence. For H, eligibility would require joint curvature,
measurability, finite sections and a justified zero extension outside
the proposed convex strip. These requirements are unpaid. Nonnegative
summands alone do not meet them. The conclusion is nonstrict; iteration
and strict curvature require additional arguments. The proofs were read
as parsed primary text, with the earlier2254 qualifications retained.

S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge2004,
author-hosted seventh printing with corrections2009, Sections3.5.1-2,
printed pp104-106, especially the full differential criterion p105:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .
For a positive twice differentiable function on a convex domain,
log-concavity is equivalent to f Hess(f)-grad(f)grad(f)^T being
negative semidefinite everywhere. The displayed log-Hessian formula
is supplied there. The same page explicitly warns that sums of
log-concave functions need not be log-concave. This covers a later
directional-curvature test, without deciding the specialized H.
Read the multiplication/sum discussion and p106 marginal/convolution
statement; use Prékopa's primary proof for the marginal theorem.
No reproof or application-specific Hessian calculation is made here.

Reuse notes2249/2254/2257 for Conrad, *Differentiating under the
integral sign*, Theorem12.3 p16 (joint continuity and integrable
parameter-independent bounds for integrand and derivative), and Tao,
*245B, notes0*,1January2009, Theorem3(4)-(5),Theorem4(1)-(2):
https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf ;
https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/ .
Dominated convergence, the summable-L1 series case, nonnegative Tonelli
and absolutely integrable Fubini are available under their exact
hypotheses. Conrad refers out for his proof; Tao omits the general
proofs. These standard citations supply no specialized domination,
root stability or curvature estimate. For a derivative series the
later proof must supply local uniform summable derivative bounds;
mere convergence of the undifferentiated series is insufficient.

## Local duplicates, failures, searches and limitations

Targeted searches of21November source notes/attempts,20November
source notes/attempts and the relevant2259 history located the nomination
and the earlier direct signed-integrand warning. No ready proof of this
specific density was found in those ranges. This is a bounded duplicate
check, not an exhaustive novelty claim. Read2257,2254,2249's integration
coverage,2259 history, L049/L050 and C919s's statement and first-zero
proof range. L049/L050 concern nonreal zeros of mixtures, not joint
log-concavity of this paired density. C919s gives a conditional certified
simple least cosine zero of the unperturbed quartic, and a negative
curvature determinant of its marginal at1. Neither settles H. Its
software contracts remain assumptions if its root result is reused.
The actual-kernel enclosure stops and completed fixed quartic test stay
closed; this nomination does not request another numerical point test
of that marginal. No cross-notebook result is used.

Actual queries included:

- `"Tuck" "log concavity" sine transform`;
  `log concavity alternating sum decreasing function paired sine transform`.
- `"log concavity" "f(x)-f(x+a)"`;
  `"log-concave" "alternating sum"`;
  `"log concavity" "difference" "translates" function`;
  `"Tuck" "paired" "log-concavity"`.
- `"log concavity" "alternating translates" kernel`;
  `"log-concavity" "sine transform" "decreasing"`.
- `"log cosh" "Fourier" "first zero" concavity`;
  `"log concavity" "alternating" "quartic"`;
  `"log-concave" "difference of translates"`.

No exact joint-density theorem, stronger applicable preservation result
or matching counterexample was identified in the primary sources read.
Discrete convolution and matroid alternating-coefficient results have
different objects; search snippets were not imported. Optional Koumandos
and Wintner/Spira originals remain unread and nonessential to the bounded
test below. An exploratory Rouché query found only leads; no Rouché
statement is imported or needed by this nomination. One mistyped Tao
URL failed; the correct existing citation above is reused. No essential
source blocker persists. Search misses do not establish originality.

## One concrete future test, entirely unproved

Retain the nomination2259 hypotheses on K, its least positive cosine
zero x of arbitrary multiplicity, a=pi/x, and the exact density

    H(u,v)=sin(xv) sum_{j>=0}
       [K(u+v+2ja)-K(u+v+(2j+1)a)], u>=0, 0<v<a.

The proposed new mechanism is to test local curvature of the density
itself under a small convex-potential perturbation, rather than repeat
the old marginal calculation. Motivation only: distinguish global
transform constraints from second derivatives of individual paired
terms. No separation estimate or sign is established in this review.

Fix the following family and point before any mathematical attempt:

    V_{rho,a}(t)=t^4+t^2+rho^(3/2)[
       log cosh((t-3a/2)/rho)+log cosh((t+3a/2)/rho)],
    K_{rho,a}(t)=exp(-V_{rho,a}(t)),
    0<rho<1, 2/3<=a<=7/10, u=v=a/4.

The only proposed test is whether, for sufficiently small positive rho,
one can choose a in that fixed interval so that pi/a is the LEAST
positive real cosine zero of K_{rho,a}, and then establish

    H H_uu-H_u^2 > 0 at (a/4,a/4).

Every assertion in this paragraph is a target, not a result: admissibility
including all derivative tails, the first-zero alignment/exclusion of
earlier zeros, positive C2 density, all derivative-series bounds and
the strict determinant sign remain unpaid. The parameter a may enforce
only the zero constraint, not optimize the sign. The exponent3/2,
location3a/2 and point(a/4,a/4) are fixed; no scan, numerical retuning,
or alternate family is authorized. The test is an analytic rho-down-to0
attempt, not a claimed effective numerical certificate.

C919s may supply the base quartic simple first zero, conditional on its
explicit software contracts. Stability under this root-linked family
must still be proved, with uniform estimates over the fixed a interval
and a real-variable intermediate-value/monotonicity argument; do not
presume a differentiable branch at rho=0. Elementary calculus and the
covered dominated-convergence tools suffice in principle, but their
application is the research problem. No perturbation theorem has been
silently imported. No claim about other complex zeros is needed.

A strictly positive determinant at an eligible interior point rejects
generic joint log-concavity for this representation under the original
hypotheses. It does not refute log-concavity of the marginal, first-zero
preservation itself, or RH. A nonpositive value tests only that family
and point. Failed root alignment, missing series bounds or an unresolved
sign stops this bounded attempt without enlargement. Positivity and the
marginal identity remain necessary for a positive marginal route; an
obstruction test need not prove that whole route first.

EXPLORE coverage is prepared only for this specified test. The original
source target is complete; no generic result has been derived or
approved in this literature turn. Newly prepared continuation coverage
requires the supervisor's separate approval next turn. Full matching
Mathlib coverage is unchecked, not asserted absent. No lemmas, scripts,
DAG, PROOF or shared infrastructure are changed.
