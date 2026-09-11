# Lemma 207: growing prime band with uniform error

**Hypotheses.** Use the actual box F_N of L202, with fixed t>0,
and the selected set S_D and integer m0 of L205. Fix z>=2, let D
be the product of primes at most z, and fix Y>=z. Let G_(z,Y)(N)
count tuples of S_D with a common prime Y<p<=N^(1/4) of m0 and ab.

**Conclusion.** Uniformly for primes p<=N^(1/4), and for either
factor e=a or e=b,

#{tuple in F_N: p divides m0 and e}/#F_N
 = 1/p² + O_t(N^(-1/24) log(N)/p + N^(-1/2)).           (1)

Consequently

G_(z,Y)(N)/#F_N
 <= 2 sum_(p>Y) p^(-2)
    + O_t(N^(-1/24)(log N)² + N^(-1/4)).               (2)

In particular the iterated limit, first limsup in N and then Y to
infinity, of this relative count is zero. This does not control
primes p>N^(1/4).

**Proof.**

All constants below may depend on fixed t, but not on p, the slice,
or a residue. Work for sufficiently large N. Write P_N for the
number of allowed pairs (a,b), so L202 gives P_N comparable to
N^(3/2) and #F_N=P_N².

First, the proportion of pairs with p dividing either specified
factor is

1/p+O_t(N^(-1/2)),                                    (3)

uniformly for p<=N^(1/4). For b, each interval has its number of
multiples equal to its length divided by p plus O(1); summing over
O(N) values of a proves this. For a, put A=2N²-2tN^(3/2),
B=2N²-tN^(3/2). Its b count is (B-A)/a+O(1).
For the decreasing function 1/y on [11N/10,6N/5], upper and lower
rectangle sums, with mesh p and with mesh 1, give respectively

sum_(a: p divides a) 1/a = (1/p) integral_(11N/10)^(6N/5) dy/y + O(1/N),
sum_a 1/a = integral_(11N/10)^(6N/5) dy/y + O(1/N).

The errors include both incomplete endpoint cells and are uniform:
a mesh-p endpoint rectangle contributes O(p/N) before division by
p. Subtracting and multiplying by B-A= tN^(3/2), then accounting
for at most O(N) rounding errors, proves (3).

Fix a,c,d. On the full b slice use s=1; on the b progression divisible
by p use s=p. Shift r to the first allowed value so the arguments
are b=r+sj, 0<=j<n. L202's interval lengths imply uniformly

n comparable to sqrt(N)/s,

since p<=N^(1/4) makes the unrounded length tend to infinity. Set
f(y)=sqrt(acd(r+sy))/p. Throughout its real interval,

f'''(y)=3 sqrt(acd) s³/[8p(r+sy)^(5/2)],

so its magnitude is comparable to s³/(pN) with fixed ratio of
upper and lower constants. Apply the named third-derivative test
recorded in foundations to kf, for integer k>=1. After division by n,

|n^(-1) sum_j exp(2πikf(j))|
 <= C_t[k^(1/6)s^(1/2)p^(-1/6)N^(-1/6)
          + k^(-1/6)p^(1/6)N^(-1/12)].                (4)

Take H=floor(N^(1/8)). For 1<=k<=H and s in {1,p}, p<=N^(1/4),
the first term is at most N^(-1/16) and the second at most
N^(-1/24). Hence (4) is O_t(N^(-1/24)), uniformly in this whole
range. Negative frequencies are complex conjugates.

Here are uniform interval bounds, including the shrinking target.
For any half-open interval J on the unit circle and 0<epsilon<1/10,
there are continuous piecewise linear functions g_-<=1_J<=g_+
with values in [0,1], integrals within 4epsilon of |J|, and

|g_hat_±(k)| <= C min(1/|k|,1/(epsilon k²)), k!=0.      (5)

To construct them, enlarge or contract J at each end by epsilon
and convolve its indicator with the normalized indicator of
[-epsilon,epsilon]. A contracted empty interval gives g_-=0;
an enlargement covering the circle gives g_+=1. The convolution
has the required pointwise inequalities even at included or excluded
endpoints. The integrals are the lengths of the changed intervals.
The Fourier coefficients of an interval are bounded by 1/(π|k|),
and those of the normalized averaging interval by
min(1,1/(2πε|k|)); their product proves (5), with harmless absolute
constants. These functions are continuous, and their absolutely
convergent Fourier series equal them by the Fejér theorem already
recorded in foundations.

Choose epsilon=N^(-1/16), truncate their series at H, and apply
(4). The zero coefficients differ from |J| by O(epsilon); (5)
bounds the low modes by a harmonic sum and the tail by
O(1/(epsilon H)). Thus, uniformly for every J,

|n^(-1) #{j: frac(f(j)) in J} - |J||
 <= C_t[epsilon + N^(-1/24) log(H+1) + 1/(epsilon H)]
 <= C_t N^(-1/24) log N.                              (6)

No fixed-prime limit has been substituted into a growing sum.
All constants in (4)-(6) are uniform before that sum is taken.

For x=sqrt(abcd), the exact event p divides m0=floor(x)+1 is
frac(x/p) in [(p-1)/p,1). This also holds when x is an integer.
Taking this interval in (6) gives conditional frequency
1/p+O_t(E_N), where E_N=N^(-1/24) log N. For p dividing a, sum
this estimate over the full slices having that property. For p
dividing b, sum it over the residue-zero b progressions of every
slice. In each case (3) says that their total population, divided
by #F_N, is 1/p+O_t(N^(-1/2)). The resulting joint frequency is

(1/p+O_t(E_N))(1/p+O_t(N^(-1/2))),

which proves (1), since E_N is bounded for large N.

If p divides ab it divides a or b. Use S_D contained in F_N and
the union bound, and sum (1) for Y<p<=N^(1/4). The main terms
are bounded by 2 sum_(p>Y) p^(-2). The errors are at most
O_t(E_N log N + N^(1/4)N^(-1/2)), using the harmonic sum over
all integers and the trivial bound on the number of primes. This
proves (2). Finally sum_(p>Y) p^(-2)<=1/floor(Y), so the claimed
iterated limit follows by nonnegativity.

## Remaining scope and verification

Let U_z(N) count tuples of S_D with a common prime p>N^(1/4)
of m0 and ab. The residual count R_(z,Y) of L206 satisfies
R_(z,Y)<=G_(z,Y)+U_z for all sufficiently large N. Therefore
U_z(N)=o(#F_N) would finish the residual-tail task. That estimate
is **unproved**. The lemma neither asserts full coprimality nor
its negation; totient selection and RH remain unresolved.

Verification is analytic: rectangle-sum errors uniform in the mesh,
progression lengths including rounding, the exact third derivative,
the exponents in (4), Fourier bounds independent of interval length,
half-open endpoints, and uniformity before prime summation. No
numerical distribution assumption is used. Formalization requires
these estimates, the named derivative and Fejér theorems, and the
exact rounded-root congruence. The overall argument is unchanged.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
