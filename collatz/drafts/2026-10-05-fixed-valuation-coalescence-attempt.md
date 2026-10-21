# Fixed initial valuation: completed attempt

Completion: [L026](../lemmas/L026-fixed-valuation-residue47-coalescence-obstruction.md)
proves the all-horizon fixed-a obstruction. The exceptional anchor c0=47
required a complete finite slope table and its explicit finite orbit;
merely copying L025's c0<=20 bound would have been incorrect. Full
checks are in `scripts/odd-run-coalescence/certificate.json`. The linear
clock fails, as does every finite clock depending only on the initial
valuation. Full-height clocks and universal descent remain unresolved.
The next invocation should critically audit the completed proof under
the same prior target assessment, not run a larger finite screen.

## Initial saved reasoning (superseded by the canonical proof)

Approved target and prior coverage:
`drafts/literature/2026-10-05-residue47-odd-run-clock-coalescence.md`.
Main gap: universal eventual descent. A smaller residue-20 companion
could transfer convergence to a hypothetical least root, but the cover,
finite base and other cylinders are not assumed.

Test: for every L>=6, impose n=47 modulo 3^(L+4) and
81n+97=0 modulo 2^(L+1), with n sufficiently large. CRT gives
unbounded positive roots. The binary condition gives n=47 modulo 64,
hence v_2(n+1)=4. The proposed actual prefix is O^4 E O^(L-5).
After t>=5 steps, y_t+1=3^(t-5)(81n+97)/2^t.

For an inverse word of length s with a odd inverses, use c+1=lambda(n+q)-d,
0<=d<=2^s-1. Before the exit q=1; afterwards q=97/81 and
lambda=2^(s-t)3^(t-1-a). Compare at anchor 47. Its difference from n
is divisible by 64 and the specified ternary modulus, so for h=s-t
the companion difference has at least h+6 factors of 2 when h>=-2.
The extra six matched parity inputs may permit the old anchor bound
despite the factor-three loss from the even step.

Unfinished: check both slope cases, exact integer/residue transfer,
the short-clock cases, and the lambda=1 offset. Only then state an
all-horizon result. A finite no-hit screen is not a proof. If this
mechanism fails, record the precise failure rather than merely enlarge L.
