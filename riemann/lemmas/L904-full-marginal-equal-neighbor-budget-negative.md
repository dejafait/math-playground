# Lemma 904: the first full-marginal equal-neighbor budget is negative

## Hypotheses

Use L898's complete actual-theta law at y=0: Phi(u)=K(|u|)/2,
p=u+v, q=u-v, W_0=p^2 Phi(u)Phi(v), and A_0=A_0(0)>0. Its
probability marginal is mu(B)=A_0^(-1) integral 1_{q in B} W_0 du dv.
All theta indices and both real spatial directions are included.

Set a=pi/16 and b=a/2. Define

\[
 I_0=[-b,b],\quad I_1=[b,3b],\quad I_2=[3b,5b],\qquad
 J=\tfrac12\int_{I_0}\cos(16q)\,d\mu(q)
      +\int_{I_1}\cos(16q)\,d\mu(q)
      +\tfrac12\int_{I_2}\cos(16q)\,d\mu(q).
\]

The computer-assisted bounds below assume precisely L037's arithmetic
contracts: outward-rounded Decimal basic operations, correctly rounded
Decimal exp widened to adjacent representable neighbors, exact integer
and rational inputs, and rejection of exceptional arithmetic. The
documented Decimal implementation, Python interpreter and execution of
the cited script are trusted; neither is independently formally verified.
The certificate uses precision 70 and the rational Machin pi enclosure
of L037. No RH, zero simplicity or total first-sign inequality is assumed.

## Conclusion

Under those contracts, the following strict rational bounds hold:

\[
                 -\frac{32}{1000}<J<-\frac{2}{1000}
                                      <-\frac1{1000}<0.
\]

Thus the assertion that every negative cosine lobe can be paid by half
of each adjacent complete positive lobe fails already at x=16,y=0.
This is a local sufficient-allocation obstruction. It neither signs the
complete transform negatively nor resolves the all-degree mixed-sign gap.
The exact finite budget was not supplied by the inspected literature;
the scoped EXPLORE assessment supports this discriminator, not a novelty
claim about general Fourier-transform theory. The independent audit of
9 November 2026 (step175), below, validates this fixed result under the
same arithmetic contracts; it supplies no new sign theorem.

## Proof

### Full marginal, normalization and conservation

Use t=(u+v)/2 and q=u-v. Then u=t+q/2 and v=t-q/2, and the absolute
Jacobian of (t,q) to (u,v) is 1 (equivalently, the (p,q) Jacobian is 1/2
and dp=2dt). Since p=2t, the factors 4 in p^2 and 1/4 in Phi(u)Phi(v)
cancel. Hence the unnormalized q density is

\[
 \rho(q)=\int_{\mathbb R}t^2K(|t+q/2|)K(|t-q/2|)\,dt
        =2\int_0^\infty t^2K(t+q/2)K(|t-q/2|)\,dt\quad(q\geq0).
 \tag{1}
\]

The second equality uses evenness of the product in t. The density is
even in q, nonnegative and integrable. L898 supplies absolute Fubini
and polynomial domination, so these changes of variables and the cosine
integrals are legitimate; no distributional or conditional marginal is
substituted. Put

\[
 B_0=\int_0^b\rho(q)\cos(16q)\,dq,\quad
 B_1=\int_b^{3b}\rho(q)\cos(16q)\,dq,\quad
 B_2=\int_{3b}^{5b}\rho(q)\cos(16q)\,dq.
\]

Evenness gives exactly N:=A_0 J=B_0+B_1+B_2/2. In particular, the
factor 1/2 on the complete central lobe is already incorporated by
retaining its positive-q half with weight 1. Discarding it or again
halving B_0 would change the proposed allocation.

For normalization write M_r=integral_0^infty u^r K(u)du for r=0,2.
Then integral_R Phi=M_0, integral_R u^2 Phi=M_2, and integral_R u Phi=0.
Expanding (u+v)^2 and using absolute Fubini therefore gives

\[
                            A_0=2M_0M_2>0.                 \tag{2}
\]

For the resource interpretation, every full positive cosine lobe has
center 2ka and every full negative lobe has center (2k+1)a, k integer.
Split each positive lobe's integrated resource into two equal halves
for its two adjacent negative lobes. Each positive resource is used
exactly twice with coefficient 1/2 and each negative lobe once with
coefficient 1. Endpoints have zero cosine. This proves conservation
without assuming any budget sign. The central positive lobe gives one
half to each of the negative lobes centered at a and -a; reflection
makes these two budget values equal, rather than supplying extra mass.
If summed over all lobes, absolute convergence follows from
integral rho |cos(16q)| <= A_0; thus no divergent resource rearrangement
is involved. Only the budget centered at a is tested here.

