# C750d: Explicit coefficient-space zero-tail bound for the fixed U12 screen

## Hypotheses

Put T=4log(3), delta=T/40 and I=(0,T). Use C750a's exact cutoff

    eta(s)=exp(-1/s) for s>0, and 0 otherwise,
    theta(s)=eta(s)/(eta(s)+eta(1-s)),
    chi(x)=theta((x-delta)/delta)*theta((T-delta-x)/delta),
    phi_k(x)=chi(x)sin(k*pi*x/T), k=1,...,12,
    mu_k=integral_I exp(x/2)phi_k(x)dx.

All functions are extended by zero. Let V be the common kernel of
the two complex moments integral exp(+-x/2)f(x)dx in the complex span
of phi_1,...,phi_6. Use precisely C750c Proof5/(15)'s ordered basis:

    b_(p,j)=phi_(p+2j)-(mu_(p+2j)/mu_p)phi_p,
    e_(p,1)=b_(p,1), e_(p,2)=b_(p,2),
    e_(p,j)=b_(p,j)-P_V b_(p,j), j=3,4,5, p=1,2.       (1)

Here P_V is the exact original L2 orthogonal projection, not a
coefficient-space or midpoint projection. The order is p=1, j=1,...,5,
then p=2, j=1,...,5. C750c proves that these are a basis of the
ten-dimensional neutral U12, with exact moment cancellation over C.
For c in C^10 put

    f=sum_(p,j) c_(p,j)e_(p,j),
    ||c||_2^2=sum_(p,j)|c_(p,j)|^2,
    F(z)=integral f(x)exp(-izx)dx, F#(z)=conjugate(F(conjugate(z))),
    H=3000000000000, z_rho=(rho-1/2)/i.                  (2)

The sum over rho includes every nontrivial zeta zero with its full
multiplicity. L018 gives |Im z_rho|<1/2 and both height signs.
Use L753's audited time-zero identity and strip estimate (10), with
N=2. Its full explicit-formula hypotheses on a wider strip have
already been verified there; a half-strip bound alone is not a
replacement for that applicability proof. For the cutoff derivatives
use the analytically justified, audited bounds in L750 Proof3/(11):
|theta'|<=5 and |theta''|<=352 on R. No numerical moments, projection
coefficients, zero ordinates or energy matrix intervals are inputs here.

Import, without reproof, Brent--Platt--Trudgian, *Accurate estimation
of sums over zeros of the Riemann zeta-function*, Math.Comp.90(2021),
2923--2935, [Lemma1 and footnote1, printed p2923](https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf),
[DOI10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652).
For 2pi*e<=T1<=T2 and nonnegative decreasing phi its statement is

    sum'_(T1<=gamma<=T2) phi(gamma)
      = integral_(T1)^(T2) phi(t)log(t/(2pi))dt/(2pi)
        + A*theta0*(2phi(T1)log(T1)
                       +integral_(T1)^(T2)phi(t)dt/t),
    |theta0|<=1, A=7/25.                               (3)

This counts all upper-half-plane nontrivial zeros, with multiplicity
and half endpoint weights. It does not assume RH. The function phi
below is the scalar power envelope, not the complex Fourier product.
The stronger source theorem's extra hypotheses are not used.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-14-neutral-zero-tail-coefficient-bound-876.md`.
This is a REPRODUCTION/known-method specialization; the explicit local
constants are the contribution, with no novelty claim beyond sources.

## Conclusion

The complete high-zero remainder is absolutely convergent and satisfies

    R_H(c)=sum_(|Re z_rho|>H) F(z_rho)F#(z_rho),
    |R_H(c)| <= epsilon_* ||c||_2^2,
    epsilon_*=(36*10^9)^2*[91/(27H^3)+1687/(50H^4)]
       =4550000000015183/28125000000000000000000000000000
       <2*10^(-16).                                    (4)

This is in the stipulated coefficient Euclidean norm, not ||f||_2.
Neither reality nor a nonnegative sign of individual high terms is
assumed. The whole remainder is real by conjugation symmetry and
absolute convergence, but (4) pays its absolute value.

A future finite zero-Gram lower bound must exceed this error and all
finite-input errors in the same coordinates. No such margin is supplied.
The estimate proves no U12 sign, infinite-complement positivity,
non-neutral sign, all-degree mixed positivity, global assembly or RH.
The independent conceptual audit879 below accepts this informal
specialization without changing its constants or hypotheses. This is
local validation of a known-method specialization, not a possible
complete solution of RH or a discovery beyond the sources checked.

