# Same-mesh matched-prefix admissibility — separate continuation

TARGET: Test whether Lamprecht's same-mesh diagonal criterion can hold in any degree d>=5 for c0=...=c4=1 and 0<c5<1, including weak separation, extremal q-symbols and arbitrary later real entries.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step488's restricted-class multiplier search and step484's universal-preserver comparison; changed quantifier and equality cases are recorded in the completed mesh-restricted-central-transfer assessment.
SOURCE_EVIDENCE: Lamprecht https://arxiv.org/html/1210.1102v1 (3 October 2012), pp.2--5 definitions/Theorem4(b,c), pp.21--22 Theorem27/full proof, pp.26--28 Theorem31(b,c)/full proof and proof of Theorem4. Leake--Ryder https://arxiv.org/pdf/1712.02499v1 pp.15--16 Corollary1.2/full boundary-degree limiting proof. Inspected step488.
COMPARISON: Known q-multiplier classification and its nonextremal log-concavity consequence cover this algebraic test. C792a's repeated-root witness is outside the separated class; L792 certifies one particular image, not same-mesh class preservation.
GAP: Exact prefix application, extremal alternative and passage between full-degree positive inputs and source closure classes remain unproved locally. No mesh-losing tolerance or actual-family obstruction is established.
REASON: Isolate a restricted-class symbol-admissibility question uniformly in d,Q instead of repeating universal preservation, degree sweeps or the constant pencil; derive only the application of known tools.
SCOPE: One algebraic test for d>=5 and 0<q=1/Q<1; no numerical replay, model coefficients, parameter rescue, actual Xi signs or mesh-loss claims. Newly saved ready coverage requires separate approval before research.

Main gap: actual-Xi all-degree mixed positivity. A same-mesh fallback
would transfer model separation as well as root reality. Testing its
prefix criterion decides whether that particular source-backed fallback
is available. Independent growing-degree model/separation and signed
residual estimates remain unpaid.

Inputs: C792a, L791/L792 and inherited L778/L018/L021/L776, with the
complete original exact-data widths and analytic/evaluator/software
contracts. Use c_j=R_j/F_j through5; allow arbitrary later real entries,
including zeros or negative entries. Assume neither invertibility nor an
infinite extension. No certificate replay is proposed.

Let C_j^d(q) be the coefficient of z^j in
R_d(q;z)=prod_(k=0)^(d-1)(1+q^k z). Test
H_(d,q)=sum C_j^d(q)c_j z^j, not the ordinary binomial symbol.
Reflection relates positive and negative roots. The proposed input class
has degree d, positive simple roots and consecutive ratios at least Q;
the property under test retains this same lower ratio and nonzero images.
Justify weak/strict, closure and degree-boundary passages before using
Theorem4(b); the source classes allow lower degrees and zero roots.

The source distinction is between extremal q-symbols and nonextremal
symbols with strict log-concavity of normalized coefficients. Check both
alternatives rather than assuming ordinary-symbol rigidity carries over.
Import the primary theorem by citation and prove only exact applicability.
Known-method specialization, no novelty claim; Mathlib matching coverage
unchecked. Full proof/citations belong in a canonical lemma if established.

Continue only with a rigorous uniform conclusion in d,q and all later
entries. If a required premise is unavailable or an admissible symbol
survives, record the precise limitation. No finite sweep. Same-mesh failure
must not be called failure of positive-root preservation with mesh loss,
particular-family transfer or RH. This routine symbolic test is not a
creative mechanism; independent signed control still blocks that route.
