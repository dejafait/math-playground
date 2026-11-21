# Lemma 559: retained endpoints in the paired-tail transverse audit

## Hypotheses

Use the explicit function in Michel Planat, *Curvature Transition Layers
and Paired-Tail Positivity for the Riemann Xi-Function*, Preprints.org
202606.1957 v1, posted 26 June 2026,
[primary text](https://www.preprints.org/manuscript/202606.1957/v1):
Section 3.1, Definitions 1--3, Theorem 3 and Proposition 9 with their
proofs, and Appendix C.1--C.3, Lemmas A3--A4.

    Phi(u) = sum_(n>=1) (2 pi^2 n^4 exp(9u/2)
                         -3 pi n^2 exp(5u/2)) exp(-pi n^2 exp(2u)).
    M(a,b) = Phi(a+b) Phi(a-b),       A(a,b) = -partial_b M(a,b).

Fix x>0, y>0 and an integer m>=0. Put

    k=2x,  l=m*pi/x,  r=(m+1)*pi/x,  J=[l,r],
    W(a)=a sinh(2ya),
    Q(a)=-integral_0^a b sinh(2yb) partial_a M(a,b) db,
    I1(a)=integral_0^a A(a,b) sin(kb) db,
    I2(a)=integral_0^a partial_b A(a,b) cos(kb) db,
    I3(a)=integral_0^a partial_b^2 A(a,b) sin(kb) db.

Here Q is exactly Definition 2. It is not the different envelope
printed in the abstract. Define the complete quantities from
Definition 3 and the explicit residual displayed in Theorem 3:

    C_Q=integral_J Q(a) sin(ka) da,
    C_eps=integral_J W(a) I1(a) da,       C_tot=C_Q+C_eps.

These definitions specify the quantities being audited. Their claimed
identification with a growth derivative is not assumed or proved.
L016 supplies the classical theta transformation used below to verify
smooth evenness of this Phi. L018 and L233 give the eventual target
interpretation only; neither is a mathematical premise for this audit.

For the additional audit dated 17 November 2026, use this same Phi,
which equals L019's K/4 by termwise comparison, and fix y>0. Let
K0=[a_-,a_+] and K1=[b_-,b_+] be nondegenerate compact intervals
with 0<b_-<a_-<a_+<b_+ and Q'(a)>=delta>0 on K0.
These intervals are not the theta kernel K. Only blocks with l in
K0 and J contained in K1 are considered in the uniform estimates.
The audited source is Michel Planat, *Nonlocal Cancellation in a
Theta-Kernel Decomposition of the Riemann Xi-Growth Derivative: An
Obstruction to Phase-Aligned Blockwise Positivity*, Preprints.org
202608.1692 v1, 25 August 2026, DOI
[10.20944/preprints202608.1692.v1](https://www.preprints.org/manuscript/202608.1692).
The precise inputs under review are Lemma 2, (8)--(11); Section 5,
Lemmas 4--5, Proposition 4 and Theorem 4, (38)--(49); Lemma 6,
(51); and Theorem 6, (60). This version is unrefereed.

## Conclusion

Both printed integrations by parts are correct before endpoint
deletion. Writing

    E(a)=A(a,a),        F(a)=partial_b A(a,a),
    G(a)=W(a) E(a),    H(a)=W(a) F(a),    T(a)=G'(a)+H(a),

the exact identities are

    I1(a)=-E(a) cos(ka)/k + I2(a)/k,
    I2(a)= F(a) sin(ka)/k - I3(a)/k,
    I1(a)=-E(a) cos(ka)/k + F(a) sin(ka)/k^2 - I3(a)/k^2.       (1)

Consequently the retained correction is

    B_J=integral_J [-G(a) cos(ka)/k + H(a) sin(ka)/k^2] da,
    C_eps=B_J-k^(-2) integral_J W(a) I3(a) da,                 (2)
    B_J=k^(-2) integral_J T(a) sin(ka) da
       =[T(l)-T(r)]/k^3 + k^(-3) integral_J T'(a) cos(ka) da.  (3)

In particular, with both outer endpoints displayed,

    C_tot=[Q(l)-Q(r)]/k + k^(-1) integral_J Q'(a) cos(ka) da
          +[T(l)-T(r)]/k^3 + k^(-3) integral_J T'(a) cos(ka) da
          -k^(-2) integral_J W(a) I3(a) da.                  (4)

The moving-limit terms are

    T(a)=W'(a) A(a,a)+W(a)[partial_a A(a,a)+2 partial_b A(a,a)],
    Q'(a)=-W(a) partial_a M(a,a)
          -integral_0^a b sinh(2yb) partial_a^2 M(a,b) db.     (5)

The boundary-free pointwise equality I1=-I3/k^2 printed after
Appendix C.3 is false for this Phi: take x=pi and a=1. More strongly,
on the single fixed complete block J_0=[0,1], x=pi, the correction
B_J is strictly negative for all sufficiently large fixed y>0.
Thus replacing I1 by -I3/k^2 while retaining the defined C_Q changes
the complete block.

This refutes the unrestricted exact cancellation in that literal
interpretation. That endpoint-deletion counterexample alone does not
refute positivity of C_tot, any global sum, or RH. The example is not
asserted to lie in Appendix C's
restricted certified post-crest region. Its regularity bounds do
not supply the missing cancellation, which Appendix C.1 separately
assumes. A differently defined residual or compensating parent term
would need an explicit identity; none is imported here.

The separate audit1275 below verifies the later source's negative-block
theorem: under the additional compact-interval hypotheses, eventually
C_tot<=-pi*delta/(4x^2) for every block starting in K0. Such increasing
intervals exist for the actual theta kernel, and pi/x<|K0| guarantees
an aligned left endpoint in K0. The complete block is used throughout.
This is a source-known obstruction to universal block nonnegativity,
with a corrected uniform-remainder constant list. It says nothing
about the sign of the global sum, a Schur form, or RH.

## Proof

### Regularity and an actual-theta endpoint

On every compact real u interval, every fixed derivative of the
displayed series is bounded termwise by C n^N exp(-c n^2), for
constants C,c>0 and some integer N. Uniform convergence therefore
justifies all differentiations used here.

Let theta be L016's theta series, and set
h(u)=exp(u/2) theta(exp(2u)). L016's transformation gives h(-u)=h(u).
Direct differentiation of this already convergent series gives

    (h''(u)-h(u)/4)/4=Phi(u).

Indeed, for t_n=pi n^2 exp(2u), applying d^2/du^2-1/4 to
exp(u/2)exp(-t_n) gives
exp(u/2)(4t_n^2-6t_n)exp(-t_n), and theta's nonzero terms have
coefficient 2. The n=0 term contributes zero. This verifies the
factor and shows that Phi is smooth and even, hence Phi'(0)=0.
This is a specialization of the imported theta transformation,
not an identification of the source's Xi normalization.

Put p0=Phi(0). Every summand of p0 is
pi n^2(2 pi n^2-3)exp(-pi n^2)>0, so p0>0.
Differentiating a Phi summand gives

    -(1/2) exp(u/2) t_n (8t_n^2-30t_n+15) exp(-t_n).

At u=2, t_n>=pi exp(4)>4. The polynomial 8t^2-30t+15
is positive for t>=4: its value at 4 is 23 and its derivative
16t-30 is positive there and thereafter. Every summand of
Phi'(2) is strictly negative and their sum converges.
Thus Phi'(2)<0.

Product differentiation, retaining the derivative at zero, now yields

    E(a)=-Phi'(2a)p0+Phi(2a)Phi'(0)=-p0 Phi'(2a),
    F(a)=-p0 Phi''(2a)-Phi(2a)Phi''(0).

In particular E(1)>0. The same calculation gives the useful check

    T(a)=-p0 W'(a)Phi'(2a)
         -W(a)[3p0 Phi''(2a)+Phi(2a)Phi''(0)].                (6)

### Inner endpoints

Freeze a,x,y while integrating in b. The first step is

    I1=[-A(a,b)cos(kb)/k]_(b=0)^(b=a)+I2/k
      =-E(a)cos(ka)/k+A(a,0)/k+I2/k.

The lower endpoint vanishes because
A(a,0)=-Phi'(a)Phi(a)+Phi(a)Phi'(a)=0. This uses the product
definition, not a cancellation with an outer term.

The second step is

    I2=[partial_b A(a,b)sin(kb)/k]_(b=0)^(b=a)-I3/k.

Its lower endpoint vanishes because sin(0)=0, without any assumption
that partial_b A(a,0) vanishes. The upper term is F(a)sin(ka)/k.
This proves (1), retaining both inner endpoints at both steps.

At x=pi and a=1, sin(ka)=0 and cos(ka)=1. Thus (1) implies

    I1(1)+I3(1)/(2pi)^2=-E(1)/(2pi)<0.                      (7)

This is an exact contradiction to the displayed boundary-free
pointwise identity, not a numerical approximation.

### Complete block and moving limits

Multiplying (1) by W(a) and integrating gives (2). The first outer
integration in its correction is

    -k^(-1) integral_J G(a)cos(ka) da
      =-[G(a)sin(ka)]_l^r/k^2
        +k^(-2) integral_J G'(a)sin(ka) da.

Both endpoint sines are zero because kl=2m*pi and kr=2(m+1)*pi.
This removes that bracket only. Adding the H integral gives the
first equality in (3). Integrating it once more gives

    -[T(a)cos(ka)]_l^r/k^3
       +k^(-3) integral_J T'(a)cos(ka) da,

and both endpoint cosines equal 1, proving the second equality.
Their coefficients need not be equal.

The total derivative of E is
E'(a)=partial_a A(a,a)+partial_b A(a,a). Combining G' and H
therefore gives precisely the first formula in (5), including the
second copy of partial_b A. Leibniz's rule on Q gives its second
formula. Independently, if

    P(a)=integral_0^a b sinh(2yb) M(a,b) db,

then P'(a)=W(a)M(a,a)-Q(a). In the Q block this reads

    C_Q=integral_J W(a)M(a,a)sin(ka) da
        -[P(a)sin(ka)]_l^r+k integral_J P(a)cos(ka) da.

Again the bracket is zero, while the diagonal W(a)M(a,a) term
remains. It is not either deleted coefficient in (1).
Finally the ordinary integration by parts of C_Q gives
[Q(l)-Q(r)]/k+k^(-1) integral_J Q'cos. Adding (2)--(3)
proves (4). All integrals are over compact sets with smooth
integrands; no infinite block sum or parameter interchange occurs.

### The correction need not vanish after complete-block integration

It would be invalid to deduce nonzero B_J merely from (7).
Here is a separate check on exactly J_0=[0,1], x=pi, k=2pi.
Let

    f(a)=a[-E(a)cos(2pi a)/(2pi)+F(a)sin(2pi a)/(2pi)^2].

This is continuous on [0,1], independent of y, with
f(1)=-E(1)/(2pi)<0. Equation (2) gives

    B_J(y)=integral_0^1 f(a)sinh(2ya) da.

For lambda=2y, substitute s=lambda(1-a) in the positive
exponential part. One obtains

    lambda exp(-lambda) integral_0^1 f(a)exp(lambda a) da
      =integral_0^lambda f(1-s/lambda)exp(-s) ds -> f(1).

Extend the integrand by zero for s>lambda. Its absolute value
is at most ||f||_infinity exp(-s), so dominated convergence
justifies the limit. The negative exponential part satisfies

    |lambda exp(-lambda) integral_0^1 f(a)exp(-lambda a) da|
      <=||f||_infinity exp(-lambda) -> 0.

Consequently

    (2y) exp(-2y) B_J(y) -> f(1)/2=-E(1)/(4pi)<0.            (8)

There is therefore a finite Y such that every fixed y>Y gives
B_J(y)<0 on this same block. This existence test supplies no
effective Y, no post-crest certification and no uniform global
bound. During each integration all parameters are fixed.
It disproves an asserted exact deletion, not a positivity inequality.

### Source comparison and the stopping decision

Proposition 9's proof appeals to equal phases and opposite
orientations without specifying the second term with its weight.
Theorem 3's proof, (7)--(8) in that source, starts instead with
the integral of M sin(kb): its two integrations retain

    -M(a,a)cos(ka)/k+M(a,0)/k
    -A(a,a)sin(ka)/k^2
    +k^(-2) integral_0^a partial_b A(a,b)sin(kb) db.

Those printed formulas provide neither the opposite terms asserted
there nor replacements for the E and F terms in (1).
Identifying an oscillatory phase supplies no coefficient identity.
We do not reconstruct the unspecified parent decomposition.

Appendix C.2--C.3's pre-deletion formulas have thus been reproduced,
while their unrestricted deletion fails for the stated explicit
quantities. The source's Proposition 11 also retains the first
boundary term, consistently with (1). Suppression arguments depending
on its removal are parked pending a different, complete identity.
This does not rule out signed estimates for the correction or
nonlocal cancellation in another correctly defined quantity.

### Audit1275: the later negative-block theorem

This subsection independently checks the hypotheses and estimates needed
for the cited later Theorem 6. It is a reproduction of a source-known
obstruction. The earlier endpoint-deletion counterexample is preserved.
The result here is that the actual theta kernel admits the intervals
in the additional hypotheses and, for every such fixed y,K0,K1,delta,
there is a finite X such that

    C_tot <= -pi delta/(4x^2) < 0                           (9)

for all x>=X and every integer m>=0 with l=m*pi/x in K0.
X also ensures J is contained in K1. For x additionally satisfying
pi/x<a_+-a_-, at least one such m exists. No numerical value of X,
uniformity as y decreases to zero, fixed-m limit, global integral
sign or Schur-form sign is asserted. Global monotonicity of Phi and
the source's Lemma 3 are not needed.

#### A rational check of the needed origin-curvature sign

Let q_n=pi n^2 and P(q)=32q^3-224q^2+330q-75. Differentiating the
uniformly convergent theta series twice gives

    c2 := Phi''(0) = sum_(n>=1) T_n,
    T_n = q_n P(q_n) exp(-q_n)/4.                          (10)

One can verify the polynomial without a numerical differentiation:
a summand is exp(u/2)(2t^2-3t)exp(-t), t=q_n exp(2u);
its first derivative is exp(u/2)(-4t^3+15t^2-15t/2)exp(-t),
and its second is exp(u/2)t P(t)exp(-t)/4. The compact
derivative domination proved above justifies summing these formulas.

We use Archimedes' classical bounds (in particular 3<pi<22/7) and the elementary
bounds 8/3<e<3. The latter follow from the positive exponential
series: terms through 1/3! sum to 8/3, and n!>=2^(n-1) for n>=2,
strictly for n>=3, bounds the remaining sum above by 1.
On [3,22/7], P''(q)=192q-448>0, while
P'(22/7)=-6358/49<0. Hence P is decreasing there and
P(pi)<P(3)=-237. Since exp(-pi)>exp(-4)>1/81,

    T_1 < -711/(4*81) = -79/36.                           (11)

For q>=12, P(12)=26925>0, P'(12)=8778>0 and P''(q)>0;
also 224q^2-330q+75>0. Thus 0<P(q)<32q^3 there, and this
applies to every q_n, n>=2. Write t_n=n^8 exp(-pi n^2).
For n>=2,

    t_(n+1)/t_n <= (3/2)^8 exp(-5pi)
                 < 26/18^5 < 1/100,

because (3/2)^8=6561/256<26 and e^3>(8/3)^3>18.
Furthermore pi^4<(22/7)^4<100 and exp(-4pi)<1/18^4.
The positive tail in (10) consequently obeys the geometric bound

    0 < sum_(n>=2) T_n
      < 8*100*256*100/(18^4*99)
      = 20480000/10392624 < 2.                            (12)

Combining (11)--(12) proves c2<-7/36<0. This deliberately coarse
rational bound verifies the sign required for (9). It does not
certify the sharper decimal intervals or c2<-8.02 printed in the
source. Put c0=Phi(0)>0, as proved above (also L019); evenness gives
Phi'(0)=0, so for p=-Phi'/Phi, p'(0)=-c2/c0>0.

The exact rational arithmetic and differentiated polynomial in
(10)--(12) are replayed by
`python3 scripts/theta-block/negative-block-arithmetic-1275.py`, with
the full arithmetic certificate at
`scripts/theta-block/negative-block-arithmetic-1275.json`.
This checks those finite operations only; the series domination,
transcendental inequalities and uniform analytic estimates are proved
in the text, not certified by the script.

#### Existence of the increasing interval, with a controlled derivative

Taylor's theorem for the smooth even Phi gives, uniformly for
0<=b<=a as a decreases to zero,

    M_a(a,b)=2c0*c2*a+O(a^3),
    M_aa(a,b)=2c0*c2+O(a^2),
    b sinh(2yb)=2y b^2+O_y(b^4).                          (13)

For example expand Phi(t)=c0+c2*t^2/2+O(t^4),
Phi'(t)=c2*t+O(t^3), Phi''(t)=c2+O(t^2) at t=a+b,a-b;
both arguments lie in [0,2a]. This proves both derivative
expansions directly, with uniform Taylor bounds.
Substitution into the definition of Q gives

    Q(a)=c_y a^4+O_y(a^6),   c_y=-(4/3)y*c0*c2>0.

We must not infer its derivative by differentiating an uncontrolled
error. Instead use the exact moving-limit formula (5). Its boundary
term is -4y*c0*c2*a^3+O_y(a^5), and its integral term is
-(4/3)y*c0*c2*a^3+O_y(a^5), by (13). Therefore

    Q'(a)=-(16/3)y*c0*c2*a^3+O_y(a^5)
          =4c_y a^3+O_y(a^5)>0                           (14)

for all sufficiently small a>0. Choose any nondegenerate closed
interval K0 strictly inside that increasing interval; continuity
gives delta=min_K0 Q'>0. This establishes the actual-theta
applicability of the interval hypotheses, without a global shape claim.

#### The complete transverse expansion

On the compact triangle a in K1, 0<=b<=a, all derivatives of A
are continuous. Oddness of A in b gives A(a,0)=A_bb(a,0)=0.
Extending (1) by two more ordinary integrations by parts gives

    I1(a)=-A(a,a)cos(ka)/k + A_b(a,a)sin(ka)/k^2
          +A_bb(a,a)cos(ka)/k^3-A_bbb(a,a)sin(ka)/k^4
          +k^(-4) integral_0^a A_bbbb(a,b)sin(kb) db.      (15)

At the first and third integrations the lower contributions contain
A(a,0) and A_bb(a,0), respectively; at the second and fourth they
contain sin(0). Thus all lower terms vanish for stated reasons.
Every upper term b=a in (15) is retained. Define the smooth functions

    g1=-W A(a,a),       g2=W A_b(a,a),
    g3= W A_bb(a,a),    g4=-W A_bbb(a,a).                 (16)

Their ordinary derivatives are derivatives along the diagonal:
for example d/da A_b(a,a)=(partial_a+partial_b)A_b(a,a).
No moving endpoint is treated as fixed. Multiplying (15) by W
gives four oscillatory terms g1*cos/k, g2*sin/k^2, g3*cos/k^3,
g4*sin/k^4 and the displayed integral remainder times W/k^4.

Here are explicit bounds that make the block expansion uniform.
Write h=2pi/k and alpha=l, so J=[alpha,alpha+h]. The required
moments, obtained by integration by parts, are

    integral_0^h sin(kt)dt = integral_0^h cos(kt)dt = 0,
    integral_0^h t sin(kt)dt = -2pi/k^2,
    integral_0^h t cos(kt)dt = 0,
    integral_0^h t^2 sin(kt)dt = -4pi^2/k^3,
    integral_0^h t^2 cos(kt)dt = 4pi/k^3.                (17)

The phase at alpha is 2m*pi. Taylor's theorem with third-derivative
supremum N3 bounds the integrated second-order Taylor remainder
by N3*h^4/24=(2/3)pi^4*N3/k^4. Consequently

    C_Q=-2pi Q'(alpha)/k^2-2pi^2 Q''(alpha)/k^3+R_Q,
    |R_Q| <= B_Q/k^4,
    B_Q=(2/3)pi^4 ||Q'''||_(infinity,K1).                (18)

Apply the cosine Taylor expansion through order two to g1 and
the sine expansion through order one to g2. The latter remainder
is at most ||g2''||*h^3/6. The g3 cosine has both its constant
and linear moments zero, giving a bound ||g3''||*h^3/6;
the g4 sine has its constant moment zero, giving
||g4'||*h^2/2. With all norms in this paragraph on K1, (15) yields

    C_eps = 2pi[g1''(alpha)-g2'(alpha)]/k^4 + R_eps,
    |R_eps| <= B_eps/k^5                 (k>=1),          (19)
    B_eps = (2/3)pi^4 ||g1'''|| + (4/3)pi^3 ||g2''||
            +(4/3)pi^3 ||g3''|| + 2pi^2 ||g4'||
            +2pi*b_+*||W||*M4,
    M4 = sup_(a in K1,0<=b<=a) |A_bbbb(a,b)|.

In fact the g3 and g4 bounds are of order k^(-6); k>=1 permits
the common k^(-5) bound. For the nested remainder we used directly

    |integral_J W(a) integral_0^a A_bbbb(a,b)sin(kb)db da|
       <= h*||W||*b_+*M4.

This does not integrate the truncated pointwise O(k^(-3)) formula
as though it had a smaller remainder. All constants are finite:
Phi has every continuous derivative on [0,2b_+]; products, diagonal
derivatives and W preserve this property; the triangle is compact.
Q is smooth by the change b=at to a fixed t interval [0,1] and
differentiation under an integral with bounded derivatives there.

Equations (18)--(19) reproduce the coefficients in the source's
Theorem 4 on substituting k=2x. Its displayed list (49) does not
explicitly include the g3/g4 derivative norms used to justify its
O(x^(-6)) assertions, or the geometric size in the nested remainder.
The valid bound (19) includes them. No uniformity across arbitrary
kernels with only the four listed norms controlled is imported.
For this fixed actual kernel and compact triangle the correction
does not change the conclusion of Theorem 6.

#### Absorption and the aligned grid

Let N2=||Q''||_(infinity,K1) and
B4=B_Q+2pi(||g1''||_(infinity,K1)+||g2'||_(infinity,K1)).
For alpha in K0, (18)--(19) give

    C_tot <= -2pi*delta/k^2
              +2pi^2*N2/k^3+B4/k^4+B_eps/k^5.           (20)

The constants depend on the fixed y and compact intervals, not on
x or m. Choose k large enough that k>=1, h is less than the
distance from K0 to the complement of the interior of K1, and

    2pi^2*N2/k+B4/k^2+B_eps/k^3 <= pi*delta.              (21)

Such a finite threshold exists since delta>0 and all constants
are finite. Then (20) is at most -pi*delta/k^2, which is precisely
(9) because k=2x. An admissible K1 may be fixed as a function of
K0, so the source's notation X(y,K0) is legitimate; no effective
threshold or numerical block certificate has been produced.

Finally let m=ceil(a_-*x/pi). Then a_-<=m*pi/x<a_-+pi/x,
except that equality with a_- may hold, which also suffices.
If pi/x<a_+-a_-, this m is nonnegative and its left endpoint is
in K0. Containment of its entire block in K1 was already enforced
by (21)'s separate distance condition. This proves existence of
a negative aligned block for every sufficiently large x at each
fixed y>0. The compact interval remains fixed as x grows; the
argument never takes m fixed while its left endpoint tends to zero.

The audit establishes the claimed obstruction to nonnegativity of
every block in this specific decomposition. Correlated regrouping,
the complete integral's sign, C233a's unpaid small-y signed estimate
and L030--L032/C032a's all-degree mixed positivity remain unresolved.
No global sum is taken in this proof. This is local verification of
a known theorem, not a result beyond the inspected literature.

## Mathlib

The full endpoint audit and its counterexample have not been checked
in Mathlib; absence is not claimed. L016 records supporting coverage
of the theta transformation at
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq).
That is supporting coverage, not a formalization of this block audit.
The additional negative-block audit1275, including its uniform remainder
and rational curvature bound, has not been checked in Mathlib. The full
matching theorem and supporting uniform-IBP coverage remain unknown;
the displayed analytic proof is not a formal verification.
