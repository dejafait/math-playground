# Lemma 509: exact symmetric fractional real-zero allocation region

## Hypotheses

Let r>0 and 0<=w<=1 be real. For real x other than +/-r define

    G(x)=2(x^2-1)/(x^2+1)^2+w/(x+r)^2+w/(x-r)^2.

This is precisely the approved m=d=1, p=q=r, alpha=beta=w
slice of the signed block. No actual-Xi configuration, multiplicity
allocation or entire function with fractional root multiplicities is
assumed. Put a=r^2 and a0=7-4 sqrt(3). For a>0 define

    f_a(y)=(1-y)(y-a)^2/((y+a)(y+1)^2)  (y>=0).

For 0<a<1 set b(a)=(1-a+sqrt(a^2+34a+1))/6.

The value f_a(a)=0 is used only to optimize this continuous rational
function; the original G remains undefined at x=+/-r. Define

    W(a)=f_a(b(a))  if 0<a<a0,
    W(a)=a          if a0<=a<=1.

## Conclusion

The exact feasibility region for G(x)>=0 at every real x!=+/-r is

    0<a=r^2<=1,       W(a)<=w<=1.                         (1)

In the first branch a<W(a)<1/8. Thus the region is nonempty
and depends on the displacement ratio r. All feasible w are positive.
For feasible parameters the complete list of zeros in the domain is:

- If w>W(a), there are none: G(x)>0 throughout its domain.
- If w=W(a), 0<a<a0, they are x=+/-sqrt(b(a)).
- If w=W(a)=a=a0, they are x=0 and x=+/-sqrt((1-a)/2).
- If w=W(a)=a and a0<a<=1, the only zero is x=0.

All listed nonzero equality points differ from +/-r. In particular,
a=1 is feasible only with w=1 and has only x=0 as an equality point.
In every feasible case G(x) tends to +infinity as x tends to either
excluded point +/-r; neither point is an additional equality case.

Every infeasible parameter pair within r>0, 0<=w<=1 has a finite
negative witness: x=0 if w<a (including every a>1); otherwise
necessarily 0<a<a0 and w<W(a), and x=+/-sqrt(b(a)) is negative.

For w>W(a), writing y=x^2, the strict margin can be expressed as

    G(x)>=2(w-W(a))(y+a)/(y-a)^2>0.                       (2)

This is not a uniform positive lower bound on the whole real axis:
G(x) tends to zero as |x| tends to infinity. The result is a finite
algebraic compensation rule, not an actual-Xi sign theorem or RH.

## Proof

### Exact reduction and critical point

Adding the two real-root terms gives, for y=x^2>=0, y!=a,

    G(x)/2=(y-1)/(y+1)^2+w(y+a)/(y-a)^2
           =A_a(y)(w-f_a(y)),
    A_a(y)=(y+a)/(y-a)^2>0.                              (3)

At x=0 this is G(0)=2(w/a-1), so w>=a is necessary.
In particular a>1 is impossible under the budget w<=1, and w=0
is always infeasible. For y>=1, f_a(y)<=0. It remains to optimize
f_a on [0,1] when 0<a<=1. Its endpoints are f_a(0)=a and
f_a(1)=0. The omitted y=a has f_a(a)=0, so deleting it cannot
delete a positive global maximum.

For 0<a<1, direct differentiation gives

    f_a'(y)=(a+1)(y-a) R_a(y)/((y+a)^2(y+1)^3),
    R_a(y)=-3y^2+(1-a)y+3a.                             (4)

The quadratic R_a has roots of opposite sign, since their product
is -a. Its positive root is b(a). Moreover

    R_a(a)=4a(1-a)>0,    R_a(1)=-2(1-a)<0,

so a<b(a)<1. Thus f_a strictly decreases on [0,a], strictly
increases on [a,b(a)] and strictly decreases on [b(a),1]. The
only possible global maxima on [0,1] are y=0 and y=b(a), and
these maxima remain available in the original domain. For a=1,
the comparison in the next paragraph handles the endpoint directly.

