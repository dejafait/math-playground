# Lemma 650: full-grid pole isolation loses on a close admissible pair

## Hypotheses

Keep n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100,
t_j=j/n and |u|=1. The common distinct pole set Z has Re(a)=x,
|a|<=R-eta and x in Z; original simple-pole residues r_a are positive
integers and M=sum r_a<=n/3. There is no separation, symmetry or
coefficient-integrality assumption. Set

    P(z)=product_a (z-a)^(r_a),  L=P'/P,
    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta),  W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

Use normalized circle measures and inner product <f,g>=mean f*conj(g),
linear in the first variable. Let F_u be C645y's full analytic component
at K=n, so b_u q_u=B_u(x)L(R*zeta)-F_u. Retain L649's c,T and
kappa=(I-T^*T)c. Define the anti-linear isometry

    (J s)(zeta)=zeta^(-1)*conjugate(s(zeta))

on boundary values of analytic polynomials. For each pole define

    S_a(z)=P(z)/(z-a)^(r_a),
    s_a(zeta)=S_a(R*zeta)/S_a(a),
    e_(a,u)=P_-(b_u J s_a),  d_(a,u)=P_+(b_u J s_a).       (1)

The denominator S_a(a) is nonzero for distinct poles. Its degree is
M-r_a: multiplicities have not been silently replaced by distinct roots.
The duals d_(a,u) are nonzero; let

    J_a(u)=|<F_u,d_(a,u)>|/||d_(a,u)||,
    C_iso,n=mean_u max_(a in Z) J_a(u)^2.                 (2)

This is the certificate obtained by selecting and scalar-normalizing
one pole-isolating dual at each angle. Arbitrary linear combinations
of different d_(a,u) are expressly outside this certificate.

## Conclusion

Under the linear Fourier identification V:l2 -> H^2_-,

    b_u V kappa_u=-F_u,  ||kappa_u||=||F_u||.             (3)

The full-grid polynomial dual in (1) has exact response and cost

    <F_u,d_(a,u)>=B_u(x)<L(R*zeta),e_(a,u)>-r_a W_a(u)/R,
    ||d_(a,u)||^2=||s_a||^2-||e_(a,u)||^2.               (4)

Each d has the full grid denominator and numerator degree <=n-1;
no grid prefix or spatial truncation of F occurs. Formula (2) is a
valid lower bound on mean ||kappa||^2.

Nevertheless this certificate fails the required relative squared rate
1/16. Take the admissible family, for every n>=6,

    epsilon=2^(-n),  a=x+i*epsilon,
    Z={x,a},  r_x=r_a=1,  P(z)=(z-x)(z-a),
    p_n=product_(1<=j<n) t_j/R,  C=217/55.

Writing beta_1=b_u'(0), one has |beta_1|=p_n, and for v=x,a, with
w the other pole,

    ||d_(v,u)||^2=(|w|^2+R^2(1-p_n^2))/epsilon^2,
    <F_u,d_(v,u)>=2 B_u(x)*conj(beta_1)/(v-w)-W_v(u)/R,
    J_v(u)<=C R^(-n).                                   (5)

Consequently, with L649's exact diagonal D_single,n,

    exp(n/16) C_iso,n/D_single,n
      <=(21/64) C^2 exp(-(2 log R-1/16)n) -> 0,
    2 log R-1/16>=85/176>0.                              (6)

This is a failure of separate pole isolation, not a counterexample to
the retained-energy comparison. In fact the sum of the two duals gives

    d_(x,u)+d_(a,u)=b_u/zeta,  ||b_u/zeta||=1,
    <F_u,b_u/zeta>=-(1+W_a(u))/R.                         (7)

For n>=10, this proves

    mean ||kappa||^2 >=(232/165)^2,
    64/21<=D_single,n<40.                                (8)

Thus the actual complete energy has a positive relative lower bound
on this sequence. Joint combinations cancel the separation cost that
individual column normalization retains. The general joint certificate,
the target for all admissible families, Xi realization and signs remain
unproved. This local finite-algebra obstruction is separately unaudited;
it is neither certified novelty nor an RH resolution candidate.

## Proof

