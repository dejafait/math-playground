# Step 501 — distinct-kernel-line matrix-pencil attempt

Ready invocation-start assessment: drafts/literature/2026-10-25-four-row-finiteness-review.md (EXPLORE), exact target unchanged. Main gap: uniform twelve-row exclusion; intermediate target: all eligible original four-row loci finite, or one explicit infinite family. A finite list could feed later-row tests; second-pair extraction and coding gates are independent. Existing L158/ATTEMPTS/050 sample failures are not repeated. L159 proves only coincidences and has no separate audit; it is not used as a proved input in the new distinct-line argument.

Saved before further work: let A=V_a, B=V_b, C=V_c, D=V_d. Both designated pairs are disjoint. A plane with four distinct intersection lines has uniquely normalized representatives x in A, y in B, x+y in C, x+t*y in D, up to common nonzero scalar, with t!=0,1; x,y are nonzero. This retains every generator coefficient, including zero coefficients on the g_j.

Set U={(x,y) in A direct-sum B : x+y in C}. The sum map is injective, so k=dim U<=3. On U define M(t)(x,y)=Q_d(x+t*y). M(1) is injective because C intersect D=0. Some k-by-k minor is nonzero at 1 and has degree at most k. Hence at most three t can support the distinct-line locus. For t!=0,1 every nonzero kernel vector automatically has x,y independent and gives four distinct kernel lines; this needs a full written check, including x=0 and y=0 and every zero-rank case. Projective kernel points should correspond bijectively to planes at that t, so dimension two is a genuine remaining infinite-family obstruction, not a finite-point proof.

Test to complete: prove the correspondence, bound all exceptional kernel dimensions and the number of exceptional t, and determine whether the actual coordinate structure excludes dimension two. Do not claim the universal target from finite t alone. If no actual exclusion or eligible infinite example results, report that remaining obstruction and reassess; no all-label rank census, fourth sample or new source retrieval.

Completed this bounded attempt: L160 gives the exact projective-kernel
bijection and all four rank-one/line-distinctness checks. A left inverse
of M(1) embeds each K_t in an eigenspace of a fixed endomorphism of
U, at distinct eigenvalues. Their dimensions sum to at most k<=3.
Dimension three is impossible: it would make all four kernel spaces
pairwise disjoint, whereas their eight I-incidences on seven coordinates
force a shared coordinate vector. A two-dimensional kernel is therefore
unique if present. Frobenius preserves its dimension and hence fixes its
parameter, which must lie in F_97. This leaves a possible projective-line
family plus at most one isolated plane, or at most three planes total.

The intended universal threshold was not reached: no original quadruple
realizing or excluding that two-dimensional kernel was obtained. The
result is a relevant partial structural input, not just a rank preview,
but it must not be promoted to finiteness. Next keep the same approved
target and test this remaining actual-map defect, preserving zero
generator coefficients and all inherited inputs. L160's t is the ordered
cross-ratio; it is distinct from L104's coding t=0. No numerical parameter
scan or all-label census was run. The canonical proof is L160; no separate
critical audit is claimed.
