# Actual-Xi scalar feasibility: source review1308

TARGET: Decide C030z's actual-Xi scalar feasibility for all real x<1 by certified one-variable sign analysis, retaining L=0 and the free-p L=N=0 branch.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reviewed C030z's full scalar equivalence and calculation1307, reused assessments1303/1305, and searched exact real-sign determination, parametric quantifier elimination, interval-coefficient root isolation and prescribed Grunsky compatibility. Inspected primary statements and relevant degeneracy/proof cases below; no inspected source decides the actual-Xi instance and no novelty inference is made.
SOURCE_EVIDENCE: Basu-Pollack-Roy, Algorithms in Real Algebraic Geometry, 2nd ed.(2006), Theorems2.33,2.50,2.58,2.61,2.76-2.77, Proposition2.65 and Algorithm11.16; Basu arXiv1409.1534v1 Sections1.2,2.1; Sagraloff-Mehlhorn arXiv1308.4088v2 Theorem3, Sections2.1-2.2/Theorem5; Obradovic-Tuneski(2025) pp23-26, definitions and(1.4)-(1.7). Direct links and inspected cases below. Reuse1303's Teo comparison and1305's actual-sum arithmetic coverage.
COMPARISON: Classical real-algebraic methods cover exact polynomial signs with zero and unbounded branches. The actual constants have rational enclosing boxes, not a supplied exact comparison oracle; rational parameter guards or uniform interval certificates can support a conclusion, whereas midpoint root isolation and generic square-free/oracle guarantees cannot. The instance-specific elimination and strict certificate remain unperformed.
GAP: Obtain a strict finite witness or an exhaustive, branch-complete obstruction from the fixed actual boxes; if equality, common-root, interval or unbounded-tail cases remain unresolved, report them and stop the fixed method. No source establishes analytic realization, univalence or all-degree positivity.
REASON: New primary coverage closes the method-level gate left open by nomination1307. Only a later bounded specialization is supported; this literature turn derives no instance polynomial, discriminant, sign or feasibility result. This newly ready continuation needs separate approval next turn.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target expressly exceeds1305's four-point scope. This review supplies the missing exhaustive-sign-method comparison, reusing unchanged actual-sum and formal Grunsky assessments.
SCOPE: Exactly C030z(2)-(3), actual A=S2,...,E=S6 in calculation1307's fixed rational outer boxes, x<1 and every strict p,V,J,H>0 condition; all three L,N branches. One finite symbolic reduction and one fixed-box certificate pass, at most256 rational subdivision cells with depth at most16. No new quadrature, precision refinement, sample sweep, higher jet degree, analytic realization or library installation.

## Relevance and saved inputs

The main gap remains L030-L032/C032a actual-Xi Q(q)>=0 in every
degree, with initialization, singular blocks, identification and
realization unpaid. The intermediate target is only C030z's finite
positive-diagonal prescription. A strict compatible jet could motivate
a separately assessed realization problem. An exhaustive exclusion
would stop that prescription, without deciding RH.

C030z's complete proof, including necessity, sufficiency and all L,N
cases, was read. Its actual singleton calculation1307 supplies strict
outer rational boxes and four exclusions. Use those canonical bounds;
do not substitute raw theta moments or rounded midpoint values for S_k.
The complete calculation and Fraction-replay certificates remain at
`scripts/grunsky/actual-singleton-certificate-1307.json` and
`scripts/grunsky/actual-singleton-replay-1307.json`. This source review
does not rerun or independently audit them. Reuse1305's source assessment
and retain L037's conditional Decimal arithmetic contracts and L917's
complete degree-twelve tails. L019/L021/L025 identify actual Xi data;
L027's finite strict signs supply no all-degree Hankel premise.

The targeted local search covered existing Grunsky assessments and
attempt records for Sturm, Tarski, quantifier elimination and all-branch
analysis. Read assessment1303, assessment1305, the relevant actual-input
review1305, and failure/history1307. No previous all-branch certificate
was located in that scoped search. Preserve C030y's fixed-weight stop,
the uniform-H2 stop and stops1297/1302/1200 as scoped evidence. Four
excluded x do not exhaust the prescription. Historical route stops
are not a ban on this different finite test.

## Primary methods inspected

