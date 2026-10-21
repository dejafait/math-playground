# New-member native field hypotheses — source scope approved

TARGET: Compare L087's G_star with IUT I Definition 3.1's exact field-generation and Galois hypotheses, including the same-member native moduli and tripodal fields.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step346 searched exact native Galois/Legendre terminology, inspected the author-hosted passages below and reused the ready old-member moduli assessment. Compared L087's hypotheses/conclusion and same-member invariant check, L086's rational model, L079's cited method and native-field proof, foundations/05 step272, and ATTEMPTS/033–034. No inspected source supplies the combined bespoke G_star verdict; no novelty is inferred.
SOURCE_EVIDENCE: Fresh author-hosted IUT I https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf (May 2020, 186 pages), Definition 3.1(a)–(c), printed pp.61–62; IUT IV https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf (April 2020, 87 pages), Proposition 1.8(ii),(iii),(iv),(vi) pp.18–21 with relevant proofs, Theorem 1.10 opening p.22, Corollary 2.2 opening and (ii) pp.41–42 and proof opening pp.43–44. Reuse the precise supporting sources and versions below.
COMPARISON: Native definitions and ready punctured/pointed and automorphism methods cover a later application to L087's fixed rational member. Definition 3.1(b)'s Galois base and IV's additional equality must be checked separately. The old L079 conclusion is not transferred; L087 already supplies the actual coefficient/root-field equality and index four as inputs.
GAP: Essential source coverage is complete; the same-member native-field identification and admissibility screen must still be written in a separate research turn. Independent initial data, Corollary 2.2 applicability and original finite B>=A remain unresolved.
REASON: This review closes the changed-member source-scope gap and corrects the attribution of field generation to Definition 3.1; it approves a known-method specialization without deriving the new native conclusion.
SCOPE: Exactly TARGET for L087's fixed E_star, literal E_L_star, t_star and G_star in its embedding. No normal-closure substitution, old-witness verdict, transfer of independent initial data, Corollary 2.2 counterexample or original volume comparison.
LITERATURE_REASON: Changed-member native applicability and the relation between field generation and the Galois hypothesis were outside L087's construction/audit scope; the old native assessment fixes another witness.

## Gap, downstream use and stopping test

The main gap remains original finite B>=A. The intermediate target is
TARGET. Its downstream use is a justified admissibility screen of this
particular prescription, or a correction of that interpretation. It
cannot by itself demonstrate an essential IUT flaw.

Continue with one mathematical specialization if the same geometric
object, actual native base and source quantifiers can all be matched.
Require comparison with index one over the correct base. A failed
identification stops that application; incomplete reasoning remains
unresolved. Do not replace G_star by its normal closure. No native
field equality or new exclusion is proved in this literature turn.

## Primary clauses and version qualifications

Both author URLs returned continuous text on 2026-10-19, with title
dates and page counts as recorded above. Citations use printed pages.
IUT I is now read at the author endpoint rather than solely through
the reproduction used in step308. Byte identity with that reproduction
or earlier downloads was not checked. No journal-version or screenshot
verification is claimed.

