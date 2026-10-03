# Strict first-return descent on residue 20: source obstruction

TARGET: Test whether the first positive-time shortcut hit of {1,2} or residue 20 modulo 27 from every positive n congruent to 20 modulo 27 is strictly smaller than n, retaining the positive affine offsets.
CHECKED: 2026-10-03
DECISION: IMPORT
SEARCH_EVIDENCE: The 2026-10-03 exact-return and sufficiency screen located the previously unread obstruction linked from the rank audit; queries and inspected sections are recorded below.
SOURCE_EVIDENCE: Read Sodelin's AB_ternary_normalized_core_residue_obstruction.md, sections 5–6, raw lines 158–239, https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/AB_ternary_normalized_core_residue_obstruction.md; reread Monks et al., arXiv:1204.3904v2, section 6 definitions and Theorem 6.4, pp. 16–17 and 22–23, https://arxiv.org/pdf/1204.3904v2; reused the prior complete hitting assessment.
COMPARISON: The inspected return note directly contradicts the saved strict-decrease assertion; the published sufficiency theorem and L013 concern visitation and do not supply that size comparison.
GAP: This particular bridge has a sourced obstruction; a terminating mechanism for the remaining residue-20 starts is still missing.
REASON: Import the exact negative example by citation, without deriving a return formula or rerunning it; change the route to the narrower covered predecessor reduction, whose ready assessment is saved separately.
SCOPE: Positive shortcut integers, first positive-time hits including the base set {1,2}, and the cited return obstruction; no universal convergence or general return-rank impossibility is imported.

## Hypotheses

Use the positive-integer shortcut map in foundations/01-target-and-scope.md.
For n=20 modulo 27 define the first subsequent hit by

    rho(n) = min{k>=1 : T^k(n) is in {1,2} or is 20 modulo 27}.

The positive-time requirement excludes the starting hit. L013's
all-start bound, applied after the first step, makes this definition
finite. The proposed assertion is T^rho(n)(n)<n for every such n.
It is a proposed sufficient bridge, not an established input.

## Conclusion

The source review rejects strict decrease at every first return. This
is NEGATIVE evidence changing the route, classified KNOWN_IMPORTED;
it is neither a new discovery nor a Collatz disproof. The starting target
above is preserved exactly. No new return calculation was performed.

## Proof

This is a citation assessment, not a new mathematical proof. Reuse
[the effective-hitting assessment](2026-10-03-mod27-effective-hitting.md)
for its already screened stopping mechanism. That source coverage remains
adequate; reviewing the different size-comparison assertion was necessary.

### Inspected return statement and applicability

Sodelin, *Ternary predecessor normalization removes F026, but a stronger
core obstruction survives*, node `AB-CORE-RESIDUE-OBSTRUCTION-001`,
[section 6, raw lines 204–239](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/routes/AB_ternary_normalized_core_residue_obstruction.md#6-stronger-smaller-targets-peel-the-new-shadows-too),
gives

    425 -> 638 -> 319 -> 479,

with residues 20,17,22,20 modulo 27 and 479 the first return. The
listed positive states avoid {1,2}; the cited example therefore matches
the saved stopping set as well. Section 5 also gives an unbounded
growing first-return family. No independent replay or new specialization
is claimed here.

Section 6 supplies c(y)=(8y-7)/9 for y=236 modulo 243, with
0<c(y)<y, c(y)=20 modulo 27 and T^3(c(y))=y. It states that repeated
c reductions reach v_3(y+7) in {3,4}. Its c(479)=425 example warns
that return followed by normalization can loop. These are source
claims, not newly derived identities.

This is an informal public mathematical note, not a locally verified
general certificate. Its concrete displayed example suffices for this
screening decision; the next mathematical application must state and
check its exact integer hypotheses. The [ready predecessor assessment](2026-10-03-residue20-predecessor-reduction.md)
identifies that bounded applicability work. No broader polynomial-rank
theorem from sections 3–4 is needed or imported.

Provenance: read the live `main` Markdown body on 2026-10-03, including
the map convention, sections 5–6, and section 9's logical qualifications.
Its declared reviewed input is
`b6eee8594714adc3b51d5005dd0b4ed8a76412e8`; this is not a verified
revision of the note itself. No immutable snapshot or external priority
review is claimed. The companion source checker was not executed.

### Published comparison and reused machinery

Monks, Monks, Monks and Monks, *Strongly sufficient sets and the
distribution of arithmetic sequences in the 3x+1 graph*,
[arXiv:1204.3904v2, section 6 definitions and Theorem 6.4](https://arxiv.org/pdf/1204.3904v2#page=16),
uses the same shortcut map. The theorem is forward and cycle sufficiency,
not strict descent of the induced return map. Reread its statement and
definitions; reuse the prior assessment's complete proof comparison and
its residue-26 qualification. The v2 identifier is dated 2012-04-20,
while the retrieved title page reads November 27, 2024, as already recorded.

Rozier (2019), Lemma 1 with proof, pp. 2–3,
[finite-parity arithmetic](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
is already adequately read in the [September 26 assessment](2026-09-26-current-target.md).
It supports checking exact finite words but asserts no universal return
decrease. No general affine-word identity needs reproof.

### Search record and limits

Queries executed on 2026-10-03:

- `Collatz "20" "27" "first return"`
- `Collatz "residue 20" "return" obstruction`
- `Collatz strongly sufficient set stopping time first return descent 20 modulo 27`
- `"Collatz" "residue20" "first" "return"`
- `"Collatz" "20 mod 27" "descent"`
- `"Collatz" "first-return" "20" obstruction`
- `Collatz "20" "27" "least" "v3" "4"`
- `Collatz "236" "243" "predecessor"`

Followed the rank audit's direct obstruction reference and read the
Markdown text, rather than relying on search snippets. Also inspected
the statement and boundary paragraphs of the [refined ancestor note](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md).
Its complete selector proof was not read and is not an input. The
[complementary ancestor note](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md),
its finite-spell follow-ups, and other claimed stronger results remain
discovery leads; no theorem is assumed from their snippets or repository
summaries. None is essential to the concrete obstruction or the selected
predecessor application. There is no persistent source blocker to retry.

### Relevance, stopping test and continuation

The main gap is still universal eventual descent. L013's achieved
ceil(24 log(n)+14) arrival bound has no target-visit size comparison;
the requested threshold was a strict endpoint inequality at every
first return. The inspected overlap fails that threshold and stops
this bridge. Eventual decrease after several returns, or convergence
transferred from a different smaller start, remains possible.

L002/L003 and Attempts 002/003 already obstruct simpler forward block
decrease. They do not constitute this exact first-hit citation. The
paired three-block theorem and depth-11 screen address another gap;
their exhausted batch remains parked. No old obstruction is relabeled
as new evidence.

The next intermediate target applies the covered predecessor rule to a
least nonconvergent residue-20 start. Its downstream use is to narrow
the arithmetic domain for a later termination argument, without equating
normalization with forward descent. Continue that application only with
positive integral predecessors, the exact shortcut guards, membership
in the selected set, and comparison with the original root. An invalid
guard would stop the proposed application and require correction. Even
success would leave an infinite residual class and its dynamics open.

Literature does not spend the mathematical exploration budget. No lemma,
mathematical script, new bound, or complete candidate was produced.

## Mathlib

Full strict first-return descent statement: **not checked**. Supporting
return-map, affine-word and congruence results: **not checked**. No
absence or matching library theorem is asserted.
