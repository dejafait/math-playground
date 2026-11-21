# Lemma 766: the actual symmetrized real-moment integrand changes sign

## Hypotheses

Use the actual theta kernel K of L019 and moments M_(2n) of L021,
with the completion convention of L018. Put

    a_n = M_(2n)/(8*4^n*(2n)!),  c_n = 1/(2n)!,  n>=0.

For an integer r>=2 put k=r-1 and

    D_(r,k) = det[a_(k+j-i)]_(i,j=0)^(r-1),
    B_ij = c_(k+j-i),
    H_r(u) = det[c_(k+j-i) u_i^(2(k+j-i))]_(i,j=0)^(r-1),
    Phi_r(u) = (1/r!) sum_(sigma in S_r) H_r(u_(sigma(0)),...,u_(sigma(r-1))),
    C_r = 8^(-r) 4^(-r(r-1)),
    W_r(u) = C_r (product_(i=0)^(r-1) K(u_i)) Phi_r(u).

All variables u_i are nonnegative. No negative-index coefficient is
used, since 0<=k+j-i<=2r-2. These definitions fix the precise
row-integral representation being tested; other representations are
not covered by the obstruction.

## Conclusion

The integrals below are absolutely convergent and factorial-exact:

    D_(r,r-1) = integral_([0,infinity)^r) W_r(u) du
              = r! integral_(0<u_0<...<u_(r-1)) W_r(u) du.

Let

    A_r = det[c_(r-2+j-i)]_(i,j=0)^(r-2),
    alpha_r = A_r/(r*(4r-4)!).

Then A_r>0 and alpha_r>0. For every even r>=2 the polynomial
P_r(t)=Phi_r(1,...,1,t) has degree 4r-4 and leading coefficient
-alpha_r. More quantitatively, for t>=1,

    P_r(t) <= -alpha_r t^(4r-4) + r! t^(4r-6).

Thus any t>=1 satisfying t^2>r!/alpha_r makes the actual W_r
strictly negative at (1,...,1,t). In particular,
t_r=1+sqrt(2r!/alpha_r) is one such choice. Negativity persists on
a nonempty open subset of the strictly ordered positive chamber.

This refutes pointwise nonnegativity of this specific symmetrized
integrand, even with the actual K retained. It gives no negative
value of D_(r,r-1), and neither refutes coefficient total positivity
nor RH. All integrated compensation questions remain open.

## Proof

The actual coefficient interface follows from L018/L021:
xi(1/2+w)=sum_n M_(2n) w^(2n)/(2n)!, so the entire function
G(z)=xi(1/2+sqrt(z)/2)/8 has coefficients a_n as stated.
Evenness removes any square-root ambiguity. No zero-location
assertion is used in this identification.

**Factorials and integrability.** In each permutation term of the
coefficient determinant, the sum of the indices k+j-i is rk.
Consequently the factors 8^(-1)4^(-(k+j-i)) contribute the common
constant C_r, leaving the determinant of c_(k+j-i) M_(2(k+j-i)).
Expand this finite determinant. For each term, Fubini applies
absolutely: its absolute integral is a product of r finite moments
from L021, times finite positive factorial constants. Row-by-row
integration therefore gives

    D_(r,r-1) = C_r integral H_r(u) product_i K(u_i) du.

Each variable permutation preserves the domain, Lebesgue measure and
the symmetric product of actual K factors. Averaging the finite sum
gives the first asserted formula with precisely 1/r! in Phi_r;
there is no further factorial in the full-domain integral. The
symmetrized integrand remains absolutely integrable. Its symmetry,
the r! disjoint ordering chambers and the measure-zero diagonals
give the ordered-domain formula, with precisely the factor r!.

**One-outlier polynomial.** When r-1 coordinates equal 1 and one
equals t, each possible outlier row occurs (r-1)! times in the
permutation average. Expanding along that row gives exactly

    P_r(t) = (1/r) sum_(ell=0)^(r-1) sum_(j=0)^(r-1)
             (-1)^(ell+j) c_(k+j-ell)
             det B^(ell,j) t^(2(k+j-ell)),

