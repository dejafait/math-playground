# C020d — Primitive source ratios retain large additive moduli

## Hypotheses

Use exactly C020c's fixed witness, coefficients, scales, own heat times,
floors and intervals, as positive integers d tend to infinity. In
particular q=log X, B=(sqrt(2)-1)X, h=3*pi/q,
R=floor(X^(1/1000))^4, N*=N(sqrt(2)X), and the distinct witness
primes p1<p2 lie in [sqrt(X)/10,sqrt(X)/5]. Put v=p1*p2.
Keep the original c_r from all four tapered factors; r,s range up to R.
The elementary asymptotics in C019/C019y give

\[
 N_*/\sqrt X\longrightarrow c_*:=\sqrt{\sqrt2/(2\pi)}<1/2,
 \qquad R< p_1<p_2,\qquad p_1p_2>N_*
 \tag{1}
\]

eventually. The first limit also follows immediately from the exact
formula for N and d comparable to X^2q^2. All conclusions below have
an absolute existential onset, unless an additional fixed parameter
is specified. No RH, actual-P estimate or nonvanishing is assumed.
The inherited C019 quadrature, C019y finite identities and C020c
mixed reduction passed scoped conceptual audit1421. Separate resonant
sign estimates and actual-P contracts are not certified by that audit.

## Conclusion

There is a complete finite regrouping of the mixed expression

\[
 \mathcal M=2\operatorname{Re}\int_D W^2(CA+C\overline A)
\]

by primitive ratios m/n=a/b, given in (5)-(7), with the same inherited
error O(X^(63/125)q^2)=o(B). Every clipped Fresnel integral, boundary
correction, remote endpoint and original coefficient remains in it.
The regrouping is not an evaluation of its arithmetic sums.

For each coprime positive pair a,b and each r,s, put

\[
 g_0=\gcd(ar,bs),\quad \mathsf A=ar/g_0,\quad
 \mathsf D=bs/g_0,\quad f=\gcd(\mathsf D,v),\quad
 Q=\mathsf D/f.
 \tag{2}
\]

The actual reduced additive phase is
e(-mathsf A*(v/f)/Q), with e(t)=exp(2*pi*i*t). Exactly the following
common-factor cases suffice:

\[
 f=\gcd(b,v)\in\{1,p_1,p_2\};\qquad
 Q\le N_*R\quad(f=1),\qquad Q\le4R\quad(f>1).
 \tag{3}
\]

The upper range in the first case cannot be replaced by X^(1/3)
merely by retaining the source floors and stationary interior.
For every witness pair that is present, (9) constructs an admissible
tuple with r=s=1, f=1 and

\[
 \sqrt X/200<b=Q\le\sqrt X/100,
 \quad m=a, n=b,\quad
 x=2\pi m v/n\in[11X/10,13X/10]\subset D
 \tag{4}
\]

eventually. Both sources are present throughout D. This is a statement
about the exact tuple support and reduced phases, not a lower bound
for the sum or even its high-modulus portion. No distribution theorem
for witness primes is needed: the construction works for each pair
in the original sum, and makes no assertion about their count.

Thus the direct use of the inspected prime-product additive-average
theorem after this grouping lacks its required modulus range, as well
as its required weight specialization. The exact unpaid high-modulus
expression is (10); it need not be negligible and could have a main
term. The inverse-phase alternatives have not been produced by this
regrouping. No full quotient bound, M2 decision or Xi positivity follows.

## Proof

### Complete grouped kernel with the original endpoints

Uniquely write m=k*a, n=k*b, with (a,b)=1 and
1<=k<=K_ab:=floor(N*/max(a,b)). Then
kappa=m*v*r/(n*s)=a*v*r/(b*s)=mathsf A*v/mathsf D does not
depend on k. Neither the heat amplitudes nor the source entries are
independent of k. For each tuple use exactly C020c (4):

\[
 J_0=[\max(X,\rho_{ka},\rho_{kb}-h),\sqrt2X-h],
 \quad J_1=[\max(X+h,\rho_{kb}+h,\rho_{ka}),\sqrt2X],
\]
\[
 \beta_0(Z)=E_{ka}(Z)\overline{E_{kb}(Z+h)}a_v(Z),
 \quad\beta_1(Z)=E_{kb}(Z-h)\overline{E_{ka}(Z)}
                                      \overline{a_v(Z-h)}.
\]

Here rho_j is the positive source-entry root defined in C020c, not
a zero of zeta. Empty intervals contribute zero, including to every
functional below. Let x=2*pi*kappa and

