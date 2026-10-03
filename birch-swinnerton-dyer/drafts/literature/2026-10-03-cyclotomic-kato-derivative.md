# Cyclotomic Kato derivative: source assessment

TARGET: Test whether the degree-one cyclotomic Kato derivative has a nonzero preimage in wedge^2(E(Q) tensor Q_p) under the Bockstein regulator, without assuming finite p-primary Sha.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the initial bounded searches below and completed the six focused derivative/finiteness, regulator, and later-source searches recorded in the completed audit; primary theorem statements, domains and the relevant descent proof were read.
SOURCE_EVIDENCE: Fresh reads: Burns--Kurihara--Sano, https://arxiv.org/pdf/1910.07404v2, Hypothesis 2.2, Section 4, Proposition 4.5, Definition 4.6 and Theorem 6.2; Sano, https://arxiv.org/pdf/2308.08875v1, Section 2 including Definition 2.7, Propositions 2.10/2.12 and Theorem 2.13 with its proof, and Sections 5.1--5.3; Castella--Sano, https://arxiv.org/pdf/2601.14504v1, Theorem A and Sections 2.1.3/2.2/2.3.1; Macias Castillo--Sano, https://arxiv.org/html/2603.23978v1, Theorem 3.4, Remark 3.14, Hypothesis 4.1 and Theorem 4.2. Earlier published-BKS, Banwait and Wiles reads below are reused with their original qualifications.
COMPARISON: BKS's rational identification and rank-indexed derivative retain finite p-primary Sha. Sano supplies a cohomological determinant regulator without that premise, with a dual H^2 factor and a degree determined by Bocksteins, but no identified rational Kummer exterior square; the inspected 2026 results govern Selmer groups or heights rather than remove this difference.
GAP: Establish the actual degree-one derivative's existence/nonvanishing and its regulator preimage's rational Kummer membership. Selmer dimension two alone does not identify the global cohomology complex, determine the derivative degree, or supply two rational directions.
REASON: Stop direct rational-certificate import and specialize the known determinant descent only for the bounded marked-Kummer/Sha model test specified below; import the formalism by citation, retain the original arithmetic target, and do not assume finite Sha, rank two or the conjectural leading-term formula.
SCOPE: The cohomological construction is covered under Sano's stated complex hypotheses; approval of the listed subtarget is for a formal sufficiency/obstruction test, with local conditions and duality tracked separately, and does not assert an arithmetic realization or the original rational certificate.
COVERED_TARGET: Test whether a dimension-two Selmer model can satisfy degree-one cyclotomic determinant descent, Kato characteristic divisibility and nonzero p-localization while its rational Kummer subspace is one-dimensional and its V_p Sha quotient is nonzero.

The initial screening below is preserved as the record of the preceding
step. Its REVIEW_REQUIRED statements describe that earlier stage; the
completed theorem-level audit later in this file supplies the decision
and scope above. The original TARGET is unchanged.

## Gap, threshold, and scope

The main target remains rank E(Q) = m(E) for every E/Q. Wiles's
[official statement, page 2](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2)
still distinguishes that assertion from the refined coefficient formula.
The assembled proof has not changed. On the current conditional
rank-two branch the available upper bound is r <= 2; r >= 2 and
q(kappa) = 0 are missing.

The proposed intermediate target asks for arithmetic information in a
cyclotomic leading class, rather than another representation admitting a
possible lift. A nonzero exterior square of actual rational Kummer
classes is the required two-direction certificate. A nonzero class in
an exterior square of a larger cohomology or Selmer space does not meet
that threshold. No such preimage or new implication is proved here.

For the prospective comparison retain non-CM E/Q, good ordinary p >= 5,
and the dimension-two Selmer space with nonzero p-localization from the
existing conditional branch. Use the cyclotomic Z_p-extension of Q;
there is no auxiliary anticyclotomic direction or W_d in this test.
Track any additional image, local-torsion, and integral hypotheses of
the source separately. Do not assume r = 2, finite p-primary Sha,
a nonzero rational regulator, or a complex/p-adic leading-term equality.
The existence and nonvanishing of an appropriate derivative are also
questions to screen, not consequences asserted from m(E) = 2.

