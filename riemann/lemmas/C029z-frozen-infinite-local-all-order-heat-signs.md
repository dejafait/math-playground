# Corollary C029z: frozen infinite-model local all-order heat signs

## Hypotheses

Use exactly L029's entire function, without parameter changes:

    a=10+i/4,
    P(z)=(1-z^2/25)(1-z^2/a^2)(1-z^2/conj(a)^2),
    F(z)=P(z)cos(z/100).

Choose one representative alpha from each opposite zero pair of F,
with multiplicity. Define

    H_F(t)=sum_alpha exp(-t alpha^2), Re(t)>0,
    beta=alpha^(-2),
    Q(q)=sum_beta beta^2 q(beta)^2, q in R[X].

Both nonreal opposite classes must occur, once each; these are not
one class and not a modulus-square pair. The conclusion concerns the
unchanged interval 0<t<=10^-8. No actual-Xi realization, global heat
complete monotonicity or positive representing measure is assumed.

## Conclusion

H_F is holomorphic on Re(t)>0. For every integer k>=0 its derivative
series converges absolutely locally uniformly there and

    (-1)^k H_F^(k)(t)=sum_alpha alpha^(2k) exp(-t alpha^2).

For every integer k>=0 and every real 0<t<=10^-8,

    (-1)^k H_F^(k)(t)>0.

For k>=1 the absolute contribution of the entire conjugate pair is
less than 1/100 of the single positive contribution from alpha=50*pi.
Nevertheless there exists q in R[X] with Q(q)<0, by L032 with its
hypotheses verified below. All zero multiplicities are retained.

Thus local all-order scalar heat signs alone do not imply all-degree
reciprocal-node mixed positivity for this general entire-function
class. This is local progress on sufficiency of a premise, not a
resolution of actual-Xi mixed positivity or RH. The proof is a
known-method specialization (REPRODUCTION) under assessment2212;
no originality beyond the sources checked is claimed. The independent
step2215 audit below accepts this result in exactly its stated scope.

## Proof

### Exact spectrum and imported analytic theorem

L029 identifies all opposite classes. We may take

    alpha=5, a, conj(a), 100*pi*(n+1/2) (n=0,1,2,...).

Each zero is simple. The three quadratic factors have distinct simple
nonzero roots; the cosine zeros are simple and real, and have absolute
value at least 50*pi>5. Hence they cannot meet the real polynomial
roots, and they cannot meet its nonreal roots. The cosine classes are
mutually distinct. Choosing negative representatives would not change
their squares or the series. Put

    A=1599/16, R=1601/16,
    a^2=A+5i, conj(a)^2=A-5i, |a^2|=R<101,
    lambda_n=10000*pi^2*(n+1/2)^2.

In particular A>0 and all lambda_n>0.

Import the Weierstrass theorem for locally uniformly convergent
holomorphic series and its derivative conclusion: Andrew V.
Sutherland, MIT18.785 Fall2025, *Lecture16*, 13November2025,
Definition16.18 and Theorems16.17/16.19, printed pp11-12:
https://math.mit.edu/classes/18.785/2025/LectureNotes16.pdf#page=11 .
The primary statement and normal-convergence interface were inspected
in review2212, reusing1188. We verify the model-specific hypotheses
next, rather than reprove the general theorem. C030g is a method
comparison for a different spectrum, not an assumed input about F.
The retained-positive-term comparison inspected in Polson/Sokolov,
*Computing the Riemann Hypothesis*, edition2 volumeI, tag v3.0.0,
ch12 label thm:ch12:window, complete statement/proof lines376-392,
is method coverage only:
https://raw.githubusercontent.com/VadimSokolov/computing_rh/v3.0.0/ch/ch12.tex .
Its actual-zero premises are not invoked. The explicit estimates
needed for this fixed function and interval are proved below.

### Normal convergence, every fixed order, and reality

Let K be a nonempty compact subset of Re(t)>0 and choose epsilon>0
such that Re(t)>=epsilon throughout K. For every fixed integer k>=0,

    sup_K |lambda_n^k exp(-lambda_n*t)|
       <=lambda_n^k exp(-epsilon*lambda_n)
       <=(10000*pi^2)^k (n+1)^(2k)
                        exp(-2500*pi^2*epsilon*(n+1)^2).

Both inequalities use that lambda_n is positive real and
(n+1)/2<=n+1/2<=n+1. With c=2500*pi^2*epsilon>0 and m=n+1,
the ratio of consecutive m^(2k) exp(-c*m^2) terms is at most

    2^(2k) exp(-c*(2m+1)).

