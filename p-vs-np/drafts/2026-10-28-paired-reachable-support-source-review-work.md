# Step 548 — paired reachable-space support source comparison

Literature-only, 2026-10-28. Completed source comparison; the initial
scope/continuation checkpoint was saved before external source reads.
The exact target is preserved in
`literature/2026-10-28-paired-reachable-generator-support.md`.
No new mathematical result, lemma, calculation or script is authorized
in this turn. The completed assessment is EXPLORE, not a theorem import.

## Scope and saved continuation

The main gap remains ordinary uniform worst-case P versus NP. The
intermediate asks for O(N) total expanded-support generators of the
paired reachable K_N for L122's original dyadic endpoints. Its plausible
use is the known common-source simulation construction; sparse induced
shift, acyclic singleton realization, both boundaries and all reception
and resource requirements remain independent. The bounded first test is
exact N=4 dimension and complete weight-at-most-four span. Finite span
does not prove a uniform bound; finite deficit alone does not disprove it.

The supplied PROOF/DAG preceded detailed reads. Notebook-scoped status
shows substantial unfinished work, preserved. Read L122 hypotheses/§2,
L125 §2, L126 hypotheses/§§1,4,7, Attempts 056–059, and the step-541/545
primary source notes. The full-E_N obstruction needs full spanning and
does not transfer to K_N without a new argument. No K_N dimension,
projection surjectivity or equality with E_N is asserted or computed.
The previously audited Clay target in foundations/01-model-and-target.md
is unchanged; no new route to unrestricted complexity is claimed.

Reuse the step-541 primary reads of Ésik–Maletti, Bhaduri,
Gottlieb–Neylon, Coleman–Pothen and Boyar–Find and step-545 support
comparison. The remaining review concerns sparse generators for the
boundary-generated binary Krylov space, rather than all of E_N.
No cross-notebook input is needed. Full matching Mathlib coverage
remains unchecked.

## Bounded search log

Actual queries submitted, in successive small batches:

- `"Krylov" "sparse basis" "finite field"`
- `"weighted automata" "reachable" "sparse" basis simulation`
- `"binary linear code" "sparsest" "generator matrix"`
- `"paired" "reachable" "Simulation vs. Equivalence"`
- `"Krylov subspace" "sparsification"`
- `"binary" "sparsest basis" code generator`
- `"reachable space" "weighted automata" basis sparse`
- `"sparse generator" "binary" "basis" code fixed`
- `"binary codes" "minimum weight basis"`
- `"reachable" "support" "Simulation vs. Equivalence"`
- `Dodunekov Manev "An improvement of the Griesmer" pdf`
- `"binary code" "basis" "weight" "Griesmer" Dodunekov Manev`
- `"sparse basis" "Krylov" binary`
- `"sparse generator matrix" "Pascal" code`
- `"A Comment on the Weight Structure" "Generator" Dodunekov`
- `"Krylov" "low-density generator"`
- `"Pascal" "low-density" "code"`
- `"Explicit Low-Weight Bases for BCH Codes" pdf Grigorescu Kaufman`
- `"On generator matrices of codes" "Simonis" pdf`

No adequate exact-family theorem was established. Numerical Krylov
preconditioning, spectral approximation and unrelated quantum/Krylov
results were not used for exact binary support. Search failure supplies
no novelty or nonexistence claim.

## Inspected primary passages and comparison

