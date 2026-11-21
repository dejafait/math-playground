# Centered Hermite residue test — working record 382

Completed: canonical L764 gives the fixed-grid stop, with the outward
interval certificate at `scripts/centered-hermite/residue-moment-382.json`.
The validated b_4 is positive and d>=max{6,ceil(12000000a)} forces a
strictly wrong extremum sign. No RH conclusion. The preliminary saved
checkpoint below is preserved; its pending checks have been completed
locally, but independent audit remains outstanding.

Approved target/assessment: the fixed-a, n=0 signed-extremum target in
`drafts/literature/2026-11-04-centered-hermite-extremum-margin.md` (EXPLORE
before invocation). Inputs read: L018–L021, L027/L028, L763. No root-sign
premise is used. Existing unfinished work is preserved.

Set c=gamma_1/gamma_0 and b_j=(Theta(z)exp(-cz))^(j)(0)/gamma_0.
The full translated polynomial is the reciprocal Jensen polynomial of
Theta exp(-cz-az^2). Preliminary finite division gives, with
K_d=2 gamma_0 a^(d/2),

 P_d/H_(d-1)/K_d = x+A/x+B/x^2+C/x^3+O(x^-4),
 A=d(d-1)b_2/(8a)-(d-1)/2,
 B=d(d-1)(d-2)b_3/(48a^(3/2)),
 C=d(d-1)(d-2)(d-3)b_4/(384a^2)
   +d(d-1)(d-2)b_2/(16a)-(d-1)(d-2)/4.

These formulas still require checking and canonical write-up. At a zero
r of H_(d-1), H_d(r)=-H_(d-1)'(r), so requested signs imply all residues
negative. In particular C must be nonpositive. A positive actual b_4
would make C positive eventually for each fixed a and stop this grid.
A floating midpoint diagnostic suggests b_2 about -3.7173e-5 and b_4
about 1.6722e-10; these are NOT certificates. The small b_4 sign requires
validated actual-theta integration. No higher coefficient hierarchy will
be attempted if this bounded test is inconclusive.

Plan for rigorous sign: composite Simpson on u in [0,2], n<=4 in L019,
with explicit fourth-derivative bounds and analytic n/u tails. Use Decimal
outward intervals; write complete certificate to scripts/centered-hermite/.
Final conclusions and a fresh checkpoint will replace this pending note.
