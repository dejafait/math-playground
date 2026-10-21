# Charge-seven family form versus metric symplectic form — source coverage ready

TARGET: Test whether the metric-normalized comparison of L062's family form with L067's L2 symplectic form forces a sign contradiction for F.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the L062 normalization and L067 geodesy audit assessments; scoped their proofs, the original geodesy assessment, histories 118/136 and ATTEMPTS/047 for duplicates/stops. Bounded searches for K3 instanton L2/trace/Mukai sign conventions and Nahm-transform metric normalization located Yang Li's primary gauge formulas; no inspected theorem gives the exact fixed-family coefficient with all notebook conventions.
SOURCE_EVIDENCE: Verbitsky alg-geom/9307008v1 (29 July 1993), Sections 1/3/4/6/7/9, especially Corollary 4.3, the construction before Corollary 7.1 and complete Proposition 9.1 proof, PDF pp. 3, 11–12, 16, 23–28, 34–37; Yang Li arXiv:1908.05017v1 (14 August 2019), full Section 2.2/Theorem 2.10 proof and equations (1)–(2), Lemma 2.12 equation (4), and complete Proposition 3.1 proof/equations (6)–(8)/Remark 9, PDF pp. 5–7, 9–10; Kuznetsov–Markushevich math/0703264v2, Section 2/Theorem 2.2/equation (12), PDF pp. 9–10; accessed 2026-10-07.
COMPARISON: Primary sources now fix the positive real unitary L2 trace metric, induced quaternionic action, harmonic quotient and real symplectic integral; these cover the comparison tools. The signed conversion to L062's ordered (0,1) integral remains a specialization. Li's global duality requires an isotropic Mukai vector and is inapplicable here; his printed equation (6) and proof ending exhibit an apparent sign mismatch, so that equation is not a signed input.
GAP: In a separate research turn identify the exact scalar between the metric-defined holomorphic symplectic form and L062's ordered integral, keeping real/complex tangent conventions, negative unitary trace, (2pi i)^2 and fixed sigma=omega_J+i omega_K. Determine the resulting positive-scale compatibility without assuming a moduli surface or citing the suspect period formula.
REASON: Essential unread normalization coverage has been retrieved; local gauge formulas permit the saved bounded test using known tools. A short explicit convention comparison is necessary because the printed global formulas do not safely certify its sign; no coefficient, exclusion or existence conclusion was derived in this literature-only turn.
SCOPE: Conditional actual L052/L060 F at the identical fixed-metric B x Y, L062's exact ordered pairing, and L063/L064/L067's natural quaternionic map; only metric/trace/tangent normalization and its positive-scale test. No new metric, H-for-h substitution, global embedding, universal family, F existence, inverse or transport.
LITERATURE_REASON: The saved REVIEW_REQUIRED target needs an essential L2-to-ordered-Yoneda convention comparison absent from the ready earlier audits; Li's explicit gauge formulas are a new relevant primary lead, not repeated browsing of their already approved conclusions.
COVERED_TARGET: Test whether the metric-normalized comparison of L062's family form with L067's L2 symplectic form forces a sign contradiction for F.

## Relevance, retained data and test

The main gap is algebraic realization of arbitrary primitive rational
Hodge classes, even on fourfolds; no complete candidate exists.
This intermediate test concerns only the actual conditional charge-seven
family with ch_2(F)=-6e_1-7e_2+tau_D, c_1=0 and
D(sigma)=2lambda sigma, 1<lambda<3/2. L052/L060 provide its
compatible hyperholomorphic connection and stable fibres; L063/L064
provide the natural classifying map, and audited L067 supplies its
quaternionic differential and a positive unspecified L2 scale.

A convention-verified nonpositive forced scale would exclude this F
and redirect the bundle-representative search. A compatible positive
scale ends this sign test, without proving existence. If the calculation
finds a substantive convention error in an input, record the correction
rather than treating the error as an obstruction. An unresolved tangent
identification must be exposed rather than replaced by an assumption.
Separation, reconstruction, larger-charge realization, transverse
transport and universal primitive Hodge algebraicity remain independent.

ATTEMPTS/047 and L068 stop the bounded tangent-character/index route.
The saved L062 audit settled its ordered curvature normalization;
L067 deliberately did not read a positive metric coefficient from it.
Scoped checks of those canonical passages and the original geodesy
assessment found no completed version of this sign test. Neither the
old index stop nor the independently parked flat-index source blocker
is a ban on this distinct necessary condition. No new index is proposed.

