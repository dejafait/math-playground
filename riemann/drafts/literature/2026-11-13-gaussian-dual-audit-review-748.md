# Critical audit of Gaussian dual specialization: coverage approved749

TARGET: Audit C998y's whole-line dual normalization, compact-source pairing, 64-node ellipse bounds and specified-loop work stop, without evaluating or retuning the fixed Gram.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate comparison749 reuses746/747's signed-measure/RKHS/whole-line-dual searches,719's analytic Gauss comparison and713's parameter-integral coverage. Read C998y and the748 failure plus scoped C998s/C998u statements and audit726; no changed witness,algorithm or discovery search. Every proposed audit technique is covered; local formulas and the certificate remain unaudited.
SOURCE_EVIDENCE: Reopened primary statements749: Sriperumbudur--Fukumizu--Lanckriet,JMLR12(2011),Lemma7/full proof p2407 and Proposition4 energy identity p2402 https://jmlr.org/papers/volume12/sriperumbudur11a/sriperumbudur11a.pdf; Novak et al.,1709.02568v1,(1) p2,K1,1/continuous representatives p3 https://arxiv.org/pdf/1709.02568v1; Bauschke et al.,SIAM J.Optim.19(2008),Section2(1)-(2) p767,Proposition3.3(i)/citation proof p769 https://webpages.math.luc.edu/~rgoebel1/publications/journals/BauschkeGoebelLucetWang08SIOPT.pdf; Trefethen,SIAM Review50(2008),(2.2) p69,Theorem4.5/(4.14) p77,Gaussian proof pp79-80 https://people.maths.ox.ac.uk/~trefethen/CC.pdf; Lebl,v1.10(5November2026),Lemma3.4.1/proofs pp81-82,Theorem3.4.5 pp84-85 https://www.jirka.org/ca/ca.pdf. Reuse746/719/713 for previously inspected supporting proof cases; exact limits below.
COMPARISON: Signed-measure embedding,full-line Sobolev kernel,quadratic conjugacy and analytic Gauss/parameter-integral theorems cover the unchanged conceptual audit. They do not certify C998y's normalization,Gaussian matrices,350 ellipses,quadrature constants,loop count or any Gram sign. No new general result or numerical feasibility is claimed.
GAP: The mathematical audit must still verify amplitude/rate scaling,whole-line products,full-Dh cutoff,all event/ellipse evidence,exact-node rescaling and the specified nine-operation loop; preserve separate unpaid arithmetic and weighted-dual errors. No essential source blocker remains for that audit alone.
REASON: Separate literature approval749 changes this new audit target from REVIEW_REQUIRED to SPECIALIZE using adequate saved coverage and direct hypothesis checks. Only the exact unchanged conceptual audit is ready for the next research turn; no lemma,mathematical script or new derivation is authorized in this literature turn.
LITERATURE_REASON: Nomination748 explicitly required separate approval for the new C998y audit; compare its exact cutoff,normalization,analytic-panel and work-model obligations with existing746/747,719 and713 coverage rather than repeat discovery or the stopped calculation.
SCOPE: Fixed C998y under its unchanged witness and source contracts;33 whole-line Gaussians,256 rates,N=64,rho=2,claimed350 panels and the specified direct common-phase loop. Critical review and a specific correction if necessary only;no retuning,Gram evaluation,alternative algorithm or uniform-S3 theorem.
COVERED_TARGET: Audit C998y's whole-line dual normalization, compact-source pairing, 64-node ellipse bounds and specified-loop work stop, without evaluating or retuning the fixed Gram.

## Completed source comparison749 — 13 November2026

The source gate is ready; C998y's proof and certificate have NOT been
critically verified in this turn. No mathematical script was run and no
lemmas/ or scripts/ file was changed. This is local source readiness,
not progress beyond the cited theorems or a mathematical audit verdict.

Main gap: L030-L032/C032a actual-Xi positivity and C744z(4)'s uniform
signed S3 against BOTH defects. The intermediate target is verification
of one fixed Gaussian lower comparison and its implementation-specific
stop. A trustworthy comparison could support a later sufficient-positive
fixed complex-scalar Gram test involving the full h=P0Uf. It cannot
settle all-vector minimization,uniform S3,C744q/H2 or Xi/global transfer.

### Exact imported coverage and remaining application checks

