# Corollary C030g: complex-time heat-series convergence audit

## Hypotheses

Use the actual nontrivial zeta zeros rho, counted with their finite
multiplicities m(rho), including any off the critical line. L018 gives
0<Re(rho)<1 and multiplicity-preserving reflection and conjugation.
L026 excludes zero ordinate (indeed |Im(rho)|>4). For each distinct
zero put a(rho)=-(rho-1/2)^2. The time domain is U={t:Re(t)>0}.

Import the multiplicity-weighted Riemann-von Mangoldt estimate
N(T)=O(T log T), where N(T) counts 0<Im(rho)<=T. A precise stronger
source is Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong,
*Counting zeros of the Riemann zeta function*, J. Number Theory235
(2022),219-241, [arXiv:2107.06506v1, 14July2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), p2: for T>=e,

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
      <=0.1038*log(T)+0.2573*log(log(T))+9.3675.

Section2/(2.1)-(2.3), p3, identifies the symmetric count with the
argument-principle count of the entire completion; multiplicities
are included. Only its coarse upper bound is needed. Neither its
explicit-constant proof nor its computations are reproduced here.

## Conclusion

For every compact K contained in U and every fixed integer j>=0,

    sum_(Im(rho)>0) m(rho) sup_(t in K)
       |a(rho)^j exp(-a(rho)*t)| < infinity.                 (1)

Consequently

    W(t)=sum_(Im(rho)>0) m(rho) exp(-a(rho)*t)
        =(1/2)sum_rho m(rho) exp(-a(rho)*t)                 (2)

is holomorphic on U, and for every fixed j>=0,

    W^(j)(t)=sum_(Im(rho)>0) m(rho)(-a(rho))^j
                     exp(-a(rho)*t).                      (3)

Every series in (2)-(3) converges absolutely locally uniformly there,
and W(conj(t))=conj(W(t)). In particular W and its derivatives are
real on positive real time. Equation(2) also equals the sum with
multiplicity over one representative of each reflection pair.

