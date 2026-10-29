# Step535 — approved swap-margin attempt, working record

The invocation gate approves exactly the TARGET in
drafts/literature/2026-10-28-first-drop-swap-margin.md (EXPLORE, saved before
invocation). Startup GOAL, PROGRESS, PROOF, DAG and that assessment were
supplied verbatim. Existing notebook changes are retained.

Main gap: universal eventual strict descent. Intermediate target: the
directed inequality M(u10v)<=M(u01v) when both words have their first
coefficient drop at the final step, using their least representatives
>=2. A successful comparison could support a guarded sorting reduction;
connectivity, base positivity and finite coefficient-drop existence would
remain independent gaps.

Use the assessed Rozier2019 Lemma1 finite coding/affine formula and
Rozier–Terracol2025 Lemma2.1 remainder order by citation. The previous
discovery assessment and its recorded failure comparison have been read;
no prior local lemma is a mathematical premise of this test. No
cross-notebook input. Full Mathlib coverage remains unchecked.

Bounded plan: derive the exact one-edge difference, retaining the modular
representative carry; search both guarded endpoints through length24,
stopping on the first strict reversal. Preserve all prefix guards, exact
representatives, affine constants, margins and direct trajectories in a
certificate. A finite pass is only EXPLORATION. A reversal rejects this
certificate and ends this attempt without tuning a variant.

## One-edge derivation before the finite screen

Put r=|u|, s=#ones(v), q=#ones(w), m=2^j, D=m-3^q>0 and
B=2^r*3^s. Rozier–Terracol Lemma2.1's two-step remainder difference
is 1/4, multiplied by the common suffix coefficient; hence
A(w')=A(w)-B. Rozier Lemma1 gives
3^q*rho(w)+A(w)=0 modulo m. Thus, if
R=(B*(3^q)^(-1)) mod m is chosen in {1,...,m-1}, then

rho(w')-rho(w)=R-c*m,
c=floor((rho(w)-2+R)/m) in {0,1},
M(w')-M(w)=D*(R-c*m)+B.

The interval [2,m+1] implements the exclusion of n=1 without deleting
its parity class. The carry must not be omitted. These identities use
only the assessed finite facts and a representative calculation, not
infinite coding or a coefficient-stopping-time assertion.

Rechecked the primary Rozier Lemma1 statement and affine proof on
printed pp.2–3, and Rozier–Terracol Definition2.2/Lemma2.1 including
both changed steps and the common suffix. No further literature search
or changed coverage is needed. The exact bounded screen is next.

## Completed attempt

The first guarded edge found is 11010-to-11100 at length5. Its exact
margin difference is64>0, against the required upper bound0. The
script stopped immediately; lengths1–4 completed and length5 did not.
The full `/counterexample` and `/lengths` certificate values were read,
including every guard and both direct trajectories. No verification
check failed. The canonical proof and precise imports are in
lemmas/L109-first-drop-swap-margin-counterexample.md; the failed route
is recorded in ATTEMPTS/036-first-drop-swap-margin.md. No modified
comparison or further mathematical mechanism was tested.
