# L099 — Rational independence from the fixed finite witnesses

## Hypotheses

Let E/Q be y²+y=x³+x²−2x, with coefficients [0,1,1,-2,0],
P=(0,0), Q=(1,0), and R=Q−4P. Both points lie on this equation
by substitution. Use L030's minimal integral model and discriminant 389,
L033's good reduction and #E(F_7)=13, L081's nonzero image of P in
E(Q_7)/7E(Q_7), L096's relation Q=4P in that quotient, and L097's
R not in 7E(Q). Only the local conclusions of these inputs are used
where indicated; no published rank, basis, saturation or Sha computation
is a hypothesis. In particular the global conclusions of L083, L034 and
L082 are excluded.

## Conclusion

The images of P,Q in E(Q) tensor_Z Q are linearly independent.
Consequently rank E(Q)>=2. More precisely, their classes induce an
injection F_7² -> E(Q)/7E(Q), and this injection survives passage to
the quotient by rational torsion.

This is a REPRODUCTION of an assessed known independence method on a
known curve. It replaces the published-basis input for this lower bound
with existing finite witnesses; it is not a new rank result beyond the
sources checked. The separate critical audit below passes.
It proves neither saturation nor a basis, a zero-log rational point,
a full strict Selmer kernel, rank equality or arbitrary-curve BSD.

## Proof

