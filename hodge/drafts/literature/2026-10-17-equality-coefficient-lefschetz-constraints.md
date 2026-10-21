# Equality coefficient Lefschetz constraints — source assessment

TARGET: Test whether hyperholomorphic Lefschetz operators on H^*(X,End_0(F)) impose a restriction beyond L116's surviving cohomology data.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted coefficient-Lefschetz/sl2/Ext searches located Verbitsky 4.2/4.2.A and Beckmann 8.5; exact-term local duplicate search found only this proposal, with ATTEMPTS/047/063/066/068 and the saved normal-curvature assessment checked for overlap.
SOURCE_EVIDENCE: Read Verbitsky alg-geom/9307008v1 (29 July 1993), Definition 1.1 and section 3 real structure, PDF pp. 2,11; section 4 setup, Propositions 4.1--4.3, Theorem 4.1, Corollary 4.3 and Theorems 4.2/4.2.A with essential proofs, PDF pp. 12--17; Beckmann author-hosted Atomic.pdf, section 8.3, Theorem 8.5 and trace splitting, printed p. 40 (PDF p. 40), inspected 2026-10-17.
COMPARISON: The known coefficient theorem applies to the product and trace-free summand and supplies an actual scalar-symplectic cup isomorphism H^1(X,V) -> H^3(X,V); L116's dimension equality does not evaluate this map. No additional dimension exclusion is established, and independent factorwise Lefschetz or LLV actions are not supplied.
GAP: Evaluate that actual cup map through L116's specific truncation/retraction, keeping both scalar factor-form contributions and any derived terms; determine whether its required invertibility gives a condition beyond the saved dimensions and alternating form.
REASON: Approve one separate bounded RESEARCH specialization of the known operator theorem, classified REPRODUCTION; stop if the actual cup isomorphism is automatic from retained inputs or its undetermined entries merely restate invertibility. No representation calculation or new constraint is made in this literature turn.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked the coefficient operator theorem and its product/trace-free proof scope; the ready connection-criterion assessment did not cover these essential inputs.
SCOPE: Hypothetical equality F of L071/L108/L116 on X=S_1 x B with the original common product metric, full negative tensor, locally free End_0(F), and finite possibly empty Z; no independent factorwise rotation invariance, strict normal stability, acyclicity, kernel existence or transport.

## Relevance and precise threshold

The main unresolved problem is universal primitive rational Hodge-class
realization. This proposed intermediate test asks for a necessary
cohomology restriction on the same hypothetical equality kernel.
A restriction beyond the existing constraints could remove some remaining
kernel possibilities. Other representatives, actual existence,
reconstruction and transverse transport remain separate gaps.

Essential inputs are L116 with L108/L109/L111/L115 and their retained
ancestors, including L071's actual compatible connection. Retain
s=|Z| in {0,...,796} union {800}, the actual unknown t=h^0(N),
0<=t<=48, t!=47, t=48 only at s=800, and
h^*(X,End_0(F))=(0,t,724+2t,t,0), with
h^1(N)=704-s+2t>=0. L108's perfect alternating normal form is also
retained; a parity constraint already implied by that form is not a
new exclusion. These are inputs from L116, not calculations made in
this proposal. Formal compatibility remains distinct from existence.

The source threshold is met for one actual-map test, not for a new
dimension calculation. The standard theorem prescribes a particular
invertible scalar cup map. Its matrix under the actual Leray splitting
has not been calculated here or in L116. The next attempt may evaluate
this map and compare it with that theorem. Continue only with an
additional checkable constraint; if its invertibility is automatic,
or evaluating it requires new uncontrolled family data, park the test.
Do not infer a violated condition from dimensions or choose arbitrary
matrices in place of the actual cup action. Other representatives,
kernel existence and transverse transport remain unresolved.

## Primary theorem, proof scope and qualifications