[IUT I, Definition 3.1(a)–(c)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf#page=61):
F contains sqrt(-1). The once-punctured curve defines F_mod; F/F_mod
must be Galois of degree prime to ell, and full 6-torsion is F-rational.
Clause (c) separately defines K/F using ell-torsion. These clauses impose
no minimal torsion-field-generation equality.

[IUT IV, Proposition 1.8(ii),(iii),(iv),(vi), pp.18–21](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=18):
perfectness is assumed; (ii) identifies the j-field and descent;
(iii) makes two-torsion descent-independent for pointed automorphisms
±1. Part (iv) needs rational full prime-level torsion on both models.
Part (vi) needs characteristic different from two, G_E=G_k and trivial
two-torsion action; its proof permits a twist to Legendre form.

[Theorem 1.10, p.22](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=22)
starts with initial theta-data, defines F_tpd using full two-torsion
of any F_mod-model, and additionally assumes
F=F_tpd(sqrt(-1),E_L[15]) for a Legendre model E_L/F_tpd.
Its F_mod(sqrt(-1),E_Fmod[30]) notation is defined by this prescription.
The separate intermediate-field Galois condition is over F_mod.

[Corollary 2.2, pp.41–44](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=41)
uses the literal monic Legendre equation. Part (ii) repeats the
prescription under compact-boundedness, j-boundedness at 2, degree and
finite-exception conditions. Its proof enlarges the exceptional set.
Those extra hypotheses are unverified here.

Thus the saved target's “Definition 3.1's exact field-generation” means
this two-source comparison; do not attribute IV's extra equality to I.
Satisfying a displayed equality does not establish the entire antecedent
of IV's theorem. Testing Corollary 2.2's conclusion is a different target
requiring separate coverage and hypothesis checks; this scope does not
approve such a test.

## Reused methods and changed-member obligations

Reuse the inspected assessment
`drafts/literature/2026-10-18-auxiliary-legendre-native-two-torsion-field.md`
and `drafts/2026-10-18-auxiliary-two-torsion-field-source-notes.md`:

- [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  I Proposition 4.18/Remark 4.19 p.38 and Theorem 6.3 p.42: unique
  extension between nonsingular projective geometrically irreducible
  completions over a perfect field. Check the omitted singleton in the
  future punctured/pointed comparison.
- [Sutherland, Lecture 21, 6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
  section 21.2 p.2: characteristic-zero pointed automorphisms for
  nonexceptional j. Check this member's invariant, not the old witness's.
- [Antieau–Meier, arXiv:1608.00851v3, 5 May 2020](https://arxiv.org/pdf/1608.00851v3),
  Definition 4.1, Proposition 4.5 and Corollary 4.6/proofs pp.13–15:
  ordered full two-torsion and its coarse parameter, retaining the
  nonequivariance warning for the Legendre section. L087 already gives
  its actual embedded coefficient/root-field equality; no new stabilizer
  calculation is necessary.

These are reused assessed inputs, not newly retrieved proofs or new
mathematics. L079's application is only a method lead. The later proof
must start with audited L087's one E_star/Q and actual pointed geometric
comparison with E_L_star. It must justify the punctured/pointed moduli
convention, apply the j-field description and verify nonexceptional
pointed automorphisms before computing native two-torsion using that
rational descent. Then use L087's embedded coefficient/root-field equality
and literal generators to compare the IV prescription. Finally compare
its audited normal-closure index four with threshold one over the native
base. Testing normality merely over the tripodal field is insufficient.

These are separate application obligations, not new-member conclusions
of this review. Import the general results without reproof. No need for
effective coefficients, new occurrence, radical calculations or scripts
was found. Full matching and supporting Mathlib coverage for this native
comparison is not checked; unknown availability is not absence.

## Discovery, overlap and preserved failures

New queries were `Mochizuki "Legendre" "Galois" "Ftpd"` and
`"inter-universal" "Legendre" "normal" field`. Results included
IUT sources and author-hosted exposition leads
`https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2018Apr16.pdf`
and `https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2018May28.pdf`.
The latter were not opened: their snippets supply no theorem evidence.
Mirrors and third-party formalization claims are not imports or Mathlib
evidence. Reuse step308's exact moduli/ordered-level searches, whose
general hypotheses have not changed. Failed searches establish no novelty.

Local checks used foundations/05 step272, its global-model source
comparison, L079's native-method proof, L087's hypotheses/conclusion and
actual j check, and L086's same-member rational-model statement. They
justify reuse of the general coverage while leaving the new native
application separate. No duplicate new-member native verdict was found
in these specific records. The canonical L087 audit remains the field,
completion and index input, not a native identification.

ATTEMPTS/033's classification/repeated-approval stop and ATTEMPTS/034's
cyclic-Frobenius nonseparation remain intact. This target uses audited
full stabilizers and native definitions, not either stopped mechanism.
Old field normality, independent initial data, native input/action,
all-image factorization, pilot transport, essentiality and original
finite B>=A remain open. No lemmas, mathematical scripts, DAG or PROOF
were changed.