**Reused common-source input.** Ésik–Maletti, *Simulation vs. Equivalence*,
2010 author manuscript, Definition 3.1/Theorem 4.2, pp.2–3,
[primary PDF](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
The complete paired reachable proof was already read in step 541 and
is reused without another extraction. The theorem assumes a Noetherian
semiring; F₂ qualifies (subsemimodules here are subspaces of finite
dimensional vector spaces). It supplies finite common-source generators
and transition/initial coordinates, with final equality from equivalence.
It does not charge expanded entries or ensure sparse acyclic realization.
No reproof or stronger quantitative specialization is supplied here.

**Mazumdar–Chandar–Wornell**, *Update-Efficiency and Local Repairability
Limits for Capacity Approaching Codes*, IEEE JSAC 32(5), May 2014,
976–988, [author PDF](https://sia.mit.edu/wp-content/uploads/2015/04/2014-mazumdar-chandar-wornell-jsac.pdf).
Read Proposition 1's linear-labeling formulation, §III Theorem 3,
Corollary 4, Theorem 5 and surrounding discussion, pp.978–980, and
references [14]/[18]/[20], p.987. The objective is maximum generator-row
weight, whereas our target charges total expanded support. Theorem 5
changes the code while preserving its parameters; it does not promise
a new basis for the same prescribed coordinate subspace. The Hamming
example additionally uses classification up to coordinate permutation.
No such identification for K_N is supplied. This source's generic bound
leads to the next primary paper; its channel-capacity results are unused.

**S. M. Dodunekov**, *A Comment on the Weight Structure of Generator
Matrices of Linear Codes*, Probl. Peredachi Inf. 26(2) (1990), 101–104;
English translation, Problems Inform. Transmission 26(2), 173–176.
Read the sole theorem in §1, p.101, the residual-code lemma in §2,
and the complete §3 proof, pp.102–103, in the
[primary Russian scan](https://www.mathnet.ru/php/getFT.phtml?jrnid=ppi&option_lang=eng&paperid=611&what=fullt);
[bibliographic/English abstract page](https://www.mathnet.ru/eng/ppi611).
For a q-ary linear [n,m,d] code over a finite field, with m,d>=1, put
`g_q(m,d)=sum_(j=0)^(m-1) ceil(d/q^j)` and `t=n-g_q(m,d)`.
The theorem gives a generator matrix for that code with every row of
weight at most d+t. Its proof treats t=0 and t>0 separately, using
residual codes, induction and subtraction of multiples of a minimum
weight row. Coordinate equivalences used in the proof are permutations
and nonzero scalings. This is a genuine fixed-code upper bound, but
K_N's dimension, distance and Griesmer defect have not been established
here. No linear total-support conclusion is imported or ruled out.

**Grigorescu–Kaufman**, *Explicit Low-Weight Bases for BCH Codes*,
IEEE Trans. Inform. Theory 58(1) (2012), 78–81; retrieved seven-page
author manuscript with 2011 copyright and no revision date established,
[primary PDF](https://cs.uwaterloo.ca/~elena-g/papers/bch5.pdf).
Read Theorem 1, manuscript p.2; Definition 3, Proposition 4 and the
trace-polynomial BCH definition, p.3; Definition 5, Lemma 6/Claim 7
and their proofs, pp.4–5; Corollary 8 and the full main proof, pp.5–6.
For sufficiently large extension degree n, Theorem 1 supplies a
weight-at-most-six affine-orbit generator of eBCH(2,n). The proof uses the
specified trace degree set, moment vanishing, a nonzero product
polynomial and shadow closure. K_N has not been identified with that
code by a support-preserving coordinate map, nor has the required
affine-permutation invariance been shown. It is not an arbitrary binary
subspace theorem. No BCH identification or extension is derived here.

The earlier rational matrix-sparsification, real null-basis and
cancellation-free Sierpinski comparisons remain as recorded in step 541.
Step 545's support-product field restrictions remain unchanged.
L126's all-parameter determinant argument cannot simply be applied
to a space not shown to span those parameters.

## Access qualifications, unread leads and decision

Several web screenshots timed out or redirected, the 1985 DOI open
failed, the direct MathNet download returned 403, and the direct BCH
download had a DNS failure. Relevant complete theorem/proof text was
nevertheless available through web extraction; the 2014 PDF was also
downloaded and text-extracted successfully. OCR damages some symbols
in the Russian proof; its exact theorem is corroborated by the English
abstract and the binary statement in the 2014 paper. No ambiguous OCR
formula is a new mathematical premise. There is no essential access
blocker for this bounded comparison.

Simonis (1992), the original 1985 Dodunekov–Manev paper, later
affine-orbit code work, and the 2012 succinct-code paper are unread
primary leads, not imported theorems or asserted obstructions. No claim
of optimal current coding bounds depends on them. They would need
their own hypothesis/proof reads before use.

Decision: EXPLORE for the exact unchanged target. This is fresh bounded
source comparison, not a mathematical advance or proof of originality.
The ready gate permits the later original-coordinate N=4 discriminant
and a support argument within K_N; it does not certify either outcome.
Continue only on a concrete uniform mechanism or defensible necessary
bound. A proven superlinear generator bound abandons this exact O(N)
proposal; a finite deficit merely narrows the search. Sparse induced
shift, graph realization, general operands/chains, receptions, full costs
and uniform complexity remain unresolved. No lemma/script, PROOF or
DAG change is required because the mathematical argument is unchanged.