- [Sriperumbudur--Fukumizu--Lanckriet, published JMLR PDF](https://jmlr.org/papers/volume12/sriperumbudur11a/sriperumbudur11a.pdf),
  Appendix B,Lemma7/full proof p2407: measurable bounded reproducing
  kernel and finite signed Borel measure; total-variation boundedness
  and Riesz representation give the integration representer.
  Proposition4's proof p2402 identifies its squared norm with the
  double kernel integral. Only that identity is needed, not the
  proposition's universality/strict-positivity equivalence. C998u's
  existing real finite signed measure, including outer atoms, fits the
  measure class. No density,positivity or probability hypothesis is
  imposed by the imported representation. Exact local normalization
  and preservation of the entire measure remain audit obligations.
- [Novak--Ullrich--Wozniakowski--Zhang,v1](https://arxiv.org/pdf/1709.02568v1),
  equation(1) p2 fixes the derivative-L2 inner product; p3 identifies
  continuous representatives for s>d/2 and gives K1,1=exp(-|x-t|)/2
  on the WHOLE real line. Reuse746's inspected Theorem1/finite-s proof.
  This covers the reference norm only. Dilation,amplitude,Gaussian
  trial membership and exterior norm must be checked, without imposing
  H1 on h. The standard named Gaussian integral is sufficient for the
  proposed elementary product computation; no new Gaussian integration
  theorem or bounded-interval norm is needed.
- [Bauschke--Goebel--Lucet--Wang,author PDF](https://webpages.math.luc.edu/~rgoebel1/publications/journals/BauschkeGoebelLucetWang08SIOPT.pdf),
  Section2(1)-(2) p767 and Proposition3.3(i) p769: real Hilbert space,
  q=norm-squared/2,q*=q. The proof cites Rockafellar--Wets,Example11.11;
  this citation proof was inspected, not independently reproved. It
  covers the variational method. The audit must check factors and the
  restricted LOWER direction. Ambient complex triple scalars do not
  license changing the real trial optimization or omitting cross entries.
- [Trefethen,author PDF](https://people.maths.ox.ac.uk/~trefethen/CC.pdf),
  (2.2) p69 uses n+1 nodes. Theorem4.5/(4.14) p77 assumes continuity
  on[-1,1] and analyticity bounded by M in the Bernstein ellipse,
  rho>1; its exact-rule bound is64M/[15(1-rho^-2)rho^(2n+2)].
  Read the Gaussian proof completion pp79-80: polynomial exactness,
  parity and the even Chebyshev tail/(5.6). Thus the source convention
  is exponent2N for N nodes. This source-level comparison does not
  verify any C998y ellipse,M,affine factor or summed error. Node,weight,
  value and arithmetic errors are outside that exact-rule theorem.
- [Lebl,author text,v1.10](https://www.jirka.org/ca/ca.pdf),
  Lemma3.4.1/proofs pp81-82 requires joint continuity on U times[0,1]
  and holomorphy in the complex parameter on open U. Proof A uses
  Fubini/Morera; Proof B justifies differentiation. Theorem3.4.5
  pp84-85 requires locally uniform convergence on an open domain and
  preserves holomorphy/derivatives. Reuse713's full proof inspection;
  reread the statements,parameter proofs and holomorphic-limit proof
  through its Cauchy-transform argument749. These cover the full
  kernel parameter integrals after local hypotheses are checked.
  The audit must exhibit an open neighborhood of every closed ellipse,
  including each one-sided analytic piece's extension. Real-valued
  restrictions do not permit conjugating the complex parameter.

For compact-source pairing,reuse746/747's assessed cutoff technique
and C998u Section4/audit726's full distributional derivative identity.
Its compact smooth tests and support statements were read here. A smooth
compact cutoff exists around the compact support by the standard smooth
bump-function theorem; applying that identity to the cutoff trial is
the pending local check. No new integration-by-parts theorem or deleted
endpoint premise is required. All classical-density terms,interior and
outer atoms,full K14 and both exact moments must survive the audit.

Exact event comparisons and the declared scalar-operation count are
finite certificate/syntax checks,not applications of a complexity
theorem. Their verification remains next turn: inspect the complete
relevant event/ratio evidence and the actual loop specification before
accepting the claimed count. This turn did not inspect that complete
JSON or replay it. The cited sources imply no universal lower bound,
finite-precision accuracy or useful Gaussian trial quality.

### Duplicates, failures and bounded decision

Reused746's recorded exact-statement/stronger-result searches and its
comparison with C998w's spectral duals; no novelty inferred. Reused719's
analytic versus BV method distinction and713's analytic-germ comparison.
Read ATTEMPTS/2026-11-13-gaussian-aggregated-loop-cost-stop-748.md and
C998y's complete claim inventory. Preserve745's direct-density stop,
C998u's full-tail loop stop,C998w's production stop and all unfinished
work. None is a global ban on other algorithms. Previously blocked
optional Feydy/Petras sources remain unused and nonessential here;
there is no new essential source blocker. No cross-notebook input.
Full matching Mathlib coverage is unchecked; no supporting Mathlib
theorem was used or newly inspected.

Continue with ONE unchanged conceptual audit,importing the known
theorems and checking their local applications rather than reproving
them. Correct a specific error if found; otherwise retain the formula
and park the specified implementation. Do not evaluate or retune the
Gram,reduce node order or nominate an alternative numerical loop as
part of that audit. Separate exact quadrature,finite arithmetic,
weighted-dual and omitted-prefix deficits. A nonpositive LOWER bound
does not prove an actual negative Gram. No affordable complete ledger
or signed margin is imported. No justified creative central mechanism
has emerged: uniform remote-plus-induced domination against both
defects remains missing. The essential audit precedes such discovery;
this standard-method check is not labeled creative.

## Original nomination748 — historical preapproval scope

The pending-source wording below records the state before this separate
approval; only that source status is superseded by comparison749.

Essential input IDs: C744v,C998r,C998s,C998u,C998x,C998y,C999l;
retained contracts and the exact witness hash are in C998y's Hypotheses.
The critical checks are factor2 in the exponential RKHS norm,retention
of endpoint atoms through the cutoff,exterior Gaussian norm,real-product
analytic continuation,all event gaps and the specified9-operation loop.
Exact quadrature errors must remain separate from complete numerical
and weighted-dual errors. Future audit must not claim a universal
algorithmic lower bound or a negative Gram. No actual entry is known.

Bounded approval test: determine whether the saved primary statements
and their already inspected proof cases cover every listed audit
technique. Approve one unchanged conceptual audit if so; otherwise name
the essential missing result and restrict to that source. No algorithm,
node order,witness or trial-space change is proposed. No cross-notebook
input; full matching Mathlib coverage remains unchecked. Uniform signed
S3 control against BOTH defects,H2 and actual-Xi/global transfer remain
open. No justified new creative mechanism is supplied by this finite
certificate; do not label its routine specialization creative.
