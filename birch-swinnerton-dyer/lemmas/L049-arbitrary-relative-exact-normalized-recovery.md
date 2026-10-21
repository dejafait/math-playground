# L049 — Terminating arbitrary-relative exact normalized recovery

## Hypotheses

Let E/Q, its global minimal equation, minimal Neron differential, exact
conductor N, associated normalized newform f and integral relative module
M have precisely the hypotheses and oriented conventions of L048. In
particular CM and additive reduction are allowed. Supply a complete
finite integral generating list x_1,...,x_d for M, each written as a finite
integral sum of actual oriented rational-cusp paths. The arithmetic input
is exact: finite initial segments of f's Fourier coefficients can be
computed, rather than supplied as floating-point approximations. This is
the computational meaning of the supplied exact newform, not a claim
about generic presentation or arithmetic software.

Put A_f({a,b})=2*pi*i integral_a^b f(z) dz and
F(x)=Re(A_f(x))/Omega(E), where Omega(E) is the integral of the absolute
minimal differential over the entire real locus. Use L048's independently
computable integer K=K(E), so K F(M) is contained in Z. No optimal model,
isogeny map, differential scalar, normalized value or nonzero twist value
is an input.

## Conclusion

There is a terminating exact-arithmetic procedure recovering every
F(x_j). For each j it constructs rational outward intervals J_j containing
F(x_j), refines them until

\[
 \lceil K\inf J_j\rceil=\lfloor K\sup J_j\rfloor=m_j,
 \qquad F(x_j)=m_j/K.
\tag{1}
\]

The intervals can have arbitrarily small width. Termination includes
zero values, nonunitary cusps and both signs of the minimal discriminant.
The recovered generator table determines the entire relative functional;
its reduced generator denominators have a computable common lcm Q, which
clears F(M). Consequently v_p(F(x))>=-v_p(Q) for all x in M.

This is an assembly of known numerical-modular-symbol and real-period
algorithms with audited L048's coarse clearing integer. It supplies no
runtime bound or executable implementation, and still grants the exact
arithmetic and complete integral generating paths. Evaluation of a new
path from this table also requires its integral coordinates; their
software construction is not proved here. It supplies no coefficient
nonvanishing, rational points, Sha statement or complex-order comparison.
The separate critical audit below passes under these unchanged hypotheses.

## Proof

