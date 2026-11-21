# C759b: A recurrent odd carrier excludes the joint arithmetic coefficient 3/2

## Hypotheses

Work in real L2(-1,1), with zero extension outside this interval,
the inner product integral f(x)g(x)dx, and C759a's fixed space

\[
 W=\{w:w(-x)=-w(x),\ \langle w,s_j\rangle=0,
             \ 1\le j\le120\},\qquad s_j(x)=\sin(\pi jx).
\]

The s_j have norm one and are mutually orthogonal. Let P be the
orthogonal projection onto their first120 modes. For a>0 define
T_a f(x)=f(x-a), restricted to(-1,1), using zero extension, and set

\[
 \mathcal S=\{2,3,4,5,7\},\quad d_n=\log n,\quad
 a_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 A=\sum_{n\in\mathcal S}a_n(T_{d_n}+T_{d_n}^*).
 \tag{1}
\]

Here Lambda(p^k)=log p, so a_4=log2/2. These are all overlapping
prime powers for this interval. Put f_0=1/sqrt2 on(-1,1), and use
only the proposed family

\[
 g_t=f_0\sin(tx),\qquad v_t=(I-P)g_t,\qquad
 w_t=v_t/\|v_t\|_2\quad\hbox{when }v_t\ne0.
 \tag{2}
\]

For form-domain relevance use precisely C759a Section1's domain

\[
 \mathcal V=\left\{f\in L^2(-1,1):
 \int_{\mathbb R}\left(1+\tfrac12\log(1+\xi^2)\right)
       |F_f(\xi)|^2\frac{d\xi}{2\pi}<\infty\right\},
 \quad F_f(\xi)=\int_{-1}^1 f(x)e^{-i\xi x}\,dx.
 \tag{3}
\]