### 1. Source scope and exact component identification

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-full-grid-polynomial-dual.md` authorizes
one P-dependent full-grid certificate and its complete norm cost.
Reuse its inspected source coverage. Import the Hardy projection
convention from L. Baratchart, S. Chevillard and T. Qian, *Minimax
principle and lower bounds in H2-rational approximation*, J. Approx.
Theory 206 (2016), 17--47, preprint v2, 24 March 2015,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004). Import scalar
orthogonality/Parseval from A. Levitt, *Analyse de Fourier et
applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
The residue theorem and simple-pole rule are R. W. Howell and J. H.
Mathews, *Complex Analysis*, online edition, front matter updated
22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
These statements were inspected in the reused assessment chain; no
new retrieval or independent audit of those sources is claimed here.

No general theorem is reproved. The specialization is needed to
identify the correct component, construct the full dual and evaluate
its separation cost. The scoped comparison checked C645y's prefix
stop, C645x's fractional universal dual, L646's exact-recovery input
and L648's reflected input. None evaluates the polewise dual (1).
They are contrasts, not mathematical premises below. The bounded
search does not establish originality.

Write Vv=sum_(k>=0) v_k zeta^(-k-1). L649's operator satisfies
V T v=P_-(b_u Vv). Multiplication by b_u is unitary on circle L2.
For g in H^2_-, conjugate(b_u)g still has strictly negative modes,
since conjugate(b_u) has only nonpositive modes. Thus its adjoint
on H^2_- is exactly multiplication by conjugate(b_u), with no
extra conjugation of sequence entries. It follows that

    b_u V T_u^* T_u c=V T_u c=B_u(x)L(R*zeta).

Subtract this from b_u q_u and use C645y's complete identity (8),
equivalently its identity (10) divided by the prescribed factors.
This proves (3). All rational functions have their poles off the
boundary; for each fixed family the relevant spatial expansions
converge absolutely and uniformly, and angular terms are continuous.
No limit in n or uniform pole separation is required for these identities.

### 2. The polynomial dual and all of its cost

For an arbitrary analytic polynomial s, the residue rule gives

    <q_u,J s>=mean zeta*q_u(zeta)*s(zeta)
             =R^(-1) sum_a r_a W_a(u) s(a/R).             (9)

Multiplying both entries of the inner product by b_u preserves it.
Separating negative and nonnegative modes in b_u J s gives

    <q_u,J s>=B_u(x)<L(R*zeta),P_-(b_u J s)>
                       -<F_u,P_+(b_u J s)>.             (10)

For s=s_a, all terms in (9) vanish except the pole a, where s_a=1.
This proves the response in (4), including the factor 1/R and the
conjugations. Unitarity, J's isometry and orthogonality give its norm
formula. Cauchy--Schwarz pointwise and then angular integration give
the lower certificate (2); angle-dependent selection adds no loss.

This really uses the complete polynomial identity. To see its form,
put beta_j=t_j*u/R, Acal=product_j(zeta-beta_j) and
Dcal=product_j(1-conj(beta_j)*zeta), so b_u=Acal/Dcal.
Here beta_0=0. If deg s=k, then J s is a Laurent polynomial from
degree -k-1 to -1. The numerator

    Acal J s-Dcal P_-(b_u J s)

has no negative powers, because its quotient by Dcal is analytic
and Dcal(0)=1. Its highest degree is at most n-1. Hence d is a
polynomial of degree <=n-1 over the same complete Dcal, with all
negative-mode subtraction included. It is also orthogonal to b_u H^2:
<b_u J s,b_u h>=<J s,h>=0 and the subtracted negative part is
orthogonal to analytic b_u h. There is no ambient inverse-recovery
optimization or initial-grid projection in this construction.

For completeness d cannot vanish for a nonzero s of degree k<n.
If it did, b_u J s=e would be a strictly negative Laurent polynomial
with lowest degree at least -k-1. Multiplication by zeta^(k+1)
would give b_u times a nonzero polynomial equal to a polynomial of
degree <=k. The latter vanishes at all n distinct grid zeros of b_u,
so is zero; this is impossible. Here k=M-r_a<n, as required.

### 3. An admissible close pair and its exact dual norms

For the displayed family n>=6, M=2<=n/3, the poles are distinct and
on the prescribed line, and

    |a|<=d+epsilon<=81/64<273/200=R-eta.

All original residues are one. Thus P has exactly the required integer
mass, and no fractional relaxation is used. For v one pole and w the
other, s_v(zeta)=(R*zeta-w)/(v-w). Write s_v=s_0+s_1*zeta.
Since b_u(0)=0, its negative product with J s_v is exactly

    e_(v,u)=beta_1*conj(s_1)*zeta^(-1),
    beta_1=product_(1<=j<n)(-t_j*u/R).

The zeroth negative coefficient of L(R*zeta) is 2/R. Therefore

    <L(R*zeta),e_(v,u)>=(2/R)*conj(beta_1)*s_1
                                 =2 conj(beta_1)/(v-w).

Also |s_0|^2=|w|^2/epsilon^2 and |s_1|^2=R^2/epsilon^2.
Substitution in (4) proves both exact expressions in (5).
In particular ||d_(v,u)||>=d/epsilon, so these duals are nonzero.

### 4. Uniform angular bounds and comparison with the required rate

The finite disk-factor identity

    |U-conj(b)z|^2-R^2|z-b|^2
                      =(U-|z|^2)(U-|b|^2)>0

for |z|,|b|<R proves |B_u(x)|<=1. To bound W_a without losing
uniformity in u, write each of its n factor ratios as

    [(x-t_j*u)/(a-t_j*u)] * [(U-t_j*a/u)/(U-t_j*x/u)].

The two factors differ from one by at most 4 epsilon and
(64/41)epsilon, respectively: |a-t_j*u|>=d-t_j>1/4,
and |U-t_j*x/u|>=U-d=41/64. Finite telescoping of products gives

    |W_a-1|<=(1+4epsilon)^n(1+(64/41)epsilon)^n-1
                  <=exp(6n epsilon)-1.                  (11)

For n>=6, n*2^(-n)<=3/32, so
|W_a|<=exp(9/16)<=1/(1-9/16)=16/7<3. The exponential estimate
uses its nonnegative series and 1/k!<=1, not a numerical approximation.
Since W_x=1, (5) consequently gives, for both v,

    J_v(u)<=(2p_n+3epsilon/R)/d.

Now p_n<=R^(-(n-1)) and epsilon=2^(-n)<=R^(-n), since R<2.
Thus J_v(u)<=((2R+3/R)/d) R^(-n)=C R^(-n), as asserted.
The anchor diagonal term is 1/(U-d^2)=64/21, proving (6).
Finally log R=integral_1^R dt/t >=(R-1)/R=3/11; hence
2 log R-1/16>=6/11-1/16=85/176. All estimates are uniform in u.
No angular sampling, omitted spatial tail or asymptotic quadrature is
used. The failure covers scalar normalization and arbitrary selection
between these two duals at each angle, but not their joint span.

### 5. The full energy stays large: precise scope of the stop

For this pair s_x+s_a=1. By (1), e_x+e_a=P_-(b_u/zeta)=0,
because b_u(0)=0; also d_x+d_a=b_u/zeta, of boundary norm one.
Adding (4) proves (7). For n>=10,
6n*2^(-n)<=60/1024<1/16, so (11) gives |W_a-1|<=1/15.
Therefore |1+W_a|>=29/15 and (7) gives
||F_u||>=29/(15R)=232/165, uniformly in u. This proves the
first bound in (8), using the exact norm link (3).

For n>=6, U-|a|^2=21/64-epsilon^2>1/4. Hence

    D_single,n=64/21+mean |W_a|^2/(21/64-epsilon^2)
                      <64/21+36<40.

This proves the second bound in (8). Separate columns have norms of
order epsilon^(-1); their sum removes those large terms exactly.
Thus this failure supplies no negative evidence about arbitrary joint
combinations or the original full energy. It specifically excludes
using (2) as a uniformly adequate relative certificate.

### 6. Verification limits

The proof above is analytic and exact. The companion finite check
`python3 scripts/one-sided-hankel/full-grid-pole-dual-check.py`
stores all rational data and checks in
`scripts/one-sided-hankel/full-grid-pole-dual-check.json`.
It compares the dual norm with complete inverse-grid-Gram interpolation
and the pairing with all grid residues, at real, imaginary and oblique
unit rotations for n=6,10. All 126 checks passed with exact identity
differences zero; all six complete check objects and the summary were
inspected. These finite checks test normalization and
conjugations; they do not prove the uniform estimates or replace a
separate conceptual audit.

## Mathlib

Full matching coverage for this exact P-dependent dual and its quantified
method obstruction has not been checked. Supporting Fourier/Parseval,
orthogonal projection, finite polynomial and residue inputs are those
cited above. Unknown coverage is not evidence of absence. No formal
result about the still-open uniform detector or actual Xi is assumed.
