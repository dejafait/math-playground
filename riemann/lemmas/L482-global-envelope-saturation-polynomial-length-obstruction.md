# Lemma 482: global-envelope saturation conflicts with the formal short-product budget

## Hypotheses

Fix a real number A>=0. Let T tend to infinity through arbitrary real
values, or along any unbounded sequence. Set

    L=log T, a=L^A,
    N=floor(T^(1/24)), M=floor(sqrt(T/(2pi))),
    S_N=sum_(1<=n<=N)n^(-1/2), B_T=S_N^6,
    F_T(t)=sum_(1<=n<=N)n^(-1/2-it).

For sufficiently large T, let p_T be a real polynomial of degree at
most the nonnegative integer d_T. Coefficients and d_T may depend
arbitrarily on T. Assume

    sup_(0<=x<=B_T)|p_T(x)-x/(a+x)|<=1/8.                 (1)

Define the stipulated formal length budget

    J_T=M N^(3d_T).                                     (2)

For the implementation interpretation only, use the exact nonchirped
component U of L481 and its imported finite mean-square interface.
No RH, zeta zero-free estimate, phase independence, coefficient
positivity or conjectural moment is assumed.

## Conclusion

Whenever B_T>=a, condition (1) implies

    d_T^2 >= B_T/(9a) >= N^3/(9 L^A).                   (3)

Consequently d_T tends to infinity for every fixed A. In contrast,
the budget

    J_T log(2J_T)=o(T)                                  (4)

requires d_T<=3 eventually along the sequence under consideration.
Thus (1) and (4) cannot coexist along any unbounded sequence for
any fixed A>=0. The actual lower bound in (3) grows at least as
(1/3+o(1)) T^(1/16)L^(-A/2) for d_T; the required budget permits
only d_T<=3. Degrees at most three do satisfy (4), considered without
the approximation condition.

This is a routine specialization of classical Markov's inequality
and a comparison with a specified implementation budget. B_T is a
triangle-inequality envelope, not an assertion that |F_T(t)|^6 visits
all of [0,B_T] on [T,2T]. The conclusion stops only global uniform
polynomial approximation with (2)--(4). It gives no obstruction to
approximation in an actual-height weighted norm, rational or other
nonpolynomial tests, different length estimates, or the bounded
saturation correlation itself. No L477 defect threshold, negative-mass
saving, individual sign or all-degree positivity follows.

## Proof

### Imported inequality and its applicability

Import the classical Markov inequality in the following precise form:
if q is a real polynomial of degree at most d on [-1,1],

    ||q'||_infinity <= d^2 ||q||_infinity.