### Complete theta and transverse spatial errors

Let K_4 be the first four theta terms. L312 proves, for every u>=0,

\[
 0<K_4(u)\leq K(u)<16,\qquad
 0\leq K(u)-K_4(u)\leq\epsilon:=160000e^{-75},\qquad
 K(u)\leq256e^{9u/2-3e^{2u}}.                            \tag{3}
\]

These are actual full-series bounds, not a use of L312's older finite
conditional-order certificate on a new domain. Set T=pi/2, so 3/2<T<2.
For 0<=t<=T and 0<=q<=5b, product subtraction and (3) bound the
K K minus K_4 K_4 error between 0 and 32 epsilon. Consequently the
pointwise density error from the finite-t theta omission is at most

\[
 64\epsilon\int_0^T t^2dt < E_\theta:=512\epsilon/3.      \tag{4}
\]

For t>=T and these q, t-q/2>0. Applying (3) to both factors and using
e^q+e^(-q)>=2 bounds their product by
65536 exp(9t-6e^(2t)). Enlarge the tail to t>=3/2. With t=3/2+w,
e^3>20 and e^(2w)>=1+2w give

\[
 9t-6e^{2t}\leq-106-231w\quad(w\geq0).
\]

Here e^3>20 follows from the positive exponential series through degree
eight, as in L312. Integrating 2t^2 times the product bound proves the
uniform full spatial-density tail bound

\[
 E_s=131072e^{-106}
       \left(\frac{9}{4\cdot231}+\frac3{231^2}+\frac2{231^3}\right).
 \tag{5}
\]

Using |cos|<=1, the absolute errors in B_0,B_1,B_2 are at most
b(E_theta+E_s), 2b(E_theta+E_s), 2b(E_theta+E_s), respectively.
Thus N's total omitted-mass error is at most 4b(E_theta+E_s), with
the outer half share retained. No omitted theta index or transverse
spatial interval is assumed to vanish.

For (2), the positive theta omissions from [0,T] in M_0,M_2 are at
most 2 epsilon and (8/3) epsilon. For u=3/2+w, (3) gives

\[
 K(u)\leq256e^{-53-115w}.
\]

Indeed 9u/2-3e^(2u)<=-53.25-115.5w<=-53-115w. The remaining
spatial errors in M_0,M_2 are therefore bounded by

\[
 H_0=256e^{-53}/115,\qquad
 H_2=256e^{-53}
       \left(\frac9{4\cdot115}+\frac3{115^2}+\frac2{115^3}\right).
 \tag{6}
\]

### Finite real boxes, endpoints and arithmetic

Fix M=32 and h=pi/(64M). Partition t in [0,T] into 32M cells
[ih,(i+1)h], and q in [0,5b] into 5M cells [2jh,2(j+1)h].
The lobe boundaries correspond exactly to j=0,M,3M,5M; they are
not rounded endpoints. On each box, the arguments of the two K_4
factors are enclosed by

\[
 [(i+j)h,(i+j+2)h],\qquad
 \big|[(i-j-1)h,(i-j+1)h]\big|.                         \tag{7}
\]

The absolute image of an interval crossing zero starts at zero. Thus
every reflected-kernel seam is included without differentiating across
it. Direct evaluation of the finite exponential formula, with interval
operations and intersection with [0,16] from (3), encloses both factors
everywhere on the box. Each summand is positive for nonnegative u,
since pi n^2 e^(2u)>3/2, which also justifies the lower intersection.

The factors 2t^2 and cos(16q) are separable and have integrated weights

\[
 T_i=\frac{2h^3}{3}((i+1)^3-i^3),\qquad
 Q_j=\frac{\sin(\pi(j+1)/(2M))-\sin(\pi j/(2M))}{16}.
 \tag{8}
\]

Cosine has a fixed sign on every q cell: positive for j<M or j>=3M,
negative otherwise. If [l,r] encloses the nonnegative product of the
two kernel factors, the cell integral is in T_i Q_j [l,r], with
interval multiplication reversing endpoints when Q_j<0. This follows
by integrating the pointwise inequalities against a measure with a
fixed sign. It is a real-box inclusion, not a Gaussian quadrature or
an unproved midpoint error estimate. The finite M_0,M_2 integrals use
one-dimensional K_4 boxes and the exact weights h and
h^3((i+1)^3-i^3)/3, respectively.

L037's pi enclosure is propagated through (7) and (8); there is no
unaccounted irrational endpoint strip. Sine evaluation uses L312's
explicit degree-49 sine/cosine Taylor enclosures: reduce an interval x
to r=x-2k*pi with any fixed integer k, check |r|<=4, and add the
remainder [-R,R], R=|r|^50/50!, to the Taylor polynomial. Every endpoint
value is enclosed before replacing multiples of pi/2 by their exact
values 0,1,-1. Every Q_j is checked strictly signed. All cache entries,
integrated cosine weights, parameters, tails and resulting enclosures
are saved; the imported Decimal interval class rejects binary floats
and arithmetic exceptions. Its standard rational/exp/pi self-check is
also executed. These checks supplement, and do not remove, the stated
implementation trust assumptions.

