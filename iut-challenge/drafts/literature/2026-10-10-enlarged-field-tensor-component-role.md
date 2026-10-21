# Enlarged field as a decomposed tensor component — completed source review

TARGET: Assess whether L039's full-30-torsion obstruction also excludes L=Q_3(zeta_20,pi), pi^27=3, as a field component of the decomposed local tensor packets in Dupuy–Hilado arXiv:2004.13228v1.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched finite-separable tensor decomposition and exact/stronger component-embedding statements; inspected Stein's Lemma 18.2.1 and complete proof, and Stacks tags 00U3/00U2; checked the packet-field-role assessment, L039 and ATTEMPTS/022 and 025 for scope and duplicates. The changed component role was not previously covered.
SOURCE_EVIDENCE: Dupuy–Hilado arXiv:2004.13228v1 (28 April 2020), section 2.4.5 p. 7 and Definitions 3.6.1/3.6.3 pp. 11–13, https://arxiv.org/html/2004.13228v1 and https://arxiv.org/pdf/2004.13228v1; William Stein, Tensor Products, author-hosted HTML dated 2004-05-06, section 18.2 Lemma 18.2.1 and equation (18.1), https://www.williamstein.org/papers/ant/html/node76.html; Stacks Lemmas 10.143.4 (00U3) and 10.143.3(2,3) (00U2), https://stacks.math.columbia.edu/tag/00U3 and https://stacks.math.columbia.edu/tag/00U2; pairing/completion coverage reused from drafts/literature/2026-10-10-enlarged-field-full-torsion-critical-audit.md.
COMPARISON: The inspected algebra supplies field decomposition and injective factor-to-component maps; the specified finite packets have base Q_3 and finite characteristic-zero factors. Together with L039's audited factor torsion and L032's local exclusion, this covers the external inputs for a separate application, not a native-IUT or numerical conclusion.
GAP: Write and check the separate root-inheritance application for every nonzero CRT field component, including the finite multi-factor case and exact order under the component maps; no enlarged-field component exclusion is proved in this literature turn.
REASON: Essential component definitions and matching primary algebra are now inspected. The next matching target should be mathematical application using this coverage, without another source search or a decomposition/pairing reproof.
SCOPE: Exactly TARGET as the finite Q_3-algebra CRT component role in Definitions 3.6.1/3.6.3 and section 2.4.5. Excludes arbitrary additive summands, invariant subfields, algebraic-closure packets, native equivalence, replacement fields, action/radius calculations, global construction and original numerical comparison.

LITERATURE_REASON: The tensor-component role changes the hypotheses beyond the ready individual-factor assessments; its tensor base and component maps were essential unread inputs at invocation start.

## Completed inspection and comparison

The main gap remains original finite B>=A with actual input/action and
pilot transport. The intermediate target tests whether the same enlarged
field can occupy a CRT component role. Its downstream use is to decide
whether that proposed applicability bridge merits further work. This
review completes essential coverage, not that application.

