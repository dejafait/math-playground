# C467u — Actual incidence signs and the prescribed adjacent matching obstruction

## Hypotheses

Retain the actual data and matching class of C467t, including its
conditional obstruction, with

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128.
\tag{1}
\]

In particular, B is the conjugation-normalized logarithm of
h(w)=xi(1/2+sqrt(w))/xi(1/2) on |w-1|<R, and

\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
G(y)=\operatorname{Re}g(iy),\quad J(y)=\operatorname{Im}g(iy),
\]
\[
\theta(y)=-3\operatorname{Im}\beta(iy),\qquad
E(y)=J''(y)-3G''(y)\tan\theta(y).
\tag{2}
\]

Use C467e's actual analytic bound |beta''|<40 on |z|<R.
The fixed real smooth bump satisfies 0<=f<=1, f=1 on
[-b_*,b_*], and supp f contained in (-2b_*,2b_*).
Neither f nor beta is assumed even.

Use L018's critical-strip zero correspondence, L021's imaginary-axis
positivity, and L024's unconditional paired product, including its
reciprocal-square summability and multiplicity convention. Also retain
the **finite-zero input recorded in C466a**: the nontrivial zeros with
positive ordinate at most 100 are accounted for on the critical line,
the first ordinate lies in (14,15), and at least one such zero exists.
The exact source locator is Suvrit Sra, *On some positivity properties
of the Riemann Xi function*,
[version-specific primary text W_pr5z5huy_v1, section 2.1, equations
(6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1), as recorded and
qualified in C466a and its source assessment882/audit883. The underlying
finite verification and first-zero isolation remain cited external
inputs, not independently replayed certificates here.

This uses the recorded exclusion of lower positive ordinates, whereas
C467q's nontriviality argument needed only existence of one zero.
That distinction is essential. No new zero-free region, counting
estimate, assertion about higher zeros being on the line, reciprocal
density theorem, or RH is assumed. Raw time, the original divisor,
the common minus sign, H/H0/F and C467r's selected trace are unchanged.

## Conclusion

For every |y|<=X,

\[
\operatorname{Re}B'''(1+iy)>0,\qquad
\operatorname{Re}B''''(1+iy)<0,\qquad G''(y)<0.
\tag{3}
\]

For 0<|y|<=X,

\[
G(y)<0,\qquad \operatorname{sgn}J''(y)
=\operatorname{sgn}\theta(y)=\operatorname{sgn}E(y)
=\operatorname{sgn}y.
\tag{4}
\]

There is y0 in (-2b_*,-b_*) with

\[
E(y_0)<0,\qquad (f^3)'(y_0)G(y_0)G''(y_0)>0.
\tag{5}
\]

Consequently C467t excludes the entire nominated matching class on
every positive common time interval: C467r's fixed lambda=1 radial
trace cannot be matched by an admissible adjacent j=1 triangle, even
before imposing its upper-pair match. This conclusion retains the
external finite-zero qualification above. Conceptual audit1062 below,
together with its audit of C467t's incidence/continuous-vertex argument,
validates this qualified class stop.

The exclusion concerns that fixed selected trace and the nominated
continuous test class. It does not exclude other selections, geometries
or weaker test classes. Global signed assembly, exterior payment,
realization, all degrees and actual-Xi transfer remain open. This is
not an RH candidate or a certified originality claim.

## Proof

### Gate, imported inputs and comparison with earlier stops

The invocation-start assessment is the unchanged EXPLORE target in
`drafts/literature/2026-11-16-adjacent-triangle-matching-nomination-1056.md`,
approved separately in review1057. The actual incidence/bump-overlap
test is part of its characteristic-compatibility obligation. We reuse
its source comparison and the already recorded source assessment882
for C466a's qualified inputs. No new assessment is approved in this
research step, and no primary source is claimed newly inspected.

L024 already proves the full paired product with the finite-order
hypothesis checked; its supporting reference is the standard named
Hadamard factorization theorem,
[UCL introductory analytic number theory notes, Theorems 7.5 and
7.7](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf).
We import that local theorem rather than reprove factorization.
The new application is an elementary sector bound for its differentiated
factors, followed by the sign integrations in (2). The product and
finite verification are known inputs, not new mathematical discoveries.

C467s/stop1058 excludes only the selected conjugate construction.
C467q's stop imposes a single physical-vertex value, which is absent
here. C467t already supplies the appropriate weaker conditional
obstruction. The local duplicate/failure check found no completed
actual E-sign test in those results or the relevant November16
assessments. This bounded comparison does not certify novelty.

### The actual zero factors lie in a sufficient sector

L021 implies xi(s)>0 for real s, since
xi(s)=Xi(-i(s-1/2)). Thus there are no zero-ordinate exceptions.
The finite-zero input and conjugation then imply |Im rho|>14 for
every zero rho of xi, as well as existence of at least one zero.
L018 gives

\[
\rho=1/2+\delta+i\gamma,\qquad |\delta|<1/2,\quad |\gamma|>14.
\tag{6}
\]

Write alpha_j for L024's representatives of the pairs of Xi zeros,
and put omega_j=-alpha_j^2. Substituting z=-i sqrt(w) into its even
product gives

\[
h(w)=\prod_j(1-w/\omega_j),\qquad
\sum_j|\omega_j|^{-1}<\infty.
\tag{7}
\]

The identity is independent of the square root. Each omega_j is a
zero of h, with its multiplicity, and equals (rho-1/2)^2 for a
corresponding zero rho of xi. The two reflected rho's produce the
same omega; they are not counted twice. No reality of omega_j is
asserted. This is the same representative convention as L024.

For w=1+iy, |y|<=X, and omega=(delta+i gamma)^2 set

\[
D=w-\omega=A+iC,\qquad
A=1-\delta^2+\gamma^2>\gamma^2+3/4,
\quad C=y-2\delta\gamma.
\tag{8}
\]

We have |C|<=|gamma|+X, and

\[
A-8|C|>
|\gamma|(|\gamma|-8)+3/4-8X
>84+23/32>0.
\tag{9}
\]

Here X=1/256 and |gamma|>14. In particular |C|/A<1/8.
If v=C/A, elementary reciprocal powers give

\[
\operatorname{Re}D^{-3}
=A^{-3}{1-3v^2\over(1+v^2)^3}>0,
\]
\[
\operatorname{Re}D^{-4}
=A^{-4}{1-6v^2+v^4\over(1+v^2)^4}>0.
\tag{10}
\]

Indeed the respective numerators are greater than 61/64 and 29/32.
These strict bounds apply to every factor, including any nonreal
zeros and every multiplicity. They are not a numerical check of
finitely many terms or an assumed cancellation of conjugate tails.

### Differentiating the product with a complete convergence bound

Every |omega_j|=delta^2+gamma^2>196. On the original B disk,
|w|<5/4, so |w-omega_j|>|omega_j|/2 and |w/omega_j|<1/2.
Use the analytic power-series logarithms log(1-w/omega_j).
Their sums, and for each fixed m>=1 their m-th derivative sums,
converge absolutely and uniformly on compact subsets of the disk.
For the derivatives a sufficient majorant is

\[
\sum_j|w-\omega_j|^{-m}
\le 2^m 196^{1-m}\sum_j|\omega_j|^{-1}<\infty.
\tag{11}
\]

The logarithm series itself is dominated by
2|w| sum_j |omega_j|^{-1}. Its exponential is (7), so it differs
from B by at most a constant logarithm branch. Uniform holomorphic
convergence and the Cauchy formula justify differentiation. Thus

\[
B^{(m)}(w)=(-1)^{m-1}(m-1)!
                 \sum_j(w-\omega_j)^{-m}\quad(m\ge1).
\tag{12}
\]

There is no unaccounted exponential factor in (7), by L024's paired
product. Absolute convergence permits taking real parts term by term.
Apply (10) to m=3 and m=4 in (12). Every summand has positive real
part, and the nonempty zero set makes the sum strictly positive.
The respective multipliers +2 and -6 prove the first two signs in
(3). No zero-count or tail asymptotic is needed for this argument.

### Sign propagation to E on both bump transitions

The chain rule and real Taylor coefficients give exactly

\[
G''(y)=-\operatorname{Re}B'''(1+iy)<0,\quad
G(0)=G'(0)=0,
\]
\[
J''(y)=-\operatorname{Im}B'''(1+iy),\quad
J'''(y)=-\operatorname{Re}B''''(1+iy)>0,\quad J''(0)=0.
\tag{13}
\]

The first line implies strict G(y)<0 for every y!=0 in this
interval. For example Taylor's integral formula writes
G(y)=y^2 integral_0^1 (1-u)G''(uy) du, which is strictly negative
for either sign of y. The second line implies that J'' has the
strict sign of y, by integration from zero.

Moreover theta'(y)=-3G(y), theta(0)=0. Hence theta has the strict
sign of y. Taylor's integral estimate from |beta''|<40 and
beta(0)=beta'(0)=0 gives

\[
|\theta(y)|\le3|\beta(iy)|\le60y^2
\le60/65536<1/16<\pi/2.
\tag{14}
\]

Thus tan(theta) has the same sign as y. Since -3G''>0, both
terms J'' and -3G''tan(theta) in E have that strict sign. This
proves (3)–(4), with E(0)=0. It controls the entire fixed mean
interval, rather than just an unspecified neighborhood of zero.

### The fixed bump necessarily meets the outgoing part

Put F_b=f^3. The support and plateau assumptions imply
F_b(-2b_*)=0 and F_b(-b_*)=1. The mean value theorem gives some
y0 in (-2b_*,-b_*) with F_b'(y0)=1/b_*>0. This interval lies
strictly in (-X,0). Equations (3)–(4) give E(y0)<0 and both
G(y0), G''(y0)<0, proving (5). No symmetry or monotonicity of
the bump was required.

Now apply C467t(5)–(7),(18)–(20) at this y0. Its outgoing-vertex
argument forces every admissible adjacent test's shared vertex
value, and its comparison with C467r's fixed selected value gives

\[
\psi_r(t,x(t,y_0),0,1)-\psi_1(t,x(t,y_0),0,0)
=c_*t^{5/2}+O(t^3),
\]
\[
c_*={8\over5\sqrt6}(f^3)'(y_0)G(y_0)G''(y_0)
                         \sec^2\theta(y_0)>0.
\tag{15}
\]

For all sufficiently small t>0 the difference is strictly positive.
C467t's mean-chart margins put x(t,y0) inside the original x box.
Every positive proposed common interval contains such times. This
contradicts the prescribed radial equality and proves the exclusion.

The argument uses only necessary continuity, initial-data and interior
transport conditions from the nominated class. Its four complex L1
products on each piece, complete independent-cutoff identities and
upper-pair equality cannot repair a contradiction already forced by
those necessary conditions. No face, corner distribution or original
divisor has been removed to obtain a positive matching assertion.
There is no new adjoint construction in this step.

The original construction imported (15)'s necessary-trace premise from
then-unaudited C467t; its sign calculation alone did not validate that
premise or the underlying C467s residual. The separate audit below
and C467t's audit1062 now check that chain as well as (6)–(14).

### Conceptual audit — 16 November 2026, step1062

This is a REPRODUCTION audit under the unchanged invocation-start
SPECIALIZE assessment
`drafts/literature/2026-11-16-adjacent-incidence-obstruction-audit-nomination-1060.md`,
approved separately in review1061. It imports L018/L021/L024 and the
qualified finite-zero input above, and checks their actual specialization.
No finite-zero certificate, general factorization theorem or transport
theory is independently reproved. The original construction's claim of
a qualified stop is validated, not promoted to a new literature discovery.

**Exact low-zero scope and product.** L021 gives xi(s)>0 for every
real s via Xi(-i(s-1/2)); hence there are no zero-ordinate exceptions.
The carried source input accounts for all positive ordinates through
100 and locates the first in (14,15), so, using conjugation, every
xi zero satisfies |gamma|>14. Existence of a single known zero would
not imply this universal exclusion. The primary locator remains Sra
v1, section2.1, (6)–(8), cited in the hypotheses and qualified in
assessment882/audit883 and review1061. Platt–Trudgian's all-zero
verification by itself is not being substituted for the first-zero
enclosure. These remain external cited inputs.

For a paired Xi zero alpha, rho=1/2+i alpha and
omega=-alpha^2=(rho-1/2)^2. The two Xi zeros alpha and -alpha
map to the same omega, with the multiplicity of either, because
alpha!=0. Thus L024's representative convention gives exactly (7),
and sum |omega|^(-1)=sum |alpha|^(-2)<infinity. Substitution into
the locally uniform even product is legitimate on compact w sets:
both choices of the square root give the same factors, and their
z values lie in a fixed compact disk. L024 already excluded a linear
or quadratic exponential factor in Xi using its order and normalization;
none is introduced by this substitution.

For every factor, |omega|=delta^2+gamma^2>196. On the entire
original disk |w-1|<1/4, |w|<5/4 and
|w-omega|>|omega|/2. Thus (11), multiplied by the fixed
factorial (m-1)!, dominates the full m-th derivative series for
every fixed m>=1, and 2|w| sum |omega|^(-1) dominates the
logarithm series. This proves locally uniform holomorphic convergence
without a zero-density estimate or an omitted infinite tail. The
summed logarithm and B have the same exponential, hence differ by a
constant on the connected disk. Cauchy differentiation gives (12),
with multipliers +2 for m=3 and -6 for m=4.

The strip bound |delta|<1/2 and |gamma|>14 give the full
sector comparison A-8|C|>84+23/32, uniformly for |y|<=X.
For v=C/A the real reciprocal-power numerators are exactly
1-3v^2 and 1-6v^2+v^4; their respective lower bounds are
61/64 and 29/32. Absolute convergence permits their real parts
to be summed. Every contribution is positive, and the zero set is
nonempty, so the sums are strictly positive. This verifies both
strict derivative signs in (3), including multiplicities and possible
off-line higher zeros; no RH assumption enters the sector argument.

**Signs, fixed bump and class exclusion.** Direct differentiation
gives G''=-Re B''', J''=-Im B''' and J'''=-Re B''''.
Conjugation and the subtraction defining g give
G(0)=G'(0)=J''(0)=0. Thus G''<0 implies G<0 away from zero,
and J'' has the strict sign of y. Also
theta'=-3 Re beta'(iy)=-3G and theta(0)=0, so theta has the
same strict sign. The original analytic bound gives
|theta|<=60y^2<=60/65536<1/16, ensuring the same sign for
tan(theta). Since -3G''>0, both summands of E have that sign.
This checks E<0 on the whole negative bump transition, not merely
at an unspecified sufficiently small mean.

For F_b=f^3 the fixed endpoints are F_b(-2b_*)=0 and
F_b(-b_*)=1. The mean value theorem therefore supplies
F_b'(y0)=1/b_*>0 at some y0 in (-2b_*,-b_*). This interval
lies strictly inside (-X,0), even when f is asymmetric or has
additional oscillations. The preceding signs give (5) with a strict
positive product. C467t's separately checked outgoing argument and
selected-trace discrepancy now give (15), with c_*>0 and a finite
O(t^3) constant for this fixed bump and mean. Therefore the difference
is positive for every sufficiently small t>0; no effective lower
bound for the common time or for c_* is needed or asserted.

Every positive proposed interval contains such times. Any nominated
solution would satisfy the continuity, interior equation, initial data
and fixed radial equality already contradicted here. Additional
upper-pair matching, integrability and cutoff conditions cannot remove
that necessary-condition contradiction. No choice of unknown upper
data or extra vertex differentiability was used. The conclusion is
exactly the qualified fixed-C467r class stop. Jointly selecting other
traces, changing geometry or changing regularity remains outside its
scope; global assembly and actual-Xi positivity are still unproved.

All audit obligations pass. C467s's graph/discrepancy passage is used
only as verified in C467t's audit; its full reflected pair construction
and cutoff proof remain unaudited. This audit uses no numerical preview,
mathematical script, cross-notebook theorem or new zero-free estimate.

## Mathlib

Full coverage of the actual incidence-sign and prescribed-matching
obstruction was not checked. L018/L021/L024 and C466a/C467e/C467t
retain their supporting-coverage qualifications. Hadamard factorization
is imported through L024; locally uniform holomorphic differentiation,
the chain rule, integral Taylor formula and mean value theorem have
the explicit roles above. No matching Mathlib theorem is claimed
present or absent. No mathematical script, numerical preview or
finite certificate is used to replace the proof of the infinite sum.
