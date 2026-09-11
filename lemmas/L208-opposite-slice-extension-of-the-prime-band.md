# Lemma 208: opposite-slice extension of the prime band

**Hypotheses.** Use the box F_N of L202 and the selected set S_D
and integer m0 of L205. Fix t>0 as there, z>=2, D the product of
primes at most z, and 0<eta<1/4. Put Q=N^(1/2-eta).

**Conclusion.** For either e=a or e=b, uniformly for primes p<=Q,

#{tuple in F_N: p divides e and m0}/#F_N
 = 1/p² + O_(t,eta)(N^(-eta/6) log(N)/p + N^(-1/2)).     (1)

In particular the count B_(z,eta)(N) of tuples in S_D with a common
prime N^(1/4)<p<=Q of m0 and ab satisfies

B_(z,eta)(N)/#F_N
 = O_(t,eta)(N^(-1/4)+N^(-eta/6)(log N)²+N^(-eta))
 = o(1).                                               (2)

Consequently, if V_(z,eta)(N) counts tuples in S_D with a common
prime p>Q of m0 and ab, the remaining count U_z of L207 obeys

V_(z,eta) <= U_z <= V_(z,eta)+B_(z,eta).                 (3)

Thus for any one fixed eta in this range, U_z=o(#F_N) is equivalent
to V_(z,eta)=o(#F_N). Neither of these tail assertions is proved here.

**Proof.**

All constants are uniform in the tuples and p; N is sufficiently
large with t and eta fixed. Write P_N for the number of pairs (a,b)
in L202. For either specified factor e, the number A_e(p) of such
pairs with p dividing e satisfies

A_e(p)/P_N=1/p+O_t(N^(-1/2)).                            (4)

Here is the rounding justification for the extended range. For e=b,
counting multiples in each b interval gives its real length divided
by p with O(1) error. Comparing with 1/p times the unrestricted
integer count and summing over O(N) choices of a gives error O(N).
For e=a, put A=2N²-2tN^(3/2), B=2N²-tN^(3/2).
The b count at a is (B-A)/a+O(1). Rectangle sums for 1/y on
[11N/10,6N/5], using mesh p, give

sum_(a: p divides a) 1/a
 = (1/p) integral_(11N/10)^(6N/5) dy/y + O(1/N).

Indeed interior rectangle errors telescope for a decreasing function;
the two incomplete end cells cost O(p/N) before division by p.
This holds uniformly for p<=Q=o(N), so the interval is longer than
a mesh cell for all sufficiently large N. Comparing with the mesh-one
sum and adding the integer b-count errors gives O_t(N) total error.
Since P_N is comparable to N^(3/2) by L202, both cases give (4).

Now fix an allowed pair (a,b) with p dividing e, and an allowed c.
Write the consecutive d values as d0+j, 0<=j<n. Their count is
comparable to sqrt(N), uniformly in c, by L202. Crucially there is
no divisibility restriction on d. Set

f(y)=sqrt(abc(d0+y))/p.

Since all four factors are comparable to N,

f'''(y)=3 sqrt(abc)/(8p(d0+y)^(5/2))

has magnitude comparable to 1/(pN), with fixed upper-to-lower ratio.
The named third-derivative test recorded in foundations, in the same
normalization as L207, gives for each integer k>=1

|n^(-1) sum_(j=0)^(n-1) exp(2πikf(j))|
 <= C_t[k^(1/6)p^(-1/6)N^(-1/6)
        +k^(-1/6)p^(1/6)N^(-1/12)].                    (5)

Take H=floor(N^(eta/2)). For 1<=k<=H and p<=Q the first
term is at most N^(-1/6+eta/12), and the second at most
N^(-eta/6). The first is also at most N^(-eta/6), since
eta<1/4<2/3. Thus (5) is O_t(N^(-eta/6)) uniformly.

Apply the interval majorant/minorant construction proved in L207
with smoothing width epsilon=N^(-eta/4). Its Fourier coefficients
are bounded by C min(1/|k|,1/(epsilon k²)); its means differ from
the interval length by O(epsilon), for every half-open circle interval
J. Using (5) up to H, and absolute convergence for the rest, gives

|n^(-1) #{j: frac(f(j)) in J}-|J||
 <= C_t[epsilon+N^(-eta/6) log(H+1)+1/(epsilon H)]
 <= C_(t,eta) N^(-eta/6) log N.                         (6)

The construction applies to intervals shorter than epsilon as well,
and includes their endpoint conventions. Thus it is valid for
J=[(p-1)/p,1). The exact condition m0=floor(sqrt(abcd))+1 being
divisible by p is frac(f(j)) in J, including integer square roots.
Consequently each full d slice has conditional frequency
1/p+O_(t,eta)(E_N), with E_N=N^(-eta/6) log N.

Summing these estimates over all c and all first pairs counted by
A_e(p), and using #F_N=P_N², gives joint frequency

(A_e(p)/P_N)(1/p+O_(t,eta)(E_N)).

Insert (4); since E_N is bounded and p>=2 this proves (1).
No phase distribution or independence involving S_D is needed:
S_D is only a subset of F_N for the following upper bound.

Use the union bound over e=a,b and N^(1/4)<p<=Q. The main
terms sum to O(N^(-1/4)), by comparison with the sum of n^(-2)
over all integers n>N^(1/4). The discrepancy terms sum to
O_(t,eta)(E_N log N), using the harmonic sum over integers up to Q.
There are at most Q primes in the range, so the rounding terms total
O(Q N^(-1/2))=O(N^(-eta)). This proves (2).
Every tuple counted by U_z has a common prime in this band or above
Q; conversely every tuple counted by V_(z,eta) is counted by U_z.
Overlap between the two events does not affect the inequalities (3).
Divide by #F_N and apply (2) to obtain the stated equivalence.

## Scope, obstruction to this estimate, and verification

This resolves only a scoped portion of the large-prime task. For
example eta=1/12 leaves just p>N^(5/12). The present derivative
bound does not itself reach p comparable to sqrt(N): its second term
at k=1 is p^(1/6)N^(-1/12), which ceases to tend to zero there.
This is a limitation of the bound, not a lower bound on the actual
exponential sum or a counterexample to the desired tail estimate.
One cannot set eta=0 or choose eta depending on N in the fixed-eta
little-o conclusion. Full coprimality, totient selection, and RH
remain unproved.

Verification is analytic: uniform rectangle errors, unrestricted slice
length, the exact third derivative, the two powers in (5), uniform
shrinking-interval approximation, and summation of all three error
terms. Direct mathematical inputs are L202 for the box and counts,
L205 for the selected-set definition, and L207 for its proved Fourier
interval construction. Formalization requires those estimates, the
named third-derivative test, and the finite union bound. No numerical
distribution assumption or new standard theorem is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
