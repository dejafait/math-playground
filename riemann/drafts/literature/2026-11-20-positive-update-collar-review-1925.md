# Positive-update collar representation: source approval1926

TARGET: Test the same fixed degree-four collar using the two-atom Uvarov kernel representation, certifying its positive 2x2 update divisor and attempting one residual-range/Krawczyk evaluation per affine orientation with unchanged moments.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused arbitrary-site and exact-image searches in source-notes1908/1920/1924; narrowly checked C028t/u, working1925 and the named Cramer failure. Reopened the primary multi-site theorem for its matrix convention and proof; details in source-notes1926.
SOURCE_EVIDENCE: Delgado et al SIGMA12(2016)090 Section2 (2.3), Section3 (3.1)-(3.14), Theorem3.1 pp8-10, primary PDF https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf (reopened2026-11-20); reuse Gautschi2004 Theorem2.1 https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf and Rump2010 Theorem13.3 https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf as fully assessed1920/1924. These sources supply no numerical collar divisor or derivative bound.
COMPARISON: The imported formula gives the same monic quartic using the base degree-three kernel and a two-site update matrix instead of the failed mixed-moment Cramer enclosure. It changes evaluation, not the reference family or matching problem; point rank and all old stops remain.
GAP: Implement and verify base norms, a positive update-divisor enclosure, every site derivative and variance bound on the unchanged collar; then try the existing two-orientation sufficient tests. Success and quantitative improvement remain unknown.
REASON: Exact primary coverage clears the changed representation's source gate; the remaining task is ordinary finite specialization and rigorous enclosure, not a new Uvarov theorem or RH advance.
SCOPE: Same d=4, unit masses, B=[-1/4,1/4]x[3/4,5/4], x0=(0,1), unchanged raw panel0 moments and both signs; finite Gram/kernel algebra, positivity-preserving determinant evaluation and complete site differentiation only. No subdivision, sweep, solver, radius/mass change or source refinement.

Main gap: L030-L032/C032a actual-Xi all-degree positivity and C028b's
H_d=o(d). The proposed finite test can only settle this collar's matching;
it cannot give a uniform-degree cost or new RH conclusion.

Essential inputs: C028a/d/h/q/t, L019/L021, unchanged L917 panel0 raw
I_0,I_2,I_4,I_6,I_8 and audit197 under L037, plus source-notes1924 and
the complete attempt1925 certificates. Reference probability moments
have no factorial factors; actual coefficients retain j!/(2j)!; empirical
power sums divide by4. Do not assume actual-root reality or positive
variance bounds that the changed arithmetic has not enclosed.

The bounded continuation test, approved by source review1926, is the same fixed B and two
orientations, with no solver, subdivision or source refinement. A usable
uniformly positive update divisor and variance enclosure must precede
any nonlinear verification. An unpaid divisor or failed sufficient test
remains inconclusive. Primary theorem coverage should be reused when
adequate; no fresh browsing quota is intended. Full matching Mathlib
coverage remains unchecked. No mathematical derivation or calculation of
the proposed representation was performed in1925 or this literature turn.
See [source-notes1926](2026-11-20-positive-update-source-notes-1926.md)
for the exact import, applicability and remaining certificate obligations.

Source-URL recovery1927: the direct published PDF above is accessible;
its Section3 setup and Theorem3.1 statement/proof, printed pp8-10,
confirm the already recorded quasi-definiteness hypotheses and matrix
convention. The other two URLs identify previously assessed inputs,
whose coverage is reused without repeating their retrieval. This repairs
the assessment's missing direct URL; target, scope, SPECIALIZE decision
and unpaid obligations are unchanged. No new mathematical result or
certificate is supplied, and full matching Mathlib coverage remains unchecked.
