# Corollary 463a: exact witness/upper-tail intersection

## Hypotheses

Use the actual Xi coefficients and all retained external hypotheses of
L461 and L463, including their manuscript/import audit qualifications.
In particular, the cited strict zero-free half-plane is Re(s)>7/8,
with the pole allowed and boundary zeros not excluded. The precise
citations and local applicability arguments are canonical in those
lemmas; no analytic result is reproved here.

Fix c>3/16 and c_0>3/8 before varying the real center a. Choose
B_c>0 as in L461 and A_(c_0)>2π as in L463. Put d=c_0/2 and,
for t=|a|≥A_(c_0), define

    X(t)=c log(2+t)+B_c,     N(t)=ceil(X(t)),
    q(t)=d log(t/(2π)),      M(t)=ceil(q(t))−1,
    W(t)=min(N(t),M(t)).

All logarithms are natural. These constants and onsets are existential.
Central real zeros and arbitrary central multiplicities are permitted.

## Conclusion

Every hypothetical nonreal zero a+ib with |a|≥A_(c_0) forces
D_n(Xi;a)<0 for some integer 1≤n≤W(|a|). If W(|a|)=0, there
is no such nonreal zero. At |a|<A_(c_0), only L461's original
cutoff N(|a|) is supplied by this argument.

For fixed 3/16<d≤c, the exact surviving cutoff is M(t), and
M(t)≤N(t)−1 throughout t≥A_(2d). If d<c, the saving satisfies

    N(t)−M(t)=(c−d)log t+B_c+d log(2π)+O(1) → ∞.

If d=c, the saving is positive but bounded as t→∞. If d>c,
W(t)=N(t) for all sufficiently large t. In every case

    lim_(t→∞) W(t)/log t = min(c,d) > 3/16.

This is an elementary REPRODUCTION/application of the two inputs,
not a new sign theorem. It shortens any fixed L461 range by choosing
d<c, but the compared fixed-parameter bounds have the same limiting
infimum 3/16. No endpoint, effective height overlap, initial sign or
RH conclusion is obtained.

## Proof

At a hypothetical nonreal zero, L461 gives a negative coefficient at
an integer 1≤n≤N(t). L463 makes every integer n≥0 with n≥q(t)
strictly positive, using the identical analytic-product coefficient
convention. Therefore this negative index must satisfy n<q(t).
The greatest integer strictly less than a real q is ceil(q)−1:
if q is an integer this is q−1; otherwise it is floor(q).
Consequently n≤M(t), proving the intersection claim, including
the integer-boundary case. Since q(t)>0, M(t)≥0; W(t)=0 leaves
no possible positive integer witness and hence excludes the zero.
No division by Xi(a) has been used. The common onset is A_(c_0),
since L461 holds at all real centers; there is no additional height
restriction to be made uniform in n.

For d≤c and t≥A_(2d)>2π,

    q(t)=d log(t/(2π)) < c log(2+t)+B_c=X(t).

Here log(t/(2π))>0, d≤c, log(t/(2π))<log(2+t), and B_c>0.
Monotonicity of ceil gives ceil(q(t))≤ceil(X(t)), hence
M(t)≤N(t)−1. Thus W(t)=M(t) throughout this height range.
To quantify the saving, use

    X(t)−q(t)=(c−d)log t+B_c+d log(2π)+c log(1+2/t).

For e_X(t)=ceil(X(t))−X(t) and e_q(t)=ceil(q(t))−q(t),
both in [0,1), the exact rounding identity is

    N(t)−M(t)=X(t)−q(t)+1+e_X(t)−e_q(t).

The last correction lies strictly between 0 and 2. This proves
the asymptotic saving and, when d=c, boundedness and strict
positivity. When d>c, X(t)−q(t)→−∞. Eventually q(t)>X(t)+2,
so M(t)≥N(t), and W(t)=N(t).

Finally N(t)/log t→c and M(t)/log t→d because B_c is fixed,
log(2+t)/log t→1, log(t/(2π))/log t→1 and rounding is bounded.
Taking the minimum proves the asserted limit. Both c and d are
strictly above 3/16. For each fixed original c, one may first choose
any fixed d in (3/16,c), then invoke L463 with c_0=2d.
The resulting onset depends on that choice. Sending d to 3/16
while varying t would require uniform onsets unavailable in these
inputs. Even an endpoint order bound would not supply the missing
initial signs. The interval below A_(2d) remains uncontrolled by
the tail theorem, with no evaluated overlap with verified heights. ∎

## Mathlib

Full matching coverage has not been checked. The range comparison
uses elementary properties of the integer ceiling and logarithms;
no particular supporting Mathlib declaration is asserted. This does
not change the external manuscript audit qualifications of the inputs.