Reproduce this one grid (163840 two-dimensional boxes) with

```
python3 scripts/theta-marginal/equal_neighbor_budget_135.py --mesh 32 --output scripts/theta-marginal/equal-neighbor-budget-135-m32.json
```

The full certificate is
`scripts/theta-marginal/equal-neighbor-budget-135-m32.json`.
Its complete `/result` and `/bounds` values were inspected, including
all three signed integrals and all tails, using the shared JSON
inspector's `--full` option on those selected fields. Larger strict
rational enclosures of the complete values are:

| Quantity | Lower | Upper |
| --- | --- | --- |
| B_0 | 0.0018416 | 0.0020518 |
| B_1 | -0.0032890 | -0.0029473 |
| B_2 | 0.0015029 | 0.0016850 |
| N | -0.000696 | -0.000053 |
| M_0 | 0.4906 | 0.5037 |
| M_2 | 0.02263 | 0.02332 |
| A_0 | 0.022 | 0.024 |
| J | -0.032 | -0.002 |

For error scale only, the rigorous certificate also gives
epsilon<4.286e-28, E_theta<7.315e-26, E_s<1.185e-43 and
4b(E_theta+E_s)<2.873e-26. The normalizer spatial errors are below
2.138e-23 and 4.866e-23. The full outward-rounded values, rather than
these rounded displays, are used in the division. The displayed coarse
bounds for N and A_0 already imply -0.032<J<-0.002 by exact rational
division, so neither a preview nor a tiny final digit is decisive.

The required allocation threshold was J>=0. Its strict negative upper
bound proves failure for this fixed budget. This is consistent with a
positive complete first transform: mass assigned differently or from
other lobes can compensate the local deficit. No neighboring-cell or
frequency sweep, nonzero-height transfer, complete signed compensation,
higher mixed positivity, or RH conclusion is established.

### Independent analytic and certificate audit — 9 November 2026, step175

The audit retains exactly x=16,y=0,M=32 and the original allocation.
Its source scope is the previously approved SPECIALIZE assessment
`drafts/literature/2026-11-09-l904-independent-budget-audit-review.md`;
Johansson's cited real-inclusion branch does not supply the sign or tails.
The full original proof, program, invoked arithmetic/trigonometric
implementations and complete load-bearing certificate were checked.
L905's different Hall computation is not an input to this audit.

**Analytic and resource checks.** The coordinate matrix has determinant
-1, so its absolute Jacobian is one; p^2=4t^2 cancels the factor 1/4
in the two Phi terms. The product is even in t and q. L019's decay,
as used in L898's domination argument, controls both quadratic moments
and every change of integration order here. Expanding (u+v)^2 gives
2M_0M_2, since the first full-line moment is zero. Each M_r is strictly
positive. The half of the entire central lobe is exactly B_0, with no
further factor 1/2. Globally, each positive lobe is spent twice by
halves, each negative lobe once, and the sum is absolutely bounded by
integral rho=A_0. Thus neither reflection nor rearrangement adds resource.

For (3), the L312 summand envelope has successive ratios at most
16e^(-9)<1/2. Starting at n=5 gives
2*128*5^4 e^(-75)=160000e^(-75); positivity bounds both K and K_4
by 16. Hence the difference of their two-factor products is between
zero and 32epsilon. Integrating 2t^2 to T<2 gives (4). On the entire
spatial-tail domain, t-q/2>=pi/2-5pi/64=27pi/64>0. The two positive
arguments therefore yield the product envelope in (5), with no reflected
argument omitted. The degree-eight positive series for e^3 is already
greater than 20. For t=3/2+w its exponent is at most
-106.5-231w<=-106-231w. Integrating
(3/2+w)^2 e^(-231w) over w>=0 gives exactly
9/(4*231)+3/231^2+2/231^3.
The single-kernel exponent is at most -53.25-115.5w, and enlarging it
to -53-115w gives both errors in (6). The finite moment omissions are
at most T epsilon<2epsilon and T^3 epsilon/3<8epsilon/3.
All three signed lobe errors, their outer half weight, and both complete
moment errors occur in the program. Symmetric lobe errors are safe even
though the omitted density itself is nonnegative; moment omissions are
one-sided. The numerator and denominator share inputs, but ordinary
interval division by a strictly positive enclosure remains valid without
independence.

