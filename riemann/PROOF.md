# Riemann hypothesis: argument overview

Incomplete. [Status](PROGRESS.md), [inputs](DAG.md), full proofs in lemmas/.

## Assembly and unresolved gap

Xi has theta/Fourier-cosine representations and an unconditional paired Hadamard product with summable reciprocal-zero nodes. L030–L032/C032a equate all-degree mixed polynomial positivity with real nodes; this remains unproved.

## Partial results

L466 (Sra v1, Thm 1.3; Platt–Trudgian, Thm 1): D_n(Xi;t)>=0 for n>=0, |t|<=3*10^12-1/2, including central multiplicities/endpoints. Application/height audited; manuscripts unaudited. Signs beyond/effective overlap open.

Finite reciprocal-power signs, degree-two Jensen and H_1/H_2 positivity are certified. Conditional arithmetic certificates exclude nonreal centers through height forty; low indices at unbounded heights remain open.

[Input](foundations/2026-10-quasi-riemann-input.md) qualifies Re(s)>7/8. L531–L534: conditional continuation/margins/orders/selection/Sobolev/heights; L535/L536: Poisson measures. L537–L539 audit conditional induction/initialization: <=40eta+tau+pi and <=11eta+pi_init+epsilon_c, zero Fourier loss. L540 audits max{1,(1+5r)/6} amplification/rows. L541: charges; L546: scalars audited. L547/L548: conditional cusp/reflection/continuation; L548: cubic phase/norm/raw bound (DR imports). L553: marks; L554–L558: rows/quadratic/cubic/sextic/DFT. L549–L552/L541 audit kernel/profile/tails; L552 total replayed. L542–L545: conditional sieves; reciprocity/cubic inputs audited. Other-Gauss/arithmetic/support/witness/fibre-count/tail/uniformity and measure/order/coordinate/accounting/bootstrap/H-import audits remain. Audited L461: conditional ceil(c log(2+|a|)+B_c), c>3/16. L468 gives ceil((3/16+3/sqrt(log log T))log T), T=2+|a|, beyond existential onset; logarithm/rectangle uniformity unaudited. C460b's deeper conditional band audited. Signs/endpoint/initial indices/bounded heights remain open.

Regulator/response and selected-law routes lack realization and regulator-uniform signs. Unaudited L469 obstructs U'+CU>=0 (U=wD_1, positive C^1 w, continuous C) at multiple real zeros; simple zeros remain compatible. Unaudited L470 excludes finite homogeneous polynomial-coefficient linear ODEs for Xi. L471 gives a zero-safe majorant and N(T)=O(T(log T)^3). Audited L483/C483a control d>=100 log log T/log T; sources remain unaudited. Using L485's count-only L2 input, unaudited L486 gives B_{>=delta}/[T(log T)^3]<=C delta^(-1)exp(-delta log T/8) for 1/log T<=delta<=1/8. Coefficient 8 suffices; delta log T->infinity alone is uncertified by this bound. Unaudited L474 gives B_epsilon<=C epsilon^3 T(log T)^3 (0<epsilon<=1); unaudited L476's h=(log T)^(-1/4) truncation error is O(T(log T)^(5/2)). Multiplicities/endpoints remain; complementary and retained masses are uncontrolled.

Audited L477 gives a two-phase residual for the fixed-square L1 defect, error O(T(log T)^(5/2)), norm O(T(log T)^3). L478's termwise certificate fails. Audited L479's divisor sum and L480's I_2 are comparable to T(log T)^8. L479's error is O(T(log T)^6). Interpolation requires I_4=O(T(log T)^18) on unbounded heights, but audited L481 gives I_4>=c T(log T)^24, limiting that certificate to O(T) for all large real T. L482 forces growing degree for global-envelope saturation error 1/8; its length budget permits degree <=3. Unaudited L484 obstructs vanishing Haar L2 error for its real Euler-phase truncation; no height transfer follows. Actual-height weighted approximation, saturation correlation, both defect thresholds, negative-mass saving and all-height signs remain open.

L475's exp(7u)/(7u^4) envelope parks global norms; saving open, specialization unaudited. Unaudited L487's zero-flux quartic collision excludes bounded backward negative-D_1 energy comparison; no Xi realization.

Audited L488/L489 bound the collision domain; C489a/C493a await application audits. L494–L496 give qualified charges and ell>24.18. Audited L497–L499 give corner mass <.999577507 and two-charge margin >.00040166. Audited C499a transfers that margin to the first open N=691004 cell at t=.16836. Imported saddle/base-phase proofs, other cells/times, H1 and zero time remain open.

