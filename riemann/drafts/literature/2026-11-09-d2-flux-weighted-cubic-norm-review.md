# Direct d=2 flux via a weighted cubic norm — completed source review

TARGET: Assess whether a shifted raw-moment Schur complement and a full-theta weighted cubic-square remainder can give a bounded direct test of L874's S7 flux threshold at full-degree d=2 contacts on 0<lambda<=1/20, distinct from the stopped origin and determinant-box tests.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step220 searched exact theta/Schur/contact-flux phrases and stronger orthogonal-polynomial/extremal-moment terminology; checked L043/L874/L917/L921, steps193/199/217, and reused steps539/546 Gaussian and L874's prior contact-source comparisons. Queries and read limits below; no novelty conclusion.
SOURCE_EVIDENCE: Inspected Gautschi OUP2004 Theorem1.24 pp8-9 with proof and Section1.2 hypotheses; Boyd-Vandenberghe CUP2004 corrected2009 AppendixA.5.5 pp650-651; Gallier author version2019-08-24 Proposition2.2 p4 and Proposition4.2/Theorem4.3 pp9-12 with relevant proof cases; Laurent updated2010-02-06 Lemma4.2 pp54-55 and proofs; DLMF18.3 Table18.3.1 Legendre rows. Direct links and scope below; reuse existing Gaussian exactness coverage.
COMPARISON: The shifted raw Gram/norm machinery is known and supplies no logarithmic contact sign. A fixed-interval actual-density minorization followed by the monic Legendre minimum gives a concrete candidate quantitative test beyond generic nonnegativity; its size and contact-deficit comparison remain unproved. Inspected newer theta claims cover low-order/undeformed statements or assume RH for the low-time matrix hierarchy.
GAP: Derive the exact weighted-cubic/flux comparison with every null row retained, obtain one fixed-interval full-theta norm floor, and decide whether that floor pays the resulting deficit. None of these theta-specific mathematical steps was performed. General source tools alone do not pay S7.
REASON: Essential source coverage is now sufficient to nominate one bounded direct-flux test, distinct from J and determinant boxes. This is literature exploration, not a new sign theorem or an actual-theta obstruction. A separate newly saved assessment specifies the mathematical continuation and requires next-turn gate approval.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned a changed target from the analytic audit to a direct quantitative S7 bound; essential norm/Schur source coverage was missing. This review supplies the standard tools, while the theta-specific comparison remains mathematical work.
SCOPE: Completed step220 was literature-only. It derived no square completion or theta bound and changed no lemma, mathematical script, PROOF or DAG. The original nomination below is historical; the separate fixed-interval test is specified in 2026-11-09-d2-flux-weighted-cubic-test.md, not executed here.

## Completed comparison — step220, 9 November 2026

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate aim is L874's full-degree d=2 boundary flux, potentially
one input to decreasing-time continuation. Contact existence,
initialization, equality/tangency, other degrees and global continuation
remain independent gaps. No actual contact or flux sign was obtained.

### Primary statements, proof cases and applicability

