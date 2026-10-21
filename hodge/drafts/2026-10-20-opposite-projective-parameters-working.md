# Opposite projective parameters — working checkpoint

2026-10-20. Active pre-existing gate:
`drafts/literature/2026-10-20-opposite-projective-polarization-specialization.md`.
One mathematical specialization; no new source discovery or cross-notebook input.

Main gap: universal primitive rational Hodge realization. Intermediate target:
opposite determinant pullbacks and projective embedding parameters. Downstream
use: later reduced-ring Hilbert-coefficient/normalization-defect comparison.
Continue if the choices depend only on fixed B,Y,D,H and fixed moduli data;
park if unknown image Hilbert data or defect is needed. Independent gaps:
F existence, collision geometry, quantitative usefulness and transport.

The active notebook has extensive prior changes; preserve them. Read the
relevant L071/L118/L120 hypotheses/proofs, L107 only as a comparison, the
ready determinant/source assessments and ATTEMPTS/070,073,078. No ready
source theorem gives numerical very-ample or ample-exponent thresholds.

Calculation in progress: with B=S_1, Y=S_2, t=H^2 and fibre
ch(c)=2-21eta, chi(c)=-17 and chi(c[O_H])=-t. Thus
ch(u_0)=-2-17eta and ch(u_1)=-2H. Relative Todd is 1+2e_2;
u_0 td=-2-21e_2. Rank-two c_1=0 forces ch_3=0, hence
c_1(det Rp_1*(F u_0))=0. The second class is
2 p_1*(tau_D p_2*H)=2D^*(H)=2D(H), retaining the full tensor.
Integral pushforward and K3 Picard injection must be stated explicitly.

Proposed parameter description: fixed projective determinant-O moduli
Mbar, A=L_0 tensor L_1^ell ample for fixed sufficiently large ell,
A^k very ample for fixed k, N=h^0(Mbar,A^k)-1. Restrict the actual
embedding to the original reduced image Z. If nu:B -> Z is finite
birational as in L120, its generic rank is one; the normalization
quotient has support of dimension at most one, so it changes no quadratic
Hilbert coefficient. This should give
  deg(Z)=4 k^2 ell^2 q(DH,DH).
No closed immersion of nu is required. Fixed choices ell,k,N are
ineffective here; H is fixed by L118, not numerically specified. Do not
compute a defect bound in this step. Final canonical proof and scoped
structure validation remain to be written.

Completed: the full calculation and parameter proof are canonical in
`lemmas/L137-opposite-determinant-projective-parameters.md`. All fixed
choices were justified independently of image Hilbert/defect data; no
numerical threshold or defect bound was obtained. An independent critical
audit remains pending. No mathematical script was needed.

Validation completed: `python3 ../scripts/docs/check_structure.py --problem hodge`
passes (138 nodes, 361 edges). Manual mathematical checks retain the
opposite GRR sign via the discriminant formula and the degree-one
Hilbert-leading-coefficient argument; these are not an independent audit.