The controlling source is M. Verbitsky, *Hyperholomorphic bundles*,
[arXiv:alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993. ArXiv lists only this version. The later publication is
*Hyperholomorphic bundles over a hyper-Kähler manifold*, J. Algebraic
Geom. **5** (1996), 633--669; its published text was not inspected, so
the theorem numbers and PDF pages here refer specifically to v1.

For a compact hyperkahler manifold of complex dimension 2n and a
hyperholomorphic coefficient bundle E, Theorems 4.2/4.2.A, PDF pp.
16--17, give the symplectic Lefschetz action on coherent H^*(X,E).
In Dolbeault notation let x be the class of the conjugate of the
metric holomorphic symplectic form. The precise isomorphism used is

\[
 x^{n-i}\cup -: H^i(X,E)\longrightarrow H^{2n-i}(X,E),
 \qquad 0\le i\le n.
\]

This is a cited standard input, not a proposed new lemma or a
reproof. Its proof uses coefficient Kahler identities, equality of
the rotated Laplacians (Theorem 4.1), and pointwise symplectic
raising/lowering operators; 4.2.A treats coefficients without a
parallel real structure by E plus its dual. The proof cases and
the real-coefficient argument preceding them have been inspected.

Two v1 qualifications must be retained. The printed one-step
injection assertion in 4.2.A includes i=n; do not import that
endpoint. The isomorphism clause above and 4.2's harmonic sl2
action are the inputs. Also the discussion before 4.2.A displays
H^*(O_X) as a single truncated polynomial ring, which is not the
whole scalar cohomology of a K3 product. Only the subalgebra
generated by x is relevant here. Neither scalar-ring equality nor
a one-dimensional H^2(O_X) occurs in 4.2's operator proof. No
injection H^2(X,V) -> H^4(X,V) is authorized.

Definition 1.1, PDF p. 2, permits compact products. The proof uses
their diagonal triple I,J,K and needs no irreducibility assumption.
With L071's actual unitary connection, the induced connection on
End(F) is hyperholomorphic; the scalar and trace-free projections
are parallel. The real structure described in section 3, PDF p. 11,
is negative Hermitian adjoint and preserves trace zero. Thus the
coefficient hypotheses hold for V=End_0(F), without requiring V
to be stable or its connection to be flat. The scalar wedge and
adjoint contraction operators preserve this parallel summand.

The source works with (p,0) connection forms and its parallel
antilinear real structure to identify holomorphic cohomology.
Passing to the usual (0,p) Dolbeault convention conjugates the
symplectic form. Fix x from the original metric triple; a nonzero
overall normalization does not change the cited isomorphism.
On the product that form is the sum of the two pulled-back metric
forms. The theorem concerns their sum; separate scalar cup maps
exist, but it supplies no separate harmonic sl2 action for them.
It supplies no full coefficient LLV algebra, arbitrary independent
factor rotations, or twisted de Rham complex for the nonflat
coefficient connection.

As a modern cross-check, T. Beckmann, *Atomic objects on hyper-Kähler
manifolds*, [author-hosted text](https://www.math.uni-bonn.de/people/beckmann/Files/Atomic.pdf),
section 8.3, Theorem 8.5, printed/PDF p. 40 in the inspected 46-page
copy, states the Ext isomorphism version and the trace splitting,
referring to Verbitsky 4.2A. This is a restatement of the same input,
not a stronger operator theorem. Atomicity is not assumed here;
the atomic-object consequences in that paper are not imported.
The product applicability above comes from the original operator
proof, not from transferring irreducible-hyperkahler conventions.

## Exact bounded continuation

For complex dimension four, the imported map to compare with the
saved actual data is x cup - from H^1(X,V) to H^3(X,V). Its abstract
dimension equality is already in L116. The endpoint isomorphism
H^0 -> H^4 also agrees with L116's zero endpoints. Corollary 4.3's
quaternionic structure in degree one is not a license to claim a
new parity obstruction while ignoring L108's alternating normal
form. No decomposition or additional dimension restriction is
computed in this review.

The next mathematical attempt should use L116's actual derived
inclusion, trace retraction and global cohomology identifications,
with L108/L109/L111/L115 retained. Compare the sum of the two
scalar-form cup actions with the imported isomorphism. Do not
assume either contribution vanishes merely from its action on a
Leray associated graded object, or assume that a chosen additive
splitting is multiplicative. Any actual derived correction must
be retained or proved absent. If the resulting condition leaves
uncontrolled cup entries, record that exact obstacle and stop;
do not create a formal matrix assignment as a bundle realization.

## Comparison with recorded failures

ATTEMPTS/068 stops repeated global transgression and section/Euler
calculations. This proposal changes the mathematical input to a possible
coefficient Lefschetz action; it cannot claim progress by recovering
h^1=h^3 or reevaluating the same Euler number. ATTEMPTS/047 forbids
assigning normal sections or acyclicity without proof. ATTEMPTS/063/066
retain their precise metric/singularity scope; no shortcut through a
singular metric is part of this proposal.

The [stable normal-curvature assessment](2026-10-14-equality-stable-normal-curvature-test.md)
requires independently controlled bracket/Green pairings that remain
unavailable. No such new estimate was obtained, so that route stays
parked. This operator test does not request those pointwise inputs.
Its exact source coverage and informativeness are nevertheless unresolved;
this is not an approved mathematical continuation or a novelty claim.

This review imports a known operator theorem with the applicability
and source qualifications above. It establishes no new lemma,
evaluated cup map, cardinality exclusion, bundle existence or
progress beyond the checked sources. Full matching Mathlib coverage
is not checked. Search failure is not evidence of novelty.

Searches used included `Verbitsky hyperholomorphic bundles Lefschetz
sl2 cohomology coefficients Theorem 4.1`, `hyperholomorphic bundles
cohomology so(5) Lefschetz H^i B holomorphic symplectic`, and
`Atomic objects Theorem 8.5 hyperholomorphic Lefschetz`; title and
theorem follow-ups led to the primary texts above. Scalar LLV and
semipositive-line Hard Lefschetz search leads were not used as
coefficient theorems. Existing connection-criterion coverage was
reused rather than reassessed.
