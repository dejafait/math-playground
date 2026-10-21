# Fixed-class covering and rational modular scalar — completed source review

TARGET: Compare elliptic Chabauty's rank and good-reduction hypotheses with the five-isogeny covering of L062's fixed class and its rational-j condition.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked the exact-map local inputs and ATTEMPTS/029–030; searched Bruin elliptic Chabauty, number-field rank, rational-map reduction and isogeny-covering variants; followed Bruin's author publication link to the complete primary paper and inspected FNS's same-field rational-j discussion.
SOURCE_EVIDENCE: Bruin 2003 Sections 4.1–4.2 pp.40–45, especially Lemmas 4.1–4.2 with both proof cases; FNS June 10, 2019 Section 7.2 pp.25–27, especially its Mordell–Weil failure and conditional Table 5; official Magma handbook text/1568 elliptic-Chabauty input/output guarantees inspected on 2026-10-14.
COMPARISON: FNS already treats rational modular j over precisely this degree-twelve field and records insufficient independent points for ordinary Chabauty; Bruin's general rationality method fits arbitrary covers, but its explicit degree-two formulas do not fit the degree-twelve modular map or a degree-five pullback. Rank alone is no effective point bound.
GAP: Certified rank below twelve, sufficient Mordell–Weil generators/index control, reduction of the entire scalar map and coset-wise nondegeneracy/zero certificates remain absent; no new covering or point enumeration is proved.
REASON: Source overlap and precise hypotheses rule out immediate off-the-shelf point enumeration; retain the general method and propose one separate, bounded good-reduction prerequisite test at thirteen, rather than repeat local class removal or conditional Selmer computations.
LITERATURE_REASON: Essential primary coverage for this changed target is missing; the ready all-prime assembly assessment covers neither elliptic Chabauty nor covering/rational-j point determination.

The main gap is positive primitive integer emptiness in the 54a1 branch.
The intermediate source-review target is an exact theorem-applicability
decision for a global point method retaining the modular scalar, rather
than only its connecting class. Potential downstream use is a certified
finite candidate set of rational modular scalars, to which the common
primitive (3,4,11) power equations would still have to be applied. A
method for this one class alone would not exclude the entire branch;
exhaustion of other global classes and the other signatures remain gaps.

Essential local inputs are L033's theta:E1 -> E0 and normalized f,
L034's entire modular map, L062's fixed sigma and alpha_sigma, and
audited L065. Read only needed ranges of these canonical inputs; no
cross-notebook theorem is proposed. Preserve ATTEMPTS/029–030 and
the finite-generator and quotient stops. Their obstructions do not
decide this global point question.

## Primary method and exact qualifications

