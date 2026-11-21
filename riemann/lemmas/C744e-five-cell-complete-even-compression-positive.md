# C744e: Positive complete five-cell even 64-mode compression

## Hypotheses

Fix ell=log(3)/2, a=5ell/2, penalty 256, C744b's ten physical
moments and its even orthonormal basis e_q^+, 0<=q<=63. Let V be
this complex span. The target form is the semibounded smooth form
closure of L744 (6), with the full response family, all nine active
prime powers 2,3,4,5,7,8,9,11,13 and the signed pole. No generator
domain, exact neutrality, complement sign or RH is assumed.

Analytic imports are Hongmin Li, *Cutoff-free positivity of localized
Weil forms through the (log 11)/2 threshold*, [paper45 displayed v2,
9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma 3.1 and (2.1)-(2.5), at arbitrary a; and
[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3#S3),
Section 3.2, (3.2)-(3.4), for the smooth cutoff method. C744c's
accepted step461 audit verifies the local Fourier normalization and
bounded complex response map. Numerical source signs/artifacts are
not inputs. C744b's finite integration formulas and C744d's stored
arithmetic/moment/pole assembly are used; C744d's coarse-box result
remains unaudited and is not promoted to a physical sign.

The digamma difference is [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6);
the rational value psi(1/4)=-gamma-pi/2-3log(2) is
[DLMF 5.4.19](https://dlmf.nist.gov/5.4.E19), p=1,q=4. The arithmetic
contract is the [Python Decimal documentation](https://docs.python.org/3/library/decimal.html):
directed basic operations, correctly rounded exp/ln/sqrt widened by
adjacent numbers, and C744b's audited Machin/Taylor trigonometry.
The finite binomial expansion and convergent logarithmic series below
implement the already assessed elementary-series method. Tightening
Euler's constant is necessary because the old uncertainty dominates
the finite sign scale; no special-function software is imported.

This is REPRODUCTION under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-complete-compression-461.md`.
No originality or progress beyond the inspected methods is claimed.

## Conclusion

For every v in V, and its centered full-interval even representative
f(x)=v(|x|)/sqrt(2), u(y)=f(y-a), the complete penalized form satisfies

\[
 \overline E_{2a}(u)+256\|Cu\|^2
 >10^{-43}\|v\|^2\quad(v\ne0).                         \tag{1}
\]

The separate conceptual audit below (11 November 2026, step466)
accepts this finite-compression result under the stated source and
arithmetic contracts.
It supplies neither a positive complement nor an exact-neutral,
odd-sector, all-window or actual-Xi sign. In particular it does not
resolve L030-L032/C032a or RH. C744b's truncated negative comparison
and C744d's artificial-box obstruction are preserved.

## Proof

### Form applicability and the exact complete matrix

For each fixed finite cosine sum, the even full-interval function and
its derivative are bounded. With the even smooth interior cutoffs of
C744c, the removed collar has L1 norm O_v(epsilon) and zero-extended
variation O_v(1), including the endpoint jumps. Its Fourier transform
is O_v(min(epsilon,1/|xi|)), hence its squared logarithmic Fourier norm
is O_v(epsilon log(1/epsilon)). The half-interval cosine coefficients
of the removed collar have the same min(epsilon,1/q) bound, by L1
estimation and integration by parts; the constant coefficient is
O_v(epsilon). Thus the shifted diagonal form norm also converges.
These arguments apply separately to real and imaginary parts.
C744c's bounded complex response map, finite delay forms, pole and
moment forms are L2-continuous. Both sides of the imported smooth
identity therefore converge for every v in V. This proves membership
in the smooth form closure and its identity here; neither equality of
whole periodic/zero-extension domains nor zero-extension H1 membership
is asserted. Polarization gives the finite Hermitian matrix.

Put k_q=q*pi/a, u_q=k_q^2, n_0=a^(-1/2), n_q=(2/a)^(1/2) for q>0,
and c_j=2j+1/2. The exact real symmetric matrix is

\[
 M_{rs}=\delta_{rs}h(k_r)+P_{rs}+p_rp_s
       +256\sum_{j=0}^4\sum_{\sigma=\pm1}m_{j\sigma,r}m_{j\sigma,s}
       +n_rn_s(-1)^{r+s}F(u_r,u_s),                    \tag{2}
\]
\[
 F(u,v)=\sum_{j\ge0}
 \frac{c_j^2(1-e^{-2ac_j})}{(c_j^2+u)(c_j^2+v)}.        \tag{3}
\]

Here h(k)=Re psi(1/4+ik/2)-log(pi). The pole row is C744b (8)'s
response row at j=0 times e^(a/2)sqrt(1-e^(-a)). The physical moment
rows are n_q/sqrt(2) times C744b (10)'s endpoint difference on each
cell, including beta=sigma/2 and the constant mode. For d=log(n),
b=a-d/2, S_d(t)=sin(tb)/t with S_d(0)=b, the prime contribution is
-2log(p)/sqrt(n) times n_rn_s/2 times

\[
 S_d(k_r-k_s)\cos((k_r+k_s)d/2)
 +S_d(k_r+k_s)\cos((k_r-k_s)d/2).
\]

This is the bilinear version of C744b (9), including r=s=0, and uses
log of the base prime at higher powers. All nine matrices, ten moment
rows and pole rows are reused from `compression-463.json` and their
component sums rechecked in the original upper-triangle arithmetic
order. This reuses numerical integration data, not its old uncertain
diagonal or its incomplete Gram matrix. The matrix is then reflected
symmetrically. For complex coefficients x+iy its value is
x^TMx+y^TMy, so a real symmetric positive certificate suffices.

### Infinite inverse-power sums with explicit elementary bounds

The implementation needs S_p=sum_(j>=512)c_j^(-p), 2<=p<=66,
and G_p=sum_(n>=512)n^(-p), 2<=p<=33. These are not approximated by
an unbounded asymptotic series. Partition [512,2^180) into integer
dyadic blocks [J,2J). Write w_j=2j-3J+1. For c_j, use center
C=3J-1/2 and relative displacement w_j/C. For integer j, use
C=(3J-1)/2 and relative displacement w_j/(3J-1). In either case
|displacement|<=rho<1/3 and the points are symmetric.

Let A_l=sum_(J<=j<2J)w_j^l. Odd moments vanish, A_0=J, and for even
l>=2 telescoping (w+1)^(l+1)-(w-1)^(l+1) gives exactly

\[
 A_l=\frac{J^{l+1}-
   \sum_{i=3,\ i\ \text{odd}}^{l+1}{l+1\choose i}A_{l+1-i}}
                {l+1}.                              \tag{4}
\]

Every numerator and division is evaluated as an exact integer; zero
remainders and nonnegative resulting even moments are checked. If D
is the relative-displacement denominator (C or 3J-1 respectively),
the binomial polynomial through degree T=144 sums to

\[
 C^{-p}\sum_{0\le l\le T,\ l\ \text{even}}
       {p+l-1\choose l}A_l/D^l.                       \tag{5}
\]

The absolute remainder is at most

\[
 JC^{-p}{p+T\choose T+1}\frac{\rho^{T+1}}{1-q},
 \qquad q=\rho\frac{p+T+1}{T+2}<1.                   \tag{6}
\]

Indeed the binomial series for (1+z)^(-p) converges for |z|<1;
the ratio of successive absolute terms after degree T is bounded
by q, since (p+l)/(l+1) decreases for p>=1. Summing that geometric
bound for each of the J points proves (6). The program adds a
symmetric interval of this radius to (5); the positive even-only
tail could give a tighter one-sided bound, but is not needed.

After the 171 blocks, the remaining positive infinite sum is enclosed
between zero and

\[
 x^{-p}+\frac{x^{1-p}}{d(p-1)},                        \tag{7}
\]

by decreasing-function integral comparison, with x=2*2^180+1/2,
d=2 for S_p, and x=2^180,d=1 for G_p. Thus every physical tail is
retained. Blocks, every power-sum enclosure, polynomial error and
final tail are saved, not merely their aggregate values.

### Sharpened diagonal and complete response evaluation

Telescoping the logarithms gives

\[
 \gamma=H_{511}-\log512+
     \sum_{n\ge512}(1/n-\log(1+1/n)).                  \tag{8}
\]

This follows directly from gamma=lim(H_m-log m), because the finite
sum of logarithms is log(m+1)-log512. The alternating logarithmic
expansion through p=32 gives the last sum as
sum_(p=2)^32 (-1)^p G_p/p, with error at most G_33/33. Absolute
convergence of these power sums justifies the finite expansion and
summed remainder. This error is <1.965e-90. It is added symmetrically;
(8) replaces the older harmonic/remainder enclosure of gamma only.
Then h(0)=-gamma-pi/2-3log2-log(pi), and the imported digamma difference
is the convergent identity

\[
 h(k)-h(0)=\sum_{j\ge0}\frac{2k^2}{c_j(c_j^2+k^2)}.    \tag{9}
\]

For j<512 evaluate its rational summands directly. For the rest,
expand 1/(1+k^2/c_j^2) through m=31, giving
2 sum_(m=0)^31 (-1)^m k^(2m+2) S_(2m+3), with error at most
2k^2 (k^2/c_512^2)^32 S_3. The geometric identity's denominator
1+k^2/c_j^2>=1 proves this bound. It includes k=0, whose difference
and error are zero. No complex asymptotic remainder is being assumed.

For (3), evaluate the first 512 terms directly, including their
exponential factors. In its remaining rational part, expand both
denominators and collect terms of total degree m<32. The result is

\[
 \sum_{m=0}^{31}(-1)^m
       \left(\sum_{t=0}^m u^t v^{m-t}\right)S_{2m+2}. \tag{10}
\]

Let R=k_63^2/c_512^2<0.02. All u/c_j^2,v/c_j^2 lie in [0,R].
The omitted absolute series is bounded by
S_2 sum_(m>=32)(m+1)R^m <=33 S_2 R^32/(1-R)^2.
The omitted exponential correction is at most exp(-2ac_512)S_2,
since c_j^2/((c_j^2+u)(c_j^2+v))<=c_j^(-2).
Both errors are added symmetrically before multiplying by
n_rn_s(-1)^(r+s). The first error is <5.142e-57. Equation (10)
works directly for u=v, u=0 and u=v=0: it does not divide by a
frequency difference, differentiate an uncertain value, or take
an unproved repeated-frequency limit. It evaluates the same full
response sum as the source divided differences by a convergent
rational-series implementation, preserving every response index.

All operations use the audited 70-digit directed interval library.
Exact integer construction in (4) precedes Decimal division. Basic
operations round outward, elementary monotone evaluations widen their
correctly rounded endpoints, and each analytic remainder is added
outward. Hence (2) is enclosed entry by entry. The maximum final
entry width is <5.850e-55. This is an actual uncertainty bound, not
a floating eigenvalue estimate. All 64 refined h intervals lie inside
the accepted old diagonal intervals, and the reconstructed C744c scalar
intersects its independently accepted positive interval; these are
consistency checks only, not the sign proof.

### Complete sign certificate and exact verification

Commands relative to this notebook, in order:

```sh
python3 scripts/five-cell-penalty/refined-464.py
python3 scripts/five-cell-penalty/sign-464.py
python3 scripts/five-cell-penalty/check-refined-464.py
```

`refined-464.json` saves all matrix entries, inverse-power data,
errors and an exact finite-decimal lower triangular matrix B. A
100-digit Decimal Cholesky/inverse of the interval midpoint merely
proposes B. The proposal's rounding and accuracy are never trusted.
The verifier treats its 65-significant-digit finite decimals as exact
rationals. Its diagonal entries are strictly positive, so B is invertible.
The directed multiplication bounds every entry of

\[
 R_B=BMB^T-I.
\]

Every complete residual entry is saved. Symmetry and the maximum
absolute row-sum bound give

\[
 \|R_B\|_2\le\|R_B\|_\infty
 \le1.77359000244861046063589037733715671965845050490701978088302
       \cdot10^{-14}<1.774\cdot10^{-14}<1.             \tag{11}
\]

The inequality between these norms uses real symmetry. Thus
BMB^T is positive definite, and congruence proves M>0. More precisely,
M >= (1-epsilon)/||B||_F^2 times I, where epsilon is the saved exact
row-sum bound. Exact rational arithmetic verifies this lower bound
is strictly greater than 10^(-43), proving (1).

The independent checker scales all finite-decimal M endpoints and
B entries to common integer denominators. It computes both full
matrix products using exact signed integer interval arithmetic,
checks containment in every saved residual interval, and checks all
64 complete row sums, every nonzero triangular diagonal and the
strict thresholds. It also checks every exact component assembly,
all block-to-power-sum aggregations, diagonal/scalar consistency and
input/current-source hashes. All 6538 checks pass with no failures.
Full rational bounds and every check are in `refined-checks-464.json`;
no preview or status label proves these inequalities. At step464 this
checked the numerical certificate only; the analytic enclosures were
reserved for the separate conceptual audit now recorded below.

Implementation failures are preserved in
`drafts/2026-11-11-five-cell-refined-compression-working-464.md`:
an equality test initially reversed mirrored interval operation order;
the optional mpmath proposal dependency was absent. The former was
corrected to the original upper-triangle order; the latter replaced
by an untrusted standard-library Decimal proposal. Neither failed run
supplied a sign or altered any form parameter. No blocked source
artifact was retried. The old scripts and certificates are unchanged.

### Separate conceptual audit — 11 November 2026, step466

This REPRODUCTION audit uses the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-refined-compression-audit-464.md`.
It accepts (1), not a new theorem beyond the inspected source methods.
These checks pay the earlier conceptual-review qualification; the
original calculation and its implementation failures remain above.

**Form and physical entries.** C744c's accepted audit establishes
semiboundedness of the supported logarithmic Fourier form and the
complex L2 boundedness of the entire response map. For each v in V,
the finite even cosine sum and its derivative are bounded, also at
zero. The interior cutoff error has L1 norm O_v(epsilon) and uniformly
bounded zero-extension variation, including both endpoint jumps.
Its Fourier transform is bounded by C_v min(epsilon,1/|xi|).
Splitting the logarithmic Fourier integral at 1/epsilon gives
O_v(epsilon log(1/epsilon)) for the squared norm. On the half interval,
integration by parts of the cosine coefficients has zero sine boundary
terms and bounded derivative L1 norm. The coefficient bound
C_v min(epsilon,1/q), with O_v(epsilon) constant coefficient, gives
the same convergent bound for the shifted diagonal form norm.
The bounded full response map, finite delays, pole and moments pass
to the limit in L2. Apply this separately to real and imaginary parts
and use polarization. Thus every vector, not only C744c's fixed witness,
lies in the smooth closure and has exactly matrix (2). Neither a
whole-domain equality nor zero-extension H1 membership is needed.

For the prime entries, shift the overlap to (-b,b). Integrating
cos(k_r(t+d/2)) cos(k_s(t-d/2)) and using product-to-sum gives the
displayed two S_d terms; odd sine integrals vanish. The full-interval
coefficients n_r/sqrt(2), n_s/sqrt(2) give n_r n_s/2. For r=s=0 the
bracket is 2b, the normalized overlap is b/a, and the arithmetic
multiplier is -2log(p)/sqrt(n). Here e^(2a)=9sqrt(3) lies in (15,16);
the nine listed prime powers and their base-prime logarithms are
precisely the active ones. For the moment endpoints,
x=(2j-5)ell/2 and (2j-3)ell/2 give k_q x=q(2j-5)pi/5 and
q(2j-3)pi/5. The exponential factors are exp(-sigma ell/4) and
exp(sigma ell/4). Differentiating C744b (10)'s antiderivative verifies
its numerator and positive denominator, including q=0. All ten rows
use n_q/sqrt(2). Finally p_+=exp(a/2)sqrt(1-exp(-a)) r_0^+ verifies
the pole row and its positive even-parity sign. The full response
projections give (3) by multiplication, with n_r n_s and (-1)^(r+s).
These checks accept the inherited physical cross entries, without
accepting C744d's separate artificial-box conclusion.

**Every inverse-power index and remainder.** In [J,2J), w_j runs
from -(J-1) to J-1 in steps of two and is symmetric. Adjacent endpoints
telescope: sum[(w+1)^(l+1)-(w-1)^(l+1)]=2J^(l+1) for even l.
Dividing its odd-binomial expansion by two proves (4), with A_0=J.
For the response sum C+w_j=2j+1/2; for the integer sum,
C(1+w_j/(3J-1))=j. Thus both centers and denominators are correct,
and rho<1/3. The first omitted absolute term is
binom(p+144,145)rho^145; subsequent ratios are bounded by
rho(p+145)/146<1 for all stored p<=66. This proves (6), including
its factor J and denominator. Odd terms cancel exactly; bounding
all omitted absolute terms remains valid. The 171 blocks have
J=2^9,...,2^179 and end at 2^180. The decreasing-function integral
comparison starts at that same index, with spacing two or one,
proving (7). No infinite index set or first tail summand is omitted.

Independently, the audit directly sums all even powers of the 512
initial displacements and doubles their distribution via
W_(2J)=(W_J-J) union (W_J+J). Thus
A_l(2J)=2 sum_(t even,0<=t<=l) binom(l,t) J^(l-t) A_t(J).
These nonnegative exact integer moments satisfy (4) at every block
and every even degree through 144. All are saved in
`replay-466/centered-moments.json` under the script directory below.
Exact Fraction checks verify every saved block-error enclosure,
every ratio, the power ranges and each final-tail enclosure.
The complete replay checks all directed polynomial sums and their
aggregations, not just a representative first block.

**Gamma, diagonal and Gram.** Summing (8) through n=m gives exactly
H_m-log(m+1), whose limit is gamma. The alternating logarithm error
after p=32 is at most n^(-33)/33; its convergent sum bounds the total
remainder. DLMF 5.4.19 at p=1,q=4 gives h(0), with all logarithm
factors as stated. DLMF 5.7.6 at z=1/4+ik/2 has no pole:
subtracting its k=0 value and taking real parts gives exactly
2k^2/[c_j(c_j^2+k^2)]. The finite geometric identity after m=31
bounds the j>=512 error by 2u(u/c_512^2)^32 S_3. It is zero for
u=0 and uses through S_65, inside the saved range.

For the Gram tail the geometric arguments lie in [0,R], R<0.02.
Absolute convergence permits the product and total-degree grouping.
The omitted sum is at most S_2 R^32(33-32R)/(1-R)^2, bounded by
(10)'s error. Removing the exponential factor subtracts a nonnegative
quantity at most exp(-2ac_512)S_2. Adding both errors symmetrically
before the signed normalization therefore encloses the true tail
for either parity of r+s. Direct prefix terms keep the exponential.
Constant, repeated and zero frequencies require no limit or divided
difference: the h(0) difference vanishes and the u=v=0 response tail
is S_2 with its bounded exponential subtraction.

**Arithmetic and sign.** All three step464 programs and the inherited
assembly through its moment rows were inspected. The original
70-digit interval library and scalar inputs have the hashes accepted
in step457. Basic operations round outward, integer moments are exact,
and exp/ln/sqrt are widened under the recorded contracts. The new
expressions have positive denominators. Magnitudes stay far within
the Decimal exponent range: even the largest integer moment used
has fewer than 8000 decimal digits. No underflow, overflow, floating
special-function value or binary Cholesky error constant is used.
The midpoint factorization only proposes exact finite decimals for B;
its numerical accuracy is not a premise.

Reproduction command:

```sh
python3 scripts/five-cell-penalty/audit-refined-466.py
```

All inherited prime matrices, ten moment rows and their matrices,
and every pole entry replay exactly. Every refined enclosure field
replays exactly with only the output destination changed, including
the complete matrix, all blocks, inverse sums, errors and diagonals.
All 46,135 new checks pass without failures; all 11 old artifacts
are preserved. The original 6538-check exact report reproduces byte
for byte. Full evidence is in `scripts/five-cell-penalty/replay-466/`:
`audit.json`, `centered-moments.json`, `refined-464.json` and
`refined-checks-464.json`. This is a complete certificate replay
and formula audit, not an independent implementation of elementary
transcendental functions; the arithmetic contracts remain inputs.

For the exact real symmetric physical M in the verified enclosure,
the integer verifier encloses both full products BM and BMB^T-I,
respecting every multiplier's sign. The saved upper triangle can
be reflected because the physical residual is symmetric, regardless
of interval dependency overestimation. Every row is checked.
The directed upper bound is exactly (11)'s decimal, strictly below
1.774e-14 and one. For a symmetric residual the spectral norm is
at most its maximum absolute row sum. The triangular B has positive
exact diagonal, so congruence yields
M >= (1-epsilon)B^(-1)B^(-T)
>= (1-epsilon)/||B||_F^2 I. Exact rational comparison gives >1e-43;
the complete numerator and denominator are in both audit reports.
The physical entry width <5.850e-55, gamma remainder <1.965e-90
and Gram remainder <5.142e-57 also pass strict exact comparisons.
Real symmetry splits complex coefficients x+iy into x^TMx+y^TMy,
completing (1) on V.

No error requiring a mathematical repair was found. This acceptance
concerns only the complete finite compression. C744b's truncated
stop, C744d's recorded coarse-box evidence and both source-artifact
blockers remain. Infinite complements, exact-neutral transfer,
odd-sector signs and all-window propagation remain unproved here.

## Mathlib

Full matching Mathlib coverage of this complete finite compression,
smooth-closure specialization and interval certificate has not been
checked. No absence claim or formal verification is made. The source
identity, binomial/logarithmic expansions and matrix congruence method
are known mathematics; this is a local specialization and implementation.
