# L024 — Exact postspell valuation and unbounded replenishment

## Hypotheses

Use the positive-integer shortcut map T(x)=x/2 for even x and
T(x)=(3x+1)/2 for odd x. Let B=OOEO and W(J,H)=B^J O^H E^2,
where J>=2 and H>=3 are integers. Every letter requires its actual
input parity. All word boundaries below are positive odd integers
congruent to 20 modulo 27, so every E^2 tail is exact.
Write V(x)=v_2(11x+23). No least-nonconvergent-root assumptions or
additional arithmetic filters are imposed.

## Conclusion

For an actual word n -> m with parameters J,H, put y=T^(4J)(n).
There is a positive odd integer u with

\[
y+1=2^H u,\qquad 4m+1=3^H u,
\]

and the exact transport identities are

\[
V(n)=4J+2,\qquad V(y)=2,\qquad
V(m)=v_2(11\cdot3^H u+81)-2.                 \tag{1}
\]

For every integer R>=2 there are infinitely many actual chains

\[
p\xrightarrow{W(2,3)}n\xrightarrow{W(2,3)}m
 \xrightarrow{W(R,3)}q
\tag{2}
\]

with all the stated guards, and V(n)=10, V(m)=4R+2. In particular,
the gain on the middle word is 4R-8, unbounded although its parameters
and its input valuation are fixed. Its input has an actual preceding
word, as required when using L023's extendibility notion.

Moreover, for every K>=1 there are positive actual K-word chains
starting at a boundary n with an allowed preceding word and V(n)=10.
Consequently no finite-valued function g of V(n) alone can bound their
length by K<=g(V(n)). This does **not** refute a bound depending on n
itself, or a uniform n>=F(K) with F(K) tending to infinity.

## Proof

### Scope and imported inputs

The unchanged prior EXPLORE assessment is
`drafts/literature/2026-10-05-postspell-inverse-to-height.md`.
This is its approved whole-word shifted-valuation test. The result is
classified POTENTIALLY_NEW only relative to that bounded comparison;
no originality is asserted for finite coding or affine identities.

L020 supplies the actual identities

\[
11y+23=(27/16)^J(11n+23),\qquad
2^H(4m+1)=3^H(y+1),                         \tag{3}
\]

and residue-20 preservation. Their inspected source is Sodelin,
*Guarded root descent after independently unbounded return spells and
odd runs*, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
live main checked 2026-10-04, without an immutable revision or checked
Lean build. L021's actual-word composition retains the positive offsets
when these identities are used successively.

Import finite input-parity coding, also recorded in L020/L021, from
Bernstein–Lagarias, *The 3x+1 Conjugacy Map*, author manuscript dated
15 February 1996, [section 1, pp. 1–3, equations (1.3)–(1.5) and
the reduction-modulo-2^d permutation statement](https://websites.umich.edu/~lagarias/doc/bernstein.pdf).
In this shortcut convention any finite length-d input-parity string
has exactly one root residue modulo 2^d. Reuse the prior assessments'
source inspection; no infinite positive-integer realization is imported.
Only the specialization to the guards and valuation in (1)–(2) is
proved here, not general parity coding again.

### Exact transport

Since 4m+1 is odd, the second identity in (3) gives
v_2(y+1)=H. Thus u=(y+1)/2^H is a positive odd integer and
3^H u=4m+1. Now

\[
11y+23=11\cdot2^H u+12
       =4(11\cdot2^{H-2}u+3).
\]

The parenthesis is odd because H>=3. Hence V(y)=2. Taking dyadic
valuations in the first identity in (3), after multiplying by 16^J,
gives 4J+V(y)=V(n). Finally

\[
11m+23=(11\cdot3^H u+81)/4,
\]

so (1) follows. All quantities valued are positive integers; this
argument uses actual paths, not an unguarded inverse affine formula.

### Replenishment with a genuine preceding word

Fix R>=2. Form the finite input string in (2), followed by one O
letter at q. Its three words have total length D=4R+31. The extra
O is a parity guard at q; the chain itself ends before that step.
Finite coding supplies a residue r modulo 2^(D+1). CRT with
p=20 modulo 27 gives a unique positive representative
p_0 in {1,...,27*2^(D+1)}, and every

\[
p=p_0+27\cdot2^{D+1}a,\qquad a\ge0,
\]

has all those input parities. The shortcut map preserves positivity.
Each word preserves residue 20 by L020, applied successively with
L021's composition. The next word's first O ensures that n and m
are odd; the extra O ensures that q is odd. The roots p are odd
because the first letter is O. Immediately before every E^2 tail
the state is four times its odd endpoint, so its valuation is exactly
2. This verifies every guard of (2), for infinitely many positive p.

Applying (1) at n and m gives 10 and 4R+2 respectively. The
preceding W(2,3) makes n extendible. At endpoint m, therefore, the
middle-word predecessor meets the full hypothesis relevant to L023;
the replenishment does not exploit its earliest-boundary exception.
There is no claim of two competing predecessors: uniqueness remains
consistent with arbitrarily high valuation at a moving endpoint.

For the length assertion, apply the same finite coding and CRT to
W(2,3)^(K+1) followed by O. Regard the first word as the preceding
word and its endpoint as n. The remaining K words are all actual,
have exact tails, and start at V(n)=10 by (1). This construction
works separately for every finite K. A finite g(10) is contradicted
by choosing an integer K>g(10). The resulting n depends on K; there
is no fixed positive n or infinite itinerary furnished by CRT.

### Concrete guarded violation and verification

At R=3 a chain (2) is

\[
234391908855899\ \longrightarrow\ 563175774171227
\ \longrightarrow\ 1353148042359899
\ \longrightarrow\ 5486437597502045.
\]

For its middle word y=1603731013167287,
u=200466376645911 and z=5412592169439596=4m. The boundary
valuations are V(n)=10 and V(m)=14; after B^2 the valuation is 2.
Thus even the nonincrease inequality V(m)<=V(n) fails on an
extendible word. The two sides are respectively 14 and 10.

`python3 scripts/postspell-valuation/check_transport.py` verifies
all 43 actual input parities, the final odd guard, positivity and
residue membership at all four boundaries, all three exact tails,
the affine identities and the claimed valuations. Its full states
and arithmetic data are saved in `scripts/postspell-valuation/result.json`.
The complete `/states` and `/words` values were inspected, not just
a preview. There are no failed checks. This finite verification
supports transcription; the all-R and all-K statements follow from
the preceding proof, not from a parameter screen.

The stopped mechanism is a consumable budget in V of the starting
boundary alone. This calculation does not rule out budgets also
controlling the odd part, total height, later compensation, or extra
least-root restrictions. It proves no positive infinite chain and no
failure of Collatz convergence. It does not impose an endpoint cutoff.

## Mathlib

Full shifted-valuation transport/replenishment and supporting affine,
valuation, finite parity coding and CRT coverage: **not checked**.
No matching declaration, library absence or formal verification is
asserted. The primary finite coding result is imported, while the
specialization and all guards are justified above.
