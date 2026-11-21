# Corollary C029e: monomial fractional-moment baseline cost

## Hypotheses

Let d>=3 be an integer, A>0 a fixed real number, L=Ad, and
nu_(A,d) the uniform probability measure on [-L,L], with density 1/(2L).
Set T_d(y)=y^d. For 0<q<=1 define

    E_(d,A)(q)=(2Ad^2/q) log(integral |T_d(y)|^(q/d) dnu_(A,d)(y))
                 -integral_(-Ad)^(Ad) d log|y| dy.

Logarithms at zero may be assigned any finite value on that null set.
The second integral is an ordinary Lebesgue integral, equivalently the
convergent improper integral across zero. For the sequence conclusion,
q=q_d in (0,1] may depend on the integer d; A is held fixed first.

The approved notebook scope takes A>=max(1,2sqrt(M)), with the fixed M
defined in C028e. The scalar calculation below works for every A>0;
it uses no property of M and no actual theta-polynomial premise.

## Conclusion

For every stated d,A,q,

    E_(d,A)(q)=2Ad^2 [1-log(1+q)/q] >=0,                    (1)
    Adq/(1+q) <= E_(d,A)(q)/d <= Adq.                     (2)

Consequently, for each fixed A>0,

    E_(d,A)(q_d)/d -> 0  if and only if  d q_d -> 0.        (3)

The same condition is equivalent to vanishing for every fixed allowed
A, before taking the outer large-A limit. For fixed q>0 the normalized
cost instead grows linearly in d. If d q_d -> c with 0<=c<infinity,
then E_(d,A)(q_d)/d -> Ac. In particular q_d asymptotic to c/d with
c>0 does not escape the cost; q_d=o(1/d) does.

These are exact reference-cost statements. They neither lower-bound
the actual H_d nor upper-bound the actual Q_d partition function in
C028d. Fixed positive q is excluded only as a rule giving o(d) excess
for this numerator-only comparison on the reference itself. Shrinking
q remains possible, subject to an unpaid actual-family estimate.

## Proof

### Imported inequality and why this specialization is recorded

Use standard Jensen's inequality for the concave logarithm: if X>0
almost surely, E X<infinity and E|log X|<infinity, then
E log X<=log E X. The inspected source is Marco Taboga,
*Jensen's inequality* (2021),
[Statement and Example](https://www.statlect.com/fundamentals-of-probability/Jensen-inequality).
Assessment1959, separately approved in review1960, covers this input
and the elementary power/log integrations below. No quantitative
entropy theorem, strong concavity, real-root hypothesis or
Carbery-Wright inequality is used. The finite calculation is recorded
to check all degree factors and the precise sequence threshold; it is
reproduction/specialization of standard inequalities, not a novelty claim.

### Probability normalization, singularity and inequality direction

The interval has length 2L, so nu_(A,d) is a probability measure.
For y!=0 set X(y)=|T_d(y)|^(q/d)=|y|^q. At y=0 set X(0)=1,
which changes no integral. Thus X>0 almost surely and is integrable
on the bounded interval. Moreover log X=q log|y| almost everywhere.
The function |log y| is integrable near zero: its integral on (0,1)
is 1, by the primitive y log y-y and the limit y log y->0.
Away from zero it is continuous on every compact interval.
Hence log X is absolutely integrable and every hypothesis of Jensen
is met. It gives

    integral_(-L)^L log|T_d(y)| dy
       =(2Ld/q) integral log X dnu_(A,d)
       <=(2Ld/q) log(integral X dnu_(A,d)).                (4)

Here 2Ld/q=2Ad^2/q. The left side equals the reference integral
subtracted in E, so (4) verifies the upper-comparison direction and
nonnegativity. No positivity of T_d itself is required, including odd d.

### Exact scalar integrations

By evenness and q>0,

    integral X dnu_(A,d)=(1/L) integral_0^L y^q dy
                       =L^q/(1+q)>0.                    (5)

The ordinary primitive and its zero limit similarly give

    integral_(-L)^L d log|y| dy=2dL(log L-1).             (6)

Substitution of (5)-(6) into the definition yields

    E_(d,A)(q)
       =(2Ad^2/q)[q log(Ad)-log(1+q)]
          -2Ad^2[log(Ad)-1]
       =2Ad^2[1-log(1+q)/q].

Both integrals are finite before subtraction; no divergent terms are
cancelled, no principal value is taken, and no degree limit is exchanged
with an integral.

### Bounds and the sequence discriminator

The fundamental theorem of calculus gives the positive identity

    1-log(1+q)/q=(1/q) integral_0^q t/(1+t) dt.           (7)

Since t/(1+q)<=t/(1+t)<=t for 0<=t<=q,

    q/[2(1+q)] <= 1-log(1+q)/q <= q/2.                 (8)

Multiplying by 2Ad proves (2). Because q<=1, these bounds also imply

    (A/2)dq <= E_(d,A)(q)/d <= Adq.

For fixed A>0 this proves both directions of (3), with no assumption
that q_d converges. If the normalized cost vanishes for one fixed
allowed A, then d q_d->0, which in turn gives vanishing for every fixed
allowed A. Each resulting inner limit is zero, so its outer A limit is
zero. No assertion of convergence uniform in A or interchange of these
limits is needed.

For fixed q>0 the bracket in (1) is strictly positive by (7), so
E/d=2A[1-log(1+q)/q]d diverges linearly. If d q_d->c<infinity,
then q_d->0. Bounds (8) show

    [1-log(1+q_d)/q_d]/q_d -> 1/2,

and substitution in (1) gives E/d->Ac. In particular the threshold
q=o(1/d) is necessary as well as sufficient for this reference test.

The calculation does not compare the actual Q_d moment with (5).
Such a degree-uniform upper estimate, together with the ordered-cutoff
central payment, remains missing. C028d's logarithmic L1 identity alone
does not supply it. No actual root, multiplicity or all-degree sign
conclusion follows from the reference calculation.

## Mathlib

Not checked. Full matching coverage for this exact normalized diagnostic
and sequence criterion is unknown. Jensen's inequality and elementary
integration are named standard inputs; the finite specialization and
all analytic justifications are given above. No formal verification or
new mathematical discovery is claimed.
