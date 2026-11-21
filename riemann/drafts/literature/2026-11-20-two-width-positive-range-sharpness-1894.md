# Oriented two-width positive-output range: assessment1894

TARGET: Determine whether C032u's sufficient coefficient range is sharp for eta_a=(1+a)delta_2-a*delta_1, a>=0, using bounded positive Laplace tests.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source comparison1894 checked signed-mixture domination and searched C032/C033 plus first-odd/reverse-domination and finite-Levy assessments for sharpness, optimality and large-s tests; no completed classification of this oriented family was located in that scoped check. No novelty claim.
SOURCE_EVIDENCE: Reuse notes1552/1562/1565: Bertoin2000 https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf Theorem1.2 pp7-8/finite activity p9; Mimica2015 https://web.math.pmf.unizg.hr/~amimica/lt.pdf Proposition1.4(i),(iv) pp6-7; Blanchard--Lee--Scott2010 https://www.jmlr.org/papers/volume11/blanchard10a/blanchard10a.pdf Proposition5 p2984/AppendixA.2 p3001. Use the standard Lebesgue dominated convergence theorem against a finite probability with dominator1.
COMPARISON: C032u constructs positive outputs in its sufficient interval and gives the exact comparison factor and zero atom. Generic sharp-domination criteria do not compute the actual range. The distinct remaining test is necessity for this oriented pair, using bounded Laplace integrals and the available factor, with no density or tail theorem.
GAP: Determine the actual necessary condition on a and compare it with the sufficient interval, retaining endpoints and a=0. The large-s ratio limit and its positivity implication are proposed calculations, not established here.
REASON: This independently testable coefficient question determines whether the existing positive constructor can be enlarged in its own orientation. Full positive-output approximation is parked. No reverse orientation, full cancellation or RH conclusion is authorized.
SCOPE: Exactly C032j/q/t/u's laws at widths1,2 and unchanged external qualifications; finite real a>=0; output nonnegativity on every Borel set of [0,infinity). No density, finite moments, RH or full J_eta=0 assumption.

## Covered test and threshold

Use C032u's existing finite positive Pi(dt)=(ell_2(t)-ell_1(t))dt,
mass M>0, comparison probability pi, q=exp(-M) in (0,1), and
nu_2=nu_1*pi with pi({0})=q. C032u already proves positivity for
0<a<=q/(1-q); a=0 is an original probability. Do not reprove its
compound-Poisson theorem or sufficient construction.

For necessity, assume this output is positive and test against
exp(-s*u), s>0. Use C032q's bounded signed integration identity.
Investigate the large-s ratio k_2(s)/k_1(s) through the comparison
factor's Laplace transform; k_1(s)>0 at every finite s. Check the
limit against the complete factor, including its zero atom, before
inferring a condition on a. This is a prospective test; no limit or
coefficient classification is derived in this literature assessment.

The known finite-activity factorization, positive bounded Laplace
integration and dominated convergence supply the needed tools.
The first-odd route's reverse comparison nu_2<=k*nu_1 is a different
orientation. No density, small-x ratio asymptotic or higher-order
Tauberian theorem is required by the proposed test. Preserve old stops.

Continue only to an exact conditional classification with endpoint
bookkeeping or an informative failure of the necessity test. If its
factor/limit interface cannot be justified, stop this pair without
adding widths or assuming densities. A pair classification cannot
decide full d_pos, cancellation, moments, signed height or Xi transfer.

Retain actual divisor/conjugation/multiplicity, excluded ordinate zero,
strict strip/gamma>14, counting, through100/retained real zero,
reciprocal-square tail, heat positivity and the separate fixed-j error
inputs needed by C032t, Gaussian half-variance and both fixed-v1
qualifications. The external preprints and finite-zero data are not
verified here. Full matching Mathlib coverage remains unknown.

This is known-tools specialization, suitable for REPRODUCTION, not
creative work or certified novelty. Its mathematics has not been
performed. This newly written ready continuation requires separate
supervisor approval on a later turn.
