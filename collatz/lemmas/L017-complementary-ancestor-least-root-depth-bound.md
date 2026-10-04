# L017 — Imported complementary ancestor depth bound at a least bad root

## Hypotheses

For positive integers use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

A positive start is nonconvergent if none of its nonnegative shortcut
iterates equals 1. Let

\[
\mathcal B_{20}=\{x>0:x\equiv20\pmod{27},\quad
T^j(x)\ne1\text{ for every }j\ge0\}.
\]

For positive x, \(v_3(x)\) is the largest nonnegative integer e with
\(3^e\mid x\). If any positive start is nonconvergent, L014 supplies
the least element n of \(\mathcal B_{20}\). In this application assume
also \(v_3(4n+1)=3\). No nonconvergent start is assumed to exist
unconditionally.

## Conclusion

The same original least root satisfies

\[
\boxed{v_3(128n-157)\le16.}
\tag{1}
\]

The valuation is of a positive integer. This is a necessary restriction
obtained from the cited complementary-coordinate ancestor theorem. It
does not prove convergence on the complementary domain or establish
descent along the forward orbit of n.

## Proof

### Precise cited ancestor input

Sodelin, *Complementary ancestor cylinders and a second ternary-depth
coordinate*, node `B-SECOND-TERNARY-ANCESTOR-001`,
[section “A uniform family with unbounded new ternary depth,” web lines 30–63 of Complementary_Ancestor_Cylinders.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md#a-uniform-family-with-unbounded-new-ternary-depth),
gives the following guarded theorem for this same shortcut map:

\[
\begin{gathered}
r>0,\qquad r\equiv20\pmod{27},\qquad v_3(128r-157)\ge17\\
\Longrightarrow\quad
\exists m\in\mathbb Z_{>0},\ b\in\mathbb Z_{\ge0}:\quad
m\equiv20\pmod{27},\quad m<r,\quad T^b(m)=r.
\end{gathered}
\tag{2}
\]

Import (2), including integrality, positivity, residue membership,
strict original-root order and the actual forward identity, by citation.
Its full prose proof and essential inverse-word and retained-tail
references were inspected in the prior IMPORT assessment
`drafts/literature/2026-10-04-complementary-valuation-three-ancestors.md`.
The source locates this family inside \(v_3(4r+1)=3\) and
\(v_3(r+7)=4\); it supplies no additional root-size guard. Its strict
slope test is \(768\cdot2^{17}<3^{17}\), with a negative intercept.
This application uses the whole guarded conclusion, rather than treating
that slope alone as an ancestor certificate.

The note was read from live `main` on 2026-10-04, without an immutable
revision identifier. It is an informal public proof input; neither a
local formal build nor a broader Collatz claim from that repository is
assumed. The separately stated fixed cylinders and the source's
valuation-16 selector boundary are outside this application. No selector
reconstruction or reduction of the cited threshold is needed.

### Applicability to the original least root

Suppose any positive start is nonconvergent. L014 makes
\(\mathcal B_{20}\) nonempty, and well-ordering gives its least
element n. Retain the original n throughout. Since n is positive and
\(n\equiv20\pmod{27}\), write \(n=20+27k\) with an integer
\(k\ge0\). In particular,

\[
128n-157=2403+3456k>0,
\tag{3}
\]

so the valuation in (1) is finite. If (1) failed, this integer valuation
would be at least 17. The positivity, residue, and valuation hypotheses
of (2) then hold with \(r=n\). Its integer m and nonnegative integer b
satisfy

\[
m>0,\qquad m\equiv20\pmod{27},\qquad m<n,\qquad T^b(m)=n.
\tag{4}
\]

Minimality of n implies that m converges; otherwise m would be a
smaller member of \(\mathcal B_{20}\). Choose \(j\ge0\) with
\(T^j(m)=1\). If \(j\ge b\), the iteration identity in (4) yields
\(T^{j-b}(n)=1\). If \(j<b\), it instead yields
\(n=T^{b-j}(1)\). As \(T(1)=2\) and \(T(2)=1\), this n lies in
\(\{1,2\}\) and also converges. Either case contradicts
\(n\in\mathcal B_{20}\), proving (1) on the stated valuation-three
domain.

Every comparison is against the original least root. A smaller ancestor
of a larger later return would not suffice for (4). This imports a
conditional necessary restriction, not a result beyond the checked
source, a termination theorem on the surviving roots, or a complete
candidate argument.

## Mathlib

Full complementary-coordinate ancestor theorem and least-root depth
bound: **not checked**. Supporting valuation, congruence, iteration and
well-ordering coverage: **not checked**. No library absence or matching
Mathlib declaration is asserted.

The external declaration
[`CollatzWork.residueAncestor_of_divisibility`](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/ResidueAncestor.lean)
concerns the older guard \(3^{13}\mid4r+1\). It is not a match for
(2) or a locally checked formal dependency. The mathematical input here
is the precisely cited complementary prose theorem.