If the proposed certificate became available, it could meet the missing
lower-bound threshold on that conditional branch. Production from
m(E) = 2 alone, uniform auxiliary/nonvanishing inputs, higher ranks,
and the refined formula would still remain unresolved.

## Three mechanisms compared

| Mechanism | Evidence and limitation | Recovery decision |
| --- | --- | --- |
| Inverse anticyclotomic BF specialization after a stable-lattice change | The [saved assessment](2026-09-26-eisenstein-kato-extension.md) already separates the coefficient construction from the unproved regularity and nonzero quotient of the actual class. | Park the exhausted recovery route. No further retrieval or renamed lattice test. |
| CM critical-Hecke-value criterion for the cyclotomic second coefficient | The newly inspected Banwait statement assumes rational rank two and concerns CM E itself. It is useful for a different coefficient/Sha question, but supplies no missing rational rank here. | Do not select it as this branch's lower-bound mechanism. Its proofs and cited inputs have not been audited. |
| Cyclotomic Darmon derivatives of Kato's actual zeta family | The BKS framework offers a different arithmetic object, with a sharp distinction between vanishing, regulators, and a leading-term comparison. Its rational scope without finite Sha remains to be screened. | Select the exact TARGET for a bounded source audit; keep REVIEW_REQUIRED. |

This comparison does not certify that any mechanism will work. It changes
the independent object to be tested, not the mathematical target or the
calculation budget. The prior obstructions in ATTEMPTS/001--011 remain.

## Primary statements actually inspected