**Primary role.** [Dupuy–Hilado v1](https://arxiv.org/html/2004.13228v1#S3.SS6)
Definition 3.6.1 takes the local tensor products over Q_p. At p=3,
write D_i for its selected completions (source notation K_underlined_v),
so a packet is D_0 tensor_(Q_3) ... tensor_(Q_3) D_r.
Definition 3.6.3 assembles these packets. Its reference to
[section 2.4.5](https://arxiv.org/html/2004.13228v1#S2.SS4)
specifies CRT field decomposition and normalization of the tensor
integer ring. The selected role is a field component of this finite
algebra, not a fixed subfield or an additive projection. The printed
PDF page references were checked. The separate algebraic-closure
variant and the forgetting of ring structure are outside this assessment.

**Matching theorem.** [William Stein, “Tensor Products”](https://www.williamstein.org/papers/ant/html/node76.html),
section 18.2, Lemma 18.2.1, assumes fields A,B over k and finite
separable B/k. It states that A tensor_k B decomposes into finitely
many fields, each containing isomorphic images of A and B. The complete
proof was read: a primitive element presents the tensor as A[X]/(f);
separability gives distinct irreducible factors over A; CRT gives the
components. Equation (18.1) identifies their evaluation maps. The proof
then checks the B-to-component map is unital and therefore injective;
the A inclusion is checked separately. This explicitly covers maps
into individual components, rather than just maps into the full tensor.
The page is dated 2004-05-06; no newer edition is silently substituted.

**Stronger algebra check.** [Stacks Lemma 10.143.4, tag 00U3](https://stacks.math.columbia.edu/tag/00U3)
characterizes etale algebras over a field as finite products of finite
separable fields; both proof directions were inspected.
[Lemma 10.143.3(2,3), tag 00U2](https://stacks.math.columbia.edu/tag/00U2)
records composition and base change of etale maps. Its statement and
proof's reference to the preceding smooth-map lemma were read; that
underlying smooth-map proof was not independently opened. These are
supporting references; Stein is the direct map-level input. Q_3 has
characteristic zero, and every D_i is finite over Q_3, so the required
finite-separable scope matches. No inseparable case, linear-disjointness
hypothesis or prescribed component embedding is needed by Stein's statement.

For the later application, use the cited two-factor theorem repeatedly
with finite-product tensor distribution, or check the unital maps from
each field into a CRT component directly. Write that finite-factor
applicability argument in the mathematical turn; it has not been proved
here. No new decomposition theorem is needed. The whole-tensor
projection has a kernel; this is distinct from the restriction to a
field factor, the exact case handled by Stein. Normalization of integer
rings is not a descent to an invariant subfield and is not needed for
this root test. Do not extrapolate to a different quotient construction.

## Reuse, failures and continuation test

Reuse the inspected Silverman III.8.1.1 coverage through the
[L039 audit assessment](2026-10-10-enlarged-field-full-torsion-critical-audit.md).
L039 supplies the primitive-third-root conclusion for each selected
completion; L031 supplies only L's exact field and value group, and
only L032's “Torsion and the genuine all-unit logarithm” paragraph is
needed for its no-third-root conclusion. These ranges were inspected;
no logarithm certificates or action proofs were loaded. Reproving the
pairing, local ramification theorem or CRT has no identified need.

The packet-field-role assessment and ATTEMPTS/022 and 025 stop only
individual-factor realization. They are preserved, and the proposed
component test remains a distinct application rather than a reopening.
No earlier matching component result was found in that narrow screen;
this says nothing about originality beyond the checked literature.
General web results included secondary tensor discussions, which were
not used as mathematical inputs. Dupuy–Hilado's numerical companion
section 3 and Eisenbud's cited exercises remain unread leads; Stein
already supplies the essential algebra, so they are not source blockers.
The Stein contents-page requests failed, but the full theorem/proof
page was accessible. Full matching/supporting Mathlib coverage is not checked.

Continue with exactly TARGET as a separate known-method application:
test order-three inheritance through the actual unital component maps
and then compare with the exact L031/L032 field. An order, role or map
mismatch requires narrowing or abandoning the proposed exclusion;
successful application stops only this finite-component realization.
Native definitions, actual input/action, global data, pilot transport,
essentiality and original finite B>=A remain open either way. No radius
calculation is an admissibility test. No lemma or mathematical script
was written, and no enlarged-field component exclusion is asserted.

This is ADVANCE in source coverage: a previously missing, precisely
cited map-level input is now available. It is KNOWN_IMPORTED literature
work, not progress beyond that source or a demonstrated IUT flaw.
Zero mathematical exploration turns are used; no counter reset is claimed.

Queries: `tensor product finite separable extensions field product canonical embeddings Stacks project`;
`Dupuy Hilado 2004.13228 tensor packets 3.6`;
`"tensor product" "fields" "each" "embeddings" "Stein" "18.2.1"`;
`"Dupuy" "Hilado" "tensor products" "decomposition"`.

## Original proposal retained (provisional source-status claims superseded)

The main gap remains finite B>=A with actual input/action and pilot
transport. The proposed intermediate target tests a different source
role, not the already excluded individual-factor realization. Its
downstream use is to decide whether reinterpreting the same auxiliary
field as a tensor component remains a possible applicability bridge.
No answer to that question is asserted in this proposal.

Next turn should first reuse the pairing and completion coverage and
L039's audited conclusion. Read the primary definitions of the local
tensor object and its decomposition, including their base fields and
the status of factor-to-component maps. Search exact/stronger known
finite-etale tensor decomposition and root-inheritance statements and
check their hypotheses against those objects. Do not assume that a
quotient, invariant subfield, component or individual completion means
the same thing. Import a matching theorem by precise citation if found;
do not derive and approve a new specialization in the literature turn.

Essential local inputs for any later application are L031's exact field
and value group, only L032's no-third-root paragraph, and L039's audited
full-torsion application. The tensor base and component maps are unresolved
source assumptions, not established inputs. L038's radius is motivation
only. No logarithm certificates need to be opened. Preserve ATTEMPTS/022–025
and all auxiliary results; the individual-factor route stays stopped.

Continue to a separately approved application only if the primary role
and known algebra give a precise root-inheritance test. If the role lacks
the needed structure, record that mismatch and narrow or abandon this
test; if an essential source remains inaccessible, park the dependent
target rather than repeat the individual-factor audit. Native input/action,
global realization, pilot transport, essentiality and original finite
B>=A remain open regardless. Mathlib coverage is not checked.

This is an unapproved continuation record, not a completed literature
review or a mathematical result. The next literature turn has a specific
reason: the changed tensor-component role lies outside all reused scopes.
