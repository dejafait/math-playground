# Full-theta recurrence concentration: source comparison1934

20 November 2026. Literature only; completes review1933's unchanged target.
No concentration limit, weight comparison, new lemma or mathematical
script is proved here. The supplied overview/DAG and checkpoint were
used directly. Existing unfinished work is preserved.

## Primary coverage and exact hypotheses

E. Levin and D. S. Lubinsky, *On recurrence coefficients for rapidly
decreasing exponential weights*, J. Approx. Theory144(2007),260-281,
DOI[10.1016/j.jat.2006.06.004](https://doi.org/10.1016/j.jat.2006.06.004).
Read the [author manuscript dated16April2006](https://lubinsky.math.gatech.edu/Research%20papers/LevLub05Apr06.pdf),
pp1-5: recurrence notation, MRS definitions, Definition1.2(a)-(e),
Theorem1.3; pp7-14: general-interval proof setup, tail/edge estimates
and bulk reduction; p17: final assembly. The full technical proof was
not independently audited; the named theorem is the proposed import.

For W=exp(-Q) on I=(a,b), -infinity<=a<0<b<=infinity,
assume all W^2 moments finite. Definition1.2(a)-(e) requires continuous
Q:I->[0,infinity), Q(0)=0, continuous Q' off0, Q''>0 off0,
Q tending to infinity at both endpoints, and, writing T(x)=xQ'(x)/Q(x),

    1<Lambda<=T(s)<=C1*T(t) whenever 0<s/t<1,
    Q''(x)/|Q'(x)|<=C2*|Q'(x)|/Q(x) almost everywhere off0.

Theorem1.3 gives A_n/delta_n=1/2+O(n^(-c)), c>0,
for xp_n=A_n*p_(n+1)+B_n*p_n+A_(n-1)*p_(n-1).
Here delta_n is half the MRS interval length. For even Q, delta_n=a_n
and its defining equation is

    n=(2/pi)*integral_0^1 a_n*t*Q'(a_n*t)/sqrt(1-t^2) dt.

Only this general-interval theorem is proposed; finite-interval
Corollaries1.4/1.5 and their extra hypotheses are unnecessary.

G. Szego, *Orthogonal Polynomials*, fourth edition(1975), AMS Colloquium
Publications23, Theorem3.1.2,p39, with Section3.1A,p38 and Section2.2A:
read the [book text](https://djvu.online/file/Nk6YlVBVuENXs).
Despite the host's1939 title, its edition list and fourth-edition preface
identify1975. A positive measure with infinite support and finite moments
has a unique monic polynomial minimizing the squared L2 norm in each
degree: the monic orthogonal polynomial. The interval can be infinite;
the finite-interval restriction on closure in Theorem3.1.5 is separate.
This minimum principle supplies the interface for a bounded density
comparison, without polynomial-density or moment-uniqueness assumptions.

Reuse DLMF18.2(iv),(vi) coverage1931 for the monic norm ratios and
parity; reopened [the monic recurrence](https://dlmf.nist.gov/18.2#E11_5).
The manuscript A_n connects degrees n and n+1, whereas local beta_j
connects degrees j-1 and j. The square and index shift must be retained
in the future application. A bounded density comparison must be applied
to the two separate extremal squared norms before taking their ratio;
it does not compare coefficients of the two polynomials term by term.
Matching Mathlib coverage for the concentration result is unchecked.

## Proposed specialization; no applicability result asserted

The source theorem controls individual model coefficients; the ratio
target asks less information once the scale and transfer steps below
are proved. L019 has not verified that class for -log K itself.
A concrete alternative is to attempt a bounded comparison with

    Q_*(x)=pi*(cosh(2*x)-1)-(9/4)*log(cosh(x)),
    w_*(x)=exp(-2*Q_*(x)), x in R.

This is a proposed comparison weight, not an established theta estimate.
The next proof attempt must verify every hypothesis above for Q_*,
including the global T inequality and the origin limits. It must prove
positive degree-independent constants c,C with
c*w_*<=K(|x|)<=C*w_* on all R, using the full positive series of L019,
controlling its entire n>=2 tail, and checking the bounded central
interval. Matching exponential orders alone is insufficient: the linear
prefactor in the exponent must also be accounted for. No finite theta
truncation or atom replacement is authorized.

The planned discriminating threshold is a two-sided comparison of the
model MRS numbers with log(n+1), followed by extremal-norm transfer.
The sought bounds on the actual beta_j are of order log(j+1)^2 above
and below, with constants independent of j beyond a fixed onset. They
are targets, not conclusions of this review. The exact requested
maximum-to-sum limit could also follow from weaker bounds; no leading
constant, monotonicity or full asymptotic for actual beta_j is needed.
All these applicability calculations belong to the later research turn.
No source theorem is to be reproved; only the specified specialization
and finite norm comparison are needed.

Continue if these global comparisons and hypotheses can be proved and
give the exact limit. Stop this comparison mechanism if its constants
depend on degree or a required class hypothesis fails without a covered
repair. That would not refute concentration for the actual theta weight.
A positive limsup for the actual ratio would reject the diffuse-base
input, but no such result is available. Mere cumulative divergence,
finite-degree samples, or replacing the actual beta_j by model data
does not decide the test.

## Duplicate, failure and search record

Read L019/L021, C028o's exact measure/recurrence and support argument,
C028p's scope/top-residual formulas, C028w through its shared finite
Uvarov system, notes1931, and ATTEMPTS1933. C028o proves T_n->infinity;
C028p uses positivity without controlling max beta_j/T_n. C028w leaves
the two-site image and norm-weighted rates unpaid. No duplicate proof
of concentration was located. Scope searches covered theta/recurrence/
companion literature and attempt filenames for the exact paper title,
Levin--Lubinsky, Erdos/Freud/MRS terminology and the proposed cosh weight.
The cosh hit in ATTEMPTS/2026-09-21-theta-moment-literature-screen.md,
lines52-71, concerns a different shifted-kernel concavity obstruction;
it supplies no recurrence-concentration result. Source-notes1716's
Toda/varying-recurrence results concern unbounded tilt and do not supply
the present base hypothesis. Earlier floors and collar stops remain.

External queries included: orthogonal polynomials recurrence coefficients
exponential Erdos weights; Riemann xi theta weight recurrence coefficients;
the exact Levin--Lubinsky title; theta kernel orthogonal polynomials;
and monic orthogonal polynomial minimum norm Szego. Search hits concerning
Riemann theta functions on multiple intervals or varying quartic weights
were discovery leads only, not theorems about L019's density. The author
publication list and publisher record identify the2007 article, while
the actual theorem coverage comes from the dated primary manuscript.
The2001 monograph's Theorem15.2 is an unread lead cited by that paper;
it is not needed when importing the fully stated Theorem1.3.

The local curl download failed DNS resolution. Web access supplied the
primary manuscript; this is not an essential source blocker. The OSU
Szego PDF exceeded the web fetch size; the book text above supplied the
selected theorem, its context and edition evidence. No conclusion is
inferred from a snippet or failed download. The old1993 mass-point lead
remains parked; this base-only method does not depend on it.

## Decision and relevance

SPECIALIZE: the general recurrence theorem and minimum principle are
covered; the exact theta applicability and elementary comparison remain
research obligations. This prepares a reproduction/specialization attempt,
not an originality claim or an imported theta asymptotic. Literature
outcome EXPLORATION: no mathematical claim for the exact weight is settled.

The main gap is L030-L032/C032a actual-Xi all-degree positivity, with
C028b's H_d=o(d) unpaid. The proposed base input could constrain how
two moving atoms alter a diffuse finite Jacobi spectrum in C028w.
It does not yet separate that image from the actual cubic/quartic pair.
Independent obligations remain: two-site shape separation or construction,
norm-weighted residual rates, omitted full costs and actual-Xi transfer.
Essential local inputs for the continuation are L019/L021,C028o/p/w,
the C028a/b conventions, and this source record plus reused1931.
No actual-root reality, parameter compactness, arbitrary realization,
theta recurrence asymptotic or cross-notebook input is assumed.
