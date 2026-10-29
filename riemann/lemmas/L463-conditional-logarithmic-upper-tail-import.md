# Lemma 463: conditional logarithmic upper-tail positivity (source import)

## Hypotheses

Let Ξ(z)=ξ(1/2+iz) be the actual entire completion of L018. For real a define

    H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0) D_n(Ξ;a)y^(2n).

The variable y is complex and coefficients are holomorphic Taylor
coefficients. This is not a modulus-square definition for complex y.

Retain precisely L461's external premise: OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, specialized to ζ, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Thus ζ has no zeros in
Re(s)>7/8; the pole at 1 is allowed and no boundary exclusion is assumed.
The [pinned source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
and [external-input register](../foundations/2026-10-quasi-riemann-input.md)
specify the retained manuscript/import-closure audit limitations.

Import the Xi conclusion of bramble_trace, *Generalized Laguerre
positivity at growing orders*, [rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026 at 07:18 UTC, Theorem 1b, equation (4b),
with definitions (1)–(2). The statement and version were checked on
25 October 2026. Its proof is Sections 4.2–4.5, including the tail
overlap and shifted-saddle cases (18a)–(18n). Those cases have source
coverage in the [assessment](../drafts/literature/2026-10-25-initial-laguerre-sign-coverage.md),
but this import is not an independent critical audit of that manuscript.

Fix a real c_0>3/8. All logarithms are natural.

## Conclusion

There exists A_(c_0)>2π such that, simultaneously for every real a
with |a|≥A_(c_0) and every integer n≥0 satisfying

    2n ≥ c_0 log(|a|/(2π)),

one has D_n(Ξ;a)>0. The onset is independent of n and there is no
upper order cutoff. Centers with Ξ(a)=0, of any multiplicity, are
included under the same quantifiers.

The onset is existential, with no effective bound or asserted overlap
with any finite verified height range. No conclusion at c_0=3/8,
uniformity as c_0 decreases to 3/8, or sign below this order threshold
is asserted. This is a KNOWN_IMPORTED conditional partial result,
not a local proof of either external theorem or of RH.

## Proof

The cited Theorem 1b assumes 1/2≤σ_0<1 and no ζ zeros in
Re(s)>σ_0. It supplies, for each fixed c_0>σ_0−1/2, a single
T_(c_0,σ_0) such that its expression ℒ_p(Ξ;t) is strictly positive
at every t≥T_(c_0,σ_0) and every order 2p≥c_0 log(t/(2π)), with
no upper order restriction. Take σ_0=7/8, using exactly the retained
external premise. The resulting lower requirement is c_0>3/8.
Increase the supplied onset if necessary to obtain A_(c_0)>2π.

Equation (2) of the source uses Ξ(t)=ξ(1/2+it), the completion of
L018. Equation (1) defines ℒ_p(f;t) as [y^(2p)]f(t+iy)f(t−iy).
Hence its p is exactly the present n. Explicitly, multiplying the
Taylor series gives

    D_n(Ξ;a)=Σ_(j=0)^(2n) (-1)^(j+n)
                    Ξ^(j)(a)Ξ^(2n−j)(a)/(j!(2n−j)!),

since i^j(−i)^(2n−j)=(−1)^(j+n). Entirety justifies this finite
coefficient identity at every center. It agrees with source (1),
with no rescaling by the auxiliary Hardy normalization b(t).
Thus the source sign is precisely D_n(Ξ;t)>0 for positive t in
the stated range.

For a≤−A_(c_0), set t=−a=|a|. Evenness from L018 gives the
identity of entire functions of y

    H_(−t)(y)=Ξ(−t+iy)Ξ(−t−iy)
             =Ξ(t−iy)Ξ(t+iy)=H_t(y).

Consequently D_n(Ξ;−t)=D_n(Ξ;t), and the same onset and order
inequality apply to negative centers.

The source theorem has no nonvanishing condition at t itself.
Its all-order extension includes repeated and zero local roots
(Sections 4.2–4.4), rather than dividing by Ξ(t)^2. The coefficient
identity and evenness argument above likewise never divide by Ξ(a).
Thus no central-zero exclusion, simplicity assumption, or additional
onset depending on n or multiplicity has entered this specialization.
This invokes the full cited theorem, not a reproof of its analytic
estimates. ∎

### Critical application audit — 25 October 2026

Verdict: the stated application passes without correction. This checks
the import and its elementary specialization, not either manuscript.
The primary page still displays v4, 24 October 2026, 07:18 UTC.
Definitions (1)–(2) and Theorem 1b (4b) match the citation above.

For normalization, each term contributing to degree 2n has indices
j and 2n−j. Its phase is
i^j(−i)^(2n−j)=i^(2n)(−1)^(2n−j)=(−1)^(n+j).
The two Taylor denominators are exactly those displayed above;
there is no extra (2n)! or b(a)^2 multiplier. The source coefficient
index p is n here, whereas its auxiliary total degree is 2p.
Entirety permits coefficient extraction from the locally convergent
product. The product is even in y and real for real y by L018's
conjugation symmetry, so its coefficients are real and the sign
comparison has its ordinary real meaning.

The source order quantifier follows its height quantifier with a
single T_(c_0,σ_0). Fixing σ_0=7/8 and taking, for example,
A_(c_0)=max(T_(c_0,7/8),2π+1) preserves every allowed integer n.
For negative a, evenness identifies entire products, hence every
coefficient; replacing t by |a| preserves the exact logarithm and
uses that same onset. No separate limit in n is taken.

The central-zero qualification was checked against source
(18e)–(18h): zero roots remain in the finite local factor, with
positive normalization defined without division by Ξ(t)^2.
Section 4.5, (18k)–(18n), supplies the lower-order range and its
overlap with Theorem 1a. These are inspected source cases, not
independently verified estimates. In particular the import invokes
the theorem, not formula (4) outside its stated range.

No new mathematical input or DAG edge is needed: L018 supplies the
completion and symmetries, while the two external statements remain
explicit hypotheses with their recorded versions and audit limits.
No boundary exclusion, effective height, initial sign, or RH conclusion
has entered this audit. The coefficient and symmetry proof above
remains the complete local applicability argument.

## Mathlib

Full matching coverage for this conditional, simultaneous upper-tail
statement has not been checked; absence is not asserted. No Mathlib
formalization or independent manuscript/import-closure verification
is claimed by this source import.
