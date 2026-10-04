# L018 — Imported fixed complementary-cylinder exclusions at a least bad root

## Hypotheses

For positive integers use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

A positive start is nonconvergent if none of its nonnegative shortcut
iterates equals 1. Put

\[
\mathcal B_{20}=\{x>0:x\equiv20\pmod{27},\quad
T^j(x)\ne1\text{ for every }j\ge0\}.
\]

If any positive start is nonconvergent, L014 supplies the least element
\(n=\min\mathcal B_{20}\). Hold this original n fixed throughout.
No nonconvergent start is assumed to exist unconditionally.

## Conclusion

For every integer \(s\ge0\), the original least root satisfies

\[
\boxed{n\ne4529+19683s\quad\text{and}\quad n\ne17813+59049s.}
\tag{1}
\]

These necessary exclusions are imported by citation. They do not
independently prove convergence of every start in either cylinder or
show that the remaining least-root domain is empty. They impose no
further valuation hypothesis on n.

## Proof

### Precise cited ancestor inputs

Sodelin, *Complementary ancestor cylinders and a second ternary-depth
coordinate*, node `B-SECOND-TERNARY-ANCESTOR-001`,
[section “Two elementary infinite families missed by the original selector,” web lines 9–29 of Complementary_Ancestor_Cylinders.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md#two-elementary-infinite-families-missed-by-the-original-selector),
states the following certificates for this same shortcut map and every
integer \(s\ge0\):

| Root r | Ancestor m | Forward identity |
|---|---|---|
| \(4529+19683s\) | \(3179+13824s\) | \(T^9(m)=r\) |
| \(17813+59049s\) | \(16679+55296s\) | \(T^{11}(m)=r\) |

The cited statement and its guard-propagation proof were read in full
on 2026-10-04 in the prior IMPORT assessment
`drafts/literature/2026-10-04-complementary-valuation-three-ancestors.md`.
Import the actual all-parameter forward identities with their integer
and intermediate admissibility guards, not merely the affine endpoint
formulas. The source was read from live `main`, without an immutable
revision identifier. It is an informal public proof input; no local
formal build or broader Collatz claim is assumed.

### Positive-integer and original-root guards

For the first cylinder, write

\[
\begin{aligned}
r&=27(167+729s)+20,\\
m&=27(117+512s)+20,\\
r-m&=1350+5859s>0.
\end{aligned}
\tag{2}
\]

For the second cylinder, the corresponding equalities are

\[
\begin{aligned}
r&=27(659+2187s)+20,\\
m&=27(617+2048s)+20,\\
r-m&=1134+3753s>0.
\end{aligned}
\tag{3}
\]

Since s is a nonnegative integer, both cases have integral positive
r and m, each congruent to 20 modulo 27, with m strictly smaller than
r. There is no extra lower-size cutoff or parameter parity restriction.
The cited forward time is the nonnegative integer b=9 or b=11.

Suppose n equals one of these r for some allowed s. Apply its
certificate at \(r=n\). Equations (2) or (3) give a positive residue-20
start m<n whose b-th shortcut iterate is this original n. Minimality
of n makes m convergent, since otherwise m would be a smaller member
of \(\mathcal B_{20}\). Choose \(j\ge0\) such that \(T^j(m)=1\).
If \(j\ge b\), then \(T^{j-b}(n)=1\). If \(j<b\), then
\(n=T^{b-j}(1)\in\{1,2\}\), since \(T(1)=2\) and \(T(2)=1\).
Both cases contradict nonconvergence of n, proving (1).

Every strict comparison is with the original least root n. An ancestor
smaller than a larger later return would not justify this contradiction.
The applicability calculation retains all positive offsets and both
orders of an ancestor's hit of 1 and its specified hit of n.

Exact arithmetic checked the coefficient identities in (2) and (3).
Finite replay at s=0,1,2 confirmed the cited times under the local
map convention, solely as a transcription check. The conclusion for
every s uses the inspected source proof by citation. This is
KNOWN_IMPORTED local progress, not a discovery beyond the checked
literature or a complete Collatz candidate.

## Mathlib

Full fixed-cylinder certificates and least-root exclusions: **not
checked**. Supporting congruence, iteration and well-ordering coverage:
**not checked**. No library absence or matching Mathlib declaration is
asserted. The direct source link above is the mathematical citation.
