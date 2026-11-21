# Corollary 999b: exact compensated finite-window majorant for the bulk

## Hypotheses

Let n>=2 be an integer, Lambda the actual von Mangoldt function,
including every prime power, and set

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    w_n(x)=K_n(log x)/x,
    B_n=sum_(exp(n)<m<=exp(2n)) Lambda(m)w_n(m)
                                     -integral_n^(2n) K_n(u)du.

All integrals below are ordinary finite integrals. In particular w_n
is real and continuous on every interval used. All integer atoms at a
right endpoint have their full weight; a left-endpoint atom is excluded.
No hypothesis on zeros or on arithmetic cancellation is made.

Put J=ceil(n/log(2)). For r=0,...,J-1 define

    X_r=exp(n)*2^r,   a_r=X_r,   b_r=min(2X_r,exp(2n)),
    p_r=floor(a_r),   q_r=floor(b_r),   N_r=q_r-p_r+1,
    H_r=floor(sqrt(X_r)),   C_r=(N_r+H_r)/(H_r+1).

For every integer j let

    P_(r,j)=1_(a_r<j<=b_r)*Lambda(j)*w_n(j),
    c_(r,j)=integral_((a_r,b_r] intersect [j,j+1)) w_n(x)dx,
    y_(r,j)=P_(r,j)-c_(r,j).

Define all three quantities to be zero outside p_r<=j<=q_r;
there are no nonempty cells or retained atoms outside that range.
The integral of an empty set is zero. Thus this convention does not
evaluate Lambda or log at nonpositive integers.

Let

    E_r=sum_j y_(r,j)^2
        +2*sum_(h=1)^H_r (1-h/(H_r+1))*sum_j y_(r,j+h)y_(r,j),
    S_(r,t)=sum_(h=0)^H_r y_(r,t+h),
    M_r=(N_r+H_r)^(-1)*sum_(t=p_r-H_r)^q_r S_(r,t)^2.

## Conclusion

The block contribution bcomp_r=sum_j y_(r,j) is exactly its original
compensated prime sum, and B_n=sum_r bcomp_r. Furthermore

    E_r=(H_r+1)^(-1)*sum_(t=p_r-H_r)^q_r S_(r,t)^2>=0,
    B_n^2 <= J*sum_r C_r*E_r = J*sum_r C_r^2*M_r.          (1)

For every block C_r<=2*sqrt(X_r). For each full block b_r=2X_r,

    sqrt(X_r)/2 <= C_r <= 2*sqrt(X_r).                    (2)

A sufficient arithmetic premise for the desired every-epsilon bulk
threshold is: for every epsilon>0 there is a finite D_epsilon>=0,
independent of n and r, such that

    M_r <= D_epsilon*exp(epsilon*n)/(4*J^2*X_r)            (3)

for all n>=2 and all its blocks. Then B_n^2<=D_epsilon*exp(epsilon*n).
Premise (3) is NOT proved here and is not asserted necessary for a
bound on B_n. Equivalently useful for paying (1) is a bound on its
whole nonnegative right side, without separate block estimates.

This is a standard-tool specialization (REPRODUCTION) under the
unchanged SPECIALIZE assessment review306, executed in step307.
Its substantive result is the exact sufficient interface and its cost,
not an arithmetic estimate or progress beyond the inspected methods.

## Proof

### Imported finite-sequence theorem

Import Hugh L. Montgomery, *Harmonic Analysis as found in Analytic
Number Theory*, in J. S. Byrnes (ed.), *Twentieth Century Harmonic
Analysis — A Celebration*, Kluwer (2001), pp271–293, unnumbered
van der Corput argument on printed pp276–277/PDF6–7:
https://www.nato-us.org/analysis2000/papers/montgomery.pdf#page=6 .
For an arbitrary complex sequence z supported on {1,...,N}, zero
elsewhere, and an integer H>=1, the signed intermediate inequality is

    |sum_j z_j|^2 <= (N+H)/(H+1)*
      [sum_j |z_j|^2+2 Re sum_(h=1)^H (1-h/(H+1))*
                                             sum_j z_(j+h)conj(z_j)].

