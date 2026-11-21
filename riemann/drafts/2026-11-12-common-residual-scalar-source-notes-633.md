# Scalar obstruction: source comparison633

Literature-only work for the exact TARGET in assessment632. Main gap:
L030-L032/C032a actual-Xi positivity. Intermediate question: whether a
single exactly feasible box point can support a scalar obstruction to the
fixed C999w sufficient certificate. Downstream use is screening that
certificate before allocating C999x's enormous PSD blocks. A nonphysical
point cannot certify negative actual energy, S3 failure or an RH disproof.

## Searches and actual local reads

Web queries on12November2026:

- `semidefinite programming exact rational infeasibility certificate weak infeasibility rational solutions Klep Schweighofer`
- `linear programming rational polyhedron rational feasible point exact certificate Farkas theorem verification`

Read C999w's hypotheses and construction/equalities/certificate
Sections1-5, limits Section6 and relevant audit cases in Section7;
C999x's core/high support and equality support, Sections1-2 and
the corresponding audit Section6. Reused completed625/599/601 scope,
read their relevant source notes and the complete598/600/603 stop records.
Scoped text searches in those common-residual assessments/histories/notes
for box points, exact equality compatibility, fresh errors, Farkas and
infeasibility found no completed matching witness. This is not a claim
of novelty or a search across unrelated notebook routes.

Read600's sign/limitations passage and the input-loading lines of its
existing exact replay script: its fixed vector is
`partial_lower_direction_direction` in
`scripts/separation-seven/joint-entrywise-600.npz`. The vector can be a
later direction proposal; its negative lower-matrix value supplies no
value of C999w(9). No array was loaded and no script executed633.

## Primary comparison

1. H. J. van Waarde, M. K. Camlibel and M. Mesbahi, *From Noisy Data to
   Feedback Controllers: Nonconservative Design via a Matrix S-Lemma*,
   IEEE TAC67(1)(2022),162-175, DOI10.1109/TAC.2020.3047577,
   [version of record](https://pure.rug.nl/ws/portalfiles/portal/206606333/From_Noisy_Data_to_Feedback_Controllers_Nonconservative_Design_via_a_Matrix_S_Lemma.pdf).
   Reused625's complete Theorems9/11 assessment; rechecked Theorem9 and
   its proof p166. Its sufficient congruence direction is the existing
   input. Converse scope remains one full matrix variable, one QMI and
   strict feasibility; Theorem11 also requires boundedness. These do not
   establish necessity for the notebook's structured multi-constraint box.

2. I. Klep and M. Schweighofer, *An Exact Duality Theory for Semidefinite
   Programming Based on Sums of Squares*, Mathematics of Operations
   Research38(3)(2013),569-590, DOI10.1287/moor.1120.0584,
   [author version dated10November2012](https://www.math.uni-konstanz.de/~schweigh/publications/sosdualsdp.pdf).
   Inspected Section3.1 definitions and Lemma3.1.1 with its full proof,
   printed pp4-5. For a real symmetric linear pencil, constant PSD
   separation certifies strong infeasibility; it is not a complete
   certificate for weak infeasibility. The proof separates the affine
   pencil image from the PSD cone and checks the converse by its trace
   functional. Read Corollary4.3.1 statement p17: nonlinear quadratic-module
   certificates cover general infeasibility. Its supporting proof chain
   was not inspected and is not imported. This stronger lead supplies
   no scalar point or practical algorithm for our instance. No strong
   infeasibility of C999w is asserted.

3. K. Fischer, B. Gärtner, S. Schönherr and F. Wessendorp,
   [CGAL6.2.1 Linear and Quadratic Programming Solver manual](https://doc.cgal.org/latest/QP_solver/index.html),
   accessed12November2026: read Which Programs can be Solved,
   Efficiency, Robustness, and the Farkas statement/verification discussion
   in Solution Certificates. Linear objectives permit affine equalities
   and box bounds; exact arithmetic supports checkable rational results.
   The stated alternative for Ax<=b,x>=0 uses y>=0, y^tA>=0,
   y^tb<0. The dense interface has serious dimension costs, so this is
   verification scope, not a practical recommendation for millions of
   constraints. A negative indefinite quadratic objective is outside
   the documented convex-QP guarantee. No solver is installed or invoked.

Search leads not inspected as theorem inputs: the Kolmogorov--Naldi--Zapata
degenerate-SDP certification paper, Schrijver's rational-polyhedron
results, and general polynomial-optimization exactness results. They are
not needed for the fixed direct-assignment attempt. No theorem is reproved.

## Decision and bounded continuation

SPECIALIZE: existing C999w Section5 supplies the sufficient implication;
the cited sources do not supply its local point, value or feasibility.
Do not replace the point requirement by a solver status, a negative
sufficient lower matrix, approximate equalities or a presumed complete
SDP dual alternative. No assertion about rational feasible SDP multipliers
is needed for a direct box-point test.

The unresolved practical prerequisite is an exact core point. Nominate
one deterministic center-repair attempt in assessment633: freeze every
symbol at zero except the fresh JY errors and head Delta errors, and
try to solve precisely the already retained affine equalities with those
coordinates. All high-row symbols stay zero. This defines a future test,
not a construction established here. The proposed repairs may be
inconsistent, violate unit bounds, or prove impracticable. Zero radii
must be checked as exact consistency conditions. No general rational
polytope existence or tractability inference substitutes for evidence.

Continue that particular point route only if it yields a complete exact
box/equality certificate or a fully specified source-covered construction
whose hypotheses are actually verified. A bound failure or missing exact
input parks this center prescription without tuning or a global
infeasibility claim. Even success leaves scalar negativity unresolved;
a later full scalar test needs fixed direction and all outputs of(9),
including signed energy, head, every residual row and the entire-tail
majorant. It must use C999w's existing implication with unrestricted
Gamma and PSD Lambda, not sparsify multipliers to manufacture an
obstruction. No point or scalar sign has been computed633.

The prescription is newly written, so assessment633 requires a separate
approval turn. Ready coverage is to be reused at that approval; no generic
discovery repeat is requested. No central creative mechanism is justified
by these sources: actual remote-plus-induced signed coupling remains
uncontrolled. No mathematical exploration counter is spent or reset.

Essential inputs remain C999w Sections1-7 and audited C999x Sections1-6;
C744v/w/z, C999k/q enter via their unchanged hypotheses.600 inclusion/pins,
analytic/IEEE754/Decimal/core/c_* contracts remain conditional. Preserve
598/600 stops and unfinished603. Higher endpoints, C744q, H2, non-neutral
coverage and global assembly remain open. Full matching Mathlib coverage
is unchecked; no cross-notebook input. Lemmas, scripts, DAG and PROOF
are unchanged because this review establishes no new mathematical input.
