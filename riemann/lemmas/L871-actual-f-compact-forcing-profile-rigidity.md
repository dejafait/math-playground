# Lemma 871: actual-F domination kills the eight compact forcing profiles

## Hypotheses

Use L847's actual nonzero entire function

\[
 G(z)=\tfrac18\xi\left(\tfrac12+\tfrac{\sqrt z}{2}\right),
 \qquad G(0)>0,
 \qquad
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \quad z_j=R e^{x_j+i y_j},\quad C,R>0.
 \tag{1}
\]

Evenness of xi about 1/2 makes the expression for G independent
of the square-root choice. Retain the entire class in L870's
hypotheses, with the additional actual-F domination below. Explicitly,
let h,q,r be real global C1 functions on R2 times
T2=(R/(2pi Z))2, periodic in both angles, and put

\[
 \widehat h_n(x)=(2\pi)^{-2}\int_{[0,2\pi]^2}
                       h(x,y)e^{-in\cdot y}\,dy,
 \qquad m(x)=\widehat h_0(x).
\]

Fix H>0 and the original Hardy-selected zero a=-4 gamma^2,
ell=log(|a|/R), with phase pi, as in L870. Require h>=0 and
m(s,s)=m(ell,s)=H for every real s. The only possible nonzero
forcing frequencies are

\[
 E=\{\pm(1,0),\ \pm(0,1),\ \pm(1,1),\ \pm(1,-1)\}.
 \tag{2}
\]

For n in E, require hhat_n(x)=U_n(n dot x), where U_n is a
complex compactly supported C1 function on R, |U_n|<=H,
U_(-n)(t)=overline(U_n(-t)), and U_n=B_n-B_n'' for some
complex C3 function B_n. For n outside E union {0}, hhat_n=0.
Retain all opposite-index tests: at every x, with a_0(x)=H and
a_k(x)=hhat_(k,-k)(x) for k!=0,

\[
 \sum_{j,l=0}^N c_j\overline{c_l}\,a_{j-l}(x)\geq0
 \quad(N\geq0,\ c_0,\ldots,c_N\in\mathbb C).
 \tag{3}
\]

The full closure system and the strengthened pointwise condition are

\[
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
 \qquad q^2+r^2\leq |F|^2
 \quad\hbox{everywhere}.
 \tag{4}
\]

In particular retain L870's selected-fiber trace
q((ell,s),(pi,v))=r((ell,s),(pi,v))=0 for all s,v; it also
follows from (1),(4). There is no growth or bandwidth condition
on q,r, no restriction on their homogeneous modes, no bound on
their zero modes beyond these hypotheses, and no Fourier
summability, RH, zero simplicity or graph-existence assumption.
All actual zeros and the diagonal of F remain in (4).

## Conclusion

Every U_n, n in E, is identically zero. Thus h(x,y)=m(x) is
independent of both angles throughout the domain. This conclusion
is for every permitted lift q,r, not only a Green or finite-mode lift.

The exact separation threshold in the proof is this: if T>0 contains
all eight profile supports in [-T,T], choose an actual negative
zero a_* with lambda=log(|a_*|/R)>2T. The corresponding two
coordinate zero fibers suffice. Hardy supplies such a zero without
an effective height or spacing bound.

This is a partial rigidity result in the stated eight-frequency,
compact-profile class. The separate conceptual audit of 6 November
2026 below accepts this exact implication. It does not assert radial
constancy of m, vanishing
of q or r, a classification for other forcing supports, the period
bound K>=-|M|, graph realization, Xi positivity or RH. The class
is nonempty: h=H and q=r=0, with all profiles zero, satisfies
every stated hypothesis.

## Proof

### Source scope and the additional actual zero

The invocation-start assessment is
`drafts/literature/2026-11-06-actual-f-compact-profile-rigidity.md`,
DECISION EXPLORE. Its scope expressly permits necessary conditions
from further actual zero fibers, while keeping all lift modes.
It found no matching theorem for this implication; this does not
certify originality. L870's negative Green form is a contrast, not
a mathematical premise of the present proof.

