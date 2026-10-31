# Full raw cusp coefficient envelope — source review

Literature-only step, 2026-10-31. Main gap: actual-Xi all-degree
positivity. The intermediate target is L548 (3), on its entire raw
support. Its possible use is removal of a coefficient-size premise in
the conditional reflection/tail argument. Arithmetic-uniform closure,
other finite inputs and signed-Xi transfer remain independent. No
coefficient application, new lemma or mathematical calculation is
completed here. No cross-notebook input.

## Primary coverage

Dunn–Radziwill (DR), *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, 14 May 2024](https://arxiv.org/html/2109.07463v3):
read (5.7)–(5.16), Appendix A rows 1,19,10, and Section 2
(2.1)–(2.3). Section 1.2 (1.7)–(1.8) agrees with the normalization.
Here is a locator map for the later application, not a new coefficient
formula:

| Input | Exact source cases to retain |
| --- | --- |
| (5.7), first three branches | arguments ±lambda^(3h-4) c d^3, ±omega lambda^(3h-4) c d^3, ±omega^2 lambda^(3h-4) c d^3; integer h>=1; respective Gauss arguments lambda^2, omega lambda^2, omega^2 lambda^2; factor 3^(h/2+2) abs(d/c) and the displayed unit phases |
| (5.7), fourth branch | argument ±lambda^(3h-3) c d^3; integer h>=0; Gauss argument 1; factor 3^(h/2+5/2) abs(d/c) |
| (5.13) | arguments lambda^(-4) c d^3, omega lambda^(-4) c d^3, omega^2 lambda^(-4) c d^3; factor 9 abs(d/c), the three Gauss arguments above, and displayed phases |
| (5.14) | negatives of the three (5.13) arguments; factor 9 abs(d/c), the same Gauss arguments, and its own displayed phases |
| (5.8) | c,d congruent to 1 modulo 3; c ideal-squarefree; no (c,d)=1 condition |
| Appendix A | d_1(mu)=tau(mu); d_19(mu)=omega^2 tau_1(omega^2 mu) check-e(mu); d_10(mu)=omega tau_2(omega mu) check-e(mu) |
| (5.12), (5.16) | nonzero lattice lambda^(-4)O; conjugate coefficient bar(d_j(-mu)); retain each family's otherwise-zero case |

The source statements are unconditional. Their hypotheses do not
exclude primes above 2 or any additional fixed S. Section 2 uses
all primary moduli and both split and inert primes. It states
g(c)^3=mu(c)c^2 bar(c), and abs(g(c)/abs(c))=mu(c)^2.
Hasse (1950), pp. 443–445, and Patterson (1977), Theorem 8.1,
(8.8)–(8.9), Table III p. 151, are upstream references, not independently
audited proofs. DR supplies the inspected formulas.

The claimed application is OpenAI, *The Quasi-Riemann Hypothesis:
A Zero-Free Half-Plane Re(s)>7/8*, 30 September 2026,
[build/paper.tex, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
read at 1806–1854. It asserts magnitudes
3^(k/6+8/3)|b| and 3^(k/6+3)|b| for tau, and 9|b| at k=-4
for tau_1,tau_2, then the envelope 27*3^(k/6)|b|.
Its complete cubic-only norm and unit-frequency scaling passage
1826–1846 explicitly includes the primary prime -2 of norm 4,
n=1, shared n,b primes and primes excluded from the primal sums.
These are source claims awaiting the separate local application audit.

## Local comparison and search

Read L548 (2)–(4) and its import/normalization paragraphs; read
L547's three conjugate coefficient formulas (9) and cusp identification.
Reuse the canonical-cusp and Mellin source assessments for that
identification and their retained-input boundary. Reuse the squarefree
normalization assessment's inspection of the finite-ring unit-shift
theorem; its good-sextic application in L548 is not an all-S proof.

The relevant distinction is between the earlier audited conversion
to gamma_2, whose domain avoids S, and the raw coefficient question,
which can use the ordinary cubic symbol without a sextic conversion.
The inspected all-primary DR norm statement supplies a source input
for this wider domain. A later specialization must check the unit
shifts for t=1,lambda^2,omega lambda^2,omega^2 lambda^2 on every
allowed modulus, including the empty modulus. No Gauss factorization
or theta reproof is needed; a direct citation plus its applicability
argument is preferable. This paragraph specifies work, not its proof.

Targeted local searches covered the family003 coefficient/cusp/Mellin
assessments, their source and critical-audit notes, and the corresponding
canonical-cusp and squarefree-composite histories. They retain the
coefficient-size premise. L547 (9) is already the coefficient identity,
so a second identity lemma would duplicate it. L548's last audit removes
only the good-squarefree normalization premise. Searching ATTEMPTS for
cubic-theta, DR and unit-Fourier terminology found only an unrelated
signed-Mellin record; its earlier pole obstruction is not a coefficient
bound. The existing unit-Fourier obstruction concerns restricted twisted
summation formulas, not these raw coefficient cases; do not reopen it.

External queries were `"cubic theta" "coefficients" "squarefree"
Dunn Radziwill` and `"27" "3^{k/6}" "theta"`. Further exact-source and
Mathlib-name queries returned no useful additional theorem evidence.
Returned expositions, other OpenAI manuscript variants, function-field
notes and quartic analogues were leads only, not inspected imports.
No novelty inference follows. A direct curl attempt failed DNS;
the essential primary passages were accessible through the web tool,
so this is not a persistent source blocker.

## Scope decision and discriminating test

SPECIALIZE: the source cases and standard inputs cover the hypotheses
needed to attempt the unchanged coefficient envelope. This is coverage
approval for a later reproduction, not a discharge of L548 (3).
The justification for auditing a known claim is that L548 explicitly
retains it, and the published formulas must be specialized to the
notebook's unmasked three-cusp conventions and numerical constant.

The later audit must track every unit/sign and otherwise-zero case;
translate h into k separately in both tau branches; test k=-4 and all
ramified exponents; check cubic norms at S-primes without sextic
characters; retain shared n,b factors and conjugation at -mu; and
compare each resulting size with 27*3^(k/6)|b|. Any missing case,
extra mask, nonunit Gauss shift or larger required constant blocks
discharge. Do not prove uniqueness of the support parametrization
unless actually necessary for this bound. Keep nonzero lattice indices
where the coefficient vanishes. The constant term is outside (3).

Mathlib: reuse the inspected supporting `gaussSum_mulShift_eq` in
[GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54),
as documented in the squarefree source notes. It works over a finite
commutative ring with a unit shift. The finite-field norm theorem is
not applicable directly to a composite quotient. Full matching cubic
theta and Eisenstein coverage has not been checked; no absence claim.

New continuations require separate gate approval. No central creative
nomination is justified by this size estimate alone: an actual-Xi
realization/sign mechanism and its discriminating test are still missing.
