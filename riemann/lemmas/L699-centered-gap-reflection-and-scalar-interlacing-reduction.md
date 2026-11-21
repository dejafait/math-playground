# Lemma 699: reflected centered-gap profile and a conditional scalar charge payment

## Hypotheses

Select exactly the fixed prescribed-center Picard solution of L696
Section 2, using L694's real even cutoff Phi, its real even cutoff eta,
and its fixed constants and width. All these choices precede n. Put

    d=5/4, x=-d, R=11/8, U=R^2, r_*=273/200,
    n=12q+3, q>=1, J=n-1, M=4q+1=n/3, h=27/(10n),
    a_m=x+i*h*(m+1/2+e_m),       -2q<=m<2q,
    Z={x} union {a_m: -2q<=m<2q}.

Use L666's full rational W_a, c_(0,n)=R^(-1) sum_a W_a and
G_n with all M spatial moments. In particular retain unit original
masses, the anchor, j=0 and denominator angle 1/u. Write

    A_a(u)=product_(k=1)^J (a-t_k*u),
    C_a(u)=product_(k=1)^J (U*u-t_k*a),       t_k=k/n,
    Q_n(u)=C_x(u)*product_(a!=x) A_a(u),
    K_(0,n)(u)=Q_n(u)*c_(0,n)(u),
    p_j=x*j/(U*n),       1<=j<=J,
    rho_(j,n)=Res_(u=p_j) c_(0,n)(u).

Here a removable p_j has residue zero. K_(0,n) is L657's polynomial
K(u,0), including any factors cancelled in the rational quotient.

The additional **conditional sign hypothesis** at a given n is:
all J residues rho_(j,n) are nonzero and have the same sign. That
sign may depend on n. This hypothesis is not established for the
selected profile, nor assumed in the unconditional conclusions below.

## Conclusion

The selected exact l1 profile satisfies

    e_(-m-1)=-e_m                  for every m in Z.             (1)

It still has L696's fixed centered Fourier gap and cap 1/8. Its finite
node set is closed under conjugation; c_(0,n) is a real rational
function, Q_n and K_(0,n) are real polynomials, and K_(0,n)(0)>0.

Let Z_(0,n) be the sum of log(1/|beta|) over all roots of K_(0,n)
in the open unit disk, with multiplicity. The exact scalar accounting is

    L_n:=mean_(|u|=1) log|c_(0,n)(u)|
       =log c_(0,n)(0)+Z_(0,n)-P_n,
    P_n=sum_(j=1)^J log(1/|p_j|),
    c_(0,n)(0)>=M*d^2/(R*r_*^2).                              (2)

Under the additional sign hypothesis at n,

    Z_(0,n)>=P_n-log(n*U/d),
    L_n>=log[d^3/(3*R*U*r_*^2)].                              (3)

Thus the sign hypothesis on an unbounded subsequence would suffice
for the step-129 scalar limsup target. On that same subsequence the
complete two-circle mean of G_n would satisfy the same lower bound.
This is a sufficient condition only: failure of a residue sign does
not refute the scalar target or the complete-spatial compensation.

The residue test remains the explicit signed expression (7) below.
No residue sign, unconditional logarithmic rate, admissible scalar
counterprofile, H/support conclusion or Xi result is established.
This is a local symmetry specialization and conditional Jensen reduction,
not progress beyond a matching inspected source theorem or a claim of
originality. Step 133 audited only the reflection and exact residue inputs
needed by L700; the conditional charge and spatial comparison remain
without a separate critical audit. The completed
step is EXPLORATION because the required charge payment remains conditional.

## Proof