**Source imports, scope and the limited rederivation.** Reuse the prior
[SPECIALIZE assessment](../drafts/literature/2026-10-11-arbitrary-relative-exact-recovery.md).
The primary imports are Wuthrich, *Numerical modular symbols for elliptic
curves*, arXiv:1608.06423v2, 23 March 2017,
[equation (2), Lemma 4 with proof, and Section 5.1 equation (11),
printed pp.6--7,11--12](https://arxiv.org/pdf/1608.06423v2);
Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997),
[Proposition 2.2.3 and its constructive proof, (2.4.1), (2.9.1) and its
arbitrary-cusp remark, pp.16--19,31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf);
and Cremona's
[Section 3.7, (3.7.1) and both real-root cases, pp.97--98](https://johncremona.github.io/book/fulltext/chapter3.pdf).
The positive AGM iteration and common-limit theorem are
[DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i).
Dirichlet's theorem, Sturm's real-root isolation theorem, Machin's formula
for pi, and Taylor's theorem with remainder are standard named inputs.

We import these identities rather than reprove modular-symbol integration
or the elliptic-period formula. The source assessment identifies a
suspect sign in Wuthrich Section 5.2's final display; hence the oriented
closing sign is checked directly against Cremona's identity below.
Outward finite-function evaluation is specified because Wuthrich's
Lemma 6 assumes a correctly computed q and does not certify the target
period. These are the differences being specialized, not a claim of a
new integration method. L048 is the only local mathematical input.
L028/L038 and the fixed period certificates are comparisons only.

**Finite arithmetic preparation and cusp matrices.** Collect all finite
cusp denominators in the supplied paths. Enumerate a prime ell>2 with
ell=1 modulo N and ell dividing none of these denominators or N.
Dirichlet supplies infinitely many eligible progression primes (ordinary
prime infinitude suffices for N=1), so excluding this finite list preserves
termination. Trial division is enough for primality. Compute a_ell exactly
and h=ell+1-a_ell=#E(F_ell)>0 by counting the target reduction. The
associated-newform hypothesis identifies the eigenvalue with this trace.

For a finite reduced cusp r=a/m, m>0, the full good-prime Hecke terms
have endpoints

\[
 v_* = \ell r,\qquad v_j=(r+j)/\ell\quad(0\le j<\ell).
\tag{2}
\]

Every endpoint in (2) is Gamma_0(N)-equivalent to r. Here is the explicit
specialization of Cremona Proposition 2.2.3(2). That criterion for reduced
p_1/q_1 and p_2/q_2 is q_2=u q_1 modulo N and u p_2=p_1 modulo
gcd(q_1,N), for a unit u modulo N. For v_* use u=1: ell is coprime to m,
so its denominator remains m and its numerator is ell a. For v_j, the
only possible cancellation in (a+jm)/(ell m) is ell, since
gcd(a+jm,m)=1. Without cancellation the denominator is ell m=m modulo N
and the numerator is a modulo gcd(m,N). With cancellation the denominator
is m and the numerator is (a+jm)/ell, also a modulo gcd(m,N), because ell
is 1 modulo N and therefore invertible there. This includes numerator
zero, necessarily at denominator m=1. Thus u=1 works in every case.

Construct gamma_v in Gamma_0(N) mapping r to each reduced v=p_v/m_v.
For completeness the constructive matrix witness is as follows. Bezout
gives integers s_r,t_r,s_v,t_v with a s_r-m t_r=1 and
p_v s_v-m_v t_v=1. Set

\[
 \delta_r=\begin{pmatrix}a&t_r\\m&s_r\end{pmatrix},\quad
 \delta_v=\begin{pmatrix}p_v&t_v\\m_v&s_v\end{pmatrix},\quad
 \gamma_v=\delta_v\begin{pmatrix}1&t\\0&1\end{pmatrix}\delta_r^{-1}.
\tag{3}
\]

Its lower-left entry is m_v s_r-m s_v-t m m_v. The linear congruence
t m m_v=m_v s_r-m s_v modulo N is solvable by the constructive proof
of Proposition 2.2.3, since the cusps are equivalent. Solve it by extended
gcd. The resulting matrix has determinant one, lower-left entry divisible
by N and gamma_v(r)=v. These are exact finite witness checks; no matrix
optimization or new cusp expansion is required. They apply even when
the transporting matrix is parabolic or elliptic.

**Oriented closing and transportation.** Use the infinity-based primitive

\[
 P(z)=2\pi i\int_\infty^z f(w)dw
     =\sum_{n\ge1}(a_n/n)e^{2\pi i n z},\qquad P(\infty)=0.
\tag{4}
\]

Cusp limits exist because f is cuspidal at every cusp. In the simply
connected upper half plane A_f({a,b})=P(b)-P(a), with cusp limits at
the endpoints. The imported Hecke action and adjointness give

\[
 (\ell+1-a_\ell)A_f(\{r,\infty\})
       =A_f(\{r,\ell r\})+
          \sum_{j=0}^{\ell-1}A_f(\{r,(r+j)/\ell\}).
\tag{5}
\]

This is precisely Cremona (2.9.1) evaluated against f, with no central
vanishing premise. Since A_f({r,infinity})=-P(r), (5) says
h P(r)=-sum_v A_f({r,v}). Imported transportation (Wuthrich (11)),
with gamma_v(r)=v, says
A_f({r,v})=P(gamma_v tau)-P(tau). Taking tau=i gives

\[
 \boxed{P(r)=\frac1h\sum_v\bigl(P(i)-P(\gamma_v i)\bigr).}
\tag{6}
\]

This fixes the sign from the oriented definitions, without relying on
the suspect source display. The sign also follows by replacing every
path in (5) by P(v)-P(r). All ell+1 terms are retained, including any
zero transport. For gamma=(A B;C D), gamma i has rational real and
imaginary parts, with Im(gamma i)=1/(C^2+D^2)>0. Thus (6) uses only a
finite list of interior points, always of positive height. For infinity
use P(infinity)=0 exactly. Applying (6) to both endpoints recovers the
oriented primitive difference for every supplied generator.

**Certified Fourier evaluation with shrinking total error.** Import
Wuthrich Lemma 4's complete tail estimate: for z=x+iy, y>0, truncating
(4) after H terms leaves complex error at most

\[
 \frac{e^{-2\pi H y}}{e^{2\pi y}-1}.
\tag{7}
\]

Its proof applies to the associated elliptic newform, including bad
reduction, and uses |a_n|<=n. At our fixed points y is an exact positive
rational. The elementary inequalities pi>3 and e>2 give the conservative
rational upper bound

\[
 R_H(y)=\frac{2^{-\lfloor6Hy\rfloor}}{6y}
\tag{8}
\]

for (7): the denominator exceeds 6y, and e^{-2*pi*H*y}<=e^{-6Hy}
<=2^{-floor(6Hy)}. Enumerating H until R_H(y)<eta/2 terminates for every
rational eta>0, since floor(6Hy) tends to infinity. No floating-point
logarithm or limit test determines the truncation.

Compute the finite sum with rational complex rectangles to error less
than eta/2. Here is a sufficient finite-function certificate convention.
Machin's identity pi=16 arctan(1/5)-4 arctan(1/239), with each arctangent
enclosed by the alternating Taylor remainder and intersected with [3,4],
gives positive rational pi intervals of arbitrarily small width. For a complex exponential at argument w,
bound |w| above by a rational L and take an integer q>=L. The degree-J
Taylor remainder is at most

\[
 3^q\frac{L^{J+1}}{(J+1)!},
\tag{9}
\]

since e^L<=3^q. Choose L uniformly using the initial pi bound [3,4].
For this fixed L, (9) tends to zero by the ratio test; first choose J to
meet the remainder budget. Finite polynomial evaluation of the rational
rectangle for w encloses every possible argument, and its width tends to
zero as that rectangle shrinks. Then refine pi at this fixed J until
the polynomial width meets its error budget. This certifies each finite
exponential and then the finite sum to the requested error. Equivalently
one can enclose q=e^{2*pi*i*z} and evaluate its finite polynomial. Exact
a_n/n and rational outward arithmetic introduce no unrecorded rounding.
No correctness theorem for a floating-point library is imported.

Every requested finite coefficient segment is computable under the exact
arithmetic input: Cremona (2.6.1)--(2.6.2), p.25, gives multiplicativity
and good/bad prime-power recurrences. Good traces are finite point counts;
the usual exact local factors at bad primes are part of the associated
newform data. No unproved optimality or normalization enters coefficients.

Expand the finite generator expression using (6). It is a finite rational
linear combination of P-values at the interior points and exact zeros,
with coefficients fixed before precision refinement. If the sum of
absolute coefficients is W, request each primitive with complex error
less than eta/(1+W). The total error is then less than eta; W=0 is an exact
zero expression. Adding the tail disk in (8) outward to each finite
rectangle gives a certified real interval U_j for Re(A_f(x_j)), of
arbitrarily small width. Signed generator coefficients and repeated
endpoints are included in W. This proves full error shrinking, not merely
pointwise floating convergence or a sampled-path approximation.

**Independent target total period, including both component factors.**
Complete the given minimal equation as

\[
 Y=y+(a_1x+a_3)/2,\quad
 Y^2=g(x)=x^3+\alpha x^2+\beta x+\gamma,
 \quad(\alpha,\beta,\gamma)=(b_2/4,b_4/2,b_6/4).
\tag{10}
\]

The differential is exactly dx/(2Y). The discriminant of g is Delta_E/16,
so its roots are simple and its sign is known exactly. Sturm isolation
and rational refinement give shrinking intervals for each real root;
roots equal to rational trial endpoints can be retained exactly.

If Delta_E>0, order the three real roots e_3>e_2>e_1 and put
a=sqrt(e_3-e_1), b=sqrt(e_3-e_2), using positive roots. Cremona (3.7.1)
gives the least positive real lattice period lambda_1=pi/AGM(a,b).
This case has two real components, so Omega(E)=2 lambda_1.

If Delta_E<0, let r be the real root and write the other roots u+iv,u-iv,
with v>0. Vieta gives

\[
 u=(-\alpha-r)/2,\quad v^2=\beta-2ru-u^2>0,\quad d=r-u,
 \quad R=\sqrt{d^2+v^2},\quad
 a=\sqrt R,\quad b=\sqrt{(R+d)/2}.
\tag{11}
\]

Indeed for z=sqrt(r-u-iv) with Re(z)>0, |z|=sqrt(R) and
Re(z)=sqrt((R+d)/2). Since v^2>0, R>|d|, so all positive branches
in (11) are defined, even if d is negative. This specializes Cremona's
one-real-root formula lambda_1=pi/AGM(|z|,Re(z)). Here the real locus
is connected, and Omega(E)=lambda_1. It is the total target period,
not a period of the optimal quotient. Write c_infinity=2 or 1 respectively.

Positive square roots of rational endpoints are enclosed by bisection,
whose rational squared comparisons certify the branches. Shrinking root
intervals and finite algebraic operations give arbitrarily accurate
enclosures of a,b; eventual positivity is certified because their true
values are positive and the roots are separated. In both cases a>=b>0.
For the exact positive AGM iterates put

\[
 A_0=a,\quad G_0=b,\qquad
 A_{n+1}=(A_n+G_n)/2,\quad G_{n+1}=\sqrt{A_nG_n}.
\tag{12}
\]

The imported positive-AGM theorem gives G_n<=M_AGM<=A_n and
A_n-G_n tending to zero. Here is a precision schedule that also controls
outward error. For each n>=1, recompute the finite first n iterations
from refined root intervals, refining every square root and input until
the final intervals for A_n and G_n each have width at most 2^{-n},
their lower bounds are positive, and the pi interval has width at most
2^{-n}. For fixed n this inner refinement terminates: it is a finite
composition of continuous arithmetic and positive square roots at strictly
positive exact arguments. Trial rational comparisons of widths and
positivity, rather than inferred decimal convergence, certify completion.

Use rational endpoints A_n^+,G_n^- and pi^-,pi^+ to form

\[
 V_n=\left[\frac{c_\infty\pi^-}{A_n^+},
            \frac{c_\infty\pi^+}{G_n^-}\right].
\tag{13}
\]

This contains Omega(E) and has positive lower bound. Its denominator
endpoints tend to the same positive M_AGM: exact AGM convergence controls
the gap, and the just-certified finite errors tend to zero. Therefore
the width of V_n tends to zero. This schedule avoids assuming that a
fixed rounding precision remains valid through arbitrarily many AGM
iterations. Enumerate n until the actual rational width is below any
requested eta>0. It terminates and certifies the total period using the
target minimal equation alone. The lattice/component convention agrees
with L048's two real-lattice cases; no Manin constant equality is used.

**Division, exact isolation and termination.** For each generator, refine
its real integration interval U_j and a positive total-period interval V
to widths tending to zero as above. Set J_j=U_j/V by full outward rational
interval division: take the minimum and maximum of the four endpoint
quotients, since V is positive. This handles either sign of U_j and zero.
It contains F(x_j). To check shrinking explicitly, eventually V has lower
bound Omega(E)/2 and U_j stays bounded. If A=Re(A_f(x_j)), then for any
u in U_j and v in V,

\[
 \left|\frac uv-\frac A{\Omega(E)}\right|
 \le\frac{|u-A|}{v}
    +\frac{|A|\,|v-\Omega(E)|}{v\Omega(E)}.
\tag{14}
\]

Both terms tend to zero, so width(J_j) tends to zero. This proof does
not require a known numerical lower bound for Omega(E): the positive
outward lower endpoint already suffices for each actual division.

Compute K by L048. At successive refinement stages calculate the two
integers in (1) exactly. The true scaled value K F(x_j) is an integer
by L048, so every scaled interval contains at least one integer. Once
K width(J_j)<1 it contains at most one integer, and the two rounded
endpoints agree. Since K is a fixed finite positive integer, shrinking
ensures this occurs. The width threshold is checked, not assumed from
the selected precision. If F(x_j)=0, enclosure inclusion keeps zero in
every interval and the same width test isolates it; no sign decision or
nonvanishing assumption is needed. There are finitely many j, so all
these separate terminating procedures finish.

Reduce each m_j/K exactly. Let Q be the lcm of the positive reduced
denominators, with zero's denominator one and Q=1 if the generating list
is empty. Integral generation gives Q F(M) contained in Z. The recovered
table already equals the genuine functional on every generator, so all
relations hold and it determines F on M; this does not independently
validate a supplied presentation. The stated all-argument valuation bound
follows. A bounded denominator alone would not give (1) without existence;
L048 supplies existence of the integer at every stage.

**Result of the bounded attempt and remaining gaps.** The continuation
test succeeds at the theorem-assembly level: all supplied generators have
shrinking independent enclosures and terminating exact isolation, with no
unknown scale or optimality premise. The finite matrix/congruence witnesses,
all Fourier terms and tails, root/AGM enclosures and endpoint divisions
describe what a future executable certificate must retain; none has been
implemented or replayed in this step. The original named-import
qualifications in L048 persist. This is local known-algorithm reproduction,
not progress beyond the inspected numerical-modular-symbol results or a
BSD candidate. In particular the recovered functional may yield a
coefficient enclosure containing zero; non-CM and the other downstream
arithmetic hypotheses of L027 remain separate. Rational directions, Sha
defects and complex-order comparison remain unresolved.

**Separate critical audit, 2026-10-11.**
BSD-2026-10-11-165-arbitrary-relative-recovery-critical-audit checks the
whole statement and proof against the unchanged approved
[audit assessment](../drafts/literature/2026-10-11-arbitrary-relative-recovery-critical-audit.md).
The theorem-assembly audit passes, without changing the hypotheses,
formulas or stopping threshold. The Wuthrich printed-page citation above
is corrected. The following checks make the source sign comparison and
finite-error bookkeeping explicit; they import the cited analytic
identities and do not claim a new integration algorithm.

1. **Eligibility and reduced cusps.** The excluded denominator primes form
   a finite set, while Dirichlet gives infinitely many primes in 1 modulo
   N. Every selected prime is good and h is the positive target point
   count. For (a+jm)/(ell m), coprimality with m excludes every cancellation
   except ell. If ell cancels, division by ell preserves the numerator
   modulo gcd(m,N), because ell is 1 modulo N. If the numerator is zero,
   gcd(a+jm,m)=1 forces m=1 and the reduced cusp is 0/1. Thus Cremona's
   criterion (2) applies with u=1 in every case, without requiring the
   original cusp to be unitary or coprime to N.

2. **Matrix sign and all Bezout choices.** Multiplying the three matrices
   in (3), rather than copying the extracted source congruence, gives
   \[
   \gamma_v=
   \begin{pmatrix}
   p_v s_r-m(p_vt+t_v)&-p_vt_r+a(p_vt+t_v)\\
   m_v s_r-m(m_vt+s_v)&-m_vt_r+a(m_vt+s_v)
   \end{pmatrix}.
   \]
   Hence the coefficient of t in its lower-left entry is -m m_v.
   Cremona Proposition 2.2.3(3) gives
   gcd(m m_v,N) dividing m_v s_r-m s_v, exactly the solvability condition
   for (3)'s congruence. Changing either Bezout solution changes the latter
   expression by a multiple of m m_v, so cannot spoil solvability. Every
   determinant is one and delta_r inverse sends r to infinity; the middle
   matrix fixes infinity and delta_v sends it to v. A representative with
   opposite overall sign has the same cusp action. This verifies the
   chosen construction, including C=0 and nonhyperbolic matrices. The
   extracted plus sign in Wuthrich Section 5.1 is not used for this fixed
   parameterization; replacing t by -t would require changing the middle
   matrix as well.

3. **Orientation and the full Hecke sum.** The imported adjointness gives
   a_ell P(r)=sum_v P(v), since all ell+1 images of infinity are infinity.
   Subtracting (ell+1)P(r) shows
   sum_v(P(v)-P(r))=-h P(r). Wuthrich (11) applied to the reversed path
   from gamma_v r to r gives P(i)-P(gamma_v i); reversing it gives
   P(v)-P(r)=P(gamma_v i)-P(i). Consequently (6) has the correct sign.
   This is the limited orientation check authorized by the suspect
   source display; no central vanishing or unknown normalized value
   enters. For gamma_v=(A B;C D), its determinant one gives
   gamma_v i=(AC+BD+i)/(C^2+D^2), so both coordinates are rational
   and the height is strictly positive. C=D=0 is impossible. Infinity
   is treated exactly, both finite endpoints use the same convention,
   and repeated or zero transport terms may be retained.

4. **All Fourier and finite-function errors.** Wuthrich Lemma 4's proof
   supplies (7) for the elliptic newform, with no optimality restriction
   on this analytic estimate. For H>=0 and y>0, the inequalities in (8)
   all have the stated direction, and floor(6Hy) tends to infinity.
   Thus the exact rational tail search terminates even at very small
   height. To make the finite-sum budget explicit, put
   S_H=sum_(1<=n<=H)|a_n/n| and epsilon=eta/(4(1+S_H)). For each
   exponential choose a rational bound L on its argument using pi in
   [3,4], for example L=8n(|x|+y). Choose J so (9) is <epsilon/8;
   factorial growth guarantees that this search terminates. Refine pi
   at that fixed J until the evaluated polynomial rectangle has the
   sum of its side lengths <epsilon/4. Finite interval polynomial
   evaluation converges at a point, so this refinement also terminates.
   Enlarging each coordinate by the Taylor remainder encloses the exact
   exponential. The resulting rectangle has diameter <epsilon: its
   diameter is at most the original sum of side lengths plus four
   remainder radii, hence is <3epsilon/4. Its rational center has error
   <epsilon, and the summed finite errors are <S_H epsilon<eta/4.
   With the tail <eta/2 this gives complex error <eta. The H=0 sum
   is exact. This explicitly realizes the arbitrary requested precision
   in the original proof; there is no fixed precision through growing H.
   For the finite rational generator combination, the sum W of absolute
   coefficients is fixed before refinement and bounds accumulated error
   by W times the primitive error. Signs and repeated endpoints cannot
   defeat this bound. Rectangle side widths, not just their centers,
   tend to zero; the real projected intervals therefore shrink too.

5. **Minimal differential and both positive period branches.** Completing
   the square leaves dx/(2Y) exactly equal to the given minimal Neron
   differential. Since disc(g)=Delta_E/16 is nonzero, root isolation
   separates the three-real-root case or the unique real root from its
   conjugate pair. In the latter case Vieta gives the stated v^2>0.
   Thus R>|d|, b^2=(R+d)/2>0 and a^2-b^2=(R-d)/2>0, including d<0.
   No decision about the sign of an approximate d is needed. The square
   root of d-iv with positive real part has modulus sqrt(R) and real
   part sqrt((R+d)/2), precisely the inputs in Cremona Section 3.7.
   In the three-real-root case both differences used in a,b are strictly
   positive. The target's total period is twice its least positive real
   period for Delta_E>0 and once for Delta_E<0, as in the real-lattice
   convention checked in L048. No equality between target and optimal
   periods, or between their differentials, is assumed.

6. **Inner and outer AGM termination.** At each fixed n there are only
   finitely many continuous operations at positive exact arguments.
   Uniformly refining root isolations and bisection tolerances eventually
   makes all square-root inputs positive, all requested output widths
   <=2^(-n), and both final lower bounds positive. Before positivity is
   certified the attempt is retried with finer input intervals. For the
   completed stage, containment and the certified widths imply
   \[
   0\le A_n^+-G_n^-\le(A_n-G_n)+2^{1-n}.
   \]
   The exact positive AGM theorem makes the right side tend to zero;
   both denominator endpoints tend to the same M_AGM>=b>0. The pi
   endpoints also converge. Thus (13) encloses the total period and its
   actual rational width tends to zero. This proves the outer search
   terminates after the separately terminating finite refinements. It
   does not assume interval nesting or a numerical convergence heuristic.

7. **Signed division, integer existence and integral extension.** Eventually
   V's lower bound exceeds Omega(E)/2, while the containing U_j remain
   bounded. Equation (14) then bounds every quotient's distance from
   the true value by a quantity tending to zero. Taking all four endpoint
   quotients is valid for either sign and for intervals crossing zero.
   The resulting closed interval contains F(x_j) and has shrinking
   width. L048 supplies the same fixed positive integer K for every
   stage and generator, so existence of an integer in K J_j precedes
   any rounding test. Width strictly less than one excludes two distinct
   integers, even at endpoints. Hence ceil(K inf J_j)=floor(K sup J_j)
   terminates and equals K F(x_j). In the zero case every interval
   contains zero, so the identical test returns zero. With finitely
   many generators all searches finish; zero has reduced denominator
   one and the empty list has lcm one. Additivity and integral generation
   give the claimed common denominator on M, rather than on M tensor Q.
   Agreement with the genuine functional forces all relations; it does
   not verify that a supplied list really generates M.

L048 remains the only direct local mathematical input. Its qualified
named Kenku and Manin imports are retained without a new verification
claim. The reopened primary passages are the already approved ones;
no further literature assessment or mathematical script was needed.
The audit validates a theoretical known-method recovery input. It gives
no executable certificate, practicable precision bound, actual normalized
table or coefficient. The granting of exact conductor/newform arithmetic
and complete integral paths, and all remaining BSD gaps, are unchanged.

## Mathlib

Full matching arbitrary-relative exact normalized recovery: not checked.
Supporting cusp equivalence/Hecke transport, certified complex Fourier
tails, target real-period identities, positive AGM convergence and Sturm
isolation: not checked. Rational interval arithmetic, elementary Taylor
remainders, integer isolation and lcm support: not checked. No absence
claim or generic software correctness follows. Precise primary imports
and the assembly above are the evidence; there is no numerical experiment
or formal verification claim.
