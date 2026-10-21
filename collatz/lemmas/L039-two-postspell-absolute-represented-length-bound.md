# L039 — Absolute represented length for a closed two-postspell word

## Hypotheses

Use T(t)=t/2 for even positive integers and T(t)=(3t+1)/2
for odd positive integers. O and E denote actual input parities.
For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be integers with
a_i congruent to 2 modulo 18. Define

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

Assume W_1W_2 is actual at a positive odd integer n>1,
x=T^{D_1}(n) is positive and odd, both n and x are congruent
to 20 modulo 27, and T^N(n)=n. Both final even tails are exact.
No least-root, first-return, primitive-period, distinct-junction,
relative-growth or global-minimum assumption is imposed.
Independent tails, repeated periods and x=n are admitted.
All logarithms are natural, and N is the represented length.

## Conclusion

Every representation satisfying these hypotheses obeys

\[
\boxed{N<4500,\quad\text{hence }N\le4499.}             \tag{1}
\]

This is a necessary restriction on the fixed two-word language,
not an integer-closure exclusion or an existence claim. Universal
entry, other cycles, divergence and eventual descent remain unresolved.
The separate critical audit below found no defect in this conditional bound.

## Proof

### Reused count, cycle and prefix estimates

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-two-postspell-total-length-bound.md`.
It approves this elementary effective combination, not the conclusion.
The working calculation is saved in
`drafts/2026-10-08-two-postspell-total-length-calculation.md`.

Put P_i=4J_i+H_i. L035 counts the actual input occurrences as

\[
K=3(J_1+J_2)+H_1+H_2
  =P_1+P_2-(J_1+J_2),\qquad
L=J_1+J_2+a_1+a_2,\qquad N=K+L.
\]

Here K>=18, L>=8 and N>=26 because a_i>=2. Both positive
odd junctions are 20 modulo 27, so they are at least 47:
the positive members of that residue class begin 20,47,74,...,
and 20 is even. Thus L035 gives

\[
0<\Lambda=N\log2-K\log3
 <\frac{23}{11}\left(\frac1n+\frac1x\right)
 \le\frac{46}{517}.                                  \tag{2}
\]

The word is nontrivial since its state n is outside the invariant
shortcut cycle {1,2}. L035's estimate is already justified for
represented occurrence counts, including repeated periods.
L038 has exactly the present actual closed-word hypotheses, and its
separate critical audit found no defect. It supplies
P_i<144 log N+95 for each i. Consequently

\[
0<K<P_1+P_2<288\log N+190.                           \tag{3}
\]

For precise inherited theorem coverage, L035 uses Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
Article 23.3.5,
[Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf).
L038 uses, through L037/L036, John Simons and Benne de Weger,
*Theoretical and computational bounds for m-cycles of the 3n+1 problem*,
Acta Arithmetica 117 (2005), 51–70,
[Lemma 12, printed p. 61, and the nonminimal-period convention in section 1.2, printed p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Their local applicability and repetition checks are reused, rather
than reproving either general theorem. Rhin's input and published
computations remain imported, not independently certified here.
The exact absolute two-word ceiling is not stated by those sources
as inspected; the following specialization supplies the difference.

### An inequality with no uncontrolled tail term

The exact integer comparison 3^5=243<256=2^8, followed by the
strictly increasing logarithm and division by 5 log2>0, gives
log3/log2<8/5. Reuse L036's proved elementary estimate log2>2/3
(its derivative proof appears under “Explicit simple constants”).
With (2) and positive K, it follows that

\[
N=K\frac{\log3}{\log2}+\frac{\Lambda}{\log2}
 <\frac85 K+\frac{69}{517}.
\]

Substitute (3). Since 69/517<1,

\[
N<\frac{2304}{5}\log N+304+\frac{69}{517}
 <\frac{2304}{5}\log N+305.                          \tag{4}
\]

Both independent tail lengths occur in N throughout; they have not
been bounded, removed or identified with one another. Equation (2)
controls their total contribution through the cycle linear form.

### Exact solution of the effective inequality

The positive exponential series, retaining its terms of degrees
zero through three, gives

\[
e>1+1+\frac12+\frac16=\frac83.
\]

Moreover 8^9=134217728 and 4500*3^9=88573500. Therefore
e^9>(8/3)^9>4500, and log4500<9. These are exact integer
and series comparisons, without a rounded logarithm or finite screen.

For real t>=4500 define F(t)=t-(2304/5)log t-305.
Its derivative is 1-2304/(5t)>0 throughout that interval, since
5t>=22500>2304. At its left endpoint,

\[
F(4500)>4500-\frac{2304}{5}\,9-305=\frac{239}{5}>0.
\]

If N>=4500, monotonicity would imply F(N)>=F(4500)>0.
But (4) says F(N)<0. This contradiction proves (1), including
the integer version N<=4499.

### Scope and limitations

Every reused estimate concerns this same represented K,N and the
same two actual word occurrences. No step requires a least period
or unequal junctions. If x=n, the two prefixes remain indexed by
their word occurrences and (3) still adds their respective bounds.
The conclusion applies to any repeated representation that satisfies
the stated two-word hypotheses; arbitrary repetitions of an arbitrary
cycle need not remain in this fixed two-word language. Thus it is
not an absolute bound for unrestricted cycle representations.

The approved continuation test succeeds: (4) is solvable with explicit
constants and requires no extra tail, height or minimum hypothesis.
The finite parameter domain may support later closure analysis, but
no such analysis, feasible enumeration claim, positive closed integer
example or exclusion of L031's divisibility condition is asserted.
Attempt 019's boundary-guard failure and history 069's full-minimum
count mismatch remain valid. This is REPRODUCTION of a quantitative
combination of known inputs, without a novelty or priority claim or
progress beyond the source mathematics checked. It supplies a new
local conditional bound, not a complete Collatz candidate.

### Separate critical audit

The 2026-10-08 audit used the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-08-two-postspell-total-length-audit.md`.
The working record is
`drafts/2026-10-08-two-postspell-total-length-audit.md`.
It checked complete L039 and the load-bearing proofs of L035, L036,
L037, L038 and L031. The conclusion and direct mathematical inputs
are unchanged. The precise primary coverage cited above is reused;
the source computations and Rhin input are not independently certified.

