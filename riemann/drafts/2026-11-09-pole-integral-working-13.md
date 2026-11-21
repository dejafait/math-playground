# Pole integral/residual attempt — working checkpoint, step 13

Completed later in this step: the canonical proof and exact bounds are
in `lemmas/L930-pole-integral-regular-residual-and-norm-floor.md`.
The reasoning below is preserved as an unfinished-stage checkpoint,
not a current task. The pointwise parameter-norm estimate is stopped;
the new proof remains unaudited. Current routing is only in PROGRESS.md.

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-09-joint-pole-integral-residual-test-12.md`.
The current user gate authorizes one mathematical attempt despite the
historical nomination's pending-approval wording. Main gap:
L030–L032/C032a actual-Xi all-degree mixed positivity. This intermediate
test concerns only L928(11); signed realization and transfer remain open.

L928 and L929 have been read in full; L737's finite identities and
step261 audit have been checked. L929's endpoint transpose agrees with
L928's two spatial kernels. L929 is not thereby fully audited.

Work in progress, not established conclusions: put A=G diag(log n) G^-1
and j(z,d)=J_(1+z)(d)/phi(d). A candidate entire endpoint family is

    F_t(z)=exp(z ell_t/2) M(z/2+i/L)^T diag(j(z)) M(z/2+i/L),
    M(v)=G diag(n^(-v)) G^-1.

At z=+2i/L and -2i/L this should give respectively exp(i ell_t/L)W_+
and exp(-i ell_t/L)W_-. Apply the already assessed de Boor first-difference
integral entrywise, retaining w_XT and exp(i epsilon_t). Next verify its
derivative, finite-operator bounds and both full H metrics. The intended
certificate is ||B_pole||+||R_reg||<=1-eta, eta>0 fixed; an upper bound
above one alone does not refute contraction. A structural floor for a
specified norm estimate would stop only that estimate. No mathematical
script, numerical certificate or new lemma has yet been produced.
