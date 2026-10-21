# L026 — Fixed initial valuation obstructs residue-47 coalescence clocks

## Hypotheses

Use T(n)=n/2 on even integers and T(n)=(3n+1)/2 on odd integers;
S denotes the positive integers congruent to 20 modulo 27. Let L>=6
be an integer. Suppose n is a positive integer satisfying

\[
n\equiv47\pmod{3^{L+4}},\qquad
81n+97\equiv0\pmod{2^{L+1}},\qquad n>12^L.                 \tag{1}
\]

No convergence, least-root or companion hypothesis is assumed.
Both clocks count shortcut steps and include zero.

## Conclusion

Every such n is odd, is 47 modulo 243, and has v_2(n+1)=4.
There are no c in S and 0<=s,t<=L with

\[
0<c<n,\qquad T^s(c)=T^t(n).                              \tag{2}
\]

For each L the roots (1) form an unbounded arithmetic progression.
Consequently no A>=1, B>=0, N>=1 gives the proposed cover with
s,t<=A v_2(n+1)+B. More generally, no clock depending only on
v_2(n+1), with a finite value at 4, gives this cover outside a finite
base. This is a method obstruction, not a Collatz counterexample.

## Proof

### Assessed inputs and the changed argument

Prior coverage is
`drafts/literature/2026-10-05-residue47-odd-run-clock-coalescence.md`.
L025 supplies the shifted inverse-word offset estimate recalled below;
its all-odd obstruction alone does not prove this result. Finite parity
coding is imported from Olivier Rozier, *Parity Sequences of the 3x+1
Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS 19 (2019),
A8, [Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
Specifically, integers equal modulo 2^p have the same first p input
parities, including signed integers via the source's 2-adic map.
No reproof of parity coding is needed. The additional work is a
post-exit word with fixed initial valuation, six extra matched binary
digits in the anchor transfer, and the exceptional anchor value 47.
Neither LaDue's adjacent companion nor an unread source is an input.
The result was not found in the assessed sources; originality is not
certified by that bounded comparison.

### The actual post-exit path

Because 81*47+97=3904=64*61, the binary condition in (1) gives
n=47 modulo 64. Hence n+1=16 modulo 32 and v_2(n+1)=4.
The first four inputs are odd, and

\[
y_t+1=(3/2)^t(n+1)\quad(0\le t\le4),\qquad
y_4=(81n+65)/16\quad\hbox{is even}.
\]

After its even exit, the rest of the prescribed path satisfies

\[
y_t+1=\frac{3^{t-5}(81n+97)}{2^t}\quad(5\le t\le L).       \tag{3}
\]

Indeed y_5=(81n+65)/32; the divisibility in (1) makes the displayed
y_t odd for 5<=t<=L. Induction using the odd branch proves (3).
Thus the first L actual input symbols are O^4 E O^(L-5).
Write y_t+1=K_t(n+q_t), where

\[
(K_t,q_t)=
\begin{cases}(3^t/2^t,1)&0\le t\le4,\\
(3^{t-1}/2^t,97/81)&5\le t\le L.
\end{cases}                                               \tag{4}
\]

### All inverse words and the slope above one

Suppose (2) holds. Reverse its actual c-path from y_t. The guarded
inverse branches are E(y)=2y and O(y)=(2y-1)/3, with O admitted only
at y=2 modulo 3. For this selected word of length s with a odd
inverses, L025's shifted inverse calculation gives

\[
c+1=\lambda(n+q_t)-d,\qquad
\lambda=K_t2^s/3^a,\qquad 0\le d\le2^s-1.                \tag{5}
\]

This offset estimate is independent of the starting shifted value:
in the coordinate z=y+1 the inverse maps are 2z-1 and 2z/3.
Their offset recurrences, 2d+1 and 2d/3, are exactly those used in
L025. Thus the same estimate applies to (4), without extending its
all-odd root hypothesis. Every actual inverse guard remains retained.

The slope in (5) has an integer numerator and denominator 2^t3^a,
so if lambda>1 then lambda-1>=6^(-L). Since q_t>=1,

\[
c-n=(\lambda-1)n+\lambda q_t-d-1
>2^L-d>0,
\]

contrary to c<n. Hence lambda<=1, including equality.
Put h=s-t. For t<=4, a<=s implies
lambda>= (3/2)^(t-s); h<0 is impossible. For t>=5,

\[
\lambda=2^h3^{t-1-a}\ge\tfrac13(2/3)^h.
\]

If h<=-3 the latter bound is at least 9/8. Thus h>=-2 in this case.

### Integer anchor and the precisely transferable prefix

Evaluate the same rational inverse word at
Y_t=K_t(47+q_t)-1, and call the output c0. Then

\[
c_0+1=\lambda(47+q_t)-d,\qquad c-c_0=\lambda(n-47).       \tag{6}
\]

We have 64*3^(L+4) dividing n-47. In (6), its power of 2 after
multiplication by lambda is at least h+6>=4. Its power of 3 is
at least L+4+t-a for t<=4, and L+3+t-a for t>=5, each at least 3.
Thus c0 is an integer, c0=c modulo 27, and

\[
c_0\equiv c\pmod{2^{h+6}}.                              \tag{7}
\]

Since lambda<=1 and d>=0, (6) gives c0<=47: in the post-exit case
c0<=47+16/81, and integrality gives the asserted bound. With its
residue guard the possibilities are c0<=20 or c0=47.

Let F be the forward affine word of the actual c-path. As an affine
identity, F(c0)=Y_t. Only its first

\[
p=\min(s,h+6)
\]

symbols are asserted actual at the signed anchor c0, by (7) and
Rozier's finite parity coding. This assertion covers no unjustified
suffix. All subsequent symbols will be bounded as formal rational maps.

If c0<=20 and c0=20 modulo 27, it is either 20 or nonpositive.
Nonpositive signed integers stay nonpositive under T; the orbit
20,10,5,8,4,2,1,2,... stays at most 20. Hence T^p(c0)<=20.

For t<=4 one has p=s. Also c0=47 would force lambda=1 and d=0
in (6), whence c=n. It follows that F(c0)<=20, whereas
Y_t=48(3/2)^t-1>=47, a contradiction. Only t>=5 remains.

### The exceptional anchor 47

Suppose now c0=47 and t>=5. If lambda=1, (6) again gives c=n;
therefore lambda<1. Nonnegativity of d in (6) forces

\[
48\le\lambda(47+97/81),\qquad
\lambda\ge\frac{243}{244}.                              \tag{8}
\]

Write lambda=2^h/3^b with the integer b=a-t+1. When h=-2,-1,0,
the largest possible value below one is respectively 3/4, 1/2, 1/3;
none meets (8). For 1<=h<=53, let b_h be the least integer with
3^b_h>2^h. The following complete finite arithmetic table gives b_h
in increasing h order and the minimum of 243*3^b_h-244*2^h in each
row. All minima are positive; this proves 2^h/3^b<243/244 whenever
b>=b_h throughout this entire finite range.

| h range | b_h in order | Minimum strict margin |
| --- | --- | ---: |
| 1–9 | 1,2,2,3,4,4,5,6,6 | 235 |
| 10–18 | 7,7,8,9,9,10,11,11,12 | 31729 |
| 19–27 | 12,13,14,14,15,16,16,17,18 | 1213891 |
| 28–36 | 18,19,19,20,21,21,22,23,23 | 20436531425 |
| 37–45 | 24,24,25,26,26,27,28,28,29 | 1560168070547 |
| 46–53 | 30,30,31,31,32,33,33,34 | 12734846662198993 |

These are integer comparisons, not a sampled asymptotic estimate.
For each entry 3^(b_h-1)<=2^h<3^b_h verifies minimality, and direct
integer multiplication verifies the margin. Every individual margin
is retained in the certificate below. Therefore (8) implies h>=54.

The full finite signed-anchor computation is

```text
47,71,107,161,242,121,182,91,137,206,103,155,233,350,175,
263,395,593,890,445,668,334,167,251,377,566,283,425,638,319,
479,719,1079,1619,2429,3644,1822,911,1367,2051,3077,4616,
2308,1154,577,866,433,650,325,488,244,122,61,92,46,23,35,
53,80,40,20,10,5,8,4,2,1.
```

Each consecutive pair is checked by its actual parity rule. In
particular T^59(47)=40 and T^66(47)=1. The displayed tail and the
cycle 1,2 prove T^j(47)<=40 for every j>=59. Since t>=5 and h>=54,
p=min(h+t,h+6)>=59. Thus T^p(c0)<=40 in this exceptional case too.
This uses convergence of one explicitly verified anchor, not a finite
base assumption about arbitrary roots.

### Bounding the formal suffix

For all the remaining cases t>=5, we now know T^p(c0)<=40. If
5<=t<=6 then p=s, so F(c0)<=40<Y_t (Y_5=121, Y_6=182).
If t>=7, p=h+6 and s-p=t-6. For any real x<=M with M>=0, both
formal forward branches are at most (3M+1)/2. Repeating this bound,

\[
F(c_0)+1\le41(3/2)^{t-6}
<183(3/2)^{t-6}=Y_t+1.                                  \tag{9}
\]

The last equality follows directly from (4) and
81*47+97=3904: Y_6+1=183, and the formal anchor word after time 6
continues with odd branches. Those later branches need not be actual
at 47. Equation (9) contradicts the affine identity F(c0)=Y_t.
This exhausts all slopes, both clocks including zero, and all words
chosen separately for each n.

### Quantifiers and reproducible checks

Because 81 is odd, the binary congruence in (1) specifies one class
modulo 2^(L+1). CRT with the ternary congruence gives a full class
modulo 2^(L+1)3^(L+4), with unbounded positive members. All are 47
modulo 243, and choosing n>12^L ensures n>47, hence n=47+243k
with k>=0. Given A,B,N, take L=max(6,4A+B) and choose such a root
above N as well. Its valuation is 4, so (2) excludes every clock
allowed by A v_2(n+1)+B. The same argument uses L at least the
finite value at 4 of any proposed valuation-only clock.

Reproduce the exact finite checks with
`python3 scripts/odd-run-coalescence/check.py`. Full evidence is in
`scripts/odd-run-coalescence/certificate.json`: all 53 individual
slope margins, the entire anchor orbit, and complete guarded inverse
trees at L=6,8,12,20. The trees have respectively 257,685,3574,61313
nodes and no admissible companions. Both empty paths, all inverse
guards, the offsets and the matched anchor prefixes are checked, with
no slope or size pruning. The finite trees support transcription;
they are not the all-L proof. The finite slope table and finite anchor
orbit are complete proofs of exactly the bounded arithmetic claims
used above, followed by the explicit cycle for later times.

The roots vary with L; no infinite positive orbit is inferred. Clocks
depending on full starting height or later arithmetic remain open.
L014 motivates convergence transfer but is not a mathematical premise
of this obstruction. Universal eventual descent is still unproved.

### Independent critical audit, 2026-10-05

The audit retained the hypotheses (1) without assuming a least root,
convergence of the CRT roots, or any companion. No defect was found.
The following checks address the load-bearing cases rather than
extrapolating the finite trees.

In the integer-anchor transfer, a<=s<=L and h>=-2 give a binary
exponent h+6>=4. The ternary exponent is at least L+4+t-L=t+4
before the exit and L+3+t-L=t+3 after it; both are at least 3.
This verifies integrality and both congruences even at the shortest
possible transferred prefix. For t<=4, h+6=s-t+6>=s and the whole
word transfers. For t>=5 only min(s,h+6) symbols transfer. In
particular, the formal suffix bound makes no parity claim past that
prefix, even when an intermediate formal value is negative.

For c0=47 the initial case forces lambda=1,d=0 and hence c=n.
In the post-exit case lambda=1 also gives c=n directly from (6),
even without asserting that d=0 there. For lambda<1, (8) and all
53 strict margins force h>=54. Thus p>=59; the entire checked
anchor orbit followed by the explicit 1,2 cycle supplies the bound
40 for every possible p, not merely for p<=66. When c0<=20,
signed nonpositive invariance and the orbit of 20 supply the bound
at every prefix length, including zero. For t=5,6 the whole word
transfers; for t>=7 the remaining length is exactly t-6 and (9)
is strictly below the formal endpoint. These cases include both
zero clocks and every slope equality. CRT supplies unbounded roots
for each separately fixed horizon, not one root for all horizons.

`python3 scripts/odd-run-coalescence/audit.py` independently reads
the complete saved evidence, checks every slope-table entry and
its canonical row minimum, every anchor edge and the terminal
cycle, and every node and guarded child in all four inverse trees.
It uses forward affine coefficients and direct actual forward
replay rather than the producing script's inverse recurrences.
Full results are in `scripts/odd-run-coalescence/audit-certificate.json`:
65,829 nodes replayed, 66 anchor edges, 53 strict margins and no
failures. None of these four finite trees exercises the exceptional
c0=47 case under the smaller-residue-20-companion guards. Its
all-horizon exclusion therefore rests on the preceding analytical
argument, complete slope comparisons and anchor orbit, not the trees.

This audit confirms the existing obstruction within the unchanged
assessment; it establishes no stronger clock bound, no additional
lemma and no progress beyond the assessed sources' novelty scope.

## Mathlib

Full fixed-valuation residue-20 coalescence obstruction: **not checked**.
Supporting finite parity coding, signed iteration, valuations and CRT:
**not checked**. The direct Rozier citation supplies the standard
parity input. Unknown availability does not assert absence; no Lean
check ran.