The prior assessment inspected its complete shift/zero-extension proof.
No bounded-coefficient, positivity, or H<=N hypothesis is imposed.
We import this theorem rather than reprove it. Finite Cauchy–Schwarz
is the named standard input for combining block totals. The remaining
work is exact cell specialization, finite counting, and cost accounting.

### Exact cells, including all endpoint cases

Since 2^(J-1)<exp(n)<=2^J, the J nonempty half-open blocks (a_r,b_r]
partition (exp(n),exp(2n)]. At a common endpoint its atom belongs to
the preceding block. Their continuum integrals partition the same
interval up to sets of measure zero. The substitution u=log x gives

    integral_n^(2n) K_n(u)du=integral_exp(n)^exp(2n) w_n(x)dx.

For any block (a,b], each included integer j contributes exactly its
P_j once. The sets (a,b] intersect [j,j+1), p<=j<=q, partition the
continuum interval up to measure zero. Therefore

    sum_(j=p)^q y_j=sum_(a<m<=b) Lambda(m)w_n(m)
                                                   -integral_a^b w_n(x)dx.

At j=p=floor(a), the atom is absent, including when a is an integer,
but the integral from a to min(b,p+1) is retained. At j=q=floor(b),
the atom is included if a<q<=b. If b is an integer its last-cell
integral is zero and its atom is still included fully. If b is not
an integer its last-cell integral ends at b, not q+1. If p=q the
single cell retains the entire integral and any admissible atom by
these same indicators. This also covers a cut cell with no integer
atom. There is no endpoint approximation and no sampled compensator.
Adjacent blocks can use parts of the same unit cell; their exact totals,
not disjoint cell indices across blocks, are what will be combined.

For later interpretation the exact local window is

    S_(r,t)=sum_(t<=m<=t+H_r, a_r<m<=b_r) Lambda(m)w_n(m)
                  -integral_((a_r,b_r] intersect [t,t+H_r+1)) w_n(x)dx.
                                                               (4)

The integer convention in (4) must not be replaced by t<m<=t+H_r+1.
Its last cell can contain integral mass with no matching right atom.
This slight offset is part of the exact centering, not an error omitted
from an estimate.

### Energy, signed correlations, and block combination

Fix r. Translate j=p_r,...,q_r to 1,...,N_r and apply the imported
theorem with H=H_r. Zero extension includes every terminal case,
even H_r>N_r in a short final block. This gives bcomp_r^2<=C_r E_r.
Expanding the finite window-square sum counts each y_j^2 exactly
H_r+1 times and each pair y_j y_(j+h), 1<=h<=H_r, exactly
H_r+1-h times. The only potentially nonzero windows have
p_r-H_r<=t<=q_r. Division by H_r+1 proves the stated identity
for E_r and its nonnegativity. This identity also gives
C_r E_r=C_r^2 M_r. Finally finite Cauchy–Schwarz gives

    (sum_r bcomp_r)^2 <= J*sum_r bcomp_r^2,

which proves (1). All cross-block pairs are paid by this factor J;
none is asserted to vanish or reconstructed as a local correlation.

The diagonal in E_r is sum_j(P_(r,j)^2-2P_(r,j)c_(r,j)+c_(r,j)^2).
For every retained h>0, its correlation is exactly

    sum_j [P_(r,j+h)P_(r,j)-P_(r,j+h)c_(r,j)
                       -c_(r,j+h)P_(r,j)+c_(r,j+h)c_(r,j)].       (5)

Thus both mixed terms and the integral–integral term are retained.
The diagonal includes Lambda(j)^2 with its actual weights. Individual
correlations in (5) may have either sign. Replacing them by absolute
values or deleting exceptional shifts is not part of (1).

### Actual cost and required bound