This passes precisely the convergence/differentiation part of
Nicholas G. Polson, *On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, 11September2026](https://arxiv.org/pdf/1708.02653v24#page=9),
Definition5.1/(4), p8, and Lemma5.2, p9. It is REPRODUCTION for
reliability under pre-existing assessment1188, not a result beyond
that source. No endpoint asymptotic, first-zero/large-time assertion,
positivity, uniform-in-j bound, or bound as Re(t) tends to zero is
claimed. C030a already covers the real-time overlap.

## Proof

### The complex compact estimate

For a nonempty compact K contained in U choose epsilon>0, B>=epsilon
and M>=0 with epsilon<=Re(t)<=B and |Im(t)|<=M throughout K.
Write rho=1/2+d+iy with real |d|<1/2. Direct expansion gives

    a=y^2-d^2-2idy,
    Re(a)>=y^2-1/4, |Im(a)|<=|y|, |a|=y^2+d^2<=y^2+1/4.

For t=x+iv in K one has exactly
Re(a*t)=x*y^2-x*d^2+2*d*y*v. Since x>0,

    Re(a*t)>=epsilon*y^2-B/4-M*|y|.

Thus for every fixed j>=0,

    sup_K |a^j exp(-a*t)|
       <=(y^2+1/4)^j exp(-epsilon*y^2+M*|y|+B/4).          (4)

This checks the source's imaginary-time term and the direction of
both real-part inequalities. It does not require Re(a)>0 for a
finite low zero, and does not assume d=0. An empty K is trivial.

### Shell summation, including multiplicity and finite exceptions

The cited count implies there is C>0 with
N(T)<=C*T*log(T+2) for T>=e. The finite low-height part causes no
problem: zeros are isolated, of finite multiplicity, and lie in a
bounded rectangle; L018's completion is entire and not identically
zero since xi(0)=1/2. A compact rectangle therefore has only finitely
many zeros. Each contributes a bounded entire summand on K. L026
actually rules out all |y|<=4 here, but this stronger bound is not
needed for summability.

For an integer n>=1 put the positive ordinates in the disjoint shell
n<=y<n+1. Its total multiplicity is at most N(n+2), hence, when
n+2>=e, at most C*(n+2)*log(n+4). Using the larger counting height
avoids any convention at a shell endpoint. Formula(4) bounds its
contribution by

    C*(n+2)*log(n+4)*((n+1)^2+1/4)^j
      *exp(-epsilon*n^2+M*(n+1)+B/4).                      (5)

For n>=max(1,4*M/epsilon), M*(n+1)<=2*M*n<=epsilon*n^2/2.
Also (n+1)^2+1/4<=(17/4)*n^2 and
(n+2)*log(n+4)<=15*n^2 for n>=1, using log(n+4)<=n+4.
Thus (5) is at most

    15*C*exp(B/4)*(17/4)^j
       *n^(2j+2)*exp(-epsilon*n^2/2).                      (6)

The series of these bounds converges. Explicitly, for p=2j+2 the
ratio of consecutive n^p exp(-epsilon*n^2/2) is
(1+1/n)^p exp(-epsilon*(2n+1)/2)
<=2^p exp(-epsilon*n-epsilon/2). For integers
n>=max(1,p*log(2)/epsilon) this is at most exp(-epsilon/2)<1.
The geometric comparison and the finitely many omitted shells prove
(1), with all multiplicities retained. Every fixed j is allowed;
the constants and onset may depend on j and K.

### Holomorphy, differentiation and pairing

The countable zero family may be enumerated, with multiplicities as
weights or repeated occurrences. Each summand is entire in t.
Equation(1) gives normal convergence on every compact subset of U;
a closed disk inside U supplies a neighborhood of each point.
The Weierstrass theorem for normally convergent holomorphic series
therefore gives holomorphy and termwise differentiation. Precisely,
use Andrew V. Sutherland, MIT18.785 Fall2025,
[Lecture16, 13November2025](https://math.mit.edu/classes/18.785/2025/LectureNotes16.pdf#page=11),
Definition16.18 and Theorems16.17/16.19, pp11-12. Apply the derivative
conclusion successively to the normally convergent series of entire
summands (-a)^j exp(-a*t). Induction proves(3); (1) already gives
normal convergence for every resulting derivative series. No limit
in j or time-to-zero is exchanged with the zero sum.

Reflection rho -> 1-rho preserves a and multiplicity by L018.
By L026 there is no zero ordinate, so every reflection pair has
exactly one positive-ordinate member and one negative-ordinate member.
In particular there is no fixed zero at rho=1/2. Absolute convergence
permits regrouping, proving the factor1/2 and independence of the
chosen reflection representative in(2). For the full zero sum the
same convergence follows by doubling the positive-ordinate sum.
This is exactly the squared-Xi-node convention already used in C030a.

To check reality within the upper half-spectrum, the involution is
rho -> 1-conj(rho), not rho -> conj(rho). It keeps y>0, preserves
multiplicity and sends a to conj(a). Thus absolute convergence gives

    conj(W(t))=sum_(Im(rho)>0) m(rho) exp(-conj(a(rho))*conj(t))
              =W(conj(t)).

The same reindexing works with the factors (-a)^j in(3).
An off-line quartet contributes two conjugate squared nodes; a
critical-line reflection pair contributes one real squared node,
with its actual multiplicity. No modulus square or positive spectral
measure has replaced an algebraic expression. All assertions hold
without RH or finite numerical zero verification.

### Effect and limits of the audit

No bound or interchange in the selected convergence paragraph fails.
C030e may use (2)-(3) locally instead of retaining this part of
Lemma5.2 as an unaudited source-proof input. Its explicit formula
remains an import. The source's other Lemma5.2 assertions and its
far-time sign argument are outside this audit. Convergence proves
none of L030-L032/C032a's missing all-degree signs, actual-theta
signing or graph realization. Stops1117/1181 remain in force for
their stated mechanisms.

## Mathlib

Full matching coverage for this heat-series statement, its zeta count
and its exact half-spectrum convention is unchecked, not asserted
absent. The named Weierstrass/normal-convergence and counting theorems
are precise informal imports, not formal verification. No Mathlib
lookup is needed for the present analytic applicability audit.
