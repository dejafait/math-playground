# C998u: A continuous derivative-measure kernel for the fixed remote energy

## Hypotheses

Use the unchanged real f=Zalpha and h=P0Uf of C998s, with C999l(1)'s
exact completion of the C998r witness, all512 raw modes, all334 shifts
of C744z(1), identity2187, full K14 and both exact projection moments.
Here ell=log(3)/2. The witness is
`scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
SHA256 `99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.
Use C998t's audited equality with the complete closed form, its real
zero-extended BV representative, and its bounds

    C(v)=integral_R h(x+v)h(x) dx, Delta(v)=C(0)-C(v),
    k(v)=2 exp(-v/2)/(1-exp(-2v)), d0=psi(1/4)-log(pi),
    a0(h,h)=d0 C(0)+integral_0^infinity k(v)Delta(v)dv,
    ||h||_infinity<M=2^20, TV_R(h)<B=2^23,
    0<=Delta(v)<=A v for v>=0, A=MB=2^43.              (1)

Retain the analytic-response, neutral-core, IEEE754/Decimal and
unreplayed c_* qualifications. This proof uses neither an inverse
estimate nor coercivity, approximate neutrality, RH or a cross-notebook
input. It does not revalidate the inherited source certificates.

Invocation-start assessment722/comparison723 is EXPLORE for this exact
bounded standard-method attempt. Supporting results are imported:

