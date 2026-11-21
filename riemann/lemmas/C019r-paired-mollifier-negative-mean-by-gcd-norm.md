# C019r — Fixed paired-mollifier negative mean via a common gcd norm

## Hypotheses

Use exactly C019m's real, positively normalized actual Jensen value
P and C019p/q's elementary reference V, scales and mollifier. In
particular d tends through positive integers, T>2*pi*e satisfies
d=(T/(2*pi))(log(T/(2*pi))-1), and

\[
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,\quad
 h=3\pi/q,\quad J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h].
\]

Put t(Y)=Y^2/(2d), ell(Y)=log(Y/(2*pi)), u(Y)=ell(Y)/2,
c_0=pi/8 and

\[
 N(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor,
 \qquad L=\lfloor X^{1/1000}\rfloor,\qquad K=L^2.
\]

The coefficients alpha(n) are those of the Euler-product branch of
zeta(s)^(-1/2) on Re(s)>1; omega(n)=log(L/n)/log L for n<=L.
Retain, with no change of taper or length,

\[
 M(Y)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-iY},\qquad
 W(Y)=|M(Y)M(Y+h)|^2.
\]

Write b_k=sum_{uv=k;u,v<=L} alpha(u)alpha(v)omega(u)omega(v)v^(-ih)
and beta_k=k^(ih/2)b_k. C019q proves that beta is real and
|beta_k|<=1. Also beta_1=b_1=1. Both actual Jensen factors and both
reference factors retain their own time, floor and normalization.

All assertions are beyond one absolute existential integer onset.
The proof uses the local reductions C019p/q with their stated
qualifications. Independent conceptual audit1401 below retains those
reductions and this development. No RH, random law, simple-zero, nonvanishing or
critical-line reciprocal hypothesis is imposed.

## Conclusion

Define the positive quadratic norm

\[
 A=\sum_{k,l\le K}\frac{\beta_k\beta_l\gcd(k,l)}{kl}.
                                                               \tag{1}
\]

Then the full reference pair and the two weighted squares satisfy

\[
 \int_D V(Y)V(Y+h)W(Y)\,dY\le-\frac{BqA}{50},\qquad
 Q_0+Q_h\le C XqA+CX^{451/500},                              \tag{2}
\]

where Q_j=integral_D V(Y+j)^2 W(Y)dY. Moreover

\[
 A\ge\frac1{3(1+\log K)},\qquad
 \left|\int_D(P(Y)P(Y+h)-V(Y)V(Y+h))W(Y)\,dY\right|
       =o(BqA).                                             \tag{3}
\]

Consequently the fixed test (M1) holds, with for example c=1/2:

\[
 \int_D P(Y)P(Y+h)W(Y)\,dY
       \le-\frac{BqA}{100}\le-\frac B2.                     \tag{4}
\]

The transfer in (3) is smaller than the proved negative margin, as
allowed by the assessed test. It is not a claim of o(B) transfer or
of A=O(1/q). Neither Q=o(Xq) nor the separate O(B) squared mass of
the weighted pair is asserted. Quantitative pair density, ordered root
selection, the exceptional-root deficit and RH remain unresolved.
Independent conceptual audit1401 retains this local result. It is not
a stronger bound than the original claim or a certified originality claim.

## Proof

### Scope, imported estimates and eventual scales

