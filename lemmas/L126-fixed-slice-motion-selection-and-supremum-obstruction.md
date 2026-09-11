# Lemma 126: fixed-slice motion selection and supremum obstruction

**Hypotheses.** Fix a real parameter λ₀ in the theta deformation of
Lemma 58. Suppose its zeros have finite positive imaginary supremum H,
and every nonreal zero in this slice is simple. Let v(w) denote the
instantaneous imaginary velocity of the local zero branch through w.

**Conclusion.** If H is not attained, there are upper zeros
w_n=a_n+ib_n with |a_n|→∞, b_n→H, E(w_n)→0, and

limsup_n v(w_n)≤−1/H,

where E is the exact upward sum of Lemma 67. If H is attained, every
zero w=a+iH at that height satisfies

v(w)≤−1/H−H/(a²+H²).

These are conditional fixed-slice conclusions. Even bounds on every
branch derivative at one parameter do not in general bound the upper
right Dini derivative of their height supremum, as the analytic example
below proves.

## Proof of the fixed-slice conclusion

For real b, the integral of Lemma 58 gives

F(λ₀,ib)=∫₀^∞ exp(λ₀u²)K(u)cosh(bu)du>0.

Convergence follows from that lemma's domination; its positive kernel
makes the inequality strict. Thus no zero is on the imaginary axis,
and every upper zero has nonzero real part. Conjugation gives the
matching lower zeros. Lemma 63 supplies reciprocal-square summability
over the full zero multiset, hence also

Σ_(Im ρ>0) (1+|ρ|²)^(-1)<∞.

Apply Lemma 125 to precisely this upper multiset. Every destination
above an upper zero is in that multiset, so its upward sum equals E
in Lemma 67, including all destination multiplicities and both signs
of the real part. No factor of two or reflected destination is missing.

If H is not attained, Lemma 125 selects w_n escaping every bounded
disk with b_n→H and E(w_n)→0. Since b_n is bounded, |a_n|→∞.
Simplicity is supplied by our hypothesis, not by the selection theorem.
The exact-sum version of Lemma 67 gives

v(w_n)≤−1/b_n−b_n/|w_n|²+E(w_n)≤−1/b_n+E(w_n).

Taking the limsup proves the conclusion. At an attained maximum,
E(w)=0 and the same estimate proves the stated bound. ∎

## Which selection condition has been discharged

This application establishes the weaker exact-sum sufficient condition
in Lemma 67. It does not establish (H−b_n)S(w_n)→0. The inequality
E(w_n)≤2(H−b_n)S(w_n) points in the wrong direction for that inference.
Nor does it prove finite strip height or simplicity for every theta
slice. If multiple nonreal zeros occur, Lemma 125 still selects points,
but need not select simple ones, and v at those points is not defined
by the simple-zero formula.

## A precise obstruction to differentiating a supremum

For integers n≥2 define entire functions of t by

b_n(t)=1−1/n−t+4t(1−exp(−n²t²)).

On the common real interval |t|<1/20 they are positive and uniformly
bounded: |b_n(t)−(1−1/n)|≤3|t|, since
−t+4t(1−exp(−n²t²))=t(3−4exp(−n²t²)).
Every b_n(0)=1−1/n and b_n'(0)=−1. Nonetheless, for t>0,

b_n(t)=1+3t−1/n−4t exp(−n²t²)<1+3t,
lim_(n→∞) b_n(t)=1+3t.

Thus M(t)=sup_(n≥2)b_n(t) has M(0)=1 and M(t)=1+3t for t>0.
Its upper right Dini derivative at zero is exactly 3, although every
branch derivative there is −1=−1/M(0). This holds even though all
branches are analytic on a common interval and their supremum is
finite and right-continuous at zero. The first-order remainders are
not uniform in n:

[b_n(t)−b_n(0)+t]/t=4(1−exp(−n²t²))

has supremum 4 for every t>0, while tending to zero for each fixed n.

If desired, place these heights at horizontal coordinates n and include
all points ±n±ib_n(t). For real t in this interval they form distinct
quartets with uniformly bounded heights and a uniformly summable
reciprocal-square majorant 4Σ_(n≥2)n^(-2). This is an abstract moving
configuration, not an asserted theta zero set or a solution of the
heat equation. It disproves the passage from pointwise branch
velocities and these geometric bounds alone to a supremum derivative.

## Remaining heat-flow obligation

Write H(λ) for the supremum of all zero heights, where finite. An upper
right Dini bound at λ₀ would require controlling

limsup_(h↓0) [H(λ₀+h)−H(λ₀)]/h.

Our conclusion instead selects favorable zeros at λ₀. An upper bound
for a supremum must control all contenders, including those whose
indices depend on h. Even favorable selection at each nearby slice
would not alone change this quantifier mismatch.

For example, a sufficient additional statement would cover every upper
zero at λ₀+h by a branch starting at λ₀ and prove, uniformly over all
such branches,

Im z(h)≤Im z(0)−h/H(λ₀)+h r(h),   r(h)→0.

Taking the supremum would give the Dini bound immediately. This is an
unproved sufficient condition, not a claimed necessary one. No such
coverage or uniform remainder follows from compact implicit-function
neighborhoods for zeros escaping to infinity. Multiple-zero splitting
requires separate treatment, and finite strip height on a parameter
interval also remains a hypothesis here. These missing assertions are
not established premises of this lemma or of an RH proof.

## Verification and formalization obligations

The proof is analytic; no numerical certificate is required. Checks
are imaginary-axis positivity, summability of the exact destination
multiset, the direction of the E versus S estimate, simplicity at each
selected point, attained versus nonattained supremum, and the explicit
exponential limit above. Formalization would require the selection
application, the sequential velocity inequality, and the elementary
analytic-family supremum and Dini-derivative computation. RH remains
unproved.
