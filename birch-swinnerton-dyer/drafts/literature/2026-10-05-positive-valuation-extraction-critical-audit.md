# Source approval for the separate extraction audit

TARGET: Critically audit L024's classical prime-deletion membership and p^(3h) span-index bound under L023's hypotheses for m > 2h, checking dual structures, tensor-normalized diagonal localizations and the nonfree quotient sequence.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the extraction assessment's terminology searches and local overlap/failure comparison; read canonical L024, L023 and ATTEMPTS/021 and retrieved the exact primary cases below; no expanded discovery search or critical proof audit.
SOURCE_EVIDENCE: Sakamoto 2022 DOI 10.4171/DM/X21, setup p. 1896, Theorem 2.1/Definitions 2.3-2.4/Lemma 2.6 pp. 1897-1898, Section 2.3/Definition 2.18/scalar definition pp. 1902-1904 and Corollary 4.10's full proof p. 1920; Mazur--Rubin 2004 Section 1.2, Definition 1.2.2 and Lemmas 1.2.3-1.2.4 with proofs, printed pp. 10-11.
COMPARISON: Canonical L024 retains the assessed representation, depth, prime set and scalar family; its three proof blocks use the covered duality and class relations and a finite-module quotient argument. The residual basis theorem is not a matching positive-h index theorem.
GAP: Independently audit L024's applicability, tensor normalization and quotient exactness; ready source coverage is not a verdict on the proof. Rational membership, depth compatibility and complex comparison remain missing.
REASON: Separate source-scope approval is complete for the unchanged exact audit; the next turn is a mathematical proof audit, with no source construction to reprove or additional theorem to assume.
LITERATURE_REASON: The newly written canonical L024 and its saved audit continuation had not received separate source-scope comparison; the supervisor requires this literature-only approval, reusing ready extraction coverage.
SCOPE: Exact L023 arithmetic hypotheses and selected pair at depth m>2h; F=S/S_div and h=length_Z_p F; fixed actual Sakamoto family and all tensor generators. No rational membership, finite Sha, coefficient compatibility of selected pairs or comparison with complex order is covered.
COVERED_TARGET: Critically audit L024's classical prime-deletion membership and p^(3h) span-index bound under L023's hypotheses for m > 2h, checking dual structures, tensor-normalized diagonal localizations and the nonfree quotient sequence.

The ready source evidence is reusable from
[the extraction assessment](2026-10-05-positive-valuation-prime-deletion-extraction.md).
Its checked primary sources cover the completed extraction, whose
argument is now in canonical L024. This separate literature turn approves
coverage for its critical audit; it does not perform the mathematical
audit or certify the extraction. No changed hypothesis is proposed.

The audit should independently check: strict dual equals relaxed and
classical self-duality in the Poitou-Tate sequence; why surjectivity
makes relaxed equal classical with a nonzero strict kernel; why each
actual tensor-valued component lies in that relaxed group; the full
finite/transverse intersection at its other prime; Definition 2.18's
last relation with d=N/ell_i and an extra prime q; the identification of
both tensor sides with L023's delta_m(N); and exactness of the quotient
sequence for a possibly nonfree Selmer module. Check h=0 and positive h
without dividing a scalar by p^h or assuming injectivity on the span.

Retain the extraction only if those checks confirm membership and
length(M/C)<=3h under exactly the retained hypotheses. Correct a real
error or record a failed claim if one is found. The audit would still
leave rational membership, compatible depths/primes, granted corank
two and complex-order comparison unresolved. Mathlib coverage remains
not checked. No new mathematical result is asserted by this assessment.

## Separate source-scope comparison — 2026-10-06

Primary text: Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Documenta Mathematica 27 (2022), 1891-1922, received 2022-05-13,
revised 2022-07-20. Retrieved the full statements and relevant proof
cases from the publisher text, not search snippets:

- [Setup and Theorem 2.1, pp. 1896-1897](https://ems.press/content/serial-article-files/29299?nt=1#page=6): p>3, assumptions (a)-(c), arbitrary m>=1 and n>=0; the theorem requires nested local structures and includes both dual groups.
- [Definitions 2.3-2.4 and Lemma 2.6, p. 1898](https://ems.press/content/serial-article-files/29299?nt=1#page=8): strict/relaxed dual exchange, classical self-duality and the away-from-p unramified condition.
- [Sections 2.3-2.4, pp. 1902-1904](https://ems.press/content/serial-article-files/29299?nt=1#page=12): eligible local splitting, tensor-valued comparison, every rank-zero relation and the scalar definition.
- [Corollary 4.10 and full proof, p. 1920](https://ems.press/content/serial-article-files/29299?nt=1#page=30): residual minimality is required for the published basis conclusion; its proof is the assessed comparison mechanism.

Also retrieved Barry Mazur and Karl Rubin, *Kolyvagin Systems*,
Memoirs AMS 168 (799) (2004),
[Section 1.2, printed pp. 10-11](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=16).
Read Definition 1.2.2 and Lemmas 1.2.3-1.2.4, including complete proofs.
The section requires residue characteristic different from p and
unramified coefficients. Lemma 1.2.3 requires artinian R, residue-unit
group order annihilating R, T finite free and free rank-one Frobenius
coinvariants; it makes the finite-singular map an isomorphism.
Lemma 1.2.4 uses the maximal totally tamely ramified abelian extension.
The audit must check the passage to Sakamoto's p-primary G_ell factor,
not drop it. L023's selected primes and coefficient setup are the
already assessed applicability data; no new local result is derived.

The source reads used complete browser text. Requested screenshots
returned references without visible images and supplied no evidence.
No essential source is blocked; no PDF or calculation certificate was
created. The 2021 regulator construction remains the inspected comparison
in the extraction assessment, not an additional input to L024's audit.

Read all of L024 and L023, including L023's earlier audit qualifications.
L024 does not change L023's representation, prime eligibility, scalar
family or granted localization/kernel data. Compare its equations (4),
(5) and (7) independently in the next research turn. In particular,
check that the dual arrow is restriction along the actual subgroup
inclusion, that the same R tensor G_N generator scalarizes both
diagonal relations, and that the quotient sequence retains K/(K intersect C).
These are audit questions, not newly proved consequences here.

Reuse the extraction assessment's comparison with L015-L017; their
crossed-error package lacks the granted full-depth surjection. The
finite-defect stop in ATTEMPTS/021 remains relevant and preserved:
the audit retains F and tests no implication that primitivity removes it.
No exact positive-h index theorem was identified in the inspected sources;
no novelty is inferred. The unchanged source scope makes this approval
STALLED as mathematical progress, with a concrete ready research target.
Only the necessary applicability and finite-module argument should be
audited; do not reprove the source theorems. Matching Mathlib coverage
remains not checked.