This attempts exactly the prior EXPLORE target in
`drafts/literature/2026-11-17-jensen-paired-mollifier-mean-test-1394.md`,
separately approved1395. It uses the inspected classical estimates
through C019p/q: H. Kösters, *On the Occurrence of the Sine Kernel in
Connection with the Shifted Moments of the Riemann Zeta Function*,
5 September2008, [arXiv:0803.1141v2, Appendix A, Lemmas A.1--A.3](https://arxiv.org/html/0803.1141v2#A).
A.1 requires a monotone first derivative of one sign and separated
from zero; A.2 requires a second derivative of one sign and separated
from zero; A.3 concerns the ordinary integer logarithmic-index sum.
These are Titchmarsh, *The Theory of the Riemann Zeta-function*,
second edition, Lemmas4.2,4.4,7.2. They are not reproved here.
The zero-shift square use below checks the changed phases and entries.
No uninspected Selberg mollified-moment theorem is imported.

C019l's exact scales give, uniformly on J,

\[
 t q^2\le5,\qquad q/2-1\le u<q/2,\qquad N\asymp\sqrt X,
 \qquad |u-\log N|=O(X^{-1/2})                              \tag{5}
\]

eventually. Indeed, with lambda=Y/X and z=log(T/(2*pi)),
t=lambda^2*pi^2/(z-1)^2 and q/(z-1)->1/2, so the limiting
upper bound is pi^2/2<5. The assertion about u follows from
1<=lambda<=sqrt2 and 0<log(2*pi/lambda)<2. The floor differs
from exp(u) by O(1): its radicand differs from exp(2u) by
O(q^(-2)). This proves the last assertion, including every floor
threshold. We may increase the onset throughout.

### A norm estimate for logarithmic kernel multipliers

For any complex vector v=(v_k)_(k<=K), define

\[
 \|v\|_A^2=\sum_{k,l\le K}\frac{v_k\overline{v_l}\gcd(k,l)}{kl}
   =\sum_{r\le K}\phi(r)|z_r(v)|^2,\qquad
 z_r(v)=\sum_{r\mid k\le K}\frac{v_k}{k}.                   \tag{6}
\]

Here phi is Euler's totient. The identity gcd(k,l)=sum_{r|k,r|l}phi(r)
proves (6). The divisor transform is triangular and invertible, so
this is a norm. All spaces and sums here are finite.

Let D_0 v have coordinates (log k)v_k and set ell_K=log K. Here
Lambda is the von Mangoldt function and mu below is the Möbius
function. The prime-power identity log n=sum_{a|n}Lambda(a) gives

\[
 z_r(D_0v)=(\log r)z_r(v)+\sum_{2\le a\le K/r}\Lambda(a)z_{ra}(v).
                                                               \tag{7}
\]

After conjugating the last operator by sqrt(phi(r)), its matrix
entry from ra to r is Lambda(a)sqrt(phi(r)/phi(ra)). Since
phi(ra)>=phi(r)phi(a), use the positive Schur weights r^(-1/2).
The weighted row sum is at most

\[
 \sum_{a\le K}\frac{\Lambda(a)}{\sqrt{a\phi(a)}}
 \le\sqrt2\sum_{a\le K}\frac{\Lambda(a)}a
 \le2\sqrt2\log K.                                        \tag{8}
\]

Only prime powers occur and phi(a)>=a/2 there. For the last
inequality, K is an integer and
log(K!)=sum_{a<=K}Lambda(a)floor(K/a), with
floor(K/a)>=K/(2a); also log(K!)<=K log K.
The weighted column sum at n is at most

\[
 \sum_{a\mid n}\Lambda(a)
       \sqrt{a\phi(n/a)/\phi(n)}
       \le\sqrt2\log n\le\sqrt2\log K.                    \tag{9}
\]

Weighted Cauchy--Schwarz proves the Schur bound: square each row
sum applied to a vector with factors sqrt(M_rn w_n/w_r), then
sum and use the column bound. Thus the operator in (7)'s sum
has norm at most 2 log K. The diagonal has norm at most log K,
so

\[
 \|D_0v\|_A\le3\ell_K\|v\|_A.                              \tag{10}
\]

For each pair put g=gcd(k,l), a=log(k/l), c=log(sqrt(kl)/g).
For complex vectors v,w consider the bilinear form

\[
 B_{s,z}(v,w)=\sum_{k,l}\frac{v_kw_lg}{kl}e^{sc+za}.
\]

The finite Jordan-divisor identity gives

\[
 B_{s,z}(v,w)=\sum_r J_{1-s}(r)
   z_r(e^{(s/2+z)D_0}v)z_r(e^{(s/2-z)D_0}w),\quad
 J_{1-s}(r)=\prod_{p^e\parallel r}p^{(e-1)(1-s)}(p^{1-s}-1).
                                                               \tag{11}
\]

Indeed sum_{r|g}J_(1-s)(r)=g^(1-s), which follows by telescoping
on each prime power. This verifies (11) without an infinite Euler
product. The absolute Taylor coefficients of J_(1-s)(r)/phi(r)
are bounded coefficient by coefficient by exp(2(log r)|s|): each
prime-power factor is

\[
 e^{-(e-1)s\log p}
 \left[1+\frac p{p-1}(e^{-s\log p}-1)\right].
\]

For C=p/(p-1) in [1,2], the absolute coefficient series of the
bracket is at most 1+C(e^x-1), which is coefficientwise at most
e^(Cx), since C<=C^m for every integer m>=1. Its product with
the first factor is dominated by e^(2e x), where x=|s|log p.
Multiplication over primes proves the assertion.

Combine this diagonal coefficient estimate with (10), the exponential
series, and Cauchy--Schwarz in (6). The absolute coefficient bound
for (11) is

\[
 \|v\|_A\|w\|_A
     \exp(5\ell_K|s|+6\ell_K|z|).
\]

To see the constants, the Jordan factor costs 2 ell_K in s; the
two exponential operators cost 3 ell_K(|s|/2+|z|) each. Equating
coefficients proves for all nonnegative integers m,n

\[
 \left|\sum_{k,l}\frac{v_kw_lg}{kl}c^ma^n\right|
 \le(5\ell_K)^m(6\ell_K)^n\|v\|_A\|w\|_A.                 \tag{12}
\]

This also applies to sesquilinear forms by taking w=conjugate(v).
Consequently an entire kernel F(c,a), whose absolute Taylor series
converges at

\[
 R_c=5\ell_K\le q/100,\qquad R_a=6\ell_K\le3q/250,           \tag{13}
\]

has its quadratic form bounded by that series value times A.
The same statement for an integrable family of such series follows
by absolute domination. Below the displayed majorants verify that
domination. Equation (12), rather than entrywise domination of a
signed matrix, is the essential estimate.

### Harmonic endpoints and the stationary integral together

This paragraph applies both to f(v)=exp(t v^2/2)cos(hv) and to
f_0(v)=exp(t v^2/2), with Y fixed in J. Write N=N(Y), u=u(Y),
delta=u-log N, R=N exp(-c-|a|/2)=Ng/max(k,l), and R_0=N/K.
Since c+|a|/2=log(max(k,l)/g)<=log K, R>=R_0 tends to infinity
uniformly. Define

\[
 E(r)=\sum_{n\le r}\frac1n-\log r-\gamma,\qquad |E(r)|\le2/r
       \quad(r\ge1),\qquad 0\le\gamma\le1.                 \tag{14}
\]

For completeness the needed bound follows from integral comparison:
H_n-log n decreases to gamma and its tail is at most 1/n. For
n<=r<n+1, subtract log(r/n), whose size is at most 1/n.
Thus |E(r)|<=1/n<=2/r. The same comparison gives 0<=gamma<=1.
These elementary bounds fix the actual endpoint error; no harmonic
endpoint is discarded or replaced by an unquantified constant.

Stieltjes summation by parts, including a possible jump at R, gives

\[
 \sum_{r\le R}\frac{f(u-c-\log r)}r
 =\int_{u-c-\log R}^{u-c}f(v)\,dv+\gamma f(u-c)
   +E(R)f(u-c-\log R)
   +\int_1^R E(r)f'(u-c-\log r)\frac{dr}{r}.                \tag{15}
\]

One can verify the endpoint convention directly by writing the
left side as H_(floor R) f(u-c-log R)+integral_1^R H_(floor r)
f'(u-c-log r)dr/r. The lower endpoint of the first integral in
(15) is |a|/2+delta. Thus adding the stationary term
integral_0^(|a|/2) f cancels that lower endpoint up to O(|delta|).
On all real arguments in (15), including the connecting interval
of length |delta|, |f|<=C and |f'|<=C/q; this follows from (5)
and |v|<=q/2+O(1). The endpoint E(R) term is O(1/R_0), and
replacing the last integral's upper limit by R_0 costs O(1/(qR_0)).
We therefore obtain uniformly in all k,l

\[
 \sum_{r\le Ng/\max(k,l)}\frac{f(u-c-\log r)}r
       +\int_0^{|a|/2}f(v)\,dv
 =I(u-c)+\mathcal E_Y(c)+O(K/\sqrt X),                      \tag{16}
\]

where I(w)=integral_0^w f(v)dv and

\[
 \mathcal E_Y(c)=\gamma f(u-c)
       +\int_1^{N/K}E(r)f'(u-c-\log r)\frac{dr}{r}.          \tag{17}
\]

Both terms on the right are entire in c. The finite upper limit is
a function of Y alone, not of k,l, which is important for (12).
For 1<=r<=N/K, w=u-log r is between delta+log K and u, so
0<=w<=u eventually. This controls the Taylor coefficients uniformly.

For f, the absolute Taylor series of f(w-c) at c=0 is bounded by

\[
 \exp\{t(w+R_c)^2/2+hR_c\}<3,                              \tag{18}
\]

and that of f'(w-c) by

\[
 [t(w+R_c)+h]\exp\{t(w+R_c)^2/2+hR_c\}\le36/q.             \tag{19}
\]

Use the half sum of the exponentials with phases +/-ihv to justify
these coefficient majorants; their constant phases have modulus one.
In (18), the exponent is at most 5(51/100)^2/2+3pi/100<1;
e<3 gives the bound. Equation (19) uses pi<22/7. The same bounds
hold for f_0 by removing h. Since integral_1^(N/K)|E(r)|dr/r<=2,
the majorant of (17) is at most 3+72/q<=4 eventually. This also
justifies integrating the Taylor series coefficient by coefficient.

Finally, the absolute sum of the weights in (16) is at most

\[
 \sum_{k,l\le K}|\beta_k\beta_l|\frac g{kl}
 \le\left(\sum_{k\le K}k^{-1/2}\right)^2\le4K.              \tag{20}
\]

The heat prefactors below are bounded on the real index set. The
total error from (16) in a quadratic form is therefore O(K^2/sqrt X),
and after integration over the band it is O(sqrt X K^2)=o(X).
This use of an absolute bound concerns only the power-saving error,
not the signed main form.

### The whole signed reference form is negative

C019q gives integral_D VV_h W=G_d+O(X^(451/500)), with G_d twice
the integral of the quadratic form having brace (16) and prefactor

\[
 H_0\widetilde H(a),\qquad
 H_0=e^{-\pi^2t/32},\qquad
 \widetilde H(a)=e^{t a^2/8}\cos(c_0ta).                    \tag{21}
\]

The absolute Taylor majorant of Htilde is at most
exp(t R_a^2/8+c_0tR_a). By (5),(13), its exponent is at most
9/100000+3pi/(400q). Consequently H_0>=1/2 and, eventually,
the majorants of Htilde and Htilde-1 are at most 1001/1000 and
1/1000 respectively. The constant coefficient of Htilde is one.

The scalar integral has the uniform negative bound

\[
 I(u)\le-q/10,\qquad |I(u)|\le q                           \tag{22}
\]

eventually. Indeed exp(t v^2/2) is increasing for v>=0. On
[0,q/6], cos(hv)>=0 and the weight is at most its value at q/6;
on [q/6,q/2], cos(hv)<=0 and the weight is at least that value.
Thus I(q/2)<=-q/(3pi). Since 0<=q/2-u<=1, replacing q/2 by u
costs at most 3. This proves the first assertion eventually. For
the second, u<=q/2 and exp(tu^2/2)<=exp(5/8)<2, so |I(u)|<=q.

The absolute Taylor majorant of I(u-c)-I(u) is at most

\[
 \int_0^{R_c}\exp\{t(u+z)^2/2+hz\}\,dz\le3q/100.          \tag{23}
\]

Combine (12), (17)--(19), and (21)--(23). Before the scalar H_0
factor, the real quadratic form in (16) is at most

\[
 A\left[-q/10+q/1000+
             \frac{1001}{1000}\frac{3q}{100}
             +\frac{1001}{1000}4\right]
 \le-\frac{qA}{20}                                         \tag{24}
\]

eventually. The contributions here are respectively the scalar
I(u), (Htilde-1)I(u), Htilde(I(u-c)-I(u)), and Htilde E_Y(c).
The majorants multiply, so (12) controls all cross terms as well.
All sums converge absolutely at (13). Since H_0>=1/2, the form
including it is at most -qA/40, apart from (20)'s error. Hence

\[
 \int_D VV_hW
 \le-\frac{|D|qA}{20}+O(X^{451/500})+O(\sqrt X K^2).        \tag{25}
\]

This uses both C019q channels. In particular the stationary integral
was necessary for the cancellation leading to (16).

### Weighted squares: the zero-shift variant with both channels

For j=0,h change variable Z=Y+j. Then E_j=D+j is contained in J,
and W(Y) is the squared modulus of the polynomial with coefficients

\[
 d_k^{(j)}=b_k k^{ij}=\beta_k k^{i(j-h/2)}.                  \tag{26}
\]

These may be complex, but their moduli are at most one. Apply the
finite cosine-product expansion to V(Z)^2 times this weight on E_j.
Here is the needed variant of the C019p/q reduction, with the changed
cases made explicit. Its main form is

\[
 Q_j=2\operatorname{Re}\int_{E_j}\sum_{k,l\le K}
  \frac{d_k^{(j)}\overline{d_l^{(j)}}g}{kl}
  e^{t(a^2/8-\pi^2/32)+ic_0ta}
  \left\{\sum_{r\le Ng/\max(k,l)}\frac{e^{t(u-c-\log r)^2/2}}r
       +\int_0^{|a|/2}e^{tv^2/2}\,dv\right\}dZ
       +O(X^{451/500}).                                    \tag{27}
\]

To justify using this formula, the difference-channel phase before
resonance extraction is now

\[
 Z\log(nl/(mk))+c_0t(Z)\log(n/m).
\]

Both entries are at Z, so the domain is E_j intersect
[max(rho_m,rho_n),infinity). For nl!=mk, put eta=log(nl/(mk)).
As in C019p, |eta|>=1/(N_*K), the slow phase derivative is
O(1/(Xq)), and its second derivative is O(1/(X^2q)). The same
integration by parts, including its endpoint and variation terms,
bounds this integral by C/(sqrt(mn)|eta|). Reindexing by mk,nl,
the divisor bound and the inspected integer A.3 give total
O(X^(753/1000)q). For nl=mk use m=(l/g)r,n=(k/g)r.
Their mean frequency is u-c-log r, their difference is a, and
the heat phase is exactly c_0ta. This gives the harmonic part
of (27); no common-entry replacement is needed.

The sum-channel leading phase is Z log(Z/x)-Z-pi/4,
x=2*pi*mn*k/l, and the slow phase is c_0t(v_m+v_n).
Its derivatives and amplitude variation satisfy the same bounds
as C019p (19), with the former hv_n term removed. Thus its
nonstationary parts, the Taylor error on |Z-x|<=X^(3/5), and
the full-line Fresnel replacement have respectively the bounds
proved there and in C019q. Moving the two band endpoints by j
does not change their separation or any exceptional-tuple count.
For retained centers, both true entries are m^2,n^2<=U(x).
The integer-gap argument of C019q gives exactly ml<=nk and
nl<=mk: a violation costs at least c sqrt(X)/K^2, whereas
U(x)-x/(2*pi)=O(q^(-2)). The converse holds directly.

For k>l the same geometric-sum averaging on this domain has
mean g/l and error O((l/g)sqrt(X)q) per (k,l) before its
1/l coefficient. The amplitude is now
exp(t(a^2+w^2)/8-pi^2t/32+ic_0ta), with w=log(m/n).
It and its m,n derivatives satisfy respectively C,C/m,C/n.
The change to (Z,w) has Jacobian l/(4*pi*k), just as in C019q.
It therefore leaves the integral over -a<=w<=a. Replacing w
by 2v gives the continuous term in (27). Under k,l interchange,
d_k conjugate(d_l) and exp(ic_0ta) both conjugate. Their real
parts agree, which justifies the symmetrization even for complex d.
For k=l the stationary tuples m=n contribute only
O(sqrt(X)log(2K)); for k<l there are no centers.

For clarity the aggregate errors in this variant are bounded by
the same quantities

\[
 O(X^{753/1000}q)+O(X^{451/500})
 +O(X^{301/500}q^2+X^{251/500}q)
 +O(X^{63/125}q)+O(\sqrt X\log(2K)).                        \tag{28}
\]

All are O(X^(451/500)) eventually. The incomplete Fresnel cases,
entry equalities and band endpoints are covered by those counts;
no positivity or omission of the stationary channel was used to
deduce (27). This is a specialization of the already written local
calculations with their changed phases checked, not an invocation
of C019q's nonzero-shift statement at an unsupported parameter.

Apply (16) to f_0 in (27). Its scalar integral is bounded by q,
its c variation by 3q/100, and its retained endpoint majorant by4.
The a-factor is now exp(ta^2/8+ic_0ta); its absolute Taylor majorant
is still at most 1001/1000. Thus (12), in its sesquilinear form,
shows that the main form in (27) is O(Xq ||d^(j)||_A^2).
The O(sqrt(X)K^2) error from (16) is absorbed in (28).
By (10) and (26),

\[
 \|d^{(j)}\|_A^2
 \le e^{6|j-h/2|\ell_K}A=e^{3h\ell_K}A\le3A.               \tag{29}
\]

Indeed 3h ell_K<=9pi/500<1. Equations (27)--(29) prove the
second bound of (2). This comparison only needs an upper bound;
it makes no assertion that these squares are o(Xq).

### Norm lower bound and the actual-P margin

Möbius inversion of (6) gives beta_1=sum_{r<=K}mu(r)z_r(beta)=1.
Cauchy--Schwarz therefore gives

\[
 A\ge\left(\sum_{r\le K}\frac{\mu(r)^2}{\phi(r)}\right)^{-1}
       \ge\frac1{3(1+\log K)}.                            \tag{30}
\]

Here is an elementary bound with the required constant. Prime-power
checking gives n/phi(n)=sum_{d|n}mu(d)^2/phi(d). Consequently

\[
 \sum_{n\le K}\frac1{\phi(n)}
 \le(1+\log K)\sum_{d\ge1}\frac{\mu(d)^2}{d\phi(d)}
 =(1+\log K)\prod_p\left(1+\frac1{p(p-1)}\right)
 \le e(1+\log K)<3(1+\log K).
\]

The nonnegative series/product converges by comparison with
sum_{n>=2}1/(n(n-1))=1, so these interchanges are justified.
This proves (30), without a prime number theorem or a reciprocal
evaluation of zeta. In particular, for q>=500,

\[
 qA\ge\frac1{3(1/q+1/500)}\ge\frac{250}{3}.                \tag{31}
\]

As |D|>=B/2 eventually and all errors in (25) are o(X), (31)
allows their absorption, giving integral_D VV_hW<=-BqA/50.
This proves the first part of (2).

Finally use C019p's exact actual-P comparison, which follows from
sup_J|P+V|=O(1/q), its weight mass O(Xq), and Cauchy--Schwarz:

\[
 \left|\int_D(PP_h-VV_h)W\right|
 \le C\sqrt{X/q}(\sqrt{Q_0}+\sqrt{Q_h})+CX/q.
\]

Insert (2). The result is at most

\[
 C X\sqrt A+C X^{951/1000}/\sqrt q+CX/q.                    \tag{32}
\]

Relative to BqA the first term is O(1/(q sqrt A))=O(q^(-1/2))
by (30), the second is O(X^(-49/1000)/sqrt q) by (31), and
the last is O(1/q). They all tend to zero uniformly along the
specified integer degrees. Increasing the common onset makes
(32) at most BqA/100. This proves (3)--(4), using (31) for
the final bound -BqA/100<=-5B/6<=-B/2.

Every onset condition is absolute and there are finitely many of
them. This argument does not require an effective value. Earlier
source floors were kept through C019p/q and (27); the subsequent
harmonic endpoint replacement is paid in (16),(20). All arithmetic
coefficient operations are finite except the explicitly dominated
positive comparison in (30).

The result answers only M1. The stopped diagonal-small-remainder
closure of C019o is not used: the whole arithmetic pair, including
its stationary contribution, is signed in a common norm. No conclusion
about rare-amplitude dominance or pair density follows without the
separate squared-mass bound. The independent audit below checks
C019p/q/r, including the norm, endpoint and square specialization,
under the original hypotheses.

### Independent conceptual audit1401 — 17 November 2026

The exact prior EXPLORE target is assessment1398, separately approved
in1399 and URL-repaired1400. This audit retains (2)--(4), including
the actual-P upper bound -B/2. It reproduces and verifies the existing
argument; it establishes no new bound or certified originality. The
essential stationary and arithmetic reductions were checked in full,
with the audit evidence recorded in C019p and C019q. Their canonical
proofs remain the complete calculations. C019l/m's audited elementary
reference and uniform normalized comparison are used with their exact
scales. C019j/k and L018/L021 enter through those stated contracts;
no new assumption about zeros is made.

**Common norm and operator constants.** The finite divisor identity
gcd(k,l)=sum_{r|k,r|l}phi(r) proves (6) for complex vectors. Its
invertibility follows by descending through k=K,...,1. Writing k=rb
and log b=sum_{a|b}Lambda(a) proves (7), including repeated prime
factors; there is no coprimality restriction on r and a.

For the conjugated off-diagonal matrix, the weighted row and column
conventions are respectively sum_n M_rn w_n/w_r and
sum_r M_rn w_r/w_n, with w_r=r^{-1/2}. These are exactly (8)
and (9). Since only prime powers a occur,
phi(a)>=a/2 and phi(ra)>=phi(r)phi(a). The row bound is
2 sqrt(2) log K, using floor(K/a)>=K/(2a) for every 1<=a<=K;
the column bound is sqrt(2) log K, using
sum_{a|n}Lambda(a)=log n. The weighted Schur test therefore gives
sqrt((2 sqrt(2))(sqrt(2))) log K=2 log K, and adding the diagonal
gives exactly 3 log K in (10).

The Schur test is a standard tool: see Grohs--Vigogna,
*Intrinsic Localization of Anisotropic Frames II: alpha-Molecules*,
ETH Research Report2014-10, March2014,
[Section2.2 Lemma(2.8), conditions(2.9) and proof, pp4--5](https://www.sam.math.ethz.ch/sam_reports/counter/ct.php?file=/sam_reports/reports_final/reports2014/2014-10_fp.pdf),
inspected in the ready assessment. The short Cauchy--Schwarz argument
in the original proof merely fixes the row/column conventions of this
specialization; it is not claimed as a new matrix theorem.

For each prime power dividing r, the absolute coefficients of
1+C(e^{-s log p}-1), C=p/(p-1), are bounded by those of
e^{C|s|log p}, since C<=C^m for m>=1. Multiplication by the
other prime-power factor gives the stated e^{2e|s|log p}
majorant. This proves the Jordan diagonal's coefficientwise bound,
not just a pointwise bound at real s. In (11), its contribution is
2 log K in s; the two exponentials of D_0 contribute
3 log K(|s|/2+|z|) each. Finite-dimensional Cauchy--Schwarz applied
coefficient by coefficient therefore gives the factorial-normalized
majorant e^{5(log K)|s|+6(log K)|z|}. Differentiation at zero
gives (12), with the factorials canceling. Taking w=conjugate(v)
is legitimate. Thus no entrywise estimate for a signed beta form
has been substituted for its relative A-norm bound.

**Harmonic endpoints, including integer R.** For n=floor(r),
0<=H_n-log n-gamma<=1/n and 0<=log(r/n)<=1/n, hence
|E(r)|<=1/n<=2/r. The finite Abel identity preceding (16)
holds with H_floor(R), including the term at an integer R. Splitting
H_floor(r)=log r+gamma+E(r) then gives exactly the signs and all
four terms of (15). In particular the gamma term is f(u-c), not
f at the lower limit.

The harmonic lower limit is |a|/2+delta, with
delta=u-log N=O(X^{-1/2}). Adding the stationary integral leaves
I(u-c) minus the integral between |a|/2 and |a|/2+delta; this
error is O(|delta|), for either sign of delta. On all relevant
real segments |f|<=C and |f'|<=C/q, and the E(R) term is
O(1/R_0). Truncating only the last E integral to R_0=N/K costs
O(1/(qR_0)). This proves (16) with error O(K/sqrt(X)).
Its sum against the absolute real-index prefactors costs
O(K^2/sqrt(X)), since (20) is at most 4K; its band integral is
O(sqrt(X)K^2). These are power-saving errors, separate from the
signed main form.

For the retained integral, w=u-log r lies between delta+log K
and u, hence in [0,u] eventually. The coefficient majorants
(18)--(19) follow by expanding both exponential phases of the cosine
about this real w. Their constants use tq^2<=5, u<=q/2 and
R_c<=q/100: the exponent is at most
5(51/100)^2/2+3*pi/100<1. The derivative prefactor is bounded
by (5*51/100+3*pi)/q<12/q. Thus 3 and 36/q are valid bounds,
and integral_1^{N/K}|E(r)|dr/r<=2 proves the eventual majorant4
in (17). Absolute domination justifies the integrated Taylor series.

**Signed margin.** The elementary sign comparison in (22) applies
because cos(3*pi*v/q) is nonnegative on [0,q/6] and nonpositive
on [q/6,q/2], while its weight is increasing. It gives
I(q/2)<=-q/(3*pi). Since 0<=q/2-u<=1, an O(1) endpoint cost
still leaves I(u)<=-q/10 eventually. Also |I(u)|<=q.
The nonconstant a-prefactor has majorant at most 1/1000 eventually:
its exponent is at most 9/100000+3*pi/(400q), and its constant
coefficient is one. The c variation costs at most 3q/100.
Consequently the coefficient of q in (24) is
-1/10+1/1000+3003/100000=-6897/100000<-1/20;
the remaining 4004/1000 is absorbed at one fixed onset.
Multiplication by H_0>=1/2 and the factor two in G_d gives (25).

There is enough room for both integrated power errors in the printed
constant 1/50: from |D|>=B/2, (25) is at most
-BqA/40 plus those errors. By (31), qA>=250/3, so the errors
divided by BqA tend to zero and are eventually at most 1/200.
Thus -1/40+1/200=-1/50. This verifies the first part of (2)
without an upper bound on A or an ineffective entrywise sign claim.

**Complex-coefficient zero-shift square.** For Z=Y+j, direct
substitution in the weight gives exactly
d_k=b_k k^{ij}=beta_k k^{i(j-h/2)}. Both source entries now
occur at Z, and E_j=D+j lies in J. The difference phase is
Z log(nl/(mk))+c_0*t log(n/m), so its nonresonances have the
same integer separation and smaller slow-phase derivative bounds as
C019p. Its resonances have coefficient d_k conjugate(d_l)g/(rkl),
heat factor exp(t(a^2/8-pi^2/32)+i*c_0*t*a), and the f_0
harmonic sum. No phase hv remains in the V square.

For the sum phase the center is again x=2*pi*mn*k/l. Removing
hv_n only reduces the amplitude derivative bounds. The endpoints of
E_j are shifted by at most h; each exceptional-tuple count remains
O(H(l/k)q+sqrt(X)). The true entries at a retained center now both
have correction O(q^{-2}); the same integer-gap test gives exactly
ml<=nk and nl<=mk. The stationary amplitude is
exp(t(a^2+w^2)/8-pi^2*t/32+i*c_0*t*a), with w=log(m/n).
Its derivative bounds, geometric row sums and row-integral variation
are precisely those checked in C019q with the h term removed.

In particular the stationary channel before symmetrization is
Re sum_{k>l} d_k conjugate(d_l)g/(kl) times the integral over
E_j and -a<=w<=a of this amplitude. The substitution w=2v
gives four times integral_0^{a/2}e^{tv^2/2}dv. Under k,l
interchange, both d_k conjugate(d_l) and e^{i*c_0*t*a}
conjugate, so their product's real part is unchanged. Replacing
the k>l sum by half of the full off-diagonal sum is therefore valid
even when d is complex. Diagonal centers cost
O(sqrt(X)log(2K)), and their continuous integral is zero. This proves
exactly (27)'s coefficient and phase, rather than a real-coefficient
formula incorrectly substituted for a complex one.

The errors listed in (28) include all those cases and have maximum
power 451/500. Applying (16) with f_0, then the sesquilinear form
of (12), bounds the main term by CXq ||d||_A^2. Finally (10)
gives ||e^{i(j-h/2)D_0}beta||_A^2
<=e^{6|j-h/2|log K}A=e^{3h log K}A<=3A. This checks the
second part of (2) without assuming Q=o(Xq).

**Lower norm, transfer and uniformity.** Finite Möbius inversion gives
1=beta_1=sum_r mu(r)z_r(beta). Weighted Cauchy--Schwarz and the
absolutely convergent positive divisor comparison in (30) therefore
give A>=1/[3(1+log K)]. The Euler product used there is bounded
by exp(sum_{n>=2}1/(n(n-1)))=e<3; no prime distribution theorem
is implicit. Since log K<=q/500, q>=500 gives (31).

The two mixed errors of C019p (9), with (2), cost
CX sqrt(A)+CX^{951/1000}/sqrt(q); its quadratic error costs CX/q.
After division by BqA their respective bounds are
O(q^{-1/2}), O(X^{-49/1000}/sqrt(q)), and O(q^{-1}), using
only the lower bound on A. All tend to zero uniformly. Taking their
sum at most 1/100 gives actual mean <=-BqA/100<=-5B/6<=-B/2.
The numerical onset need not be known: all input onsets and the
finitely many uniform eventual inequalities admit one integer maximum.

No defect requiring a change to (2)--(4) was found. The checked
sources provide standard tools, not this entire moving-heat result.
This retained first mean supplies neither the second (M2) inequality
nor quantitative opposite-sign density, disjoint root intervals or
separation from existing bulk roots. Every-degree hyperbolicity and
L030-L032/C032a remain open; this is not an RH candidate.

## Mathlib

Full matching Mathlib coverage has not been checked. No absence or
formal-verification claim is made. Finite divisor inversion, totient
identities, Cauchy--Schwarz, weighted matrix bounds and finite-dimensional
exponentials are supporting ingredients; their availability would not
by itself formalize the moving-heat stationary reduction or (4).
