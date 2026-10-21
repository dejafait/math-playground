# L033 — Strict logarithmic clocks below 1/log(6) fail on residue 47

## Hypotheses

For positive integers use the shortcut map T(n)=n/2 for even n and
T(n)=(3n+1)/2 for odd n. Let S be the positive integers congruent to
20 modulo 27. Fix real numbers 0<C<1/log(6) and B>=0, with natural
logarithms. Both clocks count shortcut steps and include zero.
No convergence or least-nonconvergent-root assumption is made.

## Conclusion

There are unbounded odd positive integers n=47+243k, k>=0, with
v_2(n+1)=4, for which no positive c in S and nonnegative integers s,t
satisfy

\[
c<n,\qquad s,t\le C\log(n)+B,\qquad T^s(c)=T^t(n).
\]

More precisely, set delta=1-C log(6)>0 and

\[
L_0=\max\left(6,\left\lceil
\frac{C\log(163)+B}{\delta}\right\rceil\right).
\]

For every integer L>=L_0 such a root can be selected with
4^L<n_L<=4^L+162*6^L<163*6^L. Thus this two-clock companion cover
fails outside every finite base for each fixed admissible C,B.
This is a partial method obstruction, not a Collatz counterexample.

## Proof

### Exact input and scope of the specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-06-subcritical-log-six-coalescence.md`.
Use L028's proved guarded horizon exclusion in its sections
“Reduced slopes give the smaller size guard” and “Reusing the anchor
exclusion with all guards”, together with its root selection in
“Controlled CRT selection and the endpoint clock”. These passages,
including their separate critical audit, establish the following input:
for every integer L>=6, roots satisfying

\[
n\equiv47\pmod{3^{L+4}},\quad
81n+97\equiv0\pmod{2^{L+1}},\quad n>4^L
\]

admit no smaller positive c in S with T^s(c)=T^t(n) and
0<=s,t<=L. They also select such an odd root n_L with valuation 4
and the height bounds in the conclusion. This is an established
horizon assertion inside L028's proof, rather than its narrower
stated logarithmic-clock conclusion. In particular L026's statement
is not being applied with its n>12^L hypothesis weakened.

