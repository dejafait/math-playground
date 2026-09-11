# Lemma 230: finite Fourier reduction with endpoint control

**Hypotheses.** Use L228's interior box, cells, weights and P, and
L227's benchmark B_0. Set D=N^(1/4), H=ceil(N^6), and

S_H(x)=-sum_(k=1)^H sin(2 pi k x)/(pi k).

All sums below range over L228's integer a,c,d and b in D(a,c,d),
and over positive e|a with e<=D. Write w_a=phi(a)/a and define

F_H=sum_(a,c,d,b) w_a sum_(e|a,e<=D) mu(e)
                         [S_H(alpha(b)/e)-S_H(beta(b)/e)],
A_D=(1/2) sum_(a,c,d,b) w_a sum_(e|a,e<=D) mu(e)
          [1_{alpha(b)/e in Z}+1_{beta(b)/e in Z}].

**Conclusion.** For each epsilon>0,

P_{<=D}=F_H-A_D+O_epsilon(N^(1+epsilon)h+N^(-1)h log(2N)), (1)
|A_D|=O_epsilon(N^(1+epsilon)h).                            (2)

Thus P_{<=D}=F_H+o(B_0), and L229 implies P=F_H+o(B_0).
This is a finite approximation, not a bound for F_H. In particular,
C-B_0=o(B_0) is equivalent to F_H=o(B_0); neither is proved here.

**Proof.**

Define the periodic centered sawtooth by psi(x)={x}-1/2 for x not
an integer, and psi(x)=0 at integers. Its endpoint identity is

{x}=psi(x)+1/2-(1/2)1_{x in Z}.

Consequently the exact strict discrepancy in L228 is

r_e=psi(alpha/e)-psi(beta/e)
             -(1/2)[1_{alpha/e in Z}+1_{beta/e in Z}].     (3)

In particular, removing the upper-endpoint atom without changing the
lower-endpoint convention would give an incorrect formula.

We use the elementary Fourier estimates, for integer H>=1,

|S_H(x)|<=C,
|psi(x)-S_H(x)|<=C/(H ||x||)  if x is not an integer.      (4)

Here ||x|| is distance to the nearest integer; both functions vanish
at integers. To verify (4), partial sums of exp(2 pi i k x) have
modulus at most 1/|sin(pi x)|. Summation by parts bounds the tail
sum_(k>H) sin(2 pi k x)/k by C/(H||x||). The full series equals
pi(1/2-{x}) away from integers: for 0<r<1 its Abel sum is the
imaginary part of -log(1-r exp(2 pi i x)), obtained by integrating
the geometric series in r. Letting r increase to 1 gives the stated
value by the argument of 1-exp(2 pi i x). The ordinary series
converges by the same partial-sum bound; its Abel limit equals its
sum by summation by parts (write the Abel mean as (1-r) times the
sum of the partial sums weighted by r^j). These steps involve only
convergent series for r<1 and bounded partial sums for the limit.
Finally set d=||x||>0. For k<=1/d use |sin(2 pi k x)|<=2 pi k d,
so this part of the partial sum is bounded. For k>1/d summation by
parts gives a uniform bound C/((floor(1/d)+1)d). This proves the
first assertion in (4), including x in Z directly.

Put rho=N^(-3). We next bound the number T of endpoint occurrences
(a,c,d,b,e), with e<=D and e|a, for which either

||alpha(b)/e||<rho or ||beta(b)/e||<rho.                   (5)

Count the two endpoint types separately, with multiplicity. Each gives
an integer t divisible by e within e rho of the endpoint. As the
endpoint is in J and equals 2N²+O(h), t belongs to J enlarged by 1
and is positive for large N. Since e<=N^(1/4),

|alpha(b)²-t²| or |beta(b)²-t²| <= C N² e rho < 1/4      (6)

for all sufficiently large N. Constants are uniform over the box.
For the lower endpoint this means that the positive integer q=abcd
lies within 1/4 of t²+R. For fixed a,t there is at most one such
integer q. If a does not divide q there are no triples; otherwise
bcd=q/a=O(N³) has O_eta(N^eta) positive ordered factorizations,
for any eta>0, by the elementary divisor estimate proved in L229.

For the upper endpoint, q=ab(cd+1) is the unique possible integer
within 1/4 of t²-R+1. If a|q, put Q=q/a=O(N³). There are at most
tau_2(Q) choices of b dividing Q. For each choice with cd=Q/b-1
positive, there are tau_2(Q/b-1) choices of c,d. Choices outside
the box can be discarded. In particular the zero-product case has
no admissible c,d. Since both positive integers are O(N³), the
same divisor bound gives O_eta(N^eta) triples in total, after
using eta/2 for each factor. This argument does not require R to
be integral or bounded away from integers.

There are O(Nh) pairs a,t in the specified ranges. For each pair the
number of e|a, e|t, e<=D is at most tau_2(a)=O_eta(N^eta).
Use exponent epsilon/2 for the factorization bound and epsilon/2
for this multiplicity. Equations (5)-(6) therefore give

T=O_epsilon(N^(1+epsilon)h).                             (7)

All exact endpoint atoms are included in (5), proving (2), even
when the Möbius signs are dropped. Notice that controlling these
exceptional cells uses exact integer products, not their real volume.

For the remaining endpoint occurrences, (4) bounds the Fourier
error by C/(H rho)<=C N^(-3). The total number of all occurrences
is bounded by

C N²(h/N) sum_(a in A) tau_2(a) <= C N²h log(2N).         (8)

Indeed L228 gives O(h/N) possible integers b for each a,c,d;
and sum_(a<=6N/5) tau_2(a)=sum_(e<=6N/5) floor((6N/5)/e)
<=C N log(2N). On the exceptional occurrences, the first bound in
(4) and |psi|<=1/2 give error O(1) each. Weights and absolute
Möbius coefficients are at most one. Thus replacing both sawtooths
in (3) by S_H costs at most

C_epsilon N^(1+epsilon)h+C N^(-1)h log(2N),

which proves (1). L227 gives B_0>=c N²h/log N. Choose any fixed
0<epsilon<1 to see that this error and (2) are o(B_0).
L229 supplies the negligible tail above D; L228 supplies the final
comparison with C-B_0. All sums defining F_H are finite.

## Qualifications, verification, and formalization

The high cutoff H is deliberate; no useful cancellation estimate for
this many frequencies is supplied. No equidistribution, independence,
or separation hypothesis for R has been assumed. The paired phases
and all retained Möbius coefficients survive in F_H. Other progression
estimates, the signed comparison, and RH remain unproved.

Analytic verification covers the Fourier tail, the strict half-atom
identity, the two distinct product counts and the aggregate exponents.
`python3 scripts/heat/check_fourier_endpoint_control.py` checks the
endpoint convention and both product-count identities in exact finite
examples, and samples the Fourier tail bound; it is not an asymptotic
proof. Formalization would require the geometric-series Fourier proof,
finite factorization counts, the near-square implication (6), and the
benchmark limit.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
