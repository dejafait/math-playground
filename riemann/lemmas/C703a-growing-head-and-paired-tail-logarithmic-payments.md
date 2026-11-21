# Corollary 703a: growing-head and paired-tail logarithmic payments

## Hypotheses

Fix one of the profiles e supplied by audited L703, with all its choices
made before n. Write

    E_c=sum_m exp(c*sqrt(1+|m|))*|e_m|<infinity,   c>0.

Use exactly L695's G_(n,e) and A_n(e), L666's family, and L657's
complete numerator K and denominator Q. Thus n=12q+3, M=n/3,
J=n-1, h=27/(10n), x=-d=-5/4, R=11/8, U=121/64, and the available
indices are -2q<=m<2q. All masses are one, the anchor is x, all M
spatial moments and j=0 are retained, and the denominator angle is 1/u.
All torus means below are normalized. No head or intermediate profile
is assumed to have a Fourier gap or to solve the Picard equation.

Put H=ceil(n^(2/3)), L=H+1, and f=e^(H). On 0<=t<=1 let
e_m(t)=e_m for |m|<=H and e_m(t)=t*e_m otherwise, restricted to
the available indices. Write G_t,K_t,Q_t for this family; subscripts
0 and 1 in this file mean the head and actual endpoints, respectively,
not the completely unshifted profile. Define

    tau_n=sum_(available |m|>H) |e_m|,
    tau_bar_n=E_c*exp(-c*sqrt(1+H)),    tau_n<=tau_bar_n.

## Conclusion

For all sufficiently large admissible n (specifically n>=10^6 and
L<=n/40000 suffice for the head bounds),

    -log(2R)-4L*log(5*n^2/(2*L^2)) <= A_n(f)
      <= log[9+200*(2H+1)*exp((81/5)*(H+5/8))].            (1)

In particular A_n(f)=o(n). Consequently the approved target is
equivalent to the still-unproved lower bound

    [A_n(f)-A_n(e)]_+=o(n)
            iff liminf_(q->infinity) A_n(e)/n>=0.         (2)

The tail denominator payment and its path derivative satisfy

    |mean_u log|Q_1|-mean_u log|Q_0|| <= (54/25)*tau_n,
    sup_(t,|u|=1) |partial_t Q_t/Q_t| <= (54/5)*tau_n.    (3)

There is also an exact signed comparison retaining all zeros, stated
in (10) below. After separating the denominator terms it gives

    [A_n(f)-A_n(e)]_+
      <= [V_n(epsilon)]_+ + E_1(epsilon)
                              +(324/25)*tau_n.           (4)

Here V_n is the signed paired-tail variation defined in (9), and
E_1 is the nonnegative actual-endpoint numerator regularization error.
Neither term in (4) is asserted to be o(n). Section 5 proves that one
specified certificate, using the full degree-rectangle term bound and
an absolute estimate for V_n, cannot certify both costs as o(n), even
after (1) and (3) have been paid. This is a failure of that certificate,
not a lower bound on V_n, a counterprofile, or a disproof of (2).

This is local reproduction/specialization of existing sparse-head,
root-formula and regularization inputs. It resolves the independently
unproved growing-head payment in the scoped attempt, not its signed
tail target or a new general continuity theorem. The result has not
received a separate critical audit. Complete compensation, H/support,
Xi realization and actual-Xi positivity remain open; there is no RH
candidate.

## Proof

