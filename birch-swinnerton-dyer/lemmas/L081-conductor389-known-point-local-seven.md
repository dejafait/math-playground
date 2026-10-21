# L081 — The supplied rational point is nonzero locally modulo seven

## Hypotheses

Let E/Q be the exact minimal equation

\[
E:\quad y^2+y=x^3+x^2-2x,
\qquad [a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0],
\]

let P=(0,0), and view P in E(Q_7). L030 supplies minimality and
discriminant 389; L033 supplies good reduction at seven and the complete
count #E(F_7)=13. No rank, independence, Selmer-corank, finite-quotient,
residual-surjectivity or complex-order premise is used. P is the known
point recorded in L034, but its rational membership follows just by
substitution; no published basis calculation is needed here.

## Conclusion

The image of P in E(Q_7)/7E(Q_7) is nonzero. More precisely, W=[13]P
is the nonidentity rational point

\[
x(W)=\frac{-791464517307769165158639}{400595921638177470929689},\qquad
y(W)=\frac{32125746116248067751254126885329224}
{253547764228101693293432324785359613},
\]

and its formal parameter is

\[
t(W)=-\frac{x(W)}{y(W)}
=\frac{41522938291582887074944757}{2662910619396726133047736},
\qquad v_7(t(W))=1.
\]

This is a fixed known-method specialization, classified REPRODUCTION,
not progress beyond the inspected source theory or a new rank result.
The separate fixed critical audit below passes for the finite instance
and its applicability proof. No L062 application is made: every L026 premise and an
appropriate exponent condition, in particular D=D_div for e=0, remain
independent obligations. No second strict rational direction or general
BSD comparison is supplied.

## Proof

**Named inputs and scope.** Import Joseph H. Silverman, *The Arithmetic
of Elliptic Curves*, second edition, GTM 106, Springer (2009),
DOI 10.1007/978-0-387-09494-6: III Group Law Algorithm 2.3, pp.53–54;
VII Proposition 2.1, pp.188–190, and Proposition 2.2, p.191; IV Lemma
6.3(b), p.131, and Theorem 6.4, p.132. Direct primary locators are
[group law](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71),
[reduction](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204),
[formal parameter](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=207)
and [logarithm](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150).
The [author errata, 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf),
entries for pp.130–133 and 185–191, qualify convergence and correct
special-fiber notation. We use only the strict logarithm radius below,
not the unqualified convergence wording corrected for IV.6.3(a).

The prior source assessment
`drafts/literature/2026-10-18-known-point-local-seven-test.md` inspected
the theorem hypotheses and relevant proof cases, errata and exact-model
overlap. These general theorems are imported, not reproved. The remaining
work is finite rational arithmetic and their stated applicability to this
point and the full local group. Recomputing this finite value is needed
because no inspected source supplies its exact depth-one certificate.

**Exact scalar chain.** For this equation negation is
-(x,y)=(x,-y-1). If neither input is O or the inverse of the other,
write the inputs (x,y),(u,v). For distinct inputs put

\[
\lambda=\frac{v-y}{u-x},\quad \nu=\frac{yu-vx}{u-x};
\]

for doubling put

\[
\lambda=\frac{3x^2+2x-2}{2y+1},\quad
\nu=\frac{-x^3-2x-y}{2y+1}.
\]

Then the sum has coordinates
x'=lambda^2-1-x-u and y'=-lambda*x'-nu-1. The a_2=1 and a_3=1
terms are retained. Every fraction below is reduced; both inputs and
the output of each row satisfy the original curve equation.

| Operation | Branch; nonzero formula denominator | lambda; nu |
|---|---|---|
| P+P=2P | tangent; 1 | -2; 0 |
| 2P+P=3P | chord; -3 | 5/3; 0 |
| 3P+3P=6P | tangent; 83/27 | 1/83; 2357/2241 |
| 6P+6P=12P | tangent; -48450391/15438249 | -9161440066/4021382453; 913945828624948/747989200405359 |
| 12P+P=13P | chord; -189342513653835405031/145543651499666674881 | 4354468520054797616597/7635718251159787407003; 0 |

The intermediate points are

\[
\begin{aligned}
2P&=(3,5),\\
3P&=(-11/9,28/27),\\
6P&=(89566/62001,-31944320/15438249),\\
12P&=(189342513653835405031/145543651499666674881,\\
&\hspace{12mm}1302656862890619288551756451671/
1755860058858920105145927789279).
\end{aligned}
\]

All are finite. In each chord row the x-coordinates differ. In each
tangent row 2y+1 is exactly the displayed nonzero denominator, so no
inverse/doubling-to-O exception occurs. Thus the algorithm applies at
every step and gives exactly the W stated above, not merely another
on-curve point.

