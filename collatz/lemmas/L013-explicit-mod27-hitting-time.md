# L013 — Explicit logarithmic hitting time for residue 20 modulo 27

## Hypotheses

For positive integers use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Let

\[
\mathcal S=\{1,2\}\cup\{n\in\mathbb Z_{>0}:n\equiv20\pmod{27}\}.
\]

All logarithms are natural. Time zero is permitted when the start is
already in \(\mathcal S\). Count shortcut steps, not unshortened Collatz
steps. No convergence assumption is made.

## Conclusion

For every positive integer \(n\), the first hitting time

\[
\tau(n)=\min\{k\ge0:T^k(n)\in\mathcal S\}
\]

exists and satisfies

\[
\boxed{\tau(n)\le\left\lceil24\log n+14\right\rceil.}
\tag{1}
\]

Thus the assessed target holds with \(A=24\), \(B=14\), \(M=2\).
This gives no comparison of a later member of \(\mathcal S\) with its
starting value, and does not establish convergence to 1.

## Proof

### The sourced certificate and its exact verification

The qualitative comparator is Monks, Monks, Monks and Monks,
*Strongly sufficient sets and the distribution of arithmetic sequences
in the 3x+1 graph*, [arXiv:1204.3904v2, Theorem 6.4, pp. 22–23](https://arxiv.org/pdf/1204.3904v2#page=22).
The residue table and weights below reproduce
[Sodelin's public reconstruction, section 2](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/sources/Sufficiency_Rank_Audit_2026-09-05.md),
also specified in [its checker, lines 14–67](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/verification/mod27_rank_check.py#L14).
They are checked directly here rather than assumed. The phase-entry
estimates and explicit constants are the quantitative specialization;
the inspected sources do not state (1). No originality claim is made.
Live-source provenance qualifications are in the prior assessment.

Call the following fifteen residues the core, and define \(h\) by the
second column. Since \(2^{-1}=14\) modulo 27, the even image is \(14r\)
and the odd image is \(14(3r+1)\), reduced modulo 27. The parity is that
of the actual integer; either parity occurs in each residue class.

| r | h(r) | Even image | Odd image |
| --- | --- | --- | --- |
| 1 | 2 | 14 | 2 |
| 2 | 1 | 1 | 17 |
| 4 | 0 | 2 | 20 |
| 5 | 1 | 16 | 8 |
| 7 | 2 | 17 | 11 |
| 8 | 0 | 4 | 26 |
| 10 | 2 | 5 | 2 |
| 11 | 1 | 19 | 17 |
| 14 | 1 | 7 | 8 |
| 16 | 2 | 8 | 11 |
| 17 | 0 | 22 | 26 |
| 19 | 2 | 23 | 2 |
| 22 | 0 | 11 | 20 |
| 23 | 1 | 25 | 8 |
| 25 | 2 | 26 | 11 |

The core comprises all residues prime to 3 except 13, 20 and 26.
Every internal core edge satisfies

\[
2p-1\le h(r)-h(r'),
\tag{2}
\]

where \(p=1\) for odd steps and \(p=0\) for even steps, as each row
checks. There are 25 internal edges and five exits. The latter enter
20 or 26. The remaining exceptional transitions are

\[
26\mathrel{\mathop{\longrightarrow}^{\rm odd}}26,
\qquad26\mathrel{\mathop{\longrightarrow}^{\rm even}}13,
\qquad13\mathrel{\mathop{\longrightarrow}^{\rm either}}20.
\tag{3}
\]

Both shortcut branches preserve coprimality to 3: an even step divides
by a unit modulo 3, and an odd step has \(2T(n)\equiv1\pmod3\).
Thus after leaving the multiples of 3, only the core, these exceptional
residues, and the stopping set can occur.

Put \((w_0,w_1,w_2)=(16,28,49)\), and for core integers put
\(Q(x)=w_{h(x\bmod27)}x\). The adjacent weight ratio is \(7/4\).
For an internal odd step, (2) lowers \(h\) by at least one. For
every nonterminal core integer \(x\ge3\),

\[
\frac{T(x)}x=\frac{3x+1}{2x}\le\frac53,
\qquad
\frac{Q(T(x))}{Q(x)}\le\frac53\frac47=\frac{20}{21}.
\tag{4}
\]

The positive additive term is included in the bound \(5/3\). For an
internal even step, (2) raises \(h\) by at most one, so

\[
\frac{Q(T(x))}{Q(x)}\le\frac12\frac74=\frac78<\frac{20}{21}.
\tag{5}
\]

A nonterminal core integer is actually at least 4, since 1 and 2
are terminal and 3 is not in the core. Consequently \(Q(x)\ge64\).
Equations (4)–(5) therefore prohibit remaining in the core indefinitely:
an infinite sequence of internal edges would give
\(64\le Q(T^j(x))\le(20/21)^jQ(x)\) for every \(j\), a contradiction.

These facts also verify the source's stopped lexicographic rank:
\((0,0)\) on \(\mathcal S\); \((3,x)\) on multiples of 3;
\((2,Q(x))\) on the core; \((1,v_2(x+1)+2)\) on residue 26;
and \((1,1)\) on residue 13. Every nonterminal step lowers it, by
(3)–(5) and the valuation identity below. It is a rank only until the
first hit, and is not claimed to decrease after leaving \(\mathcal S\).

### Initial phase and entry height

Starts in \(\mathcal S\) already have hitting time zero. It suffices
to consider other starts \(n\ge3\). If \(3\mid n\), write
\(n=2^a d\) with \(d\) odd. Then \(3\mid d\) and \(d\ge3\).
There are \(a\) halving steps, followed by one odd step to
\(m=(3d+1)/2\), which is prime to 3. Thus

\[
t_3=a+1\le\frac{\log n}{\log2}+1,
\qquad m\le\frac53d\le\frac53n.
\tag{6}
\]

If \(3\nmid n\), set \(t_3=0\), \(m=n\); both inequalities still
hold. If a terminal state is reached sooner, the stated time upper
bounds remain valid.

### Core phase and exit height

If \(m\) is in the nonterminal core, its initial weight satisfies
\(Q(m)\le49m\le245n/3\). Let \(r\ge0\) be the number of internal
core edges before the exit. Finiteness was established above. At the
last core state \(x=T^r(m)\),

\[
64\le Q(x)\le(20/21)^r\frac{245n}{3}.
\]

Taking logarithms gives

\[
r\le\frac{\log((245/192)n)}{\log(21/20)},
\qquad
t_{m core}=r+1\le
\frac{\log((245/192)n)}{\log(21/20)}+1.
\tag{7}
\]

The exit step is included. Also \(Q(x)\le Q(m)\) and every weight
is at least 16, so the exit height \(y=T(x)\) satisfies

\[
y\le\frac53x\le\frac53\frac{Q(m)}{16}
\le\frac{1225}{144}n<9n.
\tag{8}
\]

Again \(T(x)\le5x/3\) includes its positive additive term and holds
for even steps as well. If the core phase is absent, its length is
zero and its successor entry \(y=m\), when needed, also satisfies
\(y\le5n/3<9n\). The nonnegative upper bound (7) covers this case.

### Arithmetic exit phase

If \(y\) is terminal, there are no further steps. At residue 13,
(3) gives one further step. At residue 26 put \(e=v_2(y+1)\ge0\).
For an odd shortcut step the exact identity is

\[
T(z)+1=\frac32(z+1).
\tag{9}
\]

Hence the valuation decreases by exactly one while the current state
is odd and in residue 26. Inductively there are exactly \(e\) such
odd steps, all remaining in residue 26. The resulting state is even,
because its value plus one is odd. One even step then reaches residue
13 and one further step reaches residue 20. All these intermediate
states are positive and outside \(\mathcal S\). Thus the tail in
this case has exactly \(e+2\) steps, including both exit steps.
The argument covers \(e=0\) as well.

Since \(2^e\le y+1\le9n+1\le10n\), all three tail cases satisfy

\[
t_{m tail}\le\frac{\log(10n)}{\log2}+2.
\tag{10}
\]

No uniform bound on the number of residue-26 visits is assumed. Their
growth changes the height, but (9) controls their number from the entry
height before that growth.

### Explicit constants and integer time

Adding (6), (7) and (10) proves

\[
\tau(n)\le A_0\log n+B_0,
\quad
A_0=\frac2{\log2}+\frac1{\log(21/20)},
\quad
B_0=4+\frac{\log(245/192)}{\log(21/20)}+
\frac{\log10}{\log2}.
\tag{11}
\]

For \(u>1\),
\(\log u>2(u-1)/(u+1)\): the difference vanishes at 1 and has
derivative \((u-1)^2/(u(u+1)^2)>0\). Therefore
\(\log2>2/3\) and \(\log(21/20)>2/41\), giving
\(A_0<3+41/2=47/2<24\).

Also \(\log(245/192)<53/192\), by
\(\log(1+t)<t\) for \(t>0\), and
\(\log10/\log2<4\), since \(10<16\). Consequently

\[
B_0<8+\frac{53}{192}\frac{41}{2}
=\frac{5245}{384}<14.
\]

For \(n\ge3\), (11) is therefore strictly less than
\(24\log n+14\), which implies (1) for the integer \(\tau(n)\).
For \(n=1,2\), \(\tau(n)=0\) directly. This completes the proof.

### Scope and computational verification

`python3 scripts/mod27-hitting/check_hitting.py` checks the exhaustive
modular table, all 25 internal-edge inequalities by exact coefficients
with the +1 retained, and all five exits. Its rational comparisons also
check the constant arithmetic. Separate finite regressions follow the
first hit for starts 1 through 20,000, and residue-26 loop lengths
0, 1, 2, 3, 20, 100 and 1024. Results are in
`scripts/mod27-hitting/result.json`. The universal justification is the
proof above; these regressions only check the implementation and boundary
cases. This result is not a complete Collatz proof or disproof candidate.

## Mathlib

Full explicit modulo-27 hitting-time statement: **not checked**.
Supporting congruence, valuation, logarithm, and affine-inequality
results: **not checked**. No absence from Mathlib is asserted, and no
library theorem name or direct library link was verified. The source
links above identify mathematical comparators, not Mathlib coverage.
