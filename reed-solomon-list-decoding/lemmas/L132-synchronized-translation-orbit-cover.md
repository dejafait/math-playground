# L132 — An exact cover of the synchronized translation orbit

## Hypotheses

Use L131's fixed auxiliary field F_q with q=137, its two complete
bijections sigma and sigma', and its cores C,C'. Let Q=F_q[Z]_{<=2}.
Write f=u+vZ+wZ^2 and r=Z-16. Every residue used in a congruence
modulo 4 below means its unique integer representative in {0,...,136};
this congruence is not an operation in F_q.

There are separate left and right copies of Q. A synchronized candidate
indexed by f has vertices L_f,L_(f+r),R_f,R_(f+r), representing, in order,
C union sigma(B_f), C union sigma(B_(f+r)), C' union sigma'(B_f), and
C' union sigma'(B_(f+r)). The accepted witness collection is any subset
of these candidates, including precisely the collection that passes
all of L031's incidence hypotheses and has signed rank twelve at the
original labels. No translation invariance of those tests is assumed.

The required retention on each side is 1532496, so the allowed deletion
budget on each copy of Q is q^3-1532496=1038857.

## Conclusion

The following complete finite deletion rules hit every synchronized
candidate, hence every accepted witness:

\[
 D_L=\{u+vZ+wZ^2:[v]_{137}\equiv0\pmod4\},\qquad
 D_R=\{u+vZ+wZ^2:[v]_{137}\equiv2\pmod4\}.
\]

Their sizes are respectively 656915 and 638146. Thus both fit the
deletion budgets, leaving respectively 1914438 and 1933207 indices,
each strictly more than 1532496, with no accepted synchronized witness
fully retained. The result holds in particular for L131's unchanged
maps; it does not require incidence or rank enumeration.

This is a cover of a selected witness collection, not a pair of packed
families. No cross-packing, absence of other four-support witnesses,
common-center realization, arbitrary-map assertion, unsafe RS list or
change of the 955–957 bracket is claimed.

## Proof

**Coverage and use of existing results.** The invocation-start EXPLORE
[assessment](../drafts/literature/2026-10-26-synchronized-translation-witness-cover.md)
explicitly permits a structural cover proof instead of enumeration.
Its primary-source comparison supports L031's signed-rank obstruction,
but imports no orbit-expansion assertion. L131 supplies the fixed
ambient family model. Only its bijections and graph definitions are
needed here; no new rank assertion or reproof of the cited obstruction
is used. The difference addressed is the exact Boolean cover of this
particular synchronized collection. The calculation below certifies
complete finite rules, rather than a fractional or sampled cover.

**Every candidate is hit.** Adding r sends the coefficient triple
(u,v,w) to (u-16,v+1,w), with all three operations in F_137. Put
t=[v]_{137}. If t is even, the endpoint f itself is deleted on one
side: when t is 0 modulo 4 it lies in D_L, and when t is 2 modulo 4
it lies in D_R. Both L_f and R_f occur in the candidate, so either
deletion suffices.

If t is odd, then t<=135. Consequently [v+1]_{137}=t+1 is an even
integer with no wraparound. Apply the preceding even-coefficient rule
to f+r: it belongs to D_L or D_R, and the corresponding vertex
L_(f+r) or R_(f+r) occurs in the candidate. The only wraparound case,
t=136, was already covered by the even case. These two cases exhaust
all 137 possible v. The constants u and w were arbitrary throughout.
Hence every one of the q^3 candidates is hit, regardless of the
actual-label incidence test or signed rank. Taking a subset of the
candidates cannot invalidate this certificate. In particular, the
imported zero-translation witness is hit by deleting L_0.

**Exact resource check.** The integer representatives congruent to 0
modulo 4 are 0,4,...,136, exactly 35 values. Those congruent to 2
modulo 4 are 2,6,...,134, exactly 34 values. Each allows all q^2=18769
choices of (u,w), so

\[
\begin{aligned}
|Q|&=137^3=2571353,\\
|D_L|&=35\cdot18769=656915<1038857,\\
|D_R|&=34\cdot18769=638146<1038857,\\
|Q\setminus D_L|&=2571353-656915=1914438>1532496,\\
|Q\setminus D_R|&=2571353-638146=1933207>1532496.
\end{aligned}
\]

These are exact counts of indices. They are also counts of distinct
supports on the respective sides: two distinct degree-at-most-two
auxiliary polynomials cannot agree at all seven distinct points of T,
by the polynomial root bound. Thus their graph blocks differ. Applying
an injective map preserves that difference, and adjoining a core
disjoint from its image preserves it again. This uses no arithmetic
preservation by sigma or sigma'.

The proof is a full symbolic certificate of all witness hits and all
resource bounds. There is no sampled check, solver conclusion or
uninspected list of ranks behind the result. Enumeration of accepted
witnesses would be redundant for this stronger all-candidate cover.
No mathematical script or numerical certificate is required.

**Decision and limits.** Since a cover within both budgets exists,
the synchronized orbit alone cannot force a witness from retention
alone at the stated threshold. This meets the assessed abandonment
test for that amplification. The retained sets have not been checked
for cross-packing, so they do not refute a claim with that additional
hypothesis. Independently translated pairs, other witnesses, arbitrary
maps and a global RS list bound are outside this statement.

## Mathlib

Full and supporting Mathlib coverage: not checked. The argument uses
only finite coefficient counting, parity of integer representatives,
and the elementary polynomial root bound; no Mathlib absence is claimed.
