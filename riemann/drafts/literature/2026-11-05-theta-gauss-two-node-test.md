# Actual theta two-node Gaussian rule — bounded interlacing test

TARGET: Construct the two-node Gaussian rule for the actual theta pushforward in v=u^2 from gamma(0..3), verify the degree-three Laguerre averaging identity, and certify or refute common interlacing of its two reference cubics.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step539's completed arbitrary-measure quadrature and exact Gaussian-quadrature/Jensen/common-interlacing comparison; its bounded local duplicate search found no matching actual two-node certificate. No novelty claim.
SOURCE_EVIDENCE: Gautschi, Orthogonal Polynomials: Computation and Approximation (OUP2004), Theorems1.6/1.19/1.45/1.46, pp1–3/7/21–23, primary scan https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf ; https://dlmf.nist.gov/3.5.E18 and https://dlmf.nist.gov/3.5.E20_1 ; reused Laguerre and MSS Definition3.1/Lemma3.5 coverage, with full read limits in the completed comparison.
COMPARISON: Standard quadrature covers exact finite moment compression; positive nodes/weights do not supply the common-interlacing premise. L795/L796 stop different stronger realizations. GORZ Theorem2 already covers degree-three hyperbolicity; only the specified representation test is sought.
GAP: Exact actual nodes/weights, the coefficient identity and the pair's interlacer gaps remain uncertified. No degree-uniform mechanism, mixed-positivity implication or RH conclusion follows from a pass.
REASON: One finite sufficient-premise test can decide whether moment compression avoids the recorded full-support obstruction without changing the actual polynomial. Import known theorems and derive only this bounded applicability difference.
SCOPE: Newly written in literature-only step539; separate next-turn approval is required before research. Degree three, two nodes, actual gamma(0..3) only. Intended research classification REPRODUCTION; conventional calculation, not creative proof work.

Read [the completed comparison](2026-11-05-theta-gauss-compressed-interlacing-scope.md)
for theorem hypotheses, essential proof cases, exact searches, known
overlap and the support/Favard/two-atom failures. Reuse it without
another discovery search unless its hypotheses change.

The main gap is actual-Xi all-degree mixed positivity. This intermediate
target tests a finite sufficient averaging premise with a plausible
later use in a degree-dependent mechanism. It is not a proposal to
reprove known central degree-three hyperbolicity.

Essential inputs: L019/L021 for K and all finite positive moments;
L795 for P_3, F_(3,u), exact factorial/scale conventions and the full
average; only L791's audited actual gamma(0..3) intervals, retaining
L778's analytic evaluator and software contracts. L796's actual-data
section identifies provenance and audit paths; its recurrence obstruction
is comparison only. No model parameter or root from L791, no L772
counterlaw and no desired actual-Xi sign is a mathematical input.
No cross-notebook use. Full matching Mathlib coverage is unchecked.

Before numerical use inspect complete selected values in
scripts/central-jacobi/fixed-model-certificate-476.json at /gamma/0
through /gamma/3 and the relevant provenance/PASS fields in
scripts/central-jacobi/audit-478/audit-report.json, using
`python3 ../scripts/loop/inspect_json.py` with --pointer and --full
only for those load-bearing values. Verify the input/audit hashes and
contracts as in L796; rounded decimal previews are not inputs. Recover
raw normalized v moments using gamma(j)=j!m_j/(2j)!; record the exact
conversion and all denominator bounds.

Construct the monic degree-two orthogonal node polynomial for the raw
v law, using its two orthogonality equations. Apply the cited theorem
after checking the positive infinite-support measure hypotheses. Use
its roots as the two distinct positive nodes and its interpolatory
weights; preserve exact definitions, including weight sum one. Verify
moment exactness through degree three and the polynomial identity for
L795's P_3. Do not replace the actual measure globally by an atomic law,
identify this node polynomial with P_2, or truncate the theta tail.
No reproof of general Gaussian quadrature or real-zero theorems is needed.

Then isolate the three positive Laguerre reference roots and bound the
two scaled root lists with rigorous rational or algebraic arithmetic.
Check both weak-alternation gaps in MSS Definition3.1, retaining possible
endpoint equality. Use both negative cubics if invoking the source's
positive-leading-coefficient version; the same positive quadrature
weights must still represent -P_3. A strict gap separation certifies
failure of this common-interlacer premise, not failure of P_3 hyperbolicity.
A pass needs certified inequalities, not plotted or floating roots.

Bound work to one symbolic construction and one outward exact-rational
evaluation of the inherited moment boxes. If interval dependence hides
the decision, allow at most one algebraic rearrangement; if still
undecided, save that limitation and stop. No fresh theta evaluation,
precision campaign, degree extension or weight optimization. An exact
endpoint case may be resolved symbolically within the same finite test;
an interval containing zero is not an equality certificate.

Save complete formulas, input hashes, interval endpoints, exactness
checks, denominator bounds, scaled-root gap comparisons and all failures
under scripts/theta-gauss/ during the later research turn. Print only
the actual/required bounds, decision, failures and certificate paths.
Canonicalize any established specialization in its own lemma with the
source citations, full proof and inherited qualifications. Neither a
passing pair nor an exact obstruction supplies degree-uniform control,
all-degree signs or a sufficient mixed-positivity assembly. Repeating a
failed pair needs a materially changed representation and a new gate.