### Which maximum dominates

Expansion and factorization give, for every a>0 and y>=0,

    a-f_a(y)=(a+1)y Q_a(y)/((y+a)(y+1)^2),
    Q_a(y)=y^2-(1-a)y+3a.                               (5)

Its discriminant is Delta=a^2-14a+1, with roots in a equal to
7-4 sqrt(3)=a0 and 7+4 sqrt(3)>1. Hence, on 0<a<=1,
Delta<0 for a>a0, Delta=0 for a=a0, and Delta>0 for a<a0.

For a>a0 the monic quadratic Q_a is strictly positive. By (5),
f_a(y)<a for every y>0 and f_a(0)=a. This proves W(a)=a,
including a=1, and identifies its unique maximizing point.

For a=a0, Q_a(y)=(y-y0)^2 with y0=(1-a)/2.
Here 0<a0<1/3: positivity follows from 7^2>16*3,
and a0<1/3 follows from sqrt(3)>5/3. Consequently a<y0<1.
The maximum a is attained exactly at y=0 and y=y0. Also
R_a(y0)=-Delta/4=0, so y0=b(a); it is an allowed point.

For 0<a<a0, the vertex y0=(1-a)/2 lies in (a,1), since
a<a0<1/3. At this vertex Q_a(y0)=-Delta/4<0.
Equation (5) therefore gives f_a(y0)>a. The critical-point
classification in (4) forces the unique global maximum to be
f_a(b(a))>a. This establishes both branches of W without an
extraneous root from squaring a radical.

For this first branch, b=b(a) lies in (a,1). Since 0<a<b,

    (b-a)^2 < b(b+a),
    f_a(b) < b(1-b)/(b+1)^2 <= 1/8.

The strict inequality is equivalent to a^2<3ab, and the last
inequality is equivalent to (3b-1)^2>=0. Thus W(a)<1/8<1;
the other branch W(a)=a<=1 also fits the permitted budget.

### Necessity, sufficiency, equality and exclusions

On the full half-line y>=0, the maximum f_a is W(a): the
nonpositive part y>=1 adds no competing maximizer. All its
maximizers identified above avoid y=a. Equation (3) therefore
proves (1), all the equality cases and the strict margin (2).
It also proves the asserted negative witnesses: a failure w<a
is detected at y=0; a failure w>=a can occur only in the first
branch and is detected at its allowed maximizer b(a)>a.

In a feasible case w>=a>0. At x=r the term w/(x-r)^2
diverges to +infinity while the other terms stay finite because
r>0; the argument at x=-r is identical. Those points are always
excluded, even when w=0 makes their real-root terms removable.
That zero-charge case was already ruled out by G(0)=-2.
Finally direct division by x^2 shows

    lim_(|x|->infinity) x^2 G(x)=2+2w>0.

This justifies the qualification concerning a global margin.

### Verification, provenance and scope

The proof is elementary rational differentiation and real-variable
optimization. No literature theorem is being reproved to obtain an
already cited conclusion. The prior source comparison in
`drafts/literature/2026-10-30-signed-real-zero-allocation-coverage.md`
did not find this exact fractional-budget criterion; that bounded
search does not establish originality. L251 and L257 are masking
contrasts, not mathematical inputs. L471 (6) motivates the signed
block but is not used in this standalone finite calculation.

Run `python3 scripts/signed-allocation/verify_symmetric_region.py`.
The exact-rational polynomial replay writes
`scripts/signed-allocation/symmetric-region-certificate.json`.
It verifies (4)'s numerator, (5), the 1/8 comparison identity and
a0's quadratic equation. It also checks the negative example
a=w=1/16, x^2=1/2, where f_a(x^2)=49/648>w and G=-34/441.
This certificate verifies algebra only; it does not replace the
complete parameter and domain argument above or a separate audit.

