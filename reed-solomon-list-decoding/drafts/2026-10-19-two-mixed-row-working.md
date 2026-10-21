# Step 342 — two mixed rows at fixed columns, working record

Approved target: Test whether L092's retained subsystem together with mode (2, 5) has a nonnegative moment completion at L086's unchanged columns.

Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
Intermediate target: the 28 equality / 43 zero-old-block / two mixed-row / 45 sign necessary subsystem. Its feasible witness would park this stronger exclusion diagnostic; an exact separator would exclude these fixed columns conditionally. Other modes, scalar upper rows, anchors, columns/base/pairs, global moments and RS realization remain unresolved.

Reuse SPECIALIZE assessment `literature/2026-10-19-fixed-column-two-mixed-mode-subsystem.md`. Exact inputs: L021,L053,L073,L075,L076,L078,L082,L083,L084,L086,L090,L091,L092,L093, retaining foundations/04,09,10,12 qualifications. Freeze rho,p8,pairs,seven RREF/completion,L086 columns,t78=s; vary only 45 moments through the complete 18-coordinate equality locus.

Continuation/abandonment test: independently reconstruct both full old blocks, ranges, inverse costs, original/raw lift directions and all retained rows; one deterministic rational Phase I, at most 10000 pivots/300 seconds. Accept only complete original/raw feasible witness or lifted strict separator. Cap is inconclusive; preserve full initial/terminal state and stop without restart or extra row. L092 moments are regression controls only. Prior full-row/conic caps are not resumed. No solution or finite verdict yet.

## Fixed system and certificate plan

For i=9a+b use D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0, and V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0 for r+q>=8. The original row is A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq), with raw Y_88(8-r,8-q)=p8*z_rq/V_rq. The bound includes the complete forced diagonal, anchor subtraction and c_i^T*x_i for a verified solution B_i*x_i=c_i. Both selected mixed blocks are three-by-three; no invertibility assumption is used. Enumerate every principal minor, solve on the last nonsingular principal subset, fill zeros elsewhere and check the whole range equation.

Let I be L084's 28 selected rows and Z the 43 entrywise-zero-old-block modes (including all 17 empty blocks). Take J=Z union {23,31}; exactly 45 rows, with |I intersect Z|=20 and both added rows outside I union Z. The system retains all I equalities, all J inequalities and 45 signs, including duplicate/zero pullbacks. Its untested complement has 28 modes. This cardinality is a set-union calculation, not a sum of overlapping counts.

Use L084's P,N and selector F and reconstruct G from its complete row transformation. Check E*P=e,E*N=0,F*N=I,F*P=0,G*e=P,G*E+N*F=I, including original/raw augmented forward and reverse identities. Thus z=P+N*h ranges over the full equality locus, h in R^18. Pull all 90 inequalities through this lift. Split h into 18 positive and 18 negative parts; add 90 oriented slacks and 90 artificial coordinates. The initial standard tableau is 90-by-216 with artificial columns beginning at index 126. All equation orientations include their slack sign. Save the full model before pivoting.

Reuse least-index entering and minimum-ratio leaving with least-index basic-coordinate ties, and the unchanged exact Phase-I implementation from L092. No floating proposals or new optimization mechanism is involved. A final witness must be checked in all 28 original/raw equalities, 45 original/raw mode rows and 45 signs, independently of its trace. An infeasibility separator must lift to all 45 original/raw free coordinates with nonnegative inequality weights, free equality weights and a strict contradictory constant. A positive unfinished artificial objective has no feasibility implication.

The independent verifier reconstructs original beta coefficients and bounds from the complete audited affine source blocks, both added principal solves, original/raw lifts and all retained substitutions; it runs no constructor or optimizer. Dedicated critical proof/trace review would remain separate from construction-time certificate verification. Inspect complete relevant arrays programmatically; bounded JSON previews provide only schema guidance.

## Completed bounded attempt

The single run terminates at zero artificial objective after 317 pivots
(recorded finalization 13.55773904104717 seconds). All 1597 source and
1229 constructor checks pass. The independent original/raw verifier
passes 426 checks with no failures, including the explicit manuscript
bounds added on its second invocation; no Phase I restart occurs.
All 28 original/raw equalities vanish. The 45 mode slacks are 14 positive
and 31 zero; 45 moments are 33 positive and 12 zero. Row23=(2,5) has zero
original/raw remainder; row31=(3,4) has normalized remainder in
[153320960,153320961). Both original/raw minimum inequalities equal 0.

Canonical full proof/citations are L094. Full evidence and saved trace
are the `two-mixed-row-*.json` certificates under `scripts/finite-support/`;
`two-mixed-row-bound-summary.json` gives selected complete-field pointers
and concise integer bounds. The source reconstruction's negative L086
regression output concerns its older witness only. No omitted-mode row
at the new witness was tested. Outcome NEGATIVE parks this particular
exclusion diagnostic; it supplies no full-column or RS verdict. The sole
continuation is the separately unapproved conditional critical audit,
recorded REVIEW_REQUIRED. Main boundary remains 955–957.