**Pointwise boxes and arithmetic checks.** The true grid uses h=pi/2048;
interval pi encloses this one grid rather than defining perturbed domains.
Formula (7) covers every argument on a product box. Taking the full
absolute image includes all seam crossings. Positive theta terms and
K<16 justify the intersection with [0,16]. The exact phase interval
of cell j is [j*pi/64,(j+1)*pi/64]; its cosine changes sign only at
j=32,96,160, which are grid boundaries. Thus the pointwise measure has
the sign used in (8), not merely an integral of that sign. The sine
routine uses one integer period shift for each evaluation, checks the
entire reduced interval lies in [-4,4], and adds the degree-49 Taylor
remainder. Replacing endpoint sines by 0 or +/-1 uses their exact
integer multiples of pi/2, checked to lie in the original enclosures.

The imported interval class uses precision-70 directed contexts for
basic operations, exact Decimal sign changes, a nearest-rounded exp
widened at both endpoints, exact rational Machin sums, and traps for
the exceptional arithmetic named in L037. The actual code calls no
higher-order quadrature routine. Its self-check was executed in the
separate replay; such tests supplement the inspected implementation
and do not eliminate the Decimal/interpreter trust assumptions.

**Complete independent evidence.** Preserve the original step135 files.
The audit uses these separate commands:

```
python3 scripts/theta-marginal/equal_neighbor_budget_135.py --mesh 32 --output scripts/theta-marginal/equal-neighbor-budget-175-replay.json
python3 scripts/theta-marginal/l904_independent_audit_175.py
```

The replay agrees with every field of the original certificate. The
second program imports no original arithmetic or quadrature routine:
it recomputes a Machin interval with 110 rational terms and uses separate
90-digit directed endpoint operations to enclose all 2207 cached kernel
boxes and all 160 integrated cosine weights. Each resulting interval
lies inside its original precision-70 interval. It also checks the exact
set of required cache keys, all reflected images, endpoint sines, signed
weights, parameters, density errors and moment errors. Its higher
precision evaluates the existing boxes, without refining the mesh.

For an independent accumulation, let D_K,D_Q be common powers of ten
turning every saved kernel and cosine endpoint into an integer. For each
j and each endpoint side, the program sums
sum_i ((i+1)^3-i^3) k^side_(i+j,i+j+2)
k^side_|[i-j-1,i-j+1]| in exact integers. All kernel endpoints are
nonnegative. Multiplying by the two cosine endpoints, taking the minimum
and maximum of the four products, and summing the appropriate j ranges
gives an interval which is multiplied by 2h^3/(3D_K^2D_Q).
This covers all 163840 boxes. Extracting the common positive h^3 is
legitimate for the one true grid, including negative lobe totals.
The moments are reconstructed by the same exact-integer method with
weights h and h^3((i+1)^3-i^3)/3. Exact Fraction operations then add
all saved upper tail errors, form N and A_0, and divide. Every resulting
finite/complete enclosure is contained in the corresponding original
field. The ten retained rational-check assertions were checked against
the original values, rather than accepted from their saved truth flags.

All 4781 checks passed, with an empty failure list. Full per-entry
enclosures, exact rational reconstructions, checks and input hashes are
in `scripts/theta-marginal/l904-independent-audit-175.json`. The original
complete /result and /bounds were inspected in full; every cache and
weight was processed by the exhaustive audit, not sampled. The exact
reconstructed upper bound for J was also inspected in full. The retained
original endpoints are
approximately -0.03132412068 and -0.002261298746; the strict comparisons
to -32/1000 and -2/1000 are exact rational checks. In particular the
upper bound remains below the required zero threshold by more than
2/1000. No defect was found in the stated fixed-budget claim.

This validates an existing local obstruction, not a new sign beyond the
sources or a complete-transform obstruction. Other allocations, all
parameters, contact initialization/tangency, higher forms and RH remain
unresolved. The mathematical inputs and statement are unchanged. ∎

## Mathlib

Full matching coverage and supporting formalizations were not checked;
availability is unknown, not absent. The proof uses change of variables,
absolute Fubini, elementary exponential/Taylor estimates and interval
arithmetic. L037 cites the [official Decimal documentation](https://docs.python.org/3/library/decimal.html)
for the inherited arithmetic contract. The source-reviewed finite-box
inclusion method is consistent with Fredrik Johansson, *Numerical
integration in arbitrary-precision ball arithmetic*, arXiv:1802.07942v1,
Section 2 steps 2–4 and Section 2.1, pp2–4,
[primary PDF](https://arxiv.org/pdf/1802.07942v1); it does not supply
the new-domain tails or this budget's sign. The direct separable-weight
box specialization and its errors are proved above. No analytic
Gaussian-integration premise or named positive-transform theorem is
imported for the sign.