### 1. Scope, existing inputs and reflection of the exact Picard limit

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-centered-gap-scalar-complete-log-lower.md`.
It covers one analytic scalar complete-charge test using the exact
prescribed-center construction and finite endpoints. Reuse L694's
audited convergence of the same Picard iteration in both the coefficient
sup norm and the Wiener norm; L696 verifies the center and all changed
prescription hypotheses. The finite numerical array from step 127 is
not an input. No contraction theorem or Fourier-gap existence theorem
is reproved here.

For the circle coefficient convention of L694 define the linear map

    (Theta T)(t)=-exp(-2*pi*i*t)*T(-t).

It sends the real coefficient sequence alpha_m=T-hat(m) to
(Theta alpha)_m=-alpha_(-m-1). Therefore it is an involutive isometry
for both coefficient norms, preserves real coefficients, and preserves
support in the symmetric interval [-l,l]. The integer-frequency
multiplier is a well-defined smooth function on the circle.

For the selected prescription, chi is real and even. On its support
Psi(t)=-1/(2*pi*i*t), so the actual input Q to L694's Picard iteration is

    Q(t)=-exp(-pi*i*t)*chi(t)/(2*pi*i*t),                         (4)

with value zero near t=0 and outside the support. Thus Theta Q=Q.
The half-integer phase in (4) is used only on this compact support,
not asserted to be a periodic multiplier on arbitrary distributions.

L694's nonlinear operator is

    R(alpha)(t)=sum_m exp(2*pi*i*m*t)
      *(exp(2*pi*i*alpha_m*t)-1-2*pi*i*alpha_m*t)
      *Phi(t)/(2*pi*i*t).

Substitute (Theta alpha)_m=-alpha_(-m-1) and reindex k=-m-1.
Evenness of Phi and the change of sign of 2*pi*i*t give, term by term,

    R(Theta alpha)(t)=-exp(-2*pi*i*t)*R(alpha)(-t)
                    =Theta R(alpha)(t).                       (5)

This reindexing is justified in the Wiener norm: each Picard coefficient
sequence is in l1, and L694 (3)--(4) prove absolute convergence of
the nonlinear series there. The apparent t=0 values are removable.
It also holds for the final sequence by the same estimates.

The iteration T_0=Q, T_(k+1)=Q-R(c(T_k)) consequently preserves
Theta T_k=T_k by (4)--(5). L694 proves convergence of this very
iteration in the Wiener norm; Theta is continuous in that norm.
Its exact limit therefore satisfies Theta T=T, which is (1) for
e_m=T-hat(m). No uniqueness assertion outside the source's invariant
ball and no second fixed point are used. The gap, summability and cap
follow from the unchanged L694/L696 construction.

The reflection m -> -m-1 preserves exactly -2q<=m<2q and sends
m+1/2+e_m to its negative. Thus it sends a_m to its conjugate.
There is no nonanchor fixed point or collision, by cap 1/8. In L666's
finite rational formula

    W_a(u)=(x/a)*A_x(u)*C_a(u)/(A_a(u)*C_x(u)),                  (6)

all constants other than a are real. Hence
W_conjugate(a)(conjugate(u))=conjugate(W_a(u)). Summing paired nodes
proves the real-rational assertion. Q_n is real by its paired factors;
K_(0,n)=Q_n c_(0,n), already a polynomial by L657, is therefore real.
At zero, C_x(0)>0. The paired A_a(0) factors have positive product,
so Q_n(0)>0. Also c_(0,n)(0)=R^(-1) sum_a x/a is real and positive,
since each summand has real part d^2/|a|^2. The strict family bound
|a|<r_* from L666 gives the stated weak lower bound in (2) and
K_(0,n)(0)>0.

### 2. Complete scalar charge, including cancelled and boundary roots

Import the finite polynomial and rational root formula from F. Brunault
and W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
The prior assessment inspected the rational extension and all root
modulus cases. Complex coefficients and repeated or boundary roots are
allowed. No coefficient integrality or zero separation is required.
This is precisely the Jensen input already applied in L657.

Q_n has exactly the simple interior roots p_j; its other roots are
a/t_k, of modulus >d>1. K_(0,n)(0) and Q_n(0) are nonzero.
Apply the imported formula separately to these two polynomials and
subtract. Boundary numerator roots have zero charge and integrable
logarithms. The resulting scalar identity is (2). If a pole cancels,
the matching root of K_(0,n) stays counted and cancels its denominator
charge. All remaining numerator roots are retained. For each finite n
the scalar logarithm is absolutely integrable, since it is a nonzero
rational function without circle poles. No limit in n or logarithmic
regularization has been interchanged.

### 3. What real interlacing would pay, and the missing signed estimate

Assume the stated sign hypothesis at this n. The p_j are actual simple
poles, ordered p_J<...<p_1<0. There are no other poles on any interval
(p_(j+1),p_j), since all other possible poles in (6) are nonreal.
On this interval c_(0,n) is real and continuous. If all residues are
positive, its right limit at p_(j+1) is +infinity and its left limit
at p_j is -infinity. If they are all negative the two signs reverse.
The intermediate value theorem gives a zero beta_j in every such
open interval. These J-1 zeros are distinct, and Q_n is nonzero there,
so all are roots of K_(0,n). Moreover

    |beta_j|<|p_(j+1)|<1.

All additional interior numerator roots make nonnegative contributions.
Therefore

    Z_(0,n)>=sum_(j=1)^(J-1) log(1/|p_(j+1)|)
            =P_n-log(1/|p_1|)=P_n-log(n*U/d).

Together with (2) and M=n/3 this proves (3). The smallest-pole endpoint
cost log(n*U/d) is included; no zero next to the origin is assumed.
The bound is uniform in n once the conditional sign hypothesis holds.
On an unbounded subsequence division by n gives a lower limsup of zero.
This implication does not assert that such a subsequence exists.

For clarity, the exact signed residue that still needs control is

    rho_(j,n)=A_x(p_j)/[R*U*product_(1<=k<=J,k!=j)(U*p_j-t_k*x)]
              *sum_(a!=x) (x/a)*C_a(p_j)/A_a(p_j).             (7)

It follows directly by taking the residue in (6). All A_a(p_j) are
nonzero. The anchor contributes no residue, but remains in c_(0,n)
and in its center value. The conjugate pairs make the sum in (7) real;
they do not make it positive. Since J is even, A_x(p_j)>0, whereas
the displayed real prefactor has sign (-1)^(j-1). Thus the unproved
condition requires the real sums in (7) to have a strict alternating
sign pattern, up to one overall sign. Neither unit masses nor the
real-frequency gap supplies that inequality in the established inputs.
This attempt obtained no sign estimate or proof of its failure.

### 4. Legitimate downstream spatial comparison

For all angular u except the finitely many scalar zeros, G_n(u,.)
has nonzero constant coefficient c_(0,n)(u). The imported polynomial
root formula gives

    mean_(|z|=1) log|G_n(u,z)|>=log|c_(0,n)(u)|.

L657 proves absolute integrability of log|G_n| on the full product
torus for this family. The scalar logarithm is integrable as above,
so Fubini and integration of this almost-everywhere inequality give
the claimed complete-spatial comparison. All M prescribed moments and
any actual spatial degree drop remain included. This does not control
H, a norm ratio, support, realization or any actual-Xi sign.

## Mathlib

Full matching coverage for the reflected Picard specialization and the
conditional finite-family residue criterion is not checked. This is
not evidence of absence. The existing supporting
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
record includes `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`; these support the root formula, not the
unproved residue signs. No formal verification is claimed.
