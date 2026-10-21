# L068 — Exact reduction order fails the thirteen-adic index shortcut

## Hypotheses

Use L033's exact quotient model

    E1: Y²+Y=X³−X²−7820X−263580.

Use L064's entire completion F=K tensor_Q Q13, an unramified
extension of degree twelve with residue field k=F_(13^12).
L067 supplies good reduction of this same E1 over its integer ring.
The finite-field reduction is the displayed model, without a twist.
No rank, generators, index, integer solution or GRH is assumed.

## Conclusion

The complete projective counts are

    #E1(F13)=10,
    #E1(k)=23,298,078,211,200
          =13 · 1,792,159,862,400.

Thus Bruin Lemma 4.2's prime-to-residue-characteristic reduction-order
hypothesis fails for E1 over this completion at thirteen. This parks
that sufficient index shortcut at thirteen only. It does not establish
that any actual subgroup index is divisible by thirteen, exclude the
54a1 branch, obstruct every saturation method, or invalidate L067.

## Proof

### Complete projective base-field count

The coefficients reduce to −7820=6 and −263580=8 in F13. Hence the
affine equation is Y²+Y=X³−X²+6X+8. Checking every Y in F13 for
every X gives the following complete table (empty entries mean none):

| X | Y coordinates |
|---|---|
| 0 | none |
| 1 | none |
| 2 | none |
| 3 | none |
| 4 | 1, 11 |
| 5 | none |
| 6 | 6 |
| 7 | 2, 10 |
| 8 | none |
| 9 | none |
| 10 | 2, 10 |
| 11 | none |
| 12 | 0, 12 |

There are nine affine points. Homogenizing gives

    Y²Z+YZ²=X³−X²Z−7820XZ²−263580Z³.

At Z=0 it forces X=0, so the unique projective point at infinity is
[0:1:0]. The Z derivative of the left side minus the right side at
this point is 1, ensuring smoothness there. The model's discriminant
is −11, a unit modulo thirteen, so it is a smooth elliptic curve.
The certificate also checks that no affine point simultaneously has
2Y+1=0 and 3X²−2X−7820=0. The total projective count is therefore 10,
including the origin, as required by the counting theorem.

### Imported extension-count formula and exact specialization

