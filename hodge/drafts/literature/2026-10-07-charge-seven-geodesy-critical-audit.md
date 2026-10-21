# Charge-seven geodesy specialization — critical-audit coverage ready

TARGET: Critically audit L067's rotation-compatible classifying map, constant L2 homothety and fixed-metric total geodesy.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready geodesy assessment and L064 audit coverage; read full L067, its working note and histories 136--137, ATTEMPTS/046 and L064's natural tangent passage; narrowly located the primary local-family and trace-free smoothness statements, without repeating broad discovery queries.
SOURCE_EVIDENCE: Verbitsky alg-geom/9307008v1 (29 July 1993), Definition 6.3/Theorems 6.1--6.4, Section 7 through Corollary 7.1, Section 9 proof and Corollary 10.1, PDF pp. 22--27, 34--37; Huybrechts--Lehn (1997), complete 4.5.1 proof/4.5.2 and 4.5.3--4.5.4, printed pp. 101--102; Verbitsky alg-geom/9610010v1 (9 October 1996), Propositions 5.1--5.2, Definition 5.3/Corollary 5.4 and Appendix 5.3, PDF pp. 29--31; accessed 2026-10-07.
COMPARISON: General local-family, natural deformation, harmonic L2 and embedding theorems cover the audit tools; Corollary 7.1 and Theorem 4.5.4 make the local-family and trace-free smoothness sources explicit. They do not directly prove L067's actual-family analytic/coarse-germ comparison or fixed-metric specialization.
GAP: Independently check the rotation identification and construct the natural analytic/coarse-germ comparison, then audit harmonic-quotient compatibility, the constant-scale argument and local geodesy at the fixed source connection; coverage approval certifies none of these conclusions.
REASON: The separate audit now has explicit primary local-family and trace-free smoothness coverage as well as reused metric/geodesy inputs; return to mathematics for this exact audit, narrowing any unsupported bridge rather than adding it as a hypothesis.
SCOPE: Audit L067 for L052/L060's actual conditional invariant-curvature F on the identical marked K3 factors at the fixed common metric, every stable charge-seven fibre, L062 KS injectivity and L063/L064's natural common-H coarse map. No global separation, normality, completeness, inverse, F existence, reconstruction or transverse transport.
LITERATURE_REASON: The supervisor requires separate coverage for the newly proposed audit; the explicit local classifying-family construction and trace-free algebraic smoothness criterion were essential to comparing its coarse-germ bridge, while the prior metric and geodesy assessment remains adequate.

## Gap, intermediate target and decision test

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes, even on arbitrary fourfolds. This intermediate target is a
critical audit of L067's conditional local geometric constraint. If reliable,
it could support a later branch-identification test; that downstream use
has not been proved or approved here. F existence and transport remain
independent gaps.

Continue using L067 only if its actual-family bridge and every metric
inference survive. If a bridge fails, identify it and repair or narrow the
claim. Neither equal tangent dimensions nor an abstract hyperkahler
isomorphism suffices for naturality. This is source comparison only;
no proof audit, new specialization or mathematical derivation is completed.

## Primary evidence and reused coverage

Reuse [the application assessment](2026-10-07-charge-seven-classifying-map-total-geodesy.md)
and [the natural coarse-tangent audit coverage](2026-10-07-charge-seven-finite-unramified-critical-audit.md).
Their source hypotheses remain unchanged.

[Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1#page=22),
29 July 1993: Definition 6.3/Theorem 6.1 give local classifying maps and
natural KS tangents; the text distinguishes the coarse space from its
reduction. Section 7 identifies degree-zero irreducible Hermite--Einstein
connections with stable bundles. The construction preceding Corollary 7.1
(pp. 26--27), read through its conclusion, supplies a local universal
variation and tracks the conjugate complex structure in its harmonic
coordinates. Section 9 constructs the metric on harmonic classes and
its quaternionic action; Corollary 10.1 compares rotations. Theorems
6.3--6.4 and the following surface qualification provide smooth local
metric coverage. Theorems 2.1--2.4 were also reread narrowly for
integrability, zero contraction and uniqueness. None directly identifies
the given algebraic family map with these analytic charts.

[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31 (1997), 4.5.1--4.5.4, pp. 101--102](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113):
4.5.1 concerns the completed local deformation functor, and its full proof
constructs an etale slice carrying the restricted Quot family. 4.5.2 gives
the canonical tangent; its smoothness criterion uses full Ext^2 vanishing.
4.5.3--4.5.4 instead give determinant/trace-free obstruction control and
smoothness for a positive-rank stable sheaf on a smooth projective variety
when Ext^2_0 vanishes. This is the precise algebraic criterion to cite in
the audit. A formal deformation comparison alone is not an analytic
classifying map; the actual local-family comparison remains an audit
obligation. Exact GAGA/Dolbeault comparison is reused from the L064
assessment, within its projective coefficient-bundle scope.

[Verbitsky, *Deformations of trianalytic subvarieties of hyperkahler
manifolds*, alg-geom/9610010v1](https://arxiv.org/pdf/alg-geom/9610010v1#page=29),
9 October 1996: Propositions 5.1--5.2 and Definition 5.3/Corollary 5.4
require quaternionic and metric compatibility, and permit noncompact
ambient manifolds. The complete relevant Appendix 5.3 proof was reread.
Keep the stronger all-hyperholomorphic connection hypothesis: the broader
printed Proposition 5.5 omits ambient zero contraction used in its proof.
No completeness or global separation conclusion is imported.

## Obligations for the separate mathematical audit

Check the following within the exact target, without extending it:

- L052/L060's fixed connection, every restricted fibre's irreducibility,
  simultaneous product rotation and the identity of nearby connection
  classes under each actual rotated family.
- Smoothness of both germs, including coarse-space versus reduction and
  the trace-free criterion. Construct the analytic comparison using
  actual local families; check its domain, stability/local-freeness
  neighborhoods, natural differential and agreement with f. Preserve
  the distinction between metric h and algebraic polarization H.
- The quaternionic action on the natural deformation quotient. Raw mixed
  curvature is not a harmonic representative; retain gauge terms and the
  conjugate-(1,0) convention when identifying tangents.
- L067's own dimension-four homothety and closedness arguments, common
  L2 normalization on overlapping charts and positive scale. These are
  the claimed specialization to audit, not imported theorem conclusions.
- Local embedded branches, both compatibility requirements of Definition
  5.3 and the fixed-versus-induced source Levi--Civita connection.

No essential source blocker remains for this audit scope. Coverage allows
checking or repairing applicability; it does not preapprove the result.
Mathlib coverage of the combined statement remains **not checked**.

## Duplicates and preserved stops

History 137 records L067's application, not an independent audit. L064's
audit establishes its natural family tangent but no metric comparison.
ATTEMPTS/046 stops the Euler/sheaf/first-order Hom test and remains intact;
ATTEMPTS/041--045 and the parked flat-index source blocker are unchanged.
The old generic trianalytic-exclusion theorem requires hypotheses not
established for this RM surface, as recorded in the reused application
assessment. No additional broad search is justified merely by the audit.
No exact-family theorem or originality conclusion is imported.
