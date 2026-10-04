# L014 — Imported residue-20 least-bad-root restriction

## Hypotheses

For positive integers use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Call a positive start nonconvergent if no nonnegative iterate equals 1.
Let

\[
\mathcal B_{20}=\{n>0:n\equiv20\pmod{27},\quad
T^j(n)\ne1\text{ for every }j\ge0\}.
\]

For a positive integer x, \(v_3(x)\) is the largest nonnegative integer
e such that \(3^e\mid x\). No existence of a nonconvergent start is
assumed unconditionally.

## Conclusion

If any positive start is nonconvergent, then \(\mathcal B_{20}\) is
nonempty. If \(n=\min\mathcal B_{20}\), then

\[
\boxed{v_3(n+7)\in\{3,4\}.}
\tag{1}
\]

The restriction is imported from the cited predecessor reduction, with
its local applicability checked below. It leaves an infinite arithmetic
class unresolved and proves no forward descent from n or global
termination of successive target visits.

## Proof

### Citation and scope of the applicability check

Sodelin, *Ternary predecessor normalization removes F026, but a stronger
core obstruction survives*, node `AB-CORE-RESIDUE-OBSTRUCTION-001`,
[section 6, raw lines 204–239](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/AB_ternary_normalized_core_residue_obstruction.md),
states the reduction

\[
y\equiv236\pmod{243}\quad\Longrightarrow\quad
c(y)=\frac{8y-7}{9}<y,\qquad c(y)\equiv20\pmod{27},
\qquad T^3(c(y))=y,
\tag{2}
\]

and the reduction of \(v_3(y+7)\) by two, terminating at valuations 3
or 4 for residue-20 starts. The live Markdown was read on 2026-10-03
in the prior assessment. It is an informal public note; no immutable
revision of the note or general certificate is assumed. Its recorded
reviewed-input hash is not asserted to identify the note itself.

This is a known imported input, not a new inverse-word theorem.
Because the source is terse, the necessary positive-integer, parity,
residue, and least-root guards are checked explicitly. No broader
selector or rank assertion from that repository is used.

### Positive integer guards for the cited predecessor

Write \(y=243k+236\). Positivity of y implies \(k\ge0\). Formula (2)
gives

\[
c(y)=216k+209=27(8k+7)+20>0,
\qquad y-c(y)=27(k+1)>0.
\tag{3}
\]

In particular c(y) is an integer in the required starting class and
is strictly smaller than y. The actual shortcut path is

\[
216k+209\ \longmapsto\ 324k+314\ \longmapsto\
162k+157\ \longmapsto\ 243k+236.
\tag{4}
\]

The three input parities are odd, even, odd, respectively. Substitution
into the corresponding shortcut branches proves every arrow for all
\(k\ge0\), with all positive offsets retained. Thus (4) verifies the
sourced identity on exactly its stated integer domain.

For a residue-20 y, \(v_3(y+7)\ge3\). In this domain

\[
v_3(y+7)\ge5\quad\Longleftrightarrow\quad
y\equiv236\pmod{243}.
\tag{5}
\]

For (5)'s guarded y,

\[
c(y)+7=\frac{8(y+7)}9,
\qquad v_3(c(y)+7)=v_3(y+7)-2,
\tag{6}
\]

since 3 does not divide 8. Equations (3)–(6) check the source rule's
positivity, membership and valuation guard; repeated normalization is
not needed for the least-root argument.

### Nonemptiness and the fixed least root

Suppose x is a nonconvergent positive start. L013 gives a finite shortcut
hit y of \(\{1,2\}\) or residue 20 modulo 27. A hit of 1 or 2 would
make x converge, since \(T(2)=1\). Likewise, if y converged, its finite
path to 1 could be appended to the path from x. Therefore
\(y\in\mathcal B_{20}\), proving nonemptiness. Well-ordering of the
positive integers gives its least element n.

Now hold that n fixed. Membership gives \(v_3(n+7)\ge3\). If this
valuation were at least 5, (3)–(5) would give a positive residue-20
start \(c(n)<n\) whose third shortcut iterate is n. By minimality,
c(n) must converge. If it first reached 1 at a time \(j\ge3\), then
\(T^{j-3}(n)=1\). If it reached 1 at a time \(j<3\), its third iterate
would be in the shortcut cycle \(\{1,2\}\), and would also converge.
Either case contradicts \(n\in\mathcal B_{20}\). Hence the valuation
cannot be at least 5, and (1) follows.

This compares c(n) with the original least root n. Applying c to a
later returned value y would only give c(y)<y, which need not give
c(y)<n. No such replacement is made. The proof establishes a necessary
condition on a hypothetical least bad root; the convergence of the
remaining roots is still missing.

## Mathlib

Full residue-20 predecessor and least-bad-root restriction: **not
checked**. Supporting valuation, congruence, iteration and well-ordering
results: **not checked**. No library absence or matching theorem name
is asserted. The direct source link above is the mathematical citation,
not a claim of Mathlib coverage.
