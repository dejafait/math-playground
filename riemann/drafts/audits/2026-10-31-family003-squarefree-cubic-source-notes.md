# Squarefree cubic normalization — source-review record

Literature-only step, 2026-10-31. The saved target is L548's retained
composite normalization and unit modulus, restricted to squarefree primary
moduli outside S. Actual-Xi all-degree positivity is the main gap. A later
successful application could remove this finite premise; it would not
settle the independent theta coefficient, arithmetic uniformity or Xi-sign
questions. No lemma, mathematical script, DAG or argument overview is
changed here. No cross-notebook input.

## Retrieved evidence

The pinned OpenAI manuscript, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[*The Quasi-Riemann Hypothesis*, build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
was read at lines 519–591 (definitions) and 1826–1871 (the complete
finite normalization/norm argument and conversion). Its definitions are
for the composite modulus itself:

\[
 \chi_n(x)=\prod_{p\mid n}\chi_p(x)\quad(n\text{ squarefree}),\qquad
 \gamma_j(n)=q_n^{-1/2}\sum_{x\bmod n}\chi_n(x)^j e(x/n),
 \qquad \gamma_j(1)=1.
\]

The source defines chi_1 identically one; all powers are zero on
nonunits, even principal and negative powers. It identifies chi_n^2
with the ordinary cubic symbol. Its e is the notebook e, and its
q_n=|n|^2. These are source definitions, not a derived composite
factorization. The passage at 1826–1843 defines tilde-g_3(1)=1,
retains all cubic nonunit zeros, and gives a finite-field/CRT norm
argument and a unit-frequency scaling argument. Lines 1865–1871
restrict the sextic conversion precisely to (n,S)=1. The norm passage
also mentions the primary prime -2, but that wider coefficient domain
is outside this review's good-sextic target.

Dunn–Radziwiłł (DR), *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, 14 May 2024, Section 2](https://arxiv.org/html/2109.07463v3#S2),
was read at Section 1.2, (1.4)–(1.8), and the full Section 2 through
(2.3), including its primary-generator and splitting conventions.
The inspected statements are for primary c, rather than just primes:

\[
 g(c)=\sum_{x\bmod c}(x/c)_3\check e(x/c),\qquad
 g(c)^3=\mu(c)c^2\bar c,\qquad
 |\widetilde g(c)|=\mu(c)^2,
 \quad \widetilde g(c)=g(c)/|c|.
\]

Its coprime twisted multiplicativity is
\[
 \widetilde g(ab)=\overline{(a/b)_3}\,
                  \widetilde g(a)\widetilde g(b).          \tag{DR 2.3}
\]
The symbol factor must be retained in any prime-factor proof. The
direct all-modulus statement is adequate instead. Section 2 explicitly
allows split and inert prime ideals; squarefree means ideal-squarefree,
without a rational-squarefree condition or prohibition on conjugate
prime factors. These are unconditional finite statements, not the
paper's GRH-conditional prime averages. DR cites Hasse, *Vorlesungen
über Zahlentheorie* (1950), pp. 443–445; that upstream proof was not
independently read or certified here. DR is the inspected import.

The complete unit-shift proof in official Mathlib
[GaussSum.lean, lines 54–76](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54)
was also read. `gaussSum_mulShift_eq` assumes a finite commutative
source ring, a commutative target ring and a source-ring unit. It gives
inverse-multiplicative-character scaling of the additive shift. It is
not restricted to fields, so supplies a standard input for the later
composite normalization check. The later finite-field product/norm
theorem (lines 177–181) has a field hypothesis and must not be used
directly on a composite quotient. No complete Eisenstein normalization
or cubic unit-modulus theorem was found in this inspected file; global
Mathlib coverage was not checked. The modulus-one case can be handled
by the explicit source conventions, without applying a nontrivial-ring
or nonprincipal-character theorem to it.

## Search and comparison limits

External queries were `"cubic Gauss sums" "twisted multiplicativity"
squarefree` and `"Gauss sum" "gamma_2" "Quasi-Riemann"`. The primary
DR and pinned manuscript statements above supply coverage. Mirrors,
expositions, discussion pages and search snippets were leads only;
no theorem was imported from them. No novelty follows from this search.

Local searches covered the relevant L531–L558 finite-Gauss occurrences,
the family003 cubic/Fourier/reflection assessments and audit notes,
and the corresponding prime-audit histories. L556 proves only the prime
specialization and additive conversion; L557/L558 explicitly exclude
composite propagation. L548 retains the claim rather than proving it.
No completed exact composite audit was found in that scope. There is
no family003-named ATTEMPTS file; the broad keyword results in ATTEMPTS
were unrelated numerical uses of “composite.” Existing zero-support,
primary-unit and prime-product cautions remain in force.

## Decision and bounded continuation

SPECIALIZE: essential source coverage for the unchanged target is
complete. The later audit should import DR's all-primary-modulus norm
statement, verify the cubic/sextic character identification and the
unit-shift hypotheses on the whole zero-extended quotient, compare
normalizations, and check n=1 separately. It need not reprove cubic
Gauss theory or multiply prime sums. If it uses CRT instead, it must
account for the factor in DR (2.3). No such application, new identity
or discharge of L548 is completed in this literature turn.

Continue only on exact phase and norm agreement for all allowed
squarefree n. An unexplained unit/CRT factor, incorrect zero extension
or extra restriction prevents discharge. Good moduli only are assessed;
raw dual support, coefficients, uniform closure and Xi signs remain
unresolved. The new ready assessment requires the separate next-turn
gate approval. The finite sources do not yet provide a concrete
actual-Xi realization or sign mechanism for a justified creative target.
