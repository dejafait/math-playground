# Matched adjoint transport — working1043

This is the single mathematical attempt approved by review1042 in
`drafts/literature/2026-11-16-reverse-matched-adjoint-transport-nomination-1041.md`.
Its exact fixed-bump target and hypotheses are unchanged. The supplied
overview and DAG have been inspected. Earlier unfinished work is preserved.

Main gap: L030–L032/C032a actual-Xi all-degree positivity. The bounded
intermediate target is simultaneous smooth nonnegative adjoint tests on
the actual reverse chamber, pair and triple pieces. Its proposed use is
removal of exterior flux and test-derivative terms in a local tested
assembly; global assembly, realization, all degrees and Xi signs remain
unpaid.

Continue only with all nominated matches and a fixed exterior zero
neighborhood for one common positive time, or an actual-data
incompatibility in exactly this smooth-test class. A failed ansatz or
insufficient speed estimate is inconclusive. The existing stops1000,
1009 and1023 concern different conditions and are not used as a global ban.

Initial proof plan: inspect the undivided original forms near t=0 and a
single pair face before attempting global characteristics. A smooth
solution must satisfy every limiting compatibility condition there;
any genuine contradiction would already settle the nominated class.
No division through the original zero set is assumed legitimate.

Essential inputs to inspect as needed: C467e/audit1017, C467i/audit1025,
C467j/audit1029, C467k/audit1033, C467l/audit1037 and C467m/audit1041,
with their actual B/beta/H/H0/F, raw time, common minus sign and inherited
C466z/C466/C466a qualifications. No result was claimed at this initial checkpoint.

## Intermediate reasoning saved before the full write-up

Use centered initial coordinates c=x+h/3, h>0, and t=rho^2,
h=k rho, with fixed k>0. The regular coefficient flow and C467i(13)
give the leading centered cubic
v^3-(k^2/3+6)v-2k^3/27. Let r be its largest root and D>0
half the gap of its other two roots. Then D^2=k^2/3+6-3r^2/4.
The actual pair map has leading centered imaginary coordinates
rho(-r/2-sD,-r/2+sD,r). Its real shape corrections have order
rho^3; the common center has its actual order-t complex drift.

A smooth test with the nominated initial value has, where f=chi0>0,
P=f^3, K=f^3(log f)'', and
phi(0,c,h)=P+K h^2/3+O(h^3). Write A(c,s)=phi_t(0,c,s,0).
Using the original real form, the scaled adjoint equation is expected to be

    A - v(c) P' - 6r K/(r+k/3)
      - s k A_s/[D^2(r+k/3)] = 0.

Here v(c) is the same actual phase-weighted center drift for every k,s;
it must not be replaced by the pure model. At k down to zero,
r -> sqrt(6), D^2 -> 3/2, so A=v(c)P'+6K is independent of s.
At k=1 the remaining equation is 2K/(r+1/3)=0. Thus K=0,
incompatible with a smooth bump equal to one near zero and compactly
supported. This would exclude smooth pair tests even before imposing
the chamber/triple matches or exterior support.

Still to check in the canonical proof: smooth scaled polynomial division,
root derivative asymptotics at fixed physical h, all four original minors,
the nonvanishing real denominator on positive-time nonzero s,h points,
and both sequential limits. No assertion is based on numerical evidence.

## Completed attempt

The full proof is now canonical in
`lemmas/C467n-actual-h-reverse-joint-smooth-adjoint-obstruction.md`.
It verifies the indicated original coefficient limits and obtains a
contradiction for the nominated bump from the pair alone. The proof's
J denotes the time-zero test derivative called A in the scratch work
above; its A denotes the original spatial form coefficient.

The optional SymPy availability check failed because that package is
not installed. No dependency was installed or computation assumed.
The standalone standard-library exact polynomial checker instead
passed all 14 checks; the complete certificate's /checks value was
inspected with the prescribed JSON inspector. These checks verify
algebra only. Independent conceptual review of C467n remains pending.

Outcome: NEGATIVE for this exact joint-smooth class. No construction
with weaker corner regularity was attempted or approved. All prior
unfinished work is preserved. The new audit nomination is
REVIEW_REQUIRED and is not a same-turn approval of uncovered mathematics.
