# Conjugate-rate finite-convolution basis: source comparison1225

TARGET: Establish or refute the extension of Sra author-v3 C.6/(C.17)'s finite-convolution moving basis to C030q's exact conjugate-pair family: the source basis must be real and nonsingular, with alpha_i(x)=(n-2i-1)/x-(G_(i+1,b)(x)-G_(i,b)(x)) for 0<=i<d and 1<=d<=floor(n/2), throughout x>0 and x*A<=1/4.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused source1202/1213/1217 and C030l/C030q; scoped basis/determinant duplicate and named-stop searches found the nomination but no completed local extension. Fresh exact finite-exponential/complex-Hankel, quasi-definite-functional and complex-HCIZ searches located the primary statements below. No inference of novelty from search failure; query/read details below.
SOURCE_EVIDENCE: Sra author-v3 C.5 full proof pp22-23, C.6 full proof pp23-25, (C.17) p27, and C.9 basis-construction/parameter-derivative proof pp27-28 inspected; McSwiggen arXiv1712.03995v4 (2) p2, Theorem1 pp3-4 and continuation after(24) p10 inspected, reusing1213; Pozza--Pranic--Strakos ETNA50(2018), Definitions1.1-1.2/Theorem1.3/(1.3), p2, inspected. Direct primary URLs and qualifications below.
COMPARISON: The source supplies the determinant normalization and the actual derivative-moment orthogonalization, and standard complex HCIZ/quasi-definite theory supplies its algebraic prerequisites. Sra states C.5/C.6/C.9 for positive real rates. A later proof must justify the changed-rate determinant identity, its prefactor sign and all real signed pivots before differentiating the source basis. No inspected theorem directly states this entire specialization.
GAP: Establish the conjugate-rate determinant identity with its exact constant and repeated-rate limits, then check the real nonsingular source normalization and diagonal identity on the closed phase window. C030q supplies orbital nonvanishing, not this identification. Actual-Xi finite-reference supply, phase/degree/time, signed complement, off-diagonal norm control, all-degree positivity, theta signing and graph realization remain independent.
REASON: The essential construction and denominators are now located in inspected primary passages, so one source-based specialization is justified without new browsing. This literature turn proves no extension, new inequality or counterexample. The newly ready assessment requires separate next-turn approval before research.
SCOPE: Exactly nomination1224's finite family m>=1,n>=2m,a_l,r>0,b_l real, x>0,x*A<=1/4, with independent basis dimension 1<=d<=floor(n/2). Include n=2m, all contrast signs, zero phases, repeated rates and the closed phase boundary. Only the source-defined basis and displayed diagonal identity; no variance positivity, C.9 norm estimate, global PF or actual-Xi transfer is approved.
LITERATURE_REASON: Essential changed-rate basis/determinant coverage was missing from the orbital-only audit1222/1224. Reused unchanged orbital coverage; retrieved the source's actual construction and the necessary complex/algebraic theorem statements.

## Gap, use and discriminating test

The main gap is L030-L032/C032a actual-Xi all-degree positivity. A
source-defined finite-convolution interpretation would give the audited
C030q phase cost a precise possible use. Continue if a later proof pays
the exact determinant identity and real signed pivots, including
coincident rates and boundary phases. Isolate a failed constant, pivot
or continuation hypothesis if it cannot. Samples or a prescribed
diagonal for an unrelated basis do not meet TARGET. No independent Xi,
signed-complement or realization gap is assumed away.

## Local coverage and failure comparison

Read assessment1202 and working1202, the source-relevant records1213/1217,
C030l's real-array proof and downstream qualifications, and C030q's
hypotheses/nonvanishing and response proof ranges. Reuse audit1224;
this is not another independent audit of its bound. The only matching
basis nomination found by the scoped filename/content searches was1224.
No completed conjugate-rate convolution identification was found in
these checked records. This is a bounded duplicate check, not a
notebook-wide originality claim.

Read stops1117/1181/1193/1200/1107 and review884's finite-reference
qualification. They prohibit their stated automatic transfers, not this
new finite interface. In particular a degree-growing factor budget and
an unpaid signed remainder are not removed by giving a finite basis.
Prior orbital complex-HCIZ and small-coupling comparisons1213/1217 are
reused; no asymptotic theorem or complex stochastic order is imported.

## Primary source statements and cases actually inspected

**Finite convolution and source basis.** S. Sra, *On some positivity
properties of the Riemann Xi function*,
[author v3, released 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf).
Numbering is author-v3, not Hub-v1; (C.17) is an equation, not Lemma C.17.
Inspected C.5's full positive-real-rate construction and proof, C.6's
full determinant identity/proof, and C.9 through (C.23). The Exp(q)
normalization is q*exp(-q*t) on t>0, as also visible in C.5's
single-kernel minor and C.6's partial-fraction numerator.

Use the source's signed determinant D_k=mathcal D_k(f;x), D_0=1,
and put F_j=product_(h=0)^(j-1) h!, F_0=1, to avoid confusing its
factorial constant C_j with its basis matrix C_x. C.6/(C.10) states

    D_k(x)=d_k*x^(k*(n-k))*Z_k(x),  0<=k<=n,
    d_k=(product_l q_l)^k * F_k*F_(n-k)/F_n.

Its hypotheses are q_l>0, normalized Haar measure, x>0; repeated rates
are explicitly included. The proof treats distinct rates using partial
fractions, signed Cauchy--Binet, the HCIZ determinant with its precise
factorial convention, projection-spectrum confluence and subset
Vandermonde signs. It then treats repeated rates by continuity of the
companion-matrix exponential with initial derivatives zero through n-2
and derivative product_l q_l at n-1. The last step (C.13) identifies
positive-real tilted expectations by compact-support uniqueness. That
probability-law step must not be imported for complex rates.