For m>=max(1,k*log(2)/c) this is at most exp(-c)<1.
Thus the displayed majorant is summable. The three finite head
terms and all their derivatives are entire and bounded on K.
The empty compact set is trivial. These estimates establish normal
convergence on the whole open half-plane for each fixed order k.

The imported theorem, applied successively, now gives holomorphy
and the stated termwise derivative formula. In the chosen enumeration
it reads

    D_k(t):=(-1)^k H_F^(k)(t)
      =25^k exp(-25t)
       +(A+5i)^k exp(-(A+5i)t)
       +(A-5i)^k exp(-(A-5i)t)
       +sum_(n>=0) lambda_n^k exp(-lambda_n*t).          (1)

For real positive t the middle terms are conjugates; the real tail
converges absolutely. Hence D_k(t) is real, with the pair contribution
exactly 2 Re((A+5i)^k exp(-(A+5i)t)). No interchange of a limit in k
with a series has occurred. The estimates allow every fixed k; the
single comparison below is separately valid for all k>=1. We do not
assert convergence or differentiation at t=0.

### Order zero on the full fixed interval

For k=0 the conjugate contribution is

    2 exp(-At) cos(5t).

If 0<t<=10^-8, then 0<5t<=5*10^-8<1<pi/2, using pi>3.
Thus this pair contribution is positive. The real head term and
every real tail term in (1) are also positive. Absolute convergence
therefore gives H_F(t)>0 throughout the interval, including its
right endpoint. No sign is inferred from a sampled time.

### One retained real term pays every higher order

Let k>=1 and 0<t<=10^-8. The complete pair contribution E_k(t)
satisfies, including both derivative factors and its phase,

    |E_k(t)|<=2 |A+5i|^k exp(-At)<=2 R^k<2*101^k.       (2)

This estimate does not discard either nonreal multiplicity.
The elementary inequalities 3<pi<4 give

    22500<lambda_0=2500*pi^2<40000,
    0<lambda_0*t<1/2500.

Since exp(-x)>=1-x for x>=0, the retained positive tail term B_k(t)
has the uniform lower bound

    B_k(t):=lambda_0^k exp(-lambda_0*t)
       >(2499/2500)*22500^k.                           (3)

Combining (2)-(3), and using 0<101/22500<1 and k>=1, gives

    |E_k(t)|/B_k(t)
       <(5000/2499)*(101/22500)^k
       <=(5000/2499)*(101/22500)
        =202/22491<1/100.                             (4)

The last inequality is the integer comparison 20200<22491.
Its required threshold is 1; (4) is a strict bound below 1/100.
All remaining terms in (1) are positive real terms. Dropping those
terms and applying (4) therefore yields

    D_k(t)>=B_k(t)+E_k(t)
           >=B_k(t)-|E_k(t)|>(99/100)*B_k(t)>0.

This proves every integer order k>=1 with the same function and time
interval. In conjunction with the order-zero case it proves the
asserted all-order local signs. No truncation substitutes for the
infinite series: absolute convergence was proved first, and the
omitted real terms have the required positive signs for every k.

### Applicability of the existing mixed-witness theorem

The reciprocal-node multiset is exactly

    1/25, (A+5i)^(-1), (A-5i)^(-1), lambda_n^(-1) (n>=0),

each with multiplicity one. Every node is nonzero. The two nonreal
nodes are conjugates with equal multiplicity, and all other nodes
are positive real, so the entire multiset is conjugation-invariant.
Moreover

    sum_beta |beta|
       =1/25+2/R+sum_(n>=0) lambda_n^(-1)<infinity,

because lambda_n>=2500*pi^2*(n+1)^2 and sum_(m>=1)m^(-2)
converges (for example, by the integral test). The node
w=(A+5i)^(-1) is nonreal since its imaginary part is
-5/(A^2+25), which is nonzero. These are all of L032's hypotheses,
including multiplicities and summability, for this precise multiset.
Its existing polynomial-detection conclusion supplies q in R[X]
with Q(q)<0. A new explicit witness or degree bound is unnecessary.
The polynomial form uses algebraic squares throughout.

### Scope

L247's resolvent-variable signs and C919j's two heat signs are
comparisons, not premises of this proof. This statement concerns all
orders on a bounded interval for the fixed infinite-zero model;
it asserts no all-time complete monotonicity of H_F. The actual-Xi
realization and actual all-degree mixed signs remain independent
unresolved obligations. No joint countermodel to every source
hypothesis, arithmetic realization, or RH conclusion follows.