Burns--Kurihara--Sano, *On derivatives of Kato's Euler system for elliptic
curves*, J. Math. Soc. Japan 76 (2024), 855--919,
[published author PDF](https://kurihara.math.keio.ac.jp/bks4.pdf): read
Sections 1.2--1.3, Section 3's statements, and Section 4's opening.
Theorem 1.3 assumes finite p-primary Sha over F; Propositions 3.3--3.4
retain finiteness premises despite Section 3's broader opening scope.
Section 4 starts by assuming finite p-primary Sha over Q. Theorem 1.9
(Theorem 6.2) is the generalized Rubin formula. Conjecture 1.6 explicitly
assumes rank equality; Corollary 1.11's complex/p-adic comparison is
conditional on it. These are supporting statements, not a matching
unconditional rational-certificate theorem. The journal numbering is
used; the [arXiv record](https://arxiv.org/abs/1910.07404) is an earlier
2020 v2, not the version cited here.

Banwait, *Second derivatives of p-adic L-functions and the
Shafarevich--Tate group of rank-two CM elliptic curves*,
[arXiv:2609.08431v1](https://arxiv.org/abs/2609.08431v1), 2026-09-08:
read [Theorems A--B, PDF pages 3--4](https://arxiv.org/pdf/2609.08431v1#page=3).
Both assume CM by the maximal order, rank E(Q) = 2, L(E,1) = 0,
root number +1, and a good split p >= 5 outside the stated excluded
set. They relate a unit normalized second coefficient to regulator/Sha
conditions and critical Hecke values. They do not infer rational rank
from analytic rank two. This is a preprint statement comparison; its
proofs and formalization are not treated as checked inputs.

The saved Eisenstein source review is sufficient for the completed
old target. Its citations and exclusions are reused. No additional
retrieval of those papers was needed or attempted in this turn.

## Search and access record

Queries on 2026-10-03:

- `elliptic curves rank two p-adic converse theorem derived Beilinson Kato classes higher rank Birch Swinnerton Dyer`
- `elliptic curves rank two explicit rational points descent p-adic L-functions Stein Wuthrich rigorous certificates`
- `elliptic curves supersingular rank two complex order p-adic L function signed regulator theorem`
- `derived Bockstein regulators p-adic Birch Swinnerton Dyer conjecture Sano theorem rank higher 2025 2026`
- `derived Beilinson Kato elements elliptic curves higher rank Burns Sakamoto Sano theorem generalized Perrin Riou`

The BKS and Banwait primary PDFs were accessible. An attempted BKS
HTML URL ending in v3 returned 404; the arXiv record lists only v1/v2,
and the published PDF supplies the inspected statements. Do not retry
that nonexistent version. PDF screenshots returned no inspectable image
through the tool; the actual PDF text was read instead.

Sano's [arXiv:2308.08875](https://arxiv.org/abs/2308.08875) abstract was
read as a follow-up lead. Its theorem statements and proofs were not
read, so it supplies no coverage. The derivative/regulator constructions
in BKS Sections 4--6, their proof dependencies, and relevant later
specializations have not yet been audited for TARGET. Search snippets,
secondary summaries, numerical tables, and claimed complete proofs
elsewhere are not mathematical inputs. This search is not exhaustive
and establishes no novelty.

## Concrete continuation and abandonment test

The bounded audit must locate the use of finite Sha in Hypothesis 2.2,
Proposition 4.4, Definition 4.5, and Theorem 6.2, and separate existence
of a degree-one derivative from identification of its coefficients with
actual rational Kummer classes. Check the domain of the Bockstein map
before asking for a preimage: using the unknown rational rank as the
index of an already available regulator would be circular.

Continue only if the constructions give a precisely stated subtarget
without assumed rank equality or finite Sha, together with an arithmetic
test for the marked rational image. An actual cohomological construction
with a separately identified rationality gap is useful intermediate
coverage; it need not already prove the whole BSD passage. Import the
covered construction by citation and justify only the remaining
specialization. Stop a proposed direct import if it needs the excluded
finiteness premise, returns only a Selmer exterior square, or uses the
conjectural leading-term formula. Restating that missing premise will
not count as another informative result.

This is a new bounded literature exploration, not a mathematical
advance. No lemma, regulator, derivative, rank bound, or candidate
resolution is constructed. REVIEW_REQUIRED deliberately leaves the
new target unapproved for mathematics; completing this source audit is
the next task recorded in PROGRESS.md. Literature work has not spent
or renewed the mathematical exploration counter.

## Completed theorem-level audit, 2026-10-03

### Exact BKS applicability and version distinction

The published author PDF was not accessible during this audit. Reuse the
previously inspected published statements above; do not describe them as
freshly retrieved. The accessible primary
[arXiv:1910.07404v2](https://arxiv.org/pdf/1910.07404v2), submitted 2020-04-17,
was read instead. Its numbering differs: the cyclotomic divisibility is
Proposition 4.5 and the derivative is Definition 4.6, on PDF pages 24--25,
rather than the published Proposition 4.4/Definition 4.5. The new
comparison cites the actually inspected version.

[Hypothesis 2.2 and (2.2.1), PDF page 12](https://arxiv.org/pdf/1910.07404v2#page=12),
include finite p-primary Sha in the identification of global H^1 with
rational points. [Section 4, PDF page 21](https://arxiv.org/pdf/1910.07404v2#page=21),
retains finiteness throughout. In Proposition 4.5's proof the rank of
base H^2 is identified with a = max(0, r_alg - 1) before Kato divisibility
is applied. Definition 4.6 uses that same a, and
[Theorem 6.2, PDF page 39](https://arxiv.org/pdf/1910.07404v2#page=39),
explicitly invokes Hypothesis 2.2. These statements do not license
setting r_alg = 2 from Selmer dimension two.

This excludes importing their rational rank-indexed construction under
the retained assumptions. It does not assert that a derivative cannot
be constructed with a cohomological index, or that a rational preimage
is impossible. The original arithmetic target remains open.

### The available construction without finite Sha

Read Sano, *Derived Bockstein regulators and anticyclotomic p-adic Birch
and Swinnerton-Dyer conjectures*,
[arXiv:2308.08875v1](https://arxiv.org/pdf/2308.08875v1), submitted
2023-08-17. Section 2 is algebraic. Its setup requires a bounded complex
C whose localization at I is represented in degrees one and two by
finite free modules, with H^1(C)_I free and nonnegative rank difference.
Here C_0 is the derived augmentation specialization, not a replacement
of its cohomology by Mordell--Weil points.

The source's regulator has the determinant domain

\[
\mathbf Q_p\otimes
\left(\bigwedge^{r_T+e}H^1(C_0)\otimes
      \bigwedge^e H^2(C_0)^*\right),
\]

with e the cohomological H^2 rank. See
[Definition 2.7 and (2.2.1), PDF page 10](https://arxiv.org/pdf/2308.08875v1#page=10),
and [(2.4.1)/Theorem 2.13, PDF pages 13--16](https://arxiv.org/pdf/2308.08875v1#page=13).
The dual H^2 factor must be retained, or trivialized by an explicit
choice. The proof of Theorem 2.13 computes the determinant maps in a
normal form over the augmentation DVR. It does not use a marked
Mordell--Weil subspace. Cite this theorem for descent rather than
reproving the determinant identity.

[Proposition 2.10, PDF pages 11--12](https://arxiv.org/pdf/2308.08875v1#page=11),
specifies the degree through the augmentation lengths and successive
Bocksteins. Proposition 2.12 identifies the final Bockstein kernel with
universal norms. Neither statement identifies that kernel, or the
determinant preimage, with rational Kummer classes. The ordinary first
Bockstein is available without finite Sha; use of the first regulator
as the leading-term map also needs the relevant first-cokernel condition.
Higher augmentation blocks cannot be ignored merely because the base
Selmer dimension is two.

The arithmetic hypotheses are explicit in
[Hypothesis 5.1, Example 5.2(ii), Hypothesis 5.3 and Remark 5.4, PDF pages 34--36](https://arxiv.org/pdf/2308.08875v1#page=34).
For the cyclotomic Tate module over Q, E(Q)[p] = 0 gives the required
torsion/freeness setup with Sigma empty and basic rank r_T = 1; the
weak Leopoldt assertion is supplied by Kato's Theorem 12.4(1), as cited
there. Basic rank one is not a claim that rational rank is one. Finite
Sha is not among those hypotheses. General cohomology and the ordinary
Selmer complex must still be distinguished: the former has basic rank
one, while the self-dual ordinary Selmer complex has different Euler
characteristic and local conditions. Their specialized H^1 spaces may
not be identified without an applicability argument.

[Conjecture 5.5, Remark 5.7 and Theorem 5.9, PDF pages 36--37](https://arxiv.org/pdf/2308.08875v1#page=36),
separate the algebraic descent from an analytic special-element
identification. Theorem 5.9 assumes both the Iwasawa main conjecture
and the leading-term conjecture; it does not prove the latter. No such
equality, first-Bockstein nondegeneracy, nonzero degree-one coefficient,
or determinant lift of the actual Kato element is asserted here.

### Later relevant results checked for a stronger conclusion

The author research page supplied two later primary leads. Their arXiv
records list v1 as the available version on the check date.

Castella--Sano, *On refined nonvanishing conjectures by Kurihara and
Kolyvagin*, [arXiv:2601.14504v1](https://arxiv.org/pdf/2601.14504v1),
submitted 2026-01-20: read Theorem A, the introduction's hypothesis
comparison, Theorem 2.1.4, Section 2.2 and Proposition 2.3.1. Theorem A
relates refined modular-symbol nonvanishing to the cyclotomic main
conjecture under its surjectivity and Manin-constant hypotheses.
Section 2.2 supplies a determinantal formulation, but Proposition 2.3.1's
finite strict Selmer conclusion concerns a character specialization
with nonzero specialized Kato class. It does not transfer that finiteness
to the trivial character with a vanishing base class or construct a
rational exterior-square preimage of its derivative.

Macias Castillo--Sano, *On Selmer complexes, Stark systems and derived
p-adic heights*, [arXiv:2603.23978v1](https://arxiv.org/html/2603.23978v1),
submitted 2026-03-25: read Theorems 1.1/1.5/1.7, Theorem 3.4 with its
core-vertex and local hypotheses, the displayed Selmer conclusion of
Theorem 3.12, Remark 3.14, and Hypothesis 4.1/Theorem 4.2. Determinants
give Stark systems and Fitting ideals of Selmer groups; the cyclotomic
remark is still a Selmer-group statement. The height comparison acts
on the compact Selmer filtration and retains its Tamagawa, reduction
and image hypotheses. These supporting results do not identify the
Selmer lattice with the rational-point lattice. Their full arithmetic
proofs and all cited inputs were not audited for import.

No inspected stronger result matches TARGET. This is a bounded source
comparison, not an exhaustive search or a novelty assertion.

### Approved bounded test and stopping threshold

SPECIALIZE covers the cohomological determinant construction by
citation and the exact COVERED_TARGET above. The next calculation may
test formal sufficiency using a localized degree-one/two complex with
free rank-one Iwasawa H^1, torsion H^2, and base cohomological dimensions
two and one. It must track the first Bockstein, its H^2-dual factor, the
derivative degree, and the determinant descent square explicitly.
Treat characteristic divisibility and a nonzero degree-one derivative
as test premises; do not claim they have been established for the
current elliptic curve from m(E) = 2.

Mark the rational Kummer image and its Sha quotient separately. Retain
nonzero p-localization and the local-condition/duality maps used to
identify the Selmer subspace, rather than marking an arbitrary line
as arithmetic without checking compatibility. A dual complex alone
does not provide the local-condition triangle. The relevant
[duality conventions](../../foundations/10-selmer-bockstein-duality.md)
and the source statements above are available supporting inputs.

The discriminating question is whether these formal data forbid a
one-dimensional Kummer image with nonzero quotient. A compatible model
would stop inference of rational rank two from these data alone and
identify the missing arithmetic premise. Failure to construct one is
not evidence that the desired rationality theorem holds. Continue an
arithmetic direction only if a concrete additional Kummer constraint
is isolated; do not reopen the parked Eisenstein route or infer an
elliptic-curve realization from a formal model.

This test is different from L002's characteristic-order/Jordan-block
ambiguity and L011's anticyclotomic strict/relaxed determinant. It fixes
the cyclotomic degree-one descent and asks whether that additional
datum distinguishes the rational image from Sha. Repeating either old
model without the descent and local-condition checks would be redundant.
The required threshold is still a nonzero exterior square of actual
rational points, beyond the available conditional upper bound r <= 2.
Production/nonvanishing from analytic rank two, uniform auxiliary
hypotheses, higher ranks and the complex/p-adic comparison remain open.

The review supplies new source-scope evidence and replaces direct
rational import with this independently testable subtarget. It is a
literature NEGATIVE, not a mathematical rank improvement. No formal
model or new result is derived in this turn. The source constructions
are known results; the remaining rationality assertion is unproved and
its originality is not certified. The calculation counter is unchanged.

### Search, access and reuse record for the completed audit

New queries were:

- "Kato" "Bockstein" "finite" "Shafarevich" derivative rational rank two
- "Darmon derivative" "Selmer" "finiteness"
- "derived Bockstein regulators" "elliptic curves" Sano
- "On derivatives of Kato's Euler system" "4.4"
- "On derivatives of Kato" "6.2"
- "On Selmer complexes, Stark systems and derived p-adic heights"

Two further access/locator queries used the BKS title with "2024 doi"
and with "Hypothesis 2.2". Author/journal PDF retrievals timed out or
returned no text; a shell fetch could not resolve the author host.
The accessible fixed BKS v2 and Sano v1 PDF/HTML supply the statements
used in the completed comparison and the approved formal test. No
essential source for that test remains unread; reproducing the precise
published normalization is outside its scope. Do not repeat this access
blocker as a reason to defer the model test.

The Clay page still links Wiles's official statement. Reuse the earlier
theorem-level scope read, the Banwait exclusion and the Eisenstein
assessment; none was mechanically reread. Search snippets, unrelated
claimed BSD proofs and secondary commentary are not mathematical
inputs. Page locators above count PDF pages, starting at one.


## Mathlib

Full Mathlib coverage of TARGET and the approved formal test: **not checked**. Supporting coverage for
Darmon derivatives, Bockstein regulators, and rational Kummer images:
**not checked**. The named paper statements above cover the cohomological
construction and support the scope comparison; none is claimed as a full TARGET match or a
Mathlib theorem. The Banwait preprint's conditional formalization is
not an independent verification of its literature inputs.