## Primary local metric and tangent inputs

[Yang Li, *Mukai duality on K3 surfaces from the differential geometric
perspective*, arXiv:1908.05017v1](https://arxiv.org/pdf/1908.05017v1#page=5),
Section 2.2, Theorem 2.10 and its complete proof, PDF pp. 5–6,
starts with a fixed Hermitian bundle of Mukai vector v, compares stable
holomorphic structures with HYM connections, and constructs the
hyperkahler quotient of projective unitary connections. Its local
construction is not restricted to a four-real-dimensional quotient.
The separately named Mukai dual and global universal-bundle construction
in Section 2.3 explicitly impose (v,v)=0 and additional global conditions.
Those conditions are not imported for this test.

With X denoting Li's K3 and A his affine connection space, the source
specifies, for real trace-free skew-Hermitian one-form variations a,b,

\[
 G_{\rm Li}(a,b)=\frac1{4\pi^2}\int_X\langle a,b\rangle\,d\mathrm{Vol}_X,
 \qquad
 \omega_i^{\mathcal A}(a,b)=-\frac1{4\pi^2}
                      \int_X\operatorname{Tr}(a\wedge b)\wedge\omega_i^X.
\]

Here the coefficient inner product uses the negative su(r) trace
pairing. The source defines the induced operator by
I_i^{\mathcal A}a=-a\circ I_i^X and states
omega_i^{A}(a,b)=G_Li(I_i^{A}a,b). Equations (1)–(2), PDF p. 6,
identify the smooth quotient tangent with the Coulomb/linearized-ASD
space d_A^*a=0, d_A^+a=0; the metric and three forms are their
restrictions to that space. Gauge directions are d_A Phi. These are
explicit metric conventions, not an equality only up to an arbitrary
complex scalar. A different positive L2 normalization must rescale the
metric and all three forms together.

The smooth stable/irreducible locus, fixed determinant and natural
harmonic quotient are the setting already covered for L067. H^1(O_Y)=0
removes a determinant tangent here. The gauge construction uses the
fixed hyperkahler metric; its local formulas do not require replacing
h by L063's integral H. The research turn must still express the actual
KS tangent in these coordinates and compare the normalization of real
connection variations with Dolbeault (0,1) representatives. No equality
of those norms has been derived in this review.

[Li, Lemma 2.12 and equation (4)](https://arxiv.org/pdf/1908.05017v1#page=7),
PDF p. 7, explicitly gives mixed universal curvature
R_univ(a,u)=a(u) for a Coulomb-gauge variation and a fibre vector u.
The horizontal connection uses G_A d_A^*a, with G_A the inverse
trace-free scalar Laplacian at an irreducible connection. This is useful
local comparison evidence; its global U(r) lift is not a hypothesis
or conclusion about F. The actual family's tangent must be treated
through the natural quotient, retaining horizontal gauge terms.

## Reused quaternionic and family-form inputs

[Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
Section 3, PDF p. 11, fixes the End(E) real structure A -> -A^*,
which extends to coefficient forms. Section 4, PDF pp. 12 and 16,
constructs bar-J by combining J on forms with that real structure;
Corollary 4.3 gives its harmonic quaternionic action, and the paragraph
following defines Lambda_c. Section 7, PDF pp. 25–28, decomposes a
real unitary variation into its (1,0) part rho and its coefficient-real
conjugate. The construction before Corollary 7.1 explicitly equips the
(1,0)-coordinate parameter space with the conjugate complex structure.
It identifies the local-family differential with KS. Plain scalar
complex conjugation cannot silently replace this coefficient operation.

Section 9, PDF pp. 34–37, defines the positive metric by integration
of the pointwise Hermitian inner product on harmonic classes. It
constructs the form from cup-product, trace and the Lambda_c functional.
Proposition 9.1 and its complete proof give the corresponding harmonic
(1,0) expression integral Tr Lambda_c(alpha wedge beta) dVol and
identify it with the quaternionic metric form. This supports L067's
metric construction; translating it to the notebook's ordered (0,1)
pairing remains work for the research turn.

There is a convention qualification: Section 1, PDF p. 3, defines
omega_I(u,v)=g(Iu,v), while the preliminary quaternionic-vector-space
paragraph before Definition 6.5, PDF p. 23, prints omega_I(u,v)=g(u,Iv).
Do not identify these printed expressions as the same signed form.
Use the explicit real-connection convention from Li and track all
conjugations; no correction of Verbitsky's text or of L067 is asserted
by this source review. Fix J,K throughout rather than relying on the
same preliminary paragraph's claim of independence of their choice.

[Kuznetsov–Markushevich, *Symplectic structures on moduli spaces of
sheaves via the Atiyah class*, math/0703264v2](https://arxiv.org/pdf/math/0703264v2#page=10),
Section 2, Theorem 2.2 and equation (12), applies to the smooth locus
of stable or simple sheaves on a smooth complex projective Y. For a
surface its form is ordered Yoneda composition, trace and pairing with
a holomorphic two-form. Its family construction uses KS; it is not a
signed L2 comparison. Reuse the detailed coverage in the
[normalization audit assessment](2026-10-06-charge-seven-family-form-critical-audit.md)
and [geodesy audit assessment](2026-10-07-charge-seven-geodesy-critical-audit.md),
including Huybrechts–Lehn's trace/KS tools and the ordinary Chern–Weil
formula. L062 already fixes the explicit integral prefactor, order and
complex fibre orientation. Their general theorems need no reproof.

## Stronger-result comparison and source warning

[Li, Proposition 3.1, equations (6)–(8) and Remark 9](https://arxiv.org/pdf/1908.05017v1#page=9),
PDF pp. 9–10, computes periods using a universal connection for a
Mukai dual K3 surface. The complete proof retains the vertical/horizontal
curvature cross-term and determinant correction, evaluates both mixed
curvature contractions, and identifies its resulting trace integral
as minus the metric hyperkahler form. Remark 9 explicitly warns of
different numerical factors in Donaldson–Kronheimer, p. 197, and fixes
fibre-integration ordering.

The accessible primary PDF text prints a positive
(ch_2-c_1^2/(2r)) term in equation (6), whereas its proof's last sentence
identifies the computed contraction as minus the hyperkahler form.
This is an apparent internal sign mismatch, not a verified erratum or
a repaired theorem. Equation (6) must not decide this target's sign.
The explicit local gauge/metric definitions in Section 2.2 are available
independently; use them and L062's fixed ordered integral for the
comparison. This targeted verification is why a short specialization
is justified rather than importing the suspect signed period formula.

The global Mukai-duality/isometry theorems require an isotropic vector
and a K3 moduli surface. The retained charge-seven vector is (2,0,-5),
with the rank-twenty-two tangent already recorded in L068. Neither the
isotropic hypothesis nor a global universal family is available here.
No global duality, inverse transform, volume equality or F exclusion
is imported. The proposed target lies within the local metric formula
and harmonic-tangent coverage, not those stronger global results.

## Search record, access and coverage limits

Queries: `instanton moduli K3 L2 holomorphic symplectic form trace wedge
Mukai sign quaternionic`; `Verbitsky hyperholomorphic bundles 9307008
metric symplectic form trace`; `K3 instanton moduli metric symplectic
form trace omega L2`; `hyperkahler moduli connections symplectic form
-tr K3`; `Nahm transform K3 Mukai symplectic L2 metric normalization`.
The direct Verbitsky and Li PDFs supplied the load-bearing statements
and proof cases above; Kuznetsov–Markushevich's exact surface statement
was checked. No novelty conclusion follows from the bounded search.

Itoh's *Gauge fields and Kahler geometry* was located as a lead, but
its publisher/Euclid access attempts did not provide its proof text;
it is not an input. Li's reference [6] is Donaldson–Kronheimer,
*The Geometry of Four-Manifolds* (1990), p. 197 and Proposition 5.2.17.
Those passages were not extracted here and are not a second certified
normalization. They are unnecessary for the approved direct local
comparison. Shell download failed DNS and web PDF screenshots were
unavailable; the required primary text remained accessible through web
PDF extraction, including the complete relevant Li proof and local
metric construction. These access failures therefore do not block the
saved target. No other source or theorem is asserted inspected.

Mathlib: coverage of the combined L2/Yoneda metric comparison has not
been checked. Theoretical absence is not asserted. No mathematical
script, new lemma, numerical evidence or F verdict was produced.

Coverage is ready for this exact bounded target in a separate research
turn, subject to the supervisor's separate assessment approval. Keep
that target unchanged. A ready assessment is not its mathematical
verification; a positive or negative metric-scale verdict remains open.