- Guermond, *Traces and interface jumps of finite elements*, Chapter14,
  Definition14.4 and Theorem14.6/full proof, pp176-177,
  [2016 primary PDF](https://people.tamu.edu/~guermond/M610_SPRING_2016/chap14.pdf).
  The broken-derivative proof retains classical cell derivatives and
  signed interface traces. Use dimension1, cellwise W^(1,1), in an
  ambient interval strictly larger than [0,ell]. Both support endpoints
  are then interfaces; they are not boundaries at which tests vanish.
- Dyatlov, *Lecture notes for18.155: distributions, elliptic regularity,
  and applications to PDEs*, title date2November2026,
  [primary PDF](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf),
  Section3.1/(3.3)-(3.4), p39; Theorem6.7/proof and Lemma6.8, pp71-73;
  Proposition8.4/proof, p89. Distributional differentiation, compact
  convolution and mollification are used only with the hypotheses
  below. Distributional convergence alone is not a measure-pairing limit.
- Beylkin--Monzon, *On approximation of functions by exponential sums*,
  Appl.Comput.Harmon.Anal.19(2005),17-48, DOI10.1016/j.acha.2005.01.003,
  Section5.3/(39)-(42), pp34-35,
  [published primary PDF](https://www.colorado.edu/amath/sites/default/files/attached-files/bey-mon-2005.pdf).
  Ordered sweeps apply to an already discretized density and already
  approximated exponential kernel. Neither preparation is free.

These general results are not reproved. The local kernel, measure
inventory and limits are the specialization missing from the sources.
No power-kernel approximation theorem at positive distance is used
at zero. Ordinary Fubini and dominated convergence for finite signed
measures are used only after checking absolute integrability.

## Conclusion

Let mu=Dh be the distributional derivative on R, including the two
zero-extension traces, and put, for r>=0,

    a_j=2j+1/2 (j>=0),
    G(r)=sum_(j>=0) exp(-a_j r)/a_j^2,
    H(r)=G(r)-(d0/2)r.                                 (2)

G is bounded and continuous on [0,infinity), including r=0. The
complete scalar has both absolutely convergent representations

    a0(h,h)=d0 C(0)+integral integral G(|x-y|) dmu(x)dmu(y)
            =integral integral H(|x-y|) dmu(x)dmu(y).    (3)

Section1 gives the full density and every atom. No atoms-only formula
is asserted. Section2 proves the regularized identity and removes
the regularization in the required measure pairing. The j=0 term,
diagonal atom self-interactions, density-density and atom-density
terms all remain. The original infinite support tail is included.

Section3 tests ONE uncompressed aggregate prescription: truncate (2)
after N exponentials, choose the least N satisfying its stated BV
tail budget1e-7, then apply one ordered sweep per exponential. It needs

    N=43,980,465,111,040,000,001                         (4)

scalar accumulations even if every swept value is supplied at zero
cost, against10^8 operations for all work. This stops that sufficient
prescription before density quadrature, precision or a scalar batch.
It is not an actual-error lower bound, nor a lower complexity bound for
compressed, tail-corrected or otherwise reassociated algorithms.

This is a local REPRODUCTION advance in representation, with a failed
evaluation prescription, not progress beyond the general methods
checked. Separate conceptual audit726 in Section4 upholds the identity
and the limited cost stop under the same contracts. No complete numerical
scalar, affordable ledger, signed S3 statement or RH candidate results.
Other entries/endpoints, C744q/H2 and actual-Xi/global assembly remain.

## Proof

### 1. The entire zero-extension derivative

For n in C744z's P14 set

    q_n=Lambda(n)/sqrt(n), d_n=log(2187/n),
    l_n=max(0,-d_n), r_n=min(ell,ell-d_n), I_n=(l_n,r_n),
    s(x)=integral_0^ell K14(x,y)f(y)dy
                            -t_+exp(x/2)-t_-exp(-x/2),
    t=G_mom^-1 (integral_0^ell (Uf)(x) exp(+/-x/2)dx).

G_mom is C998s(6)'s exact two-by-two moment Gram matrix; it is distinct
from the kernel G in (2). All I_n have positive length. On (0,ell),
h=sum_n q_n 1_(I_n)f(x+d_n)+s(x). Each summand has smooth one-sided
traces, and the full kernel's derivative series converges uniformly
on the square by C998s(4). In particular, writing c_j=2j+1/2,

    partial_x K14(x,y)=-sum_(j>=1)c_j exp[-c_j(14ell+x-y)].

Thus the classical density on the open pieces, defined a.e., is

    b(x)=sum_n q_n 1_(I_n)(x) f'(x+d_n)
          +integral_0^ell partial_x K14(x,y)f(y)dy
          -(t_+/2)exp(x/2)+(t_-/2)exp(-x/2).           (5)

It is integrable. Apply the cited broken-derivative formula to this
finite partition and the two outer zero pieces. This gives exactly

    mu=1_(0,ell)b(x)dx
       +sum_n q_n[f(l_n+d_n)delta_(l_n)
                              -f(r_n+d_n)delta_(r_n)]
       +s(0)delta_0-s(ell)delta_ell.                   (6)

Here every endpoint value is its analytic one-sided trace. Combining
equal locations, the two outer atoms are h(0+)delta_0 and
-h(ell-)delta_ell. For n>2187 the interior atom is
q_n f(0)delta_(log(n)-14ell); for n<2187 it is
-q_n f(ell)delta_(log(n)-13ell). The identity n=2187 has no interior
atom, but contributes to the density and both outer traces. The
interior locations are distinct: two of the same type are distinct
by injectivity of log; an entrance and exit coinciding would imply
n^2=3m^2, impossible by parity of the3-adic valuation. Zero amplitudes
are permitted; no nonzero jump amplitude is presumed.

The exact P0 changes both b and the outer traces. Full K14 changes
both as well. Its infinite series has not been numerically truncated.
The total variation norm of (6) is TV_R(h)<B, and mu(R)=0, either
by telescoping the cell integrals and traces or by testing Dh against
a compactly supported function equal to1 near [0,ell]. This verifies
compact support and finite signed-measure hypotheses, not an H1 claim.

### 2. Regularization, the continuous kernel and complete scalar

For a>0 let E_a(t)=exp(-a|t|). Its classical derivative has jump -2a
at0, so the cited distributional jump rule gives

    E_a''=a^2 E_a-2a delta_0.                         (7)

Choose a nonnegative smooth mollifier rho of integral1 supported in
[-1,1], and h_e=rho_e*h, mu_e=rho_e*mu=Dh_e. For 0<e<1 these
are smooth and supported in [-1,ell+1], and ||mu_e||_TV<=B. The
full-line BV translation bound already used in C998t gives
||h_e-h||_1<=Be. Boundedness by M then gives
||h_e-h||_2^2<=2MBe, so h_e tends to h in L2.

For this smooth compactly supported h_e, distributional integration
by parts in both variables is legitimate. Since
partial_x partial_y E_a(x-y)=-E_a''(x-y), (7) gives

    integral integral E_a(x-y)dmu_e(x)dmu_e(y)
      =2a ||h_e||_2^2
          -a^2 integral integral E_a(x-y)h_e(x)h_e(y)dxdy.

Pass to the actual measure with an explicit estimate. Expressing
mu_e as averages of translates of mu, Fubini is justified by bounded
E_a and finite total variation. E_a is Lipschitz with constant a;
the two translations change its argument by at most2e. Hence

    |pair_(mu_e)(E_a)-pair_mu(E_a)|<=2ae B^2 ->0.

This is convergence against a continuous kernel, not just against
smooth distributional tests. On the function side, Cauchy--Schwarz
gives uniform convergence of the correlations C_e to C. Their error
is at most (||h_e||_2+||h||_2)||h_e-h||_2. Since E_a is integrable,
the double function integral also converges. For real h the correlation
is even, so the resulting identity is

    Q_a:=pair_mu(E_a)=2a C(0)-2a^2 integral_0^infinity e^(-av)C(v)dv
                    =2a^2 integral_0^infinity e^(-av)Delta(v)dv>=0. (8)

In the last equality use integral_0^infinity e^(-av)dv=1/a. This
integrates over all v, including v>=ell where C(v)=0. It does not
omit C998t's support-tail multiple of C(0).

For N>=1 put G_N(r)=sum_(j=0)^(N-1)exp(-a_j r)/a_j^2.
The series of suprema sum_j a_j^-2 is finite, so G_N converges
uniformly on [0,infinity) to a bounded continuous G. Finite signed
measure integration therefore gives pair_mu(G_N)->pair_mu(G), with
absolute error at most B^2 sum_(j>=N)a_j^-2. Summing the finite
identities(8) yields

    pair_mu(G_N)=integral_0^infinity
                      [2 sum_(j<N)exp(-a_j v)]Delta(v)dv.

The nonnegative integrands increase to k(v)Delta(v), and C998t(1)
has already proved that limiting integral finite. Monotone convergence
identifies pair_mu(G) with the full nonlocal energy in (1). This
proves the first equality in (3). No differentiation of the infinite
kernel at zero, or interchange against a singular kernel, was used.

For the second equality use (|t|)''=2delta_0 in the same smooth
integration by parts. It gives pair_(mu_e)(|x-y|)=-2||h_e||_2^2.
All measures have common compact support and |t| is Lipschitz1;
the same averaging estimate bounds the measure-pairing error by
2eB^2. Thus pair_mu(|x-y|)=-2C(0), proving the second equality.
H is bounded on the actual distance interval [0,ell], which suffices
for absolute convergence. The d0 term has not been discarded or
assigned a sign favorable to the full form.

To make all interactions explicit, write the combined version of (6)
as mu=b(x)dx+sum_(z in Z_atoms)w_z delta_z. For F(r)=G(r) or H(r),
the pairing means

    integral_0^ell integral_0^ell F(|x-y|)b(x)b(y)dxdy
    +2 sum_z w_z integral_0^ell F(|z-y|)b(y)dy
    +sum_(z,z') w_z w_(z') F(|z-z'|).                  (9)

Each integral is absolutely convergent because b is L1, the atom
list is finite and F is bounded on [0,ell]. Terms z=z' are included
once and use G(0)=H(0)=sum_j a_j^-2, which is finite. Boundedness
of G does not turn the derivative measure into a purely atomic one.

### 3. One aggregate prescription and its preflight stop

Select the uncompressed geometric prefix G_N and retain the exact
local term d0 C(0), equivalently the linear part of H. The error in
the nonlocal part is nonnegative by (8), and (1) gives the better
of the following two sufficient bounds:

    0<=pair_mu(G-G_N)<=2A sum_(j>=N)a_j^-2
                            <=2A/(4N-3), N>=1.        (10)

For comparison, uniform kernel approximation alone gives B^2 times
the same sum, and 2A<B^2. To prove the last inequality in (10), the
positive function (2x+1/2)^-2 is decreasing on [0,infinity), so its
sum from N is at most its integral from N-1 to infinity, namely
1/(4N-3). This is a bound on the exact full-density tail. It is not
an estimate for the atoms alone. The infinite original response is
retained by this certified remainder, rather than silently dropped.

Fix epsilon_tail=1/10^7, reserving9/10^7 for all other errors. The
selected rule takes the least positive integer satisfying

    2A/(4N-3)<=epsilon_tail.

Equivalently N>=ceil((2A*10^7+3)/4), giving (4). At N-1 the bound
is greater than epsilon_tail. This minimality concerns this chosen
majorant rule; it says nothing about the actual tail at smaller N.

The intended application aggregates the complete discretized measure
before evaluating each exponential, avoiding Section8 of C998t's
separate piece-pair resonant products. For sorted distinct nodes x_i
and real weights v_i, including density-quadrature weights and atoms,
the imported sweep can be written with strict left/right ownership:

    L_1=0, L_i=exp(-a(x_i-x_(i-1))) (L_(i-1)+v_(i-1)),
    R_last=0, R_i=exp(-a(x_(i+1)-x_i)) (R_(i+1)+v_(i+1)),
    Q_a(discrete)=sum_i v_i(L_i+v_i+R_i).

Coincident locations must first be merged exactly or their uncertainty
paid; the central v_i supplies the diagonal once. The real exponents
are negative as required for stable propagation in the cited tool.
This is only an application template: the source assumes the density
has already been discretized with sufficient accuracy. It does not
supply that quadrature or allow replacement of a density by atoms in
total-variation norm.

The specified outer loop separately adds Q_(a_j)/a_j^2 for every
j=0,...,N-1. Count only one real accumulation per exponential,
assigning every value, weight, node and sweep at zero favorable cost.
The loop still takes at least N operations, over4.39e19>1e8. Even
giving the tail the entire1e-6 error allowance would select
N=4,398,046,511,104,000,001>1e8 by the same rule. No precision or
preparation optimization rescues this particular fixed outer loop.

The ledger stops here. Tail omission is paid by (10); density
quadrature and its mixed terms, full512-mode/334-shift preparation,
K14 evaluation, exact-moment enclosures, uncertain positions,
elementary evaluations, rounding/cancellation, C(0)/d0, sufficient
precision and bytes are all unpaid. Their nonnegative costs can only
increase this fixed-loop count. No total-error certificate or scalar
is claimed. A smaller N justified by a sharper bound, diagonal-tail
extraction, or approximation by a different compressed exponential
sum would be a different prescription requiring its own bounded test.

Run `python3 scripts/separation-seven/remote-image-measure-preflight-724.py`.
The full small certificate is
`scripts/separation-seven/remote-image-measure-preflight-724.json`.
It checks the rational cutoff inequalities and work comparison and
reverifies the unchanged witness hash. It does not verify this analytic
proof or execute a sweep, density quadrature, energy or Gram batch.
Preserve stops617/603/635/640/652/705/712/716/720/722. This stop is
specific to the uncompressed tail-majorant prescription, not to (3).

### 4. Separate conceptual audit — 13 November2026, step726

The invocation-start SPECIALIZE assessment724, with source-link repair725,
covers this exact audit. The primary statements and relevant proof cases
in its comparison723 are reused. The full C998u proof, C998t Sections1-3/6,
C998s Sections1-2 and audit714, C744z(1), C999l(1) and the fixed C998r
witness definition were checked. No mathematical error requiring a repair
was found. This is verification of a local standard-method specialization,
not a new theorem beyond the methods cited above.

**The finite partition and all traces.** From 3^13<n^2<3^15 one has
13ell<log(n)<15ell, hence -ell<d_n<ell. Thus every I_n has positive
length. Finite cosine f and the uniformly convergent derivative series
for K14 give a W^(1,1) function on each of the finitely many open pieces,
with one-sided traces. The exact moment matrix is invertible by C998s(6).
The smooth derivative is therefore precisely (5); in particular the
derivative of -t_-exp(-x/2) is positive t_-exp(-x/2)/2.

For an arbitrary compact smooth test phi, each translated piece gives

    -integral_(l_n)^(r_n) q_n f(x+d_n) phi'(x)dx
      =integral_(l_n)^(r_n) q_n f'(x+d_n) phi(x)dx
         +q_n f(l_n+d_n)phi(l_n)-q_n f(r_n+d_n)phi(r_n).

The smooth s contributes its classical derivative and s(0)phi(0)
-s(ell)phi(ell). This applies the cited broken-derivative proof, using
the outer zero pieces as well, and verifies every term of (6). For
n>2187, l_n=log(n)-14ell and r_n=ell; for m<2187, l_m=0 and
r_m=log(m)-13ell. Equality of these two interior locations would give
log(n/m)=ell, hence n^2=3m^2, contradicting the parity of the3-adic
valuation. The identity2187 has l=0,r=ell. Outer atoms combine to
h(0+) and -h(ell-); their values are traces, irrespective of chosen
point values of the BV representative. Vanishing amplitudes are allowed.
There is neither a deleted endpoint nor an assumed nonzero endpoint.

The integrable density and finite atom list define a real finite signed
measure supported on [0,ell]. By the distributional BV derivative
definition its total variation is TV_R(h)<B. Testing with a function
equal to1 near the support verifies total mass zero. This does not
identify h with an H1 function across the jumps.

**Two distinct limits and the cusp normalization.** Nonnegative compact
mollification gives ||mu_e||_TV<=||mu||_TV<B and support within
[-1,ell+1] for e<1. Averaging the imported BV translation estimate
gives ||h_e-h||_1<=Be; the common supremum M gives the squared L2
bound2MBe. The distributional derivative commutes with convolution,
so mu_e=h_e' dx. These are exactly the compact-support hypotheses
needed for the cited convolution results.

At0, E_a' has right trace -a and left trace a. Its derivative thus
contains -2a delta_0. Moving both derivatives from h_e to E_a has
positive integration-by-parts sign, whereas differentiating once in
x and once in y gives -E_a''. Consequently the delta contribution is
+2a||h_e||_2^2 and the ordinary kernel contribution has coefficient
-a^2. This independently fixes both signs and the factor2 in (8).

For the measure limit, write the two convolutions explicitly as
averages over shifts u,v of size at most e. Since ||E_a||_infinity<=1,
the absolute Fubini bound is B^2; the change of argument is u-v.
The global Lipschitz bound a yields error<=2aeB^2. This is a direct
continuous-kernel pairing estimate, not an appeal to convergence in
distributions. Independently, the correlation difference is uniformly
bounded by (||h_e||_2+||h||_2)||h_e-h||_2, which tends to0.
The weight exp(-a|v|) has integral2/a, so it pays passage to the
double function integral on the whole line. Real h makes C even.
Inserting integral_0^infinity exp(-av)dv=1/a then gives exactly (8).
Delta(v)>=0 is the translation-square identity from C998t, not an
assertion that the signed product measure is positive.

The uniform majorant sum_j a_j^-2 is summable, including j=0, so
G_N converges uniformly at r=0 as well as elsewhere. Finite signed
measure pairing is continuous for this sup norm, with bound B^2.
Only after finite summation of (8) is monotone convergence applied,
to the nonnegative Lebesgue integrands 2 sum_(j<N)exp(-a_j v)Delta(v).
Their limit is k(v)Delta(v); C998t proves its integrability at both
ends. For v>=ell, C(v)=0 a.e. and Delta(v)=C(0), so the support tail
is still present. No infinite derivative of G at0 is used.

For |x-y| the same integration by parts gives -2||h_e||_2^2.
All supports lie in the same compact interval, so this unbounded
full-line kernel is bounded on the relevant product support; its
Lipschitz constant1 gives pairing error<=2eB^2. The limit is
-2C(0). Multiplication by -d0/2 therefore contributes +d0 C(0),
the required local term. G and H are bounded on [0,ell]; b is L1
and the atom list is finite. These facts prove absolute integrability
of every component of (9). The symmetric mixed terms have factor2;
ordered distinct-atom pairs and single diagonal terms are all retained.
Nonnegativity of the nonlocal part does not sign the complete a0.

**The stopped prescription and its exact arithmetic.** From (8) and
Delta(v)<=Av, each omitted weighted term obeys

    Q_(a_j)/a_j^2 <= 2A integral_0^infinity v exp(-a_j v)dv
                   =2A/a_j^2.

For j>=N>=1, the decreasing function (2x+1/2)^-2 has value at j
no greater than its integral over [j-1,j]. Summing and integrating
gives 1/(4N-3), exactly the majorant in (10). The uniform-TV
alternative has coefficient B^2=2^46, whereas 2A=2^44.

With budget1/d, d=10^7 or10^6, the integer condition is
4N-3>=2A d. In both cases 2A d is divisible by4. Thus
N=(2A d)/4+1, and the two integer margins at N and N-1 are
respectively1 and -3. This proves minimality for the stated rule,
without evaluating the true tail. The two cutoffs in Section3 follow.

Induction in the sweep recurrence gives
L_i=sum_(k<i)exp[-a(x_i-x_k)]v_k and
R_i=sum_(k>i)exp[-a(x_k-x_i)]v_k. Its central v_i therefore owns
the diagonal exactly once; off-diagonal ordered pairs occur with
their required multiplicity. This requires completed quadrature and
merged distinct nodes, as stated. A density discretization is not
being justified by total-variation convergence to an atomic measure.
The outer loop is explicitly N separate accumulations, even under
the favorable zero-cost assignment for every inner value. This
establishes only the given prescription's work failure against10^8.

Run `python3 scripts/separation-seven/remote-image-measure-audit-726.py`.
The independent certificate is
`scripts/separation-seven/remote-image-measure-audit-726.json`.
All20 finite checks pass. Integer minimality, exact rational bounds,
all original cutoff/work fields and the witness hash were checked;
the original724 script, certificate and witness were left unchanged.
Complete selected cases, checks, hashes, failures and unpaid fields
were inspected. This program does not verify the analytic proof.

No scalar, Gram, density quadrature, sweep or large loop was executed.
Stop724 remains specific to its majorant-selected uncompressed loop;
it is neither an actual-tail lower bound at smaller N nor a general
complexity obstruction. Density/mixed-term errors, preparation,
locations, rounding, local-term evaluation, precision and bytes remain
unpaid. All inherited analytic-response, neutral-core, IEEE754/Decimal
and unreplayed c_* qualifications remain. No inverse or RH premise
was used and no direct mathematical dependency was added. Signed S3,
other entries/endpoints, C744q/H2 and actual-Xi/global assembly stay open.

## Mathlib

Full matching coverage for this fixed-h measure inventory, continuous
kernel identity and sufficient-work prescription has not been checked.
The cited distribution, BV and sweep results are supporting inputs,
not a formalization of (3). The exact arithmetic script is not a
Mathlib proof. No absence claim or formal verification is asserted.
