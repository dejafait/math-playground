# Corollary 999a: uniform decay of the fully collected coefficient mass

## Hypotheses

Let n>=1 be an integer. For a nonnegative integer vector
k=(k_1,...,k_(2n)), write |k|=sum_j k_j and
wt(k)=sum_j j*k_j. For |k|>=1 define

    c(k)=(-1)^(|k|-1)(|k|-1)! / prod_j k_j!,
    w(k)=prod_j (j!)^(-k_j).

Let K_n contain exactly the vectors of weight 2n and length
1<=|k|<=n. Let H_n contain ORDERED pairs (k',k'') of vectors
of weight n each, of positive length each, and of total length
|k'|+|k''|<=n. Coordinates through 2n are retained, with zeros
where appropriate. In independent commuting formal variables
Y_1,...,Y_(2n), define

    T_n(Y)=2n sum_(k in K_n) c(k)w(k)Y^k
       +n^2 sum_((k',k'') in H_n)
                  c(k')c(k'')w(k')w(k'')Y^(k'+k''),
    b_n(ell)=[Y^ell]T_n,
    C_n=sum_ell |b_n(ell)|.

Collect contributions to each FULL exponent vector before taking
absolute values, including contributions across the two families.
Keep all factorials, ordered pairs and the total-length cutoff.
In particular H_1 is empty. These are exactly review297's definitions.
Let p(m) be the number of integer partitions of m, and put
rho=sqrt(3)/2<1. No arithmetic-function norm or RH hypothesis is used.

## Conclusion

For every n>=1,

    0 < C_n <= 2n(2n-1) p(2n) rho^n.                       (1)

Consequently

    limsup_(n->infinity) log(C_n)/n <= log(rho)<0,
    C_n -> 0,
    limsup_(n->infinity) log(max(1,C_n))/n = 0.             (2)

In particular, for every epsilon>0 there is a finite K_epsilon
such that C_n<=K_epsilon exp(epsilon*n) for all integers n>=1.
This settles the exact formal coefficient-rate test favorably, and
strengthens it to exponential decay up to a subexponential factor.
It does not establish a norm bound for the actual arithmetic factors,
the compensated prime-degree bound L984(H), or an RH candidate.

## Proof

### Imported results and why specialization is needed

The c,w,K,H coefficients are those in O. Ramaré, *On Bombieri's
asymptotic sieve*, author preprint dated 28 October 2009,
Section 2, (12)-(18), Lemma 4, printed pp8-9:
[primary preprint](https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf).
They define the finite formal observable here; no general arithmetic
identity or sieve estimate is reproved or applied.

Import Landau's inequality for every complex polynomial A,

    M(A) <= (sum_j |[t^j]A|^2)^(1/2),

and Mahler-measure multiplicativity and the linear-factor formula
M(a*t+b)=max(|a|,|b|) for a!=0. Precise statements and full proofs
are in the pinned
[Mathlib MahlerMeasure source](https://github.com/leanprover-community/mathlib4/blob/428aa8288d061ec3ae75c1b85ac178e2cb9def23/Mathlib/Analysis/Polynomial/MahlerMeasure.lean),
`Polynomial.mahlerMeasure_le_sqrt_sum_sq_norm_coeff`,
`Polynomial.mahlerMeasure_mul`, and
`Polynomial.mahlerMeasure_C_mul_X_add_C`. No integrality, monicity,
simple-root or zero-free-circle assumption is required. The historical
source is Landau, *Bulletin SMF*33 (1905),251-261, Sections IV-VI;
the exact modern formulation above is the imported statement.

Import the formal elementary-symmetric/power-sum logarithm identity
from Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed.,
1995, Chapter I, Section 2, (2.2),(2.4),(2.10)-(2.11'), pp19-24:
[primary text](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf).
It applies over characteristic zero and allows repeated variables.
For normalized finite-torus Fourier coefficient recovery use
Akhtari-Vaaler, arXiv:1810.12413v1, (1.10)-(1.12), pp2-3:
[primary paper](https://arxiv.org/pdf/1810.12413v1).
For partition growth use Hardy-Ramanujan, *Asymptotic formulae in
combinatory analysis* (1918), (1.32), Section 2.3:
[primary paper](https://ramanujan.sirinudi.org/Volumes/published/ram36.html).
Only its consequence p(m)<=A exp(B sqrt(m)), with absolute finite
A,B for all m>=1, is needed; enlarging A covers the finitely many
indices below the source's asymptotic onset.

The prior SPECIALIZE assessment is
drafts/literature/2026-11-10-collected-root-product-specialization-review-300.md;
the primary theorem statements and proof cases were inspected in
completed review299. None of these imported results directly asserts
(1) for this length-truncated, collected polynomial. The local work
is the coefficient correspondence, scalar threshold, root-pair
specialization and support accounting. This is a quantitative
specialization/reproduction, without a certified originality claim.
L998 and L999 are contrasts, not mathematical premises.

### Full-variable correspondence and the cutoff

In Q[Y_1,...,Y_(2n)][[t]] put

    E_Y(t)=1+sum_(j=1)^(2n) Y_j*t^j/j!,
    F_Y(t)=log E_Y(t),
    P_n(Y)=2n[t^(2n)]F_Y(t)+n^2([t^n]F_Y(t))^2.           (3)

All coefficients in (3) are finite polynomials: since E_Y-1 has
positive t-order, only finitely many powers contribute at any fixed
t-degree. The formal expansion log(1+S)=sum_(r>=1)(-1)^(r-1)S^r/r
and the multinomial theorem give, for every nonzero vector k,

    [Y^k]F_Y(t)=c(k)w(k)t^wt(k).                          (4)

Indeed the only contributing power is r=|k|, whose coefficient is
(-1)^(r-1)(r-1)!/prod k_j!, with the separate j! factors from E_Y.
Thus P_n has only monomials of weight 2n and length at most 2n.

For every vector ell with 1<=|ell|<=n and wt(ell)=2n,
the first term of (3) gives exactly the K_n contribution to b_n(ell).
The square gives the sum over ALL ordered splittings k'+k''=ell
with wt(k')=wt(k'')=n. Both lengths are positive, and their total
length equals |ell|<=n, so these are exactly the H_n contributions.
Multiplication retains both orders of distinct pairs; a coincident
pair occurs once at its ordered index, without a division by two.
There are no other contributing splittings. Therefore

    b_n(ell)=[Y^ell]P_n for wt(ell)=2n, |ell|<=n,           (5)

and T_n is the projection of P_n onto these full monomials.
This is coefficient equality, not a claim that monomial deletion
contracts the supremum norm. Coefficients of P_n outside this set
are not assigned to T_n. Equal full vectors retain equal length
|ell|, so this collection also retains the source's mu multiplicity;
no vectors are merged merely by weight, and no zero-degree factors,
mu*1 cancellation or independence of arithmetic functions is used.

At n=1, H_1 is empty and (3) gives P_1=Y_2; hence T_1=Y_2
and C_1=1, in accordance with (5). The cutoff is valid at this endpoint.

### Pointwise power sums with the actual degree

Fix any complex vector y=(y_1,...,y_(2n)) with |y_j|<=1.
The polynomial E_y has constant term 1 and actual degree d<=2n.
If d>=1, the fundamental theorem of algebra factors it as

    E_y(t)=prod_(i=1)^d (1-x_i*t),

where x_i are reciprocal roots, counted with multiplicity. None is
zero, since we use the actual degree; the zeros of E_y are nonzero
since E_y(0)=1. This is a pointwise choice of a finite multiset,
with no assertion of continuous root labels as y varies.

For p_m=sum_i x_i^m, the imported formal logarithm identity gives
[t^m]log E_y=-p_m/m. Specialization in (3) commutes with its finite
coefficient operations, so

    P_n(y)=p_n^2-p_(2n)=2 sum_(i<j)(x_i*x_j)^n.            (6)

The last equality cancels the diagonal terms of the finite square;
the same identity holds with repeated roots. If d=0, E_y=1 and
P_n(y)=0. If d=1, (6) gives P_n(y)=0 with an empty pair sum.
These cases require no division by a vanishing leading coefficient.

### The fixed-radius threshold

For a_j=4^j/(j!)^2, the sum of terms j=0,1,2,3 is 97/9,
a_4=4/9, and a_(j+1)/a_j=4/(j+1)^2<=4/25 for every j>=4.
Comparison with a convergent geometric series gives

    sum_(j=0)^infinity 4^j/(j!)^2
       <=97/9+(4/9)/(1-4/25)
       =2137/189 <12.                                    (7)

For d>=2 apply Landau to E_y(2t). Its coefficients have squared
absolute sum at most the left side of (7). Multiplicativity and
the linear-factor formula, including repeated and circle roots, give

    prod_(i=1)^d max(1,2|x_i|)
       =M(E_y(2t)) <=sqrt(2137/189)<sqrt(12).               (8)

For any two distinct indices i,j, all other factors on the left of
(8) are >=1. Also (2|x_i|)(2|x_j|) is at most the product of
their two max factors, irrespective of whether either |2x_i| is
below, above or equal to 1. Consequently

    |x_i*x_j| <=sqrt(2137/189)/4 <sqrt(3)/2=rho<1.         (9)

No root-boundary exclusion or continuity limit is needed. Combining
(6),(9), including the d=0,1 cases, yields the uniform estimate

    |P_n(y)| <=d(d-1)rho^n
              <=2n(2n-1)rho^n                            (10)

when d>=2, with |P_n(y)|=0 otherwise. In particular the final
bound in (10) holds on the entire (2n)-variable unit torus,
uniformly over all degree drops. The radius is exactly 2 throughout.

### Individual coefficient recovery and the support overhead

For a nonnegative integer vector ell, normalized Fourier recovery
of the finite polynomial P_n gives

    [Y^ell]P_n = integral_([0,1]^(2n))
       P_n(e^(2pi*i*theta_1),...,e^(2pi*i*theta_(2n)))
       *exp(-2pi*i*sum_j ell_j*theta_j) dtheta.

The measure has total mass 1; the final exponential has modulus 1.
Thus every such coefficient has absolute value at most the last
bound in (10). All sums are finite, so no infinite interchange or
dimension-dependent normalization loss arises. Apply this statement
to P_n before using (5), rather than estimating a truncated
supremum norm. It bounds every retained coefficient b_n(ell).

The nonnegative vectors of weight 2n correspond bijectively to
integer partitions of 2n: ell_j is the number of parts of size j.
The retained vectors impose the additional length restriction and
form a subset. Hence their number is <=p(2n); zero coefficients
may safely be included. Summing the individual bounds proves the
upper bound in (1), with every factor depending on n displayed.
For the lower bound, ell_(2n)=1 and all other coordinates zero
has coefficient 2n/(2n)!>0. It occurs in K_n; no H_n term of
positive length in each slot can have length one. Thus C_n>0.

### Asymptotic decision and limitations

The imported partition bound and (1) imply, for all n>=1,

    C_n <= 2n(2n-1) A exp(B sqrt(2n)+n log(rho)).           (11)

The logarithm of the prefactor divided by n tends to zero,
as does B sqrt(2n)/n. Since log(rho)<0, (11) proves both the
first assertion of (2) and C_n->0. Eventually max(1,C_n)=1,
so the required rate is exactly zero. The convergent sequence C_n
is bounded: taking K_epsilon=max(1,sup_(n>=1) C_n)<infinity
gives the asserted all-n bound for each epsilon>0. No effective
partition onset or finite-sample extrapolation is needed for this
existential constant.

The conclusion differs from L998 because signs were collected over
full vectors before taking absolute values; its unmerged obstruction
is preserved. L999's balanced coefficient is consistent with (1)
but is neither required for nor sufficient to prove it. This proves
only the canonical formal coefficient cost for exactly this T_n.
The arithmetic-error transfer is outside the assessed scope. Actual
factor norms, signed correlations, Laguerre reconstruction, prime
powers, endpoints, compensation, complements and regulator/infinite
zero control remain open. No zeta estimate, RH-equivalent sign input,
arithmetic saving or complete candidate argument has been established.

Independent exact finite checks use the Newton recurrence
p_m=-m*a_m-sum_(j=1)^(m-1) a_j*p_(m-j), a_j=Y_j/j!,
to construct the complete P_n and compare every retained coefficient
with direct ordered-pair summation for n=1,...,8. They also check
the scalar rational bound and the squared version of (1), without
floating-point comparisons. Reproduce with
`python3 scripts/diamond_steinig/root_pair_301.py`; the full certificate
is scripts/diamond_steinig/root_pair_301_certificate.json. All checks
pass with no coefficient differences. These finite checks are
diagnostics; (3)-(11), not the samples, prove the all-n rate.

### Independent conceptual audit — step304, 10 November 2026

Accepted (1)-(2) without a mathematical correction, under the separately
approved scope in
drafts/literature/2026-11-10-collected-root-product-audit-review-302.md.
The audit read the entire proof and review297's exact definition,
reusing the source contracts in reviews299/300 and their separate
approval in step303. This is REPRODUCTION: certification of a local
specialization of known tools, not a new arithmetic estimate or a
claim of originality. The following checks are for every integer
n>=1, not extrapolations from the finite certificate.

For (4)-(5), a fixed full vector k can occur only in the |k|-th
power of E_Y-1. The multinomial factor divided by |k| is exactly
(|k|-1)!/prod k_j!, including its stated sign; each occurrence
contributes its separate (j!)^(-1). In the square, both factors
have positive weight n, so neither can have zero length. The
ordered splittings of ell give precisely H_n when |ell|<=n.
There is no extra symmetry factor. Coefficients belonging to the
same full vector also have the same length; no length information
is lost by collection. At n=1 the Y_1^2 terms cancel before
projection, giving P_1=T_1=Y_2 and C_1=1. Thus the correspondence
holds at the endpoint as well as in general.

For (6), E_y(0)=1 excludes zero roots, and factorization at its
actual degree supplies only nonzero reciprocal roots. The constant
term fixes the scalar factor in prod(1-x_i*t) to be exactly 1.
The cited characteristic-zero formal identity applies with
multiplicities. Its two coefficient contributions are -p_(2n)
and p_n^2, with no remaining factor of n. Constant and linear
polynomials give zero separately. A separate finite multiset at
each y suffices; no continuous labeling or limiting leading
coefficient is used.

For (7)-(9), the exact rational gap is

    12-2137/189=131/189>0,
    (sqrt(2137/189)/4)^2=2137/3024<3/4=rho^2<1.

The geometric tail starts at j=4 and includes a_4; its successive
ratios are <=4/25. Landau applies to the nonzero complex polynomial
E_y(2t). Every Mahler factor is >=1, so deleting all but two of
these factors decreases their product. Each retained factor is
at least 2|x_i|, even for a root on the circle. This proves the
claimed pair bound for distinct indices even when their root
values coincide. There are d(d-1)/2 unordered pairs, and the
factor 2 in (6) gives exactly d(d-1), bounded by 2n(2n-1).
All bounds are independent of the chosen root labels and degree.

For (10)-(11), recover each coefficient of the FULL P_n on the
2n-dimensional torus with total measure 1, before invoking (5).
The character has modulus 1, so the bound loses no dimension
factor. Only then sum over retained vectors, whose partition
encoding is injective and gives at most p(2n) terms. No claim
about contraction of a projected supremum norm enters the proof.
The length-one coefficient 2n/(2n)! cannot receive a square-term
contribution and is positive; hence log(C_n) is defined. In
particular the n=1 inequality reads 1<=sqrt(3).

Finally, the imported all-index partition majorant has finite
constants A,B after enlarging A over the finite initial range.
Both log(2n(2n-1)A)/n and B*sqrt(2n)/n tend to zero. This proves
the stated negative logarithmic upper rate, decay, and eventual
max(1,C_n)=1. Boundedness of the entire sequence then supplies
the required existential K_epsilon for every positive epsilon.
No effective onset, infinite degree/cutoff interchange or
arithmetic normalization is presumed.

No mathematical conclusion of L998 or L999 is needed for these
checks; they remain contrasts. The existing empty C999a DAG row
is therefore correct. The audit did not rerun the unchanged finite
diagnostics or treat them as all-n evidence. The arithmetic gaps
listed above, including L984(H), remain wholly unpaid.

## Mathlib

The three Mahler-measure theorems named above are supporting matches
in the pinned source, with the complex-polynomial hypotheses needed
here. No Lean replay was run. Full matching coverage for (1)-(2),
the full-vector length-cutoff correspondence and its collected norm
is unchecked and unknown. The cited supporting implementation is
not a verified formalization of this entire specialization.
