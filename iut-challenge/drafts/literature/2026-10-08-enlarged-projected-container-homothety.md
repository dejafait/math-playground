# Enlarged projected-container homothety — completed coverage

TARGET: Determine whether there exists a primitive rank-one F in M such that the images of C=O_L intersect V and M=J_L intersect V in V/(Q_3 F) are scalar-homothetic.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Seven bounded normal-form, quotient-homothety and invariant-factor/interlacing queries found general primary tools but no inspected theorem deciding this exact pair; relevant assessments, histories and ATTEMPTS/022–024 contain no completed test. Queries and qualifications: drafts/2026-10-08-enlarged-projected-container-source-review.md.
SOURCE_EVIDENCE: Read Voight, Quaternion Algebras (2021), chapter 9 section 9.3 and Theorem 9.3.9, https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9; Bürgisser–Kulkarni–Lerario, Selecta Mathematica 32:10 (2026), version of record 5 January 2026, sections 2.1–2.2, Lemmas 3.1.4(1–3)/3.1.5, pp. 21–23 and Propositions 4.1.1/4.1.2 with complete proofs, pp. 35–36, https://doi.org/10.1007/s00029-025-01120-y and https://d-nb.info/1395945926/34; Sá (1980), On the diagonals of integral matrices, pp. 207–208, criterion (3)–(4), https://dml.cz/bitstream/handle/10338.dmlcz/101672/CzechMathJ_30-1980-2_4.pdf. Reuse Sehanobish/Stacks only for downstream stable-lattice work, with prior qualifications.
COMPARISON: Known simultaneous normal form, intersection/quotient lattices and quotient-only Smith-factor interlacing cover the method over Q_3 and Z_3 without nesting or O_U-linearity; they do not decide the exact rank-107 C,M pair or construct its common line. L031/L032 provide genuine local data; L033 is downstream motivation only.
GAP: Apply the cited quotient-only interlacing to the exact trace-kernel lattices and test all primitive lines/scalars; a surviving necessary test still requires an exact projected equality or a further exclusion argument. No factors, line or verdict are computed here.
REASON: Essential changed-target source coverage is now adequate for one separate bounded known-method specialization; import normal-form and interlacing inputs rather than reprove them, and retain common-line sufficiency and original-IUT limitations.
LITERATURE_REASON: The ready residual-action assessment excluded projected-container comparison; the essential quotient-only interlacing statement and its proof were previously unread for this target.
SCOPE: Same L=Q_3(zeta_20,pi), pi^27=3, J_L=log(O_L^times), V=ker(Tr_(L/Q_3)), M=J_L intersect V and C=O_L intersect V. F ranges over primitive rank-one Z_3-submodules of M, and q_F is the rational quotient V -> V/(Q_3 F). No field norm on the quotient is assumed.

Proposed inputs: audited L031 and L032 for the two genuine lattices;
audited L033 motivates the later reference-action use only. Scalar
homothety means equality q_F(C)=a q_F(M) for some a in Q_3^times,
inside the same rational quotient. It is not an abstract module
isomorphism. Primitivity means M/F has no Z_3-torsion. The actual
presentation line Z_3 y_1 is among the permitted lines, but arbitrary
primitive lines are not asserted to arise from source presentations.

A negative existence result could support a later projected-container
noninvariance test using L033 and a correctly specialized stable-lattice
criterion. A positive result would stop that presentation-independent
shortcut and require further information about the actual fixed line;
it would not prove a source container invariant. This is the explicit
continuation/abandonment test. Neither result supplies an actual input
point or the original normalized inequality. No theorem is derived here.

C is used without a numerical radius prescription. Scalar rescaling
and any subsequent numerical enclosure application need their exact
hypotheses stated in future work. This review must not assume
O_U-linearity, prescribe y_1 in the field basis, add the x_2 shear,
change the group or insert exponent twists. ATTEMPTS/024's whole-kernel
stop and ATTEMPTS/023 and 022 remain preserved. Fixed-line control,
actual/native actions and inputs, packet/global realization, pilot
transport, essentiality and finite B>=A remain independent gaps.
Full matching Mathlib coverage is not checked.

## Completed comparison, 2026-10-08

The [source review](../2026-10-08-enlarged-projected-container-source-review.md)
records primary theorem hypotheses, relevant proof cases, queries,
duplicate checks and unread leads. Approve exactly TARGET for a later
research invocation. No mathematical specialization is performed here.
The next attempt may use L031's full saved basis, compute the genuine
trace intersections and relative Smith factors, and apply Proposition
4.1.2 with identity from (V,C) to (V,M), target line Q_3 F and quotient
lattice q_F(M). Its scalar field is Q_3; field valuation on L does not
descend. Preserve all primitive lines and scalars. A failed necessary
interlacing test can exclude existence; a passing test cannot establish
existence without full same-space projected equality. No new general
line criterion is supplied by this assessment.

Voight supplies simultaneous lattice factors; Bürgisser–Kulkarni–Lerario
supplies the subspace and quotient tools and the quotient-only inequality.
No reproof of those standard statements is needed. The necessary
field-specific specialization is not a claim of mathematical originality.
Their simultaneous-row-and-column Corollary 4.1.3 is not imported;
Sá's general submatrix statement is a comparison, not an essential
premise, and its earlier references remain unread. Existing stable-lattice
coverage is reused only for eventual action on the actual fixed-line
quotient, with compactness/full-lattice hypotheses and same-space
homothety qualifications retained.

The earlier proposed test and independent unresolved assumptions above
remain unchanged. Complete outcome: EXPLORATION, LITERATURE,
NOVELTY_UNCHECKED. This establishes source readiness, no lattice verdict
or new lemma. Matching and supporting Mathlib coverage remain not checked.
No lemmas, mathematical scripts, DAG or PROOF were modified. The newly
completed coverage receives the supervisor's separate approval before
research; its target remains the exact saved Next action.