## Proof

### 1. Coarse exact moment and retained-metric bounds

We use 4<T<5, 3<pi<4, and exp(T/2)=9. For completeness e<3 follows
from its factorial series and n!>=2^(n-1), with a strict inequality
for n>=3. Also exp(5/4)>1+5/4+25/32>3. Thus 1<log3<5/4.
The cutoff obeys 0<=chi<=1, is symmetric about T/2, and equals one
on [T/20,19T/20]. It is supported in [delta,T-delta]. Consequently

    |mu_k| <= integral_0^T exp(x/2)dx=16.                (5)

On [T/4,3T/4] we have chi=1, sin(pi*x/T)>=1/2 and exp(x/2)>=1.
Since phi_1 is nonnegative everywhere, mu_1>=T/4>1. Reflection gives

    -mu_2=integral_0^(T/2) chi(x)sin(2pi*x/T)
                        [exp((T-x)/2)-exp(x/2)]dx.

The integrand is nonnegative. On [T/8,T/4], chi=1,
sin(2pi*x/T)>=sqrt(2)/2>2/3, and the bracket is at least
exp(3T/8)-exp(T/8)=2sqrt(3)>10/3. Hence

    -mu_2 > (T/8)*(20/9)=5T/18>1.                     (6)

Thus all exact ratios in (1) have absolute value <16. Every b_(p,j)
has sine coefficient l1 norm <17 and L2 norm at most 17sqrt(T).
These estimates do not depend on finite-precision denominator tests.

Fix p and write a=(a_1,a_2) in C^2. The function
g=a_1 b_(p,1)+a_2 b_(p,2) equals chi times a three-mode sine sum
with coefficients d at modes p,p+2,p+4. The latter two coefficients
are a_1,a_2, so ||d||_2^2>=||a||_2^2. Exact sine orthogonality on
(0,T) gives the uncut norm squared (T/2)||d||_2^2. The region where
chi differs from one has measure at most T/10. At every point the
uncut sine sum has modulus squared <=3||d||_2^2, by complex
Cauchy--Schwarz. Subtracting its entire possible cutoff loss gives

    ||g||_2^2 >= (T/2-3T/10)||d||_2^2
               >=(T/5)||a||_2^2.                      (7)

In particular the two-by-two original L2 Gram is >=(T/5)I. No bound
on the complete ten-mode Gram is inferred from this three-mode test.
Reflection parity makes the two retained sectors L2 orthogonal, as
proved in C750c. Thus the full P_V of a b in sector p uses only the
two retained b in that sector. Write P_V b=a_1 b_(p,1)+a_2 b_(p,2).
The contraction property of orthogonal projection and (7) imply

    sqrt(T/5)||a||_2 <=||P_V b||_2<=||b||_2<=17sqrt(T),
    |a_1|+|a_2| <=sqrt(2)||a||_2<=17sqrt(10)<68.        (8)

Subtracting this exact projection therefore bounds each projected e's
sine coefficient l1 norm by 17+68*17=1173. The unprojected first two
coordinates also satisfy this bound. This controls the original L2
projection in (1), without substituting an orthogonalization in the
ten-dimensional coefficient metric.

### 2. Uniform spatial constants in the stipulated coordinates

The two cutoff transitions are disjoint and the other cutoff factor
equals one on either transition. From L750(11) and delta=T/40>1/10,

    ||chi'||_infinity<=5/delta<50,
    ||chi''||_infinity<=352/delta^2<35200.

For k<=12, k*pi/T<12. The product rule gives

    ||phi_k''||_infinity
      <35200+2*50*12+12^2=36544<37000,
    ||phi_k||_1+||phi_k''||_1
      <5*(1+37000)=185005<200000.                      (9)

Flat joins and smooth zero extension are included; there are no
distributional boundary contributions. Each e has the fixed sine
coefficient bound 1173, so the triangle inequality gives
||e||_1+||e''||_1<=1173*200000. A second triangle inequality and
complex Cauchy--Schwarz in the TEN coordinates yield

    ||f||_1+||f''||_1
      <=1173*200000*sum_(p,j)|c_(p,j)|
      <=1173*200000*sqrt(10)||c||_2
      <938400000||c||_2<=10^9||c||_2.                 (10)

For c=0 all ensuing bounds hold trivially. For other c the displayed
strict estimates are valid. Use L753(10) with support radius R=T>1,
b=1/2 and N=2. Since exp(T/2)=9, it gives

    |F(x+iy)|, |F#(x+iy)|
        <=36*10^9 ||c||_2 (1+|x|)^(-2), |y|<=1/2.    (11)