Import Hardy's theorem from E. C. Titchmarsh, *The Theory of the
Riemann Zeta-function*, second edition, revised D. R. Heath-Brown,
Oxford (1986), [Section 10.2, pp256-258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=133):
there are infinitely many distinct zeta zeros on Re(s)=1/2.
The source statement and first proof were inspected in the reused
assessment. This theorem is not reproved.

For each nonzero ordinate gamma supplied by Hardy, L018's exact
zero correspondence gives xi(1/2+i gamma)=0.
For a_gamma=-4 gamma^2, either square root is +/-2i gamma;
L018's reflection xi(s)=xi(1-s) makes both values in (1) zero. Hence
G(a_gamma)=0, a_gamma<0, and its phase is pi. This is the same
coordinate specialization as C868b, checked here for every zero
used, not an assumption that its one originally selected zero can
be moved freely. Infinitely many distinct ordinates give infinitely
many distinct a_gamma, since squaring identifies at most two real
ordinates. Their moduli are unbounded: otherwise they have a finite
accumulation point, and the identity theorem for holomorphic
functions would force the entire G to vanish identically, contrary
to G(0)>0. For this named identity theorem reuse the input already
assessed in L847: Jiří Lebl, *Guide to Cultivating Complex Analysis*,
version 1.10, 5 November 2026,
[Theorem 2.4.7, pp49-50](https://www.jirka.org/ca/ca.pdf).
Its domain here is the connected plane and G is entire. No
information about off-line zeros or multiplicities is required.

The eight compact supports have a common finite bound [-T,T], with
T>0. Choose one of these actual negative zeros a_* so large that

\[
 |a_*|>R e^{2T},\qquad \lambda=\log(|a_*|/R)>2T.
 \tag{5}
\]

This is an existential choice of one finite radial coordinate,
not a limit of the admissible functions as x tends to infinity.

### Exact reconstruction of the forcing alone

For the finite reconstruction use the already assessed product
Fejer theorem in Loukas Grafakos, *Classical Fourier Analysis*,
third edition (2014), Definition 3.1.8, Remark 3.1.9,
Proposition 3.1.10 and Corollary 3.2.2, pp180-183; see
[the book](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf)
and the [corrected Theorem 1.2.19(2) and proof, pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf).
Normalize the angles by y/(2pi) for its unit torus.

At each fixed finite x, h(x,.) is continuous on the compact torus.
Subtract from it the finite polynomial with the prescribed
coefficients. Every Fourier coefficient of the difference is zero,
so each product Fejer polynomial of that difference is zero.
Uniform product Fejer convergence therefore gives the exact identity

\[
 h(x,y)=m(x)+\sum_{n\in E}U_n(n\cdot x)e^{in\cdot y}.
 \tag{6}
\]

This is reconstruction only of h, whose finite forcing support is
a hypothesis. Neither q nor r is reconstructed, truncated, or
differentiated through an infinite series. No uniformity in
unbounded radial coordinates is claimed or needed.

### Tangential closure on the first zero fiber

On x1=lambda,y1=pi, one has z1=a_*, so F=0 for every
x2=s,y2=v. Both z coordinates are nonzero, so the denominator
in (1) causes no exception. Domination (4) implies

\[
 q((\lambda,s),(\pi,v))=r((\lambda,s),(\pi,v))=0
 \quad(s,v\in\mathbb R).
 \tag{7}
\]

Differentiate this trace only in its tangent directions:
q_x2=0 and r_y2=0 on the fiber, because the respective difference
quotients stay on (7). C1 regularity suffices. The j=2 second
closure equation then gives h_x2=0 there. By the real mean value
theorem, for each fixed v, h((lambda,s),(pi,v)) is independent
of s. Use the assessed statement and proof in Jiri Lebl,
*Basic Analysis I*, [Theorem 4.2.4](https://www.jirka.org/ra/html/sec_mvt.html),
author HTML inspected 6 November 2026: the real C1 trace meets
its continuity and differentiability hypotheses on every finite
closed s interval. This is the tangential observation used in C869a, with
the two directions explicitly checked for this new actual fiber.
No normal derivative of q or r is set to zero.

Project this constant-in-s trace onto angular frequency +1 in v.
By the finite identity (6), its normalized coefficient is exactly

\[
 P(s)=\frac1{2\pi}\int_0^{2\pi}
       h((\lambda,s),(\pi,v))e^{-iv}\,dv
     =U_{(0,1)}(s)-U_{(1,1)}(s+\lambda)
                         -U_{(-1,1)}(s-\lambda).
 \tag{8}
\]

Indeed only the three indices with n2=1 survive. Their n1 phases
are 1,-1,-1 since exp(i pi)=exp(-i pi)=-1. The radial zero mode
m(lambda,s) has angular frequency zero and contributes nothing,
even if it varies with s. Integration preserves the established
constancy in s; no differentiation under an infinite sum or
noncompact integral is involved.

For this fixed lambda, each term on the right of (8) is compactly
supported as a function of s. Thus P is both constant and compactly
supported, so P=0. Consequently

\[
 U_{(0,1)}(s)=U_{(1,1)}(s+\lambda)+U_{(-1,1)}(s-\lambda)
 \quad(s\in\mathbb R).
 \tag{9}
\]

### The support separation kills six profiles

The possible supports of the three terms in (9), as functions of
s, are respectively

\[
 [-T,T],\qquad[-\lambda-T,-\lambda+T],\qquad
 [\lambda-T,\lambda+T].
 \tag{10}
\]

They are pairwise disjoint by the strict inequality lambda>2T.
For completeness, the following evaluations prove vanishing at
every point, without a limiting assertion. It suffices to consider
t in [-T,T], since all original profiles are zero outside it.

- At s=t, both shifted arguments t+lambda and t-lambda lie
  outside [-T,T]; (9) gives U_(0,1)(t)=0.
- At s=t-lambda, the unshifted argument s is below -T and the
  last argument t-2lambda is below -T; (9) gives U_(1,1)(t)=0.
- At s=t+lambda, the unshifted argument s is above T and the
  middle argument t+2lambda is above T; (9) gives U_(-1,1)(t)=0.

These calculations hold for complex profile values, with no sign
or real-valued assumption on an individual profile. Reality in the
stated form U_(-n)(t)=overline(U_n(-t)) now also kills
U_(0,-1), U_(-1,-1), and U_(1,-1). All six profiles with n2!=0
have vanished.

### The other coordinate fiber kills the last pair

The same actual zero also gives F=0 on x2=lambda,y2=pi, for
all x1=s,y1=v. There q=r=0, and tangential differentiation gives
q_x1=0 and r_y1=0. The j=1 second closure equation gives h_x1=0
on this fiber. Hence h((s,lambda),(v,pi)) is independent of s
for each v. Its angular frequency +1 in v, computed from (6), is

\[
 Q(s)=U_{(1,0)}(s)-U_{(1,1)}(s+\lambda)
                         -U_{(1,-1)}(s-\lambda).
 \tag{11}
\]

The last two profiles already vanish. Thus U_(1,0)=Q is constant
in s and compactly supported, and must vanish. Reality then kills
U_(-1,0). This accounts for every index in E. Identity (6) proves
h=m everywhere, as claimed.

### Scope of the obstruction and remaining gaps

All conclusions followed from necessary trace conditions on the
original q,r. Arbitrarily many homogeneous lift frequencies, their
zero modes, and all cancellations among them remain permitted in
the argument. They cannot change (7) or the tangential closure
identities. The finite support was imposed only on the forcing h.

The means, H>0, nonnegativity, magnitude bounds, C3 profile relation
and opposite-index tests were retained but were not needed for this
necessary-condition proof. No conclusion about their sufficiency is
drawn. The additional zero (5), supplied by the actual coefficient,
is the information absent from the one-fiber relaxed class in L870.
This explains why the present rigidity does not contradict L870's
audited lift or either earlier Green stop. It rules out actual-F
admissibility of a nonzero compact forcing in this exact class;
it does not repair the failed relaxed Green implication.

Finite forcing support and compactness are used explicitly in (6)
and (8)-(10). This proof does not license a finite approximation to
an arbitrary admissible forcing or an extension to noncompact or
infinitely many profiles. It also gives no estimate on the zero mode
m away from its prescribed lines or on the period constant K at the
threshold -|M|. Those issues, graph realization, and the main
L030-L032/C032a all-degree Xi positivity gap remain open.

### Independent conceptual audit, 6 November 2026

This is the separate proof audit
`2026-11-06-actual-f-compact-profile-audit-02`, under the unchanged
invocation-start EXPLORE assessment cited above. The audit accepts
the stated universal implication with no additional assumption.
It reproduces and checks the submitted argument; it establishes no
new extension or certified originality. The known Hardy, Fejer,
identity and mean-value theorems remain imports from the assessed
sources, not results proved by this audit.

**Exact class and actual coefficient.** Comparison with L870's
hypotheses confirms H>0, both mean lines, the eight frequencies,
complex C1 compact profiles, the C3 relation, all opposite-index
tests and both closure equations. The added condition is global
actual-F domination. The proof uses neither a finite Fourier
representation of q,r nor L870's constructed negative Green form.
The positive constants C,R need no normalization for this argument:
z_j never vanishes, and either actual G-zero makes F exactly zero.
In particular the original L847 normalization is included.

**Far-zero quantifier and coordinate.** L018 applies at every
nonzero critical ordinate: the xi prefactor is regular and nonzero
inside the critical strip. The two roots of -4 gamma^2 give the
reflected xi arguments, so both yield zero in (1). Squaring real
ordinates identifies at most two distinct ordinates. Infinitely
many distinct negative G-zeros are therefore obtained. If their
absolute values were bounded, a subsequence would accumulate at a
finite point of the plane; the identity theorem contradicts
G(0)>0. After the profiles and T have been fixed, one can select a
finite a_* with |a_*|>R exp(2T). The selected original ell is never
changed, and no prescribed zero, effective bound, spacing, RH or
simplicity premise enters this step.

**Reconstruction and trace regularity.** For every fixed x the
difference between h(x,.) and the finite sum (6) is continuous
and has all Fourier coefficients zero. Every product Fejer mean
of this difference is zero; uniform convergence on this one torus
therefore proves (6). This argument requires no uniform estimate
as x varies. On the first zero fiber domination and real q,r
give their pointwise vanishing. For each fixed v, changing s stays
on that fiber, so q_x2=0; for each fixed s, changing v stays on
it, so r_y2=0. The second closure equation gives h_x2=0. The
mean-value theorem on each finite s interval gives the required
constancy for each v. None of these operations takes a normal
derivative or reconstructs a lift. The same reasoning with indices
interchanged proves the second-fiber trace assertion.

**Complex projections and exhaustive support check.** In the first
projection the only surviving indices are (0,1),(1,1),(-1,1).
Their phases at y1=pi are respectively 1,-1,-1, and their arguments
are s,s+lambda,s-lambda. This independently recovers (8), with no
zero-mode contribution. Its constancy and finite union of compact
supports force P=0. For every t in [-T,T], the equation at s=t
isolates U_(0,1)(t); at s=t-lambda it isolates U_(1,1)(t), since
s<-T and t-2lambda<-T; at s=t+lambda it isolates U_(-1,1)(t),
since s>T and t+2lambda>T. These strict inequalities include both
endpoints because lambda>2T. Outside [-T,T] the profiles already
vanish. The three opposite profiles vanish by conjugation with
argument reversal; no real sign assumption on a profile is used.
The second projection contains (1,0),(1,1),(1,-1), with the same
three phase factors. Its latter two terms are already zero, so
the constant compactly supported U_(1,0) is zero; conjugation
kills U_(-1,0). All eight indices, including both mixed signs,
are thus accounted for.

**Limits of the accepted result.** Unused mean, positivity and
profile-relation assumptions remain in the statement; their lack
of use does not strengthen the conclusion here. The constant
example h=H,q=r=0 checks nonemptiness, including all tests in (3).
There is no inference that necessary zero traces suffice for
global domination. The earlier relaxed Green counterexamples lack
this global condition, so their recorded stops are unaffected.
Finite reconstruction and compact support are essential to the
written proof. No approximation argument transfers it to arbitrary
forcing, and no period, graph or Xi-sign conclusion follows. No
additional mathematical premise was introduced by the audit;
the historical contrasts are not inputs to this implication.

## Mathlib

Full matching coverage for this actual-F eight-profile implication
has not been checked. The source assessment also did not check
Mathlib coverage for the supporting Hardy, Fejer and calculus
inputs. No availability or absence claim is made. The proof above
is an informal argument using the cited named theorems and explicit
finite identities; it is not a Lean verification.
