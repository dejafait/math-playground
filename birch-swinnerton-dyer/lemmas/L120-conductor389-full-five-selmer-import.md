# L120 — Published full 5-Selmer dimension for the conductor-389 curve

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x, with Weierstrass coefficients
[0,1,1,-2,0]. Use the full classical multiplication-by-5 Selmer group,
with the local Kummer condition at every place, including the real place,
as in foundations/02. Import the published computational arithmetic
results cited below. Their original executions are not independently
replayed here. Neither BSD nor finiteness of the whole Sha is assumed.

## Conclusion

The rational torsion correction is t=dim_F5 E(Q)[5]=0, and

\[
E(\mathbf Q)/5E(\mathbf Q)\xrightarrow{\sim}
\operatorname{Sel}_5(E/\mathbf Q)\cong(\mathbf F_5)^2,
\qquad \dim_{\mathbf F_5}\operatorname{Sel}_5(E/\mathbf Q)=2.
\]

The first arrow is the rational Kummer map; the identification with
(F_5)^2 uses a choice of basis. This supplies the
bound b=2=k+t for the Selmer input of L119 with k=2; it does not supply
its absolute height approximations or determinant test. This is a local
application of known arithmetic results, not a new arithmetic discovery
or a BSD candidate. The separate step-503 critical audit below passes
with the original published computations still unreplayed.

## Proof

