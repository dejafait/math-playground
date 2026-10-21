# Six-charge direct-image polystability — completed source assessment

TARGET: Test whether R^1 p_2*F is slope-polystable at h for every L052 survivor with a=-10 and arbitrary integer b.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped local comparison found no completed preservation proof; external searches located the primary hyperkahler Fourier/Nahm transform theorem, whose hypotheses and essential proof passages were inspected below.
SOURCE_EVIDENCE: Bartocci--Bruzzo--Hernandez Ruiperez, A hyperkahler Fourier transform, Differential Geometry and its Applications 8 (1998), 239--249, Definition 2 and Theorem 3 with Lemmas 1--2, pp. 244--246; Bartocci--Jardim, arXiv:math/0312045v1, Theorems 2 and 3, pp. 4--5. Reused base-change and real-metric inputs are identified below.
COMPARISON: The known preservation theorem permits an arbitrary hermitian quaternionic-instanton product kernel and a trivial flat source line, subject to IT vanishing; it supplies a connection compatible with the actual holomorphic transform. L052 supplies the restriction framework, but the six-charge applicability argument remains unwritten.
GAP: Separately verify concentration on every fibre, obtain the locally free direct image, specialize preservation, and deduce polystability at the exact h. No six-charge character or discriminant test is approved here.
REASON: The changed slice required new essential connection coverage; the inspected theorem covers that framework, leaving explicit applicability rather than an original preservation theorem or reproof.
SCOPE: Exactly L044's S, h and full mixed tensor, rank-two locally free holomorphic F slope-polystable at p_1^*h+p_2^*h with c_1=0 and L048's character, a=-10 and integer b satisfying L052's survivor conditions, projected by p_2. Only concentration, local freeness and direct-image polystability are covered; no bundle existence, transform stability, equivalence, character obstruction or transport.

## Named gap, downstream use and bounded test

The immediate route gap is global compatible locally free polystable
realization of the mixed cubic tensor; universal primitive rational Hodge
algebraicity and transverse transport remain open. The five-charge line
identity is exhausted on its integer slice by L055. The proposed target
instead tests a connection or stability property of the six-charge higher
direct image. Such a property could allow necessary surface stability or
discriminant tests on larger charges, rather than repeating the failed
line identity. No six-charge specialization or larger-slice character
has been proved in this literature turn.

Continue only if inspected primary results cover this actual smooth
product projection and its locally free input, or a bounded independent
proof target can be given ready coverage. Abandon automatic direct-image
polystability if the hypotheses fail or a relevant counterexample rules
it out; do not impose equivalence, triviality of the family or stability
of the other factor to repair applicability silently. Park dependent
work if essential source access remains blocked.

Essential local inputs for review: L044 fixes S,h and the invariant mixed
tensor; L048 gives forced higher characters; L052 supplies factor
polystability, the stable/split tests and zero-slope lattice; L055 records
the exhausted five-charge line test. L053 provides individual bundles
only. All-fibre concentration, actual local freeness of this new direct
image and its connection/polystability must be justified in the changed
scope; none is assumed as a continuation premise.

## Inspected primary theorem and essential proof cases

