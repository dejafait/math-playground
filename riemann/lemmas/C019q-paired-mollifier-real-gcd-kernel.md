# C019q — The full paired reference mean as a real gcd quadratic form

## Hypotheses

Use exactly C019p's definitions and the hypotheses of C019l/m. Thus
d tends through positive integers, T>2*pi*e is determined by
d=(T/(2*pi))(log(T/(2*pi))-1), and

\[
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,\quad D=[X,b],\quad b=\sqrt2X-h.
\]

In particular t(Y)=Y^2/(2d), ell(Y)=log(Y/(2*pi)),
c_0=pi/8, and

\[
 N(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor,
 \qquad N_*=N(\sqrt2X).
\]

V is C019l's exact elementary finite reference, with its own time and
floor at each argument. P is C019m's actual real Jensen value with its
positive normalization. Retain precisely C019p's mollifier:
L=floor(X^(1/1000)), K=L^2, omega_L(n)=log(L/n)/log L, and the real
Euler-product coefficients alpha(n) of zeta(s)^(-1/2) on Re(s)>1.
Eventually L>=2. Set

\[
 M(Y)=\sum_{n\leq L}\alpha(n)\omega_L(n)n^{-1/2-iY},
 \quad W(Y)=|M(Y)M(Y+h)|^2,
\]
\[
 b_k=\sum_{uv=k;\ u,v\leq L}
       \alpha(u)\alpha(v)\omega_L(u)\omega_L(v)v^{-ih}.
                                                               \tag{1}
\]

All estimates below hold beyond one absolute existential integer
onset, with constants independent of d and the summation indices.
No RH, nonvanishing, simple-zero, random-law or reciprocal evaluation
on the critical line is assumed. The argument originally used C019p's
provisional analytic reduction. Independent conceptual audit1401 now
retains both that reduction and the arithmetic assembly below.

## Conclusion

The numbers

\[
 \beta_k=k^{ih/2}b_k
   =\sum_{uv=k;\ u,v\leq L}\alpha(u)\alpha(v)\omega_L(u)\omega_L(v)
                    \cos\left(\frac h2\log(u/v)\right)
                                                               \tag{2}
\]

are real and satisfy |beta_k|<=1. For each k,l<=K write
g=gcd(k,l), a=log(k/l), and define

\[
 f_Y(v)=e^{t(Y)v^2/2}\cos(hv),\qquad
 H_Y(a)=e^{t(Y)(a^2/8-\pi^2/32)}\cos(c_0t(Y)a),
\]
\[
 v_r(Y;k,l)=\frac{\ell(Y)}2-\log\frac{r\sqrt{kl}}g,
\]
\[
 \mathcal K_Y(k,l)=H_Y(a)\left\{
   \sum_{1\leq r\leq N(Y)g/\max(k,l)}
                     \frac{f_Y(v_r(Y;k,l))}{r}
       +\int_0^{|a|/2}f_Y(v)\,dv\right\}.
                                                               \tag{3}
\]

The sum is over positive integers, with its exact indicated cutoff;
an empty sum is zero. Define the real quantity

\[
 \mathcal G_d=
 2\int_D\sum_{k,l\leq K}
      \frac{\beta_k\beta_l\gcd(k,l)}{kl}\mathcal K_Y(k,l)\,dY.
                                                               \tag{4}
\]

Then the full reference mean satisfies

\[
 \int_D V(Y)V(Y+h)W(Y)\,dY
       =\mathcal G_d+O(X^{451/500}),\qquad
 \frac{X^{451/500}}B=O(X^{-49/500})\longrightarrow0.           \tag{5}
\]

The finite harmonic sum in (3) accounts for all difference-channel
resonances. Its continuous integral accounts for the sum channel;
that channel is not dropped. Both true source floors of the original
observable are respected before the explicitly paid domain replacement
in the proof.

No sign of G_d is established. With Q_j=integral_D V(Y+j)^2 W(Y)dY
for j=0,h, C019p's actual-P error bound still gives only

\[
 \left|\int_D P(Y)P(Y+h)W(Y)\,dY-\mathcal G_d\right|
 \leq C X^{451/500}
   +C\sqrt{X/q}(\sqrt{Q_0}+\sqrt{Q_h})+CX/q.                 \tag{6}
\]

Thus G_d<=-2cB and Q_0+Q_h=o(Xq) would suffice for M1 with a
fixed c>0. Neither assertion is proved here. The squared mass, ordered
root selection, all-degree positivity and RH remain independent gaps.

## Proof

### Scope of the specialization and classical input

This is a development of the unchanged EXPLORE target in
`drafts/literature/2026-11-17-jensen-paired-mollifier-mean-test-1394.md`,
separately approved in1395. C019p gives the retained resonant and
truncated-Fresnel expressions with O(X^(451/500)) error, |b_k|<=1,
and the mixed-transfer bound. C019l supplies d comparable to X^2q^2,
N_*=O(sqrt X), smooth auxiliary amplitude bounds on [X/2,2X], and
the exact entries. These local inputs are used with their stated
qualifications, not as general mollified moment theorems.

The only oscillatory source estimate additionally used below is
H. Kösters, *On the Occurrence of the Sine Kernel in Connection with
the Shifted Moments of the Riemann Zeta Function*, 5 September2008,
[arXiv:0803.1141v2, Appendix A, Lemma A.2](https://arxiv.org/html/0803.1141v2#A),
also Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition, Lemma4.4. For a real twice differentiable phase with F''>=eps>0
or F''<=-eps throughout an interval, it bounds the integral of exp(iF)
in modulus by 8/sqrt(eps). Its hypotheses and proof cases were already
covered in the reused assessments; here F(z)=z^2/(2x), x>0.

The standard Gaussian integral and its analytic continuation into
Re(A)>0 evaluate integral_R exp(-A z^2)dz=sqrt(pi) A^(-1/2), with
the branch positive for positive A. Below we include the required
damping-limit and tail argument to fix the Fresnel phase and endpoint
error; we do not assert a new stationary-phase theorem. The residue
averaging is proved directly by finite geometric sums and ordinary
summation by parts. No uninspected Selberg formula is imported.

The difference from existing inputs is the actual stationary-entry
geometry, quantitative arithmetic averaging and assembly with all
resonances. This is local progress, not a certified novelty claim.

### Real mollifier coefficients

Multiplication of (1) by k^(ih/2) replaces v^(-ih) by
exp((ih/2)log(u/v)). The summation and the real coefficient attached
to u,v are symmetric under their interchange. The imaginary parts
therefore cancel, giving (2). Since |k^(ih/2)|=1, C019p's bound on
b_k gives |beta_k|<=1. In particular

\[
 b_k\overline{b_l}=e^{-iha/2}\beta_k\beta_l.                 \tag{7}
\]

This exact cancellation includes the shift in the second mollifier;
it is not a replacement of h by zero.

### Paying the Fresnel endpoints

Use C019p's x=2*pi*mn*k/l and H=X^(3/5). Its interval is
I_mn=[max(X,rho_m,rho_n-h),b], if nonempty, where
U(rho_j)=j^2 and U(Y)=Y/(2*pi)+Y^2/(32d). Its Fresnel integral
is taken over (I_mn-x) intersect [-H,H].

For x>0 the improper integral has value

\[
 \int_{\mathbb R}e^{iz^2/(2x)}\,dz
       =\sqrt{2\pi x}\,e^{i\pi/4}.                           \tag{8}
\]

For completeness, take A=eps-i/(2x), eps>0, in the Gaussian
integral. Integration by parts on either tail starting at H gives
an absolute bound at most 1/(|A|H)<=2x/H: the boundary contribution
and the integral with factor 1/z^2 are both paid using
|exp(-A z^2)|<=1. On each finite interval dominated convergence
applies as eps decreases to zero. The same tail bound, also valid
for the undamped improper integral, then proves (8) and the error
O(x/H) for its truncation to [-H,H]. The analytic continuation used
above follows from holomorphy on Re(A)>0 and the real Gaussian
identity; no limit is interchanged without this tail estimate.

Call a tuple exceptional if x is within H of any of
X,b,rho_m,rho_n-h. Only x in [X-H,b+H] need be considered: outside
this band both C019p's truncated term and the proposed full term
are zero. For a nonexceptional tuple, either x is inside I_mn and
the truncated interval is exactly [-H,H], or both terms vanish.
Consequently (8) replaces the Fresnel factor by
sqrt(2*pi*x) exp(i*pi/4) 1_{x in I_mn}, at cost O(X/H) per
nonexceptional factor. With its amplitude and mollifier coefficient,
C019p's absolute-sum bound gives total cost

\[
 O((X/H)N_*K)=O(X^{451/500}).                               \tag{9}
\]

For exceptional tuples, A.2 bounds every incomplete Fresnel integral
by 8*sqrt(x); (8) has the same order. All relevant x lie in
[X/2,2X] eventually. The auxiliary amplitudes obey
|a_m(x)a_n(x)|<=C/sqrt(mn), and x=2*pi*mn*k/l implies

\[
 \frac{\sqrt X}{\sqrt{mnkl}}\leq C/l.                       \tag{10}
\]

Thus each exceptional tuple costs at most C/l, using |b_k|<=1.
We now count them, rather than assign a full Fresnel integral at
an unpaid endpoint. Uniformly for j<=N_*, rho_j<=sqrt(2)X and

\[
 |\rho_j-2\pi j^2|=\frac{\pi\rho_j^2}{16d}=O(q^{-2}).       \tag{11}
\]

For fixed m,k,l, either band-endpoint condition restricts n to an
interval of length at most C H l/(km). The condition near rho_m
does the same, now centered at ml/k, by (11). The condition near
rho_n-h is counted with n fixed instead, centered at nl/k for m;
h+O(q^(-2)) is absorbed by H. The number of integers in an interval
of length A is at most A+1. Summing 1/m or 1/n up to N_* gives
O(q). Hence for each k,l the union of the four exceptional sets has
at most

\[
 C(H(l/k)q+\sqrt X)
\]

tuples. By (10), summing their costs gives

\[
 O(HKq^2+\sqrt X Kq)=o(X^{451/500}).                        \tag{12}
\]

This accounts for stationary points at source entries, at both band
endpoints and outside the band but within the truncation window.
The convention at exact equality changes only these already paid
terms. Equations (9)--(12) justify the whole-line replacement.

### The exact stationary geometry after replacement

For a retained center x in [X,b], the true entry conditions are
m^2<=U(x) and n^2<=U(x+h). Since m,n<=N_* and
x=2*pi*mn*k/l>=X, both m and n are at least c*sqrt(X)/K.
If ml>nk, the integer ml-nk is at least1, and

\[
 m^2-\frac{x}{2\pi}=\frac{m(ml-nk)}l
        \geq c\sqrt X/K^2.
\]

This exceeds U(x)-x/(2*pi)=O(q^(-2)) eventually. The analogous
argument for nl>mk exceeds
U(x+h)-x/(2*pi)=O(q^(-1)). Therefore the true entry conditions
imply ml<=nk and nl<=mk. Conversely these two inequalities imply
m^2,n^2<=x/(2*pi), so both true entries hold, including equalities.
Thus the center domain is exactly

\[
 X\leq2\pi mnk/l\leq b,\qquad ml\leq nk,\quad nl\leq mk.
                                                               \tag{13}
\]

It contains no tuples with k<l. For k=l it forces m=n; for k>l,
put a=log(k/l)>0 and u=log(m/n), so |u|<=a. Conditions (13)
also imply m,n<=sqrt(b/(2*pi)). Since m,n are integers, they are
at most floor(sqrt(b/(2*pi)))<=N_*, making the prior upper index
bound redundant in this exact domain.

At these centers v_m(x)=(a-u)/2 and v_n(x)=(a+u)/2. Define

\[
 E_d(Y;a,u)=\exp\left\{
 t(Y)\left(\frac{a^2+u^2}{8}-\frac{\pi^2}{32}\right)
       +i\left(c_0t(Y)a+\frac h2(a+u)\right)\right\}.          \tag{14}
\]

Substituting (8) into C019p's stationary expression, including its
outside factor 2 Re and its phase exp(-ix-i*pi/4), gives exactly

\[
 4\pi\operatorname{Re}\sum_{1\leq l\leq k\leq K}
 \frac{b_k\overline{b_l}}l
   \sum_{(m,n)\text{ satisfying }(13)}
       e^{-2\pi i mnk/l}E_d(2\pi mnk/l;a,\log(m/n)),          \tag{15}
\]

up to (9)--(12). The identity sqrt(2*pi*x)/sqrt(mn)=2*pi*sqrt(k/l)
explains the factor 4*pi/l; there is no missing phase or square root.
For k=l, m=n, each summand has modulus O(1/k). There are O(sqrt X)
choices of m, so all k=l terms cost O(sqrt X log(2K))=o(X).

### Arithmetic averaging, with uniform errors

Fix k>l and write c=l/gcd(k,l), so k/l has reduced denominator c.
Regard the domain (13) as a region in positive real m,n. For fixed m
the n interval, when nonempty, is

\[
 A(m)=\max(e^{-a}m,Xe^{-a}/(2\pi m)),\qquad
 C(m)=\min(e^{a}m,be^{-a}/(2\pi m)).                         \tag{16}
\]

Its m range is [sqrt(X/(2*pi))e^(-a),sqrt(b/(2*pi))]. Throughout
the region both variables lie between c_1*sqrt(X)/K and C_1*sqrt(X)
for fixed positive constants c_1,C_1. Write
F(m,n)=E_d(2*pi*mn*k/l;a,log(m/n)). Because t(Y)=O(q^(-2)),
|a|,|u|<=log K<=q/500 and h=O(1/q), differentiating (14) gives

\[
 |F|\leq C,\qquad |\partial_m F|\leq C/m,
       \qquad |\partial_n F|\leq C/n.                       \tag{17}
\]

For example Y*partial_Y log E equals
2t((a^2+u^2)/8-pi^2/32+i*c_0*a), which is bounded, and
partial_u log E=t*u/4+i*h/2 is bounded. The chain rule then gives
(17). These estimates concern the smooth functions on this region,
not derivatives across a floor.

If c does not divide the integer m, partial sums in n of
exp(-2*pi*i*mn*k/l) have modulus at most Cc by the finite geometric
sum formula. If c divides m, that exponential is identically1.
Ordinary one-dimensional summation by parts, paying both endpoints
and integral |partial_n F|, therefore gives for each integer m

\[
 \sum_{n\in[A(m),C(m)]\cap\mathbb Z}e^{-2\pi i mnk/l}F(m,n)
  =1_{c\mid m}\int_{A(m)}^{C(m)}F(m,n)\,dn+O(cq).           \tag{18}
\]

Here integral |partial_n F|<=C log(C(m)/A(m))<=Cq. The same
endpoint/variation argument bounds the discrepancy between a sum
and an integral when c divides m. Empty intervals contribute zero;
singleton rows also satisfy the bound.

Set G(m)=integral_{A(m)}^{C(m)}F(m,n)dn on the nonempty region,
and zero elsewhere. Its supremum is O(sqrt X). Both endpoints in
(16) have a bounded number of monotone pieces and values at most
C sqrt X; their total variations are O(sqrt X). Their endpoint
contributions to the variation of G have that bound. The remaining
contribution is at most

\[
 C\int\frac{C(m)-A(m)}m\,dm=O(\sqrt X q),
\]

by (17). Thus G has total variation O(sqrt X q), including the
zero extension (its interval length vanishes at both outer ends).
The elementary mesh-c sum/integral comparison, obtained by paying
the variation on each mesh interval, gives

\[
 \sum_{c\mid m}G(m)=\frac1c\int G(m)\,dm+O(\sqrt X q).
\]

Summing (18) over O(sqrt X) rows consequently proves

\[
 \sum_{(m,n)\in(13)\cap\mathbb Z^2}e^{-2\pi i mnk/l}F(m,n)
    =\frac{\gcd(k,l)}l\iint_{(13)}F(m,n)\,dm\,dn
           +O(c\sqrt X q).                                 \tag{19}
\]

This proves the arithmetic average, rather than assuming cancellation
of all rational twists. After multiplication by the coefficient in
(15), its summed error is bounded by

\[
 C\sqrt X q\sum_{1\leq l<k\leq K}c/l
       \leq C\sqrt X q K^2=o(X^{451/500}).                   \tag{20}
\]

The change of variables Y=2*pi*mn*k/l, u=log(m/n) maps the region
bijectively to D times [-a,a], with Jacobian l/(4*pi*k).
Consequently the stationary channel is

\[
 \operatorname{Re}\sum_{1\leq l<k\leq K}
   \frac{b_k\overline{b_l}\gcd(k,l)}{kl}
       \int_D\int_{-a}^{a}E_d(Y;a,u)\,du\,dY
        +O(X^{451/500}).                                    \tag{21}
\]

Using (7), symmetry in u cancels the sine part, leaving
H_Y(a) times integral_{-a}^a exp(t*u^2/8) cos(h*u/2)du.
The substitution v=u/2 and the symmetry in k,l then rewrite (21) as

\[
 2\int_D\sum_{k,l\leq K}
   \frac{\beta_k\beta_l\gcd(k,l)}{kl}H_Y(a)
                    \int_0^{|a|/2}f_Y(v)\,dv\,dY
       +O(X^{451/500}).                                    \tag{22}
\]

The diagonal integral is zero. This accounts explicitly for the two
factors of2: first the even u integral and v=u/2, then replacing
the k>l sum by half of the symmetric k!=l sum.

### All difference resonances and the paid common-entry replacement

C019p's difference expression retains nl=mk and the domains I_mn.
Replace I_mn by the subinterval

\[
 J_{mn}=[\max(X,\rho_m,\rho_n),b],
\]

with the usual empty/singleton convention. Its difference from I_mn
has length at most h, even if one interval is empty. The amplitude
of each summand is bounded by C/sqrt(mnkl). C019p's total absolute
coefficient bound over all tuples is O(N_*K), also bounding its
resonant subset. Hence the domain replacement costs

\[
 O(hN_*K)=o(X^{451/500}).                                   \tag{23}
\]

It changes no observable and no phase: it only pays for the difference
between the two integration domains in this already reduced term.

For g=gcd(k,l), all positive solutions of nl=mk are exactly
m=(l/g)r, n=(k/g)r. On J_mn the integer r obeys
r<=N(Y)g/max(k,l), including floor equality. Put v=v_r(Y;k,l).
Then v_m=v+a/2, v_n=v-a/2. The product of the amplitudes and the
mollifier denominators is

\[
 \frac{g}{rkl}
   \exp\{t(Y)(v^2/2+a^2/8-\pi^2/32)\}.
\]

C019p's resonant phase is c_0*t*a-h*v_n. Combining (7) reduces
it exactly to c_0*t*a-h*v. Under interchanging k and l, the domain,
v and all real factors remain unchanged, while a changes sign.
The average of the two real parts is
cos(c_0*t*a) cos(h*v), also valid on the diagonal a=0.
Thus all resonances together equal

\[
 2\int_D\sum_{k,l\leq K}\frac{\beta_k\beta_l g}{kl}H_Y(a)
   \sum_{1\leq r\leq N(Y)g/\max(k,l)}\frac{f_Y(v_r)}r\,dY
       +O(hN_*K).                                         \tag{24}
\]

All sums are finite. The common-entry condition was essential to
this pairing and has been paid in (23), rather than assumed.

### Assembly and the still-unpaid discriminator

C019p already pays its nonresonances and local stationary expansion
by O(X^(451/500)). Adding (22) and (24) proves (3)--(5).
For clarity, the additional errors are bounded by

\[
 O(X^{451/500})
 +O(X^{301/500}q^2+X^{251/500}q)
 +O(X^{63/125}q)+O(\sqrt X\log(2K))+O(hN_*K).
\]

Here HK<=X^(301/500), sqrt(X)K<=X^(251/500), and
sqrt(X)K^2<=X^(63/125). All terms after the first are absorbed by
it beyond one onset. The entry-gap bound sqrt(X)/K^2 tends to
infinity and the finitely many scale and amplitude conditions also
hold eventually, so their maximum gives one onset uniform in all
indices. No effective numerical onset is claimed.

Equation (6) is precisely C019p's still-unpaid mixed-transfer bound
combined with (5). No new bound on Q_0 or Q_h was obtained during
this attempt. Real coefficients, a gcd weight and positive factors
in parts of (3) do not determine the sign of its whole quadratic
form. In particular the beta_k beta_l factors have both signs, and
the finite harmonic sum must not be replaced by an integral with an
unpaid O(B) endpoint error.

This result removes the incomplete stationary integrals and exposes
both channels in one explicit arithmetic form. It does not establish
M1, refute M1, or provide the independent squared-mass estimate. The
negative-margin test was inconclusive at this reduction stage; C019r
subsequently treats it. Independent audit1401 below retains (5).
No numerical computation or mathematical script is evidence for (5).

### Independent conceptual audit1401 — 17 November 2026

Under the prior EXPLORE assessment1398, separately approved1399, this
audit retains (2)--(6). It checks all cases needed by C019r, rather
than accepting the stationary contribution as a pre-established input.

**Incomplete Fresnel integrals and exceptional tuples.** For
A=epsilon-i/(2x), integration by parts on [H,infinity) bounds the
Gaussian tail by 1/(|A|H)<=2x/H, uniformly in epsilon>=0 (with an
improper integral at zero). Dominated convergence on finite intervals
and then this tail estimate give the phase e^{i*pi/4} in (8).
For a nonexceptional tuple with a nonzero truncated term, x is inside
its true I_mn at distance greater than H from each defining endpoint.
The truncated interval is therefore [-H,H]. If instead x is outside
I_mn, both terms vanish. This proves that only the stated exceptional
set needs a separate O(sqrt(X)) estimate.

For that set, the real phase z^2/(2x) has F''=1/x>0, so the
cited A.2 bounds every possible incomplete interval. The full-line
term has the same size. Since x is in [X/2,2X], the exact relation
x=2*pi*mn*k/l implies sqrt(X)/sqrt(mnkl)<=C/l. For a fixed
m,k,l the conditions near X,b or rho_m each restrict n to length
O(Hl/(km)); for the condition near rho_n-h fix n instead and
restrict m to length O(Hl/(kn)). The error
rho_j-2*pi*j^2=O(q^{-2}) and the shift h are smaller than H.
Thus the count for each k,l is O(H(l/k)q+sqrt(X)), including the
integer endpoint allowance. Summing its C/l cost gives
O(HKq^2+sqrt(X)Kq). This pays exact band endpoints, source entries,
and centers just outside the band. No half-Fresnel value is silently
replaced by a full value.

**Integer gap and normalization.** If x>=X and m,n<=N_*, then
mn>=X/(2*pi*K); since each index is at most C sqrt(X), each is
at least c sqrt(X)/K. When ml-nk>=1, the excess m^2-x/(2*pi)
is at least c sqrt(X)/K^2, which tends to infinity. This exceeds
the first entry correction O(q^{-2}). Swapping m,n gives the same
conclusion for the second correction O(q^{-1}), which includes h.
The reverse implications follow from nonnegative entry corrections.
Hence (13) is exactly the retained center domain, not a continuum
approximation to its inequalities. It is empty for k<l and diagonal
in m,n when k=l. Its original upper index bound is redundant.

Writing u=log(m/n) on this domain gives
v_m=(a-u)/2 and v_n=(a+u)/2. Multiplication of the two amplitudes
produces t((a^2+u^2)/8-pi^2/32); their sum phase produces
c_0*t*a+h(a+u)/2. The Fresnel phase cancels the original -pi/4,
leaving e^{-2*pi*i*mn*k/l}. The outside factor 2 Re and
sqrt(2*pi*x)/sqrt(mnkl)=2*pi/l prove precisely the coefficient
4*pi/l in (15). Diagonal k=l terms cost O(sqrt(X)log(2K)).

**Arithmetic average and its boundary variation.** Put c=l/g and
reduce k/l to denominator c. For an integer m with c not dividing m,
the ratio in the n geometric sum is a nontrivial c-th root of unity;
every partial sum has modulus O(c). When c divides m the ratio is
one. This gives (18) by summation by parts, with both endpoints and
integral |partial_n F| paid. The region has O(sqrt(X)) integer rows,
and its nonempty row endpoints are exactly (16).

Each endpoint is made of finitely many monotone pieces with range
O(sqrt(X)). Differentiating the row integral gives the endpoint
variation O(sqrt(X)) and the interior bound
C integral (C(m)-A(m))/m dm=O(sqrt(X)q). At both outer endpoints
the row length is zero, so extension of G by zero adds no missing
jump. Comparing each mesh-c interval to its integral incurs at most
its variation, giving O(sqrt(X)q), with no extra factor c.
Together with the row errors this proves (19), whose sum after the
1/l coefficient is O(sqrt(X)q K^2). This remains valid when the
region is thin or some rows are singletons.

The inverse coordinates are
m=sqrt(Yl/(2*pi*k))*e^{u/2},
n=sqrt(Yl/(2*pi*k))*e^{-u/2}; their Jacobian has absolute value
mn/(2Y)=l/(4*pi*k). Thus (21) has exactly its printed coefficient.
Using b_k conjugate(b_l)=e^{-iha/2} beta_k beta_l removes the
constant h*a/2 phase. The symmetric u integral removes sin(h*u/2).
Its change u=2v contributes a factor four; replacing k>l by the
full symmetric sum divides by two. This proves the factor two in
(22). The omitted k=l continuous integral is zero.

**Resonances and assembly.** Replacing I_mn by J_mn shortens an
interval by at most h, so (11) of C019p pays O(hN_*K) even across
empty intervals. Parametrization m=(l/g)r,n=(k/g)r gives
v_m=v+a/2,v_n=v-a/2 and coefficient g/(rkl). The remaining
phase after multiplication by the mollifier is c_0*t*a-h*v.
Interchange k,l preserves the common domain and v, and averaging
its real parts gives cos(c_0*t*a)cos(h*v). This verifies (24),
including the exact integer cutoff and a=0.

The extra exponents are 301/500,251/500,63/125,1/2, all strictly
less than 451/500; their fixed logarithmic factors are absorbed.
The nonexceptional Fresnel error is exactly of order X^{451/500}.
Consequently the full reference formula survives uniformly beyond one
absolute existential onset. This independently verifies the existing
reduction and adds no sign theorem beyond C019r's separate argument.

## Mathlib

Full matching Mathlib coverage has not been checked. No absence or
formal-verification claim is made. Standard Gaussian integration,
finite geometric sums, integration by parts and gcd parametrization
are supporting ingredients; none is asserted to formalize this full
moving-heat, moving-floor arithmetic reduction.
