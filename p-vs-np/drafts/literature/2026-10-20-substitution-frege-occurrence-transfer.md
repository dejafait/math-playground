# Substitution-Frege occurrence-transfer source comparison

TARGET: Assess whether L098's exact occurrence-product transfer extends to explicitly written substitution-Frege proofs of ¬F with polynomial full size/time in Q=2+M+|F|+|π|, identifying an applicable theorem or the precise extra witness-reuse obligation.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 385 searched SF/EF equivalence, substitution/noncommutative IPS and Frege/ABP witnesses; inspected Krajíček–Pudlák §5–6 and Buss §8, and reused local ER/circuit and ordinary-Frege assessments. No inspected theorem supplies the exact fg/B affine-ABP output; no absence or novelty conclusion follows.
SOURCE_EVIDENCE: Krajíček–Pudlák (JSL 54, 1989), Theorem 5.3/Corollary 5.4 and §6 pp.1075–1077; Buss, July 3, 2002 manuscript, §1 pp.2–4 and §8 Theorem 15/Corollary 16/Lemma 17 with complete proof pp.22–24; LTW 40-page revision Theorem 3.1/Lemma 3.3 pp.13–14 including all extraction cases; Pudlák, The Lengths of Proofs, Theorem 8.1.10 pp.593–594 and its replay-cost warning.
COMPARISON: The proposed rule is standard assumption-free simultaneous substitution Frege, polynomially equivalent to EF. Even variable-only, possibly noninjective renaming Frege p-simulates SF. These propositional simulations do not produce the required affine-ABP witness. LTW/L097 cover axiom/MP extraction, not repeatedly relabeled earlier witnesses.
GAP: Justify the source-to-occurrence transformation for the new rule and bound differently substituted copies of reused witnesses by one polynomial in original Q, with exact zero-at-zero and fg endpoints and unchanged B. No global ledger or failure family is established here.
REASON: Essential source coverage now permits one bounded test of literal context copying. Renaming is a source-justified diagnostic, not an assumed weaker proof system or an imported full transfer.
SCOPE: Preserve L049/L087/L097/L098 input charging and occurrence conventions. The covered mathematical test concerns only literal context-copy extraction with assumption-free renaming inferences, including its noninjective placeholder interface; it approves no arbitrary new EF-to-ABP mechanism.
COVERED_TARGET: Test whether literal context-copy extraction on supplied assumption-free renaming-Frege proofs has a polynomial original-Q ledger, or exhibit an explicit proof family with superpolynomial necessary context copies in that implementation.

## Gap, relevance and precise convention