Since b_r-a_r<=X_r, floor(b_r)-floor(a_r)+1<=X_r+2. Also
H_r<=sqrt(X_r)<H_r+1. Hence

    C_r <= sqrt(X_r)+1+2/sqrt(X_r) <=2*sqrt(X_r),

where X_r>=exp(2), so sqrt(X_r)>=e and
1+2/sqrt(X_r)<=sqrt(X_r). For a full block, N_r>=X_r and
H_r+1<=sqrt(X_r)+1<=2*sqrt(X_r), proving the lower bound (2).
The terminal block retains the actual N_r in (1); the same upper
bound holds but no full-block lower bound is claimed for it.
Inserting (3) and C_r^2<=4X_r into (1) yields

    J*sum_r C_r^2 M_r <= J*J*D_epsilon*exp(epsilon*n)/J^2,

as required. For the E_r normalization, the similarly sufficient
premise is E_r<=D_epsilon*exp(epsilon*n)/(2J^2 sqrt(X_r)).
On full blocks the exact M_r coefficient lies between X_r/4 and
4X_r, before the outside J. In particular paying this majorant
requires more than a claim that the windows are merely short:
its nonnegative summands cannot exceed the whole target upper
bound. If J*sum C_r^2 M_r<=D_epsilon exp(epsilon*n), then each
full block must satisfy M_r<=4D_epsilon exp(epsilon*n)/(J X_r).
This necessity concerns payment through (1), not actual B_n^2.
The sufficient and necessary budgets differ only by factors polynomial
in n, since J<=n/log(2)+1. All finite initial degrees remain covered
in (3); any eventual proof must also bound their finitely many blocks.

### Comparison and stopping decision

Reuse the inspected contract in review304: Matomäki–Radziwiłł–Tao,
*Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges*, arXiv1707.01315v3 (18 February2019),
Theorem1.3(i), p8, and Proposition3.1/Corollary3.2, pp32–34:
https://arxiv.org/pdf/1707.01315v3 . For fixed A>0, 0<delta<1/2,
X^(8/33+delta)<=H<=X^(1-delta), 0<=h0<=X^(1-delta), the former
controls the unweighted Lambda–Lambda correlation on X<m<=2X
for all but O_(A,delta)(H/log(X)^A) shifts in |h-h0|<=H,
with singular-series main term S(h)X and error
O_(A,delta)(X/log(X)^A). Its singular series is for nonzero h;
it does not supply the diagonal here. H=floor(sqrt(X)) is within
the permitted scale for fixed delta=1/10 and sufficiently large X,
so scale alone is not the failure of this application.

Neither that theorem nor its inspected proof cases supplies the
n-uniform growing Laguerre weights in (5), the two single-prime
mixed terms with the exact c_j, or their cancellation with the
singular series. The source's exceptional-shift count is not a
bound for their signed weighted total. Full blocks still have the
intersection of shifted supports, and a terminal piece is sharply
truncated. The arbitrary-sequence Corollary3.2 retains major/minor-arc
hypotheses; no such hypotheses have been proved for this centered
sequence. No weight variation estimate, exceptional-shift estimate,
or signed energy bound is silently imported here.

Stop at this unsupported essential premise. There is no need for
another absolute Laguerre norm or derivative calculation: the exact
arithmetic estimate (3), or an adequate aggregate variant in (1),
is absent already. No positive lower bound on B_n follows from the
size of the coefficient C_r^2; the signed window sums might be small.
The result is not an impossibility theorem for signed-energy methods.
Reopening payment through this majorant needs a materially new,
applicable estimate for the complete centered energy, not another
statement of the original criterion or a change of window notation.
L984(H) also retains both complementary logarithmic ranges and all
its other independent obligations. No RH candidate is obtained.

## Mathlib

Full matching coverage for this exact compensated specialization is
unchecked and unknown. Finite Cauchy–Schwarz and finite sum rearrangement
are supporting standard facts; no claim about a matching Mathlib theorem
or its absence is made. This proof is informal and has not been formalized.
