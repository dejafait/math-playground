# Completed source comparison for actual ordinary local images

TARGET: Assess whether Sakamoto's rank-zero prime-deletion construction gives a computable ordinary p-local image for the classical classes in L024, distinct from Kim's p-singular reciprocity.
CHECKED: 2026-10-15
DECISION: EXPLORE
SEARCH_EVIDENCE: Six targeted ordinary-localization/rank-zero/basis queries and one cited-Kurihara-source query, recorded below, found no adequate finite ordinary evaluation procedure in the inspected package; compared L014/L017/L023/L024/L062 and ATTEMPTS/021/031/032 and reused their unchanged source coverage. Search failure implies neither novelty nor impossibility.
SOURCE_EVIDENCE: Sakamoto 2022, DOI 10.4171/DM/X21, Sections 2.4–2.5 pp.1903–1907, Theorem 3.4/Proposition 3.8 pp.1909–1911, Theorem 3.17 and proof p.1915, Corollary 4.10 and complete proof p.1920; Sakamoto 2021, DOI 10.5802/jtnb.1189, Section 5.2/Lemma 5.4 pp.1089–1091, including its component formula and three relation checks; Kim's author text dated 2025-05-12, Section 3.3/Proposition 3.10, Theorem 3.11 and (3.4), printed pp.19–20; Kurihara arXiv:1407.2465v1, Sections 3.2–3.4, author pp.19–24, especially (3.3), (3.5), (3.7) and Proposition 3.4.2.
COMPARISON: The sources construct classical classes and auxiliary coordinates or p-singular scalars, while the required global inverse-regulator/cohomology inputs are not supplied as finite computational data. Whole-system scalar injectivity is retained: this is no claim that the entire scalar collection cannot determine the system.
GAP: An actual finite ordinary coordinate and a successful same-depth localization certificate remain unproduced. A certified actual global Stark component with its localization, or independently computed finite Selmer representative, is still needed; the exponent and rational/complex-order gaps are separate.
REASON: Complete the source comparison negatively and park direct ordinary-image production from the inspected scalar/transfer package. Separately assess explicit descent with REVIEW_REQUIRED; no new mathematical model or lemma is authorized.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and asks for finite ordinary evaluation beyond the earlier ready scalar-exponent and conditional localization assessments; those unchanged assessments were reused.
SCOPE: L023/L024's actual selected pairs, supplied h and m>2h, coefficient ring Z/p^m and tensor generators remain fixed. Any later L062 application retains every L026 premise, an independent exponent and the actual same-depth test. No ordinary-image lemma or numerical production schedule is approved.

This completed literature comparison produces no new mathematical result,
ordinary local value, script or rank conclusion. It records the exact
source boundary and a negative production decision.

Main gap: arbitrary higher-analytic-order rank equality. Intermediate
target: a source-backed ordinary p-local evaluation of the actual classical
classes supplied conditionally by L024. Potential downstream use: an
independently testable successful-class input to L062 once an independent
finite-quotient exponent is available. A p-singular reciprocity value alone
does not satisfy this target.

Reused the source assessments of 2026-10-03's rank-zero construction,
2026-10-05's positive-valuation extraction and 2026-10-14's finite-depth
localization witness. Read L014's obstruction proof, L023's selected-pair
statement, L024's membership/localization proof and L062's same-depth
implication. L061's coefficient coverage is inherited through the ready
L062 assessment. L017's contraction statement already tests a divisor
subsystem; another formal contraction model would not supply actual
cohomology coordinates.

Retain all L024 selection and depth hypotheses, including its independently
granted finite length h and m>2h. Retain every L026 premise for a later
L062 application, the independent exponent, classical-class condition,
same-depth inequality and actual nonzero localization. No rational points,
rational Kummer membership, finite Sha, uniform auxiliary availability or
complex-order comparison may be inferred from a local evaluation. No
cross-notebook input is needed.

The continuation test sought a computable ordinary expression or a sharply
identified independent missing term. The latter is identified below but
not supplied; direct production from this package is parked. Preserve
L014 and ATTEMPTS/021/031/032 and the closed scalar cap. The negative is
about the inspected production procedure, not eventual computability or
ordinary nonvanishing. Mathlib coverage is not checked, with no absence
claim. No cross-notebook input is used.

## Primary statements and essential proof cases

**Sakamoto 2022.** Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Documenta Mathematica 27 (2022), 1891–1922, DOI 10.4171/DM/X21;
publisher text revised 2022-07-20. Conditions (a)–(c) are good ordinary
p>3, surjective E[p], and p prime to #E(F_p) and the Tamagawa product.
L024 retains these and its stronger premises. At cyclotomic layer zero,
the representation is E[p^m] over R=Z/p^m.