**Exact model and published rational group.** L030 supplies the globally
minimal model with discriminant and conductor 389. The coefficient
convention y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6 gives exactly the
displayed equation from [0,1,1,-2,0]. J. E. Cremona, *Algorithms for
Modular Elliptic Curves*, corrected online second edition (CUP, 1997),
[Table 1, printed p.157, row 389A1](https://johncremona.github.io/book/fulltext/table1.pdf#page=49),
lists this coefficient vector, arithmetic rank 2 and rational torsion
order 1. The [column definitions, printed p.109](https://johncremona.github.io/book/fulltext/table1.pdf#page=1)
identify r and |T| as those arithmetic invariants, rather than an analytic
rank or conjectural Sha value. Table 2, printed pp.255 and 257, gives
the rational generators (0,0),(1,0) on the same model. L034 records the
assessed group-result provenance and the match between 389A1, 389a1 and
the author's 389a example. No isomorphism is inferred just from conductor
and rank. Importing the rank and torsion entries gives
E(Q) isomorphic to Z^2, hence E(Q)[5]=0. No saturation claim about a new
point list is required for this group quotient.

**Arithmetic Sha input and prime applicability.** William Stein and
Christian Wuthrich, *Algorithms for the arithmetic of elliptic curves
using Iwasawa theory*, Math. Comp. **82** (2013), 1757--1792,
DOI 10.1090/S0025-5718-2012-02649-4,
[Theorem 12.3, printed p.1788](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32),
proves Sha(E/Q)[p]=0 for the curve identified immediately before it as
389a, at every good ordinary prime p<48859 except 16231 (and separately
at 2). The model identification above matches this curve.

Here 5 does not divide the minimal discriminant 389, so reduction is
good. For completeness the right sides x^3+x^2-2x for x=0,1,2,3,4
modulo 5 are respectively 0,0,3,0,2. The numbers of solutions of
y^2+y to these values are 2,2,0,2,2, since its values for y=0,1,2,3,4
are 0,2,1,2,0. Including the unique point at infinity gives #E(F_5)=9
and a_5=5+1-9=-3. The ordinary reduction criterion at a good prime is
p not dividing a_p; it holds here. Also 5<48859 and 5 is not 16231.
Thus the cited theorem supplies Sha(E/Q)[5]=0 at the required prime.

This imports the theorem's proved torsion assertion, not the adjacent
congruence involving a conjectural BSD order. Its proof refers to the
completed computations of Section 12.4, printed pp.1787--1788, using
Algorithm 11.1 and its ordinary proof case, printed pp.1783--1784.
General conjectural termination of that algorithm is not a hypothesis
of this completed theorem. The source assessment and inspected proof
coverage are in drafts/source-notes/2026-10-26-conductor389-full-five-selmer-coverage.md.
The regulator, residual-representation and leading-term computations
are accepted as part of the published theorem, not reverified here.
In particular this import does not rederive the theorem from the printed
sigma formula disputed in ATTEMPTS/057 or resolve that discrepancy.

**Full Kummer specialization.** L001, with its arithmetic Kummer input
from J. S. Milne, *Elliptic Curves*, second edition (2021), Chapter IV,
equation (29), printed p.113, and Theorem IV.3.1, printed p.114, applies
with B=E(Q), p=5 and n=1. Explicitly it gives the exact sequence

\[
0\longrightarrow E(\mathbf Q)/5E(\mathbf Q)
\longrightarrow\operatorname{Sel}_5(E/\mathbf Q)
\longrightarrow\Sha(E/\mathbf Q)[5]\longrightarrow0.
\]

The final term is zero by the imported theorem, so the Kummer map is
an isomorphism. The group quotient of Z^2 by multiplication by 5 is
(Z/5Z)^2. The maps come from E[5] and are F5-linear; consequently the
isomorphism gives the asserted dimension, not merely a cardinality bound.
Equivalently L001's torsion-corrected order is
|Sel_5|=5^2 |E(Q)[5]| |Sha[5]|=25. Both latter factors equal 1.
No isogeny-Selmer group or marked subspace replaces the full Selmer group.
No assumption about other primary components of Sha enters this argument.

**Scope and test.** The model, ordinary prime, arithmetic Sha result and
torsion correction meet the approved import test; the achieved full
dimension equals the required threshold 2. L119 is a possible consumer,
not a premise. Independent original arithmetic replay would be a separate
target. Repeating a conditional full-descent interface or a stopped
p=7 scalar test would not supply this input; ATTEMPTS/032/034 remain
preserved. Eligible-point and absolute canonical-height certificates
for L119, uniform production and arbitrary complex-order comparison
remain unresolved by this import.

**Separate critical audit, 2026-10-26 (step 503).** The approved
SPECIALIZE audit passes as a cited-result application. It repairs the
conclusion's direction wording: the Kummer arrow goes from E(Q)/5E(Q)
to Sel_5, whereas the original displayed order had listed Sel_5 first.
The exact sequence in the original proof already had the correct direction;
no dimension or arithmetic conclusion changes.

For the model check, substituting the five Weierstrass coefficients gives
the stated equation. L030's invariant calculation gives b_2=4, b_4=-4,
b_6=1, b_8=-3 and Delta=48+512-27-144=389. In particular 5 does not
divide Delta. L030's minimality argument is valid because its local
valuations are zero or one, while any decrease between integral models
would be a positive multiple of twelve. The reopened Table 1 definitions
(p.109) and exact conductor-389 row (p.157) give this coefficient vector,
r=2 and |T|=1. L034's assessed author-data correspondence identifies
389A1 with 389a1; the book's conductor block contains one isogeny class
and one curve. Thus the source's 389a is matched by its actual model
and label provenance, not by rank and conductor alone. The Table 2
definition and p.257 entry agree with the recorded two generators;
only rank and torsion, not their saturation, are needed for this quotient.
The PDF screenshot request supplied no inspectable image, so this audit
uses extracted text and the existing assessed label evidence.

The complete affine point list modulo five is
(0,0), (0,4), (1,0), (1,4), (3,0), (3,4), (4,1), (4,3).
Indeed the right-side residues are 0,0,3,0,2, and the fibers of y^2+y
above 0,1,2,3,4 are respectively {0,4}, {2}, {1,3}, empty, empty.
This exhausts all five x and y residues. The projective equation has
exactly one point at infinity: at Z=0 it forces X=0, giving [0:1:0].
Thus #E(F_5)=8+1=9, a_5=-3 and 5 does not divide a_5. Good ordinary
reduction, the bound 5<48859 and the exclusion 5!=16231 all pass.
This elementary enumeration audits the local specialization, not the
published regulator or descent execution.

The reopened Theorem 12.3 and its complete proof (p.1788) assert
arithmetic Sha[p] vanishing in that range, separately from the conjectural
order congruence. Algorithm 11.1 and its ordinary proof (pp.1783--1784)
require p>2, nonadditive reduction and residual surjectivity; their
completed upper bound uses established regulator nondegeneracy and
Kato's divisibility. Proposition 11.2's conjectural general success is
not an extra premise of Theorem 12.3. This audit imports that theorem,
not a new run of Algorithm 11.1. Residual surjectivity and the numerical
regulator/leading-term work remain within the cited computational input.
The unresolved printed sigma discrepancy in ATTEMPTS/057 is neither
used to reconstruct that computation nor claimed resolved.

Finally, foundations/02 and L001 use the full multiplication-by-5 Kummer
conditions at every place. The rational Kummer class has local image in
the local Kummer subgroup, so lies in this Selmer group. The exact
sequence's last term is the kernel of multiplication by 5 in the full
Sha, not a quotient or an assumed finite Sha. Its vanishing makes the
injective Kummer map surjective. All three groups are killed by 5,
and the homomorphisms commute with integer multiplication, hence are
F_5-linear. From the independently cited E(Q) isomorphic to Z^2, the
rational quotient is (Z/5Z)^2, and E(Q)[5] is zero.
Consequently the achieved full dimension b=2 equals the required k+t=2;
no marked subspace, isogeny-Selmer dimension or analytic rank is used.
The F_5-basis identification is not claimed canonical.

The direct local inputs remain L001, L030 and L034. Only L034's published
group provenance is used, not its p=7 height or Iwasawa conclusions.
L082 is a distinct p=7 specialization, not an extra premise; L119 is a
possible consumer, not a premise. The existing DAG row is therefore
unchanged. This establishes the local audit verdict, with no new
arithmetic beyond the cited sources. Absolute point-height values and
the strict determinant test, a uniform producer, and comparison with
arbitrary complex analytic order remain unresolved. ATTEMPTS/032/034/057
and the original computational qualifications remain in force.

## Mathlib

Full matching coverage for the exact-curve arithmetic theorem and full
5-Selmer isomorphism: **not checked**. Supporting Kummer, finite-group,
ordinary-reduction and vector-space results: **not checked**. No absence
claim is made. This is an informal cited-result specialization, with the
published computations explicitly unreplayed.
