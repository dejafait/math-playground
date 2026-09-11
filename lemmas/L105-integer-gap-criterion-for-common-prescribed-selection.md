# Lemma 105: integer-gap criterion for common prescribed selection

**Hypotheses.** Use the prescribed set P and interpolation x_n of Lemma
100. For s∈P let t(s) be the least element of P greater than s, and put
d_s=t(s)−s and K_s=Σ_{j>s}(x_j−x_s)^(−2). Let A⊆P be infinite.
Write q=1−2^(−3/4)>0 and C=64+16sqrt(2)+18q^(−2).

**Conclusion.** The following estimates hold:

- If d_s≤s, then (16/9)sqrt(s)/d_s≤K_s≤C sqrt(s)/d_s.
- If d_s>s, then K_s≤C/sqrt(s).

Consequently K_s is bounded on A if and only if
inf_{s∈A} d_s/sqrt(s)>0. Equivalently, A is a common full-upward
vanishing subsequence for every permitted height sequence if and only
if this integer-gap condition holds. Such an infinite A exists exactly
when

limsup_{s→∞, s∈P} d_s/sqrt(s)>0.                       (1)

The limsup is allowed to be infinite.

## Proof

Fix s∈P and abbreviate t=t(s), d=d_s. Lemma 100 proves that the
coordinates increase, x_s=s^(3/4), x_t=t^(3/4), and

x_j−x_s≥(j^(3/4)−s^(3/4))/3,  j>s.                  (2)

For j>2s, (2) gives x_j−x_s≥q j^(3/4)/3. Hence the universal tail
estimate is

Σ_{j>2s}(x_j−x_s)^(−2)
 ≤9q^(−2)Σ_{j>2s}j^(−3/2)
 ≤18q^(−2)(2s)^(−1/2)
 ≤18q^(−2)s^(−1/2).                                  (3)

Here the series is bounded by the integral over [2s,∞). All series
bounds below can first be applied to finite sums and then passed to
nonnegative increasing limits.

Suppose first that d≤s. For each of the d integers s<j≤t,
monotonicity and the decreasing derivative of v^(3/4) give

0<x_j−x_s≤t^(3/4)−s^(3/4)≤(3/4)s^(−1/4)d.

Summing their inverse squares proves the stated lower bound.

For an upper bound on this first block, recall the real interpolant

g_t(v)=sqrt(v)t^(1/4)(5/4−v/(4t)).

Its derivative in v is positive for s≤v≤t. If d≥2, the first
coordinate after s equals g_t(s+1); every coordinate through t is
therefore at least g_t(s). With r=t/s∈[1,2], write

g_t(s)=s^(3/4)F(r),  F(r)=(5r^(1/4)−r^(−3/4))/4.

We have F(1)=1 and

F'(r)=(5r^(−3/4)+3r^(−7/4))/16≥1/8,  1≤r≤2.

For example r^(−3/4)≥1/2 makes the first term alone at least
5/32>1/8. Thus every gap in the first block is at least
d/(8s^(1/4)). If d=1, the sole gap is instead bounded directly by

(s+1)^(3/4)−s^(3/4)
 ≥(3/4)(s+1)^(−1/4)≥(3/4)(2s)^(−1/4)≥1/(8s^(1/4)).

This handles the case with no interpolated integer. In both cases,

Σ_{s<j≤t}(x_j−x_s)^(−2)≤64sqrt(s)/d.                (4)

For t<j≤2s, (2) and the power derivative imply
x_j−x_s≥(1/4)(2s)^(−1/4)(j−s). It follows that

Σ_{t<j≤2s}(x_j−x_s)^(−2)
 ≤16sqrt(2s)Σ_{r=d+1}^∞r^(−2)
 ≤16sqrt(2s)/d.                                       (5)

The last inequality uses the integral over [d,∞); the sum on the left
is empty when t=2s. Combining (3)–(5), and using
s^(−1/2)≤sqrt(s)/d, proves the first upper bound.

Now suppose d>s, so t>2s. Every integer s<j≤2s lies strictly inside
the same interpolation interval. F'(r)>0 for all r≥1, and the
preceding estimate on [1,2] gives F(2)−1≥1/8. Positivity of the
v derivative of g_t on [s,t] therefore gives

x_j−x_s=g_t(j)−s^(3/4)
 ≥g_t(s)−s^(3/4)≥s^(3/4)/8.

There are exactly s integers in this block, so its inverse-square sum
is at most 64s^(−1/2). Adding (3) proves the second upper bound.

If inf_A d_s/sqrt(s)=a>0, these two upper bounds imply
K_s≤C max(a^(−1),1) on A. Conversely, if K_s≤M on A,
the first lower bound yields sqrt(s)/d_s≤9M/16 whenever d_s≤s.
When d_s>s, sqrt(s)/d_s≤1. Hence
inf_A d_s/sqrt(s)≥1/max(9M/16,1)>0. Lemma 104 identifies
boundedness of K on A with common full-upward vanishing there.

Finally, a positive limsup in (1) gives an a>0 for which infinitely
many prescribed s satisfy d_s/sqrt(s)≥a; these s form a suitable A.
Conversely, any infinite A with a positive lower bound yields a
limsup at least that bound, since an infinite set of positive integers
is unbounded. This proves the existential assertion. ∎

## Qualifications and verification

This criterion concerns only the interpolation of Lemma 100. It uses
integer gaps in P, not the single coordinate gap x_(s+1)−x_s.
It imposes no further restrictions on later prescribed gaps: their
contributions are controlled by (2). It does not resolve arbitrary
coordinate selection or imply RH.

The proof is analytic and requires no numerical certificate. Checks
cover the adjacent prescribed case d=1, the boundary d=s, the common
interpolant for d>s, both parameter derivatives, the two integral
series bounds, and the distinction between a fixed A and existence of
A. Formalization would require successor enumeration in P, these
estimates, the limsup selection equivalence, and Lemma 104's common
selection equivalence.