C.5 orthogonalizes L_x(P)=P(partial_x)f(x) in polynomial degrees
0,...,n-1 once all its leading Hankel determinants are nonzero. Its
normalization has alternating norms and positive leading coefficients;
its diagonal formula is alpha_i=(log(D_(i+1)/D_i))'. C.9's proof
explicitly makes the monic coefficients rational in analytic moments
and chooses positive square roots of absolute nonzero pivots. This,
rather than ordinary positive-definite Gram--Schmidt, defines the
source's real basis. The proof differentiates the evaluation parameter,
not the polynomial variable, obtaining (C.21). Its first d rows close.
These are source statements under the source hypotheses, not claims
that their changed-rate premises have been established here.

**Complex orbital formula.** C. McSwiggen, *A new proof of Harish-Chandra's
integral formula*, [arXiv1712.03995v4, 27 April 2020](https://arxiv.org/pdf/1712.03995v4),
(2) p2, definitions pp3-4, Theorem1 p4, continuation after(24) p10.
Theorem1 allows Cartan variables in the complexified Lie algebra and
uses probability Haar measure. Equation(2) records the unitary trace
normalization and explains its SU(N)/central-factor relation. The
discriminant-multiplied formula extends analytically to singular
spectra; division by a zero Vandermonde is not licensed. Reuse1213's
earlier inspection; refreshed only the statements and continuation
needed here. No general HCIZ reproof is justified. This theorem is an
identity, not a sign, nonvanishing or variance theorem for a complex law.

**Algebraic orthogonalization prerequisite.** S. Pozza, M. S. Pranic and
Z. Strakos, *The Lanczos algorithm and complex Gauss quadrature*,
Electronic Transactions on Numerical Analysis 50 (2018), 1-19,
[publisher PDF](https://epub.oeaw.ac.at/0xc1aa5572%200x0039ff98.pdf),
Definitions1.1-1.2, Theorem1.3 and (1.3), p2. The inspected theorem
equates existence of orthogonal polynomials through a finite degree k
for the bilinear functional L(PQ), generally complex, with nonzero
leading Hankel determinants through size k+1. It does not require a
positive measure. Its recurrence has ratios of nonzero norms. The
article cites classical proofs (Chihara, Chapter I Theorem3.1, and
another reference); those book proofs were not newly read. This
theorem supplies existence only. Reality, alternating pivot signs,
positive real normalization and smooth parameter dependence for TARGET
must still be checked against the source construction. Do not replace
the bilinear form by a sesquilinear form or assert an infinite sequence
for this finite functional.

## Exact residual work authorized after separate approval

Keep the target unchanged. Define the proposed complex factors using
the source's q*exp(-q*t) convention and its convolution, with rates
the diagonal of C030q's D_b; do not call individual complex factors
positive probability densities. Prove the changed-rate version of the
displayed C.10 identity before using it to identify any determinant.
Either the source's finite determinant algebra with complex HCIZ and
removable confluence, or a fully justified holomorphic continuation of
the same normalized convolution identity, is within the assessed scope.
Check the rate-domain analyticity of both sides and the exact constant;
do not infer an identity from continuity off the real locus alone.

Then verify the prefactor's sign for this conjugate multiset, the
reality of the convolution moments, and the leading determinant signs
required by C.5/C.9 using C030q's positive orbital normalizers. Establish
the source's monic polynomials and positive real normalizations from
those actual moments, with no singularity at zero phases or repeated
rates. Check smoothness locally at every x in the closed phase window
before differentiating to obtain the nominated alpha identity. Preserve
each rank's own Z_(k,b) and hold every rate fixed under differentiation.
Dimension d and pair count m remain different parameters. Limits at
x=0, unbounded time and an infinite reference are outside TARGET.

This is a specialization/reproduction task, not a creative theorem
search. The reworking is justified by a changed hypothesis outside
Sra's stated positive-real-rate theorem. Cite HCIZ and the standard
quasi-definite existence theorem; do not reprove them. Even a successful
diagonal identity would not extend the positive-variance estimate
(C.22), the C.9 shift norm or signed smoothing. Those are different,
uncovered targets.

## Search, access and remaining qualifications

Queries issued included: `"Sra" "moving" "basis" "convolution"`;
`"exponential convolution" "complex" "Wronskian"`;
`"finite exponential" convolution "complex" Hankel determinant Grassmannian`;
`"quasi-definite" "linear functional" "orthogonal polynomials" Hankel`;
`"Harish-Chandra" "complex" "analytic continuation" McSwiggen`;
`"exponential splines" "complex" "Chebyshev" interval`;
and `Gauss quadrature quasi-definite linear functionals Pozza Pranic Strakos 2017 pdf`.
The author-v3 exact-equation/title queries recovered its indexed primary
text. The initial direct PDF open failed and shell curl had a DNS
failure; opening the indexed author URL then supplied the complete
relevant proof text. The first author-hosted ETNA link redirected in a
loop; the publisher PDF worked. No essential source blocker remains.

Exponential-Chebyshev and Bernstein-operator papers surfaced as optional
leads; no primary theorem from those leads was inspected or used. They
are not prerequisites for the bounded determinant/pivot test. No source
counterexample settling this exact window was located; no claim of
originality or truth follows. Full matching Mathlib coverage remains
unchecked. No mathematical scripts or cross-notebook input were used.