Full evidence is `scripts/known-point-seven-307/certificate.json`;
the independent complete replay is
`scripts/known-point-seven-307/verification.json`. Reproduce by

```bash
python3 scripts/known-point-seven-307/build_certificate.py
python3 scripts/known-point-seven-307/verify_certificate.py
```

The verifier imports no producer and uses the rational translation
X=x+1/3, Y=y+1/2 to Y^2=X^3-(7/3)X+107/108. It replays all five binary
rows by short-model line intersection, checks every saved branch,
denominator, slope, intercept and original-coordinate output, and then
separately computes all thirteen additions from O to 13P. Its report
retains every sequential intermediate point and denominator. All exact
curve/line identities and the final equality pass. This is independent
finite replay, not a separate critical audit.

The first verifier had a sign error in the third-intersection ordinate,
caught at its first tangent's curve check. Its source and failure are
preserved in `scripts/known-point-seven-307/initial-failed-verifier.py.txt`
and `initial-failure.txt` in the same directory. The repair changes that
ordinate to y+m*(rx-x) before negation; the producer/certificate is
unchanged. The passing report hashes the complete certificate. This
initial failure is not counted as a successful rejection test.

**Complete valuation and reduction checks.** In the reduced coordinates,
the numerator/denominator valuations are (0,2) for x(W) and (0,3) for
y(W). The exact denominator decompositions are

\[
400595921638177470929689=7^2\cdot8175426972207703488361,
\]
\[
253547764228101693293432324785359613
=7^3\cdot739206309702920388610589868178891.
\]

The two coordinate numerators and displayed denominator quotients are
units at seven. Cancellation in -x/y gives the stated reduced t, whose
numerator is

\[
41522938291582887074944757
=7\cdot5931848327368983867849251.
\]

The latter quotient and denominator 2662910619396726133047736 are
seven-adic units. The replay checks each integer factorization,
nondivisibility by seven and reducedness. Thus the actual valuations
are v_7(x)=-2, v_7(y)=-3, v_7(t)=1, meeting the required threshold one.

Clearing denominators gives the primitive homogeneous triple

\[
[X:Y:Z]=[-500938846328319659034790025232446763:
32125746116248067751254126885329224:
253547764228101693293432324785359613].
\]

It has gcd one, satisfies
Y^2 Z+YZ^2=X^3+X^2 Z-2XZ^2 exactly and reduces to [0:6:0]=O at seven.
This both certifies the reduction and avoids reducing a nonintegral
affine coordinate. Independently, the reduction homomorphism and
#E(F_7)=13 already imply [13]P lies in the reduction kernel. W is
nonidentity since it has the displayed finite affine coordinates.

**Passage from the formal subgroup to the full group.** Work over the
complete discretely valued field Q_7 with ring Z_7, maximal ideal 7Z_7,
perfect residue field F_7 and normalized valuation v_7(7)=1. The model
is minimal integral and has good reduction. Silverman VII.2.1 gives

\[
0\longrightarrow E_1(Q_7)\longrightarrow E(Q_7)
\longrightarrow E(F_7)\longrightarrow0.
\]

Here E_0(Q_7)=E(Q_7) by good reduction. VII.2.2 identifies E_1(Q_7)
with the formal group on 7Z_7 by t=-x/y, with t(O)=0. Let E_r for r>=1
be the subgroup corresponding to 7^r Z_7. The coordinate parameter at
the original P is not used: -x/y is undefined there. It is used only
at W, where y is nonzero and projective reduction is O.

The formal group has coefficients in Z_7. For r=1 and r=2 the strict
radius condition of IV.6.4 is satisfied:

\[
r>v_7(7)/(7-1)=1/6.
\]

The same formal logarithm therefore gives compatible group isomorphisms
E_1 -> 7Z_7 and E_2 -> 49Z_7. IV.6.3(b)'s strict leading-term estimate
also preserves the valuation of each nonzero parameter in this radius.
Since it is a homomorphism,

\[
\log([7]E_1)=7\log(E_1)=49Z_7=\log(E_2).
\]

Injectivity on E_1 gives [7]E_1=E_2. The computed v_7(t(W))=1 means
W belongs to E_1 but not E_2, hence W is not a seven-multiple in E_1.

Suppose W=[7]R with R in the entire E(Q_7). Reduction gives
[7]bar(R)=O. Multiplication by seven is invertible on E(F_7), since its
order is 13: Bezout's identity for 7 and 13 supplies its inverse.
Consequently bar(R)=O, so R belongs to E_1. This would put W in
[7]E_1=E_2, a contradiction. Thus W is not in 7E(Q_7).