### Independent proof audit, 21 November 2026 (step2215)

**Verdict.** Accepted under the unchanged audit2213 assessment,
separately approved in2214. No function, interval, estimate or theorem
is strengthened. This is REPRODUCTION: validation of the saved
known-method specialization, not a discovery beyond checked sources.
The full proof and the full L029/L032 statements and proofs were read.
The inspected source notes2212 supply the precise Weierstrass import;
no actual-zeta theorem or global representing measure is imported.

**Spectrum and convergence.** Independently squaring 10+i/4 gives
1599/16+5i, while its squared modulus is 1601/16. Thus the stated
A and R are exact, with A>0 and R<101. The roots of each quadratic
are simple because they are nonzero. Their six roots are distinct,
and the cosine's simple real roots have modulus at least50*pi>5;
none coincides with them. Exactly two nonreal opposite classes occur.
Every class contributes once, and changing a representative's sign
does not change any formula.

For a nonempty complex compact K in the open half-plane, the positive
minimum of Re(t) supplies epsilon. The lower bound
lambda_n>=2500*pi^2*(n+1)^2 controls its exponential, and the upper
bound lambda_n<=(10000*pi^2)*(n+1)^2 controls its kth power, including
k=0. These inequalities may be combined because all factors are
nonnegative. For m>=1 the consecutive-majorant ratio is

    (1+1/m)^(2k) exp(-c*(2m+1))
       <=exp(2k*log(2)-2cm-c)<=exp(-c)<1

when m>=k*log(2)/c. After an integer cutoff this is a geometric
majorant; its finite prefix causes no problem. This proves uniform
absolute convergence on K for every fixed k. Applying the imported
holomorphic-series theorem to successive derivative series gives
(1) on the open domain. No order-uniform convergence is needed:
each k is fixed for this analytic step. Conjugation and absolute
convergence make (1) real at real t>0. Nothing is asserted at t=0.

**Full quantifiers and strict bounds.** For k=0, 0<5t<=5*10^-8<1<pi/2
signs the pair positively at every allowed t, including t=10^-8.
For k>=1, the triangle inequality bounds both complex occurrences
together by 2 R^k exp(-At)<2*101^k. Using 3<pi<4 gives
22500<lambda_0<40000 and lambda_0*t<1/2500. Consequently
exp(-lambda_0*t)>2499/2500, so (3) has the correct strict direction.
The exact reduction of the resulting uniform ratio is

    5000*101/(2499*22500)=202/22491,
    22491-100*202=2291>0.

Since 0<101/22500<1, its kth power is bounded by its first power
for every integer k>=1. This verifies (4) for all orders and times,
not a grid. Every omitted summand is a positive real number and the
series converges, so dropping them preserves the lower inequality.
The factor99/100 is strictly positive, proving the exact threshold
D_k(t)>0. There is no hidden truncation or interchange with k tending
to infinity. The proof requires no mathematical program or numerical
certificate; the displayed exact comparisons suffice.

**Mixed witness.** All reciprocal nodes are nonzero, both nonreal
nodes occur once, and the remaining nodes are real. Their absolute
sum is 1/25+2/R+sum lambda_n^(-1); the last sum is bounded by
(2500*pi^2)^(-1) sum_(m>=1)m^(-2). It is finite. Moreover
Im((A+5i)^(-1))=-5/(A^2+25)!=0. Thus L032 applies to exactly the
stated conjugation-invariant summable multiset. Its interpolation
uses distinct head nodes and counts their multiplicities separately;
its tail estimate is absolute and its final sum is real. No modulus
square replaces the algebraic square. This checks its applicability
without adding a witness, degree bound or new mathematical input.

The audit accepts only the insufficiency of local scalar signs alone.
It supplies neither the joint source hypotheses, actual-Xi realization,
actual-Xi mixed positivity nor RH. The direct mathematical inputs
remain L029 and L032, so the DAG is unchanged. Mathlib remains
unchecked as specified below.

## Mathlib

Full matching coverage is unchecked. Supporting normal-convergence,
termwise differentiation, exponential and cosine bounds, and L032's
interpolation argument have not been matched to Mathlib theorem names
in this step. Unknown coverage is not evidence of absence. The cited
Weierstrass theorem is an informal import, not formal verification.
