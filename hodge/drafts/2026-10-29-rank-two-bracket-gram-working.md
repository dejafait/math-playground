# Rank-two bracket Gram attempt — working preservation

2026-10-29, step 606. Invocation-start gate: SPECIALIZE in
`drafts/literature/2026-10-28-rank-two-polarized-bracket-gram.md`.
This preserves the pre-proof working checkpoint, not an audited result.

Main gap: uniform primitive Hodge realization and existence of the
conditional equality kernel F. Approved intermediate test: at
s=781,t=46 compare the actual section-bracket Serre Gram rank with
dim H^2(X,End_0(F))=816. A strict excess excludes only this endpoint;
other parameters, stable types, transport and general realization remain.
Stop if the comparison needs metric/Leray compatibility, gives rank at
most 816, or admits a countermodel under all the additional identities.

Retained inputs: L116/L117's actual endpoint maps, L163's single
harmonic R and positive factor forms, and L165's Serre normalization.
L179 and ATTEMPTS/057,/090,/092–096 were checked as contrasts; their
finite witnesses do not impose the polarized rank-two trace identity.
No cross-notebook input, new source search, independent factor action,
section integrability, or multiplicative splitting is used.

Provisional algebra to check in full:

* For odd traceless matrix-valued forms, put s(a,b)=tr(a b). The
  ordinary cited coefficient identity, with the acbd exterior sign,
  should give 2tr(abcd)=s(a,b)s(c,d)+s(a,d)s(b,c)+s(a,c)s(b,d).
  For the unhalved symmetric odd bracket beta(a,b)=ab+ba this becomes
  tr(beta(a,b)beta(c,d))=2(s(a,c)s(b,d)+s(a,d)s(b,c)).
* In cohomology s(u,v)=a(u,v)theta_1+b(u,v)theta_2, with a,b
  alternating. L163 and actual j_1 give nondegenerate a and
  b(u,v)=a(Ku,v), where K is diagonalizable with positive eigenvalues.
* On Sym^2 H the induced form a_2 is nondegenerate. The bracket
  Gram form should be a nonzero scalar times
  a_2((K tensor 1+1 tensor K)-,-). All eigenvalue sums are positive,
  so its rank should be dim Sym^2 H=1081, exceeding 816 by 265.

Outstanding at this checkpoint: all four word signs and repeated inputs; descent
of the form identity through actual cups; common normalization and
the ordering of a,b; nondegeneracy on the symmetric quotient and the
pullback rank inequality. No broader t or s consequence is attempted.

Completion: the full specialization and all these checks are now written
in L180. It gives the conditional endpoint contradiction 1081>816;
separate critical audit remains pending. The analytic proof, rather than
a numerical or matrix preview, establishes the claimed rank. No
mathematical script was needed. See the current PROGRESS.md for routing.