The second bound uses reflected conjugation on the symmetric strip.
At a nonreal zero the product remains F(z)F#(z); it is not replaced
by |F(z)|^2. L018's strip and (11) give, for gamma=Re z_rho with
|gamma|>H,

    |F(z_rho)F#(z_rho)|
      <=(36*10^9)^2||c||_2^2 |gamma|^(-4).             (12)

### 3. Complete unconditional power tail and endpoints

Apply the cited (3) to phi(t)=t^(-4), T1=H. This is nonnegative
and decreasing; H>24>2pi*e. Its main integral and error integrals
converge. Taking upper bounds in (3) and letting T2 tend to infinity
through heights that are not ordinates gives

    sum_(gamma>H) gamma^(-4)
      <=H^(-3)/(6pi)*[log(H/(2pi))+1/3]
          +(7/25)H^(-4)*[2log H+1/4].                (13)

Indeed the partial sums at such T2 are nonnegative and increasing,
and the uniform finite upper bound proves their convergence. The
limit of the primed sums additionally contains half the contribution
at H, if any. Dropping that nonnegative term is valid for the strict
cutoff in (13). No endpoint zero-freeness, simplicity or RH is used.

Now log H<30: the series gives e>8/3, and the exact integer inequality
8^30>H*3^30 implies exp(30)>H. Also pi>3. Therefore the right side of
(13) is at most the strictly larger rational bound

    91/(54H^3)+1687/(100H^4).                          (14)

For clarity, the coefficients are (30+1/3)/18=91/54 and
(7/25)*(60+1/4)=1687/100. L018's zero symmetries preserve
multiplicity and pair positive and negative heights, so the complete
sum of |gamma|^(-4) at |gamma|>H is bounded by twice (14). Combining
with (12) proves absolute convergence and the first inequality (4).
This also agrees with the absolute convergence already furnished by
L753 for each fixed f. Conjugation of Xi's zeros pairs conjugate
product values, giving reality of R_H after absolute convergence;
this observation is unnecessary for its bound.

All scalar arithmetic in (4)--(14) is checked by

```sh
python3 scripts/neutral-zero-tail/check-877.py
```

Its complete exact-rational certificate is
`scripts/neutral-zero-tail/certificate-877.json`. Eleven scalar checks
pass, including the strict epsilon comparison in (4). It checks the
integer exponential comparison and rational constants, not the
analytic projection argument or the imported theorem. No floating
point computation or numerical zero evidence occurs in this proof.

The bound is one input to a possible later finite Gram screen. The
finite lower margin is unknown, so smallness of (4) is not a
positivity comparison. The earlier scalar-floor rejection and exact
energy-entry inconclusiveness in C750c remain intact.