**Counts, positivity and cycle applicability.** Every B=OOEO has
three odd and one even inputs. Thus K=3(J_1+J_2)+H_1+H_2,
L=J_1+J_2+a_1+a_2 and N=K+L, with K>=18,L>=8,N>=26.
In particular K=P_1+P_2-(J_1+J_2)<P_1+P_2. The congruence
and nonnegativity of a_i imply a_i>=2 separately for both indices.
Writing an odd positive residue-20 junction as 20+27t forces t
to be positive odd, so n,x>=47. The actual closed orbit is nontrivial
because its state n lies outside the invariant shortcut cycle {1,2}.

L035 bounds all three odd inputs of each B and the disjoint terminal
odd subrun; each word's final endpoint is excluded from its input
interval. Thus each input time is counted once, including when x=n.
Its finite geometric estimates give the occurrence mass bound used
in (2), with no hypothesis that the junctions are global minima.
Hercher's Theorem 16 applies first to the primitive cycle. For repeat
factor q>=1, K=qK_0, N=qN_0 and S=qS_0, so its normalized
inequality is unchanged. The primitive states are distinct by the
least-return argument in L035, justifying the source's state sums.
Multiplication by K log2 and then the positive finite mass estimate
give the strict upper bound in (2). Substituting n,x>=47 gives
(23/11)(2/47)=46/517 with the stated non-strict last comparison.

**Inherited prefix bounds.** The lower estimate behind L037/L038 is
the cited Simons–de Weger Lemma 12 with c=13.3*0.46057=6.125581.
Even starting from a primitive version,
Lambda=q Lambda_0>q e^(-c)K_0^(-13.3)
>=e^(-c)(qK_0)^(-13.3), so the represented use is legitimate.
Together with L035, this bounds the smaller designated junction b
by (46/11)e^c K^13.3. L037 retains its own index when deducing
log(b+23/11)<(133/10)log K+8 and 4J+H<50log N+33.
Its inequalities use b>=47, 1<K<N and positive logarithms.

L031 gives v_2(y+1)=H from the actual endpoint identity
2^H(2^a m+1)=3^H(y+1). With H>=3 it then gives
v_2(11r+23)=4J+2 for that word's own start r. No E^2-only
identity is used. L038 transfers the selected word's height using
z=G(b+23/11)-(12/11)(3/2)^H-1 and m=z/2^a,
where G=(27/16)^J(3/2)^H. Positivity and a>=2 give
m+23/11<G(b+23/11); the required additive margin follows from
b+23/11>=540/11. The exact bounds log G<(4J+H)/2
and (4J_r+H_r)<(15/4)log(r+23/11)+3 at each word's
own start give the other prefix coefficient 1149/8<144 and
constant 759/8<95. This verifies the inherited scope of (3).
The transfer runs from n to x or from x to n according to the
selected index, and in the tie it still addresses separate word
occurrences. It assumes neither a tail cap nor a junction-size ratio.

**Exact effective inequality.** The derivative of
log t-2(t-1)/(t+1) is (t-1)^2/[t(t+1)^2]>0 for t>1,
and its value at 1 is zero. Thus the imported elementary estimate
log2>2/3 is strict. Also 3^5=243<256=2^8 gives
log3/log2<8/5. Since K>0 and 0<Lambda<46/517,
division by log2 and substitution in the count identity give
N<(8/5)K+69/517. Multiplying (3) by 8/5 yields
coefficient 2304/5 and constant 304. Since 69<517,
this is exactly (4). No term in either independent tail is dropped:
both remain in the same N throughout the cycle identity.

**Exact threshold.** The omitted terms after degree three in the
positive exponential series at 1 have positive sum, so e>8/3.
The complete integer comparison is
8^9=134217728>88573500=4500*19683=4500*3^9.
Hence log4500<9. On t>=4500, F'(t)=1-2304/(5t)>0
because 5t>=22500>2304, and
4500-(2304/5)*9-305=(22500-20736-1525)/5=239/5>0.
Thus F(4500)>239/5 and monotonicity contradicts F(N)<0
whenever N>=4500. This is an all-real interval argument, not a
numerical sample; integrality of N gives N<=4499.

The audit found no defect, repair or stronger conclusion. Independent
exact tails, repeated periods and x=n all survive. The restriction
to representations with exactly two prescribed word occurrences is
essential: arbitrary repetitions need not satisfy that language.
This verifies a local REPRODUCTION, not originality, integer-closure
exclusion or a complete solution candidate. Attempt 019 and history
069 remain valid stop evidence for their different mechanisms.

## Mathlib

Full matching absolute two-word bound, the inherited effective cycle
inputs, and supporting logarithm, exponential-series and monotonicity
results: **not checked**. No matching declaration or absence from
Mathlib is asserted. The complete exact specialization and precise
imported source citations above are the informal mathematical evidence.
