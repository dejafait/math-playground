# C759e: The capped first sine has a positive complete-form modulus defect

## Hypotheses

Use exactly C759a's complete real closed form on zero-extended functions
supported in[-1,1], with Fourier convention F_f(t)=integral f(x)e^(-itx)dx:

\[
 Q(f)=\int_{\mathbb R}m(t)|F_f(t)|^2\frac{dt}{2\pi}
 +2F_f(i/2)F_f(-i/2)-2\sum_{n\in\{2,3,4,5,7\}}a_n C_f(\log n),
\]
\[
 m(t)=\Re\psi(1/4+it/2)-\log\pi,\quad
 a_n=\Lambda(n)/\sqrt n,\quad C_f(d)=\int f(x+d)f(x)\,dx.
\]

The domain is C759a's supported logarithmic Fourier domain. Its source
is Suzuki, *Weil's quadratic form via the screw function*,
[arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2#S2.SS4),
Section2.4, Theorem1.1 and the core/closure passages specified in C759a.
Use L741(7),(13),(16) only as full-line multiplier identities, from
the digamma integral [NIST DLMF5.9.13](https://dlmf.nist.gov/5.9.E13),
whose required argument has positive real part1/4. No finite-window
positivity theorem, semigroup sign or external computer certificate
is a premise. C759d supplies its separately audited unit first-sine
bound Q(s_1)<0.00364123566126519<1/250.

## Conclusion

For s_1(x)=sin(pi*x) on(-1,1), zero elsewhere, both s_1 and |s_1|
belong to H_0^1(-1,1) and the full form domain, and have L2 norm1.
The complete signed defect satisfies

\[
 \boxed{0.00111835<\Delta_1:=Q(|s_1|)-Q(s_1)<0.00111838.}
 \tag{1}
\]

Consequently there is no eta>0 such that Q(|f|)<=Q(f)-eta for every
real odd unit form-domain vector with Q(f)<=1/250. Even non-strict
modulus contraction fails on that sublevel. This is a fixed source
specialization, classified REPRODUCTION, and local negative evidence
for that comparison mechanism, with no novelty claim beyond sources
checked. It does not decide the actual parity infima, ground-state
sign/simplicity, all-window control, Xi realization or RH. The full
proof and certificate are recorded here. The separate conceptual and
complete scalar audit in Section5 accepts this fixed-pair stop.

## Proof

### 1. Domain and correlation

Put u(x)=sin(pi*x) on(0,1), zero elsewhere, and v(x)=u(-x).
Both are continuous piecewise C1 functions on R. Integration by parts
on their finitely many pieces gives their piecewise classical
derivatives as weak derivatives: all boundary terms cancel because
the values match, including zero at0 and the exterior endpoints.
These derivatives are in L2. Thus u,v, u-v=s_1 and u+v=|s_1| are in
H1(R), supported in[-1,1], with zero traces at plus/minus1, hence in
H_0^1(-1,1). The cusp at0 has no delta mass in the first derivative.
Plancherel's derivative identity gives integral (1+t^2)|F_f|^2 finite;
this implies both the logarithmic form norm and the squared-logarithm
multiplier norm are finite. The cited H_0^1 form identity applies.
Direct integration gives integral_(-1)^1 sin^2(pi*x)dx=1, also the
norm squared of its modulus.

For d>0 only the cross pairing with positive shifted coordinate can
survive. Expansion gives

\[
 C_{u+v}(d)-C_{u-v}(d)=2H(d),\quad
 H(d)=\int u(x+d)v(x)dx=(u*u)(d)\ge0.
 \tag{2}
\]

For 0<=d<=1, integrate sin(pi*a)sin(pi*(d-a)) over a in[0,d],
using the cosine product identity. For 1<=d<=2 use u(1-a)=u(a),
which makes H(2-d)=H(d). Thus with h=min(d,2-d),

\[
 H(d)=\tfrac12\left(\frac{\sin(\pi h)}\pi-h\cos(\pi h)\right)
 \quad(0\le d\le2),\qquad H(d)=0\quad(d>2).
 \tag{3}
\]

In particular H(d)=O(d^3) at0: before integration use
sin(pi*a)<=pi*a and sin(pi*(d-a))<=pi*(d-a).
This pays the singular kernel integral below without separately
evaluating divergent diagonal constants.

### 2. Archimedean defect with full regularization

L741's full-line identities set

\[
 k(d)=\frac{2e^{-d/2}}{1-e^{-2d}},\quad
 r(d)=k(d)-e^{-d}/d\in L^1(0,\infty),
\]
\[
 B_\epsilon f=\int_\epsilon^\infty\frac{e^{-d}}d
                  [f(\cdot-d)-f]dd,\quad
 B_\epsilon f\longrightarrow Bf\text{ in }L^2,
 \quad \widehat {Bf}(t)=-\log(1+it)F_f(t).
\]

The convergence holds for the present H1 tests by their squared-log
bound and L741(7)'s uniform multiplier bound. Let R be full-line
causal convolution by r. L741(16) gives
hat r(it)=log(1+it)-psi(1/4+it/2)-log2. Consequently, for
c=log(2*pi), Plancherel yields exactly

\[
 q_m(f):=\int m(t)|F_f(t)|^2\frac{dt}{2\pi}
       =-\Re\langle(B+cI+R)f,f\rangle.
\]

Indeed the real symbol of B+cI+R is -m. All pairings are valid in
L2: the B domain was checked, R is bounded by ||r||_1, and the
scalar is finite. No L741 positivity assertion at length log3 is used.
In the difference for u+v and u-v, the scalar term and the -f
subtractions in B_epsilon cancel by equal norms. The shift pairings
differ by 2H(d), since real autocorrelations are even. Passing to the
L2 limit, and combining r with e^(-d)/d, gives

\[
 q_m(u+v)-q_m(u-v)=-2\int_0^2 k(d)H(d)dd.
 \tag{4}
\]

The integrand is integrable by (3), k(d)=O(1/d) at0, and boundedness
away from0. The r pairings are justified by Fubini and
|C_f(d)|<=||f||_2^2, with r in L1.

Expand k(d)=2 sum_(j>=0) exp(-(2j+1/2)d), d>0. Tonelli applies
because H>=0. For b>0 the convolution Laplace identity, again by
Tonelli, gives

\[
 \int_0^2 e^{-bd}H(d)dd=
 \left(\int_0^1 e^{-bx}\sin(\pi x)dx\right)^2
 =\frac{\pi^2(1+e^{-b})^2}{(b^2+\pi^2)^2}.
\]

Therefore the exact archimedean defect is

\[
 \Delta_m=-4\sum_{j\ge0}
 \frac{\pi^2(1+e^{-b_j})^2}{(b_j^2+\pi^2)^2},
 \qquad b_j=2j+1/2.
 \tag{5}
\]

Keep j=0,...,511. For B=2049/2 the omitted unsigned series is in
[0,4*pi^2*R4], where

\[
 R4=B^{-4}+B^{-3}/6.
 \tag{6}
\]

This follows from (1+e^(-b))^2<=4 and (b^2+pi^2)^2>=b^4, then
the decreasing sum-integral bound
sum_(j>=512)b_j^-4<=B^-4+integral_512^infinity(2x+1/2)^-4 dx.
Multiplication by -4 puts the entire gamma-defect tail in
[-16*pi^2*R4,0]. There is no Fourier cutoff or missing exterior term.

### 3. Both poles and every overlapping prime power

Direct integration gives

\[
 I_\pm:=\int_0^1u(x)e^{\pm x/2}dx
       =\frac{\pi(1+e^{\pm1/2})}{\pi^2+1/4}.
\]

For u+v both imaginary Fourier values equal I_++I_-. For u-v they
are I_+-I_- and its negative. Retaining the signed product in Q,
the pole defect is consequently

\[
 \Delta_{pole}=2[(I_++I_-)^2+(I_+-I_-)^2]
              =4(I_+^2+I_-^2).
 \tag{7}
\]

By (2) the arithmetic defect is

\[
 \Delta_{prime}=-4\sum_{n\in\{2,3,4,5,7\}}
                   \frac{\Lambda(n)}{\sqrt n}H(\log n).
 \tag{8}
\]

These are all prime powers with log n<2; the certificate encloses
log7<2<log8. Every remaining prime power has zero correlation by
support. In particular n=4 uses Lambda(4)=log2, and neither its
contribution nor either pole has been dropped. Equations(5),(7),(8)
give Delta_1 exactly. No positivity assumption enters this evaluation.

### 4. Complete interval certificate

Reproduce with

    python3 scripts/spectral-triples/first-sine-modulus-810.py

The complete certificate is
`scripts/spectral-triples/first-sine-modulus-810.json`. It records all
512 series terms, their sum, the entire bound(6), all five signed
prime contributions with delay/branch/trigonometric values, pole
integrals, component sums, input cap, final interval, checks, failures
and script hash. The exact formulas above, rather than a numerical
quadrature preview, justify its infinite-dimensional evaluation.

The interval primitives are copied verbatim from the C759d step806
generator, independently audited in step808. Basic operations use
60-digit Decimal floor/ceiling contexts, including context-independent
negation. Division excludes zero. Monotone exp, ln and sqrt endpoints
are expanded by one adjacent representable value around the correctly
rounded operation; see the
[Python Decimal specification](https://docs.python.org/3/library/decimal.html).
Pi uses Machin's identity, pi=16atan(1/5)-4atan(1/239), with60
alternating terms in each series and the next-term remainder. For
sin/cos, reduction by integer multiples of2*pi bounds the argument
in modulus by4, and60 Taylor terms are followed by a two-next-term
absolute radius: every subsequent absolute-term ratio is below1/2.
Interval argument uncertainty is retained throughout. These methods
are supporting arithmetic reused from the audited entry, not a
reproof of the explicit formula. Python integer/Decimal correctness
is a software trust assumption; no Lean formal verification is claimed.

The certificate gives the full interval

\[
 \Delta_1\in[
 0.00111835366758016111273878882320840453855638637405461142901,
 0.00111837828647894582865025872041982873695830081444689419358].
\]

The gamma-defect tail lies in[-2.461890*10^-8,0]. All seven checks
pass with no failures; the written outward decimals in(1) follow.
The imported C759d upper endpoint is strictly below1/250, so s_1 is
eligible for the exact capped claim. Its positive defect contradicts
that claim for every eta>0. Neither evaluating the odd infimum nor
bounding Q(|s_1|) by the energy cap is required for this implication.
C998z's earlier unrestricted bump stop is consistent background,
not an input proving the cap for this different test.

### 5. Separate conceptual and complete scalar audit — 13 November2026, step812

The invocation-start SPECIALIZE assessment810, separately approved811,
covers this exact audit. Its source coverage and the audited C759d cap
are reused. No test family, window, energy cap or parameter was changed.

**Domain, convention and regularization.** On each of the intervals
cut by -1,0,1 the functions are classically differentiable. In weak
integration by parts, the endpoint terms involve the function values,
not the derivative values; those values agree at each join. Hence the
first weak derivatives are the bounded piecewise derivatives, with no
point mass at0 or the exterior endpoints. The zero traces give the
claimed H_0^1 membership. Since
|log(1+it)|^2 <= C(1+t^2), the H1 Plancherel estimate also puts all
four functions u,v,u+v,u-v in the full-line B domain of L741(7).
Its uniform truncated-multiplier bound therefore justifies strong L2
convergence and convergence of every pairing used in(4). This is
stronger than merely asserting finite logarithmic form energy.

The opposite Fourier sign in Suzuki does not alter this real form:
it replaces F(t) by F(-t), m is even, the two imaginary Fourier values
are exchanged, and real autocorrelations satisfy C_f(-d)=C_f(d).
There is consequently no sign change in the pole product or prime
coefficient. Direct substitution of L741(16) into the multiplier of
B+log(2*pi)I+R gives -psi(1/4+it/2)+log(pi), whose real part is -m.
Only that full-line identity is imported; its finite-window positivity
assertions are unnecessary.

For d>0, the mixed term v(x+d)u(x) vanishes by support, whereas
u(x+d)v(x) integrates to H(d). Expansion thus gives precisely2H(d)
in(2). The norms of u+v and u-v agree, so both the scalar term and
the subtraction inside B_epsilon cancel before any limit. The remaining
singularity is paid by H(d)<=pi^2*d^3/6 near0. The L1 kernel r permits
Fubini, and combining its pairing with the convergent B difference
gives the complete -2 integral kH, including its sign and factor2.
All exponential terms in kH are nonnegative, so Tonelli justifies(5)
without a conditional interchange. The support/reflection argument for
H on[1,2] and the convolution Laplace integral in Section2 check exactly.

**Signed terms and all infinite remainders.** Both imaginary Fourier
values of the odd vector have opposite signs. Subtracting its negative
pole product from the even product gives(7), not the square of only
one pole value. Each arithmetic term is -4*a_n*H(log n); n=4 has
Lambda(4)=log2. The exact integer list2,3,4,5,7, together with
log7<2<log8, exhausts the prime-power support. The multiplier constant
-log(pi) has already canceled with the equal norms; it is not an
unpaid term. For the omitted j>=512 terms, the decreasing integral
is B^-3/6 with B=2049/2 and the first omitted term B^-4 is included.
The unsigned estimate is multiplied by-4, hence its full interval
[-16*pi^2*(B^-4+B^-3/6),0] belongs at the lower end of the defect.
No Fourier or spatial tail is suppressed.

**Independent arithmetic and complete evidence.** Run

    python3 scripts/spectral-triples/first-sine-modulus-audit-812.py

The original generator and certificate are preserved byte-for-byte.
An exact-byte copy is replayed under ambient Decimal precision7 in
`scripts/spectral-triples/audit-812/`; every parsed field agrees with
the original. Replay alone is not the independent verification.

The second calculation uses the step808 audit's inspected Fraction
interval primitives. Basic operations use exact rational endpoints and
integer floor/ceiling rounding on a grid retaining at least100 significant
digits. Monotone ln, exp and sqrt use120-digit Decimal endpoint contexts
with adjacent-value expansion. Machin's formula uses80 exact rational
terms, with next-term remainder. Unreduced sine/cosine arguments use90
terms through degrees179/178. With |x|<7, twice the next absolute term
bounds each tail, because the subsequent ratios are below1/2.
These are independent of the generator's60-term reduced trigonometry.
The series term is separately evaluated as
pi^2*(1+exp(-b))^2/(b^2+pi^2)^2, and the pole defect is computed as
2*(I_plus+I_minus)^2 minus -2*(I_plus-I_minus)^2.

Every one of the512 series rows, all five complete prime rows, each
constant, partial sum, tail, component, imported-cap interval and result
interval is compared using exact rational inequalities against the
saved decimal endpoints. A recursive inventory verifies that all2102
saved intervals are checked, with none missing or extra. The full
certificate `scripts/spectral-triples/first-sine-modulus-audit-812.json`
records all2669 checks, independent enclosures, trigonometric errors,
hashes and no failures. Its independent final interval is contained
in the full original interval in Section4, and strictly inside(1).
The entire gamma-defect tail lies in[-2.461889879*10^-8,0]. Thus the
positive margin exceeds the paid uncertainty without using rounded
component summaries to establish the sign.

The separately audited C759d input is exactly the same unit odd sine
and normalization of Q; its upper bound0.00364123566126519 is below
0.004=1/250. The positive defect therefore refutes even non-strict
modulus contraction on the stated input sublevel. No cap on the
output modulus is required by that claim. No mathematical correction
was needed. This establishes local verification of the existing stop,
not a new theorem beyond the assessed specialization. Python integer
and Decimal/libmpdec correctness remain software trust assumptions;
actual parity infima, ground-state sign/simplicity, all-window control
and Xi realization remain open.

## Mathlib

Full matching coverage of the complete Weil-form identity and this
fixed-pair numerical certificate has not been checked. Plancherel,
the Fourier derivative identity, Tonelli and elementary real series
are supporting standard inputs. No absence or formalization claim
is made.
