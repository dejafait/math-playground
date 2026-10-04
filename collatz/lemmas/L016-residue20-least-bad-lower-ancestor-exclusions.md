# L016 — Imported lower-row exclusions for a least bad residue-20 root

## Hypotheses

For positive integers use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Let

\[
\mathcal B_{20}=\{x>0:x\equiv20\pmod{27},\quad
T^j(x)\ne1\text{ for every }j\ge0\}.
\]

If any positive start is nonconvergent, take
\(n=\min\mathcal B_{20}\), whose existence is part of L015. Define

\[
v=v_3(4n+1),\qquad u=(4n+1)/3^v,\qquad
t=2^{v-2}u\bmod9\in\{1,2,4,5,7,8\}.
\]

The residue representative t is chosen in \(\{0,\ldots,8\}\).
For \(t=4\), also put \(z=3\cdot2^{v-2}u-1\).
No existence of a nonconvergent start is assumed unconditionally.

## Conclusion

The original least root must satisfy \(3\le v\le12\) and one of the
following rows:

| t | Additional guard | Necessary upper bound on v |
|---|---|---:|
| 1 | none | 12 |
| 2 | none | 6 |
| 5 or 8 | none | 10 |
| 7 | none | 3 |
| 4 | \(z\equiv38\pmod{81}\) | 5 |
| 4 | \(z\equiv65\pmod{81}\) | 6 |
| 4 | \(z\equiv11\pmod{243}\) | 7 |
| 4 | \(z\equiv92\pmod{243}\) | 10 |
| 4 | \(z\equiv173\pmod{243}\) | 5 |

In particular, \(v\in\{11,12\}\) forces \(t=1\). The table is only
the complement of the cited guarded ancestor families within L015's
valuation range. Membership does not imply nonconvergence or absence
of some other smaller ancestor. These rows leave valuation 3
unexcluded and supply no termination theorem on the residual domain.

## Proof

### Cited guarded inputs

Sodelin, *Refined tail certificates lower the uniform ancestor cutoff to
valuation 13*, node `B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05`,
[sections 1–3 of Residue20_Refined_Ancestor.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md),
and its retained construction, *An explicit smaller residue-20 ancestor
for every sufficiently deep 3-adic root*, node
`B-RESIDUE20-VALUATION-ANCESTOR-2026-09-05`,
[sections 1–4 of Residue20_Valuation_Ancestor.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Valuation_Ancestor.md),
give the following guarded statements for this same map and these same
definitions of v, u and t. For a positive \(r\equiv20\pmod{27}\), any
one of the listed conditions supplies

\[
\exists m>0,\ b\ge0:\quad
m\equiv20\pmod{27},\qquad m<r,\qquad T^b(m)=r,
\tag{1}
\]

where m and b are integers:

- \(t=2\) and \(v\ge7\);
- \(t\in\{5,8\}\) and \(v\ge11\);
- \(t=7\) and \(v\ge4\);
- \(t=4\), with \(z=3\cdot2^{v-2}u-1\), and respectively
  \(z\equiv38\pmod{81}, v\ge6\),
  \(z\equiv65\pmod{81}, v\ge7\),
  \(z\equiv11\pmod{243}, v\ge8\),
  \(z\equiv92\pmod{243}, v\ge11\), or
  \(z\equiv173\pmod{243}, v\ge6\).

Import (1) with all its guards, not merely an affine endpoint formula.
The source proofs verify the intermediate inverse operations, their
forward orientation, positivity, residue membership, and strict order
against r. Each listed valuation threshold is within their stated
\(v\ge4\) domain. The retained \(t=1,v\ge13\) case is already excluded
by L015 and is not reapplied here. No source assertion about lower
valuation termination is imported.

Both prose proofs were read in the saved IMPORT assessment before this
turn. The exact tables were retrieved again on 2026-10-04 for this
application, without changing that assessment or its scope. The notes
were read from live `main`; their node dates are not immutable revisions.
The individually sharper lower thresholds are prose inputs, not claims
of a local Lean build or coverage by the public uniform-cutoff theorem.

### Applicability to the original root

L015 supplies the least root and \(v\le12\). Since
\(n\equiv20\pmod{27}\), \(4n+1\equiv0\pmod{27}\), so \(v\ge3\).
The definition of the valuation makes u a positive integer coprime to 3.
It is odd because \(4n+1\) and \(3^v\) are odd. Hence t is one of
the six nonzero unit residues modulo 9. These are exactly the source's
root, valuation, and unit hypotheses.

Suppose n satisfies one of the cited guarded conditions. Apply (1)
with \(r=n\); its m is a positive residue-20 start with \(m<n\).
Minimality therefore makes m convergent. Choose \(j\ge0\) with
\(T^j(m)=1\). If \(j\ge b\), then \(T^{j-b}(n)=1\). If \(j<b\),
then \(n=T^{b-j}(1)\in\{1,2\}\), since these two states form the
shortcut cycle, and n also converges. Either case contradicts
\(n\in\mathcal B_{20}\). Consequently no listed condition can hold
at the least root. This uses only \(m<n\); n is never replaced by a
later return or by an intermediate inverse state.

For \(t=4\), the definition gives
\(z\equiv3t-1\equiv11\pmod{27}\). Thus modulo 81 it is 11, 38, or
65. The first of these splits modulo 243 into 11, 92, or 173. The
five stated guards therefore partition this t case. In each cylinder,
negating its integer valuation threshold gives the corresponding upper
bound in the conclusion. Negating the retained thresholds gives the
other rows; \(t=1\) keeps only L015's bound. This proves the table and
its \(v\in\{11,12\}\) consequence.

The only new local input is the application of these already covered
source conclusions. It is KNOWN_IMPORTED, not a result beyond the
checked literature. A smaller ancestor of a larger returned value
would not suffice, and no such comparison is used.

## Mathlib

Full guarded lower-row exclusions and supporting valuation, congruence,
iteration and well-ordering coverage: **not checked**. No Mathlib
absence or matching theorem name is asserted.

The external declaration
[`CollatzWork.residueAncestor_of_divisibility`](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/ResidueAncestor.lean)
matches the uniform valuation-at-least-13 input in L015. It does not
assert the sharper lower rows used here and is not a Mathlib coverage
claim or a locally audited formal dependency.