where B^(ell,j) deletes row ell and column j in their original
orders. The largest index k+j-ell=2r-2 occurs uniquely at
ell=0,j=r-1. Its cofactor is A_r; every other term has degree at
most 4r-6. The leading coefficient is therefore

    (-1)^(r-1) A_r/(r*(4r-4)!).

**Strictness of the factorial minor (imported, not reproved).**
Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1, Definition 2, p.4, and the paragraph on
cosh(sqrt(z)), p.10](https://arxiv.org/pdf/math/0505174v1#page=10),
states that the coefficient sequence c_n of cosh(sqrt(z)) belongs
to SPF_infinity. Definition 2 specifies strict positivity of the
Toeplitz minors without vanishing rows or columns. The p.10
paragraph obtains this statement as a submatrix of the exponential
coefficient matrix. Use only that stated strictness conclusion;
no positivity property of the actual a_n is imported.

For m=r-1, our A_r selects rows 0,...,m-1 and columns
m-1,...,2m-2 from the upper Toeplitz matrix (c_(q-p)), with c_n=0
for n<0. Its entries have indices 0,...,2m-2 and are all strictly
positive, so it has no vanishing row or column. The cited strictness
applies and yields A_r>0, including m=1 where A_r=c_0=1.
This checks the exact selected minor and its boundary index; it
does not assume actual-Xi PF or LP membership.

**Effective sign bound.** Every B entry is in (0,1]. Expansion of
an (r-1)-square cofactor bounds its absolute value by (r-1)!.
In the displayed double sum each coefficient before collection has
absolute value at most (r-1)!/r. After deleting the unique leading
term, the sum of the absolute values of all remaining terms is at
most r^2 (r-1)!/r = r!. For t>=1 their powers are at most 4r-6.
For even r the resulting upper bound is the one in the conclusion.
It is strictly negative if alpha_r t^2>r!. The explicit t_r has
alpha_r t_r^2>2r! and t_r>1. Since C_r>0 and the actual K is
strictly positive by L019, W_r(1,...,1,t_r)<0. No tail or K factor
has been discarded in this sign assertion.

As a normalization check, r=2 gives

    P_2(t) = t^2/4 - (t^4+1)/48,
    P_2(4) = -65/48.

This is a value of the integrand polynomial, not a computed minor.
The conclusion for every even order follows from the leading-term
argument above, not from extrapolating this low-order check.

**Open strictly ordered witness.** The polynomial Phi_r is continuous.
The actual K is continuous and positive on [0,infinity): continuity
also follows directly from L019's series, uniformly convergent on
each compact interval by its n^4 exp(-pi n^2) majorant times a
compact-dependent constant. Thus W_r is continuous. Strict
negativity at v=(1,...,1,t_r) supplies an open ball on which W_r<0,
chosen small enough to stay in the positive orthant. For r>2 choose
epsilon>0 sufficiently small that

    w=(1,1+epsilon,...,1+(r-2)epsilon,t_r)

lies in that ball and has strictly increasing coordinates. For
r=2 the point (1,t_r) already does. A sufficiently small open ball
around w stays in the original negative ball and in the strictly
ordered chamber, because every coordinate and every consecutive
gap at w is positive. It is a nonempty open set and hence has
positive Lebesgue measure. This removes the coincident-variable
boundary issue. Signed contributions elsewhere may compensate it,
so the integral's sign has not been determined.

## Mathlib

Full matching coverage for this factorial-weighted real-integrand
obstruction and for Katkova's selected strict factorial minor is
not checked; availability is unknown. The proof uses finite
determinant expansion, absolute Fubini, finite permutation averaging
and continuity. No Mathlib theorem is asserted to establish the
full result. Reference: https://leanprover-community.github.io/mathlib4_docs/.
