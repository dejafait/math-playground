# Actual-b_m Pringsheim test — preserved working checkpoint, step210

Completion note: the obligations below were subsequently addressed in
the canonical [L976 proof](../lemmas/L976-pringsheim-obstruction-to-the-actual-bm-lower-envelope.md).
This preserves the unfinished checkpoint, not a second current result
or next-action record. The completed proof awaits independent audit.

2026-11-10. The prior SPECIALIZE assessment is unchanged and covers
this attempt. Main gap: L030-L032/C032a positivity and L966 signed
forcing. This test only concerns feasibility of L975's hypothesis H.

Candidate argument saved before completion: put g(w)=xi(1/(2-w)).
An unconditional zero and reflection allow beta>=1/2, so its image
w_rho=2-1/rho has squared modulus 4+(1-4*beta)/|rho|^2<4.
Zeros in any closed w-disk of radius below 2 form a finite set.
The intended radius is the smallest mapped-zero modulus, not the
inner map's pole distance. L975 already supplies a lower bound 3/2.

Remaining checks: prove nonremovability for arbitrary multiplicities;
extend the same logarithm through the positive-radius point; under H
choose a strictly between that radius and 2, pay every exceptional
coefficient and b_0 with C, and prove G+C/(1-w/a) has exactly the
original radius before invoking Pringsheim. A failed check stops this
test. No obstruction is recorded as established by this checkpoint.

Essential local inputs: L013, L018 and L975; L026 supplies L975's
localization through that result. Use the previously inspected DLMF
zero-existence statement and Flajolet-Sedgewick Theorem IV.3, 2004.
L968 is downstream only. No numerical evidence or new script is needed.