For any eventual use in Xi, distinct-pair allocations must conserve
each real zero's multiplicity. No such global matching, geometry,
convergent assembly, zero-safe extension or residual-pair estimate
is supplied. Even a valid first-sign application would leave higher
signs open. No general asymmetric or scaled theorem is asserted.
The separate finite audit below passes; this does not audit the cited
source manuscripts or provide an actual-Xi application.

### Separate critical audit, 30 October 2026

The audit used the prior EXPLORE assessment
`drafts/literature/2026-10-30-l509-critical-audit-coverage.md`.
Only L509's finite theorem was tested. The definition of f_a above
was made explicit for all a>0, as already used at a=1 in the proof;
no formula, threshold or mathematical conclusion changed.

Independently adding 1/(x+r)^2 and 1/(x-r)^2 gives
2(y+a)/(y-a)^2. All factors divided out in (3)--(5) are strictly
positive for y>=0, apart from the explicitly deleted y=a in (3).
Thus multiplying the inequality by these denominators neither
changes its direction nor loses a permitted equality. The map
x -> y=x^2 covers exactly [0,infinity); positive y contributes both
real square roots, whereas y=0 contributes only x=0.

Re-expansion of N'D-ND', with N=(1-y)(y-a)^2 and
D=(y+a)(y+1)^2, gives
(a+1)(y-a)(y+1)R_a(y). Cancellation of the positive factor y+1
gives (4). The negative root of R_a is strictly negative because
its root product is -a; R_a(a)>0 and R_a(1)<0 locate the other
root in (a,1). This proves the three strict monotonicity intervals,
so no stationary point or endpoint other than 0 and b can maximize.

Re-expansion of aD-N gives (a+1)yQ_a(y). The two parameter
roots of its discriminant are a0 and 7+4sqrt(3)>1, so the proof's
sign split covers the entire remaining range 0<a<=1. At a=a0
the double root y0=(1-a)/2 lies in (a,1) and satisfies R_a(y0)=0.
For a<a0 the same vertex has Q_a(y0)<0, forcing f_a(b)>a;
for a>a0, Q_a is everywhere positive. These facts verify the
transition and every maximizing point, including a=1, directly.
The strict first-branch bound uses a<b, hence a^2<3ab, and the
identity (b+1)^2-8b(1-b)=(3b-1)^2; it gives W<1/8.

The parameter cases are exhaustive: a>1 forces w<a; for
0<a<=1, w<a is negative at 0; with w>=a, failure is possible
only when a<a0 and w<f_a(b), giving the allowed witnesses
x=+/-sqrt(b). Conversely w>=W makes (3) nonnegative for every
permitted y. At equality only the maximizing y can occur; their
locations above verify the complete stated zero list. The deleted
y=a has f_a(a)=0<W and cannot conceal a maximizer. In a feasible
case w>=a>0, each deleted pole has one positive divergent summand
and all other summands bounded. The infeasible w=0 case is detected
at 0 even though its deleted poles would be removable. Finally
x^2G(x) tends to 2+2w, so strict positivity never supplies a
constant positive margin at infinity. Equation (2) retains its
stated, decaying factor.

The exact certificate script was inspected and replayed. All three
polynomial identities have zero coefficient differences, the
transition residual is (0,0) in Q(sqrt(3)), and the recorded negative
sample has required w=49/648>1/16 and G=-34/441<0. There are no
reported failures. These algebra checks support the full domain
argument above rather than replacing it. The audit finds no
mathematical defect, new threshold, stronger sign, or originality
evidence. Actual-Xi geometry, conserved multiplicity allocations,
convergence, unmatched-pair control and higher signs remain open.

## Mathlib

Full matching theorem and supporting results not checked. No absence
claim or formal verification is made. The exact Python checks above
are not Lean proofs. Reference portal:
https://leanprover-community.github.io/mathlib4_docs/
