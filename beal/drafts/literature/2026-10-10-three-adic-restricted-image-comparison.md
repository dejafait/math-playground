# Three-adic restricted connecting-image comparison — source scope approved

TARGET: Compare the primitive whole-fiber, whole-fiber and unrestricted three-adic connecting images using L047 and L048.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact 54a1/local-three, square-coordinate/whole-fiber and X0(11)/Kummer searches recorded in the realization and unrestricted-image assessments; narrowly compared L033, L035 definitions, L046 definition precedent, L047/L048 and ATTEMPTS/013–015. No duplicate completed three-adic restricted comparison was found; no novelty inference is made.
SOURCE_EVIDENCE: Reused inspected FNS June 10, 2019 manuscript Section 5 pp.17–18, Section 7.2 p.25 and Table 5 p.27; Schaefer–Stoll June 13, 2001 manuscript Lemmas 4.2–4.5 pp.6–7 and Section 5 pp.8–10; Clark Theorem 1.79 p.58. Reopened Stacks Lemma 26.17.2, tag 01JQ, statement and complete tensor-product proof on 2026-10-10.
COMPARISON: General source theorems and the independently audited L047/L048 applications cover the needed fiber, common-witness and unrestricted-map inputs. They do not state this combined restricted-image comparison; only its set definitions and tautological-point applicability remain to assemble, with no new field calculation or general theorem reproof justified.
GAP: A later mathematical step must transfer an entire-fiber isomorphism to a point under the same connecting map, establish restricted nonemptiness using L047 and decide the three sets using L048. This literature review asserts no restricted equality, strictness or emptiness verdict.
REASON: Essential source coverage is adequate for one REPRODUCTION assembly of the unchanged target; source reuse avoids another unrestricted-image audit or witness search.
SCOPE: Only L033's dual five-isogeny and 54a1 algebra at three, with the complete L034 modular fiber and L032 three-adic conditions. All isomorphisms, embeddings, exceptional evaluations and class collisions are retained; no global arithmetic or other twist.
LITERATURE_REASON: The target adds primitive whole-fiber and common-witness conditions to an assessment explicitly limited to the unrestricted image; review only this added interface.

## Gap, use and discriminating test

The main gap is unconditional global emptiness for 54a1, including
L045's unevaluated quotient classes. Other twists and infinitely many
residual signatures remain open. The intermediate target is the exact
comparison of the three local connecting images specified below. Its
plausible downstream use is deciding whether the additional primitive
fourth-power filter at three supplies any further global class condition.

Continue only to one exact comparison with restricted nonemptiness
justified when needed, or an identified missing interface. A singleton
unrestricted image by itself is insufficient. If the assembly shows no
additional restriction, retire this particular filter without another
witness enumeration or repeated audit. No local result implies global
emptiness or an integer solution.

## Exact approved definitions and interface obligations

Use A3=K tensor_Q Q3, E0, E1, theta:E1 -> E0 and delta exactly as
in L033 and L048. Use L034's complete projective modular map j.
For every finite s in Q3 other than 0 and 1728, B_s denotes the
coordinate algebra of the entire scheme-theoretic fiber j^-1(s).
Use the following definitions, matching L035/L046's definitions with
only the base field and the appropriate local witness conditions changed:

- I_all is delta(E0(A3)), in A3^*/A3^{*5}.
- I_fiber ranges over every such s and every Q3-algebra isomorphism
  B_s -> A3, applying delta to the tautological point of that fiber.
- I_pow uses exactly the same data, additionally requiring one common
  nonzero a,b,c in Z3 with min(v3(a),v3(b),v3(c))=0,
  a^3+b^4=c^11, s*c^11=1728*a^3, a=1 modulo 3,
  b^2=1 or 4 modulo 9 and c a unit.

The same c must satisfy the complementary scalar identity. No positivity,
parity or conditions at two are added over Q3. Neither restricted set is
assumed a subgroup or nonempty. Do not replace the entire isomorphism
by a selected homomorphism into one factor, restrict the allowed
isomorphisms, or require an arbitrary choice of affine generators.
The universal fiber inclusion supplies the tautological-point interface;
the later proof must state its direction from an algebra isomorphism
and use the same delta, rather than just match dimensions.

