# Corollary 466b: reciprocal-density contact forcing and retained-zero cancellation

## Hypotheses

Use C466a's actual density p=theta_1, its smooth zero extension to R,
and h(s)=xi(1/2+sqrt(s))/c_0, B=log h, c_0=xi(1/2)>0.
In particular p>0 on (0,infinity), and p^(j)(0)=0 for every j>=0.
No assertion about zeros above the verified source height is added.

Use the actual zero kernel H from Sra, *On some positivity properties
of the Riemann Xi function*, [Hub v1, 29 October 2026](https://hub.valency.io/works/W_pr5z5huy_v1),
Section 2.1, Lemma 2.2 and Proposition 2.3. Its needed properties are
H in C^1(0,infinity), H>0, H'<0, integral_0^infinity H<infinity, and
B'(s)=integral_0^infinity exp(-st)H(t)dt. The counting, strip, symmetry
and verified-zero inputs are exactly those qualified in C466a.

Import the scalar equation

    x p(x) = integral_0^x H(t) p(x-t) dt,       x>0.          (1)

The precise reference is F. W. Steutel and K. van Harn, *Infinite
Divisibility of Probability Distributions on the Real Line*, Marcel
Dekker, 2004, Chapter V Theorems 2.11/2.16, equation (2.23),
[book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
The law is nondegenerate, positive, self-decomposable, has left endpoint
zero and canonical density k=H: positive decreasing H in the cited
Bernstein representation verifies the self-decomposability hypotheses.
The normalization is B(0)=0 and the Laplace transform is exp(-B(s));
the cited representation has no drift term. Thus k=H belongs to this
same law, not to a rescaled or translated density. Its support endpoint
is zero because p is positive on every positive interval and vanishes
on the negative half-line.
A singular k at zero is allowed (also Chapter III Theorem 10.4).
Assessment883 inspected these cases; equation (1) is imported, not new.

Fix a finite integer m>=2. Set

    A(y)=[p^(i+j)(y)]_(0<=i,j<m),
    e_m=(-1)^(m(m-1)/2),    D_m(y)=e_m det A(y).

Assume a hypothetical x_*>0 with D_m(x_*)=0 and D_j(x_*)>0 for
1<=j<m. For the first-contact interpretation assume additionally
D_m>0 immediately to the left of x_*. No contact is asserted to exist.
The formulas hold for any finite m, including symbolic
m>1810540931075, beyond the finite PF range reported in Sra's
[author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Theorem 1.2, pp2-3; that finite certificate is not an input or audited here.

Freeze the cofactors at x_* and define, for 0<=t<=x_*,

    V(t)=-e_m tr(adj(A(x_*)) A(x_*-t)).                    (2)

For the retained-zero comparison only set U=100, q=gamma_1^2 in
(196,225), epsilon=U^4 exp(-U). Remove one occurrence of the first
verified real zero and write

    H(t)=exp(-qt)+R_U(t)+H_>U(t),
    R_U(t)=sum_(gamma<=U, except that occurrence) exp(-gamma^2 t).

Multiplicity is retained. H_>U contains the complete conjugate-pair
tail and need not be positive. Sra v1 Lemma 2.2 supplies

    K_U=exp(-qt)+H_>U >= (1-epsilon)exp(-qt),
    -K_U' >= (1-epsilon)q exp(-qt).                      (3)

The source identities, regularity and scalar estimates were covered
before this invocation by assessment884 and its inspected inputs.
No complete monotonicity or higher-order PF sign is assumed.

## Conclusion

All integrals in the following identities converge absolutely:

    integral_0^x_* H(t)V(t) dt = 0,                      (4)
    x_* D_m'(x_*) = integral_0^x_* (-H'(t))V(t) dt
                  = integral_0^x_* (-H'(t)-qH(t))V(t)dt. (5)

V(0)=V(x_*)=0 and V takes both strictly positive and strictly negative
values in (0,x_*). The scalar lower bounds (3) therefore cannot simply
be multiplied by V and integrated. In the last expression in (5) the
retained exponential cancels exactly:

    x_* D_m'(x_*)
      = sum_(gamma<=U, except one gamma_1)
          (gamma^2-q) integral_0^x_* exp(-gamma^2 t)V(t)dt
        + integral_0^x_* (-H_>U'(t)-qH_>U(t))V(t)dt.     (6)

Equation (6) does not assert that its summands have a sign.

For a precise threshold using the derivative estimate in (3), put

    V_+=max(V,0), V_-=max(-V,0), T=-H_>U',
    S_+=q integral exp(-qt)V_+, S_-=q integral exp(-qt)V_-,
    F_U=integral (-R_U')V, J_U=integral T V,
    B_U=integral max(T,0)V_-.

These integrals are over [0,x_*]; S_+ and S_- are strictly positive.
The exact and sufficient tests, respectively, are

    x_* D_m'=F_U+S_+-S_-+J_U,
    D_m'>0  iff  J_U>-(F_U+S_+-S_-),                   (7)
    x_* D_m'>=F_U+(1-epsilon)S_+-S_--B_U.              (8)

Thus a sufficient strict inward sign would require

    F_U+(1-epsilon)S_+ > S_-+B_U.                      (9)

Neither (7)'s strict inequality nor (9) has been established.
The tiny scalar epsilon=10^8 exp(-100) gives neither a bound for
B_U/S_+ nor a positive lower bound for the signed head F_U.
No claim that those actual ratios are unbounded is made.

Replacing p by Theta=p/c_0 multiplies D_m and V by c_0^(-m);
all identities and signs are unchanged. This conditional reduction
does not establish a contact, sign preservation, global PF or RH.
Simultaneous contacts, compact continuation and L030 transfer remain
independent gaps.

## Proof

### Localization and differentiation

Fix b>x_* and work with x in a small open neighborhood of x_* inside
(0,b). Extend H by zero to the negative axis. Choose a smooth compactly
supported cutoff chi equal to one on a neighborhood of [0,b], and set
f=chi p. For t>=0 either x-t<0, where p and all its derivatives vanish,
or 0<=x-t<b, where f^(n)=p^(n). Thus H*f=H*p here, also when any
finite number of derivatives is put on the right factor.

Shrink the x-neighborhood and difference-quotient increments so that
both x and x+h stay in (0,b). For t>b the right factor and its
derivatives vanish throughout the segment between these two arguments.
The integrands and successive difference quotients are therefore bounded
by a constant times H(t) times the indicator of [0,b], since the needed
derivatives of f are bounded. This integrable majorant permits
differentiation under the fixed-domain convolution to every finite order:

    (H*p)^(n)(x)=integral_0^x H(t)p^(n)(x-t)dt.

This is the elementary dominated-convergence specialization of the
compact-support convolution theorem recorded below. H is not
differentiated at its singular endpoint. Smooth zero extension pays
all moving-endpoint terms, since every p^(j)(0)=0. From (1),

    H*p^(n) = x p^(n)+n p^(n-1),                       (10)

with the last term interpreted as zero for n=0. The argument does not
use unit mass and therefore applies to Theta as well.

### Two cofactor contractions

Let L_(i,i-1)=i for 1<=i<m, all other entries zero, and let
N=diag(0,1,...,m-1). Entrywise (10) gives

    H*A = x A+L A+A L^T,
    H*A' = x A'+N A+A N+A.                             (11)

For singular as well as nonsingular A, A adj A=adj A A=(det A)I.
Trace cyclicity and tr L=0 give

    e_m integral H(t)tr(adj A(x) A(x-t))dt=x m D_m(x).

At x=x_* this proves (4), with the minus sign in (2).
Jacobi's polynomial determinant derivative formula is also valid at
singular matrices: e_m tr(adj A A')=D_m'. The second identity in
(11), using 2 tr N+m=m^2, therefore gives

    e_m integral H(t)tr(adj A(x) A'(x-t))dt
        =x D_m'(x)+m^2 D_m(x).                         (12)

For the frozen weight, V'(t)=e_m tr(adj A(x_*) A'(x_*-t)).
Thus at contact (12) is x_*D_m'=integral H V', and V'(0)=D_m'(x_*).
No moving-cofactor derivative has been omitted: the weight is frozen
and Jacobi's formula already differentiates det A correctly.

### Singular-endpoint integration by parts

At zero, tr(adj A A)=m det A=0, so V(0)=0 and V(t)=O(t).
At x_* all p^(i+j)(0)=0, hence V(x_*)=0. A decreasing positive
integrable H satisfies

    0<=t H(t)<=integral_0^t H(u)du ->0  as t downarrow0.

Integration by parts away from zero and then this limit give

    integral_0^x_* t(-H'(t))dt
       =integral_0^x_* H(t)dt-x_*H(x_*)<infinity.        (13)

It follows that H(t)V(t)->0 at zero and (-H')V is absolutely
integrable there. The other endpoint term is H(x_*)V(x_*)=0.
Integrating on [eta,x_*] and letting eta downarrow0 proves
integral H V'=integral (-H')V. This proves (5)'s first equality;
subtract q times (4) for its second.

Every separate tail integral also converges absolutely. H_>U is H
minus finitely many smooth exponentials, and its derivative is H'
minus their derivatives. Equation (13) and V=O(t) control all terms
near zero; away from zero they are continuous. Substitution proves (6).

### Both signs of the weight are compulsory

The leading (m-1) by (m-1) block A_0 of A(x_*) is invertible because
D_(m-1)(x_*)>0, so A(x_*) has rank exactly m-1. In its symmetric
block form write the last column as (b,a). Then
v=(-A_0^(-1)b,1) spans its kernel. The adjugate is symmetric, has
every column in that kernel and bottom-right entry det A_0. Thus

    adj A(x_*)=(det A_0) v v^T.

For the monic polynomial P(z)=sum_(i=0)^(m-1) v_i z^i, equation (2)
becomes

    V(t)=(-1)^m D_(m-1)(x_*)
                    [P(partial_y)^2 p(y)]_(y=x_*-t).   (14)

The sign follows from e_m det A_0=(-1)^(m-1)D_(m-1).
The square is a square of a differential operator, not a pointwise
square of a real function, and has no automatic positivity.

If V vanished identically, the monic constant-coefficient operator
P(partial)^2, of order r=2m-2, would annihilate p on (0,x_*).
All r initial derivatives at zero vanish. For completeness set
Y=(p,p',...,p^(r-1)); then Y'=M Y for a constant companion matrix
and Y(0)=0. Smoothness extends this equation continuously to zero,
so its integral initial-value equation holds on each [0,a], a<x_*.
Integration and iteration give

    ||Y(t)||<=sup_[0,a]||Y|| (||M||a)^n/n!  for every n.

Hence Y=0, contradicting p>0. Therefore V is not identically zero.
Since H>0 and V is continuous, (4) forces both signs. Both occur on
open subintervals, proving S_+>0 and S_->0.

### The available bound and the unpaid threshold

Equation (3) says T>=-epsilon q exp(-qt). On V>=0 it gives
TV>=-epsilon q exp(-qt)V_+. On V<0 it only gives the useful lower
estimate TV>=-max(T,0)V_-. A positive tail derivative can therefore
make a negative contribution on this latter set. Integration yields

    J_U>=-epsilon S_+-B_U.

Splitting -H'=q exp(-qt)-R_U'+T proves (7)--(9).
The absolute convergence already proved also shows B_U is finite.
Finiteness does not provide the relative bound required by (9).

The K_U estimate itself has the same signed-weight limitation; the
exact contraction with the full actual kernel is (4).
Cancellation in (6) does not prove a retained zero can never help
with an additional estimate. It shows why its scalar positive margin
alone is not an independent positive forcing after the contact
equation is imposed.

At a first contact approached from positive D_m, D_m'(x_*)<=0.
A proved strict opposite sign in (7) would exclude it. No such sign
is proved. A weak derivative inequality would also leave tangential
crossing and a local barrier argument unresolved. C466a initializes
the boundary signs but does not supply this missing estimate.
This ends the bounded scalar-domination attempt without assuming a
degree-growing verified-factor supply or an actual-Xi failure. ∎

This is a specialization of the cited scalar equation and standard
cofactor algebra with a newly recorded local obstruction.
Assessment884 did not locate the contact comparison; no novelty
claim is made.

### Independent conceptual audit, 14 November 2026, step888

The conditional conclusion passes the approved audit relative to the
stated density, actual-H and scalar-law imports. No failed premise or
incorrect identity was found. The preceding clarifications make explicit
the source normalization, cutoff neighborhood and ODE endpoint on which
the proof already relies; they add no hypothesis or stronger conclusion.

In particular, the two entrywise recurrences in (11) were checked with
indices starting at zero: their extra coefficients are i+j and i+j+1,
respectively. Cyclic trace at a singular matrix gives the factors m and
2 tr N+m=m^2 in (12), without an inverse. The frozen derivative has
the plus sign V'(0)=D_m'(x_*). The endpoint estimate (13) controls both
the full kernel and each tail after subtraction of the finite smooth
head; it also controls B_U since |T|<=-H'+|R_U'|+q exp(-qt).

For (14), e_m/e_(m-1)=(-1)^(m-1) and the minus sign in (2) yield
(-1)^m D_(m-1). The kernel vector is real because A_0 is real invertible;
its last coordinate is one, so P is real and monic. Its operator square
has order exactly 2m-2. Flatness supplies all initial data needed by
the ODE uniqueness argument, hence a nonzero V. Equation (4) with
strictly positive H then forces open positive and negative intervals;
neither an algebraic square nor a cofactor sign is mistaken for a
pointwise square.

The exact decomposition gives (7). From T>=-epsilon q exp(-qt),
the positive part costs at most epsilon S_+, while the negative part
has lower bound -B_U; thus (8) and the sufficient test (9) have the
stated directions. No upper bound for T on that negative part follows
from (3). Subtracting q times (4) gives exactly (6), including repeated
zeros. Scaling p by c_0^(-1) scales adj A by c_0^(-(m-1)), hence both
V and D_m by c_0^(-m). Positivity just to the left and differentiability
give D_m'(x_*)<=0, without a simple-contact assumption.

This is local verification of the existing reduction, not a new
positivity theorem or independent replay of the imported source proofs,
zero/counting certificates or author-v3 finite PF range. A strict
weighted sign, simultaneous-contact treatment, a local barrier,
compact propagation and all-degree transfer remain unpaid. Bare scalar
retained-zero domination stays stopped in precisely the scope stated
above; the audit does not preclude a new estimate using extra structure.

### Finite Laplace head test, 14 November 2026, step911

This extension was not part of audit888. It records the complete finite
remainder and the precise inequality still unproved, not a head-sign
theorem. Reuse the hypotheses above, with x=x_*, n=m-1,
P(X)=sum_(k=0)^n a_k X^k, a_n=1, and c=(-1)^m D_n(x).
Define

    w(y)=P(partial_y)p(y),
    L_x(z)=integral_0^x exp(-zt)p(x-t)dt,
    Q_x(z)=sum_(k=1)^n a_k sum_(j=0)^(k-1)
                                  (-z)^j p^(k-1-j)(x),
    F_*(z)=integral_0^x exp(-zt)V(t)dt.

The complete null-row equations A(x)v=0 are exactly

    w^(j)(x)=0,   0<=j<=n.                            (15)

Every w-derivative at zero vanishes by p's flatness. For every real z,
the endpoint-corrected finite formula is

    F_*(z)=c P(-z)[P(-z)L_x(z)+Q_x(z)].               (16)

There is no division by P(-z), so (16) includes its real zeros.
In particular F_*(z)=0 when P(-z)=0. The polynomial Q_x has degree
n-1 and coefficient (-1)^(n-1)p(x) at z^(n-1), including n=1.
It is not identically zero. This does not assert that its finite
weighted sum below is nonzero or has either sign.

Here is a derivation retaining both endpoints before cancellation.
For a smooth real function G on [0,x], repeated integration by parts
gives, for k>=1,

    integral_0^x exp(zy)G^(k)(y)dy
      =(-z)^k integral_0^x exp(zy)G(y)dy
       +[exp(zy) sum_(j=0)^(k-1)
                      (-z)^j G^(k-1-j)(y)]_(y=0)^(y=x).  (17)

The k=1 case is the usual integration-by-parts formula; applying that
case to G^(k) and inserting the formula for k proves k+1, including
the signs and both boundary evaluations. The imported tool is John
K. Hunter, *The Riemann Integral*, Chapter 1, Theorem 1.53 and its
proof, printed p32, [primary notes](https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf).
Smoothness on this compact interval verifies its hypotheses at every
finite order. Assessment909/review910 already inspected that theorem.
The specialization is written out because the contact endpoint and
the two copies of P have different boundary data; no new general
integration-by-parts theorem is claimed.

Change variable y=x-t in (14), obtaining
F_*(z)=c exp(-zx) integral_0^x exp(zy)P(partial_y)w(y)dy.
Apply (17) to each term in the outer P. At y=0 every boundary
derivative of w vanishes. At y=x the needed w-derivatives have orders
0 through n-1 and vanish by (15). Consequently

    F_*(z)=c P(-z) integral_0^x exp(-z(x-y))w(y)dy.    (18)

Now apply (17) to w=P(partial)p. Its y=0 boundary terms vanish;
its y=x terms are exp(zx)Q_x(z). This proves (16). The single term
k=n, j=n-1 gives Q_x's highest coefficient, since a_n=1 and p(x)>0.
The null rows therefore remove the outer boundary bracket exactly,
but do not license deleting this inner bracket.

To use also the last null row j=n explicitly, repeated integration
of w^(n+1) with all terminal data (15) zero gives

    w(y)=((-1)^(n+1)/n!) integral_y^x
                              (s-y)^n w^(n+1)(s)ds.

Indeed the right side has derivative of order n+1 equal to w^(n+1),
and derivatives of orders 0 through n zero at x. The difference from
w is a polynomial of degree at most n with those zero terminal data,
hence zero. Substitution into (18) yields the second exact remainder

    K_z(s)=integral_0^s exp(-z(x-y))(s-y)^n dy,
    F_*(z)=(D_n(x)P(-z)/n!)
                   integral_0^x K_z(s) w^(n+1)(s)ds.  (19)

Fubini here concerns a continuous integrand on the compact triangle
0<=y<=s<=x, so it is absolutely integrable. The two signs
(-1)^m and (-1)^(n+1) cancel since m=n+1. For real z and 0<s<=x,
K_z(s)>0. No sign for its pairing with w^(n+1) has been established.
The first-contact condition supplies only the following endpoint datum:

    D_m'(x)=V'(0)=(-1)^n D_n(x) w^(n+1)(x)<=0.        (20)

For the equality, differentiate V(t)=c P(partial)w(x-t).
All terms except a_n w^(n+1)(x) vanish by (15); the derivative adds
a minus sign. The inequality uses positivity of D_m immediately to
the left, as above. Equation (20) does not give the needed integral
comparison on 0<s<x. Nor does (4)'s zero H-weighted pairing establish
that comparison. We retain (4), (15) and (20); none is replaced by
a positive raw moment or global PF assumption.

Finally let M_U be the finite multiset of rates lambda=gamma^2 in
R_U, removing exactly the one occurrence specified above, U=100.
Retain all other multiplicities, including any further occurrence of
gamma_1. Define finite real quantities

    A_U=sum_(lambda in M_U) lambda P(-lambda)^2 L_x(lambda),
    B_U^end=sum_(lambda in M_U) lambda P(-lambda)Q_x(lambda).

The superscript distinguishes B_U^end from the tail cost B_U in (8).
Since p>0, x>0 and every lambda>0, L_x(lambda)>0. Thus A_U>=0,
strictly if at least one term has P(-lambda) nonzero. Finite summation
in the definition of F_U and (16) gives exactly

    F_U=(-1)^m D_n(x)(A_U+B_U^end).                  (21)

Since D_n(x)>0, the required and still-unproved thresholds are

    F_100>=0 iff B_100^end>=-A_100,   for even m,
    F_100>=0 iff B_100^end<=-A_100,   for odd m.       (22)

Equivalently the unresolved remainder is the finite weighted sum of
(19): D_n(x)/n! times the integral of w^(n+1)(s) against
sum_(lambda in M_100) lambda P(-lambda)K_lambda(s). This version
has used every null row; its signed derivative pairing is still uncontrolled.
Neither positivity of p and K_lambda nor the operator square supplies
the sign of that pairing or the endpoint budget (22). No estimate
for the actual endpoint polynomial relative to the actual truncated
transform has been proved in this attempt. This is a precise stopping
point, not a proof that an additional actual-specific estimate is
impossible, and not a counterexample to the proposed actual head sign.

The achieved result is a finite identity and equivalent unpaid bound,
so step911 is EXPLORATION, not ADVANCE or an informative actual-head
negative result. The known finite integration-by-parts tool has been
specialized, not rediscovered. No Padé or Peano positivity theorem is
imported: the positive-measure orthogonality and signed-kernel
hypotheses missing in assessment909 remain missing. C466c-e are
contrasts, not mathematical inputs to (15)--(22). Even success at (22)
would leave first-zero signed mass, the full tail, strict forcing,
simultaneous contacts, propagation and L030 transfer open.

## Mathlib

Supporting convolution results were inspected in assessment883/885:
[HasCompactSupport.hasDerivAt_convolution_right](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html#HasCompactSupport.hasDerivAt_convolution_right)
and HasCompactSupport.contDiff_convolution_right, at
[source revision 26573066084e6e2aa8526ea358bc43b66d96f970](https://github.com/leanprover-community/mathlib4/blob/26573066084e6e2aa8526ea358bc43b66d96f970/Mathlib/Analysis/Calculus/ContDiff/Convolution.lean).
The specialization uses real Lebesgue measure, locally integrable H
extended by zero, and the compactly supported smooth factor chi p.
Full matching coverage of the Volterra/PF/contact result and the
determinant identities has not been checked. Supporting differentiation
coverage is not a formalization or verification of the conclusion.
Full matching coverage of (15)--(22), including their endpoint
specialization, has not been checked. No Mathlib absence is asserted.
