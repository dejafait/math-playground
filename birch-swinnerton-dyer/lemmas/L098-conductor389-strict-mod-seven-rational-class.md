# L098 — An explicit strict rational Kummer class modulo seven

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x, with Weierstrass coefficients
[0,1,1,-2,0], and put P=(0,0), Q=(1,0), R=Q-[4]P.
Use the audited conclusions of L096 and L097 on this exact model:
R belongs to [7]E(Q_7), but R does not belong to [7]E(Q).
Only L096's local conclusion is used. Its use of L083 is confined to
the local quotient argument with L030, L033 and L081; neither L034's
published rank/basis nor L082's Sha computation is assumed here.

For each place v, including infinity with Q_infinity=R, write
j_v:H^1(Q_v,E[7])->H^1(Q_v,E) for the coefficient-inclusion map.
Use continuous Galois cohomology and define the classical group by

\[
S=\operatorname{Sel}_7(E/\mathbf Q)
 =\{c\in H^1(\mathbf Q,E[7]):j_v(\operatorname{res}_v c)=0
       \text{ for every }v\}.
\]

Define the strict classical mod-seven kernel to be

\[
S^{\mathrm{str}}=\ker\bigl(S\xrightarrow{\operatorname{res}_7}
                         H^1(\mathbf Q_7,E[7])\bigr).
\]

No finiteness of Sha, rational-rank value or saturation premise is used.

## Conclusion

The rational Kummer class

\[
c_R=\delta_{\mathbf Q,7}(R+7E(\mathbf Q))
\]

belongs to S^str and has exact additive order seven. Consequently
its span is a subgroup isomorphic to Z/7Z inside the rational Kummer
image intersected with S^str. This gives one explicit finite-level
class, not an identification of the full strict kernel.

This is a known-method REPRODUCTION with fewer global premises than
L083. The separate critical audit below passes. It supplies no
nonzero Q_7-coefficient strict rational class, rational point of zero
local logarithm, compatible higher-depth classes, uniform production,
or arbitrary-curve BSD rank comparison.

## Proof

**Imported finite Kummer theory.** Use J. S. Milne, *Elliptic Curves*,
second edition (2021), Chapter IV Proposition 1.5 and its connecting
cocycle construction, printed p.108; IV.1.9, pp.110–111; IV Lemma 2.1
(characteristic-zero case), equation (28), p.112; and the global/local
diagram, classical Selmer definition, Lemma 2.2 and equation (29),
pp.112–113, in the [primary text](https://www.jmilne.org/math/Books/EC2.pdf).
The prior assessment is
`drafts/literature/2026-10-20-strict-mod-seven-rational-class.md`.
These inputs are imported, not reproved.

For K=Q or any Q_v, these statements give an injective homomorphism

\[
\delta_{K,7}:E(K)/7E(K)\hookrightarrow H^1(K,E[7]),
\]

whose image is the kernel of H^1(K,E[7])->H^1(K,E).
All these fields have characteristic zero, including Q_7 and R.
Thus geometric multiplication by seven is surjective as required;
there is no prime-to-residue-characteristic restriction at seven.
Naturality gives, for every v,

\[
\operatorname{res}_v(c_R)
 =\delta_{\mathbf Q_v,7}(R+7E(\mathbf Q_v)).                 \tag{1}
\]

**Global order.** L097 states that R is not in 7E(Q), using the complete
good-reduction witness at 23. Hence its global quotient class is nonzero,
and injectivity of delta_Q,7 makes c_R nonzero. The point quotient is
killed by seven: 7(R+7E(Q))=0. Since the Kummer map is a homomorphism,
7c_R=0. A nonzero element killed by the prime seven has exact order
seven, proving the order assertion without a rank or basis computation.

**Every classical condition.** For each v the right side of (1) lies
in the kernel of j_v by local Kummer exactness. Therefore
j_v(res_v(c_R))=0 at every place, so c_R belongs to S. This argument
includes bad primes, seven and the real place; no ordinary, unramified
or relaxed condition replaces the classical one, and no local image
computation at those other places is needed for a global rational point.

**Strictness in the torsion coefficient group.** L096 states that
R is in 7E(Q_7). Its local point quotient class is consequently zero.
Equation (1) with v=7 gives res_7(c_R)=delta_Q_7,7(0)=0 in
H^1(Q_7,E[7]), proving membership in S^str. The restriction is zero
before applying j_7. Vanishing only after j_7 would be the automatic
classical Selmer condition and would not prove strictness.

Together with nontriviality and exact order, this proves the conclusion.
Only L096 and L097 are direct mathematical inputs beyond the cited
standard Kummer theorem. No global conclusion of L083 is activated.
The finite relation R in 7E(Q_7) says neither that its logarithm is zero
nor that a rationalized strict class is nonzero, so L005 is not applicable
on the strength of this conclusion. The main BSD gap remains open.

**Separate critical audit (2026-10-20, step 384).** The audit uses the
preexisting SPECIALIZE assessment
`drafts/literature/2026-10-20-strict-mod-seven-class-critical-audit.md`.
It checks this assembly, importing the separately audited arithmetic
conclusions rather than rerunning their certificates. No arithmetic
defect requiring an upstream replay was found.

The hypotheses match exactly: both L096 and L097 use
[0,1,1,-2,0], P=(0,0), Q=(1,0), R=Q-[4]P and scalar seven.
L096's equivalence at (a,b)=(-4,1) supplies R in 7E(Q_7).
L097 supplies nonmembership in 7E(Q), with reduction defined on the
entire local group at 23, including hypothetical division points with
nonintegral coordinates. These are compatible assertions over different
fields, not contradictory tests in one quotient.

Global injection in the cited Milne equation (28) is applied to the
nonzero class in E(Q)/7E(Q), not to a class in E(Q_7)/7E(Q_7).
Multiplication by seven kills that global quotient. Thus the resulting
cohomology element is nonzero and killed by seven; primality excludes
every smaller positive order. Neither absence of rational torsion nor
a saturated basis is needed for this exact-order inference.

The naturality diagram is applied separately at every place to this
same global rational point. Local exactness gives membership in the
classical Kummer image at bad primes, at seven and at infinity as well
as at other finite primes. Its hypotheses are characteristic zero
for Q and each Q_v, not residue characteristic different from seven.
There is no omitted ramification condition or change to ordinary or
relaxed Selmer conventions. At seven the local point quotient is zero,
so the restriction itself is zero in H^1(Q_7,E[7]). Only for the
other classical membership assertions is coefficient inclusion j_v
used. Testing j_7 alone would fail this audit, but the proof does not
make that substitution.

The restricted local input was checked against L083's proof paragraphs
"The entire local quotient at every depth" and "The actual point
generates at every depth", and L096's applicability audit. They use
the good reduction group of order thirteen, the strict-radius formal
logarithm and L081's valuation-one value; their local quotient and
generation arguments precede L083's global Kummer identification.
No conclusion from L034 or L082 is used here. The direct inputs
remain L096 and L097, so the DAG needs no change.

The critical audit passes without a mathematical correction. This
validates the existing fixed application of known Kummer theory; it
establishes no new general theorem. No map from this finite class into
a nonzero Q_7-coefficient class is supplied. Higher-depth compatibility,
the full strict kernel and the arbitrary-curve rank comparison remain
outside the conclusion. The existing Mathlib qualification is unchanged.

## Mathlib

Full matching coverage and supporting finite Kummer injection,
localization naturality and classical Selmer theorem names: not checked.
No absence claim is made. The general theory is imported from Milne;
the fixed specialization is the assembly above.