L472/L473: bounds/realization open (L472 audited). L560: audited log-concavity/sign obstruction. L561 inputs/L562 audited: strict PF256, D1<0 outside strip; Xi transfer open.

Audited L530/L565: moment/CD stops. L564: j<=2 tails <=e^(-8T), [T,2T], T>=1, N=ceil(16(T+1)^2). Audited C567a: no global SOS. L566: top-four limit; audited L568: B_64(1)<0. L569: generic C^2-small remainders can violate the absolute budget at multiple zeros; Xi transfer open.

Audited L513–L516/L519–L522 give conditional dilation/trace limits; L523–L525 remain unaudited. L526/L527's audited increments miss -2. Unaudited L528 gives sup c(h)<147/188<pi/4 for fixed K and real-even unit C_c^infinity(-1,1). Audited L529 excludes bounded [h(A_I),D_per] for h(s)=s/(1+s^2). Sources, trace extension, overlap/remainder, nullvector/trace/nonresonance, S<=P-H+K lambda, Weil identity, family bounds and Xi transfer remain open.

L502–L508 record qualified detector/majorant obstructions; L503/L507/L508 are unaudited. L506's audited stop is envelope-only. H_a bounds, costs and Xi transfer remain open.

C055a's second-level signs for L055's nonreal-zero family pass a source audit.

L571: audited disk-Hardy budget; C571a: audited real-tilt obstruction. Xi norm input open.

L463 reproduces bramble_trace v4 Theorem 1b conditionally: fixed c_0>3/8 gives D_n(Xi;a)>0 for all 2n>=c_0 log(|a|/(2pi)) beyond one onset, without upper cutoff. Section 4.5's logarithm/saddle/arcs are audited; C465a supplies overlap. Negative centers/central multiplicities are included. The external zero-free manuscript remains unaudited; initial signs, endpoint and effective height overlap remain open. C460b has a separate margin.

L464 reproduces Section 4.3: D_p(Xi;t)>0 for t>=2, integer p>=C log^2(t+2), absolute C, including central multiplicities. L467 applies Bellotti–Wong v2 Theorem 1.1 (A=18) to closed unit shells at nonnegative heights. C464a gives p>=154369 log^2(t+2); C464b gives p>=M+(17/2)M_nr U_t. Unaudited C464c replaces M_nr by degree K_t of |gamma-t|<d blocks, retaining M, U_t, equality blocks and K_t=0. Initial signs and improved degree counts remain open; source saddle estimates are unaudited.

L465 independently audits Section 4.2: for ell=log(t/(2pi)) and fixed c_0>1/2, the Hardy/Xi coefficient asymptotics have uniform relative error O(ell^(-1/2)) on c_0 ell<=2p<=ell^3, without a new zero-free premise. C465a audits overlap with L464, giving the unconditional Xi tail D_p>0 for all 2p>=c_0 ell beyond one existential onset, including integer endpoints and central zeros. This reproduces source Theorem 1a; numerical onset, c_0=1/2 and initial signs remain open.

C463a intersects L463's tail with L461's witness range. Beyond L463's onset, a negative witness must have n<=min(ceil(c log(2+|a|)+B_c),ceil((c_0/2)log(|a|/(2pi)))-1). Fixed 3/16<c_0/2<c shortens the range with leading coefficient still above 3/16. Initial signs and effective height overlap remain open.

Under L461, L462's fixed-anchor obstruction for 3/8<eta<1/2, 0<=c<eta/2, B>=0, K<=c log(2+|a|)+B makes the signed tail asymptotic to the full positive anchor. Signs, moving anchors and other witnesses remain open.

## Known traps checked

- Finite signs, narrow strips and computed zero ranges are not all-degree positivity or all-height RH. Strict boundary and pole qualifications of external results remain in force.
- Positive kernels, scalar sums and ordinary Gram matrices do not force the mixed forms' signs; retained countermodels test those generic implications only.
- Algebraic squares cannot be replaced by modulus squares. Contour changes, infinite interchanges, moving-height quantifiers and regulator limits need the exact bounds in their proofs.
- No RH counterexample or complete candidate is claimed. See [starting inputs](foundations/notation-and-inputs.md) for definitions and theorems.

## Historical overview

[Earlier overview](history/2026-10-24-proof-overview-before-compaction.txt).