The only external recurrence input is Dirichlet's simultaneous
approximation theorem, in Pete L. Clark, *Geometry of Numbers with
Applications to Number Theory*, [159-page author PDF, p72](https://plclark.github.io/PeteLClark/Expositions/geometryofnumbers.pdf#page=72),
Theorem13.3/Corollary13.4, inspected in the prior assessment on
13 November2026. The unbounded-return consequence and bounded-form
tools are already proved in L743 Sections1-2; their application below
uses no cell-neutral conclusion. No rational independence, neutrality,
RH, source positivity certificate or bounded full energy is assumed.

## Conclusion

There is a sequence t_r tending to positive infinity for which w_(t_r)
is well defined eventually, belongs to W intersected with the full form
domain (3), and

\[
 \lim_{r\to\infty}\langle Aw_{t_r},w_{t_r}\rangle
 =R:=\langle Af_0,f_0\rangle
 =\sum_{n\in\mathcal S}\frac{\Lambda(n)}{\sqrt n}(2-\log n).
 \tag{4}
\]

The rational certificate gives the strict bounds

\[
 1.745850839151<R<1.745850839159,\qquad
 R-\tfrac32>\tfrac{49}{200}=0.245.
 \tag{5}
\]

Thus unit vectors in W intersected with the form domain have arithmetic
Rayleigh value greater than1.745 eventually along this sequence.
In particular 3/2 is not an upper coefficient for (1) on C759a's W.
This is an existence proof through a limiting sequence, not a selected
numerical return frequency or an exact arithmetic supremum theorem.

This is a REPRODUCTION/specialization of the assessed recurrence and
finite-projection mechanism. It supplies new local obstruction evidence,
not a claim of novelty beyond the sources checked. The independent
step800 audit in Section6 accepts this scoped result. It stops only the
proposed3/2 arithmetic replacement. C759a's
older separate-cost stop remains valid. In the full Weil form the
arithmetic term has the negative sign -<Aw,w>, as in C759a(1) and
L744(6); (5) does not control its archimedean companion or full Q.
No shifted odd floor, coupling/Schur sign, parity ordering, even
simplicity/sign, Xi realization with multiplicities, global mixed
positivity, or RH conclusion is established.

## Proof

### 1. Recurrence and the bounded arithmetic form

Each zero-extended shift and its adjoint have operator norm at most1.
Thus A is bounded self-adjoint with

\[
 B:=2\sum_{n\in\mathcal S}a_n<\infty,\quad \|A\|\le B,
 \qquad
 |\langle Au,u\rangle-\langle Av,v\rangle|
 \le B\|u-v\|_2(\|u\|_2+\|v\|_2).
 \tag{6}
\]

These are L743 Section1's bounded-form inequalities specialized to
this finite list; translation from(0,2) to(-1,1) is unitary and keeps
the zero-extension convention. Reflection interchanges T_a and T_a^*,
so A preserves the odd sector, although the scalar calculation below
does not need a parity spectral theorem.

Apply L743 Section2's finite-list recurrence consequence to
theta_n=d_n/(2*pi), n in S. Its argument uses only finiteness of
the list: unbounded simultaneous denominators give a subsequence,
and a repeated bounded denominator gives exact returns and their
multiples. Neither its special window length nor cell neutrality is
used in that consequence. It supplies

\[
 t_r\longrightarrow+\infty,\qquad
 \max_{n\in\mathcal S}|e^{it_r d_n}-1|\longrightarrow0.
 \tag{7}
\]

The five dependent phases, including d_4=2d_2, meet the theorem's
arbitrary-real-list hypotheses. No search for a frequency is needed.

### 2. Exact projection, parity and nonzero normalization

Each g_t is real odd. Since P projects onto real odd vectors, v_t is
real odd and <v_t,s_j>=0 exactly for1<=j<=120. Direct integration gives

\[
 \|g_t\|_2^2=\frac12-\frac{\sin(2t)}{4t},\qquad t>0.
 \tag{8}
\]

For t>120*pi and1<=j<=120 the product-to-sum identity gives

\[
 \begin{split}
 b_j(t):=\langle g_t,s_j\rangle
 &=\frac1{\sqrt2}\left(
 \frac{\sin(t-j\pi)}{t-j\pi}-
 \frac{\sin(t+j\pi)}{t+j\pi}\right)\\
 &=\frac{\sqrt2(-1)^j j\pi\sin t}{t^2-j^2\pi^2}.
 \end{split}
 \tag{9}
\]

Consequently P g_t=sum_(j=1)^120 b_j(t)s_j is the exact projection,
and orthogonality gives

\[
 \begin{split}
 e_t^2:=\|Pg_t\|_2^2
 &\le\frac{2\pi^2\sum_{j=1}^{120}j^2}
              {(t^2-(120\pi)^2)^2}
 =\frac{2\pi^2\cdot583220}{(t^2-(120\pi)^2)^2}
 \longrightarrow0,\\
 \|v_t\|_2^2&=\|g_t\|_2^2-e_t^2\longrightarrow\frac12.
 \end{split}
 \tag{10}
\]

Thus v_t is nonzero for all sufficiently large t, not merely on
the selected returns. Normalization preserves exact membership in W.
The factor1/2 in(8)-(10) is retained in the Rayleigh limit.

### 3. Every actual overlap and both adjoint terms

For0<a<2, the zero-extended correlation is supported on
x in(-1,1-a). The finite product integral evaluates exactly to

\[
 \begin{split}
 C_{g_t}(a)
 &=\frac12\int_{-1}^{1-a}\sin(t(x+a))\sin(tx)\,dx\\
 &=\frac14\left((2-a)\cos(ta)
                    -\frac{\sin(t(2-a))}{t}\right).
 \end{split}
 \tag{11}
\]

Indeed the oscillatory integral of cos(2tx+ta) over that interval
is sin(t(2-a))/t. Both <T_a g_t,g_t> and <T_a^* g_t,g_t>
equal C_(g_t)(a). Every d_n in S lies strictly between0 and2,
as also certified in Section5. Equations(1),(11) therefore give

\[
 \langle Ag_t,g_t\rangle
 =\frac12\sum_{n\in\mathcal S}a_n
       \left((2-d_n)\cos(td_n)-\frac{\sin(t(2-d_n))}{t}\right).
 \tag{12}
\]

Along(7), the cosine factors tend to1 and all five sine/t terms
tend to zero. Hence(12) tends to R/2. This is a finite sum of exact
integrals. No infinite-sum interchange or Riemann-Lebesgue invocation
is required; in that alternative interpretation, each overlap
indicator is L1 on its bounded interval. Periodic shifts would remove
the actual overlap lengths and would give a different calculation.

By(6),(10) and ||v_t||<=||g_t||,

\[
 |\langle Av_t,v_t\rangle-\langle Ag_t,g_t\rangle|
 \le2B e_t\|g_t\|_2\longrightarrow0.
 \tag{13}
\]

Divide by the denominator tending to1/2 in(10). This proves the
limit(4). Finally C_(f_0)(a)=(2-a)/2 on the same overlap,
so the unmodulated Rayleigh value is exactly R as asserted.
Direct projection was necessary to pass from L743's different complex
space to these real odd tests; no abstract numerical-range theorem
has been reproved or presumed to supply the scalar.

### 4. Membership in the complete form domain

For each fixed t, g_t is smooth on[-1,1] and is extended by zero.
Integration by parts on this interval, retaining its endpoint terms,
gives, for |xi|>=1,

\[
 |F_{g_t}(\xi)|\le
 \frac{|g_t(-1)|+|g_t(1)|+\int_{-1}^1|g_t'(x)|dx}{|\xi|}
 \le\frac{\sqrt2(1+|t|)}{|\xi|}.
 \tag{14}
\]

On bounded frequency sets the L1 bound gives a bounded Fourier
transform. Since log(1+xi^2)/xi^2 is integrable at infinity,
(14) proves g_t in V for every fixed t. C759a Section1 already
verifies each s_j in V; alternatively the same integration-by-parts
argument applies to it. Finite subtraction and finite nonzero
normalization in(2) therefore give w_t in V. This proves domain
applicability despite the carrier's endpoint jumps. The t-dependent
bound(14) supplies no uniform form norm or energy estimate.

### 5. Rigorous evaluation of the one constant-envelope scalar

All the following bounds use rational arithmetic. For p=2,3,5,7 put
z=(p-1)/(p+1) and K=64. Integration of the finite geometric series
for 2/(1-z^2) gives

\[
 S_p=2\sum_{k=0}^{K-1}\frac{z^{2k+1}}{2k+1}
 <\log p<S_p+
 E_p,\qquad
 E_p=\frac{2z^{2K+1}}{(2K+1)(1-z^2)}.
 \tag{15}
\]

The lower tail is positive. For its upper bound replace each tail
denominator by2K+1 and sum the geometric series; the replacement is
strict beyond the first term. This elementary scalar identity is used
only to certify(5), not to reprove the imported recurrence theorem.
Round the lower S_p down and the upper S_p+E_p up to the rational
grid10^(-12). For square roots, integer squaring brackets sqrt n
between k/10^12 and(k+1)/10^12, k=floor(sqrt(n*10^24)); sqrt4=2
is used exactly. These give the strict logarithm intervals and closed
square-root brackets:

| n | log n lower | log n upper | sqrt n lower | sqrt n upper |
|---|---:|---:|---:|---:|
| 2 | 0.693147180559 | 0.693147180560 | 1.414213562373 | 1.414213562374 |
| 3 | 1.098612288668 | 1.098612288669 | 1.732050807568 | 1.732050807569 |
| 4 | 1.386294361118 | 1.386294361120 | 2 | 2 |
| 5 | 1.609437912434 | 1.609437912435 | 2.236067977499 | 2.236067977500 |
| 7 | 1.945910149055 | 1.945910149056 | 2.645751311064 | 2.645751311065 |

The n=4 logarithm is exactly twice the log2 interval, but its
Lambda coefficient remains log2. Let l_n,u_n be the log endpoints,
and r_n^-,r_n^+ the root endpoints. Put p(n)=n except p(4)=2.
All factors below are strictly positive, so interval multiplication
and inversion have the displayed directions:

\[
 \sum_{n\in\mathcal S}\frac{l_{p(n)}(2-u_n)}{r_n^+}
 <R<
 \sum_{n\in\mathcal S}\frac{u_{p(n)}(2-l_n)}{r_n^-}.
 \tag{16}
\]

Exact summation and outward rounding of(16) give(5). In particular
its lower endpoint exceeds1745/1000, so its margin over3/2 exceeds
49/200. Limit(4) then yields arithmetic Rayleigh values>1.745
eventually, and hence rejects the proposed3/2 upper bound. This is
a strict-gap argument, not numerical extrapolation from sampled t.

Reproduce with

    python3 scripts/spectral-triples/odd-carrier-scalar-798.py

The full certificate `scripts/spectral-triples/odd-carrier-scalar-798.json`
stores every rational log term and tail, root square check, all five
coefficient/overlap intervals, exact total endpoints and margin,
checks, failures and script hash. All checks pass; no failed run
preceded this certificate. The load-bearing scalar, contributions and
checks were inspected in full. Python integer/Fraction arithmetic is
a software trust assumption, not a formal verification. No carrier
frequency, different envelope, cutoff change or full energy was computed.

### 6. Independent conceptual audit — 13 November2026, step800

The audit accepts (4)-(5) under exactly the stated hypotheses, with no
mathematical repair. It reuses the already inspected Clark theorem and
L743 Sections1-2, not the complex cell-neutral conclusion of L743.
The source coverage was approved separately before this audit.

For recurrence, apply the cited simultaneous theorem to the five real
numbers d_n/(2*pi). An unbounded set of selected positive integer
denominators has a subsequence tending to infinity with vanishing
errors. Otherwise one positive denominator repeats along unbounded M;
all its errors are zero, and its positive multiples give exact returns.
This checks both cases, including the dependent log4 phase. No density
of an irrational torus orbit or rational independence is being presumed.

For projection, integrating sin(tx)sin(j*pi*x) gives the two sinc
terms in (9); sin(t +/- j*pi)=(-1)^j sin t gives its displayed sign
and numerator. The exact sum of j^2, 1<=j<=120, is583220. The bound
in (10) follows by bounding sin^2 t by1 and each positive denominator
below by t^2-(120*pi)^2. All120 modes are removed exactly. The squared
norm tends to1/2, so sufficiently large returns have a nonzero
denominator; finite exceptional t are irrelevant. Real odd parity
survives both projection and normalization.

The adjoint is T_a^*f(x)=f(x+a) on(-1,1-a), zero elsewhere.
Substitution in the right-shift pairing gives the same overlap as
the adjoint pairing. Product-to-sum gives (11), including the sine
boundary term and factor1/4. There are two adjoint contributions,
so (12) tends to R/2. The bound (6) applies to g_t and v_t since A
is bounded and ||v_t||<=||g_t||; thus the finite projection changes
this limit by zero. Dividing by the norm squared tending to1/2 gives
R, not R/2 or2R. For f_0 the overlap integral is(2-a)/2, verifying
the claimed equality with its arithmetic Rayleigh value.

The complete delay list is also checked: the certified bounds imply
log7<2<3log2=log8; among integers2 through7 only6 has zero Lambda.
The coefficient at4 is log2/2 throughout. Every overlap in (11) is
therefore nonempty, and no further prime power contributes. The
negative sign of the arithmetic term agrees with C759a(1)/L744(6).

For the domain check, the endpoint contribution for g_t is at most
sqrt2 and its derivative L1 norm at most sqrt2|t|, proving (14).
Its Fourier transform is bounded near zero by its finite L1 norm;
the square of the high-frequency bound is integrable against
1+(1/2)log(1+xi^2). Each projected sine has the same property.
The weighted Fourier space is linear, so finite projection and each
nonzero normalization preserve membership. Constants may depend on t:
this supplies no uniform form-norm estimate, energy limit or neutrality.

For the scalar audit, the positive tail after64 terms in (15) is
strictly below its geometric majorant because every later denominator
after the first is strictly larger than129. All lower logarithm bounds
are strict, all roots are bracketed by direct rational squaring, and
all overlaps in (16) are positive. Thus interval multiplication and
inversion give strict outer bounds even for the exact root sqrt4=2.
The independent verifier reconstructs every one of the256 stored
logarithm terms successively, all four partial sums and tails, all
five root brackets, coefficients, directed contribution intervals,
total endpoints and margins. It also recomputes every original flag
and verifies the original script hash; it does not trust PASS alone.

Reproduce this audit with

    python3 scripts/spectral-triples/odd-carrier-audit-800.py

The full audit certificate is
`scripts/spectral-triples/odd-carrier-audit-800.json`:77 checks pass,
with no failures. Its exact endpoints reproduce (5), and the lower
endpoint minus3/2 is strictly greater than49/200. All load-bearing
source certificate data were read and checked by that verifier; the
exact total, five contributions and check fields were also inspected
in full. Python integer/Fraction and file handling remain software
trust assumptions; this is not formal verification. The original
certificate and script are preserved unchanged.

Since R>1.745, the proved normalized limit eventually exceeds1.745;
this rejects the universal3/2 upper coefficient on W intersected
with the form domain. No chosen finite return frequency is needed.
The audit establishes no exact supremum, complete-energy sign, parity
ordering or RH consequence. The separate absolute-budget and
neutral-prime stops remain intact. This is verification of the prior
local specialization, with no claim of a new result beyond its sources.

## Mathlib

Full matching Mathlib coverage for this fixed real-odd120-mode
specialization is not checked. Orthogonal projection in a Hilbert
space, finite trigonometric integration and exact rational inequalities
are standard supporting mathematics; no matching formal theorem name
is asserted. The precise external recurrence citation appears above.
This does not assert absence from Mathlib or a formalized RH result.
