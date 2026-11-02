# Signed lower-edge saddle for the fixed unit lattice

Prepared STEP_ID: 2026-11-02-lattice-bottom-saddle-11.
RESEARCH / proof_attempt under the unchanged invocation-start EXPLORE
assessment `literature/2026-11-02-localized-logarithmic-joint-moment.md`.

Main gap: a uniform H-versus-exact-D comparison for all original
integer families; Xi realization and signs are independent gaps.
Intermediate target: C663a's exact bottom polynomial for L663's fixed
spacing h=27/(10n), n=6q+3, unit residues, all grid factors and moments.
Seek a signed coefficient lower bound with loss rho<261/20000. This
would feed the fully paid localization, for this lattice only. Continue
only if the complete signed saddle and all kernel/contour remainders
leave a strict exponent margin; otherwise quantify the obstruction.

Read C663a completely, L649's conventions, L663's finite contour and
analytic bounds, L658's localization, L661's diagonal statement,
L659's resonant-lattice proof, L660's phase obstruction, and scoped
endpoint/full-circle/screen stops. L659 uses a different spacing tied
to the finite anchor phase; it does not settle the present lattice.
No source refresh is needed: only finite-product Taylor and contour
specialization under the existing coverage are proposed.

Unfinished reasoning saved before lengthy work: at u=-1 set a=-e+i*s,
with 117/100<=e<=5/4 and b=5/4-e. Then W at s=0 is positive and
its linear phase is i*n*g_n(e)*s, where
g_n(e)=n^(-1) sum_j [1/(e-t_j)+t_j/(U-e*t_j)]. The kernel's first
term on y=s-i*b contributes exp(-lambda*n*b-i*lambda*n*s),
lambda=20*pi/27. Seek g_n(e_n)=lambda in the interior of this range.
If it exists, a finite-product Gaussian limit may control the full
signed integral. All higher kernel terms must be bounded, and moving
the bottom edge requires bounding the added side segments. No saddle
existence, rate or noncancellation is yet asserted.

## Completed bounded attempt

The complete argument is now canonical in
[C663b](../lemmas/C663b-lattice-bottom-saddle-paid-arc.md).
At u=-1, the unique continuum saddle satisfies g(e_*)=20*pi/27
with 117/100<e_*<5/4. Monotonicity and exact rational endpoint
bounds give loss rho<103/9375<261/20000. The finite phase error
is O(1), the full signed first-frequency integral has a positive
Gaussian limit, and all higher kernel frequencies have vanishing
relative size. C663a's top/side bound survives the shortened contour.
The resulting paid arc margin is 619n/150000-2log n-C.

The exact rational checks are saved in
`scripts/one-sided-hankel/lattice-bottom-saddle.json`; all pass.
The earlier inline decimal values only checked plausibility and are
not proof premises. No finite-family screen or numerical saddle is
used. Outcome ADVANCE is local to this fixed lattice; full-circle
failure is retained. No general-support result or RH candidate follows.
The result and its inherited contour inputs need a separate conceptual
audit, with source coverage reused and a newly saved audit assessment
subject to separate next-turn approval.

