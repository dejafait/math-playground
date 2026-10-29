# Step 535 — covariant comparison source review

2026-10-28. Completed literature-only review. No replacement transfer
has been proved and no lemma or mathematical script is changed.

The main gap is rank/order equality for arbitrary E/Q. The bounded
intermediate target is source coverage for replacing L128 Step 1's
dual-action comparison by a covariant Betti--Tate relation test on the
original labeled ordinary tower. A successful later specialization
could restore the conditional completed-branch scalar diagnostic;
rationality, nonvanishing and second-factor finite local membership
remain independent gaps. Continue only with exact finite-level
operator comparison and original transition/control coverage; otherwise
record the first uncovered map and withhold the transfer.

Inspected local evidence: L128 hypotheses, Step 1 and step-534 audit;
L127 hypotheses/conclusion; ATTEMPTS/061 and /062; the step-532 source
record and step-527 degree-one-normalizer coverage. Reuse unchanged
Milne faithfulness, completion, local signs and global-separation
assessments. The inverse-label failure and bad-U obstruction remain.
No sibling notebook or supervisor state was read or changed.

## Newly inspected primary comparison inputs

**Covariant Betti--Tate comparison.** J. S. Milne, *Abelian Varieties*,
v2.0, 16 March 2008, [official notes](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I, Theorem 2.9 and preceding definition, printed p.14, and
Remark 10.7 with its torsion-lattice calculation, printed p.45
(PDF pages 20 and 51). The former identifies algebraic homomorphisms
with complex-linear maps preserving the period lattices; the latter
identifies T_l(A) with H_1(A(C),Z) tensor Z_l. Read also the definition
of T_l(alpha) immediately before Lemma 10.6, p.45: it applies alpha
to each torsion coordinate. Thus this is covariant functoriality for
homomorphisms, rather than the precomposition dual in L128 Step 1.
These passages cover complex abelian varieties and every prime l.
The finite-level Jacobians have characteristic-zero base and admit
an embedding into C; p is allowed even though the elliptic curve has
multiplicative reduction at p. This comparison is of the underlying
geometric modules and endomorphisms, not a Betti Galois representation.
No choice of a Tate twist supplies the rejected inverse-label equality.

**Curve versus Jacobian and correspondences.** Milne, *Jacobian
Varieties*, [official corrected article, 12 June 2021](https://www.jmilne.org/math/xnotes/JVs.pdf),
Theorem 2.5, pp.7--8, including the period-lattice construction and
Abel/Jacobi proof, and Proposition 6.1/Corollary 6.3, pp.19--20,
including their proofs, were inspected. They provide the analytic
Jacobian lattice and Albanese/correspondence functoriality. The
basepoint is chosen after base change to C; this does not assume a
rational point on the Shimura curve. The corresponding passage in
the 2008 notes is Chapter III, Theorem 2.5, p.93.

For an explicit push-pull comparison, read Emre Can Sertoz, Joel
Ouaknine and James Worrell, *Computing transcendence and linear
relations of 1-periods*, [arXiv:2505.20397v1, 26 May 2025](https://arxiv.org/html/2505.20397v1),
Sections 7.3, (7.3.29)--(7.3.36), and 7.4,
(7.4.37)--(7.4.43), with the justifications by divisorial norms,
Picard pullback and Poincare--Lefschetz duality. For morphisms of
smooth proper curves over Qbar, with the specified finite disjoint
marking/puncture sets, (7.3.31) identifies covariant Jacobian
pushforward with homological pushforward; (7.3.32)--(7.3.35) identify
divisorial pullback with homological transfer. The correspondence
f_{2,*} f_1^! of (7.4.40) acts on divisor classes as f_{2,*} f_1^*
and on homology as f_{2,*} f_1^! in (7.4.41)--(7.4.42).
These are inspected statements, not an inference from a search hit.

Read also (6.1.4)--(6.1.12) for the unmarked proper specialization,
and (4.5.54)--(4.5.55) for the homological transfer construction and
its integer-matrix statement/proof. Take all marking/puncture sets
empty for ordinary Jacobians. The finite Hecke legs meet the finite
nonconstant-map setting; this comparison does not require an etale
cover or removal of cusps. Apply to smooth proper components and
their correspondences, retaining the direct sum of components.
The mixed-Hodge assertions alone are not a claim about Z_p lattices:
the integral lattice comparison is supplied by Milne and the integral
pushforward/transfer constructions. Checking their precise application
to the original labeled Hecke action remains a next-turn obligation.

The author-hosted PDF was also inspected in Sections 7.3--7.4,
pp.35--36, at
https://people.mpi-sws.org/~joel/publications/1-periods25.pdf.
It has 54 pages, whereas the arXiv v1 listing has 68; the exact
numbered passages were checked in the versioned arXiv HTML rather
than identifying the two whole files. In particular, cite the arXiv
v1 numbering (4.5.54)--(4.5.55), not the author PDF's shifted
(4.5.55)--(4.5.56). The initial MPG repository URL failed to open;
its preview is not evidence. The accessible primary replacements
remove that access issue. No algorithm for periods is used here.

## Original operators and two different towers

Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
Section 2.1.2, Definitions 2.4/2.6/2.8, Proposition 2.9 and its
entire good-Hecke, diamond and p-U proof cases, Corollary 2.10,
Section 2.2.2/(21)--(23), and Section 2.4 through Corollary 2.23
were inspected selectively. Reuse steps 527/532 for unchanged
augmentation, local-sign and completed-ring inputs.

The source defines correspondences by right translation with their
explicit point formula, then declares covariant Jacobian actions.
The p-level coefficient transition is pi_1^*, and Proposition 2.9
specifies its intertwining with the same good T, tame U, diamond
and p-U labels. Its p-U proof uses the intermediate level and both
explicit sets of coset representatives. Corollary 2.10 gives the
original right Hecke module on the pullback direct limit; (21)
defines compatible ordinary idempotents; (23) defines its p-adic
completion. None states an enlarged algebra containing W.

For the detection side, Section 2.4 defines the trivial-finite-diamond
ordinary homology and its inverse limit under (pi_1)_*. Lemma 2.22
gives finite-level base change; Corollary 2.23 gives finite freeness.
The PDF, printed pp.17--18, was inspected for the control diagram
missing from the HTML. Its horizontal maps are (pi_1)_*, its vertical
maps are U_S, and its diagonal map is [K_m eta_{varpi_S} K_{m+1}].
It is a pushdown control diagram, not an identification of pushdown
with the coefficient pullback. Screenshot requests displayed no
visible page; the PDF text and stated theorem are the evidence.

The correspondence comparison above covers endomorphisms and the
finite transition maps. A later proof must use Fornea's control on
its stated inverse system and Proposition 2.9 on its stated direct
system separately. Neither source asserts that these limits are
equal, or that their transition maps become equal under one duality.
No such identification is licensed by this assessment.

## Scope, duplicates and bounded follow-on test

The decision is SPECIALIZE. The standard covariant comparison and
correspondence inputs are now precisely available. Their application
to an enlarged operator algebra on N_0 is not a quoted theorem.
This new coverage justifies one later known-method repair attempt,
not acceptance of that repair. No reproof of comparison, Hida control
or faithful Tate detection is needed. The unchanged latter input is
Milne, Chapter I, Theorem 10.15/Lemma 10.16, pp.49--50, already
assessed at step 532; its Z_p-linear injectivity must be used, not
only integral faithfulness of a single endomorphism.

The bounded test is the original labeled finite-level relation
transfer: compare covariant curve/Jacobian/Tate operators, then
check ordinary and finite-diamond summands, descent of a relation
from the controlled H to each H_m, its detection in End(J_m) tensor
Z_p, and its action on the original pullback direct limit and
completion N_0. The application must specify product order and
left/right module conventions without changing physical labels.
In particular, all tame U and p-U operators must be checked, not
just diamonds. W's original tower compatibility is the audited L127
input. No reversed-word transfer is imported from the failed proof.

Preserve N, P, M, original R_0/I, complete invariant domains and all
maps. A successful relation-transfer test would only remove the
step-534 action obstruction. Do not infer Steps 2--5, the completed
coefficient comparison, split/division signs, or L128 (2)/(3) from
it. Stop at the first failed label, summand, transition or continuity
check and retain the obstruction. ATTEMPTS/061/062 remain valid
evidence against their respective shortcuts; neither rules out
this changed covariant mechanism. No matching theorem for the full
scalar identity was identified, and no novelty or absence claim
follows. Mathlib coverage remains not checked.

Searches included: Milne Jacobian/Tate homology covariant endomorphism
comparison; Betti--Tate homology Hecke covariance; Jacobian homology
pullback transfer correspondence; and Plectic Heegner classes normalizer.
The period-paper lead was followed to its exact primary statements
and proof explanations. Other search hits (Conrad seminar notes,
DDT exposition, Berkeley notes, theses) were not essential inputs
and were not assessed from their previews. No additional central
rationality mechanism was source-assessed; this routine comparison
repair must not be routed as creative research.

Local result: new essential source coverage and a bounded repair
target, with no new mathematics beyond the cited inputs. L128 remains
on HOLD. PROOF, DAG, lemmas and mathematical scripts are unchanged.
Literature work neither spends nor resets mathematical exploration.
