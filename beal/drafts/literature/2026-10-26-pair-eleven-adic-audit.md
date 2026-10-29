# Separate critical audit of L141 — continuation gate

TARGET: Critically audit L141's complete 11-adic Kummer image, fixed-witness certificate and combined rank bound rank Jac(B)(Q)<=7+c<=9.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-instance queries, stronger local-generation comparison and duplicate/failure evidence in 2026-10-26-pair-eleven-adic-filter.md; compared full L141 and histories 504–505 with the ready L139/L140 audit assessments. No changed model or new discovery query was needed for this critical audit.
SOURCE_EVIDENCE: Refreshed Stoll (2001), DOI 10.4064/aa98-3-4, Section 4 pp.249–251 including all of Lemmas 4.1,4.3,4.4 and their displayed proofs; Clark 161-page author PDF, Proposition 2.9/proof and Corollary 2.10 p.65, Proposition 2.20/proof p.72, Exercise 2.11 and Theorem 2.24/proof p.73. Reused inspected infinity/generation and supported/real coverage from the named assessments below.
COMPARISON: Primary theory covers the unchanged local tools and naturality; it does not certify L141's field transport, branch residues, full saved arithmetic or combined rank specialization. Complete local generation is stronger than the branch-first method, but unnecessary if its dimension gate passes. Replay alone does not settle that gate mathematically.
GAP: Source coverage is ready for exactly the saved critical audit; every instance assertion and certificate remains subject to that audit. No improved bound or critical acceptance is established by this review.
REASON: Audit-specific hypothesis comparison closes REVIEW_REQUIRED without enlarging the target or repeating the prior arithmetic search.
LITERATURE_REASON: The newly saved audit entered this invocation as REVIEW_REQUIRED; its exact local-field, branch and naturality obligations required separate approval. Adequate prior discovery and source coverage are reused.
SCOPE: Exactly TARGET using L137–L141 and their saved complete relevant evidence; no new witness, local prime, point, unit, relation-box or backend search.

The next invocation may perform the mathematical audit as REPRODUCTION
under SPECIALIZE. This approval is source coverage, not a correctness verdict.

Essential future audit inputs: L137's prime/support, L138's actual G,H and
alpha/eta transport, audited L139's V and two-torsion, audited L140's W
and 39 source records, and L141's full proof and exact certificates.
Check all complete load-bearing evidence rather than selected previews.
No cross-notebook input is required.

Audit questions include the full local factorization, normalized residue
rho=10, exact branch vector (1,0,1,0), whether it reaches the required
dimension one, whether rational-2 really belongs to V_R and lies outside
the complete image, and whether dim V_R=9+c loses exactly one additional
dimension. The full rank consequence is 7+c<=9, not the sufficient bound
one. No full Beal candidate is present. Further filtering, points and all
lifting/recovery/signature gaps remain unresolved.

## Primary coverage and qualifications

[Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*,
Acta Arith. 98 (2001), 245–277](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
publisher PDF accessed 2026-10-26: Section 4 assumes a monic integral
squarefree odd model. Lemma 4.1 provides natural injectivity and
Proposition 4.2 local compatibility. Lemma 4.3(2) gives the signed
factor-divisor formula; (3) gives two-torsion dimension. Lemma 4.4(1)–(2)
gives image and norm-kernel dimensions at every odd prime, without a
good-reduction restriction. Its proof cites Schaefer/Milne for (1) and
uses square-class dimensions and odd-degree norm surjectivity for (2).
These are imported statements; the cited underlying proofs were not
independently retrieved here. Reuse Section 6's infinity convention and
complete-generation comparison already read in the fixed-filter assessment.
Do not replace Lemma 4.4 with Proposition 4.6's narrower discriminant case.

[Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
author-hosted 161-page version accessed 2026-10-26, revision date
unidentified: Proposition 2.9 and proof give the Eisenstein DVR, root
uniformizer and residue field; Corollary 2.10 explicitly identifies the
integral closure (its proof is assigned as Exercise 2.4). Proposition
2.20 splits valuation from units. Theorem 2.24 and its proof supply the
Henselian local-square input; Exercise 2.11 states the odd-residue
square-class dimension but is not a separately proved theorem. Use the
standard named Hensel square criterion with residue characteristic
different from two. The audit must bind completeness/Henselianity and
normalization to the actual finite extension, rather than treating a
repeated residue factor as field certification.

Reuse `2026-10-26-pair-supported-norm-dimension-audit.md` for the ordinary
supported Kummer framework and `2026-10-26-pair-real-kummer-audit.md`
for the real image and coordinate conventions. These previously inspected
sources were not all fetched again. The precise field and actual model
remain unchanged. No theorem outside the assessed scope is being proposed.

## Known overlap, failures and bounded audit

The fixed-filter assessment already checked exact coefficients and standard
terminology against general local algorithms; no novelty conclusion follows.
Its ATTEMPTS/045,050,052,059–061 comparison remains adequate. Histories
504–505 distinguish source approval from arithmetic specialization. This
audit neither reopens those stopped searches nor creates a new mechanism.
No cross-notebook input is used. Preserve unfinished L108.

The main gap remains exclusion of residual primitive Beal solutions.
The intermediate target is reliability of the claimed extra local loss,
useful as a baseline for later descent/rank and point control. Acceptance
requires every load-bearing hypothesis and complete relevant record to
pass; otherwise preserve the first precise discrepancy and correct or
reject the affected claim. Even acceptance leaves bound nine versus the
sufficient bound one, with independent recovery and signature gaps.

The next audit must:

1. Bind L137's actual prime and L138's model/algebra transport. Check
   the full shifted coefficients, Eisenstein test, integer ring, full
   local factorization and normalized residue map before dimension use.
2. Check the signed branch formula in both factors, infinity convention,
   exact valuations and unit residues. Prove dimension matching rather
   than assuming rational two-torsion survives locally modulo twice.
3. Inspect both implementations and complete load-bearing certificate
   values, source hashes, all 39 witnesses and all 37 kernel products.
   Check exact division/integrality, norm signs, residue normalization,
   elimination completeness, multiplicativity, rejection/cap handling
   and rational-2's support and real compatibility. No preview suffices.
4. Check naturality into the full norm kernel, the codomain dimension,
   exact additional quotient rank, rank-nullity on V_R and subtraction
   of actual rational two-torsion. Retain c and distinguish coefficient
   independence from independence of global classes or Selmer equality.

No certificates were verified or mathematical programs run in this source
review. Full matching Mathlib coverage remains not checked, not absent.
No new lemma, reproof, critical acceptance or mathematical advance beyond
the inspected literature is claimed. Essential coverage is now sufficient;
the required audit precedes selection of any new creative mechanism.