See A. Shadrin, *Twelve Proofs of the Markov Inequality*, author-hosted
undated draft, Section 1.1, equation (1.1), PDF pp. 1--2
([primary statement](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf#page=1)).
The invocation-start literature assessment records inspection of this
statement. It includes endpoints, arbitrary real coefficients and
every integer degree, with no positivity requirement. No reproof of
Markov or of the stronger best-reciprocal-approximation theorem is
needed. All subsequent steps are elementary interval scaling,
the mean-value theorem, finite algebra and limits.

### 1. Degree forced by the transition near zero

For B=B_T>0, apply Markov to q(u)=p_T(B(u+1)/2). The chain rule
and equality of the corresponding suprema give

    ||p_T'||_[0,B] <= (2d_T^2/B)||p_T||_[0,B].            (5)

Since 0<=x/(a+x)<=1 and (1) holds, ||p_T||_[0,B]<=9/8.
Once B>=a, both 0 and a belong to the approximation interval.
Its two prescribed function values are 0 and 1/2, respectively.
Thus

    p_T(a)-p_T(0) >= (1/2-1/8)-1/8=1/4.

The mean-value theorem on [0,a] gives a point with
p_T'>=1/(4a). Combining this with (5) yields

    1/(4a) <= 9d_T^2/(4B),

which is (3)'s first inequality. This also excludes degree zero,
without assuming a nonzero leading coefficient in advance.

For each n<=N, n^(-1/2)>=N^(-1/2), so S_N>=sqrt N and
B_T>=N^3. Moreover N/T^(1/24) tends to 1 as T tends to infinity.
For any fixed A>=0,

    B_T/a >= N^3/L^A
             =(1+o(1))T^(1/8)/L^A -> infinity.            (6)

In particular B_T>=a eventually, as required above, and (3) forces
d_T>=N^(3/2)/(3L^(A/2)) to tend to infinity. These limits hold
for all sufficiently large real T, hence on every unbounded sequence.

### 2. Degree permitted by the formal length

The floors satisfy

    M/T^(1/2) -> 1/sqrt(2pi),
    N^12/T^(1/2) -> 1,
    M N^12/T -> 1/sqrt(2pi).                             (7)

If d_T>=4 at any sufficiently large T, then J_T>=M N^12.
The function y log(2y) is increasing for y>=1. Therefore on any
unbounded subsequence of such T,

    J_T log(2J_T)/T
       >= (M N^12/T) log(2M N^12) -> infinity,            (8)

by (7). This contradicts (4), which must hold on all subsequences
of the proposed sequence. Hence (4) implies d_T<=3 eventually.
Conversely, if 0<=d_T<=3, then

    1<=J_T<=M N^9<=T^(7/8)/sqrt(2pi)

for all sufficiently large T. It follows that
J_T log(2J_T)/T=O(T^(-1/8)log T)->0, uniformly over these four
integer degrees. This proves the budget threshold claimed.

Since (3) eventually forces d_T>3, the two requirements are
incompatible. No numerical test, limiting interchange or assertion
about the actual range of F_T has been used.

### 3. Envelope and relation to the finite-polynomial interface

The finite triangle inequality gives |F_T(t)|<=S_N for every real
t, hence |F_T(t)|^6<=B_T. Uniform approximation on [0,B_T]
therefore controls substitution at every actual t. Its failure on
that larger interval does not imply failure on the range actually
visited, or in any integral norm.

To explain exactly the formal length tested, write

    D_j(t)=sum_(n<=M)(log n)^j n^(-1/2-it), j=0,1,2,

where the zeroth power is 1 including n=1. The expansion of
log(n/m)^2 in L481 gives

    U=2 Re(D_2 conjugate(D_0))-2|D_1|^2.

For a nonnegative integer k, F_T^(3k) is a finite Dirichlet
polynomial supported on integers at most N^(3k), with F_T^0=1.
After grouping every equal integer product, each

    A_(j,k)=D_j F_T^(3k)

is supported on integers at most M N^(3k), and exactly

    U |F_T|^(6k)
      =2 Re(A_(2,k) conjugate(A_(0,k)))-2|A_(1,k)|^2.     (9)

For p_T(x)=sum_(k=0)^(d_T) alpha_(k,T)x^k, (9) represents
the nonchirped polynomial substitution by a finite sum of bilinear
terms of lengths at most J_T. This is the same grouping used for
k=1 in L481's Section 2. L481 (3)--(4) imports the arbitrary-finite-
coefficient mean-square estimate from Heap--Soundararajan,
*Lower bounds for moments of zeta and L-functions revisited*,
arXiv:2007.13154v1, Section 5, p. 9, equation (14)
([primary version](https://arxiv.org/pdf/2007.13154v1#page=9)).
Its bilinear error is bounded by an absolute constant times

    J_T log(2J_T) ||u||_2 ||v||_2.

Condition (4) makes this factor o(T) relative to the natural
T||u||_2||v||_2 scale. It does not bound the coefficient norms,
the sum weighted by |alpha_(k,T)|, or their ratio to a signed
diagonal. The complete residual also contains L481's chirped
component Re(exp(2i theta)V); it needs its own estimates and is
not an ordinary mean-square term. Thus J_T is the stated formal
budget for this grouping, not a universal necessary length for
all methods and not a sufficient error theorem for the complete
signed substitution. The obstruction in Sections 1--2 concerns
precisely the simultaneous conditions (1) and (4).

## Mathlib

Full matching coverage of this approximation/length incompatibility
has not been checked. No claim of absence is made. Classical Markov's
inequality and the finite mean-square theorem are retained by their
precise primary citations above, not claimed as checked Mathlib
theorems. No formal verification or mathematical script was used.