Read Bartocci, Bruzzo and Hernandez Ruiperez, *A hyperkahler Fourier
transform*, **Differential Geometry and its Applications 8 (1998),
239--249**, [author-hosted published scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
Definition 2 (p. 244) specifies odd IT as vanishing of every even
cohomology group of E tensor P_y for every y. Theorem 3 (p. 246)
assumes a hermitian quaternionic instanton P on X x Y and a
quaternionic instanton E on compact hyperkahler X satisfying IT;
the sum of higher direct images is the holomorphic sheaf of a
quaternionic instanton on Y.

Read Sections 3.1--3.3, pp. 243--246, including Lemmas 1--2: the
proof uses the twistor fibre product, transfers IT, identifies the
holomorphic restrictions with the index bundle, and descends its
compatible connection. Section 4.1 (p. 246) relates surface instantons
to degree-zero polystable bundles. Import the theorem without reproof.

Read Bartocci and Jardim, *Hyperkahler Nahm transforms*,
[arXiv:math/0312045v1, 2 December 2003, pp. 3--5](https://arxiv.org/pdf/math/0312045v1#page=3).
Theorem 2 requires a hermitian kernel and an actual smooth index
bundle. Theorem-Definition 3 uses compact M,N and odd IT, identifies
the holomorphic higher direct images with the signed index, and
retains a hermitian connection. Its target printed as M is a typo:
the projection, preceding construction and Theorem 2 place it on N.
The following remark permits a reducible transform. Neither stability
nor a Fourier--Mukai equivalence follows. The published theorem is
the main input; this discussion corroborates its hermitian qualification.

## Reused coverage and bounded applicability obligations

Reuse the [factor-restriction assessment](2026-10-04-corrected-rank-two-factor-restrictions.md)
for Verbitsky, arXiv:math/0107182v10, Theorem 3.9 and Proposition 3.7 /
Lemma 3.8, pp. 12--14, and Huybrechts, *Lectures on K3 Surfaces*,
author-hosted draft, Chapter 9, Section 3.1 and Theorem 4.9,
PDF pp. 175--176 and 182. Their invariant-curvature and real-class
Hermite--Einstein inputs remain in scope. L052's coefficient-independent
argument supplies the product connection and every factor's
polystability; its proof explicitly treats c_2=6 as requiring stability.
Its stable cohomology argument is equation (4). No existence of F
or general restriction-stability statement is added by this review.

Reuse the [five-charge assessment](2026-10-05-five-charge-relative-direct-image-slice.md)
for [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [Lemma 36.31.3, 0BDH](https://stacks.math.columbia.edu/tag/0BDH).
Their proper perfect base-change and single-degree local-freeness
hypotheses concern this same smooth projective projection independently
of the coefficients. The new fibre dimensions must be verified.
L055's exhausted line-character test supplies no preservation input.

The separate research turn must do precisely this specialization:

1. Check L052's survivor hypotheses and use its stable c_2=6 case
   on every p_2-fibre. Verify even-degree vanishings and constant
   remaining dimension at all fibres before using base change.
2. Take X=Y=S, the actual F with L052's unitary hyperholomorphic
   connection as kernel P, and O_S with its flat connection as E.
   Check the fixed holomorphic structure and simultaneous product
   metric. No moduli interpretation or irreducibility of E is required.
3. Identify actual R^1 p_2*F with the holomorphic transform, retaining
   the alternating index sign. Import preservation and deduce
   polystability at the same real h. Retain reducible transforms.

These are applicability obligations, not a completed proof of the
saved assertion. No larger-slice character has been evaluated or
additional target approved. L053 supplies individual factors only;
it cannot supply the kernel in item 2. Failure of IT or of the actual
holomorphic identification abandons this application. Adequate
coverage now makes a separate mathematical test justified.

## Searches, access and decision

Bounded queries included:

- hyperkahler Nahm transform quaternionic instanton higher direct image Bartocci Bruzzo Hernandez Ruiperez theorem
- hyperholomorphic bundles higher direct images polystable Verbitsky direct image
- Bartocci Bruzzo Hernandez Ruiperez hyperkahler Fourier Mukai transform 1994 theorem
- hyperkahler direct images quaternionic Bartocci Bruzzo
- A hyperkahler Fourier transform pdf theorem

Also read [Bartocci--Bruzzo--Hernandez Ruiperez, arXiv:dg-ga/9407004v1,
Theorem 1 and proof sketch, pp. 1--3](https://arxiv.org/pdf/dg-ga/9407004v1#page=2)
as an earlier surface formulation. The 1998 theorem suffices, so
special invertibility results were not pursued. Verbitsky's
*Positive forms on hyperkahler manifolds* and broader moduli-transform
results remain unread search leads, not theorem inputs.

The initial author-hosted fetch timed out and shell curl failed DNS;
the web tool subsequently retrieved the published scan through its
HTTP URL. Essential access is resolved; no local PDF download is
claimed. No counterexample to this narrow application was identified
in the inspected sources. Failed searches do not establish novelty.

This LITERATURE step imports known source coverage and makes the
unchanged target ready for a separate SPECIALIZE application, classified
as REPRODUCTION. It establishes no new six-charge mathematical result.
The supervisor separately approves the changed assessment before
invoking research. Mathlib coverage of the full preservation statement
is not checked; no matching theorem or absence is asserted.