**Basu, Pollack and Roy**, *Algorithms in Real Algebraic Geometry*,
second edition, Springer, 2006, DOI10.1007/3-540-33099-2.
The author's posted download timed out; the
[university-hosted second-edition PDF](https://www.cs.umd.edu/~gasarch/COURSES/752/S25/slides/AlgorithmsInRealAlgGeom.pdf)
was inspected instead. Theorem2.33, p43: Descartes counts positive roots
with multiplicity. Theorems2.50/2.58/2.61, pp51,54-56: signed remainders
count roots/Tarski queries for nonzero P, using endpoints off P's roots,
including infinities. Read the gcd cancellation, zero-remainder and
endpoint cases in the proof. Proposition2.65, p63, retains common roots.
Theorems2.76-2.77, pp67-69, give projection/quantifier elimination for
polynomial formulas over an ordered subring of a real closed field;
their proof separates identically zero specializations. Algorithm11.16,
p425, supplies an exact cylindrical elimination procedure. These are
imports, not claims of a practical runtime or an actual-Xi sign oracle.

**S. Basu**, *Algorithms in Real Algebraic Geometry: A Survey*,
[arXiv1409.1534v1](https://arxiv.org/html/1409.1534v1),
Sections1.2 and2.1, Definition1.1 and Theorems2.1/2.4.
Read the ordered-domain computation model, first-order sign predicates
and exact equivalence; comparisons count as operations. This makes
clear why arithmetic in a ring generated by unknown real constants
is not automatically an effective implementation using fixed boxes.
No complexity claim for a new implementation is imported.

**M. Sagraloff and K. Mehlhorn**, *Computing Real Roots of Real
Polynomials*, [arXiv1308.4088v2](https://arxiv.org/html/1308.4088v2),
11 March2015, Theorem3, Section2.1 and Section2.2/Theorem5 with its
proof. The root-isolation theorem assumes square-freeness, a normalized
nonzero leading coefficient and an arbitrarily accurate coefficient
oracle. Theorem5(b)'s sign/magnitude search assumes a nonzero evaluation.
Only the fixed calculation1307 boxes are approved here; arbitrary
precision access and square-freeness of eliminated polynomials have
not been established. Thus this theorem is a qualified alternative,
not a termination guarantee for the proposed actual-constant test.

**M. Obradovic and N. Tuneski**, *Some application of Grunsky
coefficients in the theory of univalent functions*, Ann. Univ.
Paedagog. Crac. Stud. Math.25(2025),23-30,
[DOI10.2478/aupcsm-2025-0005, primary PDF](https://studmath.uken.krakow.pl/article/download/12363/10958/47182).
Inspected pp23-26, definitions and(1.4)-(1.7). The analytic class assumes
disk univalence before using the Grunsky inequalities. Its bounds and
odd-transform convention do not decide C030z's general real formal jet
or supply the missing univalence. No proof or numerical optimum from
that paper is imported. Reuse1303's already inspected Teo formal
identities and Takhtajan-Teo analytic-hypothesis comparison.

## Exact applicability and permitted later test

Take the real field, with rational numbers as the coefficient domain
for the bounding computation. Treat A,...,E as shared parameters in
their canonical rational boxes, preserving repeated occurrences and
their strict positivity. C030z's displayed functions are rational
expressions with positive A,C,D,E denominators. A later calculation
must record exact cleared identities and denominator signs. No such
instance-specific algebra is derived in this review. General theorem
reproof is unnecessary; the new work is its finite specialization.

The parameter-box interpretation matters. Excluding feasible x,p for
every tuple in an outer box excludes them for the actual tuple. A
witness for some arbitrary tuple in the box does not prove actual
feasibility. A witness must use the actual constants with certified
strict inequalities, or an appropriate uniform certificate for every
tuple in the box. If different tuples give different feasibility
answers, the boxes alone need not decide the actual tuple. Parameter
quantifier elimination explains the available stronger test; it does
not promise that the actual point is separated from an equality locus.

For the intended one-variable pass, preserve C030z's complete split:
use p=N/L only after L!=0; reject L=0,N!=0 by the existing equivalence;
retain free p and all strict inequalities when L=N=0. Exact parametric
Sturm/Tarski sign determination covers the last type of question in
principle. An interval containing zero is neither exact equality nor
proof of nonzero. Repeated roots, vanishing leading coefficients and
identically zero polynomials require their own case or an explicit
unresolved outcome. Do not apply a generic square-free algorithm to
remove them. The open boundary x=1 is excluded by the hypothesis;
finite root boundaries below1 cannot be silently removed.

Allow one symbolic reduction of precisely this finite system, followed
by a single exact-rational/interval certificate pass. Use Descartes or
signed-remainder sign counts and, where useful, interval polynomial
evaluation on rational cells. Subdivision is limited to256 cells of
depth at most16. Both unbounded ends of any transformed domain must
have exact leading-term, Descartes or Sturm coverage; a finite cutoff
or root plot is insufficient. Any rational change of variable needs
its domain bijection, excluded endpoints and cleared-factor signs
verified in the later proof. No chosen change or derived polynomial
is approved as an already proved identity here.

Continue only with a strict actual witness or an exhaustive certificate
covering every branch and x<1. If the fixed boxes leave any common-root,
equality, strict-sign or tail case unresolved, save those exact cases
and stop the fixed method. Do not refine precision, launch a parameter
sweep or repeat1307's four samples within this target. Inconclusiveness
does not refute the representation. A certificate and its complete
identities, conditions, margins, coverage and failures must be saved
under scripts/grunsky/; print only a bounded summary and paths. This
is a future calculation specification, not a mathematical script
written or run in this literature turn.

## Search record, decision and limits

Queries included `Basu Pollack Roy Algorithms Real Algebraic Geometry
quantifier elimination real closed fields theorem 2.77 PDF`, `interval
polynomial coefficients robust feasibility real quantifier elimination
universal parameters Grunsky prescribed coefficients`, `polynomial
interval coefficients real root isolation exact sign determination
parameters Basu Roy`, and `"Grunsky coefficients" "prescribed"
compatibility finite`, with a separate Grunsky/Hankel query. Results
led to the inspected primary sources above. Search hits about planar
Neumann-Poincare inverse spectra and other coefficient bounds were
unread leads and are not mathematical inputs. Secondary book reviews,
search snippets and Sage documentation were discovery aids only.
No failed search establishes novelty or absence of a matching theorem.

DECISION SPECIALIZE covers the established exact-sign methods, with
the actual finite certificate still missing. A later successful result
is local progress on a finite prescription; reproduction of these
methods is not a new root-isolation theorem. Full matching Mathlib
coverage remains unchecked. No cross-notebook result is used.

No justified creative central signing mechanism follows from this
source review: realization and all-degree actual-Xi signs remain
unpaid. Keep ordinary calculation routing for this bounded test rather
than relabeling algebraic specialization as creative research. The
newly ready assessment is for separate supervisor approval next turn.