\[
 \phi(Z)=Z\log(Z/x)-Z-\pi/4,
 \qquad\Psi(Z)=\phi(Z)+x+\pi/4=Z\log(Z/x)-Z+x.
\]

Define a complex functional T_kappa[beta;J] as follows. If
X/2<=x<=2X, retain C020c's quadratic coordinate z=sgn(Z-x)*sqrt(Psi(Z)),
inverse Z(z), and removable value at z=0 in

\[
 r_\beta(z)=
 \frac{\beta(Z(z))Z'(z)-\sqrt{2x}\beta(x)}{2iz}.
\]

For J=[u,w] set

\[
 T_\kappa[\beta;J]
 =\sqrt{2x}\beta(x)\int_{z(u)}^{z(w)}e^{iz^2}\,dz
       +[r_\beta(z)e^{iz^2}]_{z(u)}^{z(w)}.
 \tag{5}
\]

For x outside [X/2,2X], instead set

\[
 T_\kappa[\beta;J]
       =[\beta(Z)e^{i\Psi(Z)}/(i\log(Z/x))]_{u}^{w}.
 \tag{6}
\]

The denominator is separated from zero on either nonempty source
interval in this remote case. These are precisely the original
positive-phase quadrature functionals after multiplication by
exp(i*x+i*pi/4). In particular (5) retains its boundary correction;
(6) retains both remote endpoints. C019 (13)-(14), specialized to
J1 as in C020c Section 2, supplies the total o(B) quadrature error.
There is no new oscillatory estimate here.

For each a,b,r,s,v define the joint weight

\[
 \mathcal K_{abrs}(v)=
 \frac{2c_r\overline{c_s}e^{-i\pi/4}}{\sqrt{abvrs}}
 \sum_{k=1}^{K_{ab}}\frac1k
 \left\{(kb)^{ih}T_\kappa[\beta_0;J_0]
 +(ka)^{-ih}\kappa^{ih}T_\kappa[\overline{\beta_1};J_1]\right\}.
\]

Then the promised complete regrouping is

\[
 \mathcal M=
 \operatorname{Re}\sum_{\substack{a,b\le N_*\\(a,b)=1}}
 \sum_{r,s\le R}\sum_{v}
 e(-\mathsf A v/\mathsf D)\mathcal K_{abrs}(v)
           +O(X^{63/125}q^2).
 \tag{7}
\]

To check the conjugations in (7), C020c (5) gives, before quadrature,
two integrals with opposite phases and respective coefficients
c_r*conj(c_s)*(kb)^(ih) and
c_s*conj(c_r)*(ka)^(ih)*kappa^(-ih), divided by
k*sqrt(abvrs). Inside the real part, replace the entire second
term by its conjugate. Its coefficient becomes
c_r*conj(c_s)*(ka)^(-ih)*kappa^(ih), its amplitude becomes
conj(beta1), and its phase becomes +phi. Both integrals therefore
have the common factor exp(-i*x-i*pi/4), yielding (7).
The map (m,n)<->(k,a,b) is bijective and every sum is finite.
C019 (14) pays the quadrature errors before or after regrouping.

This uses the original center amplitudes from C020c (5), rather than
performing its separately paid O(h/sqrt(X)) replacement. Consequently
(7) represents the entire mixed expression in C020c (2), up to the
same stated error, including its Fresnel mismatch and both endpoint
sums. It does not identify the two domains or delete any portion of
the matched formula. Factoring out a center phase also from (6)
does not make its remaining endpoint weights slowly varying; the
factors e^(i*Psi(endpoint)) remain inside K.

### All common-factor cases and the actual reduced modulus

Since (mathsf A,mathsf D)=1, reducing mathsf A*v/mathsf D cancels
exactly f=gcd(mathsf D,v). No gcd condition on a with r,s or on b
with r,s was imposed; all such factors are already in g0. A witness
prime p exceeds both r and s by (1). If p divides b, it does not
divide a, so it does not divide ar or g0; thus it divides mathsf D.
Conversely p|mathsf D implies p|bs, hence p|b. Since v is squarefree,
this proves f=gcd(b,v). The case f=v would force v|b<=N*, contradicting
(1). Common witness factors in k cancel from m/n and remain in the
k-dependent weight; they are not excluded from the sum.

If f=p_i, write b=p_i*t. Eventually N*/p_i<5, so t<=4, and

\[
 Q=bs/(g_0p_i)=ts/g_0\le4R.
 \tag{8}
\]

If f=1, Q=bs/g0<=N*R. These cases exhaust the actual tuples;
in particular no assumption of coprimality with witness primes was
silently added. Formula (7) may be partitioned by these cases with
all of K retained.

### A supported interior stratum above the inspected modulus range

For sufficiently large X put

\[
 b=2^{\lfloor\log_2(\sqrt X/100)\rfloor},\qquad
 a=\text{a nearest positive odd integer to }
       \frac{(6X/5)b}{2\pi v},\quad k=r=s=1.
 \tag{9}
\]

The nearest-odd choice has error at most one (either choice at a
tie works), and is positive eventually. Since X/100<=v<=X/25,

\[
 a\le(60/\pi)b+1\le\frac{3}{5\pi}\sqrt X+1,
 \qquad \sqrt X/200<b\le\sqrt X/100.
\]

Both a and b are strictly below sqrt(X/(2*pi)) with a fixed
constant margin for large X, hence below N(X). Monotonicity of
N(Z) puts them inside both original floors throughout D. In fact
J0=D and J1=D+h for this tuple. Also (a,b)=1, v is odd eventually,
g0=1, f=1 and Q=b. The center satisfies

\[
 |x-6X/5|\le2\pi v/b\le16\pi\sqrt X.
\]

This proves (4) for a sufficiently large absolute onset, including
the upper endpoint sqrt(2)X-h. The unshifted prefactor c1*conj(c1)
is exactly 1. In the matched notation the real shift phase is
tau=h*log(b/sqrt(v))=O(1/q), since 1/40<b/sqrt(v)<=1/10, and
gamma_v tends uniformly to 2. Thus no coefficient-support rule,
source-entry exclusion or large shift-phase convention removes
these tuples. No nonzero lower bound for their signed contribution
is inferred; interference with all other tuples remains possible.

### First unpaid expression and precise source comparison

For any fixed Lambda>0 set Q_*=X^(1/3)q^(-Lambda). Define the
following part of the complete grouped sum, without deleting its
weights or replacing its endpoints:

\[
 \mathscr R_>(X)=\operatorname{Re}
 \sum_{\substack{a,b\le N_*,\ (a,b)=1\\r,s\le R}}
 \sum_{\substack{v\\\mathsf D/\gcd(\mathsf D,v)>Q_*}}
 e(-\mathsf A v/\mathsf D)\mathcal K_{abrs}(v).
 \tag{10}
\]

By (8), the high-modulus part has f=1 eventually, but by (9) it
contains admissible interior tuples with Q asymptotic in scale to
sqrt(X). Their Q/Q_* is at least X^(1/6)q^Lambda/200, tending to
infinity. This is an actual modulus calculation, not an inference
from the upper bound N*R alone. It gives no lower bound on (10).

The reused source comparison is Bazin, *A Bombieri–Vinogradov theorem
for exponential sums over products of k primes*, arXiv:2607.15137v1,
Theorem 2, equation (3), and Section 2, Lemma 6, equations (9)-(11),
https://arxiv.org/html/2607.15137v1 . As inspected in source-notes1418,
the theorem concerns f_k=1_{Omega(n)=k}, averaged over reduced
moduli up to z^(1/3)(log z)^(-b(C)), with
|lambda|<=Q^(-3)(log z)^(-b(C)) and
1<=k<=(2-epsilon)log log z. It retains divisibility main terms.
For our product length z comparable to X and lambda=0, (9) falls
outside that modulus range for any fixed logarithmic loss. Independently,
the separate prime windows, the weight K and repeated outer sums
are not its f2 coefficients. Even the low-modulus part of (7) has
not been justified by that theorem. Enlarging the source length does
not by itself supply the required o(Xq^2) weighted error.

The other reused source is Bettin–Chandee, *Trilinear forms with
Kloosterman fractions*, arXiv:1502.00769v1, Theorem 1/(1.2),
Remark 1/(1.3), Sections 6-7,
https://arxiv.org/html/1502.00769v1 . It estimates an inverse phase
e(vartheta*a*inverse(m)/n) with separate sequence norms and explicit
coprimality. Merely relabeling ar/(bs) in (7) does not produce that
phase or separate K. No source theorem is imported to estimate (10),
and no source theorem is reproved. The local proof above is the
finite algebra and specialization required to test applicability.

The bounded attempt stops here: there is no established explicit
main form for (10) with remainder o(Bq^2), and no justification for
setting it to zero. The matched low-modulus part and endpoint weights
are also unpaid. This stops only the direct application of the
inspected additive-average theorem after primitive-ratio grouping;
a further valid transformation could change the situation. The
complete quotient still retains C019y's O(G,J), UA, denominator and
E_P terms. The all-degree Xi gap remains independent.

### Conceptual audit1421 of the complete grouping and modulus cases

18 November 2026. The audit retains (1)--(10), including the original
joint weight and the qualified applicability stop. It invokes the
audited quadrature only, not an arithmetic cancellation theorem.

For each positive pair m,n<=N*, k=gcd(m,n), a=m/k, b=n/k is
the unique triple with (a,b)=1 and k<=floor(N*/max(a,b)). The
original denominator sqrt(mn*v*r*s) is k*sqrt(ab*v*r*s), which
accounts for the full 1/k in K. The floors, heat amplitudes and
entry domains still depend on k and remain inside that weight.
In particular no summation over k is replaced by a constant mass.

In the near range, phi(Z)=Psi(Z)-x-pi/4 and (5) multiplied by
exp(-i*x-i*pi/4) is exactly C019's positive quadrature on J_j.
The same identity holds for (6) in the remote range. For the second
integral in C020c (5), conjugate the entire coefficient and integral
inside Re; the result has coefficient
c_r*conjugate(c_s)*(ka)^(-ih)*kappa^(ih), amplitude conjugate(beta1),
and positive phase. Both terms now have the factor
exp(-i*x-i*pi/4); exp(-i*x)=e(-A*v/D) with the sans-serif
A,D of (2). This proves precisely the common factor and weight
in (7). Complex linearity of the positive quadrature and its
definition under conjugation justify the same operation on its
boundary terms. Empty and singleton domains give zero throughout.
No center-amplitude matching or full-Gaussian replacement is used.

C019's absolute coefficient/error payment precedes regrouping and
is unchanged under this finite bijection. Hence the error remains
O(X^(63/125)q^2); neither an additional multiplicity factor nor an
unproved cancellation is needed. The phases e^(i*Psi(endpoint))
in the remote weights remain present after center-phase extraction.
This audit supplies no regularity or separation norm for K.

For the gcd cases, gcd(A,D)=1 by definition of g0. A witness prime
p>R divides D=bs/g0 exactly when it divides b: if p divides b,
coprimality of a,b and p>r rule out p|ar and hence p|g0; conversely
p|D implies p|bs and p>s rules out p|s. Since v is squarefree,
f=gcd(D,v)=gcd(b,v). The possibility f=v is excluded by b<=N*<v.
After cancelling f, gcd(A*(v/f),D/f)=1, so Q is the reduced
denominator, rather than just a possible modulus. If f=p_i,
b=p_i*t with t<5 because N*/sqrt X tends to
sqrt(sqrt(2)/(2*pi))<1/2 and p_i>=sqrt X/10; thus t<=4.
This verifies both bounds in (3) without excluding common factors
in k, r or s.

In (9), b is a power of two and a is odd; hence (a,b)=1.
Eventually v is odd, so f=1. The nearest-odd error is at most one,
and the inequalities displayed after (9) put a,b below N(X) with
a fixed constant margin. Consequently J0=D and J1=D+h exactly.
The center error bound 16*pi*sqrt X is o(X); it puts x inside
[11X/10,13X/10] and below sqrt(2)X-h at one common onset.
Thus the claimed Q=b>sqrt X/200 support survives all floors,
coprimality conditions and the band cutoff. The coefficient c1 is
1, but no lower bound on the joint weight or on the signed sum is
inferred. For fixed Lambda>0, 4R<Q_* eventually, whereas these
tuples have Q/Q_*>X^(1/6)q^Lambda/200 tending to infinity.
This verifies the support statement used in (10) and the existing
failure of the direct modulus-range application. The arithmetic
source comparisons of review1418 are reused within their stated
scope; no broader impossibility assertion is made.

## Mathlib

Full matching coverage for this exact moving-heat grouped kernel has
not been checked. Elementary gcd parametrization, finite-sum bijections
and conjugation are supporting facts, not a formalization of the
uniform quadrature input or the missing weighted arithmetic estimate.
This finite regrouping and its modulus obstruction are local progress,
not a claimed advance beyond the inspected literature. The grouping
and its stated analytic inputs passed the scoped conceptual audit1421
above. Full arithmetic evaluation and actual-P transfer remain open.