Import J. S. Milne, *Elliptic Curves*, second edition (2021), Chapter IV
Section 9, Theorem 9.10 and Remark 9.11(a), printed p.156
([author PDF, p.161](https://www.jmilne.org/math/Books/EC2.pdf#page=161)).
For an elliptic curve E/F_p, if N1=#E(F_p), choose alpha,beta with
alpha+beta=p+1−N1 and alpha beta=p. For every n>=1 the theorem gives

    #E(F_(p^n))=1+p^n−alpha^n−beta^n.

Its elliptic-curve and projective-count hypotheses hold above. It has
no ordinarity hypothesis. The full degree-twelve residue field comes
from L064, not an isolated factor or a degree-six subfield. The general
counting theorem is cited; reproving it is unnecessary for this finite
arithmetic specialization.

Here alpha+beta=4 and alpha beta=13. Put S_n=alpha^n+beta^n.
Each root satisfies u²=4u−13, so multiplication by u^(n−2) and
addition give S_n=4S_(n−1)−13S_(n−2) for n>=2, with S_0=2, S_1=4.
Exact integer evaluation gives, for n=0 through 12,

    2, 4, −10, −92, −238, 244, 4070, 13108,
    −478, −172316, −683050, −492092, 6911282.

Since 13^12=23,298,085,122,481, the required count is

    1+23,298,085,122,481−6,911,282=23,298,078,211,200.

As a second exact evaluation use M=((4,−13),(1,0)). Its characteristic
polynomial is u²−4u+13, with distinct roots alpha,beta. Consequently
trace(M^n)=S_n, including n=0. Independent binary matrix exponentiation
checks all thirteen sums; in particular

    M^12=((1209001,14603160),(−1123320,5702281))

has trace 6,911,282. Modulo thirteen, the recurrence gives S_12=4^12=1
by Fermat's little theorem, independently confirming that the count
has remainder 0 rather than the required remainder in {1,...,12}.

### Scope of the index comparison

N. Bruin, *Chabauty methods using elliptic curves*, J. reine angew.
Math. **562** (2003), 27–49, Lemma 4.2, printed p.44
([DOI](https://doi.org/10.1515/crll.2003.076)), requires p>2,
unramifiedness, good reduction and reduction-group orders prime to p,
as well as finite-index formal-kernel generators for its index test.
The inspected statement/proof and FNS generator limitations are retained
in `drafts/literature/2026-10-14-fixed-class-elliptic-chabauty-scope.md`.
Here there is just one prime above thirteen, since L064 identifies the
entire completion as a field. Its order is divisible by thirteen, so
this order premise fails. The other local premises do not repair it.
No use of the lemma's conclusion is made, and the absent global
generator/index hypotheses remain independent gaps.

### Replayable arithmetic evidence

Run `python3 scripts/thirteen-reduction-order/check_order.py`.
The complete certificate is
[scripts/thirteen-reduction-order/order-certificate.json](../scripts/thirteen-reduction-order/order-certificate.json).
It records all 169 affine equation residues, all solutions and the
origin, invariants, every scalar sum, every binary matrix power, all
extension counts through degree twelve, and the required/actual
remainder comparison. All ten arithmetic consistency checks pass;
there are no arithmetic failures. The mathematical order hypothesis
itself fails, explicitly recorded separately from those checks.
The entire residue table, matrix powers and extension counts were
inspected, not inferred from a bounded preview. Independent critical
review completed on 2026-10-14 confirms the conclusion below; no full
Beal candidate results.

### Independent critical audit, completed 2026-10-14

Run `python3 scripts/thirteen-reduction-order/audit_order.py`.
The full independent evidence is
[scripts/thirteen-reduction-order/audit-certificate.json](../scripts/thirteen-reduction-order/audit-certificate.json).
All 19 checks pass, with no arithmetic correction. No generating code
is imported or executed. The original certificate is preserved and
its SHA-256 is recorded in the audit certificate.

Starting from L033's integer coefficients, completing the square gives
four times the affine residual as
(2Y+1)²−(4(X³−X²−7820X−263580)+1). Multiplication by 10, the inverse
of 4 modulo 13, independently reproduces all 169 residual entries and
all nine affine points. Exhausting the normalized infinity coordinates
[1:Y:0] and [0:1:0] leaves only the latter; the homogeneous gradient
there is (0,0,1). Integer invariant arithmetic recomputes the
discriminant from (c4³−c6²)/1728 as −11. Its nonzero reduction proves
geometric smoothness, not merely absence of F13-rational singularities.

Successive ordinary matrix multiplications reproduce every full M^n
for 0<=n<=12, independently of the construction's binary powering.
As another exact check, in Z[u]/(u²−4u+13), multiplication of a+bu by
u sends (a,b) to (−13b,a+4b). Its conjugate sum is 2a+4b. All thirteen
such sums agree with the scalar recurrence and matrix traces. Every
extension count for 1<=n<=12 agrees with the original certificate.
In particular the actual remainder is zero, whereas Bruin's tested
premise requires a remainder in {1,...,12}. Complete residues, matrix
powers, quotient powers, sums and extension counts have been checked.

For applicability, L033's E1 is the displayed quotient curve, without
a twist; L067 uses this same integral model. Audited L064 identifies
the whole K tensor Q13 as one unramified degree-twelve field using the
irreducible reduction of K's defining polynomial. The squared
degree-six canonical-fiber polynomial is not used as a decomposition.
Thus there is exactly one prime above thirteen, with residue degree
twelve, and Milne's projective extension-count theorem applies to the
whole required residue field. Existing input audits are reused, not
claimed as new arithmetic reruns.

The separately approved primary-source review locates Bruin's Lemma
4.2 and complete proof on printed p.44, PDF p.19 of the
[published author copy](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf#page=19).
This corrects the former p.45 citation only. In that proof, coprimality
of the reduction-group orders with p makes a point G with pG reducing
to the origin itself reduce to the origin. Failure of this sufficient
premise does not reverse that implication or determine a subgroup
index. The arithmetic therefore confirms only the limited shortcut
stop. Rank, finite-index generators, other index methods, coset bounds,
other classes and global primitive power lifting remain unresolved.

## Mathlib

Full matching extension-count theorem and this exact count: not checked.
Supporting elliptic-curve, finite-field and matrix arithmetic coverage:
not checked. Unknown availability is not evidence of absence.
