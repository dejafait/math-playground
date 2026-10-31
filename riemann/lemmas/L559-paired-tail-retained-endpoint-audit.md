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
interpretation. It does not refute positivity of C_tot, any global
sum, or RH. The example is not asserted to lie in Appendix C's
restricted certified post-crest region. Its regularity bounds do
not supply the missing cancellation, which Appendix C.1 separately
assumes. A differently defined residual or compensating parent term
would need an explicit identity; none is imported here.

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

## Mathlib

The full endpoint audit and its counterexample have not been checked
in Mathlib; absence is not claimed. L016 records supporting coverage
of the theta transformation at
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq).
That is supporting coverage, not a formalization of this block audit.