[Section 2.5, pp.1905–1907](https://ems.press/content/serial-article-files/29299?nt=1#page=15)
starts with a trivialization of H^1_/f(Q_p,T) and the resulting global
functional phi. The transfer takes inverse Reg_1 (Theorem 2.24), contracts
the canonical Stark system by phi, and applies Reg_0. Diagrams (2)–(4)
assert delta Phi=phi. The exact sequence on p.1907 identifies classical
relaxed-at-d cohomology as the kernel of phi on canonical relaxed-at-d
cohomology. It does not identify that kernel with its finite image at p.
The exterior-bidual construction retains nonfree coefficient modules.

[Theorem 3.17 and its proof, p.1915](https://ems.press/content/serial-article-files/29299?nt=1#page=25)
define the actual system as Phi D^1_(m,n)(z_xi). The normalization is
L_(Q_n,m) on H^1_/f, not a finite Kummer logarithm. The proof uses
Proposition 3.16's commuting derivative diagram.
[Theorem 3.4 and Proposition 3.8, pp.1909–1911](https://ems.press/content/serial-article-files/29299?nt=1#page=19)
give the singular Iwasawa Coleman isomorphism and a normalized global
Euler system. Their inspected global injectivity statement is not a
finite computational inverse for global cohomology at the required depth.

[Corollary 4.10 and complete proof, p.1920](https://ems.press/content/serial-article-files/29299?nt=1#page=30)
give a mod-p basis at a delta-minimal index. The proof uses Poitou–Tate,
relaxed/classical equality, off-diagonal zero auxiliary localizations,
and diagonal finite-singular coordinates -delta. These are coordinates
at primes dividing d; there is no displayed p-local finite coordinate.
L024 already specializes this mechanism with its working-depth
surjection. The mod-p basis conclusion does not apply at positive h.

Corollary 2.22, p.1904, says delta is injective on the **whole rank-zero
system**. It would be incorrect to claim two full systems with identical
entire scalar collections can give different classes. The present gap
is an effective finite evaluation from the data actually supplied.

**The missing cohomology component.** Sakamoto, *On the theory of
Kolyvagin systems of rank 0*, J. Théor. Nombres Bordeaux 33 (2021),
no.3, part 2, 1077–1102, DOI 10.5802/jtnb.1189.
[Section 5.2/Lemma 5.4, pp.1089–1091](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=14)
give the published component formula. With precisely the source's
ordered prime factors and bases, write
epsilon_(dq)=epsilon_(d,q) tensor (f_d^* wedge f_q^*). Then

\[
\kappa_{d,q}=(-1)^{\nu(d)}
 \epsilon_{d,q}\bigl(\mathop{\bigwedge}_{s\mid d}e_s^*\bigr)
 \otimes\mathop{\bigotimes}_{s\mid d}\sigma_s.
\]

Here e_s^* is localization followed by the /tr coordinate; the remaining
bidual argument gives the global class. This is a source formula, not a
new ordinary-local identity. The proof checks (5.1) via Reg_1, (5.3)
through the initial Stark component, and the signed (5.2) by contraction.
The setup uses a zero-dimensional Gorenstein ring and the paper's
standing representation hypotheses; the rigidity isomorphism further
uses Cartesian core-rank-zero conditions and a sufficiently rich prime
set. These conditions are not replaced by one scalar calculation.

For L024 the missing computational object is a certified coordinate
description of the **actual** epsilon_(d,q), after inverse Reg_1 and
p-singular contraction, together with finite localization of the
resulting cohomology element. Its scalar contraction is not that
description. No evaluation by a p-local functional, choice of a finite
projection on all relaxed classes, division by p^h or coefficient-natural
ordinary formula is derived here.

**Kim's map.** Chan-Ho Kim, *The structure of Selmer groups and the
Iwasawa main conjecture for elliptic curves*, publisher-hosted author
text dated 2025-05-12. [Section 3.3, Proposition 3.10 and Theorem 3.11,
printed pp.19–20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=19)
use H^1_/f, including the H^2 torsion term and its splitting. Equation
(3.4) identifies the normalized torsion dual exponential on this quotient;
Theorem 3.11 gives u p^t tilde-delta_n under residual surjectivity and
prime-to-p Manin constant. L014 already checks t=0 and genuine reduction
under local p-torsion vanishing. For an L024 classical class, quotienting
by the finite Kummer condition carries no ordinary coordinate. Kim's
theorem therefore does not evaluate the desired finite image. The
original rank-one and transferred rank-zero systems remain distinct;
no termwise identification without proof is made.

**Cited predecessor checked.** Masato Kurihara, *The structure of Selmer
groups of elliptic curves and modular symbols*, arXiv:1407.2465v1,
2014-07-09; published in *Iwasawa Theory 2012* (2014), pp.317–356.
Read [Sections 3.2–3.4, author pp.19–24](https://arxiv.org/pdf/1407.2465v1#page=19).
The standing assumptions additionally include algebraic mu=0. Equation
(3.3) starts with a global cohomology preimage of an auxiliary boundary
over a high cyclotomic layer and takes corestriction; (3.5) uses invariant
descent; (3.7) needs another global preimage b'. Proposition 3.4.2 controls
auxiliary boundaries/finite coordinates under its prime and admissibility
conditions. The preimages would themselves need certified cohomology
data. No identification of every predecessor class with L024's classes
is asserted or required for this comparison.

## Search, decision and continuation

Queries on 2026-10-15:

- `Sakamoto "p-Selmer" "localization" "p" basis`
- `"rank zero" "Kolyvagin" "logarithm" Sakamoto`
- `"prime-deletion" "Kato" localization ordinary`
- `"Sakamoto" "Selmer" "comput" "basis"`
- `"p-Selmer Group and Modular Symbols" "logarithm"`
- `"Kurihara" "Kolyvagin" "finite" "localization at p"`
- `"Kurihara" "The structure of Selmer groups" "modular symbols" pdf`

Other returned Heegner/height leads were not read or imported. Browser
PDF text supplied all essential passages above. Screenshot requests
exposed no images and a shell download failed at DNS; neither limits
the inspected text evidence or creates an essential-source blocker.

NEGATIVE records a changed production decision, not a new mathematical
discovery or a disproof. EXPLORE means no adequate evaluation procedure
was matched; it approves no new lemma or additional scalar schedule.
The independently testable continuation assesses explicit descent as a
source of finite Selmer representatives and actual local Kummer images,
with separate REVIEW_REQUIRED coverage. Rational membership and arbitrary
complex-order/rank comparison remain independent even after a successful
L062 localization certificate.