Essential inputs: L033's unconditional curves, field, dual-kernel/Kummer
and good-divisor interface; L034's complete map/fiber interface; L047's
audited common witness and whole-fiber identification; L048's audited
entire local algebra and unrestricted image. L032 supplies only the
listed local conditions. Their original integer-solution hypotheses
are not assumed in constructing a local witness. L035 and L046 are
only definition/method comparisons, not three-adic theorem inputs.
No cross-notebook input is used.

## Primary sources and applicability comparison

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. 156 (2020), 77–113,
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019: Section 5 pp.17–18 supplies the explicit (13,7,54a1)
pair and scaling criterion; Section 7.2 p.25 supplies the entire
canonical twelve-subgroup fiber, with Table 5 p.27 identifying K.
Reuse their inspection in the realization and realization-audit
assessments. The later GRH-dependent Selmer columns are not inputs.
L047's independent audit already checks the added square-coordinate,
common-c specialization and full base change. No new root lifting,
covariant calculation or field computation is needed for this comparison.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS 356 (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, Lemmas 4.2–4.5 pp.6–7 and Section 5 pp.8–10.
Reuse the unrestricted-image assessment and foundation 15's precise
inspection record: away from kernel exponent five and with neither
Tamagawa number divisible by five, the connecting image is unramified
cohomology, with size equal to the rational kernel count. L048 has
already audited these hypotheses over the entire degree-twelve field,
including actual residue field and good reduction. This is stronger
than a calculation at a selected point, but does not alone establish
restricted nonemptiness. Section 5's good-divisor evaluation applies
to the same dual map, including zero/pole cases; f(T)=0 cannot be
used as an ordinary multiplicative class. Import this general theorem,
not an independent descent reproof.

[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ),
statement and complete proof reopened 2026-10-10, covers affine fiber
products by the spectrum of a tensor product. This covers the base
change of the entire finite affine canonical fiber. Its hypotheses
are affine schemes over the same base; it does not identify the
rational fiber with K by dimension alone. That identification is
FNS's imported input, already specialized and audited in L047.
The old assessment's Section 26.17 tag 01JO is a section locator;
01JQ is the precise lemma locator used here and in L047's audit.
The tautological-point step uses the fiber inclusion and the usual
contravariant affine-scheme/algebra correspondence, already implicit
in the inspected tensor-product proof and L035/L046 definitions.
No new geometric theorem or specialization is established in this review.

Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision unidentified, Theorem 1.79 p.58: complete nonarchimedean field,
integral polynomial and approximation, strict |f(r)|<|f'(r)|^2.
The realization assessment and L047 audit already inspect and check
both applications; this review does not repeat them. No cube/fourth-root
surjectivity at three or fresh extension theorem is required.

## Duplicate, failure and continuation record

The exact-target searches are reused from
[realization coverage](2026-10-10-three-adic-whole-fiber-realization.md)
and [unrestricted-image coverage](2026-10-10-three-adic-unrestricted-connecting-image.md).
The [realization audit coverage](2026-10-10-three-adic-realization-critical-audit.md)
records the essential base-change inspection. These sources contain
no inspected theorem stating this combined restricted comparison.
This is an application-scope difference, not evidence of novelty.

ATTEMPTS/015 retires primitive whole-fiber nonexistence at three;
the proposed class comparison is a different test, not a reopening.
ATTEMPTS/014 records the corresponding completed filter at two;
its residue fields and image theorem application are not transferred.
ATTEMPTS/013's exhausted polynomial boxes and absent certified global
class data are preserved. No larger witness search is justified here.

There is no essential source blocker for the bounded assembly.
No GRH, rank, Sha vanishing, class data, Selmer/point equality or
compatibility with a single global integer triple is assumed. Global
intersection and all other twists remain independent unresolved gaps.
Mathematical exploration usage stays 1/3. Full matching and supporting
Mathlib coverage remain not checked; unknown is not absence.
This is LITERATURE / NOVELTY_UNCHECKED scope approval, not a new
mathematical result. The ready continuation requires the supervisor's
separate next-turn approval before its mathematical invocation.
