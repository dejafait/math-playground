# Physical corner reserve — step148 working record

Approved target: exactly the TARGET in
`literature/2026-11-10-physical-corner-reserve-147.md` (SPECIALIZE at invocation).
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
This step is a finite calculation/reproduction, not a creative mechanism.

Use L960 definitions at t=98/625,x=6000000185827, complete support;
reuse L961 only for comparison of N, independently recertifying the floor.
Let alpha=u+iv, alpha'=d+ie at s=(1+ix)/2. Then
sigma=1/2+t*u/2, tau=x/2+t*v/2 and
ell=2Re(alpha+t*alpha*alpha'/2). Compute these exact branch-compatible
quantities, including atan(x)=pi/2-atan(1/x); never substitute x/2 for tau.
The principal branch is conjugation compatible here since Re(s)>0.

Existing L960 expansion with |a|<p, |b|<q, |S|<25R+81/2 gives
|Re(conj(A+a)(S+b))-Re(conj(A)S)|<E,
E=p*(25R+81/2)+q*R+p*q. This bound uses neither stability nor a modulus
floor. It keeps M32 and the other stated scalar/analytic hypotheses.
Strict F-E>0 pays one point conditionally; F+E<0 gives a conditional
negative obstruction. Neither sign is computed yet; overlap is inconclusive.

Implementation plan: exact 256-bit included arithmetic from step140;
logarithms via complete integer factorization, physical phases via complete
multiplicativity and certified prime argument reductions; positive amplitude
exp(t*log(n)^2/4-sigma*log(n)). New finite Taylor remainders and all
branch/reduction gates must be justified. Store exhaustive contiguous block
records, accumulated sums and scalar thresholds. Deadline600 seconds,
incremental saves and tool yields within60 seconds. Cost failure parks
this implementation. No sweep or adjacent-centre continuation is authorized.

Global/zero-time transfer and all remaining Xi signs stay unresolved.

Completed: full338-block run in88.36 seconds gives F-E>150.30619;
all11 global gates and1370 complete record/endpoint checks pass. Full
proof and qualifications are canonical in L962; no independent
transcendental replay is claimed. Next audit coverage is prepared in
`literature/2026-11-10-physical-corner-independent-audit-148.md`.
