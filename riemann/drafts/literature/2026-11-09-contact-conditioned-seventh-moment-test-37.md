# One fixed-panel contact-conditioned seventh-moment test

TARGET: Test whether L917's complete first-panel moment enclosures, common normalization, strict H1 bounds, all H2 null rows and degree-seven raw Stieltjes PSD conditions force L874's d=2 flux to be nonpositive or the feasible class to be empty, or admit one certified violating tuple.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact/stronger-result searches and local duplicate/failure comparison completed in 2026-11-09-contact-conditioned-seventh-moment-scope-36.md, step37; no exact matching sign theorem or duplicate test was inspected and no novelty is asserted.
SOURCE_EVIDENCE: The completed step37 assessment records Curto-Fialkow1991 Theorem5.1 p625 and singular proof cases https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf ; Laurent updated2010 Lemma4.2 pp54-55/Theorem3.15 p36 https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf ; Gallier2019 Proposition4.2/Theorem4.3 pp9-12 https://www.cis.upenn.edu/~jean/schur-comp.pdf . Reuse these inspected necessary-moment, singular-block and exact certificate tools without reproof.
COMPARISON: The finite class deliberately retains necessary raw PSD rather than a representing-measure converse; the odd Stieltjes theorem also requires a raw range condition. L921's different J test lacks these actual bounds; L923's Gaussian has S2=0; L922's determinant enclosure is inconclusive. None decides this S7 implication.
GAP: Establish Phi<=0 on exactly this class, prove it empty, or certify one Phi>0 member. No such result is established; actual realization, extra tilt relations, initialization/tangency, other panels/degrees and global continuation remain unresolved.
REASON: This is a bounded direct test of the unpaid boundary coefficient using available quantitative actual-law information, with essential source coverage complete and no automatic sign imported. Newly saved continuation requires separate next-turn approval before mathematics.
SCOPE: One fixed finite class and one coherent mathematical attempt only; no new quadrature, panel refinement, moment data, coefficient-family sweep, source retry or modification of earlier stops. The coverage decision authorizes no calculation during its literature-only creation turn.

The main gap is L030--L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is one full-degree d=2 contact flux. A universal
nonpositive sign could support local continuation only after actual-law
inclusion and with equality/tangency still unpaid; emptiness would
exclude those contacts on this one panel. A violating relaxed tuple
would stop this sufficient finite-data mechanism, with no actual-theta
or RH counterexample implied.

## Exact finite class

Use only `scripts/heat/low-time-h2-uniform-195.json`, panel0, whose
closed parameter panel is [0,1/5120]. For j=0,...,6, let m_j be in
the complete saved interval at `/panels/0/moments/2j` for M_(2j),
where 2j denotes the decimal-string key (0,2,4,6,8,10,12). Interpret
every saved endpoint string as its exact rational value. Inspect the
complete selected evidence with the shared JSON inspector; do not use
a preview or a rounded shortened endpoint in a certificate.

Require m0>0; put y0=1 and y_j=m_j/m0 for j=1,...,6 using this same
m0 throughout. Introduce just one further real moment y7. No y8,
additional tail bound or theta evaluator is permitted. The common
denominator is part of the class; independently rescaled quotient
boxes are not substitutes. L917's full saved intervals include both
theta and spatial tails. Its strict bounds below retain precisely its
directed-arithmetic contract; no new audit or regeneration is required.

In the finite ring R[t]/(t^8), use the existing local convention

    g(t)=sum_(j=0)^7 (-1)^j y_j t^j/(2j)!,
    log g(t)=-sum_(j=1)^7 S_j t^j/j.

Impose simultaneously:

- M3=(y_(i+j))_(0<=i,j<=3) PSD;
- N3=(y_(i+j+1))_(0<=i,j<=3) PSD;
- H2=(S_(i+j+2))_(0<=i,j<=2) PSD;
- real c=(c0,c1,c2), c0^2+c1^2+c2^2=1, c2!=0;
- all three rows of H2*c=0;
- S2>3.714*10^(-5);
- 9.7*10^(-16)<S2*S4-S3^2<7.026*10^(-15).

c0,c1 may vanish and c2 has no assumed uniform separation from zero.
No raw-block invertibility, representing measure, strict full support,
actual-contact existence or tilt relation beyond these data is assumed.
Keep singular raw PSD cases. If a Schur reduction is used, cite the
inspected singular theorem and justify all range/division hypotheses;
otherwise retain unreduced PSD conditions. Do not add a representing-
measure range condition just to exclude an inconvenient witness.

## Output and certificate standard

Use exactly L874(2) with d=r=2, N=6 and

    b_n=sum_(i+j=n-2) c_i c_j, 0<=i,j<=2,
    B=-2 sum_(n=2)^5 n(2n+1)b_n S_(n+1)
       +4 sum_(n=2)^6 n b_n sum_(a=2)^(n-1) S_a S_(n+1-a),
    Phi=-156c2^2 S7+B.

L923's existing all-row finite S7/contact algebra is optional reusable
bookkeeping. Its actual-measure norm inverse and density comparison
must not be assumed for arbitrary members of this class. Any further
elimination or bound belongs to the approved mathematical attempt,
not to the source assessment that created this target.

The bounded discriminator is either an exact proof of Phi<=0 for
every member, a rigorous infeasibility certificate, or one exact or
rigorously enclosed tuple with Phi>0 meeting every listed condition.
For a witness, certify common-mass membership, coefficient identities,
all PSD conditions, unit/nonzero conditions, all three exact null rows,
both strict H1 bounds and the strict flux sign. Approximate zero
residuals or a floating optimizer do not certify equality or PSD.
An algebraic witness may normalize c exactly; all signs still need
proof. An interval witness needs certified existence satisfying the
equalities, not merely intervals containing their residual zero.

For a universal proof retain every box face, strict inequality and
singular case. The standard all-principal-minors criterion may check
PSD; leading minors alone are insufficient in the semidefinite case.
An exact polynomial certificate may use the inspected feasibility
alternative, with positive denominators cleared legitimately and
every identity coefficient and multiplier sign verified. No compact-
strict-positivity theorem, solver success or relaxation convergence is
itself the desired nonstrict flux proof. An unbounded y7 or c2!=0
must not be replaced by an unproved compact cutoff.

If no discriminator is certified in this one attempt, save the first
unresolved comparison and stop. Do not widen the boxes, drop a null
row, change the panel, add a moment, rerun quadrature or launch a sweep.
If scripts are needed after approval, save complete certificates under
`scripts/heat/`, print only results/thresholds/failures/paths, and
inspect complete load-bearing evidence with the shared JSON inspector.

## Inputs, qualifications and proposed routing

L019/L058 supply actual-law inclusion and finite moments; L874 supplies
the exact local flux. L917 supplies the complete intervals and strict
bounds, conditional on L037's arithmetic contracts. L923 supplies only
its already proved finite S7 interface if used. L921/L922 are contrasts,
not inputs to a sign proof. No cross-notebook input; full matching
Mathlib coverage is unchecked. Standard theorem reproof is unnecessary.

Proposed purpose: proof_attempt/creative, deep_research/max, after the
separate gate approval. The precise obstruction is the external S7
coefficient in L874, unpaid by generic raw PSD or the stopped norm
floor. The new mechanism tests it jointly against strict actual lower-
moment data and all contact rows, with the single certificate/witness
test above. This is not a new general Schur theorem or a routine
application purporting to import the sign. A successful relaxed sign
or negative witness still leaves the independent main-goal gaps listed
above. No approved mathematical attempt or new lemma exists yet.
