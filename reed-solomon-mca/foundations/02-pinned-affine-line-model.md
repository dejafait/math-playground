# Pinned affine-line model and endpoint convention

Audit date: 2026-09-25. This freezes a readable, versioned model for a source
comparison. **It does not certify the unread July 6 ABF26 paper.** We use
\(E_C\), not an unqualified identification with the challenge's
\(\varepsilon_{\mathrm{mca}}\).

## Provenance

The official prize page links to the companion challenge. Its public
[dependency manifest](https://raw.githubusercontent.com/proximity-prize/proximity-prize/main/lake-manifest.json),
read on the audit date, pins upstream Verified-zkEVM/ArkLib at
`e65197892890b8fd9b0dc05b8980273cf1d595cc`. All ArkLib links below use that
immutable revision. The companion protocol itself is a separate problem.

The relevant declarations are `CoreDefinitions.IsMCA`, `mcaError`, and
`AffineLineGenerator` in
[ProximityGenerators.lean](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98).
They were read as source, not built or checked for their Lean axiom closure.

## Exact model

Let \(F\) be a finite field of size \(q\), let \(I\) be a nonempty finite
coordinate set of size \(n\), and let \(C\le F^I\) be a linear code. For
\(S\subseteq I\), write \(C|_S=\{c|_S:c\in C\}\). For real
\(\delta\in[0,1]\), define
\[
 E_C(\delta)=\max_{a,b\in F^I}\frac1q\left|\left\{\gamma\in F:
 \begin{array}{l}
 \exists S\subseteq I,\quad |S|\ge n(1-\delta),\\
 (a+\gamma b)|_S\in C|_S,\\
 a|_S\notin C|_S\ \text{or}\ b|_S\notin C|_S
 \end{array}\right\}\right|.
\]
The maximum is over all pairs, before uniform sampling of \(\gamma\) from
all of \(F\). The support and the matching codeword may depend on \(\gamma\).
Every qualifying support size is allowed, not only the smallest one. The same
support is used in both membership tests. At \(\delta=0\) only \(I\)
qualifies; at \(\delta=1\) all supports qualify, but the empty support cannot
witness failure. Degenerate directions are included and cause no difficulty.

The indexed primary PDF excerpt of Arnon, Chiesa, Fenzi, Yogev,
[*WHIR: Reed–Solomon Proximity Testing with Super-Fast Verification*,
Definition 4.8, p. 23](https://eprint.iacr.org/2024/1586.pdf#page=23),
has these support quantifiers for a general generator. Taking two inputs and
the generator \((1,\gamma)\) gives the displayed event. That antecedent
supports the event, not ABF26's current version or endpoint conventions.

## Domains, rates, and the source discrepancy

In the pinned code,
[`ReedSolomon.Smooth`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ReedSolomon.lean#L737)
means that the evaluation image is \(uH\), where \(u\in F^\times\),
\(H\le F^\times\), and \(|H|=2^m\). Ordinary RS codewords are evaluations
of polynomials of degree less than \(k\); in our range \(1\le k\le n\)
the rate is \(k/n\).

[`GrandChallenges.lean`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L63)
uses adjacent grid radii: safety at \(j/n\) and failure at \((j+1)/n\),
or safety at every grid radius through one. Its `prizeRate` gives
\(1/2,1/4,1/8,1/16\); `prizeThreshold` is \(2^{-128}\).
`PrizeDomainAdmissible` requires \(n\ge16\) and divisibility by all four
denominators, since its prize wrapper considers all four rates on one domain.
This extra wrapper condition is not silently attributed to the web statement.

`GrandMcaResolution.sublevel_iff` explicitly gives a right-open safe interval
at a crossing. The official web statement instead asks for a largest safe
real radius. A grid maximum, the supremum of safe real radii, and an attained
real maximum are distinct specifications. L001 checks the distinction directly;
C001a supplies an example at the actual error threshold. Neither fact certifies
which convention the current paper intends. The July bounds, any further
parameter restrictions, and this paper-to-model correspondence remain unread.

## Standard algebra used in the endpoint test

The finite-field existence theorem supplies a field of order \(p^r\) for
every prime \(p\) and positive integer \(r\). The multiplicative group of
a finite field is cyclic, hence has a subgroup of every order dividing
\(q-1\). The polynomial root bound says a nonzero polynomial of degree at
most \(d\) over a field has at most \(d\) roots; it follows by successive
division by \(X-\alpha\) at distinct roots. No coding-theoretic bound is
assumed in the endpoint example.

## Mathlib

Coverage of the full MCA model and endpoint example in **Mathlib: not checked**.
ArkLib is a separate library. Its declarations above supply a pinned source
for definitions, not evidence that Mathlib contains the full statements or
that the grand challenge has been resolved. Specific supporting ArkLib theorem
names and their scope are recorded with the endpoint lemma.
