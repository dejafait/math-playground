# Exact projection weighting — step447 audit record

Invocation-start target and SPECIALIZE gate are unchanged:
`literature/2026-11-04-exact-projection-similarity-review.md`.
Audit L782 only, using L777's exact columns/Laurent estimate and L779's
fixed-pair node/residue and determinant conventions. The supplied PROOF
and DAG were inspected first. Preserve all pre-existing work.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is the exact signed-pairing similarity, whose downstream use would be a
later inertia test. Continue only if the row offset, convergence,
diagonal limit and invertible scaling all match; an unrepairable defect
stops this formula. Do not test an inertia or extend to other pairs.

Independent replay so far: write l-1=r+u and h-1=v. Then the coefficient
index l+h-1 is r+1+u+v. The first three shells of S_ij/alpha_i^r are
beta_(r+1), beta_(r+2)(alpha_i+alpha_j), and
beta_(r+3)(alpha_i^2+alpha_i alpha_j+alpha_j^2). Their diagonal values
are the first three derivative terms of h_r. The complete double
series is dominated on |x|,|y|<=t<sigma by
M_b sigma^(-r-1)/(1-t/sigma)^2. No truncated-shell check replaces that
full convergence argument.

Entrywise E_i^-1 d_i alpha_i^r K_ij E_j equals
(-1)^r sign(d_i) E_i K_ij E_j. Thus the proposed orientation is
E^-1(CS)E=JQ, with Q=-EKE at r=3. All E_i>0. Remaining audit work:
finish the finite-rank determinant/dependency check and record the
qualified conclusion in canonical L782. No scripts or certificate replay
are needed for these exact checks. Existing software contracts remain.

Targeted duplicate/failure checks: step443's class-import stop, step444's
closed Taylor test, step446's derivation, and L780's distinct balancing.
None supplies a missing inertia premise. The ready source assessment
is reused; no external search or theorem reproof is needed for this audit.

Completed: the determinant and direct-input checks pass. The full audit
is now canonical in `../lemmas/L782-exact-fixed-pair-projection-weighting.md`;
no correction was necessary. No change to PROOF's argument or to DAG
edges was needed. A linked-factor block-realization source question is
nominated separately with REVIEW_REQUIRED; no such realization or
index estimate was derived here.