L028 supplies the actual paths, the positive offsets, the equal-slope
case, strict comparison with the original root and both zero clocks.
Its parity-coding input is Olivier Rozier, *Parity Sequences of the
3x+1 Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS 19
(2019), A8, Definition 1, Lemma 1 and proof, pp. 2–3,
[primary text](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
and its representative selection uses the named Chinese Remainder
Theorem. These enter through L028 and need neither a new application
nor a reproof here. The only difference derived below is the
arbitrary-real-C,B comparison with that existing integer horizon.
The overlap with L027 and L028 is not a new discovery; the assessed
search did not establish an external matching theorem for the larger
strict interval, and does not certify originality.

### Real-parameter comparison

Fix C,B before choosing L or a root. Since log(6)>0 and
0<C<1/log(6), delta=1-C log(6) is strictly positive. The number
(C log(163)+B)/delta is a finite real number, so L_0 is a finite
integer at least 6. For every integer L>=L_0 the ceiling inequality
and multiplication by delta>0 give

\[
\delta L\ge C\log(163)+B.
\]

Choose the root n_L already supplied by L028 at this horizon.
Its positive strict upper bound, logarithmic monotonicity and C>0
imply

\[
\begin{aligned}
C\log(n_L)+B
&<C\log(163\cdot6^L)+B\\
&=CL\log(6)+C\log(163)+B\\
&=L-\delta L+C\log(163)+B\\
&\le L.
\end{aligned}
\]

The logarithm identity is valid because 163 and 6^L are positive.
The first inequality remains strict even if the ceiling comparison
is an equality, including B=0. Consequently every nonnegative
integer s,t allowed by the claimed clock bound is at most L.
L028's guarded exclusion applies to every such pair and every
positive c in S strictly below this same n_L. It excludes their
actual-path coalescence. No floor convention enlarges the permitted
integer clocks, and zero clocks remain covered.

The selected roots have n_L>4^L, hence are unbounded as L ranges
over the integers at least L_0. Indeed, for any fixed real cutoff X,
all sufficiently large L have 4^L>X and therefore n_L>X; no
monotonicity of the selected representatives is needed. L028's
ternary congruence and n_L>47 give n_L=47+243k with k>=0, while
its binary congruence gives oddness and valuation 4. These facts
establish every root qualification in the conclusion.

The quantifiers are: each fixed C,B, every sufficiently large integer
horizon, a selected root, then exclusion of every smaller eligible
companion and both eligible actual paths. The root varies with the
horizon. No infinite positive orbit or nonconvergence is inferred.
At C=1/log(6), delta=0 and this comparison supplies no threshold;
that endpoint and larger clocks remain unresolved. Other cylinders
and universal eventual descent also remain unresolved.

### Verification and limitations

The proof is an exact inequality for arbitrary real parameters, not
an inference from sampled rational parameters. No new mathematical
script or finite parity screen is needed: the previously audited
horizon assertion is unchanged. The comparison explicitly checks
positive slack, the strict height inequality, ceiling equality,
B=0, integer clocks, positivity and unboundedness. The separate
critical audit below found no defect in this specialization.

### Separate critical audit, 2026-10-07

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-06-subcritical-log-six-audit.md`.
The complete L033 proof and complete L028 proof, including its canonical
audit, were read. The comparison with the earlier coefficient ranges
and the distinct failed small-CRT forcing route was checked against
Attempts 016 and 020. No mathematical correction or improved bound
was obtained. This is verification of an existing local partial result,
not an originality claim or a Collatz resolution.

**Input boundary.** L028 proves exclusion for every root satisfying
its three guards (3), at every integer L>=6, before specializing to
its stated coefficient 1/log(12). That intermediate assertion is
therefore available here with the same quantifiers. Its proof replaces
L026's large-slope size estimate by an exhaustive reduced-slope argument
under n>4^L. The subsequent anchor argument explicitly checks the
remaining height use n>47, both zero clocks, the equal-slope case,
integer anchor congruences, and the division between actual transferred
prefix and formal suffix. Its canonical audit includes the exceptional
anchor's finite evidence. L033 changes none of those hypotheses or
proof cases, and introduces no dependence on the selected root's
convergence. No specific concern requiring a new L026/L025 certificate
audit was found; those inputs remain inherited through L028. In
particular this review neither applies L026 at a smaller height nor
infers the broader coefficient range from L028's narrower conclusion.

**Root selection and qualifications.** For every integer L>=6,
L028's CRT class has modulus M=162*6^L. Its representative formula
gives 4^L<n_L<=4^L+M, regardless of whether the floor argument is
integral or negative. Since 4^L<6^L, the final inequality
n_L<163*6^L is strict. Thus all horizon guards hold before either
clock is considered. In particular n_L>4^6>47, and 3^(L+4)
is divisible by 243, so n_L=47+243k with integer k>=0.
For an explicit check of the binary qualification, L>=6 makes
2^(L+1) divisible by 64. Reducing 81n_L+97 modulo 64 gives
17n_L+33=0. Since 17*47+33=832 is divisible by 64 and 17 is
invertible modulo 64, n_L=47 modulo 64. Consequently
n_L+1=16(3+4j) for an integer j, proving oddness and valuation
exactly 4. These are the unchanged congruence consequences in L028,
not an assumption about a generic residue-47 root. Also 47=20 modulo
27, as required for the root cylinder; the excluded companions remain
all positive integers in S strictly below this original n_L.

**Parameters and clock transfer.** C and B are fixed finite reals
before L is chosen. The strict upper bound on C gives delta>0,
so A=(C log(163)+B)/delta is finite and L0=max(6,ceil(A))
is an integer. For every integer L>=L0, L>=A, whence
delta L>=C log(163)+B. Multiplying the strict logarithmic height
bound by positive C then gives

\[
0<C\log(n_L)+B
<CL\log(6)+C\log(163)+B
\le CL\log(6)+\delta L=L.
\]

The lower inequality follows from n_L>1, C>0 and B>=0; in
particular the zero clocks are retained, not removed by an empty
permitted-time interval. The strict upper inequality persists when
L=A is an integer and when B=0. It also holds arbitrarily close
to C=1/log(6) from below: L0 can grow without bound, but is
finite for each fixed pair C,B. Each permitted integer s or t is
in fact at most L-1, hence certainly at most the L028 horizon L.
The two clocks need not agree. Every candidate positive c<n_L in
S and every pair of permitted actual paths therefore falls inside
L028's exclusion. There is no interchange of parameter quantifiers,
no rounding enlargement, and no comparison against a later orbit
height instead of the original root.

**Unboundedness and limit of the claim.** For any real cutoff X,
there are integers L>=L0 with 4^L>X, and every such selection has
n_L>X. This establishes an unbounded set of eligible roots even
if representatives at consecutive horizons are not monotone or are
occasionally equal. It excludes any finite exceptional base but
does not produce a single root with infinite avoidance. At the
excluded endpoint C=1/log(6), delta=0, and the threshold argument
is unavailable. L032's unproved zero-run property is not used.
Neither that endpoint, a larger clock, a different cylinder nor
universal descent is settled by this audit.

All checks here are analytical and apply to arbitrary admissible real
parameters. No numerical sample or mathematical script was needed.
The direct local input remains L028; no DAG change is warranted.

## Mathlib

Full strict-coefficient logarithmic residue-20 coalescence obstruction:
**not checked**. Supporting real logarithm monotonicity, product/power
identities, ceiling inequalities and divergence of 4^L: **not checked**.
Unknown coverage is not evidence of absence. No Lean verification or
complete candidate Collatz resolution is claimed.