Walter Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP (2004), [Section1.2 and Theorem1.24, printed pp.8-9](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
The section assumes a positive measure with infinitely many support
points and finite moments of every order. The theorem identifies the
unique minimum squared norm among monic degree-n polynomials as that
of its monic orthogonal polynomial. Equality requires that polynomial.
The complete proof expands in the monic orthogonal basis; positive
lower-degree norms settle equality. The following coefficient
minimization discussion, (1.2.10), was also read. This is a standard
extremal theorem, with no quantitative theta constant.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, CUP (2004),
inspected author PDF, seventh printing with corrections (2009),
[AppendixA.5.5, pp.650-651](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf):
for a real symmetric block matrix [[A,B],[B^T,C]] with A positive
definite, minimization in the first variable gives the quadratic form
with matrix C-B^T A^(-1)B. PSD is equivalent to nonnegative Schur
complement. The singular case additionally requires A PSD and
(I-AA^dagger)B=0, using C-B^T A^dagger B. Omitting this range condition
is invalid. Both minimization cases and the unbounded alternatives
were read; determinant/inverse formulas are not needed here.

Jean Gallier, [*The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
author version dated24August2019, Proposition2.2 p.4,
Proposition4.2/Theorem4.3 pp.9-12, independently supplies these block
conditions. Read the congruence proof and the singular quadratic
minimization proof: the null-space linear term is unbounded unless
the range condition holds; minimization on the positive spectral
subspace handles the remaining case. Thus a finite PSD relaxation
cannot silently use an inverse. This supporting source is not a
new moment theorem.

Reuse Laurent's [updated6February2010 manuscript](https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf),
Lemma4.2(i)-(iii), printed pp.54-55. The relevant statements and full
proof cases were retrieved: a representing positive measure yields
moment PSD, and support where g>=0 yields localizing PSD at order
t-ceil(deg(g)/2). A null polynomial vanishes on its support.
These are necessary conditions, not a representation theorem for the
logarithmic matrix. Rank/equality cannot be transferred from H2 to
an ordinary raw-moment matrix.

For applicability only, the actual measure is the pushforward of
L874's normalized law under x=u^2, weighted by x. L019/L058 give
positive density on every positive interval and every finite moment.
Thus the infinite-support norm hypotheses match; no assumption on a
minor of the logarithmic H2 is substituted for them. At a hypothetical
actual contact, c0 or c1 may vanish and c2 may be arbitrarily small.
Only c2!=0 is retained. The future proof must justify any raw-block
division using the actual measure, or retain the cited singular case
in a relaxation. No weighted square-completion identity was derived.

[DLMF18.3 Table18.3.1](https://dlmf.nist.gov/18.3#T1), Legendre and
shifted-Legendre rows, gives weight1 on (-1,1) and (0,1), respectively,
with their squared norms and leading coefficients. These supply an
explicit reference minimum on a fixed finite interval after an affine
change of variable and monic normalization. Neither that specialization
nor a theta density constant was evaluated this turn.

Reuse steps539/546 in `2026-11-05-theta-gauss-compressed-interlacing-scope.md`
and `2026-11-05-theta-first-post-exact-gauss-defect.md`: Gaussian
existence, positive weights and degree2n-1 exactness, and the polynomial
Hermite-remainder cases already have inspected primary coverage.
There is no need to reprove them or use a finite-interval mean-value
remainder on an infinite support. Quadrature is optional bookkeeping,
not the missing quantitative input. Full matching Mathlib coverage of
the proposed contact mechanism is unchecked; none is asserted absent.

### Stronger results and failure comparison

The new primary lead U Jin Choi, [arXiv:2611.04359v1](https://arxiv.org/html/2611.04359v1),
3November2026, was read in Section2 (5)-(10), Theorem4.1 with its
complete proof, and Proposition5.1 with its proof and certificate
qualifications. Its kernel is L019's kernel divided by4; normalization
cancels that factor, with quadratic parameter a=lambda. Its matrix
hierarchy for low nonnegative a assumes RH; the unconditional
real-zero range starts at a>=0.05. Its unconditional undeformed
cumulant signs and sixth-order gap are not the d=2 S7 contact flux.
Neither its numerical pilot nor its conditional Stieltjes Gram proof
is an independent low-time sign input. No source certificate was
replayed and no new theorem from that manuscript was imported.

Reuse `2026-11-06-reciprocal-hankel-heat-contact.md` for the inspected
Deng-Yang-Lu contour-Hankel theorem: it moves coordinates of fixed
zeros, rather than theta heat time. Its renewed search hit does not
justify rereading it. Reuse the d2-contact-flux-discovery comparison
for the already inspected endpoint cutoff and invariance limitations.

L043 duplicates the ordinary Gram positivity, not the needed flux.
L874's scalar9-versus15 calculation already shows why strict ordinary
positivity supplies no sufficient size. L921 refutes the nominated
finite implication for J, not for S7. Steps193/199/217 stop absolute
mass payment, one density-dual class and one origin interval test.
The present candidate uses a positive norm with an independently
fixed density floor; it neither refines those boxes nor signs their
residual. The theta/Favard/Schur comparison in step567 concerns a
different factorial-normalized minor and is not a flux identity.

Searches: `orthogonal monic polynomial minimum norm Hankel determinant
Schur complement moment matrix theorem`; `Gaussian quadrature
remainder monic orthogonal polynomial squared norm Gautschi theorem`;
`Riemann xi theta kernel heat flow Hankel cumulant contact positivity
moment inequality`; `"Riemann" "Hankel" "cumulants" heat flow`;
`"theta" "monic" "cubic" "norm" Riemann`; `"Riemann" "heat"
"Hankel" "boundary" positivity cumulants`; `"theta kernel" "Schur
complement" moments`; `"Riemann" "cubic" "moment" "flux"`.
Irrelevant numerical-PDE flux hits are not evidence. A Thorin-measure
SSRN hit and universal cumulant-lifting index are uninspected leads,
not imported statements or essential premises. No inspected source
states the proposed theta-conditioned quantitative comparison; the
bounded search does not establish novelty. Direct shell downloads
failed DNS; web primary theorem text was accessible, so there is no
essential source blocker and no local PDF was obtained.

### One bounded continuation

Nominate a single fixed interval x in [1/16,1/4] (u in [1/4,1/2]).
Use only L019's positive first summand as a lower-bound candidate
for the full density, with an independently bounded full normalizing
mass, then the cited monic Legendre extremum. Compare the resulting
floor with the exact norm deficit obtained from L874 and all three
null rows. This is a proposed test, not a proved formula, floor or
margin. In particular, a lower bound for one arbitrarily chosen
cubic does not lower-bound the minimum; the reference bound must
hold for every monic cubic.

Continue only if that fixed certificate pays the entire required
deficit for the stated contacts. Otherwise preserve the first unpaid
estimate or a rigorous obstruction to this sufficient certificate;
do not tune the interval, add panels or sweep coefficients. A failed
comparison alone is inconclusive, not a negative actual flux. This
selects an independently measurable actual-theta input rather than
renaming S7>=B/A. The new contact-to-norm domination claim, rather
than the imported Schur or extremal theorem, is the potential creative
work. Separate next-turn approval of the new continuation is required.

## Original nomination — step219, preserved

The following nomination predates this completed review. Its pending
source language is superseded by the source evidence above; its
mathematical gaps remain unpaid.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate aim is an independently paid finite-contact
flux bound in L874. If it succeeds, it could contribute one boundary
direction for decreasing heat time. Actual contacts, initialization,
equality/tangency, other degrees, uniform/global continuation and the
RH endpoint would still require separate arguments.

Retain the exact L019/L058/L874 density, 0<lambda<=1/20, real unit c,
c2!=0, H2 PSD and all three rows H2*c=0. No contact is asserted to
exist; c0/c1 may vanish and |c2| has no uniform positive lower bound.
The proposed new datum is the squared norm of a monic cubic in x=u^2
under the positive measure x dmu_lambda. Its relation to a shifted
raw-moment Schur complement and to L874's S7 threshold must first be
covered by sources and then checked in an authorized mathematical turn.
No representing measure for the logarithmic H2 is assumed.

The review should retrieve precise primary statements for the finite
moment/localizing and extremal-norm or quadrature connection, including
invertibility, degenerate cases, support, finiteness and equality
conditions. Reuse inspected Laurent coverage where it actually applies;
do not redo a general moment theorem or infer a new flux inequality
from positive ordinary moments. Search the exact contact/sign statement,
stronger conclusions and known obstructions before approving a test.
Full/supporting Mathlib coverage for this proposed mechanism is unknown.

A useful later discriminator would compare the norm lower bound required
by the exact S7 flux threshold with an independently certified full-theta
lower bound, retaining all contact rows before estimates. The review
must identify one finite test and its decisive margin or obstruction,
not just restate S7>=B/A. If only generic nonnegativity is available and
it leaves the required quantitative deficit unpaid, record that limit;
do not manufacture a creative target or repeat scalar Cauchy-Schwarz.
No parameter sweep or numerical contact search is proposed.

L874's scalar 9-versus-15 deficit warns that a raw-moment lower bound
can be too weak. L921 obstructs a different finite-moment implication
for J, and supplies no actual-theta counterexample or direct flux
obstruction. L918's audited tails supply no compact sign. Step193's
rowwise absolute-payment loss and steps199/209/213/217 retain their
original scopes. Read only the precise additional records needed for
this new comparison. No box refinement, class enlargement or reopening
of the same stopped residual search is authorized by this nomination.

The connected-partition assessment and its step19 source stop were
also checked while choosing a continuation. They supply signed
identities without an actual-theta positive pairing, so merely expanding
another determinant is not selected. The present proposal instead asks
whether a positive weighted norm can quantitatively control the exact
missing coefficient. This is a motivation for review, not an approved
mathematical reduction or a claim of originality.

No protected creative mathematical task is ready yet: the missing
quantitative theta-to-threshold comparison is the blocker. If source
review identifies a genuinely new actual-theta norm mechanism with a
bounded discriminating test, nominate proof_attempt/creative and name
that precise deficit in NEXT_ESCALATION. If sources already cover it,
import or specialize them with the appropriate noncreative routing.
Do not derive and approve it in the literature turn. No cross-notebook
input, new lemma or mathematical program is part of step219.
