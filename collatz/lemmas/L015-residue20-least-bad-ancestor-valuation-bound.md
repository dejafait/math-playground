# L015 — Imported ancestor valuation bound for a least bad residue-20 root

## Hypotheses

For positive integers use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

A positive start is nonconvergent if none of its nonnegative shortcut
iterates equals 1. As in L014, let

\[
\mathcal B_{20}=\{x>0:x\equiv20\pmod{27},\quad
T^j(x)\ne1\text{ for every }j\ge0\}.
\]

For positive x, \(v_3(x)\) is the largest nonnegative integer e with
\(3^e\mid x\). The conclusion is conditional; no nonconvergent start
is assumed to exist unconditionally.

## Conclusion

If any positive start is nonconvergent, L014 makes \(\mathcal B_{20}\)
nonempty. Its least element n satisfies

\[
\boxed{v_3(4n+1)\le12.}
\tag{1}
\]

This is the least-root application of a cited guarded ancestor theorem.
It does not establish convergence on the complementary domain or
descent along the forward orbit of n.

## Proof

### Precise cited ancestor input

Sodelin, *Refined tail certificates lower the uniform ancestor cutoff to
valuation 13*, node `B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05`,
[sections 1–3 and 5 of Residue20_Refined_Ancestor.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md),
gives the following theorem for this same positive shortcut map:

\[
\begin{gathered}
r>0,\qquad r\equiv20\pmod{27},\qquad v_3(4r+1)\ge13\\
\Longrightarrow\quad
\exists m\in\mathbb Z_{>0},\ b\in\mathbb Z_{\ge0}:\quad
m\equiv20\pmod{27},\quad m<r,\quad T^b(m)=r.
\end{gathered}
\tag{2}
\]

Import (2), including positivity, integrality, residue membership,
strict order and the actual forward identity, by citation. An affine
formula with no admissibility guards would not suffice. The full prose
proof and its essential retained-branch reference were read on
2026-10-04 in the saved assessment
`drafts/literature/2026-10-03-residue20-residual-ancestor-selector.md`.
It records the source's scope and qualifications. The note was read
from live `main`; the node date is not an immutable revision, and no
independent Lean build or general Collatz claim is an input here.

The cited cutoff is sufficient on the whole stated high-valuation
domain, with no additional lower bound on r. Its lower-row refinements
and its valuation-12 selector failure are outside this application.
The source's ancestor theorem, rather than a reconstruction of its
inverse-word proof, is the known mathematical input.

### Applicability and convergence transfer

Suppose any positive start is nonconvergent. L014 proves
\(\mathcal B_{20}\ne\varnothing\), so take its least element n.
Keep this original root fixed. Then \(n>0\),
\(n\equiv20\pmod{27}\), and \(4n+1>0\), so its valuation is finite.
If (1) failed, that integer valuation would be at least 13; equivalently,
\(3^{13}\mid4n+1\). All the hypotheses of (2) therefore hold with
\(r=n\). It supplies positive integers m and a finite nonnegative
time b such that

\[
m\equiv20\pmod{27},\qquad m<n,\qquad T^b(m)=n.
\tag{3}
\]

Minimality of n implies that m converges: otherwise it would be a
smaller member of \(\mathcal B_{20}\). Choose \(j\ge0\) with
\(T^j(m)=1\). If \(j\ge b\), the iteration identity in (3) gives
\(T^{j-b}(n)=1\). If \(j<b\), it gives
\(n=T^{b-j}(1)\). Since \(T(1)=2\) and \(T(2)=1\), this n belongs
to \(\{1,2\}\) and also converges. Both cases contradict
\(n\in\mathcal B_{20}\), proving (1).

The comparison \(m<n\) is against the original least root. An ancestor
of a larger later return would not give this comparison. The argument
imports a conditional necessary restriction and leaves universal
convergence on the remaining infinite class unresolved; it supplies
no new result beyond the checked source.

## Mathlib

Full ancestor theorem and least-bad-root bound: **not checked**.
Supporting iteration, valuation and well-ordering coverage: **not
checked**. No absence from Mathlib is inferred.

The inspected external declaration
[`CollatzWork.residueAncestor_of_divisibility`](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/ResidueAncestor.lean)
matches the cited ancestor conclusion with guard \(3^{13}\mid4r+1\).
It is not a Mathlib coverage claim or a locally checked Lean dependency;
the mathematical input here is the prose theorem cited above.