Finally the quotient E(Q_7)/7E(Q_7) is killed by seven. Multiplication
by 13 is an automorphism on it, with inverse multiplication by six
because 6*13=1+11*7. Therefore [W]=13[P] is nonzero if and only if
[P] is nonzero, proving the conclusion for the supplied P.

**Downstream boundary.** A known rational point can furnish a classical
global Kummer class, but this local computation does not verify the
additional hypotheses of L062, construct a descent power-class
representative, establish D=D_div, or produce a strict rational class.
Those independent conditions cannot be replaced by this valuation. The
arbitrary-curve rank/order gap and all stopped order/descent routes are
unchanged.

**Separate critical audit, 2026-10-18 (step 309).** The approved fixed
audit passes. Reproduce its complete saved evidence without changing the
original directory by running

```bash
python3 scripts/known-point-seven-audit-309/audit.py
```

The audit copies the producer and verifier into its own `fresh/`
subdirectory, executes both, and compares the complete new certificate
and verification report byte for byte with the originals. All five
binary branches and all thirteen sequential additions pass, including
the initial identity row. The report is
`scripts/known-point-seven-audit-309/audit.json`; its complete row and
valuation evidence was inspected, not just its PASS label. All six
original files retain their SHA-256 hashes, recorded in
`scripts/known-point-seven-audit-309/original-hashes.json`.

As a distinct exact check, for every nonidentity row let the two inputs
be (x,y),(u,v), the output (z,w), and the saved line be Y=mX+n.
The audit verifies the entire polynomial identity

\[
(mX+n)^2+(mX+n)-(X^3+X^2-2X)
=-(X-x)(X-u)(X-z).
\]

It checks all four rational coefficients, both input incidences and
the reflected-output incidence -w-1=mz+n. For a tangent it also checks
(2y+1)m=3x^2+2x-2 with 2y+1 nonzero; for a chord it checks u-x nonzero
and (u-x)m=v-y. Thus the factorization has the required intersection
multiplicities and the output is the reflected third intersection,
rather than merely some on-curve point. All 17 nonidentity rows (five
binary, twelve sequential) have four zero coefficient residuals. These
are rowwise checks, with some repeated additions between the two chains,
not 17 different scalar operations. The sole identity row is exactly
O+P=P. No inverse-pair or vertical-tangent branch occurs, as certified
by the nonzero denominators and the branch conditions above.

The short-model translation is checked coefficientwise:

\[
(X-1/3)^3+(X-1/3)^2-2(X-1/3)+1/4
=X^3-(7/3)X+107/108.
\]

The inverse is x=X-1/3,y=Y-1/2; the projective translation fixes O,
preserves lines and tangencies, and changes -(x,y)=(x,-y-1) into
(X,-Y). This justifies its use with the imported group-law algorithm.
The preserved initial verifier is executed on a fresh copy and again
fails its first tangent's `assert good(r)`. The one-line difference
changes y+m*(x-rx) to y+m*(rx-x) before negation, exactly the line
incidence required above. The failure log is preserved; this verifies
the historical repair, not a malformed-certificate rejection claim.

Independent exact power divisibility and unit residues give the
numerator/denominator valuations (0,2), (0,3), (1,0) for x,y,t.
The signed unit-residue pairs are (2,4), (6,6), (5,4), respectively.
In particular t/7=3 modulo seven, so the actual parameter valuation
is exactly the required one, not merely a lower bound. The primitive
projective triple has gcd one, satisfies the full homogeneous equation,
has the stated affine ratios and reduces to [0:6:0].

The applicability review reuses L030's exact minimal integral equation
and L033's complete reduction order; it does not re-audit their unrelated
symbol/coefficient constructions. Both logarithm radii 1 and 2 strictly
exceed 1/6. The isomorphisms are restrictions of the same formal series,
so their images and injectivity justify [7]E_1=E_2, including equality
rather than only containment. For any putative W=[7]R, order 13 of the
full reduction group forces R into E_1 before this equality is used.
Finally 6*13=1+11*7 proves the quotient automorphism used to transfer
nonzero from W to P. Thus no division point outside the formal subgroup,
unqualified convergence assertion, or logarithm at P=(0,0) is hidden.
The direct mathematical inputs remain L030 and L033. The audit adds no
L026 premises, D=D_div, strict rational direction or global rank result.

## Mathlib

Full matching local-seven test and supporting formal logarithm/radius,
Weierstrass group-law and reduction coverage: not checked. No absence
from Mathlib is inferred. The general analytic and reduction results
are precise imports from Silverman; only this finite instance and the
stated applicability argument have been reproduced.