Nils Bruin, *Chabauty methods using elliptic curves*, J. reine angew.
Math. **562** (2003), 27–49, DOI
[10.1515/crll.2003.076](https://doi.org/10.1515/crll.2003.076).
The publisher page exposed bibliographic data but not the article.
The [complete author-hosted published copy](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf)
was reached through the author's publications page. Its Section 4.2,
pp.42–45, concerns an elliptic curve over L, a smaller number field F,
and a cover to P1 over L; the question is which L-points map to F-points.
The encouraging inequality is rank E(L)<[L:F], not a guarantee of a
finite effective answer. The selected primes must be unramified over
the smaller field, satisfy the formal-logarithm ramification bound,
give good curve reduction, and retain the cover after reduction.
One needs adequate global generators or the sufficient local
prime-to-residue-characteristic index condition on pp.44–45.

On each reduction coset the rationality equations are convergent power
series in the Mordell–Weil parameters. Lemma 4.1, pp.43–44, gives at
most one zero if either the affine linear reduction has full column
rank, or all constants and first derivatives vanish and the reduced
quadratic forms have no common projective residue-field zero. Both
proof cases were read. These are conditions to verify, not assumptions
licensed by rank<[L:F]. Lemma 4.2, p.45, provides a possible index
test: p>2 unramified, good reduction at every prime above p, reduction
group orders prime to p, and formal-kernel generators of finite index;
p dividing the index forces a nonzero mod-p relation of their formal
parameters modulo the squares of those primes. Its proof was read.
It is not a rank or saturation certificate for our field.

Section 4.1, pp.40–42, and the explicit expansions after Lemma 4.1
assume a degree-two cover. L034's degree-twelve map lies outside those
formulas. The general Section 4.2 construction is the relevant scope;
new expansions and nondegeneracy checks would be needed. No such
expansion has been derived in this literature turn.

The [official Magma handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1568),
section “Elliptic Curve Chabauty,” accessed 2026-10-14, documents an
arbitrary K-defined map E->P1 and a supplied Mordell–Weil group map.
The prime-specific routine requires good reduction of curve and map
at every prime above p and returns N,V,R,L. N may be infinite;
completion for E(K) requires finite index coprime to returned R.
Its sieve variant is not guaranteed to terminate. Cosets can restrict
the input group. These are implementation guarantees, not proof that
our data satisfy them; no software invocation or access is assumed.

## Same-field source overlap and covering interface

FNS, *The generalized Fermat equation with exponents 2,3,n*, Compositio
Math. **156** (2020), 77–113,
[final manuscript, June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–27, already reduces these twists to K-points
of X0(11) with rational good modular j. It explicitly requires
finite-index generators, reports failure to reach its Selmer rank
upper bounds, and describes the earlier 2006 attempt that stopped
there. Its replacement is Selmer-group Chabauty. Table 5 gives
2-Selmer dimension four for 54a1 **under GRH-dependent class/unit
computations**; this is neither an unconditional rank certificate nor
four independent points. The cubic two-torsion extension has degree
36. Existing assessment
`2026-10-07-three-four-eleven-even-c-global-descent.md` already records
the conditional elimination; that coverage is reused, not reapproved
as unconditional mathematics. The new overlap is the explicit ordinary
Mordell–Weil prerequisite/failure in this same rational-j setting.

L033's injection E0(K)/theta E1(K)->K*/K*5, imported from
Schaefer–Stoll's June 13, 2001 long manuscript Sections 5 and 9
(canonical source scope in foundations/15), and L062's actual point
P_sigma specify a possible translated-isogeny presentation of the
fixed-class point problem. The proposed map to check is
Q |-> j(P_sigma+theta(Q)) on E1 over K. This is a proposed
specialization of the connecting-map kernel statement, not a covering
construction proved here. A general Selmer class need not have a point;
this particular class comes from a named point. One must retain the
smooth projective completion, exceptional evaluations and the chosen
sigma. The affine equation f(P)=alpha*w^5 alone is insufficient.
No genus increase or rank reduction from this isogeny is claimed.

## Decision and independently testable prerequisite

The source-review continuation test is met only at the prerequisite
level: Bruin Section 4.2 and the implementation both require that the
scalar map retain its cover after reduction. L064 certifies that the
whole K tensor Q13 is unramified of degree twelve; L033 gives good
curve reduction there. L034 gives the complete map and its previously
checked exceptional charts. A separate bounded check of good reduction
of **the entire degree-twelve j map** at thirteen therefore has exact
input data and a discriminating success/failure criterion. It is
independent of the failed finite-prime class-removal target. It tests
one necessary local prerequisite of the global point method, rather
than just rewriting its class equation. Translation/isogeny reduction
would still need justification before applying it on a covering.

The new continuation assessment is
[2026-10-14-modular-map-thirteen-good-reduction.md](2026-10-14-modular-map-thirteen-good-reduction.md).
It requires separate supervisor approval before mathematics. Success
would supply one usable reduction input only; it would not bypass
the independent rank, index, coset-wise zero, other-class or power
lifting gaps. Failure parks thirteen as the chosen reduction prime;
it does not globally ban Chabauty. No rank calculation, new lemma or
mathematical script was written here. Full matching and supporting
Mathlib coverage is not checked; unknown is not absence.

Queries included “Nils Bruin elliptic Chabauty rank number field
rational function good reduction theorem 2003”, “Chabauty methods
using elliptic curves pdf”, official-handbook Ecov/index variants,
and isogeny-covering/torsor terminology. Duquesne's 2003 abstract,
other covering abstracts and torsor search hits were leads only; no
theorems from them are imported. A Milne AV PDF was located but no
extension theorem was inspected or used. Failure to find a match is
not evidence of novelty. No cross-notebook input was read.