The main gap remains a deterministic polynomial-time SAT algorithm or an
argument excluding every such algorithm. This review preserves the saved
SF target. Its downstream use is to locate the first resource obligation
between the audited ordinary-Frege supplier and a stronger source system.
A copying test may leave occurrence normalization and short-proof
availability unresolved. The [Clay problem page](https://www.claymath.org/millennium/p-vs-np/),
reopened today, still lists the problem as unsolved; retain the precise
uniform conventions in foundations/01-model-and-target.md.

Use a sequence/DAG of fully written formula trees with earlier-line
references. Add Aσ from an earlier A to the fixed schemes, MP and specified
ground constants. A finite simultaneous substitution assigns written
formula trees to listed variables, fixes unlisted variables, and does not
recursively substitute inside its images. Charge all map entries, images,
resulting formulas, binary names and references in |π|. No nonlogical
assumptions or extension definitions are premises. The conclusion is the
exact written ¬F. Fix Q=2+M+|F|+|π| before outputs. An extension must retain
L087's occurrence alphabet/provenance, exact product fg and unchanged B,
and prove H(y,0)=0 and H(y,B(y))=fg formally with one fixed full-bit
size/time polynomial in Q. A bound in unfolded proof size is weaker.

## Inspected primary sources and applicability

**Krajíček–Pudlák.** Jan Krajíček and Pavel Pudlák, *Propositional proof
systems, the consistency of first order theories and the complexity of
computations*, JSL 54(3) (1989), 1063–1079,
[author-hosted published scan](https://msekce.karlin.mff.cuni.cz/~krajicek/scan10.pdf).
Read the conventions pp.1073–1074, Theorem 5.1 p.1074, Theorem 5.3 and
Corollary 5.4 p.1075, and every case of §6 pp.1076–1077. Corollary 5.4
gives polynomial simulation of SF by ER and EF. Section 6 defines fresh
variable vectors by extensions and proves renamed formulas using axiom,
MP and substitution cases, retaining the original final conclusion.
It produces a propositional proof, not an affine-ABP witness. Replacing
its extension definitions by trees is outside its bound. No reproof is
needed; the reverse simulation is corroborated below.

**Buss.** Samuel R. Buss, *Some Remarks on Lengths of Propositional Proofs*,
[author manuscript dated July 3, 2002](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/proplengths/paper.pdf).
Read §1 pp.2–4, including the simultaneous-substitution footnote, and §8
pp.22–24 in full. Theorem 15 polynomially simulates SF by renaming Frege;
Corollary 16 covers EF. Renaming may identify variables. Lemma 17 first
reduces to constant substitutions; the remaining proof uses a
not-all-equal guard, renamings and ground evaluations. The final paragraph
requires tautological conclusions/substitution lines and excludes
arbitrary nonlogical assumptions. Our source is assumption-free. The
manuscript charges formula symbols, not merely lines; maps/references
and binary names also need local charging. No numerical exponent or
witness construction is imported. This supports the diagnostic scope.

**Pudlák.** Pavel Pudlák, *The Lengths of Proofs*, in *Handbook of Proof
Theory* (1998), [author-hosted chapter](https://users.math.cas.cz/~pudlak/length.pdf),
Definitions 8.1.3–8.1.6 pp.591–592 and Theorem 8.1.10 with proof
pp.593–594. The theorem gives SF/EF polynomial equivalence. Its proof
eliminates EF definitions in reverse order for one direction and uses
fresh extension variables for the other. It explicitly warns that
repeatedly replaying substituted prefixes can grow exponentially.
That warning is not a lower bound for our ABP implementation. Import
the simulation and its qualification, without asserting polynomial
ordinary-Frege elimination.

**LTW and ready local coverage.** Fu Li, Iddo Tzameret and Zhengyu Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*, SIAM
J. Comput. 47(4) (2018), 1424–1462,
[40-page author revision](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf)
(revision date unestablished; accessed today). Reopened Theorem 3.1 and
Lemma 3.3 pp.13–14: assumptions, axiom and MP cases, and disjoint-tree
ancestry accounting; also Definitions 2.2–2.4 p.11. That proof contains
no substitution-inference case. Retain L097's corrected seeds, constant
cases and graph implementation, including its repair of the source's
suspect Boolean-only subcase. Reuse L049's formula-to-graph coverage and
this directory's `2026-10-04-er-to-formula-ips.md`,
`2026-10-04-shared-noncommutative-er-circuit-ips.md` and
`2026-10-10-er-to-clause-product-boolean-witness.md` assessments.
Their circuit conclusions do not supply the missing affine-ABP output.

Mathlib matching coverage for SF/EF/renaming simulations and this transfer
is **not checked**, not absent. No formal verification or new lemma is
claimed; precise imported inputs are recorded above by citation.

## Search evidence, duplicates and remaining obligations

Queries actually issued: `"substitution Frege" "extended Frege" p-equivalent`;
`"substitution Frege" noncommutative IPS`;
`Krajicek Pudlak 1989 extended Frege substitution Frege theorem pdf`;
`Dowd 1989 substitution Frege extended Frege proof simulation`;
`"substitution Frege" "branching programs" IPS`;
`"noncommutative" "IPS" "extended Frege" substitution`;
`"Frege" "substitution" "ABP" witness`.
Primary passages above, not snippets, support the comparison. Jeřábek's
nonclassical SF/EF PDF returned an access error and is an unused lead,
not essential after obtaining the classical primary sources. Dowd's
1985 manuscript was not inspected. The partially commutative formula
paper returned by search already has theorem-level coverage in the
reused 2026-10-04 reverse assessment; its different identity model does
not fill this free-algebra ABP/source-rule gap.

Read relevant L049 substitution/audit passages, L087 input/occurrence
conventions, L097 §4 and L098 §§2–4. L049 transforms a complete ordinary
proof once. L098 justifies name identification and complementation only
for axiom/MP proofs. Their extension to substitution inferences needs
new syntactic justification, especially under noninjective maps or
formula images. Separately, L097's MP graph reuses unchanged labels;
it supplies no bound for differently substituted copies. Even a
polynomial single-step transformation would not settle the global
original-Q ledger. These are obligations, not new negative theorems.

Attempts 018/030/031 were read and preserved. They stop approval
repetition, universal common-order faithful values, and universal
logarithmic oriented partitions, respectively; they do not prohibit
this proof-dependent diagnostic. Ready circuit/reduced-data results
are contrasts, not added premises. No other notebook was read.

## One bounded mathematical continuation

Use the COVERED_TARGET above. Test the literal implementation that keeps
L097's axiom/MP pieces, recursively copies/relabels earlier witnesses
at renaming inferences, and merges copies only when the proof-line
index and action on actually occurring block labels agree. Explicit
renamings may be noninjective; the disposition of Boolean/commutator
placeholders when names merge must be justified, not assumed as a rule.
Count only contexts reachable from the final output. Differences on
unused names alone and unused proof padding cannot show failure.
An obstruction family must have genuinely used final-inference ancestry,
small explicit source proofs and fully charged source/occurrence data.
Save the proposed implementation/invariant before extended reasoning.
No invariant, family, bound or new identity is proved in this review.

Continue literal copying only if formal identities and all distinct
necessary copies fit one fixed polynomial in original Q. Abandon it if
an explicit family forces superpolynomial distinct active contexts or
copied bits, or the formal placeholder interface fails. That stops only
this implementation, not alternative witnesses or the general transfer.
A positive test still leaves source-to-occurrence normalization and full
SF reception open; renaming results do not automatically apply over the
restricted occurrence alphabet. Short-proof availability, an M-only
bound, arbitrary ER data, universal W₂ and unrestricted SAT remain open.

New ready continuation coverage receives separate supervisor approval
next turn. This EXPLORATION / LITERATURE / NOVELTY_UNCHECKED comparison
supplies source coverage and narrows the reuse test, without resolving
the full transfer or proving an obstruction. It claims no result beyond
inspected sources. Mathematical exploration usage stays zero. No lemma,
mathematical script, DAG or argument overview changed.