### 4. Independent conceptual audit, 14 November 2026, step879

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-14-neutral-zero-tail-audit-877.md` covers
exactly (1)--(4). The audit accepts (4) for every complex coefficient
vector, including zero. No numerical moment, approximate projection,
finite-zero census or finite Gram sign is used. The following checks
address the analytic claims that the scalar certificate cannot verify.

**Moment signs and the original metric.** The lower bound for mu_1
restricts a nonnegative integrand to [T/4,3T/4]. After reflection,
the integrand for -mu_2 is nonnegative on (0,T/2). On [T/8,T/4]
the bracket in (6) decreases to 2sqrt(3); hence restriction to this
interval is legitimate and gives -mu_2>5T/18>1. Together with (5)
this verifies the ratios used in every b, independently of saved
interval data. C750c Proof1 and the definition in Proof5/(15) give
both complex moment constraints: on a parity sector the negative
moment is the positive moment times the same signed exp(-T/2).
Subtracting vectors of V preserves these constraints.

For complex d, orthogonality of the three uncut sines gives exactly
(T/2)sum |d_k|^2. On the two end strips, of total measure T/10,
complex Cauchy--Schwarz gives |sum d_k sin(k*pi*x/T)|^2
<=3 sum |d_k|^2. Since 0<=1-chi^2<=1, this proves (7) in the
original complex L2 metric. The coefficient of each of the two
non-anchor modes is precisely the corresponding a_j; no lower
bound on the other coefficients is needed. Reflection is a unitary
involution of L2(0,T), so its two parity eigenspaces are orthogonal
also over C. A b in one sector therefore projects onto that sector's
two retained b only. Orthogonal projection is contractive in L2;
(7) consequently proves (8), and the sine coefficient l1 bound
17+68*17=1173 follows. This does not assert that the ten e are
orthonormal or that their full L2 Gram has lower bound T/5.

**Smooth constants and strip applicability.** L750 Proof3/(11),
with its audited derivative recursion, supplies the global bounds
5 and352. The transition intervals are [delta,2delta] and
[T-2delta,T-delta], and the other factor equals one on each.
Thus no product cross term is missing in the chi derivative bounds.
Flatness at their endpoints permits two integrations by parts in
the smooth zero extensions. The product-rule bound is36544, and
the subsequent L1 estimates use support length at most T<5.
The original-coordinate triangle inequality and complex
Cauchy--Schwarz give (10); no inverse ten-mode Gram is required.

The support lies in [-T,T]. L753(10) with R=T,N=2,b=1/2 gives
A=4 exp(T/2)*10^9||c||_2=36*10^9||c||_2. Since
|F#(x+iy)|=|F(x-iy)|, the same bound holds for both factors
throughout the entire zero strip. The product in (12) is therefore
bounded in absolute value even when z_rho is nonreal and c is complex.
No off-axis modulus-square identity is asserted.

The explicit-formula application has the stronger domain required
by Carneiro--Milinovich, arXiv:2403.17803v1 Section2.2 Lemma4,
as cited in L753: compact smooth f makes both factors entire, and
L753(10) with b=1,N=2 gives product decay O((1+|Re z|)^(-4))
uniformly on |Im z|<=1. This supplies epsilon=1/2 and decay exponent
delta=3 there. Both pole evaluations vanish by the exact moments.
Thus L753's time-zero identity applies; the quantitative half-strip
estimate is not used as a substitute for the wider-strip hypothesis.
Only this already audited specialization is used, not a new proof
of the explicit formula or any neighboring RH-conditional theorem.

**Unconditional tail, limits and symmetry.** Use the cited BPT
Lemma1/footnote1 exactly as assessed before invocation. The scalar
weight t^(-4) is smooth, nonnegative and decreasing on [H,infinity),
and H>24>2*pi*e. Direct integration of its main term gives
H^(-3)[log(H/(2*pi))+1/3]/(6*pi), while its error integral is
H^(-4)/4. To justify the limit, take increasing heights Y_n tending
to infinity that avoid zero ordinates. Such heights exist because
zeros of the nonzero entire xi are discrete and the strip has finite
width. The primed finite sums equal

    (m_H/2)H^(-4) + sum_(H<gamma<Y_n) gamma^(-4),

where m_H is the total multiplicity at positive ordinate H.
They increase and have the uniform finite bound obtained from (3)
by extending its nonnegative integrals to infinity. Monotone
convergence proves finiteness and the bound for their limit. Removing
the nonnegative half endpoint term gives precisely the strict tail
in (13), whether or not a zero lies at H. No endpoint exclusion or
simple-zero premise has entered.

L018's conjugation of rho reverses gamma and preserves multiplicity;
it doubles the scalar positive-height tail. Separately, the induced
symmetry z -> conjugate(z) preserves |Re z|>H and conjugates
F(z)F#(z), since that product has Schwarz symmetry for every complex f.
Absolute convergence justifies the rearrangement proving reality.
Neither symmetry makes an individual nonreal-zero term nonnegative.

**Exact arithmetic and scope.** Replayed the eleven exact checks in
`scripts/neutral-zero-tail/check-877.py`, and inspected in full the
constants, every check, both power-tail bounds, epsilon, strict slack
and failure list in `scripts/neutral-zero-tail/certificate-877.json`.
All checks pass. The strict slack to 2*10^(-16) is exactly

    1074999999984817/28125000000000000000000000000000 > 0.

The certificate proves these scalar comparisons only; the preceding
analytic checks establish their applicability. All direct mathematical
inputs remain L018, L750, C750a, C750c and L753, as in the DAG.
No constant, dependency or claim in (1)--(14) required correction.
The required finite Gram margin and finite-input errors are still
unknown. Auditing the tail does not audit C750c's unfinished energy
computation or extend this fixed ten-coordinate bound to the infinite
complement, non-neutral tests, global mixed positivity or RH.

## Mathlib

Full matching coverage for this exact ten-coordinate projected U12
tail inequality has not been checked. Cauchy--Schwarz, finite sine
orthogonality, L2 orthogonal projection and monotone convergence are
standard supporting facts. No matching Mathlib theorem, formal proof
or absence claim is asserted. The explicit formula and BPT scalar
tail are mathematical inputs by the precise citations above and in
L753, not claims of a checked Mathlib implementation.
