# Approved principal-slice calculation: working record

Target and prior gate: the exact SPECIALIZE target in
`drafts/literature/2026-11-06-real-part-principal-slice-test.md`.
Only the off-divisor L847 first-jet relation is being tested.
The full PROOF and DAG were supplied; L847(1)-(3) and the parent
source assessment's principal-space definitions were inspected.
Existing unfinished files are preserved.

At a fixed zero-jet write f=p+iq!=0. The inequality is
H(A)=p(1-det A)+q tr A>0. For a nonzero real covector xi,
the principal plane is A0+v xi^T, v in R2. Exact rank-one
determinant expansion gives
H(A0+v xi^T)=H(A0)+(q xi-p cof(A0)xi).v.
Thus every nonconstant nonempty slice is a proper open half-plane,
its sole component equals its own convex hull, and it is not ample.
Constant slices are either full or empty. The cofactor convention
is cof([[a,b],[c,d]])=[[d,-c],[-b,a]], not the adjugate.

All-frame check to retain in the canonical proof: in arbitrary base
coordinates the angular differential is an invertible real matrix B.
Varying one derivative column, then translating back via B inverse,
varies A by w xi^T for a nonzero xi. Hence considering every xi in
the original angular trivialization suffices; fixing target y does
not cause a missing base-coordinate term.

Actual attainment: theta=(0,0), y=(0,log 2) yields z1=R,z2=2R,
f=-C G(R)G(2R)/(4R^2)<0. At A=t I, t>1, H>0 and the linear
coefficient is -p t xi!=0 for every xi. This stops even local-frame
ampleness at a genuine off-divisor zero-jet, not merely at a generic
complex coefficient. More generally, for p<0 every slice containing
an admissible A is proper: if the coefficient vanished, rotation to
xi=e1 would give A12=0,A22=q/p and H=(p^2+q^2)/p<0.

Completed: the constant-slice classification, frame quantifiers,
actual attainment and scoped import stop are now canonical in L862.
The cofactor convention gives A12=0 in the degenerate case; the
preliminary A21 transcription was corrected before writing that proof.
This is routine finite-dimensional specialization; no formal
solution, global graph, Xi sign, RH claim or new general convex
integration theorem is asserted. No mathematical script is needed.
