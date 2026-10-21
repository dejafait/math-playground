# Auxiliary Legendre coefficient field and native two-torsion field — source scope approved

TARGET: Determine whether L078's coefficient field T_0=Q(t) equals the native field F_tpd for the same auxiliary geometric curve, using the native definition and the action on ordered two-torsion.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step308 searched F_tpd, field-of-moduli/two-torsion and Legendre splitting-field terminology, then inspected the primary definition and ordered-level moduli results below; checked L078, L074's auxiliary hypotheses, step272, the normalization assessment and ATTEMPTS/027,028,031,032,033. No duplicate of this native field identification was found in those scoped records; no novelty claim follows.
SOURCE_EVIDENCE: [IUT IV, April 2020 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf), Proposition 1.8(ii),(iii),(vi) and relevant proofs pp.18–21, Theorem 1.10 p.22, Corollary 2.2(ii) p.42; [IUT I May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf), Definition 3.1(a),(b) pp.61–62; [Antieau–Meier arXiv:1608.00851v3 (5 May 2020)](https://arxiv.org/pdf/1608.00851v3), Definition 4.1, Lemma 4.3/proof, Proposition 4.5/proof, Corollary 4.6/proof and following S_3-action paragraph pp.13–15; [Auer–Top (2002)](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf), general-field six-parameter paragraph p.305; [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf), I Proposition 4.18/Remark 4.19 p.38 and Theorem 6.3 p.42. Details and version qualifications: drafts/2026-10-18-auxiliary-two-torsion-field-source-notes.md.
COMPARISON: The native definition and descent-independent two-torsion action, together with the ordered-level coarse parameter and its equivariance, cover a fixed-field comparison without full mod-two image. The remaining work is the same-object applicability and equality of actual stabilizers; the coarse moduli theorem alone is not an automatic field equality or rational descent isomorphism.
GAP: Determine the native F_mod for this auxiliary geometric curve and compare the subgroup fixing t with the kernel fixing all nonzero two-torsion, including the nonexceptional-automorphism check and both embedded field inclusions. No equality is proved in this literature turn.
REASON: Essential coverage is now inspected and the unchanged saved target is ready for a separate known-method specialization. No new general theorem or reproof is needed; the native definition is no longer an unread lead.
SCOPE: Only the same L073/L074/L076/L077/L078 auxiliary geometric curve, chosen cross-residue ordering, parameter t and fixed embedding; native F_mod and F_tpd comparison with Q(t). No mod-two surjectivity, degree-six assumption, changed field, transfer of independent initial data or original numerical comparison.

## Scope and discriminating test

The main gap remains the original finite B>=A assertion. The intermediate
target is exactly TARGET. Its plausible downstream use is to determine
whether L078's exactly generated auxiliary field meets the native
base-field prescription, while leaving the other initial-data conditions
and numerical comparison independent and unresolved.

Keep the same L073 E_aux/Q, L074 ordered roots, L076 cross-residue
choice and audited L077/L078 model E_L, t, s, G, H, N and embedding.
Use the inspected native definition before identifying its field of
moduli or a two-torsion field. The sources and relevant proof cases
are recorded in the source notes; the next application must handle
the action on ordered two-torsion and exceptional automorphisms.
Do not assume full mod-2 image, equality of a
j-field and a native field, or descent of the geometric isomorphism
over Q(t). The appropriate native definition and all required
source versions are recorded in the source notes before the later application.

The future mathematical test is equality of the two actual embedded
fields, or a precise obstruction under the original definitions.
A proven equality would permit further separate initial-data checks.
An actual mismatch would stop this proposed dictionary; missing source
coverage or an incomplete proof would leave it unresolved, not refute
IUT. This assessment approves the attempt, not either verdict.

Essential local inputs are L073 and audited L078, inheriting L074,
L076 and L077, together with the native definitions recorded in
foundations/05 step272. Native T/model, independent initial data,
retained memberships/scalar occurrence, marked all-image factorization,
pilot transport, essentiality and original finite B>=A remain open.
The retained E_0,F,K_glob,q_0 and the auxiliary q_aux are not identified.
Preserve ATTEMPTS/027,028,031,032,033 and the recorded source-version
qualifications. No blocked classification retrieval is required by
this comparison. Full matching and supporting Mathlib coverage for
the changed target remain unchecked, without an absence claim.

## Primary comparison, reuse and limitations

The [step308 source notes](../2026-10-18-auxiliary-two-torsion-field-source-notes.md)
give direct source links, exact inspected passages, queries, hypotheses,
proof cases and retrieval qualifications. IUT IV defines F_tpd by the
full two-torsion field of an F_mod-model, with descent independence
under its stated automorphism hypothesis. Antieau–Meier supply the
ordered-level coarse coordinate, uniqueness and permutation action;
their warning about the Legendre section's lack of S_3-equivariance
must be retained. Auer–Top's six-parameter paragraph is general-field;
its finite-field propositions are not imported over number fields.

For the punctured/pointed comparison the source notes additionally
record Milne (2021), I Proposition 4.18/Remark 4.19 p.38 and Theorem
6.3 p.42; their perfect-field, nonsingularity and geometric-irreducibility
hypotheses must be checked. Reuse the ready Milne pointed-coordinate and nonexceptional-j
automorphism coverage cited in L074 and the retained normalization
assessment. No general descent theorem is reproved. A future proof
must explicitly check the punctured/pointed moduli convention, the
same geometric curve and its actual ordered two-torsion. Neither
coarse-moduli language alone nor an abstract permutation group
establishes equality of embedded fields. The separate native
T/model specialization and a full initial-data certificate remain
distinct from the required field equality.

Step308 performs source review only: no lemmas, mathematical scripts,
new field equality or change to the main argument. This ready scope
replaces the step307 REVIEW_REQUIRED proposal for separate subsequent
mathematical use. No new continuation target is introduced.

## Step309 — direct-URL recovery

The supervisor required direct source URLs in the ready assessment.
They were previously present only in the linked source notes. The
SOURCE_EVIDENCE field now includes those URLs explicitly; the target,
SPECIALIZE decision and mathematical scope are unchanged. On 2026-10-18,
the IUT IV and Antieau–Meier URLs were reopened successfully. The native
definition and Proposition 1.8(ii),(iii), and the ordered-level parameter
statement, proof and equivariance warning were checked at the cited
passages. Other inspected coverage is reused from step308, with its
version qualifications preserved. This is a metadata repair, not new
source coverage or a mathematical advance. No field equality is proved.
