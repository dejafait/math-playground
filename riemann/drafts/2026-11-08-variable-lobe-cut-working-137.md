# Four-demand Hall-cut working record — step137

Approved target: the exact four-demand test in the supplied SPECIALIZE
assessment `drafts/literature/2026-11-08-variable-lobe-four-demand-cut-test.md`.
The ready source comparison is reused; this is a mathematical calculation,
not a new resource theorem or a literature turn.

Main gap: L030–L032/C032a all-degree actual-Xi mixed positivity. Intermediate
target: all 15 necessary Hall cuts for F={-2,-1,0,1}, x=16,y=0. A negative
cut would eliminate every conserved nearest-neighbor allocation. A pass
would leave all other demands, infinite signed residual and higher signs
unresolved. No complete solution is claimed.

Inputs checked: L898 in full, L019/L020 interfaces, L312's uniform kernel
and theta bounds, L037 arithmetic, and L904's full change of variables and
quadrature construction. Its negative sign and L313's total sign are not
inputs. Existing equal-share failure is preserved. Source hypotheses and
duplicates are retained in step136's comparison.

In progress: specialize demand equality and resource upper capacity to
necessary cuts only. With t=(u+v)/2, rho(q)=2 integral_0^infinity
t^2 K(t+q/2)K(|t-q/2|)dt for q>=0; A0=2M0M2. Jacobian is one and
Phi=K/2 cancels p^2's factor four. Evenness reflects complete lobes once.
No positive resource outside T(S) can enter S under the stipulated rule.

New domain: q<=9b=9pi/32<9/8, b=pi/32. For t>=T=pi/2,
t-q/2>=pi/2-9pi/64=23pi/64>0. Thus L312 gives the same product
tail 65536 exp(9t-6exp(2t)), uniformly over this larger q domain.
For t=3/2+w the exponent is <=-106-231w; the spatial density tail
is 131072 exp(-106)(9/(4*231)+3/231^2+2/231^3).
The finite-t theta density error is <=512*(160000 exp(-75))/3.
Both tails include both transverse directions; use full lobe widths.

Declared bounded calculation: one real-box grid M=64, followed only if
needed by M=128 as the maximum error-budget completion. Integrate all
q cells through 9b, all t cells through pi/2, retain all four theta head
terms and both complete tails. Stop at a certified negative cut, all
strictly nonnegative lower cuts, or zero-containing intervals at M=128.
No larger mesh, block, frequency or height sweep is authorized here.
Save full grid/weights/cache/tails/cuts, failures and arithmetic assumptions.

Completed within budget: M=64 and M=128 both pass all fourteen proper
cuts and leave only the full four-demand cut unresolved. The canonical
proof and exact reproduction commands are in L905; complete certificates
are `scripts/theta-marginal/variable-hall-cuts-137-m64.json` and
`scripts/theta-marginal/variable-hall-cuts-137-m128.json`. The final proper
cuts have H>1/100, while -1/125<H(F)<1/100 contains zero. No further grid
is authorized by this attempt. Continue only with the nominated bounded
audit after its separate approval. The complete infinite residual remains
an unresolved obligation, never an input. No cross-notebook theorem is used.
