# Negative first-Laguerre energy: source-review checkpoint

2026-10-30; literature only. Startup overview and DAG supplied and read.
Existing notebook changes are preserved. No lemma or mathematical script write.

Main gap: actual-Xi all-degree mixed positivity. Reviewed target is the
saved finite-interval backward negative-energy proposal. A useful comparison
might address L471's signed negative mass, independently of L486's stopped
positive-majorant certificate; normalization, global height control and
higher signs would remain gaps.

Local scope checked: L018; L471 hypotheses/conclusion; L486 Section 4;
L058 full heat-family statement and domination/local-branch proof; L019/L020;
L126 statement/counterexample and L128 finite-domain proof; historical
ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md and the relevant Csordas
source qualification in the 2026-10-03 Gaussian assessment. Narrow term search
found no pre-existing assessment of this precise negative-energy inequality.
No cross-notebook input.

Primary material reached, before final theorem comparison:
- Rodgers--Tao, arXiv:1801.05914v3, 6 March 2020, Introduction (1)--(4),
  Theorem 1.1 and Section 4 Theorem 4.1, proof and the energy discussion.
  Their H_0(z)=Xi(z/2)/8; use L058 directly for local normalization.
  Their zero-interaction energy assumes the real-simple-zero regime
  Lambda<t<=0, rather than the proposed clipped real-axis defect.
- Csordas, arXiv:1309.0055v2, 21 February 2014, Theorem 4.6,
  Open Problem 4.7, (4.9)--(4.10), Proposition 4.9. No backward clipped
  energy inequality is supplied in those passages; cited older proofs
  remain uninspected and are not imported.
- Brezis--Ponce, Kato's inequality up to the boundary, Comm. Contemp.
  Math. 10 (2008), 1217--1241, author-hosted published PDF:
  https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf
  Introduction (1.1), X definition and Theorems 1.1--1.3 inspected.
  Need Theorem 7.1 and its zero-trace case before final boundary comparison.
- Schatz, November 20 2025 preprint doi:10.5281/zenodo.17636625,
  title/abstract and Proposition 6.3 statement located; this concerns
  Im(-E'/E) in the upper half-plane on collision-free zero-free windows.
  No direct match to integral(-D_1)_+ and no accepted RH import.
  Its collision bridge and global proof are not audited here.

Planned discriminating target, not a result: fix I=[-2,2]; test exact real
even polynomial heat families of degree at most eight with positive
imaginary-axis values, zeros confined to |Im z|<=1/2, and D_1>0 in fixed
endpoint collars. These collars remove ambiguity about external flux.
Allow multiple real zeros. Ask whether -d_lambda E<=C E can hold through
a collision with C locally bounded, independent of division by E. Full
energy evolution, polynomial certificate and its answer are deferred.
An elementary collision specialization is a calculation, not a justified
creative actual-Xi attempt. Need explain this routing if retained.

## Completion of source review

Brezis--Ponce Theorem 7.1 and Lemmas 7.1--7.2 with the complete
positive/negative/zero boundary-trace proof were subsequently read.
Alber, PDE 2 (last modified 10 June 2018), Lemma 5.2 and Theorem 5.3,
pp. 89--91, supply the a.e. Sobolev truncation rule including zero sets;
the approximation/zero-level proof was inspected completely.
Keady, J. Austral. Math. Soc. A 48 (1990), 246--263, Theorem 1.2,
Maximum Principles 2.1--2.2 and Section 4/Theorem 4.0 identify positivity
and bounded coefficients as the relevant restriction. His logarithmic
localization is not a zero-safe clipped-energy theorem.
Schatz Proposition 6.3 and surrounding pp. 34--35 were read for scope;
its different unknown and collision-free region do not cover the target.
No verdict on its full claimed proof is asserted. Browser screenshot
requests produced no inspectable image in this interface; no formula
requiring those images is imported.

Final disposition is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED.
Full checked-source citations, boundary convention, queries and the
unproved finite-polynomial test are in the completed assessment. The
matching new test assessment awaits separate approval. No mathematical
advance, obstruction certificate, lemma, energy evolution, new estimate
or source novelty is claimed. PROOF.md and DAG.md need no change.