### 1. Scope, source reuse and the growing head

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-gevrey-growing-head-signed-log-scope.md`.
Reuse its primary comparisons and the step-114/126 assessments. L695's
absolute-cost counterprofile is not used as an L703 counterprofile.
L702's surviving signed interior is not discarded. The new test pairs
the actual tail replacements before estimating their logarithms.

For the head use L692 (2), whose support/onset conditions have been
audited. There are at most 2H+1<=2L changed nodes. Since L/n->0,
eventually L<=n/40000 and n>=10^6. Its pointwise spatial-mean bound
therefore integrates to the lower bound in (1). L657 supplies absolute
log integrability, including torus zeros. L695 (8) is an explicit
finite-n bound, valid whenever the available changed indices lie in
|m|<=H and n>=30000; its proof uses only that support and the cap.
Applying that bound at this particular H, rather than substituting H
into a fixed-H limit, gives the upper bound in (1).

Here L=O(n^(2/3)), so the magnitude of the lower expression is
O(n^(2/3)*log n), and the upper expression is O(n^(2/3)+log n).
Both divided by n tend to zero. This checks the support and limit
orders explicitly. By the 1-Lipschitz property of positive part,

    |[A_n(f)/n-A_n(e)/n]_+-[-A_n(e)/n]_+|
                                                 <= |A_n(f)|/n -> 0.

For a real sequence b_n, [-b_n]_+->0 iff liminf b_n>=0, including
the extended-real cases. This proves (2). No sign for A_n(e) follows.

The root/coefficient inputs behind L692/L695 are F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7, Lemma 1.6, p.8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
Their boundary-root formula and coefficient bound are imported through
the cited local proofs, not reproved here.

### 2. Exact paired factors and denominator payment

Set a_m(t)=x+i*h*(m+1/2+e_m(t)) and, for every available tail index,

    F_m(t,u,zeta)=R^(-1)*W_(a_m(t))(u)*T_M(a_m(t)*zeta/R).

On the product torus each F_m is nonzero. Indeed W has no circle
zero or pole by L666, and T_M(z)=(1-z^M)/(1-z) has no zero for
|z|<1. All the path nodes retain |a|<=r_*=273/200 and |Im a|<9/20.
Let rho=r_*/R=273/275. L695 (6) gives

    |partial_a log W_a(u)|<=6n.

For z=a*zeta/R, logarithmic differentiation of T_M gives

    |partial_a log T_M(a*zeta/R)|
      <= R^(-1)*[1/(1-rho)+M*rho^(M-1)/(1-rho^M)] <= 200.   (5)

The last inequality uses
M*rho^(M-1)<=sum_(k=0)^(M-1)rho^k=(1-rho^M)/(1-rho)
and 2/[R*(1-rho)]=200. Thus for n>=30000,

    lambda_m:=partial_t F_m/F_m,
    |lambda_m|<=(81/5+540/n)*|e_m|<=17*|e_m|,
    F_m(t)=F_m(0)*exp(integral_0^t lambda_m(s)ds).       (6)

This is a paired relative bound on each term, with its actual complex
sign retained. It is not a relative bound on their sum G_t.

L657's Q_t=C_x*product_(a!=x) A_a has
A_a(u)=product_(j=1)^J(a-t_j*u). Only the tail factors move. Since
|a-t_j*u|>=d-1=1/4 on |u|=1, differentiation gives

    ell_t(u):=partial_t Q_t/Q_t
      =sum_(tail m) sum_(j=1)^J i*h*e_m/(a_m(t)-t_j*u),
    |ell_t(u)|<=4hJ*tau_n<=(54/5)*tau_n.               (7)

Integration along the nonvanishing path also gives
|Q_t/Q_0|<=exp((54/5)*tau_n) on the angular circle. No branch of a
logarithm is continued through a zero; equivalently integrate the
logarithmic derivative of these nonzero individual factors.

The complete root formula, already specialized in L657 (10), gives

    mean_u log|Q_t|=J*log U+J*sum_(a!=x)log|a_m(t)|.

Because |a_m(t)|>=d, the absolute derivative of each moving logarithm
is at most h*|e_m|/d. Integrating yields
|mean log|Q_1|-mean log|Q_0||<=Jh*tau_n/d<=(54/25)*tau_n.
This proves (3) with all exterior factors and original endpoints.
L703 supplies tau_n<=tau_bar_n=o(1). No Fourier gap on the path
was needed or inferred.

### 3. Exact signed comparison, normalization and zeros

Fix n and put b=||K_0||coeff,infinity>0 and P_t=K_t/b. This b is
constant along the path, so no derivative of a normalization is omitted.
For epsilon>0 define

    R_t(epsilon)=mean_(u,zeta) (1/2)*log(|P_t|^2+epsilon^2),
    E_t(epsilon)=R_t(epsilon)-mean log|P_t| >=0.          (8)

All K_t are nonzero by L657. Its integrability conclusion applies to
every fixed t, since every path displacement is admissible. For fixed
n and t, E_t(epsilon)->0 as epsilon decreases to zero: for epsilon<=1
the integrand is bounded by
(1/2)*log(|P_t|^2+1)-log|P_t|, an integrable function. No assertion
uniform in n or t is made. For fixed epsilon>0, smoothness on the
compact path and torus justifies differentiating R_t and integrating
that derivative. There is no differentiation of an unregularized log.

Since partial_t G_t=sum_(tail m)lambda_m F_m, exact differentiation
of K_t=Q_t G_t gives

    partial_t P_t=ell_t*P_t+(Q_t/b)*sum_(tail m)lambda_m F_m.

Define the real signed quantity

    V_n(epsilon)=-integral_0^1 mean_(u,zeta)
      Re[conj(P_t)*(Q_t/b)*sum_(tail m)lambda_m F_m]
                                  /(|P_t|^2+epsilon^2) dt,
    D_Q(epsilon)=-integral_0^1 mean_(u,zeta)
      |P_t|^2*Re ell_t/(|P_t|^2+epsilon^2) dt,
    Delta_Q=mean_u log|Q_1|-mean_u log|Q_0|.             (9)

The numerator polynomial and the actual inverse-angle denominator
have been kept together until this exact identity. Subtracting the
two endpoint means, with the signs of the errors retained, yields

    A_n(f)-A_n(e)
      =V_n(epsilon)+D_Q(epsilon)-E_0(epsilon)
                                   +E_1(epsilon)+Delta_Q. (10)

By (3) and (7), |D_Q|+|Delta_Q|<=(324/25)*tau_n. Dropping only
the favorable -E_0 term and taking positive part proves (4).
Thus the negative logarithmic mass is explicitly present in E_1 and
V_n. Boundary zeros, multiplicities, spatial degree drops, and cancelled
Q factors are all retained. The independent limit epsilon->0 is valid
at fixed n; choosing epsilon_n still requires quantitative payment.

### 4. A fully specified regularization certificate

Reuse F. Brunault, A. Guilloux, M. Mehrabdollahei and R. Pengo,
*Limits of Mahler Measures in Multiple Variables*,
[arXiv:2203.12259v2](https://arxiv.org/pdf/2203.12259v2),
27 June 2022, Proposition 4.10 and proof p.11, with the normalization
and matrix conventions in Sections 2.2--2.3. This is the source
inspected in the invocation-start assessment. For d variables, k>=2
terms, maximum coefficient one, 0<alpha<1 and the ordinary torus
(A=I_d, hence rho(A)=infinity), its nonnegative error for
(1/2)log(|P|^2+epsilon_source) is at most

    12*k^2*(18*d*k^2)^(d-1)*alpha^(1-d)/(1-alpha)
                *epsilon_source^((1-alpha)/(2*(k-1))).

Here use d=2, alpha=1/2 and

    T_n=M*(M*J+1),     B_n=1728*T_n^4,
    b_1=||P_1||coeff,infinity>0,     s=epsilon/b_1<=1.

L657 gives deg_u K_t<=MJ and deg_zeta K_t<=M-1, so T_n bounds
the number of nonzero coefficients; it is a coarse bound, not a claim
that every coefficient is nonzero. Apply the source to P_1/b_1 with
epsilon_source=s^2. If its actual term count is k>=2, increasing k
to T_n increases the bound for 0<s<=1. If it has one term, its error
is (1/2)log(1+s^2)<=s^2/2 and is bounded by the same expression.
Thus, with every normalization included,

    0<=E_1(epsilon)<=B_n*s^(1/[2*(T_n-1)]).             (11)

No assumption on coefficient separation, transversality or absence of
torus zeros enters this specialization. The theorem is not reproved.

### 5. The absolute variation certificate still fails

Test whether (6) combined with (11) pays (4). Integrating L695 (6)
from the anchor to any node gives |W_a|<=exp(6n*|Im a|)
<=exp(27n/10). Also R^(-1)|T_M(a*zeta/R)|<=100. The elementary
inequality y/(y^2+epsilon^2)<=1/(2epsilon), (6) and (7) therefore
give the valid, but unsigned, estimate

    |V_n(epsilon)|<=U_n(epsilon),
    U_n(epsilon)=850*exp((54/5)*tau_bar_n)*tau_bar_n
          *(||Q_0||infinity/b)*exp(27n/10)/epsilon.     (12)

The infinity norm in (12) is on the angular circle. This estimate was
obtained only after exact pairing. It does not estimate the sign of V_n.

The incompatibility of these two particular returned bounds can be
checked including their previously unknown coefficient normalization.
Cauchy's coefficient formula on the product torus and K_1=Q_1 G_1
give

    b_1<=||K_1||infinity/b
       <=exp((54/5)*tau_n)*(||Q_0||infinity/b)
                                           *100*M*exp(27n/10).

Consequently (12), as an explicit expression, satisfies

    U_n(epsilon)>= (17/(2M))*tau_bar_n/s.              (13)

For (11)'s returned upper bound to be o(n), it must eventually be
at most n. Hence it requires

    s<= (n/B_n)^(2*(T_n-1)).

At every such choice (13) implies

    U_n(epsilon)>= (17/(2M))*tau_bar_n
                              *(B_n/n)^(2*(T_n-1)).   (14)

For E_c>0, the logarithm of the right side is
Theta(n^3*log n)-O(n^(1/3)), since T_n~n^3/9 and
log tau_bar_n=log E_c-c*sqrt(1+ceil(n^(2/3))). It therefore grows
faster than n. If E_c=0 there is no tail and no obstruction. Requiring
the error bound to be o(n), rather than merely at most n, only makes
the incompatibility stronger.

Equations (13)--(14) lower-bound the computed upper-bound expression
U_n, not the actual |V_n| or the target loss. A large majorant never
establishes a large mathematical error. Actual term sparsity, signed
variation, sharper zero geometry or a different comparison could do
better. This attempt has not proved any of them. It stops the tested
pairing-plus-absolute-variation certificate and preserves (2) as open;
it does not revive L695's old counterprofile or discard L702's interior.
No numerical screen, n-dependent profile selection, or interchange of
the n and regularization limits is used.

## Mathlib

Full matching coverage of this growing-head specialization, paired-tail
identity and certificate incompatibility has not been checked. The
supporting Mahler/root-formula coverage recorded in L657/L695 is reused;
no full matching theorem or formal verification is claimed. Coverage
of the imported multivariate regularization bound is also unchecked.
Unknown availability is not evidence of absence.