**Imported results and reason for specialization.** Mordell–Weil finite
generation is Silverman, *The Arithmetic of Elliptic Curves*, second
edition (2009), VIII Theorem 6.7, printed p.239
([primary text](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=254)).
The finitely generated abelian group decomposition is Milne, *Group
Theory*, v4.01 (6 November 2025), Theorems 1.54 and 1.57, pp.25–26
([author text](https://www.jmilne.org/math/CourseNotes/GT.pdf#page=25)).
We use the pointwise independence criterion proved in Datta–Smith,
*Frobenius and valuation rings*, ANT 10:5 (2016), Lemma 5.5, p.1073,
DOI 10.2140/ant.2016.10.1057
([primary text](https://msp.org/ant/2016/10-5/ant-v10-n5-p05-s.pdf#page=18)):
classes independent modulo p in a torsion-free abelian group are
Z-independent. Their *Correction*, ANT 11:4 (2017), Section 1,
pp.1003–1004, DOI 10.2140/ant.2017.11.1003, explicitly retains this lemma
([correction](https://msp.org/ant/2017/11-4/ant-v11-n4-s.pdf#page=239)).
Its valuation-theoretic hypotheses are not hypotheses of this group lemma.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-finite-witness-rational-independence.md`.
The necessary specialization is the finite independence and torsion
check for these exact witnesses, rather than a reproof of that criterion
or a substitution of Cremona's stronger published basis.

**Finite independence in the full rational group.** Put A=E(Q),
G=E(Q_7). The inclusion A -> G induces a linear map A/7A -> G/7G.
In G/7G, L096 gives [R]=0 and L081 gives [P]!=0. Consider integers
u,v with uP+vR in 7A. Localization gives u[P]=0. The nonzero [P]
has order seven because G/7G is killed by seven; hence 7 divides u.
Subtracting uP, which is in 7A, gives vR in 7A. By L097, [R] is
nonzero in A/7A, and thus also has exact order seven. It follows that
7 divides v. This proves injectivity of F_7² -> A/7A for (P,R).

The equality Q=4P+R holds in A itself. Therefore
 aP+bQ=(a+4b)P+bR,
and the coefficient change (a,b) -> (a+4b,b) has determinant one,
both over Z and over F_7. The same injectivity holds for (P,Q).
In particular the global and local uses concern the identical rational
point R, not merely two classes with similar labels.

**Torsion does not account for this independence.** To check this without
any global rank or Sha result, use Silverman VII Propositions 2.1–2.2,
pp.188–191, and IV Theorem 6.4(b) and Remark 6.5, p.132
([reduction](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204),
[logarithm](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150)),
retaining the author's 13 October 2022 errata for pp.130–133 and 185–191.
These are the already assessed local imports of L081. Minimality and
good reduction give kernel U=E_1(Q_7) for G -> E(F_7). Since
1>v_7(7)/(7−1)=1/6, the strict-radius logarithm is a group isomorphism
U -> 7Z_7. If 7^n S=0 in G, its reduction has order dividing both
7^n and 13, so is zero. Thus S lies in U; injectivity of logarithm
and torsion-freeness of 7Z_7 imply S=0. Inclusion A -> G therefore
excludes nonzero rational seven-primary torsion. This is exactly the
local torsion argument isolated in L083, before its global assembly;
none of that assembly is needed here.

By Mordell–Weil and the cited group structure theorem, T=A_tors is
finite and Gamma=A/T is a finitely generated free abelian group.
Since T has no element of order seven, multiplication by seven on T
is injective and hence surjective: T=7T. The quotient map induces
an isomorphism A/7A -> Gamma/7Gamma. Indeed it is surjective; if
 a+T=7(b+T), then a−7b=t in T. Choose s in T with 7s=t.
Then a=7(b+s), proving injectivity. This retains all rational torsion,
without assuming that T is trivial or using a saturation statement.
Consequently the images of P,Q remain independent in Gamma/7Gamma.

**Passage to rational independence.** Gamma is torsion-free, so the
cited Datta–Smith criterion applies with p=7 to those two images.
They are Z-independent in Gamma. Also the structure theorem identifies
A tensor Q with Gamma tensor Q, and Gamma embeds in Gamma tensor Q.
A rational linear relation between P,Q in this tensor product, after
clearing denominators, would be an integer relation between their
images in Gamma, contrary to that independence. Thus their rational
span has dimension two, proving the claimed rank lower bound.

The achieved finite threshold is exactly injectivity on F_7², preserved
through torsion removal; no arithmetic search or new finite calculation
was necessary. This can supply the independent-point premise of L004
for the fixed curve, but all upper-bound hypotheses remain separate.
Uniform production, comparison with arbitrary complex analytic order,
and rationalized strictness remain unresolved. No such downstream
application is performed here.

**Separate critical audit, 2026-10-20 (step 387).** The unchanged
SPECIALIZE assessment above covers this audit. The complete argument
was checked against its precise imported hypotheses, with the following
load-bearing tests. No new arithmetic or general theorem is asserted.

First, the finite test is in the full group A/7A. Given
aP+bQ in 7A, the local equality gives (a+4b)[P]=0. L081's
nonzero class has exact order seven, so write a+4b=7c with c in Z.
Then aP+bQ=7cP+bR, hence bR is in 7A. L097 excludes [R]=0
in A/7A; this quotient is killed by seven, so 7 divides b, and
then 7 divides a. This checks both coefficients directly, agreeing
with the proof's determinant-one change of basis. It never divides a
point by seven in A, assumes localization injective, or infers global
independence merely from one nonzero finite strict class.

The R in both inputs is exactly Q-[4]P on [0,1,1,-2,0]. L096's
audited identity 13(Q-4P) in E_2=7E_1, followed by invertibility of
13 modulo seven, gives its local divisibility. L097's audited full
reduction homomorphism at 23 gives reduction (4,14) outside the complete
seven-multiple image, including hypothetical division points with
nonintegral affine coordinates. These are compatible local and global
statements about the same point. Their existing complete arithmetic
audits are reused; no finite certificate is claimed to have been rerun.

Second, the torsion argument uses only the integral model and reduction
order. L030's invariant calculation gives Delta=389 and minimality;
L033's full table has twelve affine points plus O at seven. Good
reduction therefore makes E_0(Q_7)=G and G/U of order thirteen.
Silverman's strict logarithm theorem applies over Q_7 with normalized
v_7(7)=1 and radius 1>1/6, identifying U with the torsion-free
additive group 7Z_7. Every seven-primary torsion point of G must first
reduce to zero, and is then zero by that logarithm. The inspected
local portion of L083 uses exactly these hypotheses, before its
published-rank and Sha arguments. L096's citation of that portion
introduces neither of those global premises here. The local result
has also been justified explicitly above, so L083 is not a new direct
mathematical input to L099.

Third, Mordell–Weil and the cited structure theorem give finite T
and free Gamma=A/T without specifying the rank. Absence of seven-torsion
makes [7] on T injective; its finite cardinality makes it surjective.
For the induced map A/7A -> Gamma/7Gamma, every target class lifts
from A. If a maps to zero, a=7b+t with t in T=7T, so a is in
7A. This proves both directions of the claimed isomorphism, rather
than silently discarding torsion. It preserves the specific two classes.

Finally, Gamma meets the torsion-free hypothesis of Datta–Smith
Lemma 5.5's pointwise argument. The previously inspected correction
explicitly retains that lemma. The structure theorem also supplies
Gamma -> Gamma tensor Q injective and A tensor Q = Gamma tensor Q
under the natural quotient map. Clearing denominators in a rational
relation therefore produces an actual integer relation in Gamma,
which the cited criterion excludes. No assumed rank enters this step.

The audit passes without a mathematical repair. It establishes the
checked fixed-curve lower-bound input, not a new theorem beyond the
sources assessed. The existing DAG row has exactly the direct inputs
used above; the partial use of L096/L083 must retain its stated local
scope and cannot import their unrelated global conclusions transitively.
No L034 basis, saturation, L082 Sha value or L098 strict-class assembly
was used. The threshold remains two independent rational directions;
no upper-bound application, full kernel, zero-log rational point,
uniform production or arbitrary-curve rank comparison is established.

## Mathlib

Full matching theorem for this exact finite-witness independence
specialization and supporting torsion/group/logarithm declarations:
not checked. No absence claim is made. The general inputs are imported
by the precise citations above; no formal verification is claimed.
