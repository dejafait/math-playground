# Actual-Xi scalar sign attempt1309

Approved target: Decide C030z's actual-Xi scalar feasibility for all real x<1 by certified one-variable sign analysis, retaining L=0 and the free-p L=N=0 branch.

The supplied SPECIALIZE assessment1308 was read before work. This is
one RESEARCH calculation, using its fixed1307 rational outer boxes;
no new quadrature, precision refinement, sample sweep or general
root-isolation theorem is attempted. Main gap: actual-Xi all-degree
positivity L030-L032/C032a. A finite witness could inform separately
assessed realization; it proves neither univalence nor that positivity.

Bounded test: one symbolic reduction and one exact rational interval
sign pass, at most256 cells, depth at most16. Continue on a strict
actual witness or exhaustive obstruction; otherwise preserve unresolved
cells and stop this fixed method. Existing four-point, fixed-weight,
uniform-H2 and1297/1302/1200 stops remain intact.

Saved algebra before implementation: use z=1/(2-x), a bijection from
x<1 onto 0<z<1, inverse x=2-1/z. Write L=l0+l1*x and
N=n2*x^2+n1*x+n0. Then l=z*L, n=z^2*N are polynomials. Define
v=n-k*(3*z-1)*l, j=v-(B/D)*(2*z-1)*l and
h=n*j-(C/E)*(2*z-1)*v*l+(1-z)*(B^2/(2*A*E))*n*l.
For l!=0, p=n/(z*l), V=v/(z*l), J=j/(z*l),
H=h/(z^2*l^2). These identities require exact verification in the
certificate and canonical proof before any conclusion. At l=0 retain
n!=0 rejection or n=0 free-p, never divide a zero-containing box.

Completed: full proof is in C030z's calculation1309; certificates are
scripts/grunsky/actual-sign-certificate-1309.json and
scripts/grunsky/actual-sign-replay-1309.json. One29-cell pass, depth<=16,
gave9 feasible,18 excluded and2 unresolved cells. The rational center
of the first feasible cell gives x=-16162/111 and exact p=N/L in the
actual constants. All p,V,J,H,tau have strict positive lower margins.
The unique L root has N>0; no free-p branch occurs. Both tails and
every -1<=x<1 are excluded. Exact replay passes all145 sign bounds.

The unresolved closed z cells are [439/65536,55/8192] and
[2131/32768,4263/65536]; neither is declared an exact equality locus.
Their status does not affect existence. No further refinement follows.
Decimal assumptions remain inherited through1307; no source novelty,
Mathlib coverage or RH conclusion is claimed. All load-bearing values
and replay checks were inspected. The witness has c11<-1; no analytic
realization is supplied. New critical-audit nomination1309 is
REVIEW_REQUIRED before interpreting the excluded range against exact
Grunsky hypotheses; reuse1303/1308 rather than generic browsing.
No justified new creative mechanism follows yet: realization and
all-degree actual signs remain unpaid.
