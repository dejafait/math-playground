# Exact associated-theta radial test — working record

Approved target: the radial limit in the preexisting assessment
`literature/2026-10-31-associated-theta-boundary-growth-test.md` (EXPLORE).
Inputs: L019 and the actual-k strip proof in L239; L233 only interprets
the downstream first-sign gap. Existing proportional-index saddle work
is a contrast, not an input to this estimate.

Proposed estimate, still being checked: write y=pi/4-delta,
h=sin(2delta), v=pi exp(2(s+iy)). On the real-s interval
10<=Re(v)<=20, one has |v|>=10. Factor the exact series as

    k(s+iy)=8pi^2 exp(9(s+iy)/2-v)
      [1-3/(2v)+sum_(m>=2)(m^4-3m^2/(2v))exp(-(m^2-1)v)].

Use m<=2^(m-1) and m^2-1>=3(m-1) to dominate the entire tail
by (23/20) sum_(j>=1)(16 exp(-30))^j < 1/20.
Together with 3/(2|v|)<=3/20 this should give |bracket|>=4/5,
so the weaker factor 1/2 is available. Squaring and integrating over
s in [s0,s0+(log 2)/2], s0=(1/2)log(10/(pi h)), should give
A(iy)>=16pi^4 exp(-40) ((log 2)/2) s0^2 exp(9s0).
Since h<=2delta, this is stronger than needed for delta*A(iy)->infinity.

Checks still required: exact factorization and constants; convergence and
holomorphy of the associated integral on compact complex-z sets with
arbitrary bounded real shifts; conjugation giving A(iy)=integral s^2
|k(s+iy)|^2 ds; and the precise limitation to radial O(delta^-1) models.
No boundary trace or Fourier sign follows. No mathematical script is
needed if these analytic inequalities check out.

Completed: the proposed inequalities and compact-set domination are
written in canonical L596. The complete tail certificate is geometric,
with q=16 exp(-30)<16/481 and tail <368/9300<1/20. The achieved
lower bound is A(iy)>=C delta^(-9/2), hence delta*A(iy)>=C delta^(-7/2).
No numerical sampling or boundary-limit interchange is used. This is
an informative rejection of the low-order radial ansatz, not a sign
theorem. Independent audit is pending; the provisional reasoning above
is retained for recovery, with L596 authoritative for the full proof.
